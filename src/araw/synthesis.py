"""
ARAW Synthesis Engine

Query and reason over ARAW trees to extract insights.
Answers arbitrary questions about the exploration.

Usage:
    python synthesis.py --db worlddirection.db "What are the key cruxes?"
    python synthesis.py --db worlddirection.db "If institutions can self-correct, what follows?"
    python synthesis.py --db worlddirection.db "Where do different branches converge?"
"""

import argparse
import json
import os
import sqlite3
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

from araw_engine import ARAWEngine, Node


DEFAULT_MODEL = "gpt-5-nano"
DEFAULT_KEY_FILE = str(Path.home() / ".config" / "gosm" / "openai_api_key")


def read_api_key(path: Optional[str] = None) -> Optional[str]:
    """Read API key from env or file"""
    env = os.environ.get("OPENAI_API_KEY", "").strip()
    if env:
        return env
    for p in ([path] if path else []) + [DEFAULT_KEY_FILE]:
        if p and Path(p).expanduser().is_file():
            key = Path(p).expanduser().read_text().splitlines()[0].strip()
            if key:
                return key
    return None


def llm_call(api_key: str, system: str, user: str, model: str = DEFAULT_MODEL) -> Optional[str]:
    """Make LLM API call"""
    payload = {
        "model": model,
        "max_output_tokens": 4000,
        "input": [
            {"role": "system", "content": [{"type": "input_text", "text": system}]},
            {"role": "user", "content": [{"type": "input_text", "text": user}]},
        ],
    }

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json") as f:
        json.dump(payload, f)
        payload_path = f.name

    try:
        cmd = [
            "curl", "-sS", "https://api.openai.com/v1/responses",
            "-H", f"Authorization: Bearer {api_key}",
            "-H", "Content-Type: application/json",
            "-d", f"@{payload_path}"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        resp = json.loads(result.stdout)

        # Extract text from response
        if "output" in resp:
            for item in resp.get("output", []):
                for c in item.get("content", []):
                    if isinstance(c, dict) and c.get("type") in ("output_text", "text"):
                        return c.get("text", "").strip()
        return None
    except Exception as e:
        print(f"LLM error: {e}")
        return None
    finally:
        Path(payload_path).unlink(missing_ok=True)


class SynthesisEngine:
    """Query and synthesize insights from ARAW trees"""

    def __init__(self, db_path: str, api_key: str, model: str = DEFAULT_MODEL):
        self.engine = ARAWEngine(db_path)
        self.api_key = api_key
        self.model = model
        self.conn = self.engine.conn

    def get_root_claim(self) -> str:
        """Get the root claim"""
        return self.engine.get_root_claim() or "Unknown"

    def get_stats(self) -> Dict[str, Any]:
        """Get basic tree statistics"""
        return self.engine.get_stats()

    def get_crux_nodes(self, limit: int = 20) -> List[Dict]:
        """Get the most important crux nodes"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, claim, depth, leverage_score, content, branch_type
            FROM nodes
            WHERE leverage_score >= 0.8
            ORDER BY leverage_score DESC, depth ASC
            LIMIT ?
        """, (limit,))

        results = []
        for row in cursor:
            content = json.loads(row['content']) if row['content'] else {}
            results.append({
                'id': row['id'],
                'claim': row['claim'],
                'depth': row['depth'],
                'leverage': row['leverage_score'],
                'is_crux': content.get('is_crux', False),
                'branch_type': row['branch_type'],
                'strategy': content.get('discovered_by_strategy', 'unknown')
            })
        return results

    def get_foundational_nodes(self, limit: int = 20) -> List[Dict]:
        """Get foundational/bedrock claims"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, claim, depth, branch_type
            FROM nodes
            WHERE status = 'pruned'
            ORDER BY depth DESC
            LIMIT ?
        """, (limit,))

        return [{'id': row['id'], 'claim': row['claim'], 'depth': row['depth'],
                 'branch_type': row['branch_type']} for row in cursor]

    def get_path_to_root(self, node_id: int) -> List[Dict]:
        """Get the causal chain from a node back to root"""
        path = []
        current_id = node_id

        while current_id:
            node = self.engine.get_node(current_id)
            if not node:
                break
            path.append({
                'id': node.id,
                'claim': node.claim,
                'depth': node.depth,
                'branch_type': node.branch_type
            })
            current_id = node.parent_id

        path.reverse()
        return path

    def find_convergence(self, min_similarity: float = 0.5) -> List[Dict]:
        """Find claims that appear similar across different branches"""
        cursor = self.conn.cursor()

        # Get all claims with their branch paths
        cursor.execute("""
            SELECT id, claim, parent_id, depth
            FROM nodes
            WHERE depth > 0
            ORDER BY depth
        """)

        nodes = list(cursor.fetchall())

        # Simple word-overlap similarity to find potential convergences
        convergences = []
        seen_pairs = set()

        for i, node1 in enumerate(nodes[:500]):  # Limit for performance
            words1 = set(node1['claim'].lower().split())
            if len(words1) < 4:
                continue

            for node2 in nodes[i+1:500]:
                if node1['id'] == node2['id']:
                    continue

                # Skip if same parent (siblings aren't convergence)
                if node1['parent_id'] == node2['parent_id']:
                    continue

                words2 = set(node2['claim'].lower().split())
                if len(words2) < 4:
                    continue

                # Jaccard similarity
                intersection = len(words1 & words2)
                union = len(words1 | words2)
                similarity = intersection / union if union > 0 else 0

                if similarity >= min_similarity:
                    pair_key = tuple(sorted([node1['id'], node2['id']]))
                    if pair_key not in seen_pairs:
                        seen_pairs.add(pair_key)
                        convergences.append({
                            'claim1': node1['claim'],
                            'claim2': node2['claim'],
                            'depth1': node1['depth'],
                            'depth2': node2['depth'],
                            'similarity': similarity
                        })

        return sorted(convergences, key=lambda x: -x['similarity'])[:20]

    def get_branch_summary(self, node_id: int) -> Dict:
        """Get summary of a branch (descendants of a node)"""
        cursor = self.conn.cursor()

        # Get all descendants using recursive CTE
        cursor.execute("""
            WITH RECURSIVE descendants AS (
                SELECT id, claim, depth, leverage_score, status, branch_type
                FROM nodes WHERE id = ?
                UNION ALL
                SELECT n.id, n.claim, n.depth, n.leverage_score, n.status, n.branch_type
                FROM nodes n
                JOIN descendants d ON n.parent_id = d.id
            )
            SELECT * FROM descendants
        """, (node_id,))

        nodes = list(cursor.fetchall())

        crux_count = sum(1 for n in nodes if n['leverage_score'] and n['leverage_score'] >= 0.8)
        foundational_count = sum(1 for n in nodes if n['status'] == 'pruned')
        max_depth = max(n['depth'] for n in nodes) if nodes else 0

        return {
            'total_nodes': len(nodes),
            'crux_nodes': crux_count,
            'foundational_nodes': foundational_count,
            'max_depth': max_depth,
            'assume_right': sum(1 for n in nodes if n['branch_type'] == 'assume_right'),
            'assume_wrong': sum(1 for n in nodes if n['branch_type'] == 'assume_wrong')
        }

    def propagate_belief(self, node_id: int, assumed_true: bool) -> List[Dict]:
        """
        Given a node is assumed true or false, what are the implications?
        Returns the if_true consequences (assume_right children) or
        traces what would be invalidated (assume_wrong path).
        """
        cursor = self.conn.cursor()

        node = self.engine.get_node(node_id)
        if not node:
            return []

        implications = []

        if assumed_true:
            # Get downstream consequences (assume_right children)
            cursor.execute("""
                SELECT id, claim, depth, leverage_score
                FROM nodes
                WHERE parent_id = ? AND branch_type = 'assume_right'
            """, (node_id,))

            for row in cursor:
                implications.append({
                    'type': 'consequence',
                    'claim': row['claim'],
                    'depth': row['depth'],
                    'leverage': row['leverage_score']
                })
        else:
            # If false, the upstream causes need re-examination
            cursor.execute("""
                SELECT id, claim, depth, leverage_score
                FROM nodes
                WHERE parent_id = ? AND branch_type = 'assume_wrong'
            """, (node_id,))

            for row in cursor:
                implications.append({
                    'type': 'undermined_cause',
                    'claim': row['claim'],
                    'depth': row['depth'],
                    'leverage': row['leverage_score']
                })

        # Also trace impact on root
        path = self.get_path_to_root(node_id)
        if len(path) > 1:
            implications.append({
                'type': 'path_to_root',
                'steps': len(path),
                'path': [p['claim'][:60] for p in path]
            })

        return implications

    def get_long_chains(self, branch_type: str = "assume_wrong", min_length: int = 5, limit: int = 10) -> List[Dict]:
        """
        Find long consecutive chains of the same branch type.
        These represent deep causal reasoning in one direction.
        """
        cursor = self.conn.cursor()

        # Get all nodes with their parent and branch type
        cursor.execute("""
            SELECT id, parent_id, claim, branch_type, depth
            FROM nodes
            WHERE branch_type = ?
            ORDER BY depth DESC
        """, (branch_type,))

        nodes = {row['id']: dict(row) for row in cursor.fetchall()}

        # For each deep node, trace back and count consecutive same-type branches
        chains = []
        seen_chains = set()

        for node_id, node in sorted(nodes.items(), key=lambda x: -x[1]['depth']):
            chain = [node]
            current_id = node['parent_id']

            # Trace back through same branch_type ancestors
            while current_id:
                cursor.execute("""
                    SELECT id, parent_id, claim, branch_type, depth
                    FROM nodes WHERE id = ?
                """, (current_id,))
                parent = cursor.fetchone()
                if not parent or parent['branch_type'] != branch_type:
                    break
                chain.append(dict(parent))
                current_id = parent['parent_id']

            if len(chain) >= min_length:
                # Use the deepest node id as chain identifier to avoid duplicates
                chain_key = chain[0]['id']
                if chain_key not in seen_chains:
                    seen_chains.add(chain_key)
                    chain.reverse()  # Root to leaf order
                    chains.append({
                        'length': len(chain),
                        'start_depth': chain[0]['depth'],
                        'end_depth': chain[-1]['depth'],
                        'claims': [c['claim'] for c in chain]
                    })

        # Sort by length descending
        chains.sort(key=lambda x: -x['length'])
        return chains[:limit]

    def get_deepest_paths(self, limit: int = 5) -> List[Dict]:
        """Get the deepest paths from root to leaf"""
        cursor = self.conn.cursor()

        # Find deepest leaf nodes
        cursor.execute("""
            SELECT id, claim, depth FROM nodes
            ORDER BY depth DESC
            LIMIT ?
        """, (limit,))

        paths = []
        for row in cursor.fetchall():
            path = self.get_path_to_root(row['id'])

            # Count branch types in path
            right_count = sum(1 for p in path if p['branch_type'] == 'assume_right')
            wrong_count = sum(1 for p in path if p['branch_type'] == 'assume_wrong')

            paths.append({
                'depth': row['depth'],
                'leaf_claim': row['claim'],
                'path_length': len(path),
                'assume_right_count': right_count,
                'assume_wrong_count': wrong_count,
                'path': path
            })

        return paths

    def get_domain_distribution(self) -> Dict[str, int]:
        """Analyze which domains are represented"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT claim FROM nodes")

        domains = defaultdict(int)
        domain_keywords = {
            'HUMAN': ['person', 'people', 'individual', 'competent', 'skill', 'bias', 'motivation', 'psychology'],
            'INSTITUTIONAL': ['system', 'organization', 'policy', 'government', 'institution', 'regulation'],
            'EVIDENTIAL': ['evidence', 'data', 'test', 'study', 'research', 'measure', 'observation'],
            'EPISTEMOLOGICAL': ['knowledge', 'truth', 'logic', 'reason', 'method', 'assumption'],
            'PRACTICAL': ['cost', 'money', 'resource', 'time', 'budget', 'feasible'],
            'RELATIONAL': ['family', 'relationship', 'trust', 'communication', 'social'],
            'ETHICAL': ['moral', 'ethic', 'fair', 'justice', 'value', 'right', 'wrong'],
            'TEMPORAL': ['future', 'past', 'history', 'trend', 'generation', 'change'],
            'CULTURAL': ['culture', 'tradition', 'norm', 'society', 'worldview'],
            'ENVIRONMENTAL': ['environment', 'climate', 'ecology', 'sustainable'],
            'TECHNOLOGICAL': ['technology', 'ai', 'automation', 'digital', 'innovation'],
            'GEOPOLITICAL': ['international', 'power', 'conflict', 'cooperation', 'nation'],
            'ECONOMIC': ['market', 'inequality', 'trade', 'incentive', 'economic'],
            'INFORMATIONAL': ['media', 'misinformation', 'narrative', 'attention'],
            'SYSTEMIC': ['feedback', 'complexity', 'emergence', 'unintended'],
        }

        for row in cursor:
            claim_lower = row['claim'].lower()
            matched = False
            for domain, keywords in domain_keywords.items():
                if any(kw in claim_lower for kw in keywords):
                    domains[domain] += 1
                    matched = True
                    break
            if not matched:
                domains['OTHER'] += 1

        return dict(sorted(domains.items(), key=lambda x: -x[1]))

    def build_context(self, question: str) -> str:
        """Build relevant context for answering a question"""
        stats = self.get_stats()
        root = self.get_root_claim()
        crux_nodes = self.get_crux_nodes(10)
        foundational = self.get_foundational_nodes(10)
        domains = self.get_domain_distribution()

        context = f"""ARAW TREE ANALYSIS

