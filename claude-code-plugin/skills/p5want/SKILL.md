---
name: "p5want - Pick 5 Want"
description: "Pick 5 skills to help someone clarify, explore, or achieve what they want. Classifies the want by clarity level and selects skills matching the user's journey phase. Standalone implementation of the WANT algorithm from /pick with N=5."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "want", "desire", "exploration"]
---

# Pick 5 Want

**Input**: $ARGUMENTS

---

## Core Principles

1. **Wants have clarity levels.** "I don't know what I want" is a vague want. "I want to be healthier" is directional. "I want to negotiate a 20% raise by March" is specific. The clarity level determines which skills help — giving execution tools to someone with a vague want is harmful.

2. **The journey has phases.** Discovery (what do I want?), Analysis (what does it require?), Planning (how do I get there?), Execution (do the thing), Validation (is it working?). Match skills to the phase the user is in, not the phase you think they should be in.

3. **Vague wants need exploration, not execution.** The most common error is treating "I want to figure out what I want" as a goal and immediately deploying goal analysis. Vague wants need self-assessment, value clarification, and exploration — not SMART goals.

4. **The want behind the want.** "I want to write a business plan" often means "I want to decide if this idea is viable." The stated want is instrumental; the real want is deeper. Identifying the real want changes the skill selection.

5. **Five skills should span the journey arc.** Even if the user is in a specific phase, include at least one skill from the adjacent phases (one from before, one from after) so they can navigate if their phase assessment is wrong.

---

## Phase 1: Want Classification

```
[A] STATED_WANT: [from $ARGUMENTS]

[B] CLARITY_LEVEL:
    Step 1: Can the user name what they want? [Y/N]
    Step 2: Can they measure whether they got it? [Y/N]
    Step 3: Do they know what's needed to get it? [Y/N]

    Classification:
        N/N/N → VAGUE ("I don't know what I want")
        Y/N/N → DIRECTIONAL ("I want to be healthier")
        Y/Y/N → SPECIFIC_UNCLEAR ("I want to lose 20 lbs but don't know how")
        Y/Y/Y → SPECIFIC_CLEAR ("I know what I want and how to get there — I just need to do it")

[C] DEEPER_WANT:
    Step 1: Is the stated want instrumental to something else? [Y/N]
    Step 2: If Y: what is the deeper want? [identify]
    Step 3: Does the deeper want change the clarity level? [Y/N]

[D] JOURNEY_PHASE:
    VAGUE → DISCOVERY phase
    DIRECTIONAL → ANALYSIS phase
    SPECIFIC_UNCLEAR → PLANNING phase
    SPECIFIC_CLEAR → EXECUTION phase
```

---

## Phase 2: Phase-Matched Selection

```
[E] SKILL_SELECTION:

For VAGUE wants (Discovery phase):
    Core: /gu (goal understanding), /ve (values exploration), /pre (priorities/energy)
    Support: /dd (divergent discovery), /wt (what-if thinking)
    Journey bonus: +2 for exploration skills, +1 for self-assessment, -1 for execution

For DIRECTIONAL wants (Analysis phase):
    Core: /gu (goal understanding), /grf (goal reframing), /uga (full goal analysis)
    Support: /se (solution exploration), /poa (path of action)
    Journey bonus: +2 for analysis skills, +1 for exploration, -1 for validation

For SPECIFIC_UNCLEAR wants (Planning phase):
    Core: /gd (goal decomposition), /de (dependency extraction), /to (topological ordering)
    Support: /ria (risk assessment), /cba (cost-benefit)
    Journey bonus: +2 for planning skills, +1 for analysis, -1 for exploration

For SPECIFIC_CLEAR wants (Execution phase):
    Core: /dbg (debugging), /pw (practical writing), /pv (pre-validation)
    Support: /iterate (iteration), /mv (milestone validation)
    Journey bonus: +2 for execution skills, +1 for planning, -1 for exploration

[F] SCORING:
    For each candidate:
        RELEVANCE: How directly does this address the want? (0-3)
        JOURNEY_BONUS: Phase-appropriate bonus (-1 to +2)
        TIER_WEIGHT: tier1=3, tier2=2.5, category=2, tier3=2, tier4=1
        TOTAL = RELEVANCE + JOURNEY_BONUS + TIER_WEIGHT

    Step 1: Score candidates
    Step 2: Rank by total
    Step 3: Take top 5
    Step 4: Verify journey span:
        - At least 1 skill from the user's current phase
        - At least 1 skill from the adjacent earlier phase
        - At least 1 skill from the adjacent later phase
        If not: swap to ensure span
```

