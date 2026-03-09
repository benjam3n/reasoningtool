---
name: "p10random - Pick 10 Random"
description: "Pick 10 skills uniformly at random from the full library. No bias, no optimization — pure serendipitous discovery. Standalone implementation of the RANDOM algorithm from /pick."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "random", "serendipity"]
---

# Pick 10 Random

**Input**: $ARGUMENTS

---

## Core Principles

1. **Random is a feature, not a bug.** Optimization algorithms surface the same high-tier skills repeatedly. Random selection breaks this pattern and surfaces skills the user would never encounter through goal-directed search.

2. **No filtering, no weighting.** Every skill in the library has an equal probability of selection. Tier1 and tier4, well-known and obscure — all equally likely. This is the defining property. If you weight by anything, it's not random.

3. **The pool can be constrained.** While selection within the pool is uniform, the pool itself can be narrowed. `/p10random tier3` or `/p10random Research` constrains the pool first, then picks randomly within it. The constraint is explicit, not hidden.

4. **Random selections demand context.** Because the picks are not curated for a purpose, each one needs enough description for the user to understand why they might care. Random without context is just noise.

5. **Re-rolling is expected.** Random is low-commitment. If the 10 picks don't interest the user, running it again costs nothing and produces a completely different set. This is a feature of the algorithm.

---

## Phase 1: Pool Definition

```
[A] POOL_CONSTRAINT: [parse from $ARGUMENTS — if any]

Step 1: Check if $ARGUMENTS contains a constraint:
    - Tier name (e.g., "tier3", "core", "experimental") → filter to that tier
    - Category name (e.g., "Research", "Decision") → filter to that category
    - No constraint → use full library

Step 2: Load the pool
    POOL_SOURCE: [full library / tier: X / category: X]
    POOL_SIZE: [N skills in pool]

Step 3: Verify pool is large enough
    IF pool < 10: → WARNING: Pool has only [N] skills. Returning all [N].
    IF pool >= 10: → proceed with random selection
```

---

## Phase 2: Random Selection

```
[B] SELECTION:

Step 1: Assign each skill in the pool a random position
Step 2: Take the first 10 (or all if pool < 10)
Step 3: No re-ranking, no re-ordering by quality — preserve the random order
    (This communicates that the ordering is arbitrary, not a ranking)

[C] SELECTED:
    1. [skill ID]
    2. [skill ID]
    ...
    10. [skill ID]
```

---

## Phase 3: Context Generation

For each selected skill, provide enough context for the user to decide if it interests them.

```
[D] CONTEXTUALIZED:

For each skill:
    Step 1: Read its metadata from skills.json (title, description, tier, categories, tags)
    Step 2: Summarize in one line what it DOES (not what it IS)
    Step 3: Note its tier and primary category
    Step 4: Flag if it's particularly unusual or specialized (surprise value)
```

---

## Phase 4: Post-Selection Analysis

```
[E] DISTRIBUTION_ANALYSIS:

    Categories represented: [list with counts]
    Tiers represented: [list with counts]
    Functions represented: [analysis/decision/planning/creation/validation — which are present]

    ACCIDENTAL_COVERAGE: [did random selection happen to cover anything well?]
    NOTABLE_CLUSTERS: [did random selection cluster in any area?]
    SURPRISE_PICKS: [which of the 10 are least commonly seen in curated lists?]
```

---

## Phase 5: Output

```
ALGORITHM: RANDOM
POOL: [pool size] ([full library / constrained to: X])
PICKED: 10

  1. /[id] — [title]
     [1-line: what it does]
     Tier: [tier] | Category: [category]

  2. /[id] — [title]
     [1-line: what it does]
     Tier: [tier] | Category: [category]

  [continue to 10...]

DISTRIBUTION:
  Categories: [list]
  Tiers: [list]
  Functions: [list]

SURPRISE PICKS: [which of these are least commonly encountered]

NOTE: This is a random selection — not a recommendation.
Re-run /p10random for a completely different set.
For curated picks, try /p10goal [your goal] or /p10useful.
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Hidden weighting** | Selection clearly biased toward high-tier or popular skills | Verify: every skill in pool had equal chance. Do not "improve" random |
| **No context** | Skill listed with just ID and title — user can't evaluate | Provide 1-line action description for each pick |
| **Treating random as recommendation** | Output implies these are the "right" skills | Explicitly state "this is random, not curated" |
| **Pool constraint not honored** | User said "random tier3" but tier1 skills appear | Verify pool was filtered before selection |
| **Re-ranking after selection** | Picks are subtly re-ordered by quality | Preserve random order — do not sort by tier or score |
| **Insufficient pool warning** | Pool has 5 skills but output says "picked 10" | If pool < N, warn and return all available |

---

## Depth Scaling

| Depth | Pool | Selection | Context |
|-------|------|-----------|---------|
| 1x | Full library, no analysis | 10 random picks | ID + title + tier |
| 2x | Pool + constraint handling | 10 random + distribution analysis | 1-line descriptions + surprise flags |
| 4x | Pool analysis + size verification | 10 random + full distribution + coverage check | Descriptions + connections + suggested exploration order |
| 8x | Pool comparison across tiers/categories | Multiple random draws + statistical coverage | Full skill summaries + comparison to curated alternatives |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Pool constraint parsed and applied (if any)
- [ ] Selection is genuinely random (no hidden weighting)
- [ ] Exactly 10 skills returned (or all if pool < 10)
- [ ] Each pick has a 1-line action description
- [ ] Distribution analysis shows what categories/tiers/functions are represented
- [ ] Output explicitly states this is random, not curated
- [ ] Suggestion provided for curated alternatives

---

## Integration

- **Shortcut for**: `/pick 10 random`
- **Use when**: You want serendipitous discovery, not targeted search
- **Routes to**: The 10 picked skills; re-run for different set
- **Related**: `/p10diverse` (systematic coverage), `/p10useful` (quality-ranked)
- **Differs from /p10diverse**: diverse guarantees coverage; random does not
- **Differs from /p10useful**: useful ranks by quality; random ignores quality
- **Variant**: `/p10random [tier/category]` constrains the pool before random selection
