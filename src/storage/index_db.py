"""
Cross-session index database.

Maintains a single index.db that tracks all sessions across all skill families,
enabling cross-session search, linking, and discovery. This database is fully
reconstructable from session directories — it is an index, not a source of truth.
"""

import json
import sqlite3
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


# Skill → family mapping
SKILL_FAMILIES = {
    # Tree family (ARAW/UAUA)
    "ar": "tree", "aw": "tree", "araw": "tree", "claim": "tree",
    "decide": "tree", "viability": "tree", "evaluate": "tree",
    "certainty": "tree", "uaua": "tree", "search": "tree",
    "diagnose": "tree",
    # Procedure family
    "stg": "procedure", "dcp": "procedure", "pv": "procedure",
    "ac": "procedure", "fla": "procedure", "pcd": "procedure",
    "to": "procedure", "de": "procedure",
    # Analysis family
    "cba": "analysis", "rca": "analysis", "fia": "analysis",
    "sya": "analysis", "swa": "analysis", "cma": "analysis",
    "ria": "analysis", "er": "analysis", "src": "analysis",
    # Enumeration family
    "se": "enumeration", "dd": "enumeration", "ma": "enumeration",
    "gn": "enumeration", "cls": "enumeration", "poa": "enumeration",
    "gg": "enumeration",
    # Goal family
    "gd": "goal", "gu": "goal", "grf": "goal", "dcm": "goal",
    "gosm": "goal", "wt": "goal",
}


def get_family(skill: str) -> str:
    """Get the skill family for a given skill ID."""
    return SKILL_FAMILIES.get(skill, "other")


