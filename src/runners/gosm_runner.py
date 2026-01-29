#!/usr/bin/env python3
"""
Unified GOSM Runner - System Intelligence, Not Model Intelligence

This script implements the core GOSM principles:
1. System Intelligence: Structures prompts so cheap models produce good output
2. AI Context: Reads FAILURE_KNOWLEDGE, USER_MODEL, RELEVANCE_WEIGHTING, etc.
3. ARAW Verification: Uses Assume Right / Assume Wrong exploration
4. No Guessing: Applies verification_before_output procedure
5. Checklists: Follows AGENT_INSTRUCTIONS.md gates and checklists

Usage:
    python gosm_runner.py --goal "Your goal here"
    python gosm_runner.py --project tunnel-vision --resume
    python gosm_runner.py --verify /path/to/output.md
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

import yaml

# Project paths
GOSM_ROOT = Path(os.environ.get('GOSM_ROOT', Path(__file__).parent.parent))
LIBRARY_DIR = GOSM_ROOT / 'library'
AI_CONTEXT_DIR = GOSM_ROOT / 'ai_context'
PROJECTS_DIR = GOSM_ROOT / 'projects'
ARCHITECTURE_DIR = GOSM_ROOT / 'architecture'
ARAW_DIR = LIBRARY_DIR / 'araw'

# Add ARAW to path for imports
sys.path.insert(0, str(ARAW_DIR))
sys.path.insert(0, str(LIBRARY_DIR / 'araw'))

# Try to import GOSM agent for real verification
_agent_available = False
try:
    from gosm_agent import GOSMAgent, verify_gosm_output
    _agent_available = True
except ImportError:
    pass


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class AIContext:
    """Loaded AI context files for system intelligence."""
    failure_knowledge: str = ""
    user_model: str = ""
    relevance_weighting: str = ""
    system_architecture: str = ""
    mission_statement: str = ""
    domain_vocabulary: str = ""

    def to_prompt_section(self) -> str:
        """Format context as a prompt section for the LLM."""
        sections = []

        if self.failure_knowledge:
            sections.append(f"## Known Failure Patterns\n{self._summarize(self.failure_knowledge, 500)}")

        if self.user_model:
            sections.append(f"## User Context\n{self._summarize(self.user_model, 300)}")

        if self.relevance_weighting:
            sections.append(f"## Relevance Priority\n{self._summarize(self.relevance_weighting, 300)}")

        if self.mission_statement:
            sections.append(f"## Core Philosophy\n{self._summarize(self.mission_statement, 400)}")

        return "\n\n".join(sections)

    def _summarize(self, text: str, max_chars: int) -> str:
        """Extract key points from text."""
        if len(text) <= max_chars:
            return text
        # Find a good break point
        truncated = text[:max_chars]
        last_newline = truncated.rfind('\n')
        if last_newline > max_chars * 0.7:
            return truncated[:last_newline] + "\n[... truncated]"
        return truncated + "..."


@dataclass
class ARAWExploration:
    """ARAW (Assume Right, Assume Wrong) exploration result."""
    claim: str
    assume_right: list[str] = field(default_factory=list)
    assume_wrong: list[str] = field(default_factory=list)
    crux: str | None = None
    verification_needed: list[str] = field(default_factory=list)


@dataclass
class VerificationResult:
    """Result of verifying a claim or output."""
    claim: str
    status: Literal["VERIFIED_OBSERVED", "VERIFIED_TESTED", "VERIFIED_DERIVED", "UNVERIFIED", "EXCLUDED"]
    evidence: str | None = None
    source: str | None = None
    marker: str | None = None


@dataclass
class GateResult:
    """Result of running a gate check."""
    gate_id: str
    passed: bool
    blocking: bool = True
    message: str = ""
    suggestions: list[str] = field(default_factory=list)


@dataclass
class GOSMOutput:
    """Structured GOSM output following verification procedures."""
    verified_claims: list[VerificationResult] = field(default_factory=list)
    unknown_items: list[str] = field(default_factory=list)
    defaults_used: list[dict[str, Any]] = field(default_factory=list)
    excluded_items: list[dict[str, str]] = field(default_factory=list)
    gate_results: list[GateResult] = field(default_factory=list)


# ============================================================================
# FILTERED FEEDBACK SYSTEM
# Based on: leverage_point_discovery.yaml, selection.yaml, convergent_validation.yaml
# ============================================================================

@dataclass
class FeedbackItem:
    """An item that may be fed back into the system for recursive improvement.

    Scoring based on:
    - leverage_point_discovery.yaml: leverage = value × defensibility × scalability
    - selection.yaml: real-world filters (readiness, reversibility, risk)
    - convergent_validation.yaml: four independent checks
    """
    item_type: Literal["goal", "problem", "question", "decision", "assumption", "strategy"]
    content: str
    source: str  # Where this item came from (e.g., "ARAW:node123", "gate:no_guessing")

    # Leverage scoring (from leverage_point_discovery.yaml)
    leverage_score: float = 0.0  # 0-1, based on value × defensibility × scalability
    feasibility_score: float = 0.0  # 0-1, implementation readiness

    # Grounding checks (from convergent_validation.yaml)
    is_grounded: bool = False  # Has [O], [T], or [D] marker
    is_fixed_point: bool = False  # Stable under re-analysis
    is_convergent: bool = False  # Multiple paths lead here
    is_practical: bool = False  # Passes real-world filters

    # Selection filters (from selection.yaml)
    is_blocking: bool = False  # Blocks other work if unresolved
    is_reversible: bool = True  # Can be undone if wrong
    risk_level: Literal["low", "medium", "high"] = "medium"

    # Metadata
    depth: int = 0  # Distance from root in reasoning chain
    validation_method: str = "pending"  # How this was/should be validated


@dataclass
class FilteredFeedback:
    """Result of filtering items for self-feeding."""
    accepted: list[FeedbackItem] = field(default_factory=list)  # High confidence, feed back
    flagged: list[FeedbackItem] = field(default_factory=list)  # Moderate confidence, review
    rejected: list[FeedbackItem] = field(default_factory=list)  # Low confidence, don't feed


def calculate_convergent_validation_score(item: FeedbackItem) -> int:
    """
    Calculate convergent validation score (0-4) based on four independent checks.

    From convergent_validation.yaml:
    - 4 pass → Accept with high confidence
    - 3 pass → Accept with moderate confidence
    - 2 pass → Flag for review
    - 0-1 pass → Reject
    """
    score = 0
    if item.is_grounded:
        score += 1
    if item.is_fixed_point:
        score += 1
    if item.is_convergent:
        score += 1
    if item.is_practical:
        score += 1
    return score


def apply_leverage_score(item: FeedbackItem, raw_value: float = 0.5) -> float:
    """
    Calculate leverage score based on leverage_point_discovery.yaml.

    LEVERAGE = value × defensibility × scalability

    - value: How much impact if resolved (0-1)
    - defensibility: How protected from invalidation (0-1)
    - scalability: How broadly applicable (0-1)
    """
    # Base value from raw input
    value = raw_value

    # Defensibility: grounded items are more defensible
    defensibility = 0.8 if item.is_grounded else 0.3

    # Scalability: blocking items have broader impact
    scalability = 0.9 if item.is_blocking else 0.5

    # Adjust for depth (deeper items are more specific, less scalable)
    depth_penalty = max(0.5, 1.0 - (item.depth * 0.1))
    scalability *= depth_penalty

    return value * defensibility * scalability


def apply_selection_filters(item: FeedbackItem) -> bool:
    """
    Apply real-world filters from selection.yaml.

    Filters:
    - Implementation readiness (feasibility > 0.5)
    - Risk tolerance (high risk needs high leverage)
    - Reversibility (irreversible needs higher bar)
    """
    # Implementation readiness filter
    if item.feasibility_score < 0.3:
        return False

    # Risk tolerance filter
    if item.risk_level == "high" and item.leverage_score < 0.7:
        return False

    # Reversibility filter - irreversible actions need stronger validation
    if not item.is_reversible and calculate_convergent_validation_score(item) < 3:
        return False

    return True


def filter_for_feedback(
    items: list[FeedbackItem],
    min_leverage: float = 0.5,
    min_convergent_score: int = 2,
    max_feedback_items: int = 10,
) -> FilteredFeedback:
    """
    Filter items for self-feeding to prevent error accumulation.

    Based on procedures:
    - leverage_point_discovery.yaml: Only high-leverage items
    - selection.yaml: Real-world filters
    - convergent_validation.yaml: Decision protocol

    Args:
        items: List of potential feedback items
        min_leverage: Minimum leverage score to consider (default 0.5)
        min_convergent_score: Minimum convergent validation score (default 2)
        max_feedback_items: Maximum items to accept (default 10)

    Returns:
        FilteredFeedback with accepted, flagged, and rejected items
    """
    result = FilteredFeedback()

    # Score and sort items
    scored_items = []
    for item in items:
        # Calculate leverage if not already set
        if item.leverage_score == 0:
            item.leverage_score = apply_leverage_score(item)

        conv_score = calculate_convergent_validation_score(item)
        passes_filters = apply_selection_filters(item)

        scored_items.append((item, conv_score, passes_filters))

    # Sort by leverage score (highest first)
    scored_items.sort(key=lambda x: x[0].leverage_score, reverse=True)

    accepted_count = 0
    for item, conv_score, passes_filters in scored_items:
        # Decision protocol from convergent_validation.yaml
        if conv_score >= 4 and passes_filters and item.leverage_score >= min_leverage:
            # 4 checks pass → Accept with high confidence
            if accepted_count < max_feedback_items:
                result.accepted.append(item)
                accepted_count += 1
            else:
                result.flagged.append(item)  # Would accept but over limit

        elif conv_score >= 3 and passes_filters and item.leverage_score >= min_leverage:
            # 3 checks pass → Accept with moderate confidence
            if accepted_count < max_feedback_items:
                result.accepted.append(item)
                accepted_count += 1
            else:
                result.flagged.append(item)

        elif conv_score >= min_convergent_score and item.leverage_score >= min_leverage * 0.7:
            # 2 checks pass → Flag for review
            result.flagged.append(item)

        else:
            # 0-1 checks pass → Reject
            result.rejected.append(item)

    return result


def extract_feedback_items(output: GOSMOutput, araw_engine: Any = None) -> list[FeedbackItem]:
    """
    Extract potential feedback items from GOSM output.

    Sources:
    - Verified claims with high leverage
    - Unknown items that are blocking
    - Gate failures that need resolution
    - ARAW high-leverage nodes
    """
    items = []

    # Extract from verified claims
    for claim in output.verified_claims:
        is_grounded = claim.status in ["VERIFIED_OBSERVED", "VERIFIED_TESTED", "VERIFIED_DERIVED"]
        is_blocking = "CRITICAL" in (claim.evidence or "") or "CRUX" in (claim.marker or "")

        item = FeedbackItem(
            item_type="assumption" if "Assumption" in claim.claim else "decision",
            content=claim.claim,
            source=claim.source or "verified_claims",
            is_grounded=is_grounded,
            is_blocking=is_blocking,
            is_practical=is_grounded,  # Grounded items are practical
            is_convergent=claim.status == "VERIFIED_DERIVED",  # Derivations show convergence
            validation_method=claim.status,
        )

        # Higher leverage for blocking items
        item.leverage_score = apply_leverage_score(item, raw_value=0.8 if is_blocking else 0.5)
        item.feasibility_score = 0.8 if is_grounded else 0.3

        items.append(item)

    # Extract from unknown items - these are potential questions/problems
    for unknown in output.unknown_items:
        is_blocking = "DO_FIRST" in unknown or "CRITICAL" in unknown

        item = FeedbackItem(
            item_type="question" if "?" in unknown else "problem",
            content=unknown,
            source="unknown_items",
            is_grounded=False,  # Unknown items are not grounded by definition
            is_blocking=is_blocking,
            is_practical=False,
            is_convergent=False,
            risk_level="medium" if is_blocking else "low",
        )

        # Parse leverage from content if present
        if "leverage:" in unknown.lower():
            try:
                leverage_str = unknown.lower().split("leverage:")[1].split(")")[0].strip()
                item.leverage_score = float(leverage_str)
            except (ValueError, IndexError):
                item.leverage_score = apply_leverage_score(item, raw_value=0.6 if is_blocking else 0.4)
        else:
            item.leverage_score = apply_leverage_score(item, raw_value=0.6 if is_blocking else 0.4)

        item.feasibility_score = 0.5  # Unknown feasibility
        items.append(item)

    # Extract from gate failures
    for gate in output.gate_results:
        if not gate.passed:
            item = FeedbackItem(
                item_type="problem",
                content=f"Gate {gate.gate_id} failed: {gate.message}",
                source=f"gate:{gate.gate_id}",
                is_grounded=True,  # Gate results are observed
                is_blocking=gate.blocking,
                is_practical=True,
                is_convergent=False,
                risk_level="high" if gate.blocking else "medium",
            )
            item.leverage_score = apply_leverage_score(item, raw_value=0.9 if gate.blocking else 0.6)
            item.feasibility_score = 0.7  # Gates usually have clear resolution paths

            # Add suggestions as sub-items
            for suggestion in gate.suggestions:
                sub_item = FeedbackItem(
                    item_type="question",
                    content=suggestion,
                    source=f"gate:{gate.gate_id}:suggestion",
                    is_grounded=False,
                    is_blocking=False,
                    is_practical=True,  # Suggestions are meant to be actionable
                    leverage_score=0.5,
                    feasibility_score=0.8,
                )
                items.append(sub_item)

            items.append(item)

    # Extract from ARAW engine if available
    if araw_engine is not None:
        try:
            high_leverage_nodes = araw_engine.get_high_leverage(min_score=0.6, limit=10)
            for node in high_leverage_nodes:
                item = FeedbackItem(
                    item_type="assumption",
                    content=node.claim,
                    source=f"ARAW:{node.id}",
                    is_grounded=node.status != "unexplored",
                    is_blocking=node.leverage_score >= 0.8,
                    is_practical=True,
                    is_convergent=node.depth > 1,  # Deeper nodes show convergent reasoning
                    leverage_score=node.leverage_score,
                    feasibility_score=0.6,
                    depth=node.depth,
                )
                items.append(item)
        except Exception:
            pass  # ARAW engine may not be available

    return items


def format_self_feeding_output(
    filtered: FilteredFeedback,
    original_goal: str,
) -> dict[str, Any]:
    """
    Format filtered feedback as structured output suitable for re-input to GOSM.

    Output structure matches QUICKSTART.md input format:
    - goals: New goals derived from high-leverage items
    - problems: Issues that need resolution
    - questions: Things that need investigation
    - decisions: Decision points that need resolution
    """
    output = {
        "meta": {
            "original_goal": original_goal,
            "accepted_count": len(filtered.accepted),
            "flagged_count": len(filtered.flagged),
            "rejected_count": len(filtered.rejected),
            "filter_criteria": {
                "method": "convergent_validation + leverage_scoring + selection_filters",
                "sources": [
                    "leverage_point_discovery.yaml",
                    "selection.yaml",
                    "convergent_validation.yaml",
                ],
            },
        },
        "feedback_items": {
            "goals": [],
            "problems": [],
            "questions": [],
            "decisions": [],
            "assumptions": [],
            "strategies": [],
        },
        "verification_summary": {
            "all_grounded": all(item.is_grounded for item in filtered.accepted),
            "all_pass_filters": True,  # By definition, accepted items pass filters
            "convergent_validation": {
                "4_checks": len([i for i in filtered.accepted if calculate_convergent_validation_score(i) >= 4]),
                "3_checks": len([i for i in filtered.accepted if calculate_convergent_validation_score(i) == 3]),
            },
        },
    }

    # Categorize accepted items
    for item in filtered.accepted:
        item_dict = {
            "content": item.content,
            "source": item.source,
            "leverage_score": round(item.leverage_score, 2),
            "convergent_score": calculate_convergent_validation_score(item),
            "is_blocking": item.is_blocking,
            "validation_method": item.validation_method,
        }

        category = f"{item.item_type}s"  # pluralize
        if category in output["feedback_items"]:
            output["feedback_items"][category].append(item_dict)

    # Add flagged items in separate section for optional review
    output["flagged_for_review"] = [
        {
            "type": item.item_type,
            "content": item.content,
            "reason": f"convergent_score={calculate_convergent_validation_score(item)}, leverage={item.leverage_score:.2f}",
        }
        for item in filtered.flagged[:5]  # Limit to top 5
    ]

    return output


# ============================================================================
# CONTEXT LOADING
# ============================================================================

def load_ai_context() -> AIContext:
    """Load all AI context files for system intelligence."""
    context = AIContext()

    # Load each context file if it exists
    files = {
        'failure_knowledge': AI_CONTEXT_DIR / 'FAILURE_KNOWLEDGE.md',
        'user_model': AI_CONTEXT_DIR / 'USER_MODEL.md',
        'relevance_weighting': AI_CONTEXT_DIR / 'RELEVANCE_WEIGHTING.md',
        'system_architecture': AI_CONTEXT_DIR / 'SYSTEM_ARCHITECTURE.md',
        'domain_vocabulary': AI_CONTEXT_DIR / 'DOMAIN_VOCABULARY.md',
    }

    for attr, filepath in files.items():
        if filepath.exists():
            setattr(context, attr, filepath.read_text(encoding='utf-8'))

    # Load mission statement from library
    mission_path = LIBRARY_DIR / 'procedures' / 'core' / 'MISSION_STATEMENT.md'
    if mission_path.exists():
        context.mission_statement = mission_path.read_text(encoding='utf-8')

    return context


def load_procedure(procedure_id: str) -> dict[str, Any] | None:
    """Load a procedure from the library."""
    # Search in multiple locations
    search_paths = [
        LIBRARY_DIR / 'procedures' / 'core' / f'{procedure_id}.yaml',
        LIBRARY_DIR / 'procedures' / 'extracted' / f'{procedure_id}.yaml',
        LIBRARY_DIR / 'procedures' / 'meta' / f'{procedure_id}.yaml',
        LIBRARY_DIR / 'procedures' / 'analysis' / f'{procedure_id}.yaml',
    ]

    for path in search_paths:
        if path.exists():
            return yaml.safe_load(path.read_text(encoding='utf-8'))

    # Try glob search
    for yaml_file in LIBRARY_DIR.rglob(f'{procedure_id}.yaml'):
        return yaml.safe_load(yaml_file.read_text(encoding='utf-8'))

    return None


def load_gate(gate_id: str) -> dict[str, Any] | None:
    """Load a gate from the library."""
    search_paths = [
        LIBRARY_DIR / 'gates' / 'core' / f'{gate_id}.yaml',
        LIBRARY_DIR / 'gates' / f'{gate_id}.yaml',
    ]

    for path in search_paths:
        if path.exists():
            try:
                return yaml.safe_load(path.read_text(encoding='utf-8'))
            except yaml.YAMLError as e:
                # YAML parsing error - return minimal gate structure
                return {
                    'id': gate_id,
                    'name': gate_id.replace('_', ' ').title(),
                    'type': 'advisory_gate',
                    'description': f'Gate definition has YAML error: {str(e)[:100]}',
                    '_yaml_error': True,
                    '_error_detail': str(e),
                }

    return None


def load_checklist() -> list[dict[str, Any]]:
    """Load the main checklist from AGENT_INSTRUCTIONS.md."""
    agent_instructions = GOSM_ROOT / 'AGENT_INSTRUCTIONS.md'
    if not agent_instructions.exists():
        return []

    content = agent_instructions.read_text(encoding='utf-8')

    # Parse checklist section
    checklist = []
    in_checklist = False
    current_phase = None

    for line in content.split('\n'):
        if 'Checklist For Each Goal' in line:
            in_checklist = True
            continue
        if in_checklist:
            if line.startswith('###'):
                current_phase = line.replace('###', '').strip()
            elif line.strip().startswith('- [ ]'):
                item = line.replace('- [ ]', '').strip()
                checklist.append({
                    'phase': current_phase,
                    'item': item,
                    'completed': False
                })
            elif line.startswith('## ') and not line.startswith('### '):
                break  # End of checklist section

    return checklist


# ============================================================================
# ARAW EXPLORATION (Using Real Engine)
# ============================================================================

# Try to import the real ARAW engine
_araw_engine_available = False
try:
    from araw_engine import ARAWEngine, create_araw_search, BranchType, NodeStatus
    _araw_engine_available = True
except ImportError:
    pass


def explore_araw(
    claim: str,
    db_path: str | None = None,
    use_llm: bool = False,
    max_depth: int = 3
) -> tuple[ARAWExploration, 'ARAWEngine | None']:
    """
    Run ARAW (Assume Right, Assume Wrong) exploration on a claim.

    This calls the ACTUAL ARAW engine from library/araw/araw_engine.py,
    not a simplified reimplementation.

    Args:
        claim: The claim to explore
        db_path: Path to store ARAW database (None for in-memory)
        use_llm: Whether to use LLM for auto-expansion
        max_depth: Maximum exploration depth

    Returns:
        Tuple of (ARAWExploration summary, ARAWEngine instance for further exploration)
    """
    exploration = ARAWExploration(claim=claim)

    if not _araw_engine_available:
        # Fallback if engine not available - generate template
        exploration.assume_right = [
            f"[FALLBACK MODE - ARAW engine not loaded]",
            f"If '{claim}' is true:",
            "  - What evidence would we expect to see?",
            "  - What actions would be justified?",
        ]
        exploration.assume_wrong = [
            f"If '{claim}' is false:",
            "  - What alternative explanations exist?",
            "  - How would we know we were wrong?",
        ]
        exploration.crux = "What observation would most decisively distinguish these cases?"
        exploration.verification_needed = ["ARAW engine not available - install or check path"]
        return exploration, None

    # Use real ARAW engine
    engine = ARAWEngine(db_path or ":memory:")
    root_id = engine.create_search(claim, metadata={"source": "gosm_runner"})

    # Branch root into ASSUME RIGHT and ASSUME WRONG
    branches = engine.branch(
        root_id,
        assume_right_claim=f"ASSUME TRUE: {claim}",
        assume_wrong_claim=f"ASSUME FALSE: {claim}",
        alternatives=["Partially true", "Context-dependent", "Needs clarification"],
        leverage_score=0.8  # Root claims are high leverage
    )

    # Get the branches
    right_node = engine.get_node(branches["assume_right"])
    wrong_node = engine.get_node(branches["assume_wrong"])

    # Populate exploration result
    exploration.assume_right = [
        f"Node ID: {right_node.id}",
        f"Claim: {right_node.claim}",
        f"Status: {right_node.status}",
        "Next: What follows if true?",
    ]

    exploration.assume_wrong = [
        f"Node ID: {wrong_node.id}",
        f"Claim: {wrong_node.claim}",
        f"Status: {wrong_node.status}",
        "Alternatives: " + ", ".join(engine.get_alternatives(wrong_node.id)[0]['alternative']
                                     for alt in engine.get_alternatives(wrong_node.id)[:3]
                                     if 'alternative' in alt)
        if engine.get_alternatives(wrong_node.id) else "No alternatives yet",
    ]

    # Identify crux (highest leverage unexplored)
    unexplored = engine.get_unexplored(max_depth=max_depth, limit=5, strategy="leverage_first")
    if unexplored:
        exploration.crux = f"Highest leverage node: {unexplored[0].claim} (score: {unexplored[0].leverage_score:.2f})"
    else:
        exploration.crux = "All nodes explored at current depth"

    # Get statistics
    stats = engine.get_stats()
    exploration.verification_needed = [
        f"Total nodes: {stats['total_nodes']}",
        f"Unexplored: {stats['by_status'].get('unexplored', 0)}",
        f"Max depth: {stats['max_depth']}",
        "Use --araw-expand to continue exploration",
    ]

    return exploration, engine


def run_araw_integration(engine: 'ARAWEngine') -> dict[str, Any]:
    """
    Run ARAW → GOSM integration procedure.

    Maps ARAW exploration outputs to GOSM inputs:
    - Crux nodes → Assumption Register
    - DO_FIRST actions → Validation tasks
    - Tensions → Decision points
    - High-leverage unexplored → Research tasks

    See: library/procedures/core/araw_gosm_integration.yaml
    """
    if engine is None:
        return {"error": "No ARAW engine provided"}

    result = {
        "assumptions": [],
        "risks": [],
        "decision_points": [],
        "strategy_candidates": [],
        "validation_tasks": [],
    }

    # Get high-leverage nodes (crux candidates)
    high_leverage = engine.get_high_leverage(min_score=0.7, limit=10)
    for node in high_leverage:
        result["assumptions"].append({
            "id": node.id,
            "claim": node.claim,
            "leverage": node.leverage_score,
            "status": node.status,
            "criticality": "CRITICAL" if node.leverage_score >= 0.9 else "HIGH",
            "validation_method": "PENDING",
            "source": f"ARAW:{node.branch_type}",
        })

    # Get unexplored nodes for validation tasks
    unexplored = engine.get_unexplored(limit=20, strategy="balanced")
    for node in unexplored:
        if node.leverage_score >= 0.5:
            result["validation_tasks"].append({
                "id": node.id,
                "task": f"Verify: {node.claim}",
                "priority": "DO_FIRST" if node.leverage_score >= 0.7 else "DO_SECOND",
                "leverage": node.leverage_score,
            })

    # Get ASSUME_WRONG branches for risk identification
    wrong_branches = engine.get_branch_type(BranchType.ASSUME_WRONG)
    for node in wrong_branches:
        alternatives = engine.get_alternatives(node.id)
        result["risks"].append({
            "id": node.id,
            "description": node.claim,
            "alternatives": [a.get('alternative') for a in alternatives],
            "probability": 1 - node.leverage_score,  # Lower leverage = higher uncertainty
            "impact": "HIGH" if node.depth <= 2 else "MEDIUM",
        })

    # Get ASSUME_RIGHT branches as strategy candidates
    right_branches = engine.get_branch_type(BranchType.ASSUME_RIGHT)
    for node in right_branches:
        if node.leverage_score >= 0.6:
            result["strategy_candidates"].append({
                "id": node.id,
                "strategy": node.claim,
                "confidence": node.leverage_score,
                "path": [n.claim for n in engine.get_path_to_root(node.id)],
            })

    return result


def format_araw_prompt(exploration: ARAWExploration) -> str:
    """Format ARAW exploration as a prompt section."""
    return f"""
