#!/usr/bin/env python3
"""
Backfill existing session markdown files into the session storage system.

Scans docs/sessions/*.md, creates session directories, and populates index.db.
This is a COPY operation — original files remain untouched.

Usage:
    python scripts/backfill_sessions.py
    python scripts/backfill_sessions.py --sessions-dir /custom/path
    python scripts/backfill_sessions.py --dry-run
"""

import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from storage.session_store import SessionStore
from storage.index_db import get_family


def parse_session_filename(filename: str) -> dict:
    """Extract skill, date, and topic from session filename.

    Expected format: skill_YYYY-MM-DD_topic-slug.md
    """
    stem = Path(filename).stem

    # Try standard format: skill_date_slug
    match = re.match(r"^([a-z_]+)_(\d{4}-\d{2}-\d{2})_(.+)$", stem)
    if match:
        return {
            "skill": match.group(1),
            "date": match.group(2),
            "slug": match.group(3),
        }

    # Try: session_date_slug (legacy)
    match = re.match(r"^session_(\d{4}-\d{2}-\d{2})_(.+)$", stem)
    if match:
        return {
            "skill": "araw",
            "date": match.group(1),
            "slug": match.group(2),
        }

    # Try: just slug (no date)
    return {
        "skill": "unknown",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "slug": stem,
    }


def extract_input_from_md(content: str, slug: str) -> str:
    """Try to extract the original input from the markdown content."""
    # Look for common patterns
    patterns = [
        r'\*\*Input\*\*:\s*"([^"]+)"',
        r'\*\*Input\*\*:\s*(.+?)$',
        r'Root claim:\s*(.+?)$',
        r'# (?:ARAW|UAUA|AR|AW)[^—]*—\s*(.+?)$',
        r'^# (.+?)$',
    ]
    for pattern in patterns:
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            text = match.group(1).strip().strip('"')
            if len(text) > 5 and text.lower() not in ["araw", "uaua", "session"]:
                return text

    # Fallback: use slug
    return slug.replace("-", " ").replace("_", " ")


def extract_depth_from_md(content: str) -> int | None:
    """Try to extract depth from markdown content."""
    match = re.search(r'\*\*Depth\*\*:\s*(\d+)x?', content)
    if match:
        return int(match.group(1))
    return None


def backfill(sessions_dir: str = None, dry_run: bool = False):
    docs_sessions = PROJECT_ROOT / "docs" / "sessions"
    if not docs_sessions.exists():
        print(f"No docs/sessions/ directory found at {docs_sessions}")
        return

    md_files = sorted(docs_sessions.glob("*.md")) + sorted(docs_sessions.glob("*.txt"))
    print(f"Found {len(md_files)} session files to backfill\n")

    if not dry_run:
        store = SessionStore(sessions_dir=sessions_dir)

    imported = 0
    skipped = 0

    for md_file in md_files:
        info = parse_session_filename(md_file.name)
        content = md_file.read_text(errors="replace")
        input_text = extract_input_from_md(content, info["slug"])
        depth = extract_depth_from_md(content)

        skill = info["skill"]
        # Normalize skill names
        if skill == "comparison":
            skill = "araw"
        elif skill == "example":
            skill = "araw"
        elif skill == "session":
            skill = "araw"

        family = get_family(skill)

        if dry_run:
            print(f"  [DRY RUN] {md_file.name}")
            print(f"    skill={skill} family={family} depth={depth}")
            print(f"    input: {input_text[:60]}")
            print()
            imported += 1
            continue

        # Create session
        session = store.create_session(
            skill=skill,
            input_text=input_text,
            depth=depth,
            tags=["backfill", f"original:{md_file.name}"],
        )

        # Copy the original markdown into the session's exports dir
        shutil.copy2(md_file, session.exports_dir / "original.md")

        # Also create summary.md pointing back to original
        summary = f"# {skill.upper()} — {input_text[:80]}\n\n"
        summary += f"**Date**: {info['date']}\n"
        summary += f"**Skill**: {skill}\n"
        summary += f"**Family**: {family}\n"
        if depth:
            summary += f"**Depth**: {depth}\n"
        summary += f"\n**Original file**: `docs/sessions/{md_file.name}`\n"
        (session.exports_dir / "summary.md").write_text(summary)

        print(f"  {md_file.name}")
        print(f"    → {session.dir_path.name} (id={session.id})")
        imported += 1

    print(f"\nBackfill complete: {imported} imported, {skipped} skipped")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Backfill existing sessions into storage system")
    parser.add_argument("--sessions-dir", help="Override sessions directory")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be imported without doing it")
    args = parser.parse_args()

    backfill(sessions_dir=args.sessions_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