ROOT CLAIM: "{root}"

STATISTICS:
- Total nodes: {stats['total_nodes']}
- Max depth: {stats['max_depth']}
- Explored: {stats['by_status'].get('explored', 0)}
- Foundational (pruned): {stats['by_status'].get('pruned', 0)}
- Unexplored: {stats['by_status'].get('unexplored', 0)}

TOP CRUX NODES (most pivotal claims):
"""
        for i, node in enumerate(crux_nodes[:10], 1):
            context += f"{i}. [{node['branch_type']}] {node['claim'][:100]}...\n"

        context += "\nFOUNDATIONAL CLAIMS (bedrock beliefs):\n"
        for i, node in enumerate(foundational[:10], 1):
            context += f"{i}. {node['claim'][:100]}...\n"

        context += "\nDOMAIN COVERAGE:\n"
        for domain, count in list(domains.items())[:10]:
            context += f"- {domain}: {count}\n"

        # Add convergence if question seems to ask about it
        if 'converg' in question.lower() or 'common' in question.lower() or 'shared' in question.lower():
            convergences = self.find_convergence()
            if convergences:
                context += "\nCONVERGENCE (similar claims across branches):\n"
                for conv in convergences[:5]:
                    context += f"- \"{conv['claim1'][:50]}...\" ≈ \"{conv['claim2'][:50]}...\" (sim={conv['similarity']:.2f})\n"

        return context

    def answer_question(self, question: str) -> str:
        """Answer an arbitrary question about the tree using LLM"""
        context = self.build_context(question)

        system_prompt = """You are an expert analyst examining an ARAW (Assume Right Assume Wrong) causal exploration tree.