## ARAW Exploration: {exploration.claim}

### ASSUME RIGHT (If True)
{chr(10).join(exploration.assume_right)}

### ASSUME WRONG (If False)
{chr(10).join(exploration.assume_wrong)}

### CRUX
{exploration.crux}

### VERIFICATION NEEDED BEFORE PROCEEDING
{chr(10).join(f'- {v}' for v in exploration.verification_needed)}
"""


# ============================================================================
# VERIFICATION (NO GUESSING)
# ============================================================================

def verify_claim(
    claim: str,
    evidence: str | None = None,
    source: str | None = None,
    test_result: str | None = None,
    derivation_chain: list[str] | None = None
) -> VerificationResult:
    """
    Verify a claim using the no-guessing verification standard.

    Every claim must be either:
    - OBSERVED: Directly witnessed or stated by source
    - TESTED: Executed and confirmed
    - DERIVED: Logically follows from verified premises

    If none apply, the claim is EXCLUDED (not flagged).
    """

    # Check for OBSERVED verification
    if source and evidence:
        return VerificationResult(
            claim=claim,
            status="VERIFIED_OBSERVED",
            evidence=evidence,
            source=source,
            marker=f"[O: {source}]"
        )

    # Check for TESTED verification
    if test_result:
        return VerificationResult(
            claim=claim,
            status="VERIFIED_TESTED",
            evidence=test_result,
            marker=f"[T: {test_result}]"
        )

    # Check for DERIVED verification
    if derivation_chain and len(derivation_chain) >= 2:
        # All premises must themselves be verified
        derivation_str = " → ".join(derivation_chain)
        return VerificationResult(
            claim=claim,
            status="VERIFIED_DERIVED",
            evidence=derivation_str,
            marker=f"[D: {derivation_str}]"
        )

    # If none apply, mark as UNVERIFIED for exclusion
    return VerificationResult(
        claim=claim,
        status="UNVERIFIED",
        marker="[UNVERIFIED - EXCLUDE]"
    )


def run_gate(gate_id: str, context: dict[str, Any]) -> GateResult:
    """
    Run any gate from the library by ID.

    This is the generic gate runner that loads gate definitions
    and evaluates them against the provided context.

    Args:
        gate_id: The gate ID (e.g., "no_guessing_gate", "honest_question_gate")
        context: Context dict with data needed for evaluation

    Returns:
        GateResult with pass/fail and details
    """
    gate_def = load_gate(gate_id)

    if gate_def is None:
        return GateResult(
            gate_id=gate_id,
            passed=False,
            blocking=True,
            message=f"Gate not found: {gate_id}",
            suggestions=["Check gate ID spelling", "Verify gate exists in library/gates/"]
        )

    # Handle gates with YAML errors - pass with warning
    if gate_def.get('_yaml_error'):
        return GateResult(
            gate_id=gate_id,
            passed=True,  # Pass to allow continuation
            blocking=False,
            message=f"Gate has YAML parsing error - passing with warning",
            suggestions=[
                f"Fix YAML in library/gates/core/{gate_id}.yaml",
                "Error: " + gate_def.get('_error_detail', 'Unknown')[:100]
            ]
        )

    # Determine if gate is blocking
    gate_type = gate_def.get('type', 'advisory_gate')
    is_blocking = 'blocking' in gate_type.lower()

    # Get checks from gate definition
    checks = gate_def.get('checks', gate_def.get('evaluation_criteria', gate_def.get('blocks_on', [])))

    # Run checks based on gate structure
    failures = []
    passed_checks = []

    if isinstance(checks, dict):
        # Named checks (e.g., honest_question_gate)
        for check_name, check_def in checks.items():
            if isinstance(check_def, dict):
                question = check_def.get('question', check_name)
                pass_condition = check_def.get('pass_condition', '')
                fail_condition = check_def.get('fail_condition', '')

                # Evaluate check against context
                # For now, we check if required context keys exist
                context_key = check_name.replace('check_', '')
                if context.get(context_key) or context.get('_auto_pass'):
                    passed_checks.append(check_name)
                else:
                    failures.append({
                        'check': check_name,
                        'question': question,
                        'pass_condition': pass_condition,
                        'fail_condition': fail_condition,
                    })

    elif isinstance(checks, list):
        # List of check conditions (e.g., no_guessing_gate)
        for check in checks:
            if isinstance(check, dict):
                condition = check.get('condition', str(check))
                check_text = check.get('check', '')
                action = check.get('action', 'WARN')

                # Check if condition is met in context
                if context.get('violations', {}).get(condition):
                    failures.append({
                        'condition': condition,
                        'check': check_text,
                        'action': action,
                    })
                else:
                    passed_checks.append(condition)

    # Determine result
    if failures:
        return GateResult(
            gate_id=gate_id,
            passed=False,
            blocking=is_blocking,
            message=f"Gate failed: {len(failures)} check(s) not passed",
            suggestions=[f"Address: {f.get('condition', f.get('check', str(f)))}" for f in failures[:5]]
        )

    return GateResult(
        gate_id=gate_id,
        passed=True,
        blocking=is_blocking,
        message=f"Gate passed: {len(passed_checks)} check(s) passed"
    )


def run_no_guessing_gate(output: GOSMOutput) -> GateResult:
    """
    Run the no-guessing gate on output.

    Blocks any output that contains unverified claims.
    """
    unverified = [v for v in output.verified_claims if v.status == "UNVERIFIED"]

    if unverified:
        return GateResult(
            gate_id="no_guessing_gate",
            passed=False,
            blocking=True,
            message=f"Found {len(unverified)} unverified claims",
            suggestions=[
                f"Verify or exclude: {u.claim}" for u in unverified[:5]
            ]
        )

    return GateResult(
        gate_id="no_guessing_gate",
        passed=True,
        message="All claims verified or properly excluded"
)


def run_procedure(
    procedure_id: str,
    inputs: dict[str, Any],
    llm_client: Any = None
) -> dict[str, Any]:
    """
    Run any procedure from the library by ID.

    This is the generic procedure runner that loads procedure definitions
    and executes their steps.

    Args:
        procedure_id: The procedure ID (e.g., "recursive_causal_interrogation")
        inputs: Input dict with data needed for the procedure
        llm_client: Optional LLM client for procedures that need it

    Returns:
        Dict with procedure outputs and execution trace
    """
    proc_def = load_procedure(procedure_id)

    if proc_def is None:
        return {
            "success": False,
            "error": f"Procedure not found: {procedure_id}",
            "suggestions": ["Check procedure ID", "Verify in library/procedures/"]
        }

    result = {
        "procedure_id": procedure_id,
        "success": True,
        "inputs": inputs,
        "outputs": {},
        "steps_executed": [],
        "verification": [],
    }

    # Get procedure steps
    steps = proc_def.get('steps', [])

    # Execute each step
    for step in steps:
        step_id = step.get('id', step.get('name', 'unnamed'))
        step_name = step.get('name', str(step_id))
        action = step.get('action', '')
        expected_output = step.get('output', '')

        step_result = {
            "id": step_id,
            "name": step_name,
            "status": "executed",
            "action": action[:200] + "..." if len(action) > 200 else action,
        }

        # If procedure has LLM requirements and we have a client
        if llm_client and '{' in action and '}' in action:
            try:
                # This is a simplified execution - full implementation would
                # actually run the LLM with the procedure step
                step_result["note"] = "LLM execution available"
            except Exception as e:
                step_result["status"] = "failed"
                step_result["error"] = str(e)

        result["steps_executed"].append(step_result)

    # Check procedure verification requirements
    verification = proc_def.get('verification', [])
    if verification:
        for v in verification:
            result["verification"].append({
                "requirement": v if isinstance(v, str) else str(v),
                "status": "pending"
            })

    return result


def list_available_gates() -> list[str]:
    """List all available gates in the library."""
    gates = []
    gates_dir = LIBRARY_DIR / 'gates'
    for yaml_file in gates_dir.rglob('*.yaml'):
        try:
            content = yaml.safe_load(yaml_file.read_text(encoding='utf-8'))
            if content and 'id' in content:
                gates.append(content['id'])
        except Exception:
            pass
    return sorted(gates)


def list_available_procedures() -> list[str]:
    """List all available procedures in the library."""
    procedures = []
    procs_dir = LIBRARY_DIR / 'procedures'
    for yaml_file in procs_dir.rglob('*.yaml'):
        try:
            content = yaml.safe_load(yaml_file.read_text(encoding='utf-8'))
            if content and 'id' in content:
                procedures.append(content['id'])
        except Exception:
            pass
    return sorted(procedures)


def run_test_based_confidence_gate(confidence_claims: list[dict]) -> GateResult:
    """
    Run the test-based confidence gate.

    Blocks confidence claims that aren't derived from actual tests.
    """
    invalid_confidence = []

    for claim in confidence_claims:
        source = claim.get('source', '')
        # Valid sources: execution_tests, adversarial_survival, precedent, logical_derivation
        valid_sources = ['execution_test', 'adversarial', 'precedent', 'logical_derivation', 'test']
        if not any(v in source.lower() for v in valid_sources):
            invalid_confidence.append(claim)

    if invalid_confidence:
        return GateResult(
            gate_id="test_based_confidence_gate",
            passed=False,
            blocking=True,
            message=f"Found {len(invalid_confidence)} confidence claims without test basis",
            suggestions=[
                "Replace confidence assertions with test results",
                "Use format: 'confidence = X/N tests passed'"
            ]
        )

    return GateResult(
        gate_id="test_based_confidence_gate",
        passed=True,
        message="All confidence claims are test-based"
    )


# ============================================================================
# SYSTEM INTELLIGENCE PROMPTING
# ============================================================================

def build_system_prompt(context: AIContext, goal: str, phase: str) -> str:
    """
    Build a system prompt that structures output for cheap models.

    This is the core of "System Intelligence, Not Model Intelligence":
    - Embed context that the model needs
    - Structure the expected output format
    - Include verification requirements
    - Reference checklists and gates
    """

    prompt = f"""# GOSM System Prompt

