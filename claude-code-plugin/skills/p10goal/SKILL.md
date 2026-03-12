---
name: "p10goal - Pick 10 Goal"
description: "Pick 10 skills most likely to help achieve a specific goal. Decomposes the goal into sub-capabilities and selects skills covering each. Standalone implementation of the GOAL algorithm from /pick."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "goal", "capability"]
output:
  format: "prose"
---

# Pick 10 Goal

**Input**: $ARGUMENTS

---

## Core Principles

1. **Goals decompose into capabilities.** "Launch a product" requires understanding (analysis), choosing (decision), sequencing (planning), building (creation), and checking (validation). Each capability maps to a skill function. Missing a capability means missing a skill.

2. **Coverage beats depth.** 10 skills covering 5 capabilities beats 10 skills deeply covering 2 capabilities. The user can go deeper on any one later. The first pass should ensure nothing important is missed.

3. **Tier is a proxy for reliability.** Higher-tier skills have been used more, refined more, and handle edge cases better. Weight tier when scoring, but don't let it exclude a tier3 skill that perfectly fits a capability no tier1 skill covers.

4. **Compound skills multiply value.** A skill that invokes other skills (a compound skill) covers multiple capabilities in one pick. These are high-value selections because they expand the effective toolkit beyond 10.

5. **The gap matters more than the pick.** After picking 10, the most important output is what they DON'T cover. The user should know their blind spots.

---

## Phase 1: Goal Decomposition

```
[A] GOAL: [from $ARGUMENTS]

[B] SUB-CAPABILITIES:

Step 1: Decompose the goal into what must happen:
    C1. What must be UNDERSTOOD? → [specific knowledge/analysis needed]
    C2. What must be DECIDED? → [specific choices to make]
    C3. What must be PLANNED? → [specific sequences/timelines]
    C4. What must be VALIDATED? → [specific things to check/test]
    C5. What must be CREATED? → [specific outputs to produce]
    C6. What could go WRONG? → [specific risks/failure modes]
    C7. What is UNKNOWN? → [specific questions to answer]

Step 2: Rate each sub-capability:
    - Criticality: [blocking / important / nice-to-have]
    - Current status: [covered / partially covered / uncovered]
```

---

## Phase 2: Skill Search and Scoring

```
[C] CANDIDATE_SEARCH:

For each sub-capability, search skills.json:
    - Match on description keywords
    - Match on category alignment
    - Match on tag overlap
    - Match on title relevance

[D] SCORING:

For each candidate:
    RELEVANCE: How directly does this skill address a sub-capability? (0-3)
    TIER_WEIGHT: tier1=3, tier2=2.5, category=2, tier3=2, experimental=1.5, tier4=1
    CHAIN_BONUS: +1 if this skill invokes other relevant skills
    MULTI_CAP: +1 for each additional sub-capability this skill addresses (beyond the first)
    TOTAL = RELEVANCE + TIER_WEIGHT + CHAIN_BONUS + MULTI_CAP

Step 1: Score all candidates
Step 2: Rank by total
Step 3: Take top 10
Step 4: Verify sub-capability coverage:
    - How many of C1-C7 are addressed by at least one pick?
    - If < 5 covered: swap lowest-scoring duplicate-capability pick
      for highest-scoring uncovered-capability pick
    - Repeat until coverage >= 5 or no swaps improve coverage
```

---

## Phase 3: Workflow Design

```
[E] WORKFLOW:

Step 1: Order the 10 picks by natural execution sequence:
    - Understanding skills first (C1, C7)
    - Decision skills after understanding (C2)
    - Planning skills after decisions (C3)
    - Creation/execution skills after planning (C5)
    - Validation skills last (C4)
    - Risk skills throughout (C6)

Step 2: Identify dependencies:
    - Which picks require output from another pick as input?
    - Which picks can run in parallel?

Step 3: Design the workflow:
    Stage 1 (UNDERSTAND): /[skill], /[skill]
    Stage 2 (DECIDE): /[skill]
    Stage 3 (PLAN): /[skill], /[skill]
    Stage 4 (EXECUTE): /[skill], /[skill]
    Stage 5 (VALIDATE): /[skill], /[skill]
```

