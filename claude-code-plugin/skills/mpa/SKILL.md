---
name: mpa
description: "Generate, evaluate, and manage multiple alternative plans for the same goal"
---

# Multi-Plan Aggregation

## Overview
Generate, evaluate, and manage multiple alternative plans for the same goal

## Steps

### Step 1: Divergent generation
Generate maximum variety of approaches to the goal:
1. Brainstorm obvious approaches (3-5 conventional methods)
2. Apply strategy inversion (what if we did the opposite?)
3. Cross-domain bridging (what works in other fields?)
4. Constraint removal (what if X weren't true?)
5. Stakeholder perspective (what would expert Y do?)

Target: 8-15 distinct approaches before any filtering.

SAFETY: Only generate legal, ethical approaches. Flag any
approaches that might have compliance concerns.

### Step 2: Quick filter
Eliminate clearly infeasible approaches:
- Violates hard constraints?
- Requires unavailable resources?
- Mathematically/physically impossible?
- Ethically problematic?
- Already tried and failed?

Keep "unlikely but possible" - only remove "impossible".

SAFETY: Document why each eliminated plan was removed.
Human can review eliminations if desired.

### Step 3: Rapid development
For each surviving approach, develop a quick plan sketch:
- One-paragraph summary of the approach
- Key steps (5-10 high-level steps)
- Resource requirements estimate
- Major risks identified
- Initial probability estimate (gut feel)

Time limit: 15-30 minutes per plan to avoid over-investing
before scoring.

SAFETY: Do not commit any resources yet. This is planning only.

### Step 4: Systematic scoring
Score each plan on 5 dimensions:

1. Probability of Success (weight: 0.30)
   Scale: 0-100%
   Question: "If executed well, what's the chance of achieving the goal?"

2. Resource Efficiency (weight: 0.20)
   Scale: 1-10
   Question: "How well does resource investment match potential return?"

3. Robustness (weight: 0.20)
   Scale: 1-10
   Question: "How well does plan handle unexpected problems?"

4. Speed (weight: 0.15)
   Scale: 1-10
   Question: "How quickly can this achieve results?"

5. Learning Value (weight: 0.15)
   Scale: 1-10
   Question: "How much will we learn even if it fails?"

Formula: Score = (Prob * 0.3) + (Efficiency * 0.2) +
                 (Robust * 0.2) + (Speed * 0.15) + (Learning * 0.15)

SAFETY: Document reasoning for each score. Human can adjust weights
based on priorities.

### Step 5: Portfolio selection
Based on portfolio_strategy, select plans for the portfolio:

CONCENTRATED (all resources on best plan):
- When: High confidence in best plan, limited resources
- Selection: Top 1 plan as primary, top 2 as documented backup

DIVERSIFIED (spread across multiple plans):
- When: High uncertainty, parallel execution possible
- Selection: Top 3 plans with different approaches, run in parallel

STAGED (primary + ready backups):
- When: Serial execution, need pivot capability
- Selection: Top plan as primary, next 2 as ready backups

SAFETY: This step REQUIRES human approval before proceeding.
Present portfolio recommendation and wait for confirmation.

### Step 6: Full development
Develop selected plans to appropriate detail:

PRIMARY PLAN:
- Complete STEPS.md with all phases and tasks
- Detailed resource allocation
- Decision gates with criteria
- Pivot triggers (conditions that activate backup)
- Success metrics and checkpoints

BACKUP PLANS:
- Summary-level development
- Key steps identified
- Resources reserved or identified
- Activation procedure defined

STANDBY PLANS:
- Minimal development
- Core concept documented
- Can be developed quickly if needed

SAFETY: Resource commitments require human approval.

### Step 7: Initialize tracking
Set up portfolio management infrastructure:

1. Create PLAN_DATABASE.md with:
   - All plans with status (active/ready/standby/archived)
   - Ranking and scores
   - Resource allocation
   - Decision log

2. Define rebalancing triggers:
   - Active plan hits major blocker
   - New information changes probabilities
   - Resource availability changes
   - Deadline approaches with active plan behind

3. Schedule regular reviews:
   - Weekly probability updates
   - Milestone-based reassessment
   - Pre-deadline final check

SAFETY: All plan status changes logged with timestamp and reason.


## When to Use
- Goal has multiple valid approaches worth exploring
- Uncertainty is high and single-plan risk is unacceptable
- Stakes are significant enough to warrant backup plans
- Time permits exploration before commitment
- Competition context where multiple entries improve odds
- Past experience shows plans often need pivoting
- Resources allow parallel development of alternatives
- Complex goal with many unknown dependencies

## Verification
- Portfolio has minimum 2 plans (primary + at least one backup)
- All plans satisfy hard constraints
- Scoring is documented and defensible
- Pivot triggers are specific and measurable
- Human has approved portfolio selection
- Primary plan is fully executable
- Backup plans can be activated within defined timeframe
- Resource allocation does not exceed available resources

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.