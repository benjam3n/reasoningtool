---
name: o
description: "Rank viable options from best to worst using multi-criteria optimization"
---

# Optimization

## Overview
Rank viable options from best to worst using multi-criteria optimization

## Steps

### Step 1: Prepare scoring matrix
Organize inputs into a decision matrix:
1. List all viable options as rows
2. List all criteria as columns
3. Fill in scores from comparison phase
4. Normalize scores to comparable scale (0-10 or 0-100)

### Step 2: Establish criteria weights
Determine importance weight for each criterion:
1. If weights provided, validate they sum to 1.0 (or normalize)
2. If not provided, start with equal weights
3. Consider stakeholder preferences in weighting
4. Document rationale for each weight

Weight assignment approaches:
- Direct assignment: stakeholder states importance
- Pairwise comparison: compare criteria in pairs
- Swing weighting: how much does best-to-worst matter?

### Step 3: Calculate composite scores
For each option, calculate weighted composite score:
1. Multiply each criterion score by its weight
2. Sum the weighted scores
3. Record the composite score

Formula: composite_score = sum(score_i * weight_i)

Also track component contributions to understand what's driving the score.

### Step 4: Identify Pareto optimal set
Find options that are not dominated by any other option:
1. Option A dominates Option B if A is >= B on all criteria AND > on at least one
2. Pareto optimal options are those not dominated by any other
3. If optimizing for different goals (max value vs min risk), find Pareto frontier

Options on the Pareto frontier represent genuinely different trade-offs,
not clearly inferior choices.

### Step 5: Perform sensitivity analysis
Test ranking stability under different assumptions:
1. Vary each weight by +/- 20% and recompute rankings
2. Try alternative weighting schemes (equal weights, extreme weights)
3. Identify which weight changes would change the top-ranked option
4. Note "robust" rankings (stable) vs "fragile" rankings (weight-sensitive)

Key questions:
- Does the top option change if we care more about X?
- How much would weights need to change to alter the ranking?

### Step 6: Analyze trade-offs
For top 2-3 options, make trade-offs explicit:
1. Compare top option vs second option: what do we gain? lose?
2. Identify criteria where top option is weaker
3. Quantify the trade-off (e.g., "20% more cost for 50% less risk")
4. Consider non-quantified factors that might affect the trade-off

Trade-off analysis helps stakeholders understand what they're choosing.

### Step 7: Compile final ranking
Produce the final ranked list:
1. Order options by composite score (highest first)
2. Annotate each with: rank, score, Pareto status, key strengths/weaknesses
3. Write rationale for top-ranked option
4. Note any caveats or conditions on the ranking

The ranking should be defensible and transparent.


## When to Use
- When multiple viable options remain after comparison
- When trade-offs between options need to be made explicit
- When stakeholders disagree on which option is best
- When the decision has significant consequences
- At strategy selection to rank competing strategies
- When you need a defensible, transparent ranking method

## Verification
- All viable options are ranked (none dropped)
- Composite scores are calculated correctly (math is right)
- Pareto analysis identifies non-dominated options
- Sensitivity analysis tests ranking robustness
- Trade-offs are explicit and quantified
- Ranking rationale is clear and defensible

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.