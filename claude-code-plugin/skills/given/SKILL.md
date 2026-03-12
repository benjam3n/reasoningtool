---
name: "given - Rank Skills by ROI for a Given Goal"
description: "Given a goal, rank relevant skills from highest to lowest expected ROI, including negative-ROI skills with reasons."
output:
  format: "prose"
---

# Given - Rank Skills by ROI for a Given Goal

**Input**: $ARGUMENTS

---

## Core Principles

1. **ROI is contextual, not intrinsic.** A skill doesn't have a fixed ROI — it depends on the goal, the current state, what's already been done, and what resources are available. `/gu` is high-ROI when the goal is vague, negative-ROI when the goal is already crystal clear.

2. **Timing dominates.** A skill can be high ROI later but low ROI now. `/pv` (procedure validation) is worthless before you have a procedure, essential after. Score for NOW, but flag future timing.

3. **Skills interact.** Running `/gu` first might make `/foht` much more valuable — it clarifies what "how" means. Score skills both independently AND in combination with likely predecessors.

4. **Negative ROI is real and important.** Some skills are tempting but actively harmful at the wrong time. `/iterate` on a first draft wastes effort. `/ma` when you need focus causes sprawl. Flagging these is as valuable as recommending positive-ROI skills.

5. **RUN_NOW must be short.** The user needs 2-4 immediate actions, not a ranked list of 20. The full ranking exists for reference; the execution slice exists for action.

---

## Phase 1: Goal Parse

```
[G1] GOAL: [restated in one sentence]
[G2] GOAL_TYPE: [achievement | exploration | prevention | restoration | maintenance]
[G3] CONSTRAINTS: [time, resources, dependencies, blockers]
[G4] URGENCY: [exploring | planning | ready-to-act | deadline-driven | crisis]
[G5] CURRENT_STATE: [what's been done, what exists, what's known]
[G6] GOAL_CLARITY: [clear | somewhat clear | vague | contradictory]
```

If GOAL_CLARITY is vague or contradictory:
```
[G7] CLARITY_ISSUE: [what's unclear]
[G8] RESOLUTION: Consider running /gu first — ROI ranking on a vague goal produces vague rankings
```

---

## Phase 2: Candidate Selection

From the full skill library, select skills plausibly relevant to the goal. Exclude obviously irrelevant skills.

For each candidate:
```
[G-N] CANDIDATE: /skill-id — RELEVANCE: [how it connects to the goal]
```

### Selection Lenses

| Lens | What it finds |
|------|--------------|
| **Direct** | Skills that directly accomplish the goal or a sub-goal |
| **Preparatory** | Skills that would make direct skills more effective |
| **Validation** | Skills that would verify progress or output quality |
| **Risk** | Skills that reduce uncertainty or prevent failure |
| **Recovery** | Skills useful if the primary approach fails |

---

## Phase 3: ROI Scoring

For each candidate, score on four dimensions:

| Dimension | Question | Scale |
|-----------|----------|-------|
| **UPSIDE** | How much progress does this skill contribute? | None / Low / Medium / High / Critical |
| **COST** | How much time and complexity does it add? | Trivial / Low / Medium / High / Prohibitive |
| **RISK** | How likely is misdirection or wasted effort? | Negligible / Low / Medium / High / Certain |
| **TIMING_FIT** | How useful is this skill RIGHT NOW vs later? | Wrong time / Early / Right time / Urgent / Overdue |

### ROI Classification

```
[G-N] SCORE: /skill-id
  UPSIDE: [level] — [why]
  COST: [level] — [why]
  RISK: [level] — [why]
  TIMING_FIT: [level] — [why]
  ROI_CLASS: HIGH | MEDIUM | LOW | NEGATIVE
  ROI_REASONING: [one sentence explaining the ROI]
```

Classification rules:
- **HIGH**: Upside ≥ High, Cost ≤ Medium, Risk ≤ Low, Timing = Right time or Urgent
- **MEDIUM**: Upside ≥ Medium, no dimension is prohibitive/certain
- **LOW**: Upside is Low, or Cost/Risk outweigh upside
- **NEGATIVE**: Running this skill now would actively hurt — wrong timing, causes sprawl, wastes effort on premature optimization