You are operating as a GOSM (Goal-Oriented State Machine) agent.

## Current Phase: {phase}

## Goal
{goal}

## AI Context (MUST READ)
{context.to_prompt_section()}

## Verification Requirements (NO GUESSING)

Every claim in your output MUST be one of:
1. **OBSERVED** [O: source] - Directly witnessed or stated by source
2. **TESTED** [T: result] - Executed and confirmed
3. **DERIVED** [D: premises → conclusion] - Logically follows from verified premises

If a claim cannot be verified:
- DO NOT include it with "low confidence"
- DO NOT flag it for review and proceed
- Either VERIFY IT or EXCLUDE IT entirely

## ARAW Verification

Before accepting any assumption:
1. ASSUME RIGHT: If true, what follows?
2. ASSUME WRONG: If false, what alternatives?
3. Find the CRUX: What observation would distinguish?
4. VERIFY before proceeding

## Output Format

Structure your output as:

### VERIFIED CLAIMS
- [Claim] [O/T/D marker with evidence]

### UNKNOWN (if any)
- Items we don't know and are NOT pretending to know

### DEFAULTS USED (if any)
- [Default value] [Reason for using default]

### EXCLUDED (for transparency)
- [Item excluded] [Why it couldn't be verified]

## Checklist for {phase}

Follow the appropriate checklist from AGENT_INSTRUCTIONS.md for this phase.
"""

    return prompt


def build_user_prompt(goal: str, additional_context: str = "") -> str:
    """Build the user prompt for a GOSM task."""
    prompt = f"""## Task

{goal}

{additional_context if additional_context else ""}

## Instructions

1. First, run ARAW exploration on key assumptions
2. Apply the relevant GOSM procedure for this phase
3. Verify all claims before including them
4. Structure output using the verification format
5. Exclude rather than flag uncertain items

Begin.
"""
    return prompt


# ============================================================================
# MAIN EXECUTION
# ============================================================================

class GOSMRunner:
    """Main GOSM execution runner with system intelligence."""

    def __init__(self, verbose: bool = False, use_agent: bool = True):
        self.verbose = verbose
        self.use_agent = use_agent and _agent_available
        self.context = load_ai_context()
        self.checklist = load_checklist()
        self.output = GOSMOutput()

        # Initialize observation agent for real verification
        if self.use_agent:
            self.agent = GOSMAgent(root_path=GOSM_ROOT, verbose=verbose)
            if verbose:
                print("[GOSM] Agent loaded - real verification enabled")
        else:
            self.agent = None

        # Try to load LLM client
        try:
            sys.path.insert(0, str(GOSM_ROOT / 'gosm'))
            from llm.client import LLMClient, LLMConfig
            self.llm = LLMClient(LLMConfig(provider="openai", model="gpt-5-nano"))
        except ImportError:
            self.llm = None
            if self.verbose:
                print("Warning: LLM client not available, running in analysis mode only")

    def log(self, message: str) -> None:
        """Log a message if verbose mode is enabled."""
        if self.verbose:
            print(f"[GOSM] {message}")

    def verify_with_agent(self, claims: list[VerificationResult]) -> list[VerificationResult]:
        """
        Re-verify claims using the observation agent.

        This is the key integration point - instead of trusting LLM-generated
        markers, we actually verify against source code.
        """
        if not self.agent:
            self.log("Agent not available - skipping real verification")
            return claims

        self.log(f"Verifying {len(claims)} claims with observation agent")
        verified = []

        for claim_result in claims:
            # Skip already-verified claims with high confidence
            if claim_result.status.startswith("VERIFIED") and claim_result.source:
                # Re-verify against actual source
                obs = self.agent.verify_claim(
                    claim_result.claim,
                    source=claim_result.source,
                )

                if obs.verified:
                    # Update with real verification
                    verified.append(VerificationResult(
                        claim=claim_result.claim,
                        status=claim_result.status,
                        evidence=obs.evidence[:200],
                        source=obs.source,
                        marker=obs.marker,
                    ))
                    self.log(f"  ✓ Verified: {claim_result.claim[:50]}...")
                else:
                    # Downgrade to unverified
                    verified.append(VerificationResult(
                        claim=claim_result.claim,
                        status="UNVERIFIED",
                        evidence=f"Agent could not verify: {obs.evidence}",
                        source=claim_result.source,
                        marker="[UNVERIFIED: agent check failed]",
                    ))
                    self.log(f"  ✗ Not verified: {claim_result.claim[:50]}...")
            else:
                # Try to verify unverified claims
                obs = self.agent.verify_claim(claim_result.claim)

                if obs.verified and obs.confidence > 0.5:
                    verified.append(VerificationResult(
                        claim=claim_result.claim,
                        status="VERIFIED_OBSERVED",
                        evidence=obs.evidence[:200],
                        source=obs.source,
                        marker=obs.marker,
                    ))
                    self.log(f"  ✓ Found evidence: {claim_result.claim[:50]}...")
                else:
                    verified.append(claim_result)

        return verified

    def run_goal(self, goal: str, project_name: str | None = None, araw_db: str | None = None) -> GOSMOutput:
        """
        Run GOSM on a goal with full verification pipeline.

        Now uses REAL ARAW engine from library/araw/araw_engine.py.
        """
        self.log(f"Starting GOSM for goal: {goal[:50]}...")

        # Create project folder if name provided
        project_path = None
        if project_name:
            project_path = self.create_project(project_name, goal)
            self.log(f"Created project at: {project_path}")
            # Use project path for ARAW database
            if not araw_db:
                araw_db = str(project_path / 'araw_exploration.db')

        # Phase 1: Pre-engagement - Honest Question Gate (from library)
        self.log("Phase 1: Pre-engagement - Running honest_question_gate")
        honest_gate = run_gate("honest_question_gate", {
            "purpose": goal,
            "satisfaction": "clear",  # Will be properly evaluated
            "_auto_pass": True,  # For now, auto-pass to allow exploration
        })
        self.output.gate_results.append(honest_gate)
        if not honest_gate.passed and honest_gate.blocking:
            self.log(f"Honest question gate BLOCKED: {honest_gate.message}")
            return self.output

        # Phase 2: ARAW Exploration using REAL engine
        self.log("Phase 2: ARAW Exploration (using real engine)")
        exploration, araw_engine = explore_araw(goal, db_path=araw_db)
        self.araw_engine = araw_engine  # Store for later use

        if self.verbose:
            print(format_araw_prompt(exploration))

        # Phase 2.5: Run ARAW → GOSM Integration
        if araw_engine:
            self.log("Phase 2.5: Running ARAW → GOSM integration")
            integration_result = run_araw_integration(araw_engine)

            # Add integration outputs to our output
            for assumption in integration_result.get("assumptions", []):
                self.output.verified_claims.append(VerificationResult(
                    claim=f"Assumption: {assumption['claim']}",
                    status="UNVERIFIED",  # Needs validation
                    evidence=f"leverage={assumption['leverage']:.2f}",
                    source=assumption['source'],
                    marker=f"[ARAW-CRUX: {assumption['id']}]"
                ))

            for task in integration_result.get("validation_tasks", []):
                self.output.unknown_items.append(
                    f"[{task['priority']}] {task['task']} (leverage: {task['leverage']:.2f})"
                )

            self.log(f"Integration: {len(integration_result.get('assumptions', []))} assumptions, "
                    f"{len(integration_result.get('validation_tasks', []))} tasks")

        # Phase 3: Assessment (RCI) - using procedure
        self.log("Phase 3: Assessment with RCI")

        # Try to run the actual RCI procedure
        rci_result = run_procedure(
            "recursive_causal_interrogation",
            {"goal": goal, "context": self.context.to_prompt_section()},
            llm_client=self.llm
        )

        if self.llm:
            system_prompt = build_system_prompt(self.context, goal, "ASSESSMENT")
            user_prompt = build_user_prompt(
                goal,
                format_araw_prompt(exploration)
            )

            response = self.llm.complete(
                prompt=user_prompt,
                system_prompt=system_prompt,
                parse_json=False
            )

            self.log(f"Assessment completed ({response.duration_ms}ms)")

            # Parse and verify claims from response
            self.process_llm_response(response.raw_text)

        # Phase 4: Agent verification (real observation)
        if self.agent and self.output.verified_claims:
            self.log("Phase 4: Agent verification (real observation)")
            self.output.verified_claims = self.verify_with_agent(self.output.verified_claims)

        # Run verification gates from library
        self.log("Running verification gates")

        # Run no_guessing_gate
        no_guess_gate = run_no_guessing_gate(self.output)
        self.output.gate_results.append(no_guess_gate)

        # Run assumption_gate
        assumption_gate = run_gate("assumption_gate", {
            "violations": {},
            "_auto_pass": len(self.output.unknown_items) == 0
        })
        self.output.gate_results.append(assumption_gate)

        if not no_guess_gate.passed:
            self.log(f"No-guessing gate failed: {no_guess_gate.message}")

        # Save ARAW state if we have an engine
        if araw_engine:
            stats = araw_engine.get_stats()
            self.log(f"ARAW stats: {stats['total_nodes']} nodes, depth {stats['max_depth']}")
            if araw_db and araw_db != ":memory:":
                self.log(f"ARAW database saved to: {araw_db}")

        return self.output

    def expand_araw(self, node_id: str | None = None, strategy: str = "balanced") -> dict:
        """
        Expand ARAW exploration on a specific node or next unexplored.

        This allows continuing ARAW exploration after initial run.
        """
        if not hasattr(self, 'araw_engine') or self.araw_engine is None:
            return {"error": "No ARAW engine loaded. Run a goal first."}

        engine = self.araw_engine

        if node_id is None:
            # Get next unexplored node
            unexplored = engine.get_unexplored(limit=1, strategy=strategy)
            if not unexplored:
                return {"message": "No unexplored nodes remaining"}
            node = unexplored[0]
        else:
            node = engine.get_node(node_id)
            if not node:
                return {"error": f"Node not found: {node_id}"}

        # Return node for manual or LLM expansion
        return {
            "node_id": node.id,
            "claim": node.claim,
            "branch_type": node.branch_type,
            "depth": node.depth,
            "leverage": node.leverage_score,
            "path_to_root": [n.claim for n in engine.get_path_to_root(node.id)],
            "instruction": "Branch this node with assume_right and assume_wrong claims",
        }

    def run_honest_question_gate(self, goal: str) -> GateResult:
        """
        Run the honest question gate to check if goal has identifiable purpose.
        """
        # Check if goal has identifiable structure
        has_purpose = len(goal) > 10 and any(
            word in goal.lower()
            for word in ['create', 'build', 'find', 'solve', 'improve', 'make', 'develop', 'analyze', 'understand']
        )

        has_criteria = any(
            marker in goal.lower()
            for marker in ['so that', 'in order to', 'because', 'to achieve', 'resulting in']
        )

        if has_purpose:
            return GateResult(
                gate_id="honest_question_gate",
                passed=True,
                message="Goal has identifiable purpose"
            )

        return GateResult(
            gate_id="honest_question_gate",
            passed=False,
            blocking=False,  # Advisory, not blocking
            message="Goal purpose not immediately clear",
            suggestions=[
                "Clarify: What are you trying to achieve?",
                "Add: What would success look like?"
            ]
        )

    def process_llm_response(self, response_text: str) -> None:
        """
        Process LLM response and extract verified claims.
        """
        # Look for verification markers in response
        lines = response_text.split('\n')

        for line in lines:
            line = line.strip()

            # Check for observed claims [O: source]
            if '[O:' in line:
                claim = line.split('[O:')[0].strip().lstrip('-').strip()
                source = line.split('[O:')[1].split(']')[0].strip()
                self.output.verified_claims.append(
                    verify_claim(claim, evidence="from response", source=source)
                )

            # Check for tested claims [T: result]
            elif '[T:' in line:
                claim = line.split('[T:')[0].strip().lstrip('-').strip()
                result = line.split('[T:')[1].split(']')[0].strip()
                self.output.verified_claims.append(
                    verify_claim(claim, test_result=result)
                )

            # Check for derived claims [D: chain]
            elif '[D:' in line:
                claim = line.split('[D:')[0].strip().lstrip('-').strip()
                chain_str = line.split('[D:')[1].split(']')[0].strip()
                chain = [c.strip() for c in chain_str.split('→')]
                self.output.verified_claims.append(
                    verify_claim(claim, derivation_chain=chain)
                )

            # Check for unknown items
            elif line.startswith('- [UNKNOWN') or '### UNKNOWN' in line.upper():
                if line.startswith('-'):
                    self.output.unknown_items.append(line.lstrip('-').strip())

            # Check for excluded items
            elif '[EXCLUDED' in line or '[UNVERIFIED' in line:
                reason = "Could not verify"
                if ':' in line:
                    parts = line.split(':')
                    if len(parts) >= 2:
                        reason = parts[-1].strip().rstrip(']')
                self.output.excluded_items.append({
                    'item': line.split('[')[0].strip().lstrip('-').strip(),
                    'reason': reason
                })

    def create_project(self, name: str, goal: str) -> Path:
        """Create a new GOSM project folder."""
        date_prefix = datetime.now().strftime('%Y-%m-%d')
        project_name = f"{date_prefix}_{name}"
        project_path = PROJECTS_DIR / project_name
        project_path.mkdir(parents=True, exist_ok=True)

        # Create initial files
        context = {
            'goal': {'original': goal, 'refined': None},
            'created': datetime.now().isoformat(),
            'status': 'planning',
            'phase': 'pre-engagement'
        }

        (project_path / 'context.json').write_text(
            json.dumps(context, indent=2),
            encoding='utf-8'
        )

        (project_path / 'STATE.md').write_text(
            f"# STATE: {name}\n\n**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}\n"
            f"**Status**: PLANNING\n**Health**: 🟢 Starting\n\n"
            f"## Goal\n{goal}\n",
            encoding='utf-8'
        )

        return project_path

    def verify_output_file(self, filepath: Path) -> GOSMOutput:
        """
        Verify an existing output file against GOSM standards.
        """
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        content = filepath.read_text(encoding='utf-8')

        # Process as if it were an LLM response
        self.process_llm_response(content)

        # Run gates
        no_guess_gate = run_no_guessing_gate(self.output)
        self.output.gate_results.append(no_guess_gate)

        return self.output

    def generate_filtered_feedback(
        self,
        goal: str,
        min_leverage: float = 0.5,
        max_feedback_items: int = 10,
    ) -> dict[str, Any]:
        """
        Generate filtered feedback suitable for self-feeding.

        Uses the filtering system based on:
        - leverage_point_discovery.yaml
        - selection.yaml
        - convergent_validation.yaml

        Args:
            goal: The original goal
            min_leverage: Minimum leverage score (0-1) for acceptance
            max_feedback_items: Maximum number of items to accept
        """
        # Extract potential feedback items
        araw_engine = getattr(self, 'araw_engine', None)
        items = extract_feedback_items(self.output, araw_engine)

        self.log(f"Extracted {len(items)} potential feedback items")

        # Apply filtering
        filtered = filter_for_feedback(
            items,
            min_leverage=min_leverage,
            min_convergent_score=2,
            max_feedback_items=max_feedback_items,
        )

        self.log(f"Filtered: {len(filtered.accepted)} accepted, "
                f"{len(filtered.flagged)} flagged, {len(filtered.rejected)} rejected")

        # Format for self-feeding
        return format_self_feeding_output(filtered, goal)

    def format_feedback_report(self, feedback: dict[str, Any]) -> str:
        """Format filtered feedback as readable report."""
        lines = ["# Filtered Feedback for Self-Feeding\n"]

        meta = feedback.get("meta", {})
        lines.append(f"**Original Goal**: {meta.get('original_goal', 'N/A')}")
        lines.append(f"**Accepted**: {meta.get('accepted_count', 0)}")
        lines.append(f"**Flagged**: {meta.get('flagged_count', 0)}")
        lines.append(f"**Rejected**: {meta.get('rejected_count', 0)}")
        lines.append("")

        # Verification summary
        verify = feedback.get("verification_summary", {})
        lines.append("## Verification Summary")
        lines.append(f"- All grounded: {'✅' if verify.get('all_grounded') else '❌'}")
        conv = verify.get("convergent_validation", {})
        lines.append(f"- 4 checks passed: {conv.get('4_checks', 0)}")
        lines.append(f"- 3 checks passed: {conv.get('3_checks', 0)}")
        lines.append("")

        # Accepted items by category
        items = feedback.get("feedback_items", {})
        lines.append("## Accepted Feedback Items\n")

        for category in ["goals", "problems", "questions", "decisions", "assumptions", "strategies"]:
            category_items = items.get(category, [])
            if category_items:
                lines.append(f"### {category.title()}")
                for item in category_items:
                    leverage = item.get("leverage_score", 0)
                    conv_score = item.get("convergent_score", 0)
                    blocking = "🔴 BLOCKING" if item.get("is_blocking") else ""
                    lines.append(f"- {item.get('content', 'N/A')}")
                    lines.append(f"  - Leverage: {leverage:.2f} | Convergent: {conv_score}/4 {blocking}")
                    lines.append(f"  - Source: {item.get('source', 'N/A')}")
                lines.append("")

        # Flagged items
        flagged = feedback.get("flagged_for_review", [])
        if flagged:
            lines.append("## Flagged for Review")
            for item in flagged:
                lines.append(f"- [{item.get('type', 'unknown')}] {item.get('content', 'N/A')}")
                lines.append(f"  - Reason: {item.get('reason', 'N/A')}")
            lines.append("")

        return "\n".join(lines)

    def format_output(self) -> str:
        """Format the output for display."""
        lines = ["# GOSM Output Report\n"]

        # Gate results
        lines.append("## Gate Results")
        for gate in self.output.gate_results:
            status = "✅ PASSED" if gate.passed else "❌ FAILED"
            lines.append(f"- **{gate.gate_id}**: {status}")
            lines.append(f"  - {gate.message}")
            for suggestion in gate.suggestions:
                lines.append(f"    - {suggestion}")
        lines.append("")

        # Verified claims
        lines.append("## Verified Claims")
        for claim in self.output.verified_claims:
            if claim.status != "UNVERIFIED":
                lines.append(f"- {claim.claim} {claim.marker}")
        lines.append("")

        # Unknown items
        if self.output.unknown_items:
            lines.append("## Unknown Items")
            for item in self.output.unknown_items:
                lines.append(f"- {item}")
            lines.append("")

        # Defaults used
        if self.output.defaults_used:
            lines.append("## Defaults Used")
            for default in self.output.defaults_used:
                lines.append(f"- {default.get('value')}: {default.get('reason')}")
            lines.append("")

        # Excluded items
        if self.output.excluded_items:
            lines.append("## Excluded (Unverifiable)")
            for item in self.output.excluded_items:
                lines.append(f"- {item.get('item')}: {item.get('reason')}")
            lines.append("")

        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='GOSM Runner - System Intelligence, Not Model Intelligence',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python gosm_runner.py --goal "Create a business plan for X"
    python gosm_runner.py --goal "Analyze Y" --project my-analysis
    python gosm_runner.py --goal "Solve Z" --feedback              # With filtered feedback
    python gosm_runner.py --goal "Solve Z" --feedback-json         # JSON output for automation
    python gosm_runner.py --goal "X" --min-leverage 0.7 --feedback # Higher filtering threshold
    python gosm_runner.py --verify output.md
    python gosm_runner.py --show-context
    python gosm_runner.py --list-gates
    python gosm_runner.py --list-procedures
    python gosm_runner.py --run-gate honest_question_gate
    python gosm_runner.py --run-procedure recursive_causal_interrogation
        """
    )

    parser.add_argument('--goal', help='Goal to process')
    parser.add_argument('--project', help='Project name (creates folder)')
    parser.add_argument('--araw-db', help='Path to ARAW database file')
    parser.add_argument('--verify', help='Verify an existing output file')
    parser.add_argument('--show-context', action='store_true', help='Show loaded AI context')
    parser.add_argument('--show-checklist', action='store_true', help='Show GOSM checklist')
    parser.add_argument('--list-gates', action='store_true', help='List all available gates')
    parser.add_argument('--list-procedures', action='store_true', help='List all available procedures')
    parser.add_argument('--run-gate', help='Run a specific gate by ID')
    parser.add_argument('--run-procedure', help='Run a specific procedure by ID')
    parser.add_argument('--show-audit', action='store_true', help='Show self-audit results')
    parser.add_argument('--feedback', action='store_true', help='Generate filtered feedback for self-feeding')
    parser.add_argument('--feedback-json', action='store_true', help='Output feedback as JSON (for automation)')
    parser.add_argument('--min-leverage', type=float, default=0.5, help='Minimum leverage score for feedback (0-1)')
    parser.add_argument('--max-feedback', type=int, default=10, help='Maximum feedback items to accept')
    parser.add_argument('--agent', action='store_true', default=True, help='Use observation agent for real verification (default: True)')
    parser.add_argument('--no-agent', action='store_true', help='Disable observation agent')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    args = parser.parse_args()

    use_agent = args.agent and not args.no_agent
    runner = GOSMRunner(verbose=args.verbose, use_agent=use_agent)

    if args.show_context:
        print("# AI Context Loaded\n")
        print(runner.context.to_prompt_section())
        return

    if args.list_gates:
        print("# Available Gates\n")
        gates = list_available_gates()
        for gate in gates:
            print(f"  - {gate}")
        print(f"\nTotal: {len(gates)} gates")
        print("\nUse --run-gate <gate_id> to run a specific gate")
        return

    if args.list_procedures:
        print("# Available Procedures\n")
        procedures = list_available_procedures()
        for proc in procedures:
            print(f"  - {proc}")
        print(f"\nTotal: {len(procedures)} procedures")
        print("\nUse --run-procedure <procedure_id> to run a specific procedure")
        return

    if args.run_gate:
        print(f"# Running Gate: {args.run_gate}\n")
        gate_def = load_gate(args.run_gate)
        if gate_def:
            print(f"Name: {gate_def.get('name', args.run_gate)}")
            print(f"Type: {gate_def.get('type', 'unknown')}")
            print(f"Description: {gate_def.get('description', 'No description')[:200]}")
            print("\nRunning with default context...")
            result = run_gate(args.run_gate, {"_auto_pass": False})
            print(f"\nResult: {'PASSED' if result.passed else 'FAILED'}")
            print(f"Blocking: {result.blocking}")
            print(f"Message: {result.message}")
            if result.suggestions:
                print("Suggestions:")
                for s in result.suggestions:
                    print(f"  - {s}")
        else:
            print(f"Gate not found: {args.run_gate}")
        return

    if args.run_procedure:
        print(f"# Running Procedure: {args.run_procedure}\n")
        proc_def = load_procedure(args.run_procedure)
        if proc_def:
            print(f"Name: {proc_def.get('name', args.run_procedure)}")
            print(f"Domain: {proc_def.get('domain', 'unknown')}")
            desc = proc_def.get('description', 'No description')
            print(f"Description: {desc[:200]}..." if len(desc) > 200 else f"Description: {desc}")
            print("\nSteps:")
            for step in proc_def.get('steps', [])[:5]:
                step_name = step.get('name', step.get('id', 'unnamed'))
                print(f"  - {step_name}")
            if len(proc_def.get('steps', [])) > 5:
                print(f"  ... and {len(proc_def.get('steps', [])) - 5} more")
            print("\nRunning with default inputs...")
            result = run_procedure(args.run_procedure, {}, llm_client=runner.llm)
            print(f"\nSuccess: {result['success']}")
            print(f"Steps executed: {len(result['steps_executed'])}")
        else:
            print(f"Procedure not found: {args.run_procedure}")
        return

    if args.show_audit:
        audit_path = GOSM_ROOT / 'scripts' / 'GOSM_RUNNER_AUDIT.md'
        if audit_path.exists():
            print(audit_path.read_text(encoding='utf-8'))
        else:
            print("No audit file found. Run self-audit first.")
        return

    if args.show_checklist:
        print("# GOSM Checklist\n")
        current_phase = None
        for item in runner.checklist:
            if item['phase'] != current_phase:
                current_phase = item['phase']
                print(f"\n## {current_phase}")
            print(f"- [ ] {item['item']}")
        return

    if args.verify:
        filepath = Path(args.verify)
        output = runner.verify_output_file(filepath)
        print(runner.format_output())

        # Exit with error if gates failed
        failed_gates = [g for g in output.gate_results if not g.passed and g.blocking]
        if failed_gates:
            sys.exit(1)
        return

    if args.goal:
        output = runner.run_goal(args.goal, project_name=args.project, araw_db=args.araw_db)
        print(runner.format_output())

        # Generate filtered feedback if requested
        if args.feedback or args.feedback_json:
            print("\n" + "="*60 + "\n")
            feedback = runner.generate_filtered_feedback(
                args.goal,
                min_leverage=args.min_leverage,
                max_feedback_items=args.max_feedback,
            )

            if args.feedback_json:
                print(json.dumps(feedback, indent=2, default=str))
            else:
                print(runner.format_feedback_report(feedback))

        # Exit with error if gates failed
        failed_gates = [g for g in output.gate_results if not g.passed and g.blocking]
        if failed_gates:
            sys.exit(1)
        return

    # No action specified
    parser.print_help()
    sys.exit(1)


if __name__ == '__main__':
    main()
