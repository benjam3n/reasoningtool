#!/usr/bin/env python3
"""
Markdown to SQLite ARAW Bridge

Converts conversational ARAW sessions (markdown) to SQLite format
for use with synthesize.py and other ARAW tools.

Usage:
    python md_to_sqlite.py session.md              # Creates session.db
    python md_to_sqlite.py session.md -o output.db # Custom output name
    python md_to_sqlite.py sessions/*.md -o all.db # Merge multiple sessions
"""

import argparse
import json
import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple
import yaml


@dataclass
class ParsedNode:
    """A node parsed from markdown ARAW tree"""
    id: int
    parent_id: Optional[int]
    claim: str
    branch_type: str  # 'root', 'assume_right', 'assume_wrong'
    depth: int
    status: str  # 'explored', 'frontier'
    commitment_status: Optional[str]  # 'foundational', 'guess', None
    leverage_score: float


def create_schema(conn: sqlite3.Connection):
    """Create ARAW database schema matching araw_engine.py"""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS nodes (
            id INTEGER PRIMARY KEY,
            parent_id INTEGER,
            claim TEXT NOT NULL,
            branch_type TEXT NOT NULL,
            status TEXT DEFAULT 'explored',
            depth INTEGER DEFAULT 0,
            leverage_score REAL DEFAULT 0.5,
            content TEXT,
            created_at TEXT,
            explored_at TEXT,
            commitment_status TEXT,
            commitment_reason TEXT,
            source_file TEXT,
            FOREIGN KEY (parent_id) REFERENCES nodes(id)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    conn.execute("CREATE INDEX IF NOT EXISTS idx_parent ON nodes(parent_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_depth ON nodes(depth)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_status ON nodes(status)")
    conn.commit()


def parse_frontmatter(content: str) -> Tuple[dict, str]:
    """Extract YAML frontmatter from markdown"""
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    try:
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2]
        # Convert any date objects to strings for JSON serialization
        if frontmatter:
            for key, value in frontmatter.items():
                if hasattr(value, 'isoformat'):
                    frontmatter[key] = value.isoformat()
        return frontmatter or {}, body
    except yaml.YAMLError:
        return {}, content


def extract_root_claim(content: str) -> Optional[str]:
    """Extract the root claim from ARAW markdown"""
    # Look for "Root claim:" or "ROOT:" patterns
    patterns = [
        r'Root claim:\s*(.+?)(?:\n|$)',
        r'ROOT:\s*"?([^"\n]+)"?',
        r'^#+ ARAW[^:]*:\s*(.+?)$',
        r'topic:\s*(.+?)(?:\n|$)',
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.MULTILINE | re.IGNORECASE)
        if match:
            return match.group(1).strip().strip('"')

    return None


def parse_tree_lines(content: str) -> List[Tuple[int, str, str]]:
    """
    Parse tree structure from markdown.
    Returns list of (indent_level, branch_type, claim)
    """
    nodes = []

    # Find code blocks with tree structure
    tree_pattern = r'```[\s\S]*?```'

    for match in re.finditer(tree_pattern, content):
        block = match.group()
        lines = block.split('\n')

        for line in lines:
            # Skip empty lines and code fence markers
            if not line.strip() or line.strip().startswith('```'):
                continue

            # Count leading spaces/tree characters for indent
            stripped = line.lstrip('│├└─ ')
            indent = len(line) - len(line.lstrip())

            # Determine branch type
            branch_type = 'root'
            if 'ASSUME RIGHT' in line.upper() or '→ AR' in line or 'AR →' in line:
                branch_type = 'assume_right'
            elif 'ASSUME WRONG' in line.upper() or '→ AW' in line or 'AW →' in line:
                branch_type = 'assume_wrong'

            # Extract claim text
            claim = stripped
            # Remove common prefixes
            for prefix in ['ASSUME RIGHT →', 'ASSUME WRONG →', 'AR →', 'AW →', '→']:
                if claim.upper().startswith(prefix.upper()):
                    claim = claim[len(prefix):].strip()

            # Skip structural lines
            if claim and not claim.startswith('│') and len(claim) > 3:
                nodes.append((indent // 4, branch_type, claim))

    return nodes


def parse_claims_table(content: str) -> List[Tuple[str, str, str]]:
    """Parse claims from markdown table"""
    claims = []

    # Find claims table
    table_pattern = r'\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|'

    for match in re.finditer(table_pattern, content):
        row = match.group()
        cells = [c.strip() for c in row.split('|')[1:-1]]

        if len(cells) >= 3:
            # Skip header rows
            if cells[0].lower() in ['#', 'claim', 'number']:
                continue
            if '---' in cells[0]:
                continue

            # Extract claim, type, importance
            claim = cells[1] if len(cells) > 1 else ''
            claim_type = cells[2] if len(cells) > 2 else 'explicit'
            importance = cells[3] if len(cells) > 3 else 'MED'

            if claim and len(claim) > 5:
                claims.append((claim.strip('"'), claim_type, importance))

    return claims


def parse_tensions(content: str) -> List[Tuple[str, str, str]]:
    """Parse tensions from synthesis section"""
    tensions = []

    # Look for tension table
    tension_pattern = r'\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|'

    in_tension_section = False
    for line in content.split('\n'):
        if 'tension' in line.lower() and '|' in line:
            in_tension_section = True
            continue

        if in_tension_section and '|' in line:
            match = re.match(tension_pattern, line)
            if match:
                name = match.group(1).strip()
                ar_pos = match.group(2).strip()
                aw_pos = match.group(3).strip()

                # Skip headers
                if name.lower() in ['tension', '---', 'ar position', 'aw position']:
                    continue
                if '---' in name:
                    continue

                tensions.append((name, ar_pos, aw_pos))

    return tensions


def parse_crux_points(content: str) -> List[Tuple[str, str]]:
    """Parse CRUX points from markdown"""
    crux_points = []

    # Pattern for CRUX sections
    crux_pattern = r'###\s*CRUX\s*\d*[:\s]*([^\n]+)[\s\S]*?(?=###|$)'

    for match in re.finditer(crux_pattern, content, re.IGNORECASE):
        title = match.group(1).strip()
        body = match.group(0)

        # Extract the question
        question_match = re.search(r'\*\*The question\*\*:\s*([^\n]+)', body)
        question = question_match.group(1) if question_match else title

        crux_points.append((title, question))

    return crux_points


def parse_commitment_status(content: str) -> List[Tuple[str, str]]:
    """Parse commitment status markers"""
    statuses = []

    # Look for [FOUNDATIONAL] and [GUESS] markers
    foundational_pattern = r'\[FOUNDATIONAL\][:\s]*([^\n\[]+)'
    guess_pattern = r'\[GUESS\][:\s]*([^\n\[]+)'

    for match in re.finditer(foundational_pattern, content):
        statuses.append(('foundational', match.group(1).strip()))

    for match in re.finditer(guess_pattern, content):
        statuses.append(('guess', match.group(1).strip()))

    return statuses


def build_nodes_from_parsed(
    root_claim: str,
    tree_nodes: List[Tuple[int, str, str]],
    claims: List[Tuple[str, str, str]],
    commitment_statuses: List[Tuple[str, str]],
    source_file: str
) -> List[ParsedNode]:
    """Build node list from parsed data"""
    nodes = []
    node_id = 1

    # Create root node
    nodes.append(ParsedNode(
        id=node_id,
        parent_id=None,
        claim=root_claim,
        branch_type='root',
        depth=0,
        status='explored',
        commitment_status=None,
        leverage_score=1.0
    ))
    node_id += 1

    # Add claims as depth-1 nodes
    for claim, claim_type, importance in claims:
        leverage = 0.9 if importance == 'HIGH' else 0.5 if importance == 'MED' else 0.3

        # Check commitment status
        commit_status = None
        for status, text in commitment_statuses:
            if claim.lower() in text.lower() or text.lower() in claim.lower():
                commit_status = status
                break

        nodes.append(ParsedNode(
            id=node_id,
            parent_id=1,  # Link to root
            claim=claim,
            branch_type='assume_right',  # Claims start as AR
            depth=1,
            status='explored',
            commitment_status=commit_status,
            leverage_score=leverage
        ))
        node_id += 1

    # Add tree nodes with parent tracking
    parent_stack = [(0, 1)]  # (indent, node_id)

    for indent, branch_type, claim in tree_nodes:
        # Find parent
        while parent_stack and parent_stack[-1][0] >= indent:
            parent_stack.pop()

        parent_id = parent_stack[-1][1] if parent_stack else 1

        # Check commitment status
        commit_status = None
        for status, text in commitment_statuses:
            if claim.lower() in text.lower() or text.lower() in claim.lower():
                commit_status = status
                break

        nodes.append(ParsedNode(
            id=node_id,
            parent_id=parent_id,
            claim=claim,
            branch_type=branch_type,
            depth=len(parent_stack),
            status='explored',
            commitment_status=commit_status,
            leverage_score=0.5
        ))

        parent_stack.append((indent, node_id))
        node_id += 1

    return nodes


def insert_nodes(conn: sqlite3.Connection, nodes: List[ParsedNode], source_file: str):
    """Insert parsed nodes into database"""
    now = datetime.now().isoformat()

    for node in nodes:
        content = json.dumps({
            'source': 'markdown_import',
            'source_file': source_file
        })

        conn.execute("""
            INSERT INTO nodes (
                id, parent_id, claim, branch_type, status, depth,
                leverage_score, content, created_at, explored_at,
                commitment_status, source_file
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            node.id, node.parent_id, node.claim, node.branch_type,
            node.status, node.depth, node.leverage_score, content,
            now, now, node.commitment_status, source_file
        ))

    conn.commit()


def convert_markdown_to_sqlite(md_path: Path, db_path: Path, append: bool = False):
    """Convert a markdown ARAW session to SQLite"""
    print(f"Processing: {md_path}")

    # Read markdown
    content = md_path.read_text()

    # Parse frontmatter
    frontmatter, body = parse_frontmatter(content)

    # Extract components
    root_claim = extract_root_claim(content) or frontmatter.get('topic', 'Unknown topic')
    tree_nodes = parse_tree_lines(content)
    claims = parse_claims_table(content)
    tensions = parse_tensions(content)
    crux_points = parse_crux_points(content)
    commitment_statuses = parse_commitment_status(content)

    print(f"  Root claim: {root_claim[:50]}...")
    print(f"  Found: {len(claims)} claims, {len(tree_nodes)} tree nodes")
    print(f"  Found: {len(tensions)} tensions, {len(crux_points)} CRUX points")
    print(f"  Found: {len(commitment_statuses)} commitment markers")

    # Build nodes
    nodes = build_nodes_from_parsed(
        root_claim, tree_nodes, claims, commitment_statuses, str(md_path)
    )

    # Create/open database
    if not append and db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    create_schema(conn)

    # Get ID offset for appending
    if append:
        cursor = conn.execute("SELECT MAX(id) FROM nodes")
        max_id = cursor.fetchone()[0] or 0
        for node in nodes:
            node.id += max_id
            if node.parent_id:
                node.parent_id += max_id

    # Insert nodes
    insert_nodes(conn, nodes, str(md_path))

    # Store metadata
    conn.execute(
        "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
        ('source_files', json.dumps([str(md_path)]))
    )
    conn.execute(
        "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
        ('frontmatter', json.dumps(frontmatter))
    )
    conn.execute(
        "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
        ('tensions', json.dumps(tensions))
    )
    conn.execute(
        "INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)",
        ('crux_points', json.dumps(crux_points))
    )
    conn.commit()

    print(f"  Created {len(nodes)} nodes in {db_path}")

    conn.close()
    return len(nodes)


def main():
    parser = argparse.ArgumentParser(
        description="Convert markdown ARAW sessions to SQLite"
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="Markdown file(s) to convert"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output database path (default: same name as input with .db)"
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge multiple files into single database"
    )
    args = parser.parse_args()

    files = [Path(f) for f in args.files]

    if args.merge and args.output:
        # Merge all into one database
        db_path = Path(args.output)
        total_nodes = 0

        for i, md_path in enumerate(files):
            if not md_path.exists():
                print(f"Warning: {md_path} not found, skipping")
                continue

            nodes = convert_markdown_to_sqlite(
                md_path, db_path, append=(i > 0)
            )
            total_nodes += nodes

        print(f"\nMerged {len(files)} files into {db_path}")
        print(f"Total nodes: {total_nodes}")

    else:
        # Convert each file separately
        for md_path in files:
            if not md_path.exists():
                print(f"Warning: {md_path} not found, skipping")
                continue

            if args.output:
                db_path = Path(args.output)
            else:
                db_path = md_path.with_suffix('.db')

            convert_markdown_to_sqlite(md_path, db_path)

    print("\nDone!")


if __name__ == "__main__":
    main()
