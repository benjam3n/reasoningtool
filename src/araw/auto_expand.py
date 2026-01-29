"""
ARAW Auto-Expander

Automatically expands an ARAW search tree by recursively branching on claims.
Uses patterns and heuristics to generate meaningful branches.

Usage:
    python auto_expand.py --duration 3600  # Run for 1 hour
    python auto_expand.py --nodes 10000    # Generate 10k nodes
"""

import argparse
import time
import random
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from araw_engine import ARAWEngine, BranchType, NodeStatus, Node


# ============================================
# EXPANSION PATTERNS
# ============================================

# Patterns for generating ASSUME WRONG alternatives
ALTERNATIVE_PATTERNS = {
    # If claim contains these keywords, suggest these alternatives
    "need": [
        "might not actually need this",
        "want this but don't need it",
        "need something else instead",
        "need has been misidentified",
    ],
    "want": [
        "don't actually want this",
        "want something different",
        "want is based on false assumption",
        "want conflicts with other wants",
    ],
    "must": [
        "don't actually have to",
        "there are other ways",
        "requirement is artificial",
        "constraint can be removed",
    ],
    "should": [
        "shouldn't actually",
        "should do something else",
        "should is based on others' expectations",
        "should is outdated advice",
    ],
    "can't": [
        "actually can",
        "constraint is assumed not real",
        "haven't tried hard enough",
        "need to find another way",
    ],
    "always": [
        "not always true",
        "exceptions exist",
        "pattern can be broken",
        "generalization is false",
    ],
    "never": [
        "sometimes does happen",
        "conditions can change",
        "haven't tried the right approach",
        "belief is limiting",
    ],
    "only": [
        "other options exist",
        "haven't explored alternatives",
        "constraint is artificial",
        "more possibilities than assumed",
    ],
    "best": [
        "might not be the best",
        "best for whom?",
        "best by what criteria?",
        "better options exist",
    ],
    "correct": [
        "might be incorrect",
        "partially correct",
        "correct but incomplete",
        "based on flawed information",
    ],
    "true": [
        "might be false",
        "partially true",
        "true in some contexts only",
        "truth is more nuanced",
    ],
    "certain": [
        "uncertainty exists",
        "certainty is overconfident",
        "new information could change this",
        "certainty is assumed not verified",
    ],
    "know": [
        "might not actually know",
        "knowledge is incomplete",
        "knowledge is outdated",
        "belief mistaken for knowledge",
    ],
    "works": [
        "might not work",
        "works partially",
        "works in limited conditions",
        "appears to work but doesn't",
    ],
    "causes": [
        "correlation not causation",
        "other factors involved",
        "causation is reversed",
        "causation is indirect",
    ],
    "because": [
        "reason is wrong",
        "reason is incomplete",
        "real reason is different",
        "multiple reasons exist",
    ],
    "problem": [
        "not actually a problem",
        "symptom not root cause",
        "problem is misdiagnosed",
        "problem is opportunity",
    ],
    "solution": [
        "not actually a solution",
        "solution creates new problems",
        "better solutions exist",
        "solution addresses wrong problem",
    ],
    "will": [
        "might not happen",
        "outcome is uncertain",
        "prediction is overconfident",
        "future is unpredictable",
    ],
    "is": [
        "might not be",
        "is partially",
        "appears to be but isn't",
        "depends on perspective",
    ],
}

# Meta-level patterns (can be applied to any claim)
META_PATTERNS = [
    ("source is unreliable", "information source might be wrong"),
    ("outdated", "this might be outdated information"),
    ("context changed", "context has changed since this was true"),
    ("perspective limited", "this is from limited perspective"),
    ("assumption hidden", "hidden assumption underlies this"),
    ("definition unclear", "key term is poorly defined"),
    ("measurement flawed", "how this was measured might be flawed"),
    ("sample biased", "based on biased sample"),
    ("incentives misaligned", "someone benefits from this being believed"),
    ("complexity reduced", "oversimplification of complex reality"),
]

