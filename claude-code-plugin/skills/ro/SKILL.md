---
name: "ro - Reorder a List Expertly"
description: Reorder an existing list using an explicit objective, constraints, and scoring method. Produces a defensible best-to-worst order.
---

# RO - Reorder

**Input**: $ARGUMENTS

---

## Purpose

Take a provided list and reorder it optimally for a stated objective.

## Steps

### 1. Parse Inputs

Extract:
- ORIGINAL_LIST
- OBJECTIVE
- CONSTRAINTS
- TIME_HORIZON

If objective is missing, set a default objective from context and state it.

### 2. Define Scoring Dimensions

Use 3-6 dimensions tied to objective.
Example: impact, effort, risk, reversibility, dependency unlock.

### 3. Score Each Item

For each dimension use a consistent scale.
Compute total score.

### 4. Build Ordered Output

Sort highest-to-lowest score.
Break ties with objective alignment and dependency order.

### 5. Sanity Check

Check top 3 and bottom 3 for obvious misplacements.
Adjust if needed and state why.

---

## Output Format

```text
OBJECTIVE: ...
SCORING_DIMENSIONS: [d1, d2, ...]

1. [item]
   SCORE: ...
   REASON: ...
2. [item]
   SCORE: ...
   REASON: ...
...

LOWEST_CONFIDENCE_PLACEMENT: [item]
```
