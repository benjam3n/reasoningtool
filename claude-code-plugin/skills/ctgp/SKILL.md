---
name: "ctgp - Category Gap Analysis"
description: Analyzes gaps within a category by comparing what should exist to what currently exists, then prioritizes missing items by importance.
---

# Category Gap Analysis

**Input**: $ARGUMENTS

---

## Step 1: Define the Category

State the category clearly and establish its scope.

```
CATEGORY: [The category being analyzed]
SCOPE: [What belongs in this category and what doesn't]
PURPOSE: [What this category exists to serve]
COMPLETENESS STANDARD: [What would "complete" look like for this category?]
```

---

## Step 2: List What Should Exist

Build the ideal inventory — everything a complete version of this category would contain.

```
IDEAL INVENTORY:
1. [Item 1] — purpose: [why it should exist]
2. [Item 2] — purpose: [why it should exist]
3. [Item 3] — purpose: [why it should exist]
...

DERIVATION METHOD: [How did you determine what should exist?
  Options: industry standard, first principles, user needs, reference implementation]

TOTAL IDEAL COUNT: [number]
```

---

## Step 3: List What Currently Exists

Inventory the actual current state.

```
CURRENT INVENTORY:
1. [Item 1] — status: [COMPLETE/PARTIAL/STUB]
2. [Item 2] — status: [COMPLETE/PARTIAL/STUB]
3. [Item 3] — status: [COMPLETE/PARTIAL/STUB]
...

TOTAL CURRENT COUNT: [number]
COVERAGE: [current / ideal as percentage]
```

---

## Step 4: Diff the Two Lists

Identify exactly what is missing, what is extra, and what is incomplete.

```
MISSING (in ideal but not in current):
1. [Item] — importance: [CRITICAL/HIGH/MEDIUM/LOW]
2. [Item] — importance: [CRITICAL/HIGH/MEDIUM/LOW]
...

INCOMPLETE (exists but not fully realized):
1. [Item] — what's missing: [specifics]
2. [Item] — what's missing: [specifics]

EXTRA (in current but not in ideal):
1. [Item] — verdict: [KEEP/EVALUATE/REMOVE] — rationale: [why]

GAP COUNT: [number missing + number incomplete]
```

---

## Step 5: Prioritize Missing Items

Rank gaps by importance and recommend what to add first.

```
PRIORITY RANKING:
1. [Item] — importance: [CRITICAL] — reason: [why this gap hurts most]
2. [Item] — importance: [HIGH] — reason: [why]
3. [Item] — importance: [HIGH] — reason: [why]
4. [Item] — importance: [MEDIUM] — reason: [why]
...

ADD FIRST: [Top 1-3 items with brief justification]
ADD NEXT: [Next tier]
ADD EVENTUALLY: [Low priority items]
SKIP: [Items from ideal list that aren't actually needed — and why]
```

---

## Integration

Use with:
- `/undr` -> Deep dive into why specific gaps are under-represented
- `/satr` -> Check if filling gaps would create over-saturation
- `/efrt` -> Estimate effort to fill the top-priority gaps
- `/benf` -> Estimate benefits of closing each gap
