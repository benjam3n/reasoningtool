"""
Resumable ARAW Protocol

Enables multi-session ARAW for 16x+ and 32x depth by:
1. Summarizing session state at pause points
2. Loading prior context when resuming
3. Tracking exploration frontiers across sessions
4. Maintaining coherence despite context gaps

Key insight: ARAW sessions can be chunked if we properly track:
- What's been explored (explored nodes)
- What's pending (frontier nodes)
- What's foundational (committed claims)
- What's still uncertain (open claims)

Protocol:
1. PAUSE: Save state with summary, frontiers, commitments
2. RESUME: Load summary, inject frontier nodes, continue expansion
3. MERGE: Combine multiple session trees into unified view

Depth Requirements (from SKILL.md):
- 16x: 25 claims, 10 levels, 12 CRUX, 14 DO_FIRST, 3200-4400 lines
- 32x: 35 claims, 12 levels, 16 CRUX, 20 DO_FIRST, 6400-8800 lines

16x/32x specific features:
- Cross-domain synthesis tracking
- Second-order pattern identification
- Adversarial review tracking
- External reference integration
- Complete space mapping with unexplored regions
"""

import json
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple

from context_loader import ContextLoader, ContextBlock, ContextNode


@dataclass
class DepthRequirements:
    """Requirements for each ARAW depth level"""
    claims: int
    levels: int
    crux_points: int
    do_first_actions: int
    min_lines: int
    max_lines: int
    unconventional_quota: int
    # 16x/32x specific
    cross_domain_synthesis: bool = False
    second_order_patterns: bool = False
    adversarial_review: bool = False
    external_references: bool = False
    complete_mapping: bool = False


DEPTH_REQUIREMENTS = {
    '1x': DepthRequirements(5, 3, 2, 3, 250, 350, 1),
    '2x': DepthRequirements(7, 4, 3, 4, 400, 600, 2),
    '3x': DepthRequirements(10, 5, 4, 5, 600, 900, 3),
    '4x': DepthRequirements(12, 6, 5, 6, 800, 1100, 4),
    '8x': DepthRequirements(18, 8, 8, 10, 1600, 2200, 6),
    '16x': DepthRequirements(
        claims=25, levels=10, crux_points=12, do_first_actions=14,
        min_lines=3200, max_lines=4400, unconventional_quota=8,
        cross_domain_synthesis=True, second_order_patterns=True
    ),
    '32x': DepthRequirements(
        claims=35, levels=12, crux_points=16, do_first_actions=20,
        min_lines=6400, max_lines=8800, unconventional_quota=12,
        cross_domain_synthesis=True, second_order_patterns=True,
        adversarial_review=True, external_references=True, complete_mapping=True
    ),
}


