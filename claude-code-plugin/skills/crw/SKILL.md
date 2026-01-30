---
name: crw
description: "Also known as: Weighted scoring model, Decision matrix, Pugh matrix."
---

# Criteria Weighting Decision Matrix

## Overview
Also known as: Weighted scoring model, Decision matrix, Pugh matrix.

Complex decisions become manageable when broken into:
1. Independent criteria
2. Importance weights
3. Option ratings
4. Mechanical aggregation

Each individual judgment is simple; the math does the combining.

## Goal
Make decisions by decomposing into criteria, weighting by importance,
rating options on each criterion, and calculating weighted scores.
Decomposition makes evaluation tractable; aggregation is mechanical.

## Steps

### Step 1: Define the Decision
Clearly state what you're deciding.
What choice are you making? What's the goal?

**Output**: Decision statement

### Step 2: List All Options
Enumerate all options being considered.
Include "do nothing" or "status quo" if relevant.

**Output**: Option list

### Step 3: Identify Criteria
List all factors that matter for this decision.

Good criteria are:
- Relevant (actually affects decision quality)
- Measurable (can rate options on it)
- Independent (not redundant with other criteria)

Common criteria types:
- Cost/price
- Quality/performance
- Time/speed
- Risk
- Ease/convenience
- Alignment with goals
- Stakeholder preference

**Output**: Criteria list

### Step 4: Assign Weights
Distribute 100 points across criteria by importance.
Higher weight = more important in decision.

Methods:
- Direct allocation: Just assign points
- Pairwise: Compare criteria pairs to derive weights
- Ranking: Rank criteria, assign points by rank

Weights should sum to 100 (or 1.0).

**Output**: Weighted criteria

### Step 5: Rate Options on Each Criterion
For each option, for each criterion:
Rate on scale of 1-10 (or 1-5).

1 = Worst possible on this criterion
10 = Best possible on this criterion

Rate consistently across options.

**Output**: Rating matrix

### Step 6: Calculate Weighted Scores
For each option:
Weighted Score = Σ (Weight_i × Rating_i)

If weights sum to 100 and ratings are 1-10,
max possible score = 1000.

**Output**: Weighted scores

### Step 7: Rank Options
Sort options by weighted score (descending).
Highest score = recommended option.

**Output**: Final ranking

### Step 8: Sensitivity Analysis
Test how robust the ranking is:
- What if weights changed?
- What if ratings changed?
- How close are the top options?

If top two are very close, decision is sensitive.
If top option wins by large margin, decision is robust.

**Output**: Sensitivity assessment

### Step 9: Sanity Check
Does the recommended option feel right?
If not, examine:
- Are criteria missing?
- Are weights wrong?
- Are ratings inaccurate?

The matrix is a tool to structure thinking, not replace judgment.

**Output**: Final decision


## When to Use
- Choosing between multiple options
- Making decisions with multiple criteria
- Need to justify decision transparently
- Want to reduce bias from single-factor focus
- Team needs to align on priorities

## Verification
- All relevant criteria are included
- Criteria are independent (not double-counting)
- Weights sum to 100 (or 1.0)
- Ratings are consistent across options
- Calculations are correct
- Sensitivity analysis performed
- Result passes sanity check

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.