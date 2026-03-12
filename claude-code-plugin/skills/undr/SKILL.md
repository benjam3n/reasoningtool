---
name: "undr - Under-Represented Analysis"
description: Analyzes an under-served area to determine what it needs. Assesses current coverage, identifies gaps relative to demand, and recommends build order.
output:
  format: "prose"
---

# Under-Represented Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify the Area

Define the under-served area precisely. What is it, and why does it seem under-represented?

```
AREA: [The area under analysis]
BELONGS TO: [The larger category or system it sits within]
SIGNAL OF UNDER-REPRESENTATION: [What made you notice this area is under-served?]
```

---

## Step 2: Assess Current Coverage

Inventory what currently exists in this area.

```
EXISTING COVERAGE:
1. [Item 1] — quality: [HIGH/MEDIUM/LOW] — coverage: [what it handles]
2. [Item 2] — quality: [HIGH/MEDIUM/LOW] — coverage: [what it handles]
3. [Item 3] — quality: [HIGH/MEDIUM/LOW] — coverage: [what it handles]
...

TOTAL ITEMS: [count]
QUALITY DISTRIBUTION: [How many high/medium/low]
COVERAGE MAP: [What percentage of the area is currently served?]
```

---

## Step 3: Identify What's Missing

Compare current coverage to what the area actually needs.

```
DEMAND SIGNALS:
- [Evidence of need 1]
- [Evidence of need 2]
- [Evidence of need 3]

GAPS (what's missing relative to demand):
1. [Gap 1] — demand level: [HIGH/MEDIUM/LOW]
2. [Gap 2] — demand level: [HIGH/MEDIUM/LOW]
3. [Gap 3] — demand level: [HIGH/MEDIUM/LOW]
...

MOST CRITICAL GAP: [Which gap causes the most pain if left unfilled?]
```

---

## Step 4: Estimate Effort to Fill Gaps

For each gap, estimate what it would take to address it.

```
GAP 1 — [name]:
- Effort: [LOW/MEDIUM/HIGH]
- Dependencies: [What else needs to exist first?]
- Complexity: [Simple addition or requires new infrastructure?]

GAP 2 — [name]:
- Effort: [LOW/MEDIUM/HIGH]
- Dependencies: [What else needs to exist first?]
- Complexity: [Simple addition or requires new infrastructure?]

[Repeat for each gap]
```

---

## Step 5: Prioritize and Recommend Build Order

Rank gaps by impact-to-effort ratio and recommend a sequence.

```
PRIORITY RANKING (by impact / effort):
1. [Gap] — impact: [H/M/L], effort: [H/M/L] — DO FIRST
2. [Gap] — impact: [H/M/L], effort: [H/M/L]
3. [Gap] — impact: [H/M/L], effort: [H/M/L]
...

RECOMMENDED BUILD ORDER:
Phase 1: [What to build first and why]
Phase 2: [What to build next]
Phase 3: [What can wait]

SKIP: [Anything that seems like a gap but isn't worth filling — and why]
```

---

## Integration

Use with:
- `/satr` -> Check if the parent category is over-served elsewhere
- `/ctgp` -> Formal category gap analysis
- `/efrt` -> Detailed effort estimation for top-priority gaps
- `/benf` -> Estimate benefits of filling each gap