@dataclass
class SessionSummary:
    """Summary of an ARAW session for resumption"""
    root_claim: str
    session_id: str
    created_at: str
    paused_at: str

    # Exploration state
    total_nodes: int
    max_depth: int
    explored_count: int
    frontier_count: int

    # Key findings
    foundational_claims: List[str]  # Claims marked as foundational
    open_claims: List[str]  # Claims still uncertain
    crux_points: List[str]  # Key decision points
    do_first_actions: List[str]  # Prioritized actions

    # For resumption
    frontier_nodes: List[Dict[str, Any]]  # Nodes to explore next
    tensions: List[Tuple[str, str]]  # AR vs AW tensions

    # ARAW depth tracking (NEW for 16x/32x)
    depth_level: str = '8x'  # 1x, 2x, 3x, 4x, 8x, 16x, 32x
    session_number: int = 1  # N of M for multi-session
    total_sessions_planned: int = 1  # M
    claims_covered: List[str] = field(default_factory=list)
    claims_remaining: List[str] = field(default_factory=list)

    # 16x/32x specific tracking
    cross_domain_insights: List[str] = field(default_factory=list)
    second_order_patterns: List[str] = field(default_factory=list)
    adversarial_reviews: List[Dict[str, str]] = field(default_factory=list)
    external_references: List[str] = field(default_factory=list)
    unexplored_regions: List[str] = field(default_factory=list)
    what_would_change_mind: List[Dict[str, str]] = field(default_factory=list)

    def to_context_nodes(self) -> List[ContextNode]:
        """Convert summary to context nodes for injection"""
        nodes = []

        # Root as context anchor
        nodes.append(ContextNode(
            claim=f"[RESUMING] Previous root: {self.root_claim}",
            branch_type='context',
            parent_claim=None,
            source=f'session:{self.session_id}',
            metadata={'type': 'root_anchor'}
        ))

        # Foundational claims - high confidence
        for claim in self.foundational_claims:
            nodes.append(ContextNode(
                claim=f"[FOUNDATIONAL] {claim}",
                branch_type='context',
                parent_claim=None,
                source=f'session:{self.session_id}',
                metadata={'type': 'foundational'},
                leverage_score=0.9
            ))

        # CRUX points - high leverage
        for crux in self.crux_points:
            nodes.append(ContextNode(
                claim=f"[CRUX] {crux}",
                branch_type='context',
                parent_claim=None,
                source=f'session:{self.session_id}',
                metadata={'type': 'crux'},
                leverage_score=0.8
            ))

        # Frontier nodes - to continue exploration
        for frontier in self.frontier_nodes:
            nodes.append(ContextNode(
                claim=frontier['claim'],
                branch_type=frontier.get('branch_type', 'context'),
                parent_claim=frontier.get('parent_claim'),
                source=f'session:{self.session_id}',
                metadata={'type': 'frontier', 'original_depth': frontier.get('depth', 0)},
                leverage_score=frontier.get('leverage_score', 0.5)
            ))

        return nodes

    def to_markdown(self) -> str:
        """Generate markdown summary for human review"""
        lines = [
            f"# ARAW Session Summary",
            f"",
            f"**Root**: {self.root_claim}",
            f"**Session**: {self.session_id}",
            f"**Depth**: {self.depth_level}",
            f"**Progress**: Session {self.session_number} of {self.total_sessions_planned}",
            f"**Paused**: {self.paused_at}",
            f"",
            f"## Exploration State",
            f"- Total nodes: {self.total_nodes}",
            f"- Max depth: {self.max_depth}",
            f"- Explored: {self.explored_count}",
            f"- Frontier (to explore): {self.frontier_count}",
        ]

        # Show depth requirements progress
        if self.depth_level in DEPTH_REQUIREMENTS:
            req = DEPTH_REQUIREMENTS[self.depth_level]
            lines.extend([
                f"",
                f"## Progress vs {self.depth_level} Requirements",
                f"- Claims: {len(self.claims_covered)}/{req.claims} covered",
                f"- Levels: {self.max_depth}/{req.levels} deep",
                f"- CRUX: {len(self.crux_points)}/{req.crux_points}",
                f"- DO_FIRST: {len(self.do_first_actions)}/{req.do_first_actions}",
            ])

        lines.extend([
            f"",
            f"## Foundational Claims (COMMITTED)",
        ])

        for claim in self.foundational_claims:
            lines.append(f"- {claim}")

        lines.extend([
            f"",
            f"## Open Claims (UNCERTAIN)",
        ])

        for claim in self.open_claims[:10]:  # Limit for readability
            lines.append(f"- {claim}")

        lines.extend([
            f"",
            f"## CRUX Points",
        ])

        for crux in self.crux_points:
            lines.append(f"- {crux}")

        lines.extend([
            f"",
            f"## DO_FIRST Actions",
        ])

        for action in self.do_first_actions:
            lines.append(f"1. {action}")

        lines.extend([
            f"",
            f"## Frontier (Next to Explore)",
        ])

        for frontier in self.frontier_nodes[:10]:
            lines.append(f"- {frontier['claim'][:80]}...")

        # 16x/32x specific sections
        if self.depth_level in ('16x', '32x'):
            if self.claims_remaining:
                lines.extend([
                    f"",
                    f"## Claims Remaining (to cover in next session)",
                ])
                for claim in self.claims_remaining[:15]:
                    lines.append(f"- {claim}")

            if self.cross_domain_insights:
                lines.extend([
                    f"",
                    f"## Cross-Domain Insights",
                ])
                for insight in self.cross_domain_insights:
                    lines.append(f"- {insight}")

            if self.second_order_patterns:
                lines.extend([
                    f"",
                    f"## Second-Order Patterns (patterns in patterns)",
                ])
                for pattern in self.second_order_patterns:
                    lines.append(f"- {pattern}")

            if self.unexplored_regions:
                lines.extend([
                    f"",
                    f"## Unexplored Regions (document for completeness)",
                ])
                for region in self.unexplored_regions:
                    lines.append(f"- {region}")

            if self.what_would_change_mind:
                lines.extend([
                    f"",
                    f"## What Would Change My Mind",
                ])
                for item in self.what_would_change_mind:
                    lines.append(f"- **{item.get('conclusion', 'Unknown')}**: {item.get('evidence', 'N/A')}")

        # 32x specific
        if self.depth_level == '32x':
            if self.adversarial_reviews:
                lines.extend([
                    f"",
                    f"## Adversarial Reviews",
                ])
                for review in self.adversarial_reviews:
                    lines.append(f"- **Conclusion**: {review.get('conclusion', 'Unknown')}")
                    lines.append(f"  **Challenge**: {review.get('challenge', 'N/A')}")
                    lines.append(f"  **Response**: {review.get('response', 'N/A')}")

            if self.external_references:
                lines.extend([
                    f"",
                    f"## External References",
                ])
                for ref in self.external_references:
                    lines.append(f"- {ref}")

        return "\n".join(lines)


