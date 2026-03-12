---
name: "p7cat - Pick 7 Category"
description: "Pick 7 skills from a specific category or matching a category pattern. Fuzzy-matches the user's input to known categories and returns the best skills from the match. Standalone implementation of the CATEGORY algorithm from /pick with N=7."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "category", "filter"]
output:
  format: "prose"
---

# Pick 7 Category

**Input**: $ARGUMENTS

---

## Core Principles

1. **Fuzzy matching is essential.** Users will say "research" when the category is "Research & Analysis." They'll say "decisions" when the category is "Decision & Comparison." The matcher must handle partial, case-insensitive, and synonym-based matches.

2. **Category boundaries are porous.** Skills tagged in one category often serve adjacent categories. When a matched category has fewer than 7 skills, extend to adjacent categories rather than returning a short list.

3. **Within-category ranking uses tier and depth.** Once the category is matched, rank skills by tier score and line count (proxy for depth). The highest-tier, deepest skills rise to the top.

4. **Seven gives a comprehensive view.** 7 skills from one category shows the user the full range of that category's capabilities — from core tools to specialized variants. It's enough for category mastery, not so many as to overwhelm.

5. **The category itself is informative.** Part of the output should describe what this category IS and what it covers, not just list its skills. The user should understand the category's scope.

---

## Phase 1: Category Matching

```
[A] USER_INPUT: [from $ARGUMENTS]

[B] CATEGORY_MATCH:

Step 1: Load all known categories from skills.json
Step 2: Score each category against user input:
    - Exact match: 10
    - Contains user input as substring: 7
    - User input contains category as substring: 5
    - Shared significant word (excluding "and", "the", "of"): 3
    - Synonym match ("research" ↔ "analysis", "decision" ↔ "choice"): 3
Step 3: Select highest-scoring category

    MATCHED_CATEGORY: [category name]
    MATCH_CONFIDENCE: [exact / partial / fuzzy]
    MATCH_SCORE: [N]

Step 4: If no match scores above 2:
    → Ask user: "I couldn't confidently match '[input]' to a category. Available categories are: [list]. Which did you mean?"

[C] CATEGORY_DESCRIPTION:
    What this category covers: [describe in 1-2 sentences]
    Typical use cases: [list 3-4]
    Adjacent categories: [list categories that share skills/tags with this one]
```

---

## Phase 2: Skill Pool and Ranking

```
[D] CATEGORY_POOL:

Step 1: Filter skills.json to skills in MATCHED_CATEGORY
    Pool size: [N]

Step 2: IF pool >= 7:
    Rank by:
        TIER_SCORE: tier1=10, tier2=8, category=7, tier3=4, tier4=2
        DEPTH_SCORE: line_count > 200 = 4, 100-200 = 3, 50-100 = 2, <50 = 1
        TOTAL = TIER_SCORE + DEPTH_SCORE
    Take top 7

Step 3: IF pool < 7:
    Take all from matched category
    Remaining slots = 7 - pool
    Fill from adjacent categories:
        - Skills sharing tags with matched-category skills
        - Skills invoked by matched-category skills
        - Skills in the nearest related category
    Rank adjacent candidates by relevance to matched category
    Take top [remaining slots]

[E] SELECTED: [list of 7 skills with scores]
```

---

## Phase 3: Category Landscape

```
[F] LANDSCAPE:

Step 1: Group the 7 picks by function:
    Analysis skills: [list]
    Decision skills: [list]
    Planning skills: [list]
    Validation skills: [list]
    Other: [list]

Step 2: Identify the category's "star" skill:
    The single most-used/highest-tier/most-connected skill in this category
    STAR: /[id] — [why it's the star]

Step 3: Identify the category's "hidden gem":
    A lower-tier or less-connected skill that is surprisingly useful
    GEM: /[id] — [why it's worth knowing]

Step 4: What's NOT in this category that users often need alongside it?
    COMPLEMENT_CATEGORIES: [list 1-2 categories that pair well]
```

---

## Phase 4: Output

```
ALGORITHM: CATEGORY
CATEGORY: [matched category]
MATCH: "[user input]" → "[matched category]" (confidence: [exact/partial/fuzzy])
POOL: [N skills in category]
PICKED: 7

CATEGORY OVERVIEW:
  [1-2 sentence description of what this category covers]
  Use cases: [list 3-4 typical scenarios]

7 SKILLS FROM [CATEGORY]:

  1. /[id] — [title] ★ [if star skill]
     [1-line description]
     Tier: [tier] | Lines: [N] | Score: [total]

  2. /[id] — [title]
     [1-line description]
     Tier: [tier] | Lines: [N] | Score: [total]

  [continue to 7...]

  [if any from adjacent categories:]
  Note: Skills [N-7] are from adjacent category "[name]" — included because [reason]

CATEGORY LANDSCAPE:
  Analysis: [skills]
  Decision: [skills]
  Planning: [skills]
  Validation: [skills]

STAR SKILL: /[id] — [why]
HIDDEN GEM: /[id] — [why]

COMPLEMENT: For skills that pair well with [category], see: [adjacent categories]
  Try: /p7cat [adjacent category name]

REMAINING: [N - 7] more skills in this category not shown
  Use /pick [N] category [name] to see more
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Failed match** | User input doesn't match any category | List available categories and ask for clarification |
| **Wrong match** | Fuzzy match selects wrong category (e.g., "planning" matches "Organizational Planning" when user meant "Project Planning") | Show match and confidence — let user correct |
| **Thin category** | Matched category has < 3 skills | Extend to adjacent categories transparently |
| **All tier4** | Category is specialized and all skills are tier4 | Still rank by depth/quality — tier4 skills vary in quality |
| **No landscape** | Skills listed without context about what the category is | Category description and use cases are mandatory |
| **Missing adjacencies** | User doesn't learn about related categories | Always suggest 1-2 complement categories |

---

## Depth Scaling

| Depth | Matching | Ranking | Landscape |
|-------|---------|---------|-----------|
| 1x | Best match, no disambiguation | Tier score only | List only |
| 2x | Fuzzy match with confidence | Tier + depth + adjacency filling | Star + gem + complement |
| 4x | Multi-match with disambiguation if ambiguous | Full scoring + quality audit | Full landscape + inter-category relationships |
| 8x | Semantic category analysis | Complete category audit with quality ranking | Category map with all connections and usage patterns |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] User input fuzzy-matched to a category with confidence level
- [ ] Category described with overview and use cases
- [ ] Exactly 7 skills returned
- [ ] Adjacent categories used if matched category is too small
- [ ] Skills ranked by tier + depth
- [ ] Star skill and hidden gem identified
- [ ] Complement categories suggested
- [ ] Remaining skills count noted

---

## Integration

- **Shortcut for**: `/pick 7 category $ARGUMENTS`
- **Use when**: You know the category you want to explore
- **Routes to**: The 7 picked skills; `/p7cat [adjacent]` for related categories
- **Related**: `/p8tier` (filter by tier instead), `/p10diverse` (cross-category selection)
- **Differs from /p8tier**: cat filters by topic; tier filters by quality level
- **Differs from /p10diverse**: diverse spans all categories; cat goes deep in one
