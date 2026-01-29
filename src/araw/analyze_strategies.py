"""
Analyze which queue strategies discovered the best nodes.

Usage:
    python analyze_strategies.py araw_llm.db
"""

import json
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path


def analyze(db_path: str):
    """Analyze strategy effectiveness from a database"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    # Get all nodes with their content
    cursor.execute("SELECT * FROM nodes WHERE content IS NOT NULL")
    rows = cursor.fetchall()

    # Collect stats per strategy
    stats = defaultdict(lambda: {
        "count": 0,
        "depths": [],
        "leverages": [],
        "foundational": 0,
        "branch_types": defaultdict(int),
    })

    no_strategy = 0

    for row in rows:
        content = json.loads(row["content"]) if row["content"] else {}
        strategy = content.get("discovered_by_strategy")

        if not strategy:
            no_strategy += 1
            continue

        s = stats[strategy]
        s["count"] += 1
        s["depths"].append(row["depth"])
        s["leverages"].append(row["leverage_score"])
        s["branch_types"][row["branch_type"]] += 1

        if row["status"] == "pruned":
            s["foundational"] += 1

    print("=" * 70)
    print("STRATEGY ANALYSIS")
    print("=" * 70)
    print(f"Database: {db_path}")
    print(f"Nodes with strategy tag: {sum(s['count'] for s in stats.values())}")
    print(f"Nodes without strategy tag: {no_strategy}")
    print()

    # Sort by count descending
    sorted_strategies = sorted(stats.items(), key=lambda x: -x[1]["count"])

    print(f"{'Strategy':<18} {'Nodes':>8} {'Avg Depth':>10} {'Max Depth':>10} {'Avg Conf':>10} {'Found':>8}")
    print("-" * 70)

    for strategy, s in sorted_strategies:
        if s["count"] == 0:
            continue

        avg_depth = sum(s["depths"]) / len(s["depths"]) if s["depths"] else 0
        max_depth = max(s["depths"]) if s["depths"] else 0
        avg_leverage = sum(s["leverages"]) / len(s["leverages"]) if s["leverages"] else 0

        print(f"{strategy:<18} {s['count']:>8} {avg_depth:>10.1f} {max_depth:>10} {avg_leverage:>10.2f} {s['foundational']:>8}")

    print("-" * 70)

    # Detailed breakdown
    print("\n>>> DETAILED BREAKDOWN BY STRATEGY:\n")

    for strategy, s in sorted_strategies:
        if s["count"] == 0:
            continue

        print(f"  {strategy.upper()}:")
        print(f"    Total nodes: {s['count']}")

        if s["depths"]:
            depth_dist = defaultdict(int)
            for d in s["depths"]:
                bucket = (d // 10) * 10
                depth_dist[bucket] += 1

            print(f"    Depth distribution:")
            for bucket in sorted(depth_dist.keys()):
                bar = "█" * (depth_dist[bucket] // 5)
                print(f"      {bucket:3d}-{bucket+9:3d}: {depth_dist[bucket]:4d} {bar}")

        print(f"    Branch types: {dict(s['branch_types'])}")
        print(f"    Foundational claims found: {s['foundational']}")
        print()

    # Recommendations
    print("=" * 70)
    print("RECOMMENDATIONS:")
    print("=" * 70)

    if sorted_strategies:
        best_depth = max(sorted_strategies, key=lambda x: max(x[1]["depths"]) if x[1]["depths"] else 0)
        best_count = sorted_strategies[0]
        best_foundational = max(sorted_strategies, key=lambda x: x[1]["foundational"])

        print(f"  - Most productive: {best_count[0]} ({best_count[1]['count']} nodes)")
        print(f"  - Deepest exploration: {best_depth[0]} (max depth {max(best_depth[1]['depths']) if best_depth[1]['depths'] else 0})")
        print(f"  - Most foundational: {best_foundational[0]} ({best_foundational[1]['foundational']} foundational claims)")

    conn.close()


def sample_by_strategy(db_path: str, strategy: str, limit: int = 10):
    """Show sample claims discovered by a specific strategy"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM nodes
        WHERE content LIKE ?
        ORDER BY depth DESC
        LIMIT ?
    """, (f'%"discovered_by_strategy": "{strategy}"%', limit))

    print(f"\n>>> SAMPLE CLAIMS FROM {strategy.upper()}:\n")
    for row in cursor.fetchall():
        print(f"  [d{row['depth']:2d}] {row['claim'][:70]}...")

    conn.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_strategies.py <db_path> [strategy_to_sample]")
        sys.exit(1)

    db_path = sys.argv[1]

    if not Path(db_path).exists():
        print(f"Database not found: {db_path}")
        sys.exit(1)

    analyze(db_path)

    if len(sys.argv) > 2:
        sample_by_strategy(db_path, sys.argv[2])
