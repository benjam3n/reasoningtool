"""
Assume Right Assume Wrong Search Engine

A recursive branching search for exploring possibility space.
For every claim, branch into ASSUME RIGHT (closed) and ASSUME WRONG (open).
Recurse until hitting foundations or depth limits.

Uses SQLite for scalable storage (handles 100k+ nodes).
"""

import sqlite3
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, asdict
from enum import Enum


class BranchType(Enum):
    ROOT = "root"
    ASSUME_RIGHT = "assume_right"
    ASSUME_WRONG = "assume_wrong"


class NodeStatus(Enum):
    UNEXPLORED = "unexplored"
    EXPLORING = "exploring"
    EXPLORED = "explored"
    PRUNED = "pruned"


@dataclass
class Node:
    id: str
    parent_id: Optional[str]
    claim: str
    branch_type: str
    status: str
    depth: int
    leverage_score: float
    content: Dict[str, Any]
    created_at: str
    explored_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class ARAWEngine:
    """
    Assume Right Assume Wrong Search Engine

    Usage:
        engine = ARAWEngine("my_search.db")
        root_id = engine.create_search("I need $50k for mom's surgery")

        # Branch on a claim
        engine.branch(root_id, "Mom needs surgery")

        # Get unexplored nodes
        unexplored = engine.get_unexplored(max_depth=3)

        # Explore a node
        engine.add_assume_right(node_id, "Proceed with surgery funding")
        engine.add_assume_wrong(node_id, alternatives=["Other treatments", "Different hospital"])

    Session-managed usage:
        engine = ARAWEngine.from_session(skill="araw", input_text="Should I change careers?", depth=4)
        # ... use normally ...
        engine.finalize()  # registers findings in the session index
    """

    def __init__(self, db_path: str = "araw_search.db"):
        self.db_path = Path(db_path)
        self.conn = sqlite3.connect(str(self.db_path), check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._session = None  # Set by from_session()
        self._init_schema()

    @classmethod
    def from_session(cls, skill: str, input_text: str, depth: Optional[int] = None,
                     sessions_dir: Optional[str] = None, tags: Optional[List[str]] = None) -> "ARAWEngine":
        """Create an engine backed by a session directory.

        Creates a session dir, places tree.db inside it, and registers
        in the session index.
        """
        try:
            from ..storage.session_store import SessionStore
        except ImportError:
            from src.storage.session_store import SessionStore

        store = SessionStore(sessions_dir=sessions_dir)
        session = store.create_session(
            skill=skill, input_text=input_text, depth=depth, tags=tags
        )
        engine = cls(str(session.tree_db_path))
        engine._session = session
        return engine

    def _init_schema(self):
        """Initialize database schema"""
        cursor = self.conn.cursor()

        cursor.executescript("""
            -- Main nodes table
            CREATE TABLE IF NOT EXISTS nodes (
                id TEXT PRIMARY KEY,
                parent_id TEXT,
                claim TEXT NOT NULL,
                branch_type TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'unexplored',
                depth INTEGER NOT NULL DEFAULT 0,
                leverage_score REAL DEFAULT 0.0,
                content JSON,
                created_at TEXT NOT NULL,
                explored_at TEXT,
                FOREIGN KEY (parent_id) REFERENCES nodes(id)
            );

            -- Alternatives discovered for assume_wrong branches
            CREATE TABLE IF NOT EXISTS alternatives (
                id TEXT PRIMARY KEY,
                node_id TEXT NOT NULL,
                alternative TEXT NOT NULL,
                explored BOOLEAN DEFAULT FALSE,
                created_at TEXT NOT NULL,
                FOREIGN KEY (node_id) REFERENCES nodes(id)
            );

            -- Metadata for the search
            CREATE TABLE IF NOT EXISTS metadata (
                key TEXT PRIMARY KEY,
                value JSON
            );

            -- Indexes for fast querying
            CREATE INDEX IF NOT EXISTS idx_nodes_status ON nodes(status);
            CREATE INDEX IF NOT EXISTS idx_nodes_depth ON nodes(depth);
            CREATE INDEX IF NOT EXISTS idx_nodes_parent ON nodes(parent_id);
            CREATE INDEX IF NOT EXISTS idx_nodes_branch_type ON nodes(branch_type);
            CREATE INDEX IF NOT EXISTS idx_nodes_leverage ON nodes(leverage_score);
            CREATE INDEX IF NOT EXISTS idx_alternatives_node ON alternatives(node_id);
        """)

        self.conn.commit()

    def _generate_id(self) -> str:
        """Generate a unique node ID"""
        return str(uuid.uuid4())[:8]

    def _now(self) -> str:
        """Get current timestamp"""
        return datetime.now().isoformat()

    # ============================================
    # SEARCH MANAGEMENT
    # ============================================

    def create_search(self, initial_claim: str, metadata: Optional[Dict] = None) -> str:
        """
        Create a new ARAW search with an initial claim.
        Returns the root node ID.
        """
        root_id = self._generate_id()

        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO nodes (id, parent_id, claim, branch_type, status, depth, content, created_at)
            VALUES (?, NULL, ?, ?, ?, 0, ?, ?)
        """, (
            root_id,
            initial_claim,
            BranchType.ROOT.value,
            NodeStatus.UNEXPLORED.value,
            json.dumps(metadata or {}),
            self._now()
        ))

        # Store search metadata
        cursor.execute("""
            INSERT OR REPLACE INTO metadata (key, value)
            VALUES ('root_id', ?), ('initial_claim', ?), ('created_at', ?)
        """, (
            json.dumps(root_id),
            json.dumps(initial_claim),
            json.dumps(self._now())
        ))

        # Store session ID if session-managed
        if self._session:
            cursor.execute(
                "INSERT OR REPLACE INTO metadata (key, value) VALUES ('session_id', ?)",
                (json.dumps(self._session.id),),
            )
            cursor.execute(
                "INSERT OR REPLACE INTO metadata (key, value) VALUES ('skill', ?)",
                (json.dumps(self._session.skill),),
            )

        self.conn.commit()
        return root_id

    def get_root(self) -> Optional[Node]:
        """Get the root node of the search"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM metadata WHERE key = 'root_id'")
        row = cursor.fetchone()
        if row:
            root_id = json.loads(row['value'])
            return self.get_node(root_id)
        return None

    def get_root_claim(self) -> Optional[str]:
        """Get the original root claim (for context anchoring)"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM metadata WHERE key = 'initial_claim'")
        row = cursor.fetchone()
        if row:
            return json.loads(row['value'])
        return None

    # ============================================
    # NODE OPERATIONS
    # ============================================

    def get_node(self, node_id: str) -> Optional[Node]:
        """Get a node by ID"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM nodes WHERE id = ?", (node_id,))
        row = cursor.fetchone()
        if row:
            return Node(
                id=row['id'],
                parent_id=row['parent_id'],
                claim=row['claim'],
                branch_type=row['branch_type'],
                status=row['status'],
                depth=row['depth'],
                leverage_score=row['leverage_score'],
                content=json.loads(row['content']) if row['content'] else {},
                created_at=row['created_at'],
                explored_at=row['explored_at']
            )
        return None

    def add_node(
        self,
        parent_id: str,
        claim: str,
        branch_type: BranchType,
        content: Optional[Dict] = None,
        leverage_score: float = 0.0
    ) -> str:
        """Add a new node as a child of parent"""
        parent = self.get_node(parent_id)
        if not parent:
            raise ValueError(f"Parent node {parent_id} not found")

        node_id = self._generate_id()
        depth = parent.depth + 1

        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO nodes (id, parent_id, claim, branch_type, status, depth, leverage_score, content, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            node_id,
            parent_id,
            claim,
            branch_type.value,
            NodeStatus.UNEXPLORED.value,
            depth,
            leverage_score,
            json.dumps(content or {}),
            self._now()
        ))

        self.conn.commit()
        return node_id

    def update_status(self, node_id: str, status: NodeStatus):
        """Update a node's status"""
        cursor = self.conn.cursor()
        explored_at = self._now() if status == NodeStatus.EXPLORED else None

        cursor.execute("""
            UPDATE nodes SET status = ?, explored_at = COALESCE(?, explored_at)
            WHERE id = ?
        """, (status.value, explored_at, node_id))

        self.conn.commit()

    def update_leverage(self, node_id: str, leverage_score: float):
        """Update a node's leverage score"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE nodes SET leverage_score = ? WHERE id = ?
        """, (leverage_score, node_id))
        self.conn.commit()

    # ============================================
    # BRANCHING (THE CORE ARAW OPERATION)
    # ============================================

    def branch(
        self,
        node_id: str,
        assume_right_claim: str,
        assume_wrong_claim: str,
        alternatives: Optional[List[str]] = None,
        leverage_score: float = 0.5
    ) -> Dict[str, str]:
        """
        Branch a node into ASSUME RIGHT and ASSUME WRONG.
        Returns dict with 'assume_right' and 'assume_wrong' node IDs.
        """
        # Create ASSUME RIGHT branch
        right_id = self.add_node(
            parent_id=node_id,
            claim=assume_right_claim,
            branch_type=BranchType.ASSUME_RIGHT,
            content={"parent_claim": self.get_node(node_id).claim},
            leverage_score=leverage_score
        )

        # Create ASSUME WRONG branch
        wrong_id = self.add_node(
            parent_id=node_id,
            claim=assume_wrong_claim,
            branch_type=BranchType.ASSUME_WRONG,
            content={
                "parent_claim": self.get_node(node_id).claim,
                "alternatives": alternatives or []
            },
            leverage_score=leverage_score
        )

        # Add alternatives if provided
        if alternatives:
            for alt in alternatives:
                self.add_alternative(wrong_id, alt)

        # Mark parent as explored
        self.update_status(node_id, NodeStatus.EXPLORED)

        return {"assume_right": right_id, "assume_wrong": wrong_id}

    def add_assume_right(
        self,
        parent_id: str,
        claim: str,
        content: Optional[Dict] = None
    ) -> str:
        """Add an ASSUME RIGHT child to a node"""
        return self.add_node(
            parent_id=parent_id,
            claim=claim,
            branch_type=BranchType.ASSUME_RIGHT,
            content=content
        )

    def add_assume_wrong(
        self,
        parent_id: str,
        claim: str,
        alternatives: Optional[List[str]] = None,
        content: Optional[Dict] = None
    ) -> str:
        """Add an ASSUME WRONG child to a node with alternatives"""
        node_id = self.add_node(
            parent_id=parent_id,
            claim=claim,
            branch_type=BranchType.ASSUME_WRONG,
            content={**(content or {}), "alternatives": alternatives or []}
        )

        if alternatives:
            for alt in alternatives:
                self.add_alternative(node_id, alt)

        return node_id

    # ============================================
    # ALTERNATIVES
    # ============================================

    def add_alternative(self, node_id: str, alternative: str) -> str:
        """Add an alternative to an ASSUME WRONG node"""
        alt_id = self._generate_id()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO alternatives (id, node_id, alternative, created_at)
            VALUES (?, ?, ?, ?)
        """, (alt_id, node_id, alternative, self._now()))
        self.conn.commit()
        return alt_id

    def get_alternatives(self, node_id: str) -> List[Dict]:
        """Get all alternatives for a node"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM alternatives WHERE node_id = ?
        """, (node_id,))
        return [dict(row) for row in cursor.fetchall()]

    def mark_alternative_explored(self, alt_id: str):
        """Mark an alternative as explored"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE alternatives SET explored = TRUE WHERE id = ?
        """, (alt_id,))
        self.conn.commit()

    # ============================================
    # QUERYING
    # ============================================

    def get_children(self, node_id: str) -> List[Node]:
        """Get all children of a node"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM nodes WHERE parent_id = ?
        """, (node_id,))
        return [self._row_to_node(row) for row in cursor.fetchall()]

    def get_unexplored(
        self,
        max_depth: Optional[int] = None,
        limit: int = 100,
        strategy: str = "balanced"
    ) -> List[Node]:
        """
        Get unexplored nodes using different queue strategies.

        Strategies:
        - "leverage_first": Highest leverage scores first (exploit high-impact claims)
        - "depth_first": Deepest nodes first (find foundations quickly)
        - "breadth_first": Shallowest nodes first (explore breadth)
        - "frontier": Prioritize claims that open new domains (novelty)
        - "balanced": Mix of leverage and depth (default)
        - "random": Random selection (avoid bias)
        """
        cursor = self.conn.cursor()
        depth_filter = "AND depth <= ?" if max_depth is not None else ""
        params = [max_depth, limit] if max_depth is not None else [limit]

        if strategy == "leverage_first":
            # Pure leverage - exploit high-impact claims
            query = f"""
                SELECT * FROM nodes
                WHERE status = 'unexplored' {depth_filter}
                ORDER BY leverage_score DESC, created_at ASC
                LIMIT ?
            """
        elif strategy == "depth_first":
            # Deepest first - find foundations quickly
            query = f"""
                SELECT * FROM nodes
                WHERE status = 'unexplored' {depth_filter}
                ORDER BY depth DESC, leverage_score DESC
                LIMIT ?
            """
        elif strategy == "breadth_first":
            # Shallowest first - explore breadth
            query = f"""
                SELECT * FROM nodes
                WHERE status = 'unexplored' {depth_filter}
                ORDER BY depth ASC, leverage_score DESC
                LIMIT ?
            """
        elif strategy == "frontier":
            # Novelty - claims with fewest siblings (less explored branches)
            query = f"""
                SELECT n.*,
                    (SELECT COUNT(*) FROM nodes WHERE parent_id = n.parent_id) as sibling_count
                FROM nodes n
                WHERE n.status = 'unexplored' {depth_filter.replace('depth', 'n.depth')}
                ORDER BY sibling_count ASC, n.leverage_score DESC
                LIMIT ?
            """
        elif strategy == "random":
            # Random - avoid systematic bias
            query = f"""
                SELECT * FROM nodes
                WHERE status = 'unexplored' {depth_filter}
                ORDER BY RANDOM()
                LIMIT ?
            """
        else:  # "balanced" (default)
            # Balanced: high leverage at moderate depths, with depth tiebreaker
            # Score = leverage * (1 - depth/100) to favor shallower high-leverage
            query = f"""
                SELECT *, (leverage_score * (1.0 - MIN(depth, 50) / 100.0)) as priority
                FROM nodes
                WHERE status = 'unexplored' {depth_filter}
                ORDER BY priority DESC, depth ASC
                LIMIT ?
            """

        cursor.execute(query, tuple(p for p in params if p is not None))
        return [self._row_to_node(row) for row in cursor.fetchall()]

    def get_unexplored_mixed(self, limit: int = 100, max_depth: Optional[int] = None) -> List[Node]:
        """
        Get unexplored nodes using a MIX of strategies for diversity.
        Returns roughly equal parts from different strategies.
        """
        per_strategy = max(1, limit // 4)
        results = []
        seen_ids = set()

        for strategy in ["leverage_first", "depth_first", "frontier", "random"]:
            nodes = self.get_unexplored(
                max_depth=max_depth,
                limit=per_strategy * 2,  # Get extra to account for dedup
                strategy=strategy
            )
            for node in nodes:
                if node.id not in seen_ids and len(results) < limit:
                    results.append(node)
                    seen_ids.add(node.id)

        return results

    def get_high_leverage(self, min_score: float = 0.7, limit: int = 50) -> List[Node]:
        """Get high-leverage nodes (where ASSUME WRONG changes everything)"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM nodes
            WHERE leverage_score >= ?
            ORDER BY leverage_score DESC
            LIMIT ?
        """, (min_score, limit))
        return [self._row_to_node(row) for row in cursor.fetchall()]

    def get_by_depth(self, depth: int) -> List[Node]:
        """Get all nodes at a specific depth"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM nodes WHERE depth = ?
        """, (depth,))
        return [self._row_to_node(row) for row in cursor.fetchall()]

    def get_branch_type(self, branch_type: BranchType) -> List[Node]:
        """Get all nodes of a specific branch type"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM nodes WHERE branch_type = ?
        """, (branch_type.value,))
        return [self._row_to_node(row) for row in cursor.fetchall()]

    def get_path_to_root(self, node_id: str) -> List[Node]:
        """Get the path from a node back to root"""
        path = []
        current = self.get_node(node_id)

        while current:
            path.append(current)
            if current.parent_id:
                current = self.get_node(current.parent_id)
            else:
                break

        return list(reversed(path))

    def _row_to_node(self, row: sqlite3.Row) -> Node:
        """Convert a database row to a Node object"""
        return Node(
            id=row['id'],
            parent_id=row['parent_id'],
            claim=row['claim'],
            branch_type=row['branch_type'],
            status=row['status'],
            depth=row['depth'],
            leverage_score=row['leverage_score'],
            content=json.loads(row['content']) if row['content'] else {},
            created_at=row['created_at'],
            explored_at=row['explored_at']
        )

    # ============================================
    # STATISTICS
    # ============================================

    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the search"""
        cursor = self.conn.cursor()

        stats = {}

        # Total nodes
        cursor.execute("SELECT COUNT(*) as count FROM nodes")
        stats['total_nodes'] = cursor.fetchone()['count']

        # By status
        cursor.execute("""
            SELECT status, COUNT(*) as count FROM nodes GROUP BY status
        """)
        stats['by_status'] = {row['status']: row['count'] for row in cursor.fetchall()}

        # By branch type
        cursor.execute("""
            SELECT branch_type, COUNT(*) as count FROM nodes GROUP BY branch_type
        """)
        stats['by_branch_type'] = {row['branch_type']: row['count'] for row in cursor.fetchall()}

        # By depth
        cursor.execute("""
            SELECT depth, COUNT(*) as count FROM nodes GROUP BY depth ORDER BY depth
        """)
        stats['by_depth'] = {row['depth']: row['count'] for row in cursor.fetchall()}

        # Max depth
        cursor.execute("SELECT MAX(depth) as max_depth FROM nodes")
        stats['max_depth'] = cursor.fetchone()['max_depth']

        # Total alternatives
        cursor.execute("SELECT COUNT(*) as count FROM alternatives")
        stats['total_alternatives'] = cursor.fetchone()['count']

        # Unexplored alternatives
        cursor.execute("SELECT COUNT(*) as count FROM alternatives WHERE explored = FALSE")
        stats['unexplored_alternatives'] = cursor.fetchone()['count']

        return stats

    # ============================================
    # EXPORT
    # ============================================

    def export_tree(self, node_id: Optional[str] = None) -> Dict:
        """Export the tree (or subtree) as a nested dictionary"""
        if node_id is None:
            root = self.get_root()
            if not root:
                return {}
            node_id = root.id

        node = self.get_node(node_id)
        if not node:
            return {}

        result = node.to_dict()
        result['alternatives'] = self.get_alternatives(node_id)

        children = self.get_children(node_id)
        if children:
            result['children'] = [self.export_tree(child.id) for child in children]

        return result

    def export_json(self, filepath: str, node_id: Optional[str] = None):
        """Export tree to JSON file"""
        tree = self.export_tree(node_id)
        with open(filepath, 'w') as f:
            json.dump(tree, f, indent=2)

    def export_flat(self) -> List[Dict]:
        """Export all nodes as a flat list"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM nodes ORDER BY depth, created_at")
        return [dict(row) for row in cursor.fetchall()]

    # ============================================
    # UTILITIES
    # ============================================

    def prune(self, node_id: str):
        """Mark a node and all descendants as pruned"""
        self.update_status(node_id, NodeStatus.PRUNED)
        for child in self.get_children(node_id):
            self.prune(child.id)

    def reset_exploration(self):
        """Reset all nodes to unexplored (except root)"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE nodes SET status = 'unexplored', explored_at = NULL
            WHERE branch_type != 'root'
        """)
        self.conn.commit()

    def finalize(self):
        """Finalize the session: update node count and extract key findings to the index.

        Only does anything if this engine was created via from_session().
        """
        if not self._session:
            return

        stats = self.get_stats()
        findings = self._extract_key_findings()
        self._session.finalize(
            node_count=stats["total_nodes"],
            findings=findings,
        )

    def _extract_key_findings(self) -> List[Dict[str, Any]]:
        """Extract key findings from the tree for indexing.

        Extracts: crux nodes, high-leverage nodes, and grounded nodes.
        """
        findings = []
        cursor = self.conn.cursor()

        # Crux nodes
        cursor.execute(
            "SELECT id, claim, content FROM nodes WHERE json_extract(content, '$.is_crux') = 1"
        )
        for row in cursor.fetchall():
            findings.append({
                "text": row["claim"],
                "type": "crux",
                "code": row["id"],
            })

        # High-leverage nodes (top 10)
        cursor.execute(
            "SELECT id, claim, leverage_score FROM nodes WHERE leverage_score >= 0.8 ORDER BY leverage_score DESC LIMIT 10"
        )
        for row in cursor.fetchall():
            findings.append({
                "text": row["claim"],
                "type": "high_leverage",
                "code": row["id"],
                "severity": f"leverage={row['leverage_score']:.2f}",
            })

        # Grounded nodes (via groundings table if it exists)
        try:
            cursor.execute(
                "SELECT n.id, n.claim FROM nodes n JOIN groundings g ON n.id = g.node_id"
            )
            for row in cursor.fetchall():
                findings.append({
                    "text": row["claim"],
                    "type": "grounded",
                    "code": row["id"],
                })
        except sqlite3.OperationalError:
            pass  # groundings table may not exist

        return findings

    def close(self):
        """Close the database connection"""
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# ============================================
# CONVENIENCE FUNCTIONS
# ============================================

def create_araw_search(claim: str, db_path: str = "araw_search.db") -> ARAWEngine:
    """Create a new ARAW search and return the engine"""
    engine = ARAWEngine(db_path)
    engine.create_search(claim)
    return engine


def load_araw_search(db_path: str) -> ARAWEngine:
    """Load an existing ARAW search"""
    return ARAWEngine(db_path)


# ============================================
# CLI INTERFACE
# ============================================

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python araw_engine.py <command> [args]")
        print("Commands:")
        print("  create <claim> [db_path]  - Create new search")
        print("  stats [db_path]           - Show statistics")
        print("  export [db_path]          - Export to JSON")
        print("  unexplored [db_path]      - List unexplored nodes")
        sys.exit(1)

    command = sys.argv[1]

    if command == "create":
        claim = sys.argv[2] if len(sys.argv) > 2 else "Initial claim"
        db_path = sys.argv[3] if len(sys.argv) > 3 else "araw_search.db"

        engine = ARAWEngine(db_path)
        root_id = engine.create_search(claim)
        print(f"Created search with root ID: {root_id}")
        print(f"Database: {db_path}")
        engine.close()

    elif command == "stats":
        db_path = sys.argv[2] if len(sys.argv) > 2 else "araw_search.db"
        engine = ARAWEngine(db_path)
        stats = engine.get_stats()
        print(json.dumps(stats, indent=2))
        engine.close()

    elif command == "export":
        db_path = sys.argv[2] if len(sys.argv) > 2 else "araw_search.db"
        engine = ARAWEngine(db_path)
        tree = engine.export_tree()
        print(json.dumps(tree, indent=2))
        engine.close()

    elif command == "unexplored":
        db_path = sys.argv[2] if len(sys.argv) > 2 else "araw_search.db"
        engine = ARAWEngine(db_path)
        unexplored = engine.get_unexplored(limit=20)
        for node in unexplored:
            print(f"[{node.id}] depth={node.depth} leverage={node.leverage_score:.2f}: {node.claim[:60]}")
        engine.close()

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
