---
name: "p5similar - Pick 5 Similar"
description: "Find 5 skills most similar to a specified skill based on shared categories, tags, invocation partners, and functional overlap. Standalone implementation of the SIMILAR algorithm from /pick with N=5."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "similar", "related"]
output:
  format: "prose"
---

# Pick 5 Similar

**Input**: $ARGUMENTS

---

## Core Principles

1. **Similarity is multi-dimensional.** Two skills can be similar in category, in function, in the skills they invoke, in the tags they share, or in the type of input they accept. True similarity scores across all dimensions, not just one.

2. **Similar is not identical.** The most useful similar skills are those that approach the same problem from a slightly different angle. Perfect overlap means redundancy. Partial overlap means alternative perspective.

3. **Invocation partners reveal hidden similarity.** If two skills are both invoked by the same parent skill, they serve related roles even if their descriptions differ. Shared invocation context is a stronger signal than shared tags.

4. **Similarity has a direction.** Skill A can be similar to Skill B without B being equally similar to A. If A is a general analysis tool and B is a specialized variant, B is more similar to A than A is to B. Report the highest-overlap direction.

5. **Five similar skills define a neighborhood.** The 5 most similar skills to any given skill define its functional neighborhood — the cluster it belongs to. This helps the user understand where a skill fits in the larger ecosystem.

---

## Phase 1: Target Skill Analysis

```
[A] TARGET: /[skill from $ARGUMENTS]
[B] TARGET_METADATA:
    Title: [title]
    Description: [description]
    Tier: [tier]
    Categories: [list]
    Tags: [list]
    Invokes: [list]
    Invoked_by: [list]
    Line_count: [N]

[C] TARGET_PROFILE:
    Function: [analyze / decide / plan / create / validate / explore / diagnose]
    Domain: [technical / business / personal / general / meta]
    Input_type: [what does it accept?]
    Output_type: [what does it produce?]
```

---

## Phase 2: Similarity Scoring

Score every other skill in the library against the target.

```
[D] SCORING_DIMENSIONS:

For each candidate skill:

1. CATEGORY_OVERLAP:
    Shared categories / (target categories + candidate categories - shared)
    → Jaccard similarity × 3 (weight: high)

2. TAG_OVERLAP:
    Shared tags / (target tags + candidate tags - shared)
    → Jaccard similarity × 2 (weight: medium)

3. INVOCATION_OVERLAP:
    Step 1: Does candidate invoke any skill the target invokes? (+1 per shared)
    Step 2: Is candidate invoked by any skill that invokes the target? (+1 per shared)
    Step 3: Does candidate invoke the target or vice versa? (+2 — direct connection)
    → Sum (weight: high)

4. FUNCTION_MATCH:
    Same primary function as target? → +2
    Same secondary function? → +1
    Different function → 0

5. DESCRIPTION_SIMILARITY:
    Shared keywords between descriptions (excluding stop words)
    → Count / max(target_words, candidate_words) × 2

TOTAL_SIMILARITY = CATEGORY_OVERLAP + TAG_OVERLAP + INVOCATION_OVERLAP + FUNCTION_MATCH + DESCRIPTION_SIMILARITY
```

---

## Phase 3: Selection and Analysis

```
[E] SELECTION:

Step 1: Rank all candidates by TOTAL_SIMILARITY
Step 2: Take top 5
Step 3: For each of the 5, identify:
    - SHARED: What they have in common with the target
    - DIFFERENT: What they do differently
    - USE_CASE: When you'd use THIS skill instead of the target

[F] NEIGHBORHOOD_MAP:
    The target and its 5 similar skills form a neighborhood.
    What is this neighborhood's domain? [identify]
    What is this neighborhood's function? [identify]
    Are there sub-clusters within the 5? [identify]
```

---

## Phase 4: Output

```
ALGORITHM: SIMILAR
TARGET: /[id] — [title]
POOL: [total skills scored]
PICKED: 5

5 MOST SIMILAR SKILLS TO /[target]:

  1. /[id] — [title] — Similarity: [score]
     Shared: [what they have in common]
     Different: [what this does differently]
     Use instead when: [when you'd pick this over the target]
     Overlap: categories=[N shared] | tags=[N shared] | invocations=[N shared]

  2. /[id] — [title] — Similarity: [score]
     Shared: [common ground]
     Different: [distinction]
     Use instead when: [scenario]
     Overlap: categories=[N] | tags=[N] | invocations=[N]

  [continue to 5...]

NEIGHBORHOOD: /[target] belongs to the "[name]" neighborhood
  Domain: [domain]
  Function: [primary function of this cluster]
  Common thread: [what unites these 6 skills]

DISTINCTION GUIDE:
  If you need [X], use /[target]
  If you need [Y], use /[similar-1]
  If you need [Z], use /[similar-2]
  ...
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Surface similarity only** | All 5 share categories but do completely different things | Include invocation overlap and function match in scoring |
| **Same skill, different name** | A similar skill is functionally identical to the target | Note it as "near-duplicate" — user should pick one and ignore the other |
| **Ignoring invocation links** | Skills that share invocation partners scored low | Invocation overlap is a strong signal — weight it appropriately |
| **No distinction guide** | User gets 5 similar skills but can't tell them apart | "Use instead when" is mandatory for each pick |
| **Target is unique** | No skill scores above a minimal threshold | Report: "Target has no close neighbors — it's a unique skill" |
| **Missing the obvious** | A clearly related skill is not in the top 5 | Check direct invokes/invoked_by — these should always rank high |

---

## Depth Scaling

| Depth | Scoring | Analysis | Output |
|-------|---------|----------|--------|
| 1x | Category + tag overlap only | Top 5 list | Basic similarity scores |
| 2x | All 5 dimensions | Shared/different for each pick | Full output with neighborhood and distinction guide |
| 4x | All dimensions + read target and candidate SKILL.md for deep comparison | Functional analysis of neighborhood | Detailed use-case matrix |
| 8x | Full library scoring + cluster analysis | Neighborhood comparison across the library | Comprehensive similarity map with transition guide |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Target skill metadata extracted
- [ ] All candidates scored on 5 similarity dimensions
- [ ] Exactly 5 skills returned
- [ ] Each pick has shared/different/use-instead-when
- [ ] Neighborhood identified and named
- [ ] Distinction guide provided (when to use each)
- [ ] No near-duplicates passed off as distinct skills

---

## Integration

- **Shortcut for**: `/pick 5 similar $ARGUMENTS`
- **Use when**: You know a skill you like and want to find alternatives
- **Routes to**: The 5 similar skills; `/p10complement` for skills that pair (opposite of similar)
- **Related**: `/p10complement` (opposite — finds gaps, not overlap)
- **Differs from /p10complement**: complement finds skills that DIFFER from the target; similar finds skills that MATCH
- **Differs from /p7cat**: cat finds skills in a category; similar finds skills like a specific skill regardless of category