### Interaction Effects

Check whether any high-scoring skill's ROI changes based on running another skill first:
```
[G-N] INTERACTION: /skill-a ROI becomes [higher/lower] if /skill-b runs first — [why]
```

---

## Phase 4: Ranking and Execution Slice

Sort all scored candidates highest to lowest ROI. Then extract the RUN_NOW subset.

RUN_NOW rules:
- Maximum 4 skills
- Must include the highest-ROI skill
- Must respect dependencies (if A needs B's output, B comes first)
- Should cover different needs (not 3 analytical skills and no action skills)

---

## Phase 5: Output

```
GOAL: [restated]
CURRENT_STATE: [summary]
GOAL_CLARITY: [level]

RUN_NOW (immediate execution slice):
1. /skill-id — ROI: HIGH — WHY: [one sentence]
2. /skill-id — ROI: HIGH — WHY: [one sentence]
3. /skill-id — ROI: MEDIUM — WHY: [one sentence]

FULL_RANKING:
1. /skill-id — ROI: HIGH
   UPSIDE: [level] — COST: [level] — RISK: [level] — TIMING: [level]
   WHY: [one sentence]
2. /skill-id — ROI: MEDIUM
   UPSIDE: [level] — COST: [level] — RISK: [level] — TIMING: [level]
   WHY: [one sentence]
...

NEGATIVE_ROI (tempting but harmful now):
- /skill-id — WHY_NEGATIVE_NOW: [reason] — WHEN_IT_BECOMES_POSITIVE: [condition]
- /skill-id — WHY_NEGATIVE_NOW: [reason] — WHEN_IT_BECOMES_POSITIVE: [condition]

INTERACTION_EFFECTS:
- /skill-a + /skill-b: [how they interact]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Vague goal, precise ranking** | Detailed ROI scores on an unclear goal | Flag goal clarity issue; suggest /gu first |
| **All HIGH** | Every skill scored HIGH ROI | Recalibrate — if everything is high, nothing is |
| **No NEGATIVE entries** | Negative ROI section empty | There are always tempting-but-wrong skills. Find them |
| **Timing ignored** | Great skill scored HIGH but it's the wrong phase | TIMING_FIT must factor into final ROI class |
| **Independence assumption** | Skills scored without interaction effects | Check top 5 for interaction effects |
| **RUN_NOW too long** | More than 4 skills in execution slice | The point is focus. Cut to 4 max |
| **Cost blindness** | High-upside skill recommended despite prohibitive cost | Cost matters. A simpler alternative might exist |

---

## Depth Scaling

| Depth | Min Candidates | Min Scored | Min Negative ROI | Min Interactions |
|-------|---------------|-----------|------------------|-----------------|
| 1x | 5 | 5 | 1 | 0 |
| 2x | 10 | 10 | 2 | 2 |
| 4x | 15 | 15 | 4 | 5 |
| 8x | 25 | 25 | 6 | 10 |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Goal restated clearly with type and constraints
- [ ] Goal clarity assessed (if vague, flagged before ranking)
- [ ] Candidates selected from multiple lenses (not just direct)
- [ ] Each candidate scored on all four ROI dimensions with reasoning
- [ ] Interaction effects checked between top candidates
- [ ] Negative ROI skills identified (not left empty)
- [ ] RUN_NOW is ≤4 skills with dependency order respected
- [ ] TIMING_FIT factored into ROI class (not just UPSIDE)

---

## Integration

- Use from: `/meta`, `/want` (after goal is clear, to decide what to run)
- Differs from `/wsib`: wsib picks one best skill by intent fit; given ranks many by ROI
- Differs from `/extract`: extract maps skills by sub-need coverage; given ranks by value
- Differs from `/fonss`: fonss sequences skills; given ranks them by ROI
- Routes to: whatever skills are in the RUN_NOW slice
