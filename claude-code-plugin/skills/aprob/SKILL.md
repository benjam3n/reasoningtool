---
name: "aprob - Assume Problem"
description: "Force the assumption that something IS the problem. Trace what follows if this is truly the root cause. What would fixing it look like? What evidence would confirm it?"
output:
  format: "prose"
---

# Assume Problem

**Input**: $ARGUMENTS

---

## Core Move

Take something — a factor, condition, person, system, belief — and **assume it is THE problem.** Not a contributing factor. THE root cause. Then trace what follows.

Useful for testing candidate root causes without getting lost in "well, it's complicated."

---

## Procedure

### Step 1: State the Candidate Problem
What are we assuming is the problem?

### Step 2: Force the Assumption
"[X] is the root cause. Everything else is a symptom or downstream effect."

### Step 3: Trace Implications
If this is the problem:

1. **What symptoms does it explain?** — List every observed issue that would flow from this root cause.
2. **What symptoms does it NOT explain?** — What's left unexplained? (These challenge the assumption.)
3. **What does fixing it look like?** — Concrete actions to address this specific root cause.
4. **What's the predicted result of fixing it?** — If we fix this and it IS the problem, what specifically improves?
5. **How did it become the problem?** — What's the causal history?
6. **Why hasn't it been fixed already?** — What's prevented the fix? Incentives? Visibility? Difficulty?

### Step 4: Test the Assumption
- Does this explain MORE symptoms than alternative root causes?
- Would fixing this actually resolve the situation, or would new problems emerge?
- Is there a way to test this hypothesis before committing to a fix?
- Could this be a symptom mistaken for a cause?

### Step 5: Synthesize
```
CANDIDATE PROBLEM: [X]
ASSUMING IT'S THE ROOT CAUSE:
  Explains: [symptoms accounted for]
  Doesn't explain: [gaps]
  Fix: [concrete actions]
  Predicted result: [what improves]
ROOT CAUSE CONFIDENCE: [high/medium/low]
TEST: [how to verify before committing]
```

---

## When to Use
- Have multiple candidate root causes and need to test each
- Stuck in analysis paralysis about what the "real" problem is
- Want to trace implications of a specific diagnosis

## Integration
- Run multiple times with different candidates, then compare
- Pair with `/rca` for systematic root cause analysis
- Follow with `/asol` to test candidate solutions