---

## Phase 3: Journey Design

```
[G] JOURNEY:

    Step 1: Order the 5 picks by journey phase (discovery → analysis → planning → execution → validation)
    Step 2: For each, describe what it contributes to the user's want
    Step 3: Identify the transition point: which skill moves them from current phase to next phase?
```

---

## Phase 4: Output

```
ALGORITHM: WANT
STATED WANT: [want]
CLARITY LEVEL: [vague / directional / specific-unclear / specific-clear]
DEEPER WANT: [if identified — otherwise "same as stated"]
JOURNEY PHASE: [discovery / analysis / planning / execution]
PICKED: 5

JOURNEY:
  Phase 1 ([current or prior phase]):
    1. /[id] — [title]
       Want-fit: [how this helps with THIS want]
       Tier: [tier] | Journey role: [what phase this serves]

  Phase 2 ([current phase]):
    2. /[id] — [title]
       Want-fit: [how this helps]
       Tier: [tier] | Journey role: [phase]

    3. /[id] — [title]
       Want-fit: [how this helps]
       Tier: [tier] | Journey role: [phase]

  Phase 3 ([next phase]):
    4. /[id] — [title]
       Want-fit: [how this helps]
       Tier: [tier] | Journey role: [phase]

    5. /[id] — [title]
       Want-fit: [how this helps]
       Tier: [tier] | Journey role: [phase]

TRANSITION POINT: /[skill] — this is the skill that moves you from [current phase] to [next phase]

SUGGESTED SEQUENCE:
  Start with: /[skill] — because: [why this first]
  Then: /[skill] — because: [why next]
  Key moment: /[skill] — this is where [what changes]
  Then: /[skill]
  End with: /[skill] — because: [why validate at end]

CLARITY NOTE:
  [If vague: "Your want is still forming. Start with discovery skills. Don't jump to planning."]
  [If specific-clear: "You know what you want. These skills help you DO it, not re-analyze it."]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Execution tools for vague wants** | User says "I don't know what I want" and gets planning/execution skills | Check clarity level — vague wants need discovery, not SMART goals |
| **Ignoring the deeper want** | Skills address the stated want but miss the underlying desire | Ask: is this want instrumental? What's underneath it? |
| **No journey span** | All 5 skills are from the same phase | Enforce at least 1 from adjacent earlier and 1 from adjacent later phase |
| **Clarity mis-assessment** | User classified as vague when they're actually specific | Check all 3 criteria: can they name, measure, and plan for the want? |
| **Generic want-handling** | Same 5 skills returned regardless of the stated want | Every pick must reference the SPECIFIC want in its justification |
| **Missing transition skill** | Skills for current phase and future phase but nothing to bridge them | Identify and flag the transition point explicitly |

---

## Depth Scaling

| Depth | Want Analysis | Selection | Journey |
|-------|-------------|-----------|---------|
| 1x | Clarity level only | Phase-matched top 5 | Linear sequence |
| 2x | Clarity + deeper want + journey phase | Scored selection with journey span | Sequence + transition point |
| 4x | Deep want analysis + phase validation | All library scored + journey optimization | Full journey design with decision points |
| 8x | Want modeling + value alignment analysis | Custom selection + interaction analysis | Journey with contingency paths per clarity shift |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Want classified by clarity level (vague/directional/specific-unclear/specific-clear)
- [ ] Deeper want identified if stated want is instrumental
- [ ] Journey phase identified
- [ ] Exactly 5 skills returned
- [ ] Journey span verified (skills from current + adjacent phases)
- [ ] Transition point identified
- [ ] Each pick's justification references the specific stated want

---

## Integration

- **Shortcut for**: `/pick 5 want $ARGUMENTS`
- **Use when**: You have a desire or want and need skills to clarify/pursue it
- **Routes to**: The 5 picked skills in journey order; `/gu` if want is vague
- **Related**: `/p10goal` (for clear goals, not wants), `/p5qm` (question-driven discovery)
- **Differs from /p10goal**: goal assumes a defined objective; want handles desires at any clarity level
- **Differs from /p5qm**: qm asks questions to narrow the library; want classifies the desire to match the journey
