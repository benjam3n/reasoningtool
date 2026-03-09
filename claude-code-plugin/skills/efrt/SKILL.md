---
name: "efrt - Effort Estimation"
description: Estimates how much effort something will take. Decomposes into subtasks, applies three-point estimation, adds buffers, and compares to reference classes.
---

# Effort Estimation

**Input**: $ARGUMENTS

---

## Step 1: Decompose into Subtasks

Break the work into concrete, estimable pieces.

```
WORK ITEM: [What is being estimated]
DEFINITION OF DONE: [What counts as complete]

SUBTASKS:
1. [Subtask 1] — deliverable: [what it produces]
2. [Subtask 2] — deliverable: [what it produces]
3. [Subtask 3] — deliverable: [what it produces]
...

DEPENDENCIES: [Which subtasks depend on others?]
DECOMPOSITION CONFIDENCE: [Are these subtasks well-defined enough to estimate?]
```

---

## Step 2: Three-Point Estimate Each Subtask

For each subtask, estimate optimistic, likely, and pessimistic effort.

```
SUBTASK 1 — [name]:
  Optimistic:  [time/effort — everything goes right]
  Likely:      [time/effort — normal conditions]
  Pessimistic: [time/effort — significant obstacles]
  Expected:    [weighted average: (O + 4L + P) / 6]

SUBTASK 2 — [name]:
  Optimistic:  [time/effort]
  Likely:      [time/effort]
  Pessimistic: [time/effort]
  Expected:    [weighted average]

[Repeat for all subtasks]

RAW TOTAL: [Sum of all expected values]
```

---

## Step 3: Add Buffer for Unknowns

Account for things you cannot see yet.

```
KNOWN UNKNOWNS:
- [Thing you know you don't know 1]
- [Thing you know you don't know 2]

UNKNOWN UNKNOWN RISK: [LOW/MEDIUM/HIGH]
  LOW = well-understood work, multiply by 1.2x
  MEDIUM = some novelty, multiply by 1.5x
  HIGH = significant unknowns, multiply by 2.0x

BUFFER MULTIPLIER: [1.2x / 1.5x / 2.0x]
BUFFERED TOTAL: [raw total * multiplier]
```

---

## Step 4: Reference Class Comparison

Compare to similar past work for a sanity check.

```
REFERENCE CLASS: [What category of work is this similar to?]

COMPARABLE EXAMPLES:
1. [Past work 1] — actual effort: [what it took]
2. [Past work 2] — actual effort: [what it took]
3. [Past work 3] — actual effort: [what it took]

REFERENCE CLASS AVERAGE: [typical effort for this kind of work]
COMPARISON: [How does your estimate compare? Within range or outlier?]
ADJUSTMENT: [If your estimate differs significantly, adjust or explain why]
```

---

## Step 5: Final Estimate

```
FINAL ESTIMATE: [time/effort]
CONFIDENCE RANGE: [low end] to [high end]
CONFIDENCE LEVEL: [How confident: 50%? 80%? 90%?]

BIGGEST RISK TO ESTIMATE: [What could blow this estimate up?]
WHAT WOULD MAKE IT FASTER: [Conditions that could reduce effort]
WHAT WOULD MAKE IT SLOWER: [Conditions that could increase effort]

RECOMMENDATION: [Commit to this estimate? Or gather more info first?]
```

---

## Integration

Use with:
- `/benf` -> Pair effort with benefit for ROI calculation
- `/ratn` -> Build a rationale around the estimate for stakeholders
- `/ctgp` -> Estimate effort for filling category gaps