The tree explores a root claim by recursively asking:
- IF TRUE: What downstream consequences follow?
- IF FALSE (upstream): What assumptions would need to be wrong?

CRUX NODES are pivotal claims where true vs false dramatically changes belief in the root.
FOUNDATIONAL NODES are bedrock beliefs that terminate exploration.

Answer the user's question based on the tree analysis provided. Be specific and cite claims from the tree.
If asked about implications, trace through the causal structure.
If asked about gaps, identify underexplored domains or missing perspectives."""

        user_prompt = f"""{context}

USER QUESTION: {question}

Provide a clear, structured answer based on the tree analysis above."""

        response = llm_call(self.api_key, system_prompt, user_prompt, self.model)
        return response or "Failed to generate response"

    def interactive(self):
        """Interactive query mode"""
        print(f"ARAW Synthesis Engine")
        print(f"Root claim: {self.get_root_claim()}")
        print(f"Stats: {self.get_stats()['total_nodes']} nodes")
        print("-" * 60)
        print("Ask questions about the tree. Type 'quit' to exit.")
        print("Examples:")
        print("  - What are the key cruxes?")
        print("  - Where do branches converge?")
        print("  - What domains are underexplored?")
        print("  - If [claim] is true, what follows?")
        print("-" * 60)

        while True:
            try:
                question = input("\nQuestion: ").strip()
                if question.lower() in ('quit', 'exit', 'q'):
                    break
                if not question:
                    continue

                print("\nAnalyzing...")
                answer = self.answer_question(question)
                print(f"\n{answer}")

            except KeyboardInterrupt:
                break
            except EOFError:
                break

        print("\nGoodbye!")


def main():
    parser = argparse.ArgumentParser(description="ARAW Synthesis Engine")
    parser.add_argument("--db", type=str, required=True, help="Database file")
    parser.add_argument("question", nargs="?", help="Question to answer (or interactive mode if omitted)")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help="Model to use")
    parser.add_argument("--crux", action="store_true", help="Show top crux nodes")
    parser.add_argument("--foundational", action="store_true", help="Show foundational nodes")
    parser.add_argument("--convergence", action="store_true", help="Find convergent claims")
    parser.add_argument("--domains", action="store_true", help="Show domain distribution")
    parser.add_argument("--propagate", type=int, help="Propagate belief from node ID")
    parser.add_argument("--true", action="store_true", help="Assume node is true (with --propagate)")
    parser.add_argument("--long-chains", type=str, choices=["right", "wrong", "both"], help="Show long consecutive chains of assume_right or assume_wrong")
    parser.add_argument("--min-chain", type=int, default=5, help="Minimum chain length (default: 5)")
    parser.add_argument("--deepest", action="store_true", help="Show deepest paths from root to leaf")

    args = parser.parse_args()

    api_key = read_api_key()
    if not api_key:
        print("Error: No API key found")
        return

    engine = SynthesisEngine(args.db, api_key, args.model)

    # Handle specific queries
    if args.crux:
        print("TOP CRUX NODES:")
        for node in engine.get_crux_nodes(20):
            print(f"  [{node['leverage']:.1f}] {node['claim']}")
        return

    if args.foundational:
        print("FOUNDATIONAL NODES:")
        for node in engine.get_foundational_nodes(20):
            print(f"  [d={node['depth']}] {node['claim']}")
        return

    if args.convergence:
        print("CONVERGENT CLAIMS:")
        for conv in engine.find_convergence():
            print(f"  [{conv['similarity']:.2f}]")
            print(f"    1: {conv['claim1']}")
            print(f"    2: {conv['claim2']}")
            print()
        return

    if args.domains:
        print("DOMAIN DISTRIBUTION:")
        for domain, count in engine.get_domain_distribution().items():
            bar = "█" * (count // 100)
            print(f"  {domain:<20} {count:5d} {bar}")
        return

    if args.propagate:
        assumed = args.true
        print(f"BELIEF PROPAGATION: Node {args.propagate} assumed {'TRUE' if assumed else 'FALSE'}")
        for impl in engine.propagate_belief(args.propagate, assumed):
            print(f"  [{impl['type']}] {impl.get('claim', impl.get('path', ''))}")
        return

    if args.long_chains:
        if args.long_chains in ["wrong", "both"]:
            print(f"LONG ASSUME_WRONG CHAINS (min length {args.min_chain}):")
            print("These are deep 'why?' chains - drilling into upstream causes")
            print("-" * 60)
            for chain in engine.get_long_chains("assume_wrong", args.min_chain):
                print(f"\n[Chain length: {chain['length']}, depth {chain['start_depth']}-{chain['end_depth']}]")
                for i, claim in enumerate(chain['claims']):
                    indent = "  " * min(i, 5)
                    arrow = "↳ " if i > 0 else ""
                    print(f"{indent}{arrow}{claim}")

        if args.long_chains in ["right", "both"]:
            print(f"\nLONG ASSUME_RIGHT CHAINS (min length {args.min_chain}):")
            print("These are deep 'if true?' chains - tracing downstream consequences")
            print("-" * 60)
            for chain in engine.get_long_chains("assume_right", args.min_chain):
                print(f"\n[Chain length: {chain['length']}, depth {chain['start_depth']}-{chain['end_depth']}]")
                for i, claim in enumerate(chain['claims']):
                    indent = "  " * min(i, 5)
                    arrow = "→ " if i > 0 else ""
                    print(f"{indent}{arrow}{claim}")
        return

    if args.deepest:
        print("DEEPEST PATHS (root to leaf):")
        print("-" * 60)
        for path_info in engine.get_deepest_paths(5):
            print(f"\n[Depth: {path_info['depth']}, {path_info['assume_wrong_count']} wrong / {path_info['assume_right_count']} right]")
            print(f"Leaf: {path_info['leaf_claim']}")
            print("Path:")
            for i, step in enumerate(path_info['path'][:15]):  # Show first 15 steps
                bt = "→" if step['branch_type'] == 'assume_right' else "↗" if step['branch_type'] == 'assume_wrong' else "●"
                print(f"  {i:2d}. [{bt}] {step['claim'][:100]}...")
            if len(path_info['path']) > 15:
                print(f"  ... and {len(path_info['path']) - 15} more steps")
        return

    # Question or interactive mode
    if args.question:
        answer = engine.answer_question(args.question)
        print(answer)
    else:
        engine.interactive()


if __name__ == "__main__":
    main()
