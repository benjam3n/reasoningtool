---
name: "p10diverse - Pick 10 Diverse"
description: "Pick 10 skills maximizing coverage across different categories, tiers, and functions. Produces the broadest possible sample of the skill library. Standalone implementation of the DIVERSE algorithm from /pick."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "diverse", "coverage"]
---

# Pick 10 Diverse

**Input**: $ARGUMENTS

---

## Core Principles

1. **Diversity is coverage, not randomness.** Random selection sometimes produces diverse results, sometimes clusters. Diverse selection guarantees coverage by construction — it is an anti-clustering algorithm.

2. **Five dimensions of diversity.** Skills vary by category, tier, function (analyze/decide/plan/create/validate), workflow phase (early/mid/late), and connectivity (standalone vs hub). True diversity covers all five dimensions, not just category.

3. **Round-robin prevents dominance.** If you pick the "best" from each category, large categories dominate because they have higher-quality peaks. Round-robin across categories, then within categories by tier, prevents this.

4. **Mandatory function coverage.** The 10 picks must include at least one skill from each of these functions: analysis, decision, planning, validation, and exploration. Missing any function creates a blind spot in the user's toolkit.

5. **Surprise has learning value.** A diverse set should include at least one skill the user probably hasn't encountered. If all 10 are well-known, the diversity is only surface-level.

---

## Phase 1: Dimension Mapping

```
[A] CATEGORY_MAP:

Step 1: List all categories in skills.json with skill counts
    | Category | Skill Count | Representative Skills |
    |----------|-------------|----------------------|
    | [cat]    | [N]         | [top 3 by tier]      |

Step 2: Identify underrepresented categories (fewer than 5 skills)
Step 3: Note: underrepresented categories get priority — their skills are rarer

[B] FUNCTION_MAP:
    ANALYSIS: [skill IDs whose primary purpose is understanding/decomposing]
    DECISION: [skill IDs whose primary purpose is choosing/comparing]
    PLANNING: [skill IDs whose primary purpose is sequencing/scoping]
    CREATION: [skill IDs whose primary purpose is producing/writing]
    VALIDATION: [skill IDs whose primary purpose is checking/testing]
    EXPLORATION: [skill IDs whose primary purpose is discovering/generating]
    DIAGNOSIS: [skill IDs whose primary purpose is finding problems/causes]

[C] TIER_MAP:
    tier1 (core): [count]
    tier2 (important): [count]
    tier3 (domain): [count]
    tier4 (specialized): [count]
    category (router): [count]
    experimental: [count]
```

---

## Phase 2: Round-Robin Selection

```
[D] SELECTION:

Step 1: Order categories by size (smallest first — rare categories get first pick)
Step 2: Round-robin: take the highest-tier skill from each category
    - Skip categories already represented
    - Continue until 10 slots filled or all categories visited
Step 3: If fewer than 10 categories: take second-best from largest categories
Step 4: If more than 10 categories: prioritize categories covering unfilled functions

[E] FUNCTION_COVERAGE_CHECK:
    After selection, verify:
    - Analysis represented? [Y/N — if N, swap weakest pick for best analysis skill]
    - Decision represented? [Y/N — if N, swap]
    - Planning represented? [Y/N — if N, swap]
    - Validation represented? [Y/N — if N, swap]
    - Exploration represented? [Y/N — if N, swap]
```

---

## Phase 3: Diversity Verification

```
[F] DIVERSITY_METRICS:

    Categories covered: [N] out of [total]
    Tiers covered: [list]
    Functions covered: [N] out of 7
    Phases covered: [early/mid/late — which are present]
    Connectivity mix: [N standalone] + [M hub skills]

    SURPRISE_CHECK:
    - How many of these 10 are well-known (tier1/tier2 with high connectivity)? [N]
    - If N > 7: swap 1-2 well-known for lesser-known skills from underrepresented areas

[G] DIVERSITY_SCORE:
    = (categories_covered / total_categories × 25)
    + (functions_covered / 7 × 25)
    + (tiers_covered / 6 × 25)
    + (surprise_picks / 10 × 25)
    = [0-100]
    Target: >= 70
```

---

## Phase 4: Output

```
ALGORITHM: DIVERSE
POOL: [total skills in library]
PICKED: 10
DIVERSITY SCORE: [X/100]

  1. /[id] — [title]
     Category: [cat] | Tier: [tier] | Function: [func]
     [1-line description]

  2. /[id] — [title]
     Category: [cat] | Tier: [tier] | Function: [func]
     [1-line description]

  [continue to 10...]

COVERAGE:
  Categories: [N/total] — [list covered]
  Functions: [N/7] — [list covered]
  Tiers: [list covered]
  Phases: [list covered]

GAPS:
  Categories NOT covered: [list]
  Functions NOT covered: [list — if any]
  To fill gaps, add: /[suggested skill for each gap]

SUGGESTED EXPLORATION ORDER:
  Start with: /[most accessible skill]
  Then try: /[skill that builds on first]
  Deep dive: /[most specialized pick]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Category clustering** | 4+ picks from same category | Round-robin prevents this — verify the algorithm ran |
| **Tier bias** | All picks are tier1/tier2 | Include at least 1 tier3 and 1 tier4 pick |
| **Function gap** | No validation or no planning skill | Mandatory coverage check — swap to fill |
| **Popularity bias** | All 10 are skills every user already knows | Surprise check — include 2+ lesser-known picks |
| **Random masquerading as diverse** | No systematic coverage, just scattered picks | Verify diversity score >= 70 |
| **Ignoring user context** | Diverse set doesn't account for $ARGUMENTS | If $ARGUMENTS provided, weight toward relevant categories |

---

## Depth Scaling

| Depth | Mapping | Selection | Verification |
|-------|---------|-----------|-------------|
| 1x | Category counts only | Round-robin by category | Function coverage check |
| 2x | Full 5-dimension mapping | Round-robin + function coverage swaps | Diversity score calculation |
| 4x | Dimension mapping + connectivity analysis | Optimized selection maximizing diversity score | Full verification + gap analysis |
| 8x | Complete library analysis | Simulated annealing on diversity score | Cross-validation with alternative diverse sets |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All categories in library identified and counted
- [ ] Round-robin selection performed (smallest categories first)
- [ ] All 5 mandatory functions represented (analysis, decision, planning, validation, exploration)
- [ ] Exactly 10 skills returned
- [ ] At least 2 lesser-known or surprise picks included
- [ ] Diversity score calculated and >= 70
- [ ] Gaps explicitly identified with suggested additions
- [ ] Exploration order suggested

---

## Integration

- **Shortcut for**: `/pick 10 diverse`
- **Use when**: You want a broad sample of the skill library, not a targeted search
- **Routes to**: The 10 picked skills; `/p10useful` for quality-ranked alternative
- **Related**: `/p10random` (random, not guaranteed diverse), `/p10useful` (quality-ranked)
- **Differs from /p10random**: random may cluster; diverse guarantees coverage
- **Differs from /p10useful**: useful ranks by quality; diverse ranks by coverage
- **Differs from /p10complement**: complement centers on one skill; diverse covers the whole library
