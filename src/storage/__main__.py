"""
CLI interface for the session storage system.

Usage:
    python -m src.storage list [--skill SKILL] [--family FAMILY]
    python -m src.storage search "query text"
    python -m src.storage show SESSION_ID
    python -m src.storage link SOURCE_ID TARGET_ID TYPE [--note "..."]
    python -m src.storage rebuild
    python -m src.storage stats
    python -m src.storage export SESSION_ID
"""

import argparse
import json
import sys
from pathlib import Path

from .session_store import SessionStore


def get_store(args) -> SessionStore:
    sessions_dir = getattr(args, "sessions_dir", None)
    return SessionStore(sessions_dir=sessions_dir)


def cmd_list(args):
    store = get_store(args)
    sessions = store.list_sessions(skill=args.skill, family=args.family, limit=args.limit)
    if not sessions:
        print("No sessions found.")
        return
    for s in sessions:
        date = s["created_at"][:10]
        node_info = f" ({s['node_count']} nodes)" if s.get("node_count") else ""
        tags = json.loads(s.get("tags", "[]"))
        tag_str = f" [{', '.join(tags)}]" if tags else ""
        print(f"  [{date}] {s['skill']:>8}: {s['input'][:60]}{node_info}{tag_str}")
        print(f"           id={s['id']}  family={s['family']}")


def cmd_search(args):
    store = get_store(args)
    results = store.search(args.query)

    sessions = results["sessions"]
    findings = results["findings"]

    if sessions:
        print(f"\n  Sessions matching '{args.query}':")
        for s in sessions[:10]:
            date = s["created_at"][:10]
            print(f"    [{date}] {s['skill']}: {s['input'][:60]}")
            print(f"             id={s['id']}")

    if findings:
        print(f"\n  Findings matching '{args.query}':")
        for f in findings[:20]:
            code = f"[{f['code']}] " if f.get("code") else ""
            print(f"    {code}{f['text'][:70]}")
            print(f"      in: {f['skill']} session ({f['session_date'][:10]})")

    if not sessions and not findings:
        print(f"  No results for '{args.query}'.")


def cmd_show(args):
    store = get_store(args)
    idx = store._get_index()
    session = idx.get_session(args.session_id)
    if not session:
        print(f"Session {args.session_id} not found.")
        idx.close()
        return

    print(f"\n  Session: {session['id']}")
    print(f"  Skill: {session['skill']} (family: {session['family']})")
    print(f"  Input: {session['input']}")
    print(f"  Created: {session['created_at']}")
    print(f"  Path: {session['dir_path']}")
    if session.get("node_count"):
        print(f"  Nodes: {session['node_count']}")
    if session.get("depth"):
        print(f"  Depth: {session['depth']}")

    tags = json.loads(session.get("tags", "[]"))
    if tags:
        print(f"  Tags: {', '.join(tags)}")

    findings = idx.get_session_findings(args.session_id)
    if findings:
        print(f"\n  Findings ({len(findings)}):")
        for f in findings:
            code = f"[{f['code']}] " if f.get("code") else ""
            severity = f" ({f['severity']})" if f.get("severity") else ""
            print(f"    {code}{f['text'][:70]}{severity}")

    links = idx.get_session_links(args.session_id)
    if links:
        print(f"\n  Links ({len(links)}):")
        for link in links:
            direction = "→" if link["source_id"] == args.session_id else "←"
            other = link["target_id"] if link["source_id"] == args.session_id else link["source_id"]
            note = f" ({link['note']})" if link.get("note") else ""
            print(f"    {direction} {link['link_type']} {other}{note}")

    idx.close()


def cmd_link(args):
    store = get_store(args)
    idx = store._get_index()
    idx.link_sessions(args.source_id, args.target_id, args.link_type, note=args.note)
    idx.close()
    print(f"Linked: {args.source_id} --{args.link_type}--> {args.target_id}")


def cmd_rebuild(args):
    store = get_store(args)
    store.rebuild_index()


def cmd_stats(args):
    store = get_store(args)
    idx = store._get_index()
    stats = idx.get_stats()
    idx.close()

    print(f"\n  Session Index Statistics")
    print(f"  {'='*40}")
    print(f"  Total sessions: {stats['total_sessions']}")
    print(f"  Total findings: {stats['total_findings']}")
    print(f"  Total links:    {stats['total_links']}")

    if stats["by_family"]:
        print(f"\n  By family:")
        for family, count in sorted(stats["by_family"].items()):
            print(f"    {family:>12}: {count}")

    if stats["top_skills"]:
        print(f"\n  Top skills:")
        for skill, count in stats["top_skills"].items():
            print(f"    {skill:>12}: {count}")


def cmd_export(args):
    from .export import export_all

    store = get_store(args)
    idx = store._get_index()
    session = idx.get_session(args.session_id)
    idx.close()

    if not session:
        print(f"Session {args.session_id} not found.")
        return

    export_all(session["dir_path"])
    print(f"Exported to {session['dir_path']}/exports/")


def main():
    parser = argparse.ArgumentParser(
        prog="python -m src.storage",
        description="Reasoning Toolkit session storage CLI",
    )
    parser.add_argument(
        "--sessions-dir",
        help="Override sessions directory (default: PROJECT_ROOT/sessions/)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list
    p_list = subparsers.add_parser("list", help="List sessions")
    p_list.add_argument("--skill", help="Filter by skill")
    p_list.add_argument("--family", help="Filter by family")
    p_list.add_argument("--limit", type=int, default=20, help="Max results")

    # search
    p_search = subparsers.add_parser("search", help="Search sessions and findings")
    p_search.add_argument("query", help="Search text")

    # show
    p_show = subparsers.add_parser("show", help="Show session details")
    p_show.add_argument("session_id", help="Session ID")

    # link
    p_link = subparsers.add_parser("link", help="Link two sessions")
    p_link.add_argument("source_id", help="Source session ID")
    p_link.add_argument("target_id", help="Target session ID")
    p_link.add_argument("link_type", help="Link type (follows_up, contradicts, extends, informed_by)")
    p_link.add_argument("--note", help="Optional note")

    # rebuild
    subparsers.add_parser("rebuild", help="Rebuild index from session directories")

    # stats
    subparsers.add_parser("stats", help="Show index statistics")

    # export
    p_export = subparsers.add_parser("export", help="Export session to all formats")
    p_export.add_argument("session_id", help="Session ID")

    args = parser.parse_args()

    commands = {
        "list": cmd_list,
        "search": cmd_search,
        "show": cmd_show,
        "link": cmd_link,
        "rebuild": cmd_rebuild,
        "stats": cmd_stats,
        "export": cmd_export,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
