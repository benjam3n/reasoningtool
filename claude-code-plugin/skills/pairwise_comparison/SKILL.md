---
name: pairwise_comparison
description: "Instead of rating each option absolutely (hard), compare pairs"
---

# Pairwise Comparison Matrix

## Overview
Instead of rating each option absolutely (hard), compare pairs
directly (easier). "Is A better than B?" is easier than "How good is A?"
Aggregate comparisons to produce ranking.

## Goal
Rank options by comparing all pairs and counting wins.
Each individual comparison is simple; aggregation is mechanical.
Avoids the difficulty of absolute rating.

## Steps

### Step 1: List All Options
Enumerate all options to be compared.
Label them for easy reference (A, B, C... or 1, 2, 3...).

**Output**: Labeled option list

### Step 2: Define Comparison Criterion
Clearly state what you're comparing on.
Can be single criterion or composite.

Single: "Which is more important?"
Composite: "Considering cost, quality, and time, which is better?"

**Output**: Criterion statement

### Step 3: Create Comparison Matrix
Create N×N matrix with options on both axes.
Diagonal is empty (don't compare to self).
Only need to fill upper triangle (lower is symmetric).

**Output**: Empty matrix

### Step 4: Compare Each Pair
For each pair (i, j) where i < j:
Ask: "Is [Option i] better than [Option j] on [criterion]?"

Record:
- "1" in cell (i,j) if i wins
- "0" in cell (i,j) if j wins
- "0.5" each if tie

Be consistent. If A > B and B > C, then A > C (transitivity).

**Output**: Filled comparison matrix

### Step 5: Check for Inconsistencies
Look for intransitive cycles: A > B > C > A
If found, reconsider those comparisons.
Some intransitivity may be acceptable (different criteria).

**Output**: Consistency check result

### Step 6: Calculate Scores
For each option, sum its wins.
Win = 1 point, Tie = 0.5 points, Loss = 0 points
Total possible points = N - 1

**Output**: Score for each option

### Step 7: Produce Ranking
Sort options by score (descending).
Handle ties by re-comparing or accepting tie.

**Output**: Final ranking


## When to Use
- Ranking options when absolute scoring is difficult
- Prioritizing features/tasks
- Multi-criteria decision making
- Reducing bias from anchoring
- When options are hard to rate but easy to compare

## Verification
- All pairs were compared
- Criterion was applied consistently
- No significant intransitivity
- Scores sum correctly
- Ranking reflects scores

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.