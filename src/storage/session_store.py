"""
Session store — creates and manages session directories.

Each skill invocation that produces persistent output gets a session directory:

    sessions/
        2026-01-31_should-i-change-careers/
            tree.db          ← ARAW/UAUA tree (SQLite)
            analysis.json    ← Analysis output (JSON)
            meta.json        ← Session metadata
            exports/
                tree.json    ← Sigma.js export
                tree.gexf    ← Gephi export
                summary.md   ← Human-readable summary
"""

import json
import os
import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from .index_db import IndexDB, get_family


def _slugify(text: str, max_length: int = 60) -> str:
    """Convert input text to a filesystem-safe slug."""
    slug = text.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = slug.strip("-")
    return slug[:max_length].rstrip("-")


class SessionStore:
    """Manages session directories and registration."""

    def __init__(
        self,
        sessions_dir: Optional[str] = None,
        index_db_path: Optional[str] = None,
    ):
        # Default: sessions/ at project root
        if sessions_dir:
            self.sessions_dir = Path(sessions_dir)
        else:
            self.sessions_dir = Path(
                os.environ.get(
                    "REASONINGTOOL_SESSIONS_DIR",
                    Path(__file__).resolve().parents[2] / "sessions",
                )
            )
        self.sessions_dir.mkdir(parents=True, exist_ok=True)

        # Index database
        if index_db_path:
            self._index_path = index_db_path
        else:
            self._index_path = str(self.sessions_dir / "index.db")

    def _get_index(self) -> IndexDB:
        """Get an IndexDB connection. Caller should close when done."""
        return IndexDB(self._index_path)

    def create_session(
        self,
        skill: str,
        input_text: str,
        depth: Optional[int] = None,
        tags: Optional[list] = None,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> "Session":
        """Create a new session directory and register it in the index.

        Returns a Session object with paths and metadata.
        """
        session_id = str(uuid.uuid4())[:12]
        date_str = datetime.now().strftime("%Y-%m-%d")
        slug = _slugify(input_text)
        dir_name = f"{date_str}_{slug}" if slug else date_str

        # Handle naming collisions
        session_dir = self.sessions_dir / dir_name
        counter = 2
        while session_dir.exists():
            session_dir = self.sessions_dir / f"{dir_name}_{counter}"
            counter += 1

        session_dir.mkdir(parents=True)
        (session_dir / "exports").mkdir()

        # Write meta.json
        meta = {
            "id": session_id,
            "skill": skill,
            "family": get_family(skill),
            "input": input_text,
            "depth": depth,
            "parameters": parameters or {},
            "created_at": datetime.now().isoformat(),
            "tags": tags or [],
            "findings": [],
        }
        meta_path = session_dir / "meta.json"
        with open(meta_path, "w") as f:
            json.dump(meta, f, indent=2)

        # Register in index
        index = self._get_index()
        index.register_session(
            session_id=session_id,
            dir_path=str(session_dir),
            skill=skill,
            input_text=input_text,
            depth=depth,
            tags=tags,
        )
        index.close()

        return Session(
            id=session_id,
            skill=skill,
            family=get_family(skill),
            input_text=input_text,
            dir_path=session_dir,
            meta=meta,
            index_db_path=self._index_path,
        )

    def load_session(self, session_id: str) -> Optional["Session"]:
        """Load an existing session by ID from the index."""
        index = self._get_index()
        session_data = index.get_session(session_id)
        index.close()

        if not session_data:
            return None

        session_dir = Path(session_data["dir_path"])
        meta_path = session_dir / "meta.json"

        if meta_path.exists():
            with open(meta_path) as f:
                meta = json.load(f)
        else:
            meta = session_data

        return Session(
            id=session_id,
            skill=session_data["skill"],
            family=session_data["family"],
            input_text=session_data["input"],
            dir_path=session_dir,
            meta=meta,
            index_db_path=self._index_path,
        )

    def list_sessions(self, **kwargs) -> list:
        """List sessions from the index."""
        index = self._get_index()
        result = index.list_sessions(**kwargs)
        index.close()
        return result

    def search(self, query: str) -> list:
        """Search sessions and findings."""
        index = self._get_index()
        sessions = index.search_sessions(query)
        findings = index.search_findings(query)
        index.close()
        return {"sessions": sessions, "findings": findings}

    def rebuild_index(self):
        """Rebuild index.db from session directories."""
        index = self._get_index()
        index.rebuild_from_sessions_dir(str(self.sessions_dir))
        index.close()


class Session:
    """Represents an active session with convenience accessors."""

    def __init__(
        self,
        id: str,
        skill: str,
        family: str,
        input_text: str,
        dir_path: Path,
        meta: Dict,
        index_db_path: str,
    ):
        self.id = id
        self.skill = skill
        self.family = family
        self.input_text = input_text
        self.dir_path = dir_path
        self.meta = meta
        self._index_db_path = index_db_path

    @property
    def tree_db_path(self) -> Path:
        """Path to the SQLite tree database."""
        return self.dir_path / "tree.db"

    @property
    def analysis_json_path(self) -> Path:
        """Path to the analysis JSON output."""
        return self.dir_path / "analysis.json"

    @property
    def meta_path(self) -> Path:
        """Path to the session metadata."""
        return self.dir_path / "meta.json"

    @property
    def exports_dir(self) -> Path:
        """Path to the exports subdirectory."""
        return self.dir_path / "exports"

    def update_meta(self, **kwargs):
        """Update metadata fields and persist to meta.json."""
        self.meta.update(kwargs)
        with open(self.meta_path, "w") as f:
            json.dump(self.meta, f, indent=2)

    def finalize(self, node_count: Optional[int] = None, findings: Optional[list] = None):
        """Finalize a session: update node count, extract findings to index."""
        if node_count is not None:
            self.update_meta(node_count=node_count)

        index = IndexDB(self._index_db_path)
        if node_count is not None:
            index.update_session(self.id, node_count=node_count)

        if findings:
            self.update_meta(findings=findings)
            index.add_findings_batch(self.id, findings)

        index.close()

    def __repr__(self):
        return f"Session(id={self.id!r}, skill={self.skill!r}, input={self.input_text[:40]!r})"