class IndexDB:
    """Cross-session index database manager."""

    def __init__(self, db_path: str = "index.db"):
        self.db_path = Path(db_path)
        self.conn = sqlite3.connect(str(self.db_path), check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL")
        self._init_schema()

    def _init_schema(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                dir_path TEXT NOT NULL,
                skill TEXT NOT NULL,
                family TEXT NOT NULL,
                input TEXT NOT NULL,
                depth INTEGER,
                node_count INTEGER,
                created_at TEXT NOT NULL,
                tags JSON DEFAULT '[]'
            );

            CREATE TABLE IF NOT EXISTS session_links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_id TEXT NOT NULL REFERENCES sessions(id),
                target_id TEXT NOT NULL REFERENCES sessions(id),
                link_type TEXT NOT NULL,
                note TEXT,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS session_findings (
                id TEXT PRIMARY KEY,
                session_id TEXT NOT NULL REFERENCES sessions(id),
                code TEXT,
                text TEXT NOT NULL,
                type TEXT,
                severity TEXT
            );

            CREATE INDEX IF NOT EXISTS idx_sessions_skill ON sessions(skill);
            CREATE INDEX IF NOT EXISTS idx_sessions_family ON sessions(family);
            CREATE INDEX IF NOT EXISTS idx_sessions_created ON sessions(created_at);
            CREATE INDEX IF NOT EXISTS idx_findings_session ON session_findings(session_id);
            CREATE INDEX IF NOT EXISTS idx_findings_type ON session_findings(type);
            CREATE INDEX IF NOT EXISTS idx_links_source ON session_links(source_id);
            CREATE INDEX IF NOT EXISTS idx_links_target ON session_links(target_id);
        """)
        self.conn.commit()

    def register_session(
        self,
        session_id: str,
        dir_path: str,
        skill: str,
        input_text: str,
        depth: Optional[int] = None,
        node_count: Optional[int] = None,
        tags: Optional[List[str]] = None,
    ) -> str:
        """Register a session in the index. Returns the session ID."""
        family = get_family(skill)
        self.conn.execute(
            """INSERT OR REPLACE INTO sessions
               (id, dir_path, skill, family, input, depth, node_count, created_at, tags)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                session_id,
                dir_path,
                skill,
                family,
                input_text,
                depth,
                node_count,
                datetime.now().isoformat(),
                json.dumps(tags or []),
            ),
        )
        self.conn.commit()
        return session_id

    def update_session(self, session_id: str, **kwargs):
        """Update session fields (node_count, depth, tags)."""
        allowed = {"node_count", "depth", "tags"}
        updates = {k: v for k, v in kwargs.items() if k in allowed}
        if not updates:
            return
        if "tags" in updates:
            updates["tags"] = json.dumps(updates["tags"])
        set_clause = ", ".join(f"{k} = ?" for k in updates)
        self.conn.execute(
            f"UPDATE sessions SET {set_clause} WHERE id = ?",
            (*updates.values(), session_id),
        )
        self.conn.commit()

    def add_finding(
        self,
        session_id: str,
        text: str,
        finding_type: Optional[str] = None,
        code: Optional[str] = None,
        severity: Optional[str] = None,
    ) -> str:
        """Add a key finding to the index for cross-session search."""
        finding_id = str(uuid.uuid4())[:12]
        self.conn.execute(
            """INSERT INTO session_findings (id, session_id, code, text, type, severity)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (finding_id, session_id, code, text, finding_type, severity),
        )
        self.conn.commit()
        return finding_id

    def add_findings_batch(self, session_id: str, findings: List[Dict[str, Any]]):
        """Add multiple findings at once."""
        for f in findings:
            self.add_finding(
                session_id,
                text=f["text"],
                finding_type=f.get("type"),
                code=f.get("code"),
                severity=f.get("severity"),
            )

    def link_sessions(
        self,
        source_id: str,
        target_id: str,
        link_type: str,
        note: Optional[str] = None,
    ):
        """Link two sessions (follows_up, contradicts, extends, informed_by)."""
        self.conn.execute(
            """INSERT INTO session_links (source_id, target_id, link_type, note, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (source_id, target_id, link_type, note, datetime.now().isoformat()),
        )
        self.conn.commit()

    # ── Query methods ──────────────────────────────────────────

    def list_sessions(
        self,
        skill: Optional[str] = None,
        family: Optional[str] = None,
        limit: int = 50,
    ) -> List[Dict]:
        """List sessions, optionally filtered by skill or family."""
        query = "SELECT * FROM sessions WHERE 1=1"
        params: list = []
        if skill:
            query += " AND skill = ?"
            params.append(skill)
        if family:
            query += " AND family = ?"
            params.append(family)
        query += " ORDER BY created_at DESC LIMIT ?"
        params.append(limit)
        rows = self.conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]

    def search_findings(self, query: str, limit: int = 50) -> List[Dict]:
        """Full-text search across all session findings."""
        rows = self.conn.execute(
            """SELECT f.*, s.skill, s.input, s.created_at as session_date
               FROM session_findings f
               JOIN sessions s ON f.session_id = s.id
               WHERE f.text LIKE ?
               ORDER BY s.created_at DESC
               LIMIT ?""",
            (f"%{query}%", limit),
        ).fetchall()
        return [dict(r) for r in rows]

    def search_sessions(self, query: str, limit: int = 50) -> List[Dict]:
        """Search sessions by input text."""
        rows = self.conn.execute(
            """SELECT * FROM sessions
               WHERE input LIKE ?
               ORDER BY created_at DESC
               LIMIT ?""",
            (f"%{query}%", limit),
        ).fetchall()
        return [dict(r) for r in rows]

    def get_session(self, session_id: str) -> Optional[Dict]:
        """Get a single session by ID."""
        row = self.conn.execute(
            "SELECT * FROM sessions WHERE id = ?", (session_id,)
        ).fetchone()
        return dict(row) if row else None

    def get_session_findings(self, session_id: str) -> List[Dict]:
        """Get all findings for a session."""
        rows = self.conn.execute(
            "SELECT * FROM session_findings WHERE session_id = ?", (session_id,)
        ).fetchall()
        return [dict(r) for r in rows]

    def get_session_links(self, session_id: str) -> List[Dict]:
        """Get all links involving a session."""
        rows = self.conn.execute(
            """SELECT * FROM session_links
               WHERE source_id = ? OR target_id = ?""",
            (session_id, session_id),
        ).fetchall()
        return [dict(r) for r in rows]

    def get_stats(self) -> Dict[str, Any]:
        """Get index statistics."""
        total = self.conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0]
        by_family = dict(
            self.conn.execute(
                "SELECT family, COUNT(*) FROM sessions GROUP BY family"
            ).fetchall()
        )
        by_skill = dict(
            self.conn.execute(
                "SELECT skill, COUNT(*) FROM sessions GROUP BY skill ORDER BY COUNT(*) DESC LIMIT 10"
            ).fetchall()
        )
        findings_count = self.conn.execute(
            "SELECT COUNT(*) FROM session_findings"
        ).fetchone()[0]
        links_count = self.conn.execute(
            "SELECT COUNT(*) FROM session_links"
        ).fetchone()[0]
        return {
            "total_sessions": total,
            "by_family": by_family,
            "top_skills": by_skill,
            "total_findings": findings_count,
            "total_links": links_count,
        }

    # ── Rebuild ────────────────────────────────────────────────

    def rebuild_from_sessions_dir(self, sessions_dir: str):
        """Rebuild the entire index by scanning session directories.

        This makes index.db fully reconstructable — not a single point of failure.
        """
        sessions_path = Path(sessions_dir)
        if not sessions_path.exists():
            print(f"Sessions directory not found: {sessions_dir}")
            return

        # Clear existing data
        self.conn.executescript("""
            DELETE FROM session_findings;
            DELETE FROM session_links;
            DELETE FROM sessions;
        """)

        count = 0
        for session_dir in sorted(sessions_path.iterdir()):
            if not session_dir.is_dir():
                continue

            # Try to read session metadata from tree.db or analysis.json
            meta = self._read_session_meta(session_dir)
            if meta:
                self.register_session(
                    session_id=meta["id"],
                    dir_path=str(session_dir),
                    skill=meta["skill"],
                    input_text=meta["input"],
                    depth=meta.get("depth"),
                    node_count=meta.get("node_count"),
                    tags=meta.get("tags", []),
                )
                # Extract findings if available
                for finding in meta.get("findings", []):
                    self.add_finding(
                        meta["id"],
                        text=finding["text"],
                        finding_type=finding.get("type"),
                        code=finding.get("code"),
                        severity=finding.get("severity"),
                    )
                count += 1

        print(f"Rebuilt index with {count} sessions from {sessions_dir}")

    def _read_session_meta(self, session_dir: Path) -> Optional[Dict]:
        """Read session metadata from a session directory."""
        meta_path = session_dir / "meta.json"
        if meta_path.exists():
            with open(meta_path) as f:
                return json.load(f)

        # Fallback: try tree.db
        tree_db = session_dir / "tree.db"
        if tree_db.exists():
            try:
                conn = sqlite3.connect(str(tree_db))
                conn.row_factory = sqlite3.Row
                meta = {}
                for row in conn.execute("SELECT key, value FROM metadata"):
                    meta[row["key"]] = json.loads(row["value"]) if row["value"] else None
                node_count = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
                max_depth = conn.execute("SELECT MAX(depth) FROM nodes").fetchone()[0]
                conn.close()

                return {
                    "id": meta.get("session_id", str(uuid.uuid4())[:12]),
                    "skill": meta.get("skill", "araw"),
                    "input": meta.get("initial_claim", session_dir.name),
                    "depth": max_depth,
                    "node_count": node_count,
                    "findings": [],
                }
            except Exception:
                pass

        # Fallback: try analysis.json
        analysis_path = session_dir / "analysis.json"
        if analysis_path.exists():
            try:
                with open(analysis_path) as f:
                    data = json.load(f)
                return {
                    "id": data.get("session_id", str(uuid.uuid4())[:12]),
                    "skill": data.get("skill", "unknown"),
                    "input": data.get("input", session_dir.name),
                    "findings": [],
                }
            except Exception:
                pass

        return None

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
