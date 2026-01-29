"""
ARAW Context Loader

Shared infrastructure for injecting external context into ARAW sessions.
Supports two use cases:
  1. Library seeding: Load relevant guesses from guess_libraries
  2. Resumable sessions: Load summary of previous ARAW session

Both use the same mechanism: inject pre-existing nodes/context at session start.
"""

import json
import sqlite3
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any


@dataclass
class ContextNode:
    """A node to inject into an ARAW session"""
    claim: str
    branch_type: str  # 'assume_right', 'assume_wrong', 'root', 'context'
    parent_claim: Optional[str]  # None for root-level injection
    source: str  # 'library:filename' or 'session:filename'
    metadata: Dict[str, Any]
    leverage_score: float = 0.5


@dataclass
class ContextBlock:
    """A block of context to inject at session start"""
    nodes: List[ContextNode]
    summary: str  # Human-readable summary of what's being injected
    source_type: str  # 'library' or 'session'
    source_path: str
    injected_at: Optional[str] = None


class ContextSource(ABC):
    """Abstract base class for context sources"""

    @abstractmethod
    def load(self, query: str) -> ContextBlock:
        """Load context relevant to the query"""
        pass

    @abstractmethod
    def matches(self, query: str) -> float:
        """Return relevance score 0-1 for this source vs query"""
        pass


class LibrarySource(ContextSource):
    """Load context from guess_libraries"""

    def __init__(self, library_dir: Path):
        self.library_dir = Path(library_dir)
        self._index = None

    def _build_index(self):
        """Build keyword index of libraries"""
        if self._index is not None:
            return

        self._index = {}
        for lib_file in self.library_dir.glob("**/*.md"):
            content = lib_file.read_text()
            # Extract keywords from frontmatter and content
            keywords = self._extract_keywords(content)
            self._index[lib_file] = {
                'keywords': keywords,
                'content': content
            }

    def _extract_keywords(self, content: str) -> List[str]:
        """Extract relevant keywords from library content"""
        import re
        # Simple keyword extraction - could be made smarter
        words = re.findall(r'\b[a-z]{4,}\b', content.lower())
        # Count frequency, keep top words
        from collections import Counter
        return [w for w, _ in Counter(words).most_common(50)]

    def matches(self, query: str) -> float:
        """Return relevance score based on keyword overlap"""
        self._build_index()
        query_words = set(query.lower().split())

        best_score = 0.0
        for lib_file, data in self._index.items():
            keywords = set(data['keywords'])
            overlap = len(query_words & keywords)
            score = overlap / (len(query_words) + 1)  # +1 to avoid div by zero
            best_score = max(best_score, score)

        return best_score

    def load(self, query: str) -> ContextBlock:
        """Load most relevant library as context"""
        self._build_index()
        query_words = set(query.lower().split())

        best_file = None
        best_score = 0.0

        for lib_file, data in self._index.items():
            keywords = set(data['keywords'])
            overlap = len(query_words & keywords)
            score = overlap / (len(query_words) + 1)
            if score > best_score:
                best_score = score
                best_file = lib_file

        if best_file is None:
            return ContextBlock(
                nodes=[],
                summary="No matching library found",
                source_type='library',
                source_path='none'
            )

        # Parse library into context nodes
        nodes = self._parse_library(best_file)

        return ContextBlock(
            nodes=nodes,
            summary=f"Loaded {len(nodes)} guesses from {best_file.name}",
            source_type='library',
            source_path=str(best_file)
        )

    def _parse_library(self, lib_file: Path) -> List[ContextNode]:
        """Parse markdown library into context nodes"""
        import re
        content = lib_file.read_text()
        nodes = []

        # Find all guess entries (lines starting with - or *)
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('- ') or line.startswith('* '):
                claim = line[2:].strip()
                if len(claim) > 10:  # Skip very short lines
                    nodes.append(ContextNode(
                        claim=claim,
                        branch_type='context',
                        parent_claim=None,
                        source=f'library:{lib_file.name}',
                        metadata={'library': lib_file.name}
                    ))

        return nodes


