---
name: "p8tier - Pick 8 Tier"
description: "Pick 8 skills from a specific tier. Maps user input to a tier level, filters the library, and returns a representative set. Standalone implementation of the TIER algorithm from /pick with N=8."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "tier", "quality"]
---

# Pick 8 Tier

**Input**: $ARGUMENTS

---

## Core Principles

1. **Tiers reflect maturity, not value.** Tier1 skills are the most tested and reliable. Tier4 skills are specialized or new. A tier4 skill can be exactly right for a specific task that no tier1 skill covers. Tier communicates confidence level, not importance.

2. **Tier names have synonyms.** Users will say "core" (tier1), "important" (tier2), "domain" (tier3), "specialized" (tier4), "experimental," or "category." The matcher must handle all of these.

3. **Eight skills per tier shows the tier's range.** Each tier contains dozens of skills. Eight is enough to see the tier's breadth without listing everything. The 8 should represent the tier's diversity, not just its top-ranked skills.

4. **Adjacent tier padding prevents empty results.** Some tiers may have fewer than 8 skills. When this happens, pad from the adjacent tier (tier2 pads from tier1 or tier3) rather than returning a short list.

5. **Tier context helps the user choose.** The output should explain what this tier MEANS — what level of reliability, specialization, and depth the user can expect from skills in this tier.

---

## Phase 1: Tier Mapping

```
[A] USER_INPUT: [from $ARGUMENTS]

[B] TIER_MATCH:

Step 1: Map input to tier:
    "core" | "tier1" | "essential" | "fundamental" → tier1
    "important" | "tier2" | "key" | "recommended" → tier2
    "domain" | "tier3" | "specialized domain" | "field-specific" → tier3
    "specialized" | "tier4" | "niche" | "specific" → tier4
    "category" | "router" | "orchestrator" → category
    "experimental" | "new" | "beta" | "untested" → experimental

Step 2: If no match: fuzzy match against tier descriptions
    tier1: "Core foundational skills — most tested, most broadly applicable"
    tier2: "Important skills — well-tested, frequently useful"
    tier3: "Domain-specific skills — deep expertise in particular areas"
    tier4: "Specialized skills — narrow focus, specific use cases"
    category: "Router skills — classify input and route to other skills"
    experimental: "Experimental skills — new, unproven, potentially valuable"

Step 3: If still no match: list available tiers and ask

    MATCHED_TIER: [tier name]
    MATCH_CONFIDENCE: [exact / synonym / fuzzy]
```

---

## Phase 2: Tier Profile

```
[C] TIER_PROFILE:

    Tier: [name]
    Description: [what this tier means]
    Total skills in tier: [N]
    Reliability expectation: [high / medium / low / unknown]
    Typical use: [when you'd specifically want this tier]

    Key characteristics:
        - Depth: [typical line count range]
        - Connectivity: [avg invokes + invoked_by]
        - Category spread: [how many categories represented]
```

---

## Phase 3: Selection

```
[D] POOL:

Step 1: Filter skills.json to MATCHED_TIER
    Pool size: [N]

Step 2: IF pool >= 8:
    Rank within tier by:
        CONNECTIVITY: invokes + invoked_by count
        DEPTH: line_count (higher = more developed)
        BREADTH: number of categories + tags
        COMPOSITE = CONNECTIVITY × 2 + DEPTH + BREADTH

    Diversity enforcement:
        - No more than 2 skills from any single category
        - Swap if needed: replace lowest-scoring duplicate-category with highest-scoring uncovered-category

    Take top 8 after diversity enforcement

Step 3: IF pool < 8:
    Take all [N] from matched tier
    Remaining = 8 - N
    Pad from adjacent tier:
        tier1 → pad from tier2
        tier2 → pad from tier1 or tier3
        tier3 → pad from tier2 or tier4
        tier4 → pad from tier3
        category → pad from tier1
        experimental → pad from tier4
    Mark padded skills as "[from adjacent tier: X]"

[E] SELECTED: [8 skills with scores and sources]
```

---

## Phase 4: Tier Landscape