# Deeper questioning patterns
DEEP_PATTERNS = [
    "who said this and why?",
    "what evidence supports this?",
    "what would falsify this?",
    "who benefits from this being true?",
    "what's the opposite and could it be true?",
    "what assumptions does this rest on?",
    "how was this determined?",
    "what's the track record of similar claims?",
    "what are the boundary conditions?",
    "does this generalize or is it specific?",
]


class ARAWAutoExpander:
    """
    Automatically expands ARAW search trees using patterns and heuristics.
    """

    def __init__(self, engine: ARAWEngine):
        self.engine = engine
        self.nodes_created = 0
        self.start_time = None
        self.log_interval = 100  # Log every N nodes

    def expand_node(self, node: Node) -> int:
        """
        Expand a single node by creating ASSUME RIGHT and ASSUME WRONG branches.
        Returns number of nodes created. No depth limit - expands until naturally terminal.
        """
        claim = node.claim
        nodes_created = 0

        # Generate ASSUME RIGHT branch
        right_claim = self._generate_assume_right(claim)
        right_id = self.engine.add_node(
            parent_id=node.id,
            claim=right_claim,
            branch_type=BranchType.ASSUME_RIGHT,
            content={"generated": True, "parent_claim": claim},
            leverage_score=self._calculate_leverage(claim, node.depth)
        )
        nodes_created += 1

        # Generate ASSUME WRONG branch with alternatives
        wrong_claim, alternatives = self._generate_assume_wrong(claim)
        wrong_id = self.engine.add_node(
            parent_id=node.id,
            claim=wrong_claim,
            branch_type=BranchType.ASSUME_WRONG,
            content={"generated": True, "parent_claim": claim, "alternatives": alternatives},
            leverage_score=self._calculate_leverage(claim, node.depth)
        )
        nodes_created += 1

        # Add alternatives
        for alt in alternatives:
            self.engine.add_alternative(wrong_id, alt)

        # Mark parent as explored
        self.engine.update_status(node.id, NodeStatus.EXPLORED)

        return nodes_created

    def _generate_assume_right(self, claim: str) -> str:
        """Generate an ASSUME RIGHT claim"""
        claim_lower = claim.lower()

        # Simple patterns
        if "might" in claim_lower or "maybe" in claim_lower:
            return claim.replace("might", "does").replace("maybe", "definitely")

        if claim_lower.startswith("is "):
            return f"Confirmed: {claim}"

        if "?" in claim:
            return f"Answer is yes: {claim.replace('?', '')}"

        # Default: affirm the claim
        prefixes = [
            "This is correct: ",
            "Verified: ",
            "Confirmed: ",
            "True that ",
            "Accept: ",
        ]
        return random.choice(prefixes) + claim

    def _generate_assume_wrong(self, claim: str) -> Tuple[str, List[str]]:
        """Generate an ASSUME WRONG claim with alternatives"""
        claim_lower = claim.lower()
        alternatives = []

        # Find matching patterns
        for keyword, alts in ALTERNATIVE_PATTERNS.items():
            if keyword in claim_lower:
                alternatives.extend(alts[:2])  # Take up to 2 from each match

        # Add meta-level alternatives
        meta_choice = random.choice(META_PATTERNS)
        alternatives.append(f"{meta_choice[1]}")

        # Add deep questioning
        deep_choice = random.choice(DEEP_PATTERNS)
        alternatives.append(f"Question: {deep_choice}")

        # Limit alternatives
        alternatives = alternatives[:6]

        # Generate wrong claim
        if "is" in claim_lower:
            wrong_claim = claim.replace(" is ", " might not be ")
        elif "will" in claim_lower:
            wrong_claim = claim.replace(" will ", " might not ")
        elif "can" in claim_lower:
            wrong_claim = claim.replace(" can ", " might not be able to ")
        else:
            prefixes = [
                "Questioning: ",
                "Uncertain: ",
                "Challenging: ",
                "Doubt: ",
            ]
            wrong_claim = random.choice(prefixes) + claim

        return wrong_claim, alternatives

    def _calculate_leverage(self, claim: str, depth: int) -> float:
        """Calculate leverage score for a claim"""
        # Base leverage decreases with depth
        base = max(0.3, 1.0 - (depth * 0.08))

        # Boost for certain keywords
        high_leverage_keywords = ["must", "only", "always", "never", "certain", "need", "critical", "essential"]
        claim_lower = claim.lower()

        for keyword in high_leverage_keywords:
            if keyword in claim_lower:
                base = min(1.0, base + 0.15)
                break

        # Add some randomness
        base += random.uniform(-0.1, 0.1)

        return max(0.1, min(1.0, base))

    def run_for_duration(self, duration_seconds: int, target_nodes: Optional[int] = None):
        """Run expansion for a specified duration or until target nodes reached"""
        self.start_time = datetime.now()
        end_time = self.start_time + timedelta(seconds=duration_seconds)

        print(f"Starting ARAW auto-expansion")
        print(f"Duration: {duration_seconds}s ({duration_seconds/3600:.1f} hours)")
        print(f"No depth limit - runs until naturally terminal")
        if target_nodes:
            print(f"Target nodes: {target_nodes}")
        print("-" * 60)

        iteration = 0
        last_log_time = time.time()

        while datetime.now() < end_time:
            # Check target
            if target_nodes and self.nodes_created >= target_nodes:
                print(f"\nReached target of {target_nodes} nodes")
                break

            # Get unexplored nodes (prioritize by leverage, then depth)
            unexplored = self.engine.get_unexplored(limit=50)

            if not unexplored:
                print("\nNo more unexplored nodes - all paths exhausted")
                break

            # Expand nodes
            for node in unexplored:
                if datetime.now() >= end_time:
                    break
                if target_nodes and self.nodes_created >= target_nodes:
                    break

                created = self.expand_node(node)
                self.nodes_created += created
                iteration += 1

                # Periodic logging
                if self.nodes_created % self.log_interval == 0:
                    elapsed = (datetime.now() - self.start_time).total_seconds()
                    rate = self.nodes_created / elapsed if elapsed > 0 else 0
                    stats = self.engine.get_stats()
                    print(f"[{elapsed/60:.1f}m] Nodes: {stats['total_nodes']} | "
                          f"Rate: {rate:.1f}/s | "
                          f"Unexplored: {stats['by_status'].get('unexplored', 0)} | "
                          f"Max depth: {stats['max_depth']}")

        # Final summary
        self._print_summary()

    def run_for_nodes(self, target_nodes: int):
        """Run until target number of nodes is reached"""
        self.run_for_duration(duration_seconds=999999, target_nodes=target_nodes)

    def run_forever(self):
        """Run until Ctrl+C or all paths exhausted"""
        self.start_time = datetime.now()

        print(f"Starting ARAW auto-expansion")
        print(f"No depth limit, no time limit - Ctrl+C to stop")
        print("-" * 60)

        while True:
            unexplored = self.engine.get_unexplored(limit=50)

            if not unexplored:
                print("\nNo more unexplored nodes - all paths exhausted")
                break

            for node in unexplored:
                created = self.expand_node(node)
                self.nodes_created += created

                if self.nodes_created % self.log_interval == 0:
                    elapsed = (datetime.now() - self.start_time).total_seconds()
                    rate = self.nodes_created / elapsed if elapsed > 0 else 0
                    stats = self.engine.get_stats()
                    print(f"[{elapsed/60:.1f}m] Nodes: {stats['total_nodes']} | "
                          f"Rate: {rate:.1f}/s | "
                          f"Unexplored: {stats['by_status'].get('unexplored', 0)} | "
                          f"Max depth: {stats['max_depth']}")

        self._print_summary()

    def _print_summary(self):
        """Print expansion summary"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        stats = self.engine.get_stats()

        print("\n" + "=" * 60)
        print("EXPANSION COMPLETE")
        print("=" * 60)
        print(f"Duration: {elapsed/60:.1f} minutes ({elapsed/3600:.2f} hours)")
        print(f"Total nodes: {stats['total_nodes']}")
        print(f"Nodes created this run: {self.nodes_created}")
        print(f"Rate: {self.nodes_created/elapsed:.2f} nodes/second")
        print(f"Max depth reached: {stats['max_depth']}")
        print(f"\nBy status:")
        for status, count in stats['by_status'].items():
            print(f"  {status}: {count}")
        print(f"\nBy depth:")
        for depth, count in sorted(stats['by_depth'].items()):
            bar = "█" * min(50, count // 10)
            print(f"  {depth:2d}: {count:5d} {bar}")
        print(f"\nTotal alternatives: {stats['total_alternatives']}")


def create_initial_claims() -> List[str]:
    """Create a diverse set of initial claims to seed the search"""
    return [
        # Life decisions
        "I need to make an important decision",
        "The current path is the right one",
        "Change is necessary",
        "This opportunity is worth pursuing",
        "The risk is acceptable",

        # Work/career
        "My career is on track",
        "This job is the right fit",
        "I should stay in my current role",
        "Growth requires leaving comfort zone",
        "Success requires sacrifice",

        # Relationships
        "This relationship is healthy",
        "Communication is effective",
        "Trust has been established",
        "Boundaries are appropriate",
        "Expectations are realistic",

        # Health
        "Current lifestyle is sustainable",
        "Health habits are adequate",
        "Stress levels are manageable",
        "Self-care is sufficient",
        "Energy levels are normal",

        # Finance
        "Financial situation is stable",
        "Spending is under control",
        "Savings are adequate",
        "Investments are sound",
        "Income is sufficient",

        # Goals
        "Goals are clearly defined",
        "Timeline is realistic",
        "Resources are available",
        "Support system exists",
        "Motivation will persist",

        # Knowledge
        "Understanding is complete",
        "Information is accurate",
        "Sources are reliable",
        "Analysis is correct",
        "Conclusion is valid",

        # Meta
        "This approach is correct",
        "Assumptions are valid",
        "Evidence supports this",
        "Logic is sound",
        "Perspective is balanced",
    ]


def main():
    parser = argparse.ArgumentParser(description="ARAW Auto-Expander")
    parser.add_argument("--duration", type=int, default=None, help="Duration in seconds (default: unlimited)")
    parser.add_argument("--nodes", type=int, default=None, help="Target number of nodes (optional)")
    parser.add_argument("--db", type=str, default="araw_auto.db", help="Database file")
    parser.add_argument("--continue", dest="continue_existing", action="store_true", help="Continue existing search")
    parser.add_argument("--seed", type=str, default=None, help="Initial claim to seed the search")

    args = parser.parse_args()

    # Create or load engine
    engine = ARAWEngine(args.db)

    # Check if we're continuing or starting fresh
    root = engine.get_root()
    if root and not args.continue_existing:
        print(f"Database {args.db} already has a search. Use --continue to expand it.")
        print(f"Or delete the database to start fresh.")
        stats = engine.get_stats()
        print(f"Current stats: {stats['total_nodes']} nodes, max depth {stats['max_depth']}")
        engine.close()
        return

    if not root:
        # Create new search with initial claims
        if args.seed:
            initial_claims = [args.seed]
        else:
            initial_claims = create_initial_claims()

        print(f"Creating new search with {len(initial_claims)} initial claims...")
        root_id = engine.create_search(
            "ARAW Search Root",
            metadata={"created": datetime.now().isoformat(), "type": "auto_expand"}
        )

        # Add initial claims as children of root
        for claim in initial_claims:
            engine.add_node(
                parent_id=root_id,
                claim=claim,
                branch_type=BranchType.ROOT,
                leverage_score=0.8
            )

        engine.update_status(root_id, NodeStatus.EXPLORED)
        print(f"Added {len(initial_claims)} seed claims")

    # Run expansion
    expander = ARAWAutoExpander(engine)

    try:
        if args.nodes:
            expander.run_for_nodes(args.nodes)
        else:
            expander.run_forever()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        expander._print_summary()

    # Export tree structure
    export_file = args.db.replace(".db", "_export.json")
    print(f"\nExporting tree to {export_file}...")
    engine.export_json(export_file)

    engine.close()


if __name__ == "__main__":
    main()
