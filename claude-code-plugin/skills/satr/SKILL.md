---
name: "satr - Saturation Analysis"
description: Analyzes whether an area has too much coverage. Identifies redundancy, finds rarely-used items, and recommends consolidation or pruning.
---

# Saturation Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify the Area

Define the area suspected of being over-saturated.

```
AREA: [The area under analysis]
BELONGS TO: [The larger category or system it sits within]
SATURATION SIGNAL: [What made you suspect over-coverage?]
```

---

## Step 2: Count Existing Items

Inventory everything currently in this area.

```
EXISTING ITEMS:
1. [Item 1] — purpose: [what it does]
2. [Item 2] — purpose: [what it does]
3. [Item 3] — purpose: [what it does]
...

TOTAL COUNT: [number]
EXPECTED COUNT: [How many items would a well-designed version of this area have?]
RATIO: [actual / expected — over 1.5x suggests saturation]
```

---

## Step 3: Assess Redundancy

Identify items that serve the same or overlapping purposes.

```
REDUNDANCY CLUSTERS:
Cluster A — purpose: [shared purpose]
  - [Item X]
  - [Item Y]
  - Overlap: [percentage or description of overlap]
  - Best of cluster: [which one is strongest]

Cluster B — purpose: [shared purpose]
  - [Item X]
  - [Item Y]
  - Overlap: [percentage or description of overlap]
  - Best of cluster: [which one is strongest]

UNIQUE ITEMS (no redundancy):
- [Item] — uniquely serves: [what]

REDUNDANCY RATE: [What percentage of items overlap with at least one other?]
```

---

## Step 4: Identify Low-Usage Items

Flag items that exist but are rarely used or needed.

```
USAGE ASSESSMENT:
- [Item 1]: [HIGH/MEDIUM/LOW/NEVER] — evidence: [how you know]
- [Item 2]: [HIGH/MEDIUM/LOW/NEVER] — evidence: [how you know]
...

RARELY USED:
1. [Item] — last meaningful use: [when/context]
2. [Item] — last meaningful use: [when/context]

COST OF KEEPING: [What is the maintenance burden of unused items?]
```

---

## Step 5: Recommend Consolidation or Pruning

Provide specific, actionable recommendations.

```
CONSOLIDATE (merge these):
1. Merge [Item A] + [Item B] into: [new combined item] — rationale: [why]
2. Merge [Item C] + [Item D] into: [new combined item] — rationale: [why]

PRUNE (remove these):
1. Remove [Item] — rationale: [why it's safe to remove]
2. Remove [Item] — rationale: [why it's safe to remove]

KEEP AS-IS:
- [Item] — rationale: [why it earns its place]

RESULT: [Current count] -> [Recommended count] ([percentage] reduction)
WARNING: [Anything that looks prunable but should be kept — and why]
```

---

## Integration

Use with:
- `/undr` -> Check if the reduction went too far
- `/ctgp` -> Verify no important gaps were created by pruning
- `/cmp` -> Compare redundant items to pick the best one
