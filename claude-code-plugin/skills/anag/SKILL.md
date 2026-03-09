---
name: "anag - Analogy Generation"
description: Explains concept X in terms of familiar concept Y by mapping structural correspondence, then testing where the analogy breaks.
---

# Analogy Generation

**Input**: $ARGUMENTS

---

## Step 1: Identify the Source Concept

What needs to be explained through analogy?

```
SOURCE CONCEPT: [the thing to explain]
KEY PROPERTIES: [list 3-5 structural features that define how it works]
1. [property — e.g., "has multiple competing inputs"]
2. [property — e.g., "output depends on threshold"]
3. [property — e.g., "feedback loop adjusts sensitivity"]
...

AUDIENCE: [who is this analogy for? what do they already understand?]
```

---

## Step 2: Find a Target Domain

Search for a familiar domain that shares the same structure. The best analogies:
- Come from the audience's everyday experience
- Match on structure (how things relate), not surface (what things look like)
- Are concrete and visual

Generate 3 candidate analogies:

```
CANDIDATES:
1. [familiar concept] — matches on: [which properties]
2. [familiar concept] — matches on: [which properties]
3. [familiar concept] — matches on: [which properties]

BEST FIT: [which candidate and why]
```

---

## Step 3: Map the Correspondence

For the best-fit analogy, map each part of the source to its counterpart.

```
MAPPING:
| Source (unfamiliar) | Target (familiar) | Relationship preserved |
|--------------------|-------------------|----------------------|
| [element A] | [maps to X] | [what structural relationship is the same] |
| [element B] | [maps to Y] | [what structural relationship is the same] |
| [element C] | [maps to Z] | [what structural relationship is the same] |
...
```

---

## Step 4: Build the Analogy

Write the analogy as a natural explanation. Structure: "X is like Y. Specifically, [mapping]. This means [insight]."

```
ANALOGY:

[The complete analogy, written in plain language, ready to use in conversation or teaching]
```

---

## Step 5: Test the Limits

Every analogy breaks somewhere. Find where.

```
WHERE IT BREAKS:
1. [difference] — Source does X but target does Y. This matters because [consequence].
2. [difference] — Source has [feature] with no target equivalent.
...

CAVEATS TO INCLUDE: [which breaks are important enough to mention when using this analogy]
MISLEADING IMPLICATIONS: [what wrong conclusions someone might draw if they take the analogy too far]
```

---

## Step 6: Final Output

Present the analogy with its caveats in a clean, usable format.

```
FINAL ANALOGY:

[Analogy text]

NOTE: This analogy breaks when [key caveat]. Specifically, [what's different].
```

---

## Integration

Use with:
- `/teach` -> When the analogy is part of a larger explanation
- `/sim` -> When the source concept needs simplification before analogy
- `/deb` -> When the analogy is being used as an argument and needs stress-testing
- `/sp` -> When the question "explain X like Y" needs sharpening first
