---
name: "gapf - Gap-Filling Analysis"
description: Systematically find what's missing in any system, plan, or collection. Defines intended coverage, enumerates what exists, identifies categories, checks each for coverage, flags gaps, and prioritizes by impact.
output:
  format: "prose"
---

# Gap-Filling Analysis

**Input**: $ARGUMENTS

---

## Step 1: Define Intended Coverage

Articulate what the system/plan/collection is supposed to cover.

```
SUBJECT: [what is being analyzed]
INTENDED SCOPE: [what full coverage would look like]
STATED GOALS: [explicit goals, if any]
IMPLIED GOALS: [goals that are implied but not stated]
COMPLETENESS STANDARD: [how do we know when it's "complete"?]
```

---

## Step 2: Enumerate What Exists

List everything currently present in the system.

```
EXISTING COMPONENTS:
1. [component] — covers [what it addresses]
2. [component] — covers [what it addresses]
...
```

SKIP: If the inventory is already provided or obvious, summarize rather than enumerate.

---

## Step 3: Identify Categories

Break the intended coverage into logical categories or dimensions.

```
COVERAGE CATEGORIES:
1. [category] — description
2. [category] — description
...

CATEGORIZATION METHOD: [how these categories were derived]
```

---

## Step 4: Check Coverage Per Category

For each category, assess whether existing components provide adequate coverage.

```
COVERAGE MAP:
| Category | Covered By | Coverage Level | Notes |
|----------|-----------|----------------|-------|
| [cat 1]  | [components] | FULL / PARTIAL / NONE | [detail] |
| [cat 2]  | [components] | FULL / PARTIAL / NONE | [detail] |
...
```

---

## Step 5: Flag Gaps

Identify what is missing, underdeveloped, or only superficially covered.

```
GAPS FOUND:
1. [gap] — Category: [cat] — Severity: [CRITICAL / SIGNIFICANT / MINOR]
   Why it matters: [impact of this gap]
2. [gap] — Category: [cat] — Severity: [CRITICAL / SIGNIFICANT / MINOR]
   Why it matters: [impact of this gap]
...

PARTIAL COVERAGE (needs deepening):
1. [component] — What's missing: [detail]
...
```

---

## Step 6: Prioritize by Impact

Rank gaps by their impact on the overall system's effectiveness.

```
PRIORITY ORDER:
1. [gap] — Impact: [HIGH/MED/LOW] — Effort: [HIGH/MED/LOW] — Rationale: [why this matters most]
2. [gap] — Impact: [HIGH/MED/LOW] — Effort: [HIGH/MED/LOW] — Rationale: [reasoning]
...

QUICK WINS (high impact, low effort):
- [gap]: [what to do]

STRATEGIC GAPS (high impact, high effort):
- [gap]: [what to do]
```

---

## Step 7: Synthesize

```
SUMMARY:
- Total categories: [N]
- Fully covered: [N]
- Partially covered: [N]
- Not covered: [N]
- Top priority gap: [description]
- Recommended first action: [what to do next]
```

---

## Integration

Use with:
- `/ecomp` -> Assess overall ecosystem coherence after filling gaps
- `/roip` -> Prioritize which gaps to fill based on ROI
- `/se` -> Explore the space to ensure categories are complete
