"""
ARAW → Goal Journey Field Mapper

Extracts Goal Journey structure from completed ARAW sessions.

Goal Journey Fields:
- Current state: Where user is now
- Desired state: Where user wants to be
- Immediate goal: Next actionable target
- Serves: What higher goal this serves
- Intrinsic goal: Terminal value (valued for itself)
- Why now: Temporal urgency/importance
- Success criteria: How to know it worked
- Constraints: Limitations and boundaries

Mapping from ARAW:
- Root claim → Desired state (often)
- Claims → Can contain current state, constraints
- AR branches → What follows if true → Success criteria, Serves
- AW branches → Alternatives, constraints, why not
- CRUX points → Key uncertainties, may indicate Why now
- DO_FIRST → Immediate goal candidates
- Commitment status → Confidence in mappings
"""

import json
import re
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple


@dataclass
class GoalJourneyField:
    """A field in the Goal Journey structure"""
    name: str
    value: str
    confidence: str  # 'high', 'medium', 'low'
    source: str  # Where this was extracted from
    is_guess: bool = True  # Per GOSM: all items are marked as GUESSES


@dataclass
class GoalJourney:
    """Complete Goal Journey structure"""
    current_state: Optional[GoalJourneyField] = None
    desired_state: Optional[GoalJourneyField] = None
    immediate_goal: Optional[GoalJourneyField] = None
    serves: List[GoalJourneyField] = field(default_factory=list)  # Chain of goals
    intrinsic_goal: Optional[GoalJourneyField] = None
    why_now: Optional[GoalJourneyField] = None
    success_criteria: List[GoalJourneyField] = field(default_factory=list)
    constraints: List[GoalJourneyField] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        def field_to_dict(f: Optional[GoalJourneyField]) -> Optional[Dict]:
            if f is None:
                return None
            return {
                'value': f.value,
                'confidence': f.confidence,
                'source': f.source,
                'is_guess': f.is_guess
            }

        return {
            'current_state': field_to_dict(self.current_state),
            'desired_state': field_to_dict(self.desired_state),
            'immediate_goal': field_to_dict(self.immediate_goal),
            'serves': [field_to_dict(f) for f in self.serves],
            'intrinsic_goal': field_to_dict(self.intrinsic_goal),
            'why_now': field_to_dict(self.why_now),
            'success_criteria': [field_to_dict(f) for f in self.success_criteria],
            'constraints': [field_to_dict(f) for f in self.constraints]
        }

    def to_markdown(self) -> str:
        """Format as markdown"""
        lines = ["## Goal Journey\n"]

        def add_field(name: str, f: Optional[GoalJourneyField]):
            if f:
                conf_marker = {'high': '', 'medium': ' [?]', 'low': ' [??]'}[f.confidence]
                guess_marker = ' [GUESS]' if f.is_guess else ''
                lines.append(f"**{name}**: {f.value}{conf_marker}{guess_marker}")
                lines.append(f"  - Source: {f.source}")
                lines.append("")

        add_field("Current State", self.current_state)
        add_field("Desired State", self.desired_state)
        add_field("Immediate Goal", self.immediate_goal)

        if self.serves:
            lines.append("**Serves (Goal Chain)**:")
            for i, f in enumerate(self.serves, 1):
                lines.append(f"  {i}. {f.value} (→ serves next)")
            lines.append("")

        add_field("Intrinsic Goal", self.intrinsic_goal)
        add_field("Why Now", self.why_now)

        if self.success_criteria:
            lines.append("**Success Criteria**:")
            for f in self.success_criteria:
                lines.append(f"  - {f.value}")
            lines.append("")

        if self.constraints:
            lines.append("**Constraints**:")
            for f in self.constraints:
                lines.append(f"  - {f.value}")
            lines.append("")

        return "\n".join(lines)


