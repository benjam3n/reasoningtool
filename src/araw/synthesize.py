#!/usr/bin/env python3
"""
Cross-ARAW Synthesis Tool

Analyzes multiple ARAW databases to find:
- Common themes across runs
- High-confidence findings
- Actionable items (HIGH impact + LOW effort)
- Contradictions and tensions
- Gaps and unexplored areas

Usage:
    python synthesize.py *.db
    python synthesize.py --extract-actions *.db
    python synthesize.py --find-tensions *.db
"""

import argparse
import json
import sqlite3
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Tuple, Optional
import re


def connect_db(db_path: str) -> sqlite3.Connection:
    """Connect to ARAW database."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_root_claim(conn: sqlite3.Connection) -> str:
    """Get the root claim of the ARAW tree."""
    cursor = conn.execute("SELECT claim FROM nodes WHERE depth = 0 LIMIT 1")
    row = cursor.fetchone()
    return row['claim'] if row else "Unknown"


def get_all_claims(conn: sqlite3.Connection) -> List[Dict]:
    """Get all claims with their metadata."""
    cursor = conn.execute("""
        SELECT id, claim, depth, leverage_score, content, status
        FROM nodes
        ORDER BY leverage_score DESC
    """)
    results = []
    for row in cursor:
        content = {}
        if row['content']:
            try:
                content = json.loads(row['content'])
            except:
                pass
        results.append({
            'id': row['id'],
            'claim': row['claim'],
            'depth': row['depth'],
            'leverage': row['leverage_score'] or 0.5,
            'content': content,
            'status': row['status'],
            'effort': content.get('effort_to_address', 'MEDIUM'),
            'impact': content.get('potential_impact', 'MEDIUM'),
            'is_crux': content.get('is_crux', False),
            'direct_path': content.get('direct_path', True)
        })
    return results


def extract_actions(claims: List[Dict], db_name: str) -> List[Dict]:
    """Extract actionable items: HIGH impact + LOW effort."""
    actions = []
    for claim in claims:
        # DO FIRST: LOW effort + HIGH impact
        if claim['effort'] == 'LOW' and claim['impact'] == 'HIGH':
            actions.append({
                'priority': 'DO_FIRST',
                'claim': claim['claim'],
                'source': db_name,
                'leverage': claim['leverage'],
                'direct_path': claim['direct_path']
            })
        # DO SECOND: HIGH effort + HIGH impact (if crux)
        elif claim['impact'] == 'HIGH' and claim['is_crux']:
            actions.append({
                'priority': 'DO_SECOND',
                'claim': claim['claim'],
                'source': db_name,
                'leverage': claim['leverage'],
                'direct_path': claim['direct_path']
            })
    return actions


def find_common_themes(all_claims: Dict[str, List[Dict]], threshold: float = 0.3) -> List[Dict]:
    """Find claims that appear across multiple databases (by keyword overlap)."""
    # Simple keyword extraction
    def extract_keywords(text: str) -> set:
        text = text.lower()
        # Remove common words
        stopwords = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been',
                     'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                     'would', 'could', 'should', 'may', 'might', 'must', 'shall',
                     'can', 'need', 'dare', 'ought', 'used', 'to', 'of', 'in',
                     'for', 'on', 'with', 'at', 'by', 'from', 'as', 'into',
                     'through', 'during', 'before', 'after', 'above', 'below',
                     'between', 'under', 'again', 'further', 'then', 'once',
                     'that', 'this', 'these', 'those', 'and', 'but', 'or', 'not'}
        words = set(re.findall(r'\b[a-z]{4,}\b', text))
        return words - stopwords

    # Build keyword index
    keyword_to_claims = defaultdict(list)
    for db_name, claims in all_claims.items():
        for claim in claims:
            keywords = extract_keywords(claim['claim'])
            for kw in keywords:
                keyword_to_claims[kw].append({
                    'claim': claim['claim'],
                    'source': db_name,
                    'leverage': claim['leverage']
                })

    # Find keywords that appear in multiple databases
    cross_db_themes = []
    for kw, claim_list in keyword_to_claims.items():
        sources = set(c['source'] for c in claim_list)
        if len(sources) >= 2:  # Appears in 2+ databases
            cross_db_themes.append({
                'keyword': kw,
                'sources': list(sources),
                'count': len(claim_list),
                'sample_claims': [c['claim'][:100] for c in claim_list[:3]]
            })

    # Sort by how many databases it appears in, then by total count
    cross_db_themes.sort(key=lambda x: (len(x['sources']), x['count']), reverse=True)
    return cross_db_themes[:20]  # Top 20 themes


def find_tensions(all_claims: Dict[str, List[Dict]]) -> List[Dict]:
    """Find potential contradictions or tensions between claims."""
    tensions = []

    # Keywords that often indicate opposing views
    tension_pairs = [
        ('necessary', 'unnecessary'),
        ('required', 'optional'),
        ('always', 'never'),
        ('must', 'should not'),
        ('helps', 'harms'),
        ('increases', 'decreases'),
        ('enables', 'prevents'),
        ('transparency', 'opacity'),
        ('trust', 'distrust'),
        ('centralized', 'decentralized'),
    ]

    all_claim_texts = []
    for db_name, claims in all_claims.items():
        for claim in claims:
            all_claim_texts.append({
                'text': claim['claim'].lower(),
                'source': db_name,
                'full': claim['claim']
            })

    for word1, word2 in tension_pairs:
        claims_with_word1 = [c for c in all_claim_texts if word1 in c['text']]
        claims_with_word2 = [c for c in all_claim_texts if word2 in c['text']]

        if claims_with_word1 and claims_with_word2:
            tensions.append({
                'dimension': f"{word1} vs {word2}",
                'claims_for': [c['full'][:80] for c in claims_with_word1[:2]],
                'claims_against': [c['full'][:80] for c in claims_with_word2[:2]],
                'sources_for': list(set(c['source'] for c in claims_with_word1)),
                'sources_against': list(set(c['source'] for c in claims_with_word2))
            })

    return tensions


def get_frontier(conn: sqlite3.Connection, limit: int = 10) -> List[Dict]:
    """Get highest-leverage unexplored claims."""
    cursor = conn.execute("""
        SELECT claim, leverage_score, depth, content
        FROM nodes
        WHERE status = 'unexplored'
        ORDER BY leverage_score DESC
        LIMIT ?
    """, (limit,))

    results = []
    for row in cursor:
        content = {}
        if row['content']:
            try:
                content = json.loads(row['content'])
            except:
                pass
        results.append({
            'claim': row['claim'],
            'leverage': row['leverage_score'] or 0.5,
            'depth': row['depth'],
            'effort': content.get('effort_to_address', 'MEDIUM'),
            'impact': content.get('potential_impact', 'MEDIUM')
        })
    return results


def summarize_db(db_path: str) -> Dict:
    """Generate summary for a single database."""
    conn = connect_db(db_path)

    root = get_root_claim(conn)
    claims = get_all_claims(conn)

    # Stats
    cursor = conn.execute("SELECT COUNT(*) FROM nodes")
    total = cursor.fetchone()[0]

    cursor = conn.execute("SELECT status, COUNT(*) FROM nodes GROUP BY status")
    by_status = {row['status']: row[1] for row in cursor}

    cursor = conn.execute("SELECT MAX(depth) FROM nodes")
    max_depth = cursor.fetchone()[0] or 0

    # Top findings
    high_leverage = [c for c in claims if c['leverage'] >= 0.8][:5]
    crux_nodes = [c for c in claims if c['is_crux']][:5]
    actions = extract_actions(claims, Path(db_path).name)
    frontier = get_frontier(conn, 5)

    conn.close()

    return {
        'db': Path(db_path).name,
        'root_claim': root,
        'total_nodes': total,
        'by_status': by_status,
        'max_depth': max_depth,
        'high_leverage': high_leverage,
        'crux_nodes': crux_nodes,
        'actions': actions,
        'frontier': frontier
    }


def print_summary(summary: Dict):
    """Print summary for a database."""
    print(f"\n{'='*70}")
    print(f"DATABASE: {summary['db']}")
    print(f"{'='*70}")
    print(f"Root: {summary['root_claim'][:80]}...")
    print(f"Nodes: {summary['total_nodes']} | Max depth: {summary['max_depth']}")
    print(f"Status: {summary['by_status']}")

    if summary['actions']:
        print(f"\n📋 ACTIONABLE ({len(summary['actions'])} items):")
        for action in summary['actions'][:5]:
            print(f"  [{action['priority']}] {action['claim'][:60]}...")

    if summary['crux_nodes']:
        print(f"\n⚡ CRUX NODES ({len(summary['crux_nodes'])} items):")
        for node in summary['crux_nodes'][:3]:
            print(f"  - {node['claim'][:60]}...")

    if summary['frontier']:
        print(f"\n🔭 FRONTIER (unexplored high-leverage):")
        for node in summary['frontier'][:3]:
            print(f"  [{node['leverage']:.2f}] {node['claim'][:55]}...")


def print_synthesis(summaries: List[Dict], themes: List[Dict], tensions: List[Dict]):
    """Print cross-database synthesis."""
    print(f"\n{'#'*70}")
    print(f"# CROSS-ARAW SYNTHESIS")
    print(f"# Analyzing {len(summaries)} databases")
    print(f"{'#'*70}")

    # Aggregate stats
    total_nodes = sum(s['total_nodes'] for s in summaries)
    total_actions = sum(len(s['actions']) for s in summaries)

    print(f"\nTotal nodes across all runs: {total_nodes}")
    print(f"Total actionable items: {total_actions}")

    # Common themes
    if themes:
        print(f"\n{'='*70}")
        print("COMMON THEMES (appear in 2+ databases)")
        print(f"{'='*70}")
        for theme in themes[:10]:
            print(f"\n  [{', '.join(theme['sources'])}] '{theme['keyword']}' ({theme['count']} mentions)")
            for sample in theme['sample_claims'][:2]:
                print(f"    - {sample}...")

    # Tensions
    if tensions:
        print(f"\n{'='*70}")
        print("TENSIONS & CONTRADICTIONS")
        print(f"{'='*70}")
        for tension in tensions[:5]:
            print(f"\n  ⚔️  {tension['dimension']}")
            print(f"      FOR: {tension['claims_for'][0][:50]}...")
            print(f"      AGAINST: {tension['claims_against'][0][:50]}...")

    # All actions consolidated
    all_actions = []
    for s in summaries:
        all_actions.extend(s['actions'])

    if all_actions:
        print(f"\n{'='*70}")
        print("CONSOLIDATED ACTION ITEMS")
        print(f"{'='*70}")

        do_first = [a for a in all_actions if a['priority'] == 'DO_FIRST']
        do_second = [a for a in all_actions if a['priority'] == 'DO_SECOND']

        if do_first:
            print(f"\n🔥 DO FIRST ({len(do_first)} items - LOW effort, HIGH impact):")
            for action in sorted(do_first, key=lambda x: -x['leverage'])[:10]:
                print(f"  [{action['source']}] {action['claim'][:55]}...")

        if do_second:
            print(f"\n📌 DO SECOND ({len(do_second)} items - HIGH impact crux nodes):")
            for action in sorted(do_second, key=lambda x: -x['leverage'])[:10]:
                print(f"  [{action['source']}] {action['claim'][:55]}...")


def export_actions(summaries: List[Dict], output_path: str):
    """Export all actions to JSON file."""
    all_actions = []
    for s in summaries:
        for action in s['actions']:
            all_actions.append({
                'priority': action['priority'],
                'claim': action['claim'],
                'source': action['source'],
                'leverage': action['leverage'],
                'direct_path': action['direct_path']
            })

    # Sort by priority then leverage
    priority_order = {'DO_FIRST': 0, 'DO_SECOND': 1}
    all_actions.sort(key=lambda x: (priority_order.get(x['priority'], 99), -x['leverage']))

    with open(output_path, 'w') as f:
        json.dump(all_actions, f, indent=2)

    print(f"\nExported {len(all_actions)} actions to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Cross-ARAW Synthesis Tool")
    parser.add_argument("databases", nargs="+", help="ARAW database files to analyze")
    parser.add_argument("--extract-actions", type=str, metavar="FILE",
                        help="Export actions to JSON file")
    parser.add_argument("--find-tensions", action="store_true",
                        help="Find contradictions between databases")
    parser.add_argument("--themes-only", action="store_true",
                        help="Only show cross-database themes")

    args = parser.parse_args()

    # Filter to existing .db files
    db_files = [f for f in args.databases if Path(f).exists() and f.endswith('.db')]

    if not db_files:
        print("No valid .db files found")
        return

    print(f"Analyzing {len(db_files)} databases...")

    # Get summaries
    summaries = []
    all_claims = {}

    for db_path in db_files:
        try:
            summary = summarize_db(db_path)
            summaries.append(summary)

            conn = connect_db(db_path)
            all_claims[Path(db_path).name] = get_all_claims(conn)
            conn.close()

            if not args.themes_only:
                print_summary(summary)
        except Exception as e:
            print(f"Error processing {db_path}: {e}")

    # Cross-database analysis
    themes = find_common_themes(all_claims)
    tensions = find_tensions(all_claims) if args.find_tensions else []

    print_synthesis(summaries, themes, tensions)

    # Export if requested
    if args.extract_actions:
        export_actions(summaries, args.extract_actions)


if __name__ == "__main__":
    main()
