#!/usr/bin/env python3
"""
ARAW to GOSM Bridge

Exports ARAW findings in GOSM-compatible format for planning integration.

Usage:
    python bridge_to_gosm.py database.db --output assumptions.yaml
    python bridge_to_gosm.py *.db --synthesize --output combined.yaml
"""

import argparse
import json
import sqlite3
import yaml
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime


def connect_db(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_root_claim(conn: sqlite3.Connection) -> str:
    cursor = conn.execute("SELECT claim FROM nodes WHERE depth = 0 LIMIT 1")
    row = cursor.fetchone()
    return row['claim'] if row else "Unknown"


def extract_must_verify(conn: sqlite3.Connection) -> List[Dict]:
    """Extract crux nodes and HIGH impact items that must be verified."""
    items = []

    # Crux nodes
    cursor = conn.execute("""
        SELECT id, claim, leverage_score, content, depth
        FROM nodes
        WHERE content LIKE '%"is_crux": true%'
        ORDER BY leverage_score DESC
    """)
    for row in cursor:
        content = json.loads(row['content']) if row['content'] else {}
        items.append({
            'claim': row['claim'],
            'type': 'crux',
            'leverage': row['leverage_score'] or 0.5,
            'effort': content.get('effort_to_address', 'MEDIUM'),
            'impact': content.get('potential_impact', 'HIGH'),
            'depth': row['depth'],
            'verification_method': 'TBD',
            'pass_criteria': 'TBD',
            'fail_action': 'Re-evaluate downstream assumptions'
        })

    # HIGH impact + LOW effort (DO_FIRST)
    cursor = conn.execute("""
        SELECT id, claim, leverage_score, content, depth
        FROM nodes
        WHERE content LIKE '%"potential_impact": "HIGH"%'
        AND content LIKE '%"effort_to_address": "LOW"%'
        ORDER BY leverage_score DESC
    """)
    for row in cursor:
        content = json.loads(row['content']) if row['content'] else {}
        if not any(i['claim'] == row['claim'] for i in items):  # Avoid duplicates
            items.append({
                'claim': row['claim'],
                'type': 'do_first',
                'leverage': row['leverage_score'] or 0.5,
                'effort': 'LOW',
                'impact': 'HIGH',
                'depth': row['depth'],
                'verification_method': 'TBD',
                'pass_criteria': 'TBD',
                'fail_action': 'TBD'
            })

    return items[:20]  # Limit to top 20


def extract_should_verify(conn: sqlite3.Connection) -> List[Dict]:
    """Extract HIGH impact items for later verification."""
    items = []

    cursor = conn.execute("""
        SELECT id, claim, leverage_score, content, depth
        FROM nodes
        WHERE content LIKE '%"potential_impact": "HIGH"%'
        AND content NOT LIKE '%"is_crux": true%'
        AND content NOT LIKE '%"effort_to_address": "LOW"%'
        ORDER BY leverage_score DESC
        LIMIT 30
    """)
    for row in cursor:
        content = json.loads(row['content']) if row['content'] else {}
        items.append({
            'claim': row['claim'],
            'type': 'high_impact',
            'leverage': row['leverage_score'] or 0.5,
            'effort': content.get('effort_to_address', 'MEDIUM'),
            'impact': 'HIGH',
            'depth': row['depth']
        })

    return items


def extract_frontier(conn: sqlite3.Connection, limit: int = 10) -> List[Dict]:
    """Extract unexplored high-leverage claims."""
    items = []

    cursor = conn.execute("""
        SELECT claim, leverage_score, content, depth
        FROM nodes
        WHERE status = 'unexplored'
        ORDER BY leverage_score DESC
        LIMIT ?
    """, (limit,))

    for row in cursor:
        content = json.loads(row['content']) if row['content'] else {}
        items.append({
            'claim': row['claim'],
            'leverage': row['leverage_score'] or 0.5,
            'effort': content.get('effort_to_address', 'UNKNOWN'),
            'impact': content.get('potential_impact', 'UNKNOWN'),
            'depth': row['depth'],
            'note': 'Unexplored - requires investigation'
        })

    return items


def extract_constraints(conn: sqlite3.Connection) -> List[Dict]:
    """Extract claims that represent constraints on action."""
    constraints = []

    # Look for claims with constraint-like patterns
    cursor = conn.execute("""
        SELECT claim, leverage_score, content
        FROM nodes
        WHERE claim LIKE '%cannot%'
           OR claim LIKE '%must%'
           OR claim LIKE '%required%'
           OR claim LIKE '%necessary%'
           OR claim LIKE '%impossible%'
        ORDER BY leverage_score DESC
        LIMIT 20
    """)

    for row in cursor:
        content = json.loads(row['content']) if row['content'] else {}
        constraints.append({
            'constraint': row['claim'],
            'leverage': row['leverage_score'] or 0.5,
            'impact': content.get('potential_impact', 'MEDIUM')
        })

    return constraints


def generate_gosm_output(db_path: str) -> Dict:
    """Generate GOSM-compatible output from single database."""
    conn = connect_db(db_path)
    root = get_root_claim(conn)

    output = {
        'metadata': {
            'source': Path(db_path).name,
            'root_claim': root,
            'generated': datetime.now().isoformat(),
            'generator': 'araw_to_gosm_bridge'
        },
        'assumptions': {
            'must_verify': extract_must_verify(conn),
            'should_verify': extract_should_verify(conn),
            'frontier': extract_frontier(conn)
        },
        'constraints': extract_constraints(conn),
        'decisions': [],  # Would need synthesis across DBs for tensions
        'out_of_scope': []  # Could extract drifted/pruned nodes
    }

    conn.close()
    return output


def generate_combined_output(db_paths: List[str]) -> Dict:
    """Generate combined GOSM output from multiple databases."""
    all_must_verify = []
    all_should_verify = []
    all_frontier = []
    all_constraints = []
    sources = []

    for db_path in db_paths:
        try:
            conn = connect_db(db_path)
            root = get_root_claim(conn)
            sources.append({
                'file': Path(db_path).name,
                'root': root[:80]
            })

            for item in extract_must_verify(conn):
                item['source'] = Path(db_path).name
                all_must_verify.append(item)

            for item in extract_should_verify(conn):
                item['source'] = Path(db_path).name
                all_should_verify.append(item)

            for item in extract_frontier(conn):
                item['source'] = Path(db_path).name
                all_frontier.append(item)

            for item in extract_constraints(conn):
                item['source'] = Path(db_path).name
                all_constraints.append(item)

            conn.close()
        except Exception as e:
            print(f"Warning: Error processing {db_path}: {e}")

    # Sort by leverage
    all_must_verify.sort(key=lambda x: -x.get('leverage', 0))
    all_should_verify.sort(key=lambda x: -x.get('leverage', 0))
    all_frontier.sort(key=lambda x: -x.get('leverage', 0))

    return {
        'metadata': {
            'sources': sources,
            'generated': datetime.now().isoformat(),
            'generator': 'araw_to_gosm_bridge',
            'mode': 'synthesized'
        },
        'assumptions': {
            'must_verify': all_must_verify[:30],
            'should_verify': all_should_verify[:30],
            'frontier': all_frontier[:20]
        },
        'constraints': all_constraints[:20],
        'decisions': [],
        'out_of_scope': []
    }


def main():
    parser = argparse.ArgumentParser(description="ARAW to GOSM Bridge")
    parser.add_argument("databases", nargs="+", help="ARAW database files")
    parser.add_argument("--output", "-o", type=str, default="gosm_assumptions.yaml",
                        help="Output file (default: gosm_assumptions.yaml)")
    parser.add_argument("--synthesize", "-s", action="store_true",
                        help="Combine multiple databases into single output")
    parser.add_argument("--format", choices=["yaml", "json"], default="yaml",
                        help="Output format (default: yaml)")

    args = parser.parse_args()

    # Filter to existing files
    db_files = [f for f in args.databases if Path(f).exists() and f.endswith('.db')]

    if not db_files:
        print("No valid .db files found")
        return

    print(f"Processing {len(db_files)} database(s)...")

    if args.synthesize or len(db_files) > 1:
        output = generate_combined_output(db_files)
    else:
        output = generate_gosm_output(db_files[0])

    # Write output
    with open(args.output, 'w') as f:
        if args.format == 'yaml':
            yaml.dump(output, f, default_flow_style=False, allow_unicode=True, width=120)
        else:
            json.dump(output, f, indent=2)

    print(f"\nWritten to {args.output}")
    print(f"  Must verify: {len(output['assumptions']['must_verify'])} items")
    print(f"  Should verify: {len(output['assumptions']['should_verify'])} items")
    print(f"  Frontier: {len(output['assumptions']['frontier'])} items")
    print(f"  Constraints: {len(output['constraints'])} items")


if __name__ == "__main__":
    main()
