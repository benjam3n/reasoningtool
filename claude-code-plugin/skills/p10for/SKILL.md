---
name: "p10for - Pick 10 For Situation"
description: "Pick 10 skills matched to a described situation. Analyzes the user's situation, infers their actual need, and selects skills appropriate to their phase and domain. Standalone implementation of the SITUATION algorithm from /pick."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "situation", "contextual"]
output:
  format: "prose"
---

# Pick 10 For Situation

**Input**: $ARGUMENTS

---

## Core Principles

1. **Situations encode phase, not just topic.** "I need to launch a product" is early-phase. "My product launch failed" is recovery-phase. The same domain requires completely different skills depending on where the user is in their process.

2. **The stated situation is not always the real need.** "I need to write a business plan" might mean "I need to decide if this idea is viable." Situation analysis must look through the stated task to the underlying need.

3. **Phase-appropriate skills outperform best-in-class skills.** The best analysis skill is useless if the user is past analysis and needs execution. Match the skill to where they ARE, not where they should be.

4. **Situation complexity determines skill depth.** Simple situations need tier1/tier2 skills. Complex multi-stakeholder situations need tier3/tier4 specialized skills. Match skill sophistication to situation complexity.

5. **Action orientation wins.** When in doubt, prefer skills that produce actionable output over skills that produce understanding. Understanding is valuable but situations demand movement.

---

## Phase 1: Situation Parsing

```
[A] RAW_SITUATION: [verbatim from $ARGUMENTS]

[B] SITUATION_ANALYSIS:
    Step 1: What is the DOMAIN?
        [technical / business / personal / creative / organizational / mixed]
    Step 2: What is the PHASE?
        [exploring / planning / deciding / executing / stuck / recovering / validating]
    Step 3: What is the COMPLEXITY?
        [simple (1 actor, 1 goal) / moderate (few actors, clear goal) / complex (many actors, unclear goal)]
    Step 4: What is the URGENCY?
        [no deadline / weeks / days / hours / already late]
    Step 5: What is the UNDERLYING NEED? (look through the stated situation)
        [what does the user actually need to move forward?]

[C] INFERRED_GOAL: [restate the situation as a goal: "Achieve [X] given [constraints]"]
```

---

## Phase 2: Phase-Matched Skill Search

```
[D] PHASE_SKILL_MAP:

Based on identified phase, weight skill selection:

EXPLORING:
    Primary: exploration skills (/se, /dd, /poa, /lr)
    Secondary: framing skills (/gu, /grf, /pre)
    Avoid: execution/validation skills (premature)

PLANNING:
    Primary: planning skills (/de, /to, /gd, /dcm)
    Secondary: risk skills (/ria, /rca)
    Avoid: divergent exploration (already past that)

DECIDING:
    Primary: decision skills (/dcp, /cmp, /cba, /dm)
    Secondary: validation skills (/aex, /ht)
    Avoid: more exploration (decision paralysis risk)

EXECUTING:
    Primary: action skills (/dbg, /pw, /stl)
    Secondary: monitoring skills (/pv, /mv)
    Avoid: re-analysis (sunk cost territory)

STUCK:
    Primary: diagnostic skills (/rca, /dbg, /fohw)
    Secondary: reframing skills (/ai, /cda, /ie)
    Avoid: more of what got them stuck

RECOVERING:
    Primary: recovery skills (/rmm, /kta, /cor)
    Secondary: analysis skills (/araw, /rca)
    Avoid: premature re-execution

VALIDATING:
    Primary: validation skills (/vbo, /val, /pv, /mv)
    Secondary: improvement skills (/iterate, /imps)
    Avoid: re-planning (validate what exists)
```

---

## Phase 3: Scoring and Selection

