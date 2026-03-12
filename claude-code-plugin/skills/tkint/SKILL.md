---
name: "tkint - Toolkit Integrity Analysis"
description: "Assess structural integrity of a collection, system, or toolkit. Finds broken references, orphans, circular dependencies, and naming inconsistencies."
output:
  format: "prose"
---

# Toolkit Integrity Analysis

**Input**: $ARGUMENTS

---

## Step 1: Map All Components

Enumerate every component in the collection/system being analyzed.

1. List each component with its identifier (name, ID, path)
2. For each component, note:
   - What it does (one-line description)
   - What it references (outgoing links/dependencies)
   - What references it (incoming links/dependencies)
3. Count the total

```
COMPONENT MAP:
Total: [count]

| # | Component | Description | References | Referenced By |
|---|-----------|-------------|------------|---------------|
| 1 | [name]    | [desc]      | [list]     | [list]        |
| 2 | [name]    | [desc]      | [list]     | [list]        |
...
```

If the collection is too large to enumerate fully, sample systematically (e.g., every Nth item, or all items in each category) and note the sampling strategy.

---

## Step 2: Check for Broken References

Find components that point to things that don't exist.

For each outgoing reference in Step 1:
1. Does the target exist?
2. If not, is it a typo, a deletion that wasn't cleaned up, or a planned-but-not-yet-created item?
3. What is the impact of the broken reference?

```
BROKEN REFERENCES:
- [component] -> [missing target] — Likely cause: [typo / deleted / planned]
- [component] -> [missing target] — Likely cause: [typo / deleted / planned]
...
TOTAL: [count] broken references
```

If zero: state "No broken references found."

---

## Step 3: Check for Orphans

Find components that nothing else references.

1. List all components with zero incoming references
2. For each, determine:
   - Is this an intentional entry point (top-level item users access directly)?
   - Is this genuinely orphaned (forgotten, disconnected, unreachable)?

```
ORPHANS:
- [component] — Verdict: [entry point / genuinely orphaned]
...
TOTAL: [count] orphans ([X] entry points, [Y] genuinely orphaned)
```

Not all orphans are problems — entry points are supposed to have zero incoming references. Focus on genuinely orphaned items.

---

## Step 4: Check for Circular Dependencies

Find components that reference each other in loops.

1. Trace reference chains looking for cycles
2. For each cycle found:
   - List the full loop
   - Assess whether the circularity is intentional (mutual dependencies) or accidental
   - If accidental, identify which link should be broken

```
CIRCULAR DEPENDENCIES:
- [A] -> [B] -> [C] -> [A] — Verdict: [intentional / accidental]
...
TOTAL: [count] cycles
```

If zero: state "No circular dependencies found."

---

## Step 5: Assess Naming Consistency

Check whether component names follow consistent conventions.

1. **Length**: Are names consistently short/long, or wildly varying?
2. **Format**: Is there a consistent format (camelCase, kebab-case, abbreviations)?
3. **Descriptiveness**: Can you guess what a component does from its name alone?
4. **Uniqueness**: Are any names confusingly similar?
5. **Conventions**: Are abbreviations used consistently (e.g., always "msg" or always "message", not both)?

```
NAMING ISSUES:
- [issue description] — Affected: [list of components]
...
NAMING CONSISTENCY SCORE: [HIGH / MODERATE / LOW]
```

---

## Step 6: Coverage and Gap Analysis

Assess whether the collection covers its intended scope:

1. What is the stated or implied purpose of the collection?
2. What categories or dimensions should it cover?
3. For each category, is coverage adequate?
4. Are there obvious gaps — things you'd expect to find but don't?
5. Are there redundancies — multiple components doing essentially the same thing?

```
COVERAGE:
- [category]: [adequate / thin / missing]
...

GAPS: [things that should exist but don't]
REDUNDANCIES: [things that overlap significantly]
```

---

## Step 7: Structural Improvements Summary

Prioritize all findings into an action list:

```
CRITICAL (broken functionality):
1. [fix broken reference / remove orphan / etc.]

IMPORTANT (structural health):
1. [resolve naming inconsistency / break circular dep / etc.]

NICE-TO-HAVE (polish):
1. [fill coverage gap / reduce redundancy / etc.]

OVERALL INTEGRITY: [STRONG / ADEQUATE / NEEDS WORK / FRAGILE]
```

---

## Integration

Use with:
- `/ctcov` -> Assess cognitive coverage of a thinking toolkit
- `/de` -> Plan the project to implement structural fixes
- `/se` -> Explore the full scope the toolkit should cover
- `/pv` -> Validate specific components after fixes
