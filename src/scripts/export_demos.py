#!/usr/bin/env python3
"""Export ARAW databases to static JSON demos for the website viewer."""

import json
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

# Add src to path so we can import the visualizer
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))

from araw.visualize import ARAWVisualizer

DATABASES_DIR = ROOT / "databases" / "araw"
DEMOS_DIR = ROOT / "website" / "public" / "demos"


def get_root_claim(db_path: Path) -> str:
    """Extract the root claim from an ARAW database."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            "SELECT claim FROM nodes WHERE depth = 0 LIMIT 1"
        ).fetchone()
        return row["claim"] if row else "Unknown"
    finally:
        conn.close()


def make_display_name(stem: str) -> str:
    """Convert a filename stem into a human-readable name."""
    return stem.replace("_", " ").replace("-", " ").title()


def export_all():
    """Scan databases/araw/*.db, export each to website/public/demos/."""
    DEMOS_DIR.mkdir(parents=True, exist_ok=True)

    db_files = sorted(DATABASES_DIR.glob("*.db"))
    if not db_files:
        print(f"No .db files found in {DATABASES_DIR}")
        return

    demos = []

    for db_path in db_files:
        stem = db_path.stem
        out_path = DEMOS_DIR / f"{stem}.json"

        print(f"Exporting {db_path.name} -> {out_path.name} ...", end=" ")

        try:
            viz = ARAWVisualizer(str(db_path))
            viz.export_json(str(out_path))

            # Read back stats from the exported JSON
            with open(out_path) as f:
                data = json.load(f)

            stats = data.get("stats", {})
            root_claim = get_root_claim(db_path)

            demos.append({
                "id": stem,
                "name": make_display_name(stem),
                "file": f"{stem}.json",
                "nodes": stats.get("total_nodes", len(data.get("nodes", []))),
                "max_depth": stats.get("max_depth", 0),
                "root_claim": root_claim,
            })

            print(f"OK ({demos[-1]['nodes']} nodes, depth {demos[-1]['max_depth']})")
        except Exception as e:
            print(f"FAILED: {e}")

    # Write manifest
    manifest = {
        "generated": datetime.now().isoformat(),
        "demos": demos,
    }

    manifest_path = DEMOS_DIR / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nManifest written to {manifest_path}")
    print(f"Total: {len(demos)} demo(s) exported")


if __name__ == "__main__":
    export_all()