```
[E] CANDIDATE_SCORING:

For each candidate skill:
    RELEVANCE: How directly does this address the inferred goal? (0-3)
    PHASE_FIT: Does this match the identified phase? (+2 if primary, +1 if secondary, -1 if avoid)
    TIER_WEIGHT: tier1=3, tier2=2.5, category=2, tier3=2, experimental=1.5, tier4=1
    COMPLEXITY_MATCH: Does skill sophistication match situation complexity? (+1 if matched)
    ACTION_BONUS: Does this skill produce actionable output? (+1 if yes)
    TOTAL = RELEVANCE + PHASE_FIT + TIER_WEIGHT + COMPLEXITY_MATCH + ACTION_BONUS

Step 1: Score top 30 candidates (3x the target of 10)
Step 2: Rank by total score
Step 3: Take top 10
Step 4: Verify coverage:
    - At least 3 different skill functions represented
    - At least 1 skill from the primary phase category
    - At least 1 skill from the secondary phase category
    If not, swap lowest-scoring picks to fill gaps
```

---

## Phase 4: Output

```
ALGORITHM: SITUATION
SITUATION: [raw situation]
INFERRED: Domain=[domain] | Phase=[phase] | Complexity=[complexity] | Urgency=[urgency]
UNDERLYING NEED: [inferred goal]
POOL: [total candidates scored]
PICKED: 10

  1. /[id] — [title]
     Situation fit: [why this helps with THIS situation specifically]
     Phase: [primary/secondary] | Tier: [tier] | Score: [total]

  2. /[id] — [title]
     Situation fit: [why]
     Phase: [primary/secondary] | Tier: [tier] | Score: [total]

  [continue to 10...]

SUGGESTED WORKFLOW:
  First: /[skill] — because: [why start here given the phase]
  Then: /[skill] → /[skill] — because: [sequence logic]
  Finally: /[skill] — because: [why end here]

COVERAGE:
  Functions covered: [list]
  Phase coverage: [primary skills: N, secondary: M]

GAPS:
  Not covered: [what aspects of the situation are unaddressed]
  To fill: /[suggested additions]

PHASE WARNING: [if applicable]
  [e.g., "You appear to be in STUCK phase but requested planning skills — consider diagnostic skills first"]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Phase mismatch** | Skills for wrong phase (analysis skills for someone in execution) | Re-read situation for phase signals: tense, verbs, emotional tone |
| **Surface-level situation reading** | Picks address the stated task, not the underlying need | Ask: what does this person need to MOVE FORWARD, not just what did they say? |
| **Complexity mismatch** | Simple situation gets heavy analytical tools, or complex situation gets shallow ones | Match tool sophistication to situation complexity |
| **All analysis, no action** | 10 analytical skills for someone who needs to DO something | Include at least 2 action-oriented skills for any non-exploring phase |
| **Ignoring urgency** | Recommending deep analysis for a "need it today" situation | Check urgency — under time pressure, prefer direct action skills |
| **Generic picks** | Skills that are always recommended regardless of situation | Each pick must reference the SPECIFIC situation in its justification |

---

## Depth Scaling

| Depth | Situation Analysis | Scoring | Output |
|-------|-------------------|---------|--------|
| 1x | Phase identification only | Score top 20 candidates | Ranked list |
| 2x | Full 5-dimension analysis + underlying need | Score top 30 + coverage verification | List + workflow + gaps |
| 4x | Situation analysis + analogous situation comparison | Score all library + phase interaction analysis | Full workflow with contingencies |
| 8x | Deep situation modeling with stakeholder/system analysis | Complete library + multi-phase scenario scoring | Situation-specific toolkit with decision tree |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Situation parsed for domain, phase, complexity, and urgency
- [ ] Underlying need identified (not just stated task)
- [ ] Skills weighted by phase appropriateness
- [ ] Exactly 10 skills returned
- [ ] Each pick's justification references the specific situation
- [ ] At least 3 functions represented
- [ ] Suggested workflow matches the identified phase
- [ ] Phase warnings issued if situation signals conflict with picks

---

## Integration

- **Shortcut for**: `/pick 10 for $ARGUMENTS`
- **Use when**: You have a situation and want the right tools, not a specific goal
- **Routes to**: The 10 picked skills; `/gu` if underlying need is unclear
- **Related**: `/p10goal` (goal-directed, not situation-directed), `/wsib` (single best skill)
- **Differs from /p10goal**: goal assumes clarity of objective; for handles ambiguous situations
- **Differs from /wsib**: wsib returns 1 skill; p10for returns 10 with workflow
