---
name: "p10useful - Pick 10 Useful"
description: "Pick the 10 most generally useful skills based on tier, connectivity, breadth, and depth. The 'greatest hits' of the skill library. Standalone implementation of the USEFUL algorithm from /pick."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "useful", "quality"]
output:
  format: "prose"
---

# Pick 10 Useful

**Input**: $ARGUMENTS

---

## Core Principles

1. **Usefulness is breadth times depth.** A skill is useful if it applies to many situations (breadth) AND produces substantial output when it does (depth). High breadth + low depth = superficial. Low breadth + high depth = niche. High both = useful.

2. **Connectivity is a signal.** Skills that invoke many other skills or are invoked by many other skills sit at network hubs. Hub skills are useful because they are entry points to larger capability chains.

3. **Tier reflects community validation.** Higher-tier skills have survived more usage and refinement. Tier is not a perfect proxy for usefulness, but it is a strong prior.

4. **Category diversity prevents echo chambers.** The 10 most useful skills should not all be analysis skills. Cap any single category at 3 to ensure the user gets a well-rounded toolkit.

5. **The list should be defensible.** For each pick, you should be able to answer: "If a new user could only learn 10 skills, why THIS one?" If you can't answer that, the pick is not in the top 10.

---

## Phase 1: Universal Scoring

Score every skill in the library on four dimensions.

```
[A] SCORING_DIMENSIONS:

For each skill:

1. TIER_SCORE:
    tier1 = 10
    tier2 = 8
    category = 7
    experimental = 6
    tier3 = 4
    tier4 = 2

2. CONNECTIVITY:
    Count of (invokes + invoked_by)
    Skills with 0 connections = 0
    Skills with 1-3 connections = 2
    Skills with 4-7 connections = 4
    Skills with 8+ connections = 6

3. BREADTH:
    Count of non-empty categories + count of tags
    0-2 = 1
    3-5 = 2
    6-8 = 3
    9+ = 4

4. DEPTH_PROXY:
    line_count > 200 = 4
    line_count 100-200 = 3
    line_count 50-100 = 2
    line_count < 50 = 1

TOTAL = TIER_SCORE + CONNECTIVITY + BREADTH + DEPTH_PROXY
```

---

## Phase 2: Ranking and Diversity Enforcement

```
[B] RANKING:

Step 1: Sort all skills by TOTAL score (descending)
Step 2: Take top 10

Step 3: DIVERSITY CHECK:
    Count skills per category in the top 10
    IF any category has > 3 skills:
        → Remove the lowest-scoring excess skills from that category
        → Replace with the highest-scoring skills from underrepresented categories
    Repeat until no category has > 3 skills

Step 4: FUNCTION CHECK:
    Verify at least 4 of these functions are represented:
    [analysis / decision / planning / creation / validation / exploration / diagnosis]
    IF < 4:
        → Swap lowest-scoring pick for highest-scoring from missing function
```

---

## Phase 3: Justification

For each of the 10 picks, generate a defensible justification.

```
[C] JUSTIFICATIONS:

For each pick:
    QUESTION: "If a new user could only learn 10 skills, why this one?"
    ANSWER: [1-2 sentence justification]
    SCORE_BREAKDOWN: tier=[X] + connectivity=[Y] + breadth=[Z] + depth=[W] = [total]
    UNIQUE_VALUE: [what does this skill do that no other top-10 skill does?]
```

---

## Phase 4: Output

```
ALGORITHM: USEFUL
POOL: [total skills scored]
PICKED: 10

TOP 10 MOST USEFUL SKILLS:
  1. /[id] — [title] — Score: [X] (tier=[T], connections=[C], breadth=[B], depth=[D])
     [1-line description]
     Why top 10: [justification]

  2. /[id] — [title] — Score: [X] (tier=[T], connections=[C], breadth=[B], depth=[D])
     [1-line description]
     Why top 10: [justification]

  [continue to 10...]

CATEGORY DISTRIBUTION:
  [category]: [N picks]
  [category]: [N picks]
  ...

FUNCTION COVERAGE:
  [analysis/decision/planning/creation/validation/exploration/diagnosis]: [which are covered]

HONORABLE MENTIONS (skills 11-15):
  11. /[id] — [title] — Score: [X]
  12. ...

NOTABLE ABSENCES:
  [any skill type or category conspicuously missing from the top 10]
  To fill: /[suggested skill]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Category clustering** | 5+ picks from analysis or decision skills | Enforce 3-per-category cap |
| **Tier-only ranking** | Top 10 are just the 10 highest-tier skills regardless of connectivity/breadth | All 4 scoring dimensions must contribute |
| **No justification** | Picks listed without explaining why they're useful | "Why top 10?" answer is mandatory for each |
| **Stale results** | Same 10 every time regardless of library changes | Score should reflect current skills.json state |
| **Missing functions** | All picks are analytical — no decision, planning, or creation skills | Function check is mandatory |
| **Line count gaming** | Long but shallow skill scores high on depth proxy | Depth proxy is line_count, but justification checks actual quality |

---

## Depth Scaling

| Depth | Scoring | Ranking | Justification |
|-------|---------|---------|---------------|
| 1x | Tier + connectivity only | Top 10 with category cap | 1-line descriptions |
| 2x | All 4 dimensions | Top 10 + diversity + function check | Full justifications + honorable mentions |
| 4x | 4 dimensions + quality audit of candidates | Optimized ranking with diversity/function iteration | Justifications + notable absences + comparison |
| 8x | Full library audit with quality-adjusted scores | Multi-pass ranking with cross-validation | Defensible essay per pick + alternative top-10 sets |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All skills scored on 4 dimensions (tier, connectivity, breadth, depth)
- [ ] Top 10 selected with diversity enforcement (no category > 3)
- [ ] At least 4 functions represented in the top 10
- [ ] Each pick has a defensible "why top 10" justification
- [ ] Exactly 10 skills returned
- [ ] Score breakdown shown for each pick
- [ ] Honorable mentions (11-15) included
- [ ] Notable absences identified

---

## Integration

- **Shortcut for**: `/pick 10 useful`
- **Use when**: You want the objectively best general-purpose skills
- **Routes to**: The 10 picked skills; `/p10diverse` for coverage-maximizing alternative
- **Related**: `/p10diverse` (coverage over quality), `/p10random` (serendipity over quality)
- **Differs from /p10diverse**: diverse maximizes coverage; useful maximizes quality
- **Differs from /p10random**: random has no quality bias; useful is entirely quality-driven
- **Differs from /p10goal**: goal matches to a specific purpose; useful is purpose-agnostic