class ResumableARAW:
    """
    Protocol for multi-session ARAW exploration.

    Usage:
        # Session 1: Start exploration
        session = ResumableARAW.start("I need to change careers", "session_001")
        # ... run ARAW expansion ...
        session.pause(db_path, summary_path)

        # Session 2: Resume
        session = ResumableARAW.resume(summary_path, db_path)
        # ... continue ARAW expansion from frontiers ...
        session.pause(db_path, summary_path)

        # Session N: Final synthesis
        session = ResumableARAW.resume(summary_path, db_path)
        final_tree = session.synthesize()
    """

    def __init__(self, root_claim: str, session_id: str):
        self.root_claim = root_claim
        self.session_id = session_id
        self.created_at = datetime.now().isoformat()
        self.summaries: List[SessionSummary] = []

    @classmethod
    def start(cls, root_claim: str, session_id: Optional[str] = None) -> 'ResumableARAW':
        """Start a new resumable ARAW session"""
        if session_id is None:
            session_id = f"araw_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        return cls(root_claim, session_id)

    @classmethod
    def resume(cls, summary_path: Path, db_path: Path) -> Tuple['ResumableARAW', ContextBlock]:
        """Resume from a previous session"""
        summary_data = json.loads(summary_path.read_text())
        summary = SessionSummary(**summary_data)

        session = cls(summary.root_claim, summary.session_id)
        session.summaries.append(summary)

        # Create context block for injection
        context = ContextBlock(
            nodes=summary.to_context_nodes(),
            summary=f"Resuming from {summary.session_id} with {len(summary.frontier_nodes)} frontier nodes",
            source_type='session',
            source_path=str(summary_path),
            injected_at=datetime.now().isoformat()
        )

        return session, context

    def pause(self, db_path: Path, summary_path: Path) -> SessionSummary:
        """Pause session and save state for resumption"""
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row

        # Get exploration statistics
        cursor = conn.execute("SELECT COUNT(*) as total, MAX(depth) as max_depth FROM nodes")
        row = cursor.fetchone()
        total_nodes = row['total']
        max_depth = row['max_depth'] or 0

        cursor = conn.execute("SELECT COUNT(*) FROM nodes WHERE status = 'explored'")
        explored_count = cursor.fetchone()[0]

        cursor = conn.execute("SELECT COUNT(*) FROM nodes WHERE status = 'frontier'")
        frontier_count = cursor.fetchone()[0]

        # Get foundational claims
        cursor = conn.execute(
            "SELECT claim FROM nodes WHERE commitment_status = 'foundational'"
        )
        foundational_claims = [row['claim'] for row in cursor]

        # Get open claims (no commitment status)
        cursor = conn.execute(
            "SELECT claim FROM nodes WHERE commitment_status IS NULL OR commitment_status = 'guess' LIMIT 50"
        )
        open_claims = [row['claim'] for row in cursor]

        # Get frontier nodes for resumption
        cursor = conn.execute("""
            SELECT claim, branch_type, depth, leverage_score, parent_id,
                   (SELECT claim FROM nodes p WHERE p.id = n.parent_id) as parent_claim
            FROM nodes n
            WHERE status = 'frontier'
            ORDER BY leverage_score DESC
            LIMIT 20
        """)
        frontier_nodes = [
            {
                'claim': row['claim'],
                'branch_type': row['branch_type'],
                'depth': row['depth'],
                'leverage_score': row['leverage_score'],
                'parent_claim': row['parent_claim']
            }
            for row in cursor
        ]

        # Get CRUX points and DO_FIRST from metadata
        crux_points = []
        do_first_actions = []
        tensions = []

        cursor = conn.execute("SELECT key, value FROM metadata")
        for row in cursor:
            if row['key'] == 'crux_points':
                crux_data = json.loads(row['value'])
                crux_points = [f"{c[0]}: {c[1]}" if isinstance(c, (list, tuple)) else str(c) for c in crux_data]
            elif row['key'] == 'tensions':
                tensions = json.loads(row['value'])

        conn.close()

        # Create summary
        summary = SessionSummary(
            root_claim=self.root_claim,
            session_id=self.session_id,
            created_at=self.created_at,
            paused_at=datetime.now().isoformat(),
            total_nodes=total_nodes,
            max_depth=max_depth,
            explored_count=explored_count,
            frontier_count=frontier_count,
            foundational_claims=foundational_claims,
            open_claims=open_claims,
            crux_points=crux_points,
            do_first_actions=do_first_actions,
            frontier_nodes=frontier_nodes,
            tensions=tensions
        )

        # Save summary
        summary_path.write_text(json.dumps(summary.__dict__, indent=2))

        # Also save markdown version for human review
        md_path = summary_path.with_suffix('.md')
        md_path.write_text(summary.to_markdown())

        self.summaries.append(summary)
        return summary

    def synthesize(self, db_path: Path) -> Dict[str, Any]:
        """
        Synthesize final results from multi-session exploration.

        Combines all session summaries and current database state
        into unified findings.
        """
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row

        # Aggregate foundational claims across sessions
        all_foundational = set()
        for summary in self.summaries:
            all_foundational.update(summary.foundational_claims)

        # Get current foundational
        cursor = conn.execute(
            "SELECT claim FROM nodes WHERE commitment_status = 'foundational'"
        )
        all_foundational.update(row['claim'] for row in cursor)

        # Get all CRUX points
        all_crux = []
        for summary in self.summaries:
            all_crux.extend(summary.crux_points)

        # Get exploration coverage
        cursor = conn.execute("""
            SELECT branch_type, COUNT(*) as count, MAX(depth) as max_depth
            FROM nodes
            GROUP BY branch_type
        """)
        coverage = {row['branch_type']: {'count': row['count'], 'max_depth': row['max_depth']} for row in cursor}

        conn.close()

        return {
            'root_claim': self.root_claim,
            'session_count': len(self.summaries) + 1,
            'total_exploration': sum(s.total_nodes for s in self.summaries),
            'foundational_claims': list(all_foundational),
            'crux_points': all_crux,
            'coverage': coverage,
            'sessions': [s.session_id for s in self.summaries]
        }


def validate_depth_requirements(summary: SessionSummary) -> Dict[str, Any]:
    """Check if session meets depth requirements"""
    if summary.depth_level not in DEPTH_REQUIREMENTS:
        return {'valid': True, 'message': 'Unknown depth level, skipping validation'}

    req = DEPTH_REQUIREMENTS[summary.depth_level]
    issues = []

    if len(summary.claims_covered) < req.claims:
        issues.append(f"Claims: {len(summary.claims_covered)}/{req.claims}")
    if summary.max_depth < req.levels:
        issues.append(f"Depth: {summary.max_depth}/{req.levels}")
    if len(summary.crux_points) < req.crux_points:
        issues.append(f"CRUX: {len(summary.crux_points)}/{req.crux_points}")
    if len(summary.do_first_actions) < req.do_first_actions:
        issues.append(f"DO_FIRST: {len(summary.do_first_actions)}/{req.do_first_actions}")

    # 16x/32x specific checks
    if req.cross_domain_synthesis and not summary.cross_domain_insights:
        issues.append("Missing cross-domain synthesis")
    if req.second_order_patterns and not summary.second_order_patterns:
        issues.append("Missing second-order patterns")
    if req.adversarial_review and not summary.adversarial_reviews:
        issues.append("Missing adversarial reviews")
    if req.complete_mapping and not summary.unexplored_regions:
        issues.append("Missing unexplored regions documentation")

    return {
        'valid': len(issues) == 0,
        'issues': issues,
        'depth': summary.depth_level,
        'requirements': req
    }


