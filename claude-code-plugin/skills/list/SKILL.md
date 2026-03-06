---
name: "list - Build High-Quality Lists"
description: Create rigorous, useful lists with clear scope, ordering logic, coverage checks, and concise rationale per item.
---

# List

**Input**: $ARGUMENTS

---

## Purpose

Produce great lists that are clear, complete enough for the goal, and usable immediately.

## Steps

### 1. Define List Contract

State:
- LIST_GOAL: what the list is for.
- AUDIENCE: who will use it.
- DEPTH: quick / standard / exhaustive.
- ORDER_BASIS: ranked / grouped / chronological / dependency.

### 2. Set Inclusion Rules

Write explicit include/exclude rules before generating items.

### 3. Generate Candidate Items

Generate broadly first.
Then remove duplicates and merge overlaps.

### 4. Order and Label

For each item include:
- ITEM
- WHY_IT_MATTERS (one sentence)
- PRIORITY or GROUP

### 5. Coverage Check

Check for obvious missing categories.
If missing, add items.

### 6. Output

Output only the final list and optional brief assumptions.

---

## Output Format

```text
LIST_GOAL: ...
ORDER_BASIS: ...

1. [item]
   WHY_IT_MATTERS: ...
2. [item]
   WHY_IT_MATTERS: ...
...

ASSUMPTIONS:
- ...
```
