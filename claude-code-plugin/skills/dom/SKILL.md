---
name: "dom - Dominance Analysis"
description: Identify options that dominate others — strictly better on all dimensions, or better on some and equal on the rest.
output:
  format: "prose"
---

# Dominance Analysis

**Input**: $ARGUMENTS

---

## Step 1: IDENTIFY THE OPTIONS

List all options being compared. If not provided, generate the obvious option set.

```
OPTIONS:
1. [option A]
2. [option B]
3. [option N]
```

---

## Step 2: IDENTIFY THE DIMENSIONS

What dimensions matter for this comparison?

For each dimension:
- Is it a MAXIMIZE dimension (more is better)?
- Is it a MINIMIZE dimension (less is better)?
- Is it a THRESHOLD dimension (must meet minimum)?

```
DIMENSIONS:
1. [dim 1] — [MAX/MIN/THRESHOLD]
2. [dim 2] — [MAX/MIN/THRESHOLD]
...
```

---

## Step 3: SCORE THE MATRIX

Rate each option on each dimension. Use consistent scales.

```
           | Dim 1 | Dim 2 | Dim 3 | ...
Option A   |       |       |       |
Option B   |       |       |       |
Option C   |       |       |       |
```

---

## Step 4: STRICT DOMINANCE CHECK

Option X **strictly dominates** Option Y if X is better on EVERY dimension.

For each pair of options:
- Does X beat Y on all dimensions? -> X strictly dominates Y
- Does X beat Y on some and tie on rest? -> X weakly dominates Y
- Does X beat Y on some but lose on others? -> Neither dominates (Pareto)

```
DOMINANCE RESULTS:
- [Option A] strictly dominates [Option C] — better on all dimensions
- [Option B] weakly dominates [Option C] — better on 2, equal on 1
- [Option A] vs [Option B] — neither dominates (Pareto optimal pair)

DOMINATED OPTIONS (can eliminate):
- [Option C] — dominated by A and B

PARETO FRONTIER (non-dominated):
- [Option A], [Option B]
```

---

## Step 5: NEAR-DOMINANCE

Sometimes an option loses on one trivial dimension but wins on everything else.

For each non-dominated pair:
- Where does each option lose?
- How much does it lose by?
- Is that dimension important enough to matter?

Flag any option that is "almost dominated" — loses on only one low-weight dimension.

---

## Step 6: HIDDEN DIMENSIONS

Before concluding, check:
1. Are there dimensions we didn't consider that would change the ranking?
2. Are any dimensions actually correlated (not independent)?
3. Does the scoring change under different conditions/timeframes?
4. Is there an option we didn't consider that might dominate everything?

---

## Step 7: OUTPUT

```
DOMINANCE ANALYSIS:

Eliminated (dominated): [list]
Pareto frontier: [list of non-dominated options]

If one option dominates all others:
  DOMINANT OPTION: [X] — strictly better on all dimensions, choose this.

If Pareto frontier has multiple options:
  TRADE-OFF: [X] vs [Y]
  - Choose [X] if you prioritize [dim]
  - Choose [Y] if you prioritize [dim]

Key insight: [what the dominance analysis reveals]
```

---

## Integration

Use with:
- `/cmp` -> Full comparison when no option dominates
- `/cba` -> Cost-benefit when trade-offs need quantifying
- `/dd` -> Discover dimensions you might have missed
- `/obv` -> Add obvious checks before concluding