class GoalJourneyMapper:
    """
    Maps ARAW session outputs to Goal Journey structure.

    Works with both:
    - SQLite databases (from auto_expand_llm.py)
    - Markdown files (from conversational ARAW)
    """

    def __init__(self):
        self.journey = GoalJourney()

    def map_from_sqlite(self, db_path: Path) -> GoalJourney:
        """Extract Goal Journey from SQLite ARAW database"""
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row

        # Get root claim
        cursor = conn.execute(
            "SELECT claim FROM nodes WHERE parent_id IS NULL LIMIT 1"
        )
        row = cursor.fetchone()
        if row:
            self._extract_desired_state(row['claim'], 'root_claim')

        # Get all claims for analysis
        cursor = conn.execute("""
            SELECT n.claim, n.branch_type, n.depth, n.leverage_score, n.commitment_status,
                   p.claim as parent_claim
            FROM nodes n
            LEFT JOIN nodes p ON n.parent_id = p.id
            ORDER BY n.depth, n.id
        """)

        for row in cursor:
            self._analyze_node(
                claim=row['claim'],
                branch_type=row['branch_type'],
                depth=row['depth'],
                leverage_score=row['leverage_score'],
                commitment_status=row['commitment_status'],
                parent_claim=row['parent_claim']
            )

        # Get metadata (tensions, crux points)
        cursor = conn.execute("SELECT key, value FROM metadata")
        for row in cursor:
            if row['key'] == 'crux_points':
                crux_points = json.loads(row['value'])
                self._extract_from_crux(crux_points)

        conn.close()
        return self.journey

    def map_from_markdown(self, md_path: Path) -> GoalJourney:
        """Extract Goal Journey from markdown ARAW session"""
        content = md_path.read_text()

        # Extract root claim from topic
        topic_match = re.search(r'topic:\s*(.+)', content)
        if topic_match:
            self._extract_desired_state(topic_match.group(1).strip(), 'frontmatter')

        # Extract claims table
        self._extract_claims_from_table(content)

        # Extract DO_FIRST actions → immediate goals
        self._extract_do_first(content)

        # Extract CRUX points
        self._extract_crux_from_markdown(content)

        # Extract constraints from AW branches
        self._extract_constraints_from_aw(content)

        # Extract success criteria from AR branches
        self._extract_success_from_ar(content)

        return self.journey

    def _extract_desired_state(self, claim: str, source: str):
        """Root claim often represents desired state"""
        # Clean up claim
        claim = claim.strip('"\'')

        # Check if it's a goal statement
        goal_patterns = [
            r'^I want', r'^I need', r'^achieve', r'^get', r'^become',
            r'^build', r'^create', r'^should I'
        ]

        confidence = 'medium'
        for pattern in goal_patterns:
            if re.search(pattern, claim, re.IGNORECASE):
                confidence = 'high'
                break

        self.journey.desired_state = GoalJourneyField(
            name='desired_state',
            value=claim,
            confidence=confidence,
            source=source
        )

    def _analyze_node(
        self,
        claim: str,
        branch_type: str,
        depth: int,
        leverage_score: float,
        commitment_status: Optional[str],
        parent_claim: Optional[str]
    ):
        """Analyze a single node for Goal Journey mapping"""

        # ASSUME WRONG branches often contain constraints
        if branch_type == 'assume_wrong':
            if any(kw in claim.lower() for kw in ['cannot', "can't", 'impossible', 'limited', 'constraint', 'blocker']):
                self.journey.constraints.append(GoalJourneyField(
                    name='constraint',
                    value=claim,
                    confidence='medium',
                    source=f'aw_branch_depth_{depth}'
                ))

        # ASSUME RIGHT branches often contain success criteria
        if branch_type == 'assume_right':
            if any(kw in claim.lower() for kw in ['success', 'achieve', 'result', 'outcome', 'then']):
                self.journey.success_criteria.append(GoalJourneyField(
                    name='success_criterion',
                    value=claim,
                    confidence='medium',
                    source=f'ar_branch_depth_{depth}'
                ))

        # High leverage + foundational → potentially intrinsic goal
        if leverage_score > 0.8 and commitment_status == 'foundational':
            if any(kw in claim.lower() for kw in ['value', 'meaning', 'purpose', 'fulfillment', 'happiness', 'freedom']):
                self.journey.intrinsic_goal = GoalJourneyField(
                    name='intrinsic_goal',
                    value=claim,
                    confidence='medium',
                    source=f'foundational_high_leverage'
                )

        # Track serves chain
        if parent_claim and branch_type == 'assume_right':
            self.journey.serves.append(GoalJourneyField(
                name='serves',
                value=f"{claim} → serves → {parent_claim}",
                confidence='low',
                source=f'ar_chain_depth_{depth}'
            ))

    def _extract_claims_from_table(self, content: str):
        """Extract claims from markdown claims table"""
        # Find claims marked HIGH importance
        table_pattern = r'\|\s*\d+\s*\|([^|]+)\|[^|]*\|[^|]*HIGH[^|]*\|'

        for match in re.finditer(table_pattern, content, re.IGNORECASE):
            claim = match.group(1).strip().strip('"')

            # Check for current state indicators
            if any(kw in claim.lower() for kw in ['currently', 'right now', 'at present', 'is currently']):
                self.journey.current_state = GoalJourneyField(
                    name='current_state',
                    value=claim,
                    confidence='medium',
                    source='claims_table'
                )

    def _extract_do_first(self, content: str):
        """Extract DO_FIRST actions as immediate goals"""
        do_first_pattern = r'DO_FIRST\s*\d*[:\s]+([^\n]+)'

        for match in re.finditer(do_first_pattern, content):
            action = match.group(1).strip()

            # First DO_FIRST becomes immediate goal
            if self.journey.immediate_goal is None:
                self.journey.immediate_goal = GoalJourneyField(
                    name='immediate_goal',
                    value=action,
                    confidence='high',
                    source='do_first_1'
                )

    def _extract_crux_from_markdown(self, content: str):
        """Extract CRUX points for timing/urgency"""
        crux_pattern = r'CRUX[^:]*:\s*([^\n]+)'

        for match in re.finditer(crux_pattern, content):
            crux = match.group(1).strip()

            # Check for timing indicators
            if any(kw in crux.lower() for kw in ['when', 'timing', 'urgent', 'deadline', 'now', 'before']):
                self.journey.why_now = GoalJourneyField(
                    name='why_now',
                    value=crux,
                    confidence='medium',
                    source='crux_point'
                )
                break

    def _extract_from_crux(self, crux_points: List[Tuple[str, str]]):
        """Extract from structured CRUX points"""
        for title, question in crux_points:
            if any(kw in title.lower() for kw in ['when', 'timing', 'urgent', 'deadline']):
                self.journey.why_now = GoalJourneyField(
                    name='why_now',
                    value=f"{title}: {question}",
                    confidence='medium',
                    source='crux_points_metadata'
                )

    def _extract_constraints_from_aw(self, content: str):
        """Extract constraints from ASSUME WRONG sections"""
        aw_pattern = r'ASSUME WRONG[^→]*→([^\n]+)'

        for match in re.finditer(aw_pattern, content):
            aw_text = match.group(1).strip()

            if any(kw in aw_text.lower() for kw in ['cannot', "can't", 'impossible', 'limited', 'blocker', 'risk']):
                self.journey.constraints.append(GoalJourneyField(
                    name='constraint',
                    value=aw_text,
                    confidence='medium',
                    source='aw_branch'
                ))

    def _extract_success_from_ar(self, content: str):
        """Extract success criteria from ASSUME RIGHT sections"""
        ar_pattern = r'ASSUME RIGHT[^→]*→([^\n]+)'

        for match in re.finditer(ar_pattern, content):
            ar_text = match.group(1).strip()

            if any(kw in ar_text.lower() for kw in ['success', 'achieve', 'result', 'then', 'works', 'validated']):
                self.journey.success_criteria.append(GoalJourneyField(
                    name='success_criterion',
                    value=ar_text,
                    confidence='medium',
                    source='ar_branch'
                ))


def main():
    """CLI for testing Goal Journey mapping"""
    import argparse

    parser = argparse.ArgumentParser(description="ARAW → Goal Journey Mapper")
    parser.add_argument("input", help="ARAW session file (.db or .md)")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    parser.add_argument("--format", choices=['json', 'markdown'], default='markdown')

    args = parser.parse_args()

    input_path = Path(args.input)
    mapper = GoalJourneyMapper()

    if input_path.suffix == '.db':
        journey = mapper.map_from_sqlite(input_path)
    else:
        journey = mapper.map_from_markdown(input_path)

    if args.format == 'json':
        output = json.dumps(journey.to_dict(), indent=2)
    else:
        output = journey.to_markdown()

    if args.output:
        Path(args.output).write_text(output)
        print(f"Wrote Goal Journey to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