```
[F] LANDSCAPE:

Step 1: Group the 8 picks by category
    [category]: /[id], /[id]
    [category]: /[id]
    ...

Step 2: Identify tier superstars:
    TOP_IN_TIER: /[id] — [why this is the tier's best skill]

Step 3: Identify underappreciated skills:
    UNDERRATED: /[id] — [why this deserves more attention]

Step 4: Tier comparison:
    How does this tier compare to adjacent tiers?
    - vs [higher tier]: [what this tier lacks / what it has that higher doesn't]
    - vs [lower tier]: [what this tier offers / what lower tier specializes in]
```

---

## Phase 5: Output

```
ALGORITHM: TIER
TIER: [matched tier]
MATCH: "[user input]" → "[tier name]" (confidence: [exact/synonym/fuzzy])
POOL: [N skills in tier]
PICKED: 8

TIER OVERVIEW:
  [tier name]: [1-2 sentence description]
  Reliability: [high/medium/low/unknown]
  Total skills: [N]
  Best for: [when you'd want skills from this tier]

8 SKILLS FROM [TIER]:

  1. /[id] — [title] ★ [if top-in-tier]
     [1-line description]
     Category: [cat] | Connections: [N] | Lines: [N]

  2. /[id] — [title]
     [1-line description]
     Category: [cat] | Connections: [N] | Lines: [N]

  [continue to 8...]

  [if any padded:]
  Note: Skills [N-8] are from adjacent tier [name] — included to fill the set

TIER LANDSCAPE:
  Categories represented: [list with counts]
  Top skill: /[id] — [why]
  Underrated: /[id] — [why]

TIER COMPARISON:
  vs [higher tier]: [key differences]
  vs [lower tier]: [key differences]

EXPLORE MORE:
  All [N] skills in [tier]: /pick [N] tier [tier name]
  Adjacent tier: /p8tier [adjacent tier name]
  Cross-tier best: /p10useful
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Failed tier match** | User input doesn't map to any tier | List available tiers with descriptions |
| **Category clustering** | 5+ picks from same category within the tier | Enforce 2-per-category cap |
| **Padding not disclosed** | Adjacent-tier skills mixed in without marking | Clearly mark "[from adjacent tier]" on padded picks |
| **Tier bias in description** | Lower tiers described as "worse" rather than "more specialized" | Frame each tier by its purpose, not its rank |
| **No tier context** | Skills listed without explaining what the tier means | Tier overview with reliability and use-case is mandatory |
| **Ignoring connectivity** | Skills ranked by line count only, missing hub skills | Connectivity should be weighted 2x in composite score |

---

## Depth Scaling

| Depth | Tier Mapping | Selection | Landscape |
|-------|-------------|-----------|-----------|
| 1x | Direct match only | Top 8 by connectivity | List only |
| 2x | Synonym + fuzzy matching | Composite score + diversity enforcement | Top + underrated + tier comparison |
| 4x | Full tier analysis with profile | Optimized selection with quality audit | Full landscape + cross-tier analysis |
| 8x | Tier evolution analysis (how tiers relate historically) | Complete tier audit | Tier ecosystem map with promotion candidates |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] User input mapped to a tier with confidence level
- [ ] Tier described with overview, reliability, and use-case
- [ ] Exactly 8 skills returned
- [ ] No more than 2 per category within the 8
- [ ] Adjacent-tier padding clearly marked if used
- [ ] Top-in-tier and underrated skills identified
- [ ] Tier comparison with adjacent tiers provided
- [ ] Path to explore more of the tier shown

---

## Integration

- **Shortcut for**: `/pick 8 tier $ARGUMENTS`
- **Use when**: You want to explore skills at a specific quality/maturity level
- **Routes to**: The 8 picked skills; `/p8tier [adjacent]` for comparison
- **Related**: `/p7cat` (filter by category instead), `/p10useful` (best across all tiers)
- **Differs from /p7cat**: cat filters by topic; tier filters by maturity level
- **Differs from /p10useful**: useful picks the best regardless of tier; tier constrains to one tier
- **Differs from /p10diverse**: diverse spans tiers and categories; tier focuses within one tier
