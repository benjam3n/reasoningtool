"""
Export utilities for session data.

Provides JSON, GEXF, and Markdown export from session tree databases.
These are convenience wrappers that write to a session's exports/ directory.
"""

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


def export_tree_json(tree_db_path: str, output_path: str, **kwargs) -> Path:
    """Export a tree.db to JSON (Sigma.js/D3.js format).

    Delegates to the existing ARAWVisualizer for full feature support.
    """
    # Import here to avoid circular dependency with visualize.py
    import sys
    araw_dir = str(Path(__file__).resolve().parents[1] / "araw")
    if araw_dir not in sys.path:
        sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from araw.visualize import ARAWVisualizer

    viz = ARAWVisualizer(tree_db_path)
    viz.export_json(output_path, **kwargs)
    return Path(output_path)


def export_tree_gexf(tree_db_path: str, output_path: str, **kwargs) -> Path:
    """Export a tree.db to GEXF (Gephi format)."""
    import sys
    araw_dir = str(Path(__file__).resolve().parents[1] / "araw")
    if araw_dir not in sys.path:
        sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from araw.visualize import ARAWVisualizer

    viz = ARAWVisualizer(tree_db_path)
    viz.export_gexf(output_path, **kwargs)
    return Path(output_path)


def export_session_summary(session_dir: str, output_path: Optional[str] = None) -> str:
    """Generate a Markdown summary from a session directory.

    Reads from meta.json + tree.db or analysis.json.
    Returns the markdown string and optionally writes to file.
    """
    session_path = Path(session_dir)
    meta_path = session_path / "meta.json"

    if not meta_path.exists():
        raise FileNotFoundError(f"No meta.json found in {session_dir}")

    with open(meta_path) as f:
        meta = json.load(f)

    lines = [
        f"# Session: {meta.get('skill', 'unknown')} — {meta.get('input', 'no input')[:80]}",
        "",
        f"**Date**: {meta.get('created_at', 'unknown')[:10]}",
        f"**Skill**: {meta.get('skill', 'unknown')}",
        f"**Family**: {meta.get('family', 'unknown')}",
    ]

    if meta.get("depth"):
        lines.append(f"**Depth**: {meta['depth']}")
    if meta.get("node_count"):
        lines.append(f"**Nodes**: {meta['node_count']}")
    if meta.get("tags"):
        lines.append(f"**Tags**: {', '.join(meta['tags'])}")

    lines.append("")

    # Add findings if present
    findings = meta.get("findings", [])
    if findings:
        lines.append("## Key Findings")
        lines.append("")
        for f in findings:
            code = f"[{f['code']}] " if f.get("code") else ""
            severity = f" ({f['severity']})" if f.get("severity") else ""
            lines.append(f"- {code}{f['text']}{severity}")
        lines.append("")

    # Add tree stats if tree.db exists
    tree_db = session_path / "tree.db"
    if tree_db.exists():
        try:
            conn = sqlite3.connect(str(tree_db))
            node_count = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
            max_depth = conn.execute("SELECT MAX(depth) FROM nodes").fetchone()[0]
            by_branch = dict(
                conn.execute(
                    "SELECT branch_type, COUNT(*) FROM nodes GROUP BY branch_type"
                ).fetchall()
            )
            conn.close()

            lines.append("## Tree Statistics")
            lines.append("")
            lines.append(f"- Total nodes: {node_count}")
            lines.append(f"- Max depth: {max_depth}")
            for bt, count in by_branch.items():
                lines.append(f"- {bt}: {count}")
            lines.append("")
        except Exception:
            pass

    # Add analysis summary if analysis.json exists
    analysis_path = session_path / "analysis.json"
    if analysis_path.exists():
        try:
            with open(analysis_path) as f:
                analysis = json.load(f)
            lines.append("## Analysis Output")
            lines.append("")
            lines.append(f"- Skill: {analysis.get('skill', 'unknown')}")
            output = analysis.get("output", {})
            if isinstance(output, dict):
                for key in list(output.keys())[:5]:
                    val = output[key]
                    if isinstance(val, (str, int, float)):
                        lines.append(f"- {key}: {val}")
                    elif isinstance(val, list):
                        lines.append(f"- {key}: {len(val)} items")
            lines.append("")
        except Exception:
            pass

    md = "\n".join(lines)

    if output_path:
        Path(output_path).write_text(md)

    return md


def export_all(session_dir: str):
    """Export all formats for a session to its exports/ directory."""
    session_path = Path(session_dir)
    exports = session_path / "exports"
    exports.mkdir(exist_ok=True)

    # Summary markdown
    export_session_summary(session_dir, str(exports / "summary.md"))

    # Tree exports
    tree_db = session_path / "tree.db"
    if tree_db.exists():
        try:
            export_tree_json(str(tree_db), str(exports / "tree.json"))
        except Exception as e:
            print(f"Warning: JSON export failed: {e}")
        try:
            export_tree_gexf(str(tree_db), str(exports / "tree.gexf"))
        except Exception as e:
            print(f"Warning: GEXF export failed: {e}")