def main():
    """CLI for resumable ARAW protocol"""
    import argparse

    parser = argparse.ArgumentParser(description="Resumable ARAW Protocol")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Start command
    start_parser = subparsers.add_parser('start', help='Start new session')
    start_parser.add_argument('claim', help='Root claim')
    start_parser.add_argument('--session-id', help='Session identifier')
    start_parser.add_argument('--depth', default='8x', choices=['1x', '2x', '3x', '4x', '8x', '16x', '32x'],
                              help='ARAW depth level')
    start_parser.add_argument('--total-sessions', type=int, default=1,
                              help='Planned total sessions for multi-session ARAW')

    # Pause command
    pause_parser = subparsers.add_parser('pause', help='Pause session')
    pause_parser.add_argument('db', help='Database file')
    pause_parser.add_argument('summary', help='Summary output file')
    pause_parser.add_argument('--claim', help='Root claim (for new sessions)')
    pause_parser.add_argument('--depth', default='8x', help='ARAW depth level')
    pause_parser.add_argument('--session-number', type=int, default=1, help='Current session number')
    pause_parser.add_argument('--total-sessions', type=int, default=1, help='Total planned sessions')

    # Resume command
    resume_parser = subparsers.add_parser('resume', help='Resume session')
    resume_parser.add_argument('summary', help='Summary file to resume from')
    resume_parser.add_argument('--db', help='Database to inject context into')

    # Synthesize command
    synth_parser = subparsers.add_parser('synthesize', help='Synthesize results')
    synth_parser.add_argument('db', help='Database file')
    synth_parser.add_argument('--summaries', nargs='+', help='Summary files to include')

    # Validate command (NEW)
    validate_parser = subparsers.add_parser('validate', help='Validate session meets depth requirements')
    validate_parser.add_argument('summary', help='Summary file to validate')

    # Requirements command (NEW)
    req_parser = subparsers.add_parser('requirements', help='Show depth requirements')
    req_parser.add_argument('--depth', help='Show requirements for specific depth')

    args = parser.parse_args()

    if args.command == 'start':
        session = ResumableARAW.start(args.claim, args.session_id)
        session.depth_level = args.depth
        session.total_sessions_planned = args.total_sessions
        print(f"Started session: {session.session_id}")
        print(f"Root claim: {session.root_claim}")
        print(f"Depth: {args.depth}")
        if args.depth in ('16x', '32x'):
            req = DEPTH_REQUIREMENTS[args.depth]
            print(f"\n{args.depth} Requirements:")
            print(f"  Claims: {req.claims}")
            print(f"  Levels: {req.levels}")
            print(f"  CRUX: {req.crux_points}")
            print(f"  DO_FIRST: {req.do_first_actions}")
            print(f"  Lines: {req.min_lines}-{req.max_lines}")
            if req.cross_domain_synthesis:
                print("  Cross-domain synthesis: Required")
            if req.adversarial_review:
                print("  Adversarial review: Required")

    elif args.command == 'pause':
        session = ResumableARAW.start(args.claim or "unknown", "pausing")
        summary = session.pause(Path(args.db), Path(args.summary))
        print(f"Paused session with {summary.total_nodes} nodes")
        print(f"Frontier nodes: {summary.frontier_count}")
        print(f"Foundational claims: {len(summary.foundational_claims)}")
        print(f"Saved to: {args.summary}")

    elif args.command == 'resume':
        session, context = ResumableARAW.resume(Path(args.summary), Path(args.db) if args.db else Path('/dev/null'))
        print(f"Resuming: {session.session_id}")
        print(f"Root claim: {session.root_claim}")
        print(f"Context nodes to inject: {len(context.nodes)}")

        if args.db:
            from context_loader import ContextLoader
            loader = ContextLoader()
            count = loader.inject_into_db(context, Path(args.db))
            print(f"Injected {count} nodes into {args.db}")

    elif args.command == 'synthesize':
        session = ResumableARAW.start("synthesis", "synth")

        if args.summaries:
            for summary_path in args.summaries:
                data = json.loads(Path(summary_path).read_text())
                session.summaries.append(SessionSummary(**data))

        results = session.synthesize(Path(args.db))
        print(json.dumps(results, indent=2))

    elif args.command == 'validate':
        data = json.loads(Path(args.summary).read_text())
        summary = SessionSummary(**data)
        result = validate_depth_requirements(summary)

        print(f"Validating {summary.depth_level} ARAW session...")
        print(f"Session: {summary.session_id}")
        print(f"Progress: Session {summary.session_number} of {summary.total_sessions_planned}")
        print()

        if result['valid']:
            print("✓ Session meets depth requirements")
        else:
            print("✗ Session does NOT meet depth requirements:")
            for issue in result['issues']:
                print(f"  - {issue}")

    elif args.command == 'requirements':
        if args.depth:
            depths = [args.depth] if args.depth in DEPTH_REQUIREMENTS else []
        else:
            depths = list(DEPTH_REQUIREMENTS.keys())

        for depth in depths:
            req = DEPTH_REQUIREMENTS[depth]
            print(f"\n{depth} Requirements:")
            print(f"  Claims: {req.claims}")
            print(f"  Levels: {req.levels}")
            print(f"  CRUX points: {req.crux_points}")
            print(f"  DO_FIRST actions: {req.do_first_actions}")
            print(f"  Lines: {req.min_lines}-{req.max_lines}")
            print(f"  Unconventional quota: {req.unconventional_quota}")
            if req.cross_domain_synthesis:
                print("  Cross-domain synthesis: Required")
            if req.second_order_patterns:
                print("  Second-order patterns: Required")
            if req.adversarial_review:
                print("  Adversarial review: Required")
            if req.external_references:
                print("  External references: Required")
            if req.complete_mapping:
                print("  Complete mapping: Required")


if __name__ == "__main__":
    main()