class SessionSource(ContextSource):
    """Load context from previous ARAW sessions"""

    def __init__(self, sessions_dir: Path):
        self.sessions_dir = Path(sessions_dir)

    def matches(self, query: str) -> float:
        """Check if query explicitly mentions resuming"""
        resume_keywords = ['continue', 'resume', 'pick up', 'where we left']
        query_lower = query.lower()
        for kw in resume_keywords:
            if kw in query_lower:
                return 0.9
        return 0.0

    def load(self, query: str) -> ContextBlock:
        """Load most recent matching session"""
        # Find most recent session matching query keywords
        session_files = sorted(
            self.sessions_dir.glob("*.md"),
            key=lambda f: f.stat().st_mtime,
            reverse=True
        )

        query_words = set(query.lower().split())

        for session_file in session_files[:10]:  # Check recent sessions
            content = session_file.read_text()
            content_words = set(content.lower().split())
            overlap = len(query_words & content_words)

            if overlap >= 2:  # At least 2 matching words
                nodes = self._parse_session(session_file, content)
                return ContextBlock(
                    nodes=nodes,
                    summary=f"Resuming from {session_file.name}",
                    source_type='session',
                    source_path=str(session_file)
                )

        return ContextBlock(
            nodes=[],
            summary="No matching previous session found",
            source_type='session',
            source_path='none'
        )

    def _parse_session(self, session_file: Path, content: str) -> List[ContextNode]:
        """Parse session markdown into context nodes"""
        import re
        nodes = []

        # Extract claims from the session
        # Look for patterns like "CLAIM N:" or numbered lists
        claim_pattern = r'(?:CLAIM \d+|Claim \d+|^\d+\.)[:.]?\s*"?([^"\n]+)"?'

        for match in re.finditer(claim_pattern, content, re.MULTILINE):
            claim = match.group(1).strip()
            if len(claim) > 10:
                nodes.append(ContextNode(
                    claim=claim,
                    branch_type='context',
                    parent_claim=None,
                    source=f'session:{session_file.name}',
                    metadata={'session': session_file.name}
                ))

        # Also extract CRUX points
        crux_pattern = r'CRUX.*?:\s*([^\n]+)'
        for match in re.finditer(crux_pattern, content):
            crux = match.group(1).strip()
            if len(crux) > 10:
                nodes.append(ContextNode(
                    claim=f"CRUX: {crux}",
                    branch_type='context',
                    parent_claim=None,
                    source=f'session:{session_file.name}',
                    metadata={'type': 'crux', 'session': session_file.name}
                ))

        # Extract DO_FIRST actions
        action_pattern = r'DO_FIRST.*?:\s*([^\n]+)'
        for match in re.finditer(action_pattern, content):
            action = match.group(1).strip()
            if len(action) > 10:
                nodes.append(ContextNode(
                    claim=f"ACTION: {action}",
                    branch_type='context',
                    parent_claim=None,
                    source=f'session:{session_file.name}',
                    metadata={'type': 'action', 'session': session_file.name}
                ))

        return nodes


class ContextLoader:
    """
    Main entry point for loading context into ARAW sessions.

    Usage:
        loader = ContextLoader(library_dir, sessions_dir)
        context = loader.load("I need to make money")
        # context.nodes contains ContextNodes to inject
        # context.summary describes what was loaded
    """

    def __init__(
        self,
        library_dir: Optional[Path] = None,
        sessions_dir: Optional[Path] = None
    ):
        self.sources: List[ContextSource] = []

        if library_dir:
            self.sources.append(LibrarySource(Path(library_dir)))
        if sessions_dir:
            self.sources.append(SessionSource(Path(sessions_dir)))

    def load(self, query: str) -> ContextBlock:
        """
        Load context relevant to the query.

        Automatically determines whether to use library or session based on:
        1. Explicit resume keywords -> SessionSource
        2. Keyword matching -> LibrarySource
        """
        best_source = None
        best_score = 0.0

        for source in self.sources:
            score = source.matches(query)
            if score > best_score:
                best_score = score
                best_source = source

        if best_source is None or best_score < 0.1:
            return ContextBlock(
                nodes=[],
                summary="No relevant context found",
                source_type='none',
                source_path='none'
            )

        context = best_source.load(query)
        context.injected_at = datetime.now().isoformat()
        return context

    def inject_into_db(self, context: ContextBlock, db_path: Path, parent_id: int = 1):
        """
        Inject context nodes into an ARAW database.

        Creates nodes linked to the specified parent (usually root).
        """
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get max ID
        cursor.execute("SELECT MAX(id) FROM nodes")
        max_id = cursor.fetchone()[0] or 0

        now = datetime.now().isoformat()

        for i, node in enumerate(context.nodes):
            node_id = max_id + i + 1

            conn.execute("""
                INSERT INTO nodes (
                    id, parent_id, claim, branch_type, status, depth,
                    leverage_score, content, created_at, source_file
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                node_id,
                parent_id,
                node.claim,
                node.branch_type,
                'explored',  # Context nodes start as explored
                1,  # Depth 1 (children of root)
                node.leverage_score,
                json.dumps(node.metadata),
                now,
                node.source
            ))

        # Record injection in metadata
        conn.execute(
            "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
            ('context_injection', json.dumps({
                'summary': context.summary,
                'source_type': context.source_type,
                'source_path': context.source_path,
                'injected_at': context.injected_at,
                'node_count': len(context.nodes)
            }))
        )

        conn.commit()
        conn.close()

        return len(context.nodes)


def main():
    """CLI for testing context loading"""
    import argparse

    parser = argparse.ArgumentParser(description="ARAW Context Loader")
    parser.add_argument("query", help="Query to find relevant context for")
    parser.add_argument(
        "--library-dir",
        default="/home/ben/Documents/projects/GOSM/data/guess_libraries",
        help="Directory containing guess libraries"
    )
    parser.add_argument(
        "--sessions-dir",
        default="/home/ben/Documents/projects/GOSM/library/araw/sessions",
        help="Directory containing ARAW sessions"
    )
    parser.add_argument(
        "--inject",
        metavar="DB",
        help="Inject context into specified database"
    )

    args = parser.parse_args()

    loader = ContextLoader(
        library_dir=Path(args.library_dir),
        sessions_dir=Path(args.sessions_dir)
    )

    context = loader.load(args.query)

    print(f"Source type: {context.source_type}")
    print(f"Source path: {context.source_path}")
    print(f"Summary: {context.summary}")
    print(f"Nodes loaded: {len(context.nodes)}")

    if context.nodes:
        print("\nSample nodes:")
        for node in context.nodes[:5]:
            print(f"  - {node.claim[:80]}...")

    if args.inject:
        count = loader.inject_into_db(context, Path(args.inject))
        print(f"\nInjected {count} nodes into {args.inject}")


if __name__ == "__main__":
    main()