---

## Phase 4: Output

```
ALGORITHM: GOAL
GOAL: [stated goal]
POOL: [total candidates scored]
PICKED: 10

SUB-CAPABILITIES IDENTIFIED:
  [C1] [capability] — addressed by: [skill IDs]
  [C2] [capability] — addressed by: [skill IDs]
  [C3] [capability] — addressed by: [skill IDs]
  [C4] [capability] — addressed by: [skill IDs]
  [C5] [capability] — addressed by: [skill IDs]
  [C6] [capability] — addressed by: [skill IDs]
  [C7] [capability] — addressed by: [skill IDs]

PICKED 10 SKILLS:
  1. /[id] — [title] — [1-line why this helps with the goal]
     Addresses: [C-numbers] | Tier: [tier] | Score: [total]
     Invokes: [list or none]

  2. /[id] — [title] — [1-line why]
     Addresses: [C-numbers] | Tier: [tier] | Score: [total]
     Invokes: [list or none]

  [continue to 10...]

COVERAGE: [X of 7 sub-capabilities addressed]
UNCOVERED: [list capabilities with no pick — these are blind spots]

SUGGESTED WORKFLOW:
  Stage 1 (UNDERSTAND): [skills + what they produce]
  Stage 2 (DECIDE): [skills + what they produce]
  Stage 3 (PLAN): [skills + what they produce]
  Stage 4 (EXECUTE): [skills + what they produce]
  Stage 5 (VALIDATE): [skills + what they produce]

GAPS: [what's NOT covered — suggest additional skills to add]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Capability clustering** | 6+ picks address the same sub-capability | Force coverage check — swap duplicates for uncovered capabilities |
| **Tier bias** | All picks are tier1/tier2, ignoring specialized fits | Include at least 1 tier3+ pick if it uniquely covers a capability |
| **Generic justifications** | "This helps with goals" instead of "This helps with [specific capability]" | Each pick must reference the SPECIFIC sub-capability it addresses |
| **Missing risk coverage** | No skill addresses C6 (what could go wrong) | Risk is always relevant — ensure at least 1 risk/diagnostic skill |
| **No workflow** | Skills listed without execution sequence | Suggested workflow is mandatory for goal-directed picks |
| **Ignoring compound skills** | All picks are single-function, missing chain opportunities | Check for skills that invoke others — they multiply coverage |

---

## Depth Scaling

| Depth | Goal Decomposition | Scoring | Output |
|-------|-------------------|---------|--------|
| 1x | 4 sub-capabilities | Score top 30 candidates | Ranked list + coverage |
| 2x | All 7 sub-capabilities with criticality | Score top 50 + coverage swaps | List + workflow + gaps |
| 4x | Sub-capabilities + inter-capability dependencies | Score all matching skills + verify each pick | Full workflow with stage outputs |
| 8x | Deep goal analysis (/gu-level) + capability mapping | Full library score + chain analysis | Multi-path workflow with contingencies |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Goal decomposed into sub-capabilities
- [ ] At least 5 of 7 capability types addressed by picks
- [ ] Each pick has a specific justification tied to a sub-capability
- [ ] Exactly 10 skills returned
- [ ] At least 1 compound skill included (invokes others)
- [ ] Suggested workflow with stages provided
- [ ] Gaps and uncovered capabilities explicitly listed
- [ ] At least 1 non-obvious pick included

---

## Integration

- **Shortcut for**: `/pick 10 goal $ARGUMENTS`
- **Use when**: You have a clear goal and want the toolkit to achieve it
- **Routes to**: The 10 picked skills; `/to` for execution ordering
- **Related**: `/p10for` (situation-directed), `/p5want` (want-directed), `/gu` (goal understanding)
- **Differs from /p10for**: for handles ambiguous situations; goal handles clear objectives
- **Differs from /p5want**: want handles desires/exploration; goal handles defined targets
