---
name: "extract - Skill Extractor"
description: "Given any prompt, decompose it into implicit sub-tasks and extract every potentially useful skill, grouped by role and prioritized with invocation-ready suggestions."
---

# Extract - Skill Extractor

**Input**: $ARGUMENTS

---

## Core Principles

1. **Prompts are layered.** A single sentence can contain a surface request, an implicit prerequisite, a validation need, and an emotional undercurrent. Extract skills for all layers, not just the obvious one.

2. **Role determines value.** A skill can serve as primary (does the core work), preparatory (should run first), supporting (enhances output), validation (checks output), or recovery (useful if primary fails). The same skill in different roles has different priority.

3. **Sequence is load-bearing.** Running `/aex` before `/dcp` changes the decision. Running `/gu` before `/want` changes the goal. Skill ordering is analytical work, not decoration.

4. **Implicit beats explicit.** The user who says "help me write a proposal" probably also needs `/gu` (clarify the goal), `/aex` (check assumptions about the audience), and `/pv` (validate the draft). The unexpressed needs are where extraction earns its keep.

5. **Interaction effects exist.** Some skill pairs amplify each other (`/aex` + `/ht`). Some conflict (`/ma` diverges, `/dcp` converges — sequence matters). Flag these.

---

## Phase 1: Prompt Decomposition

Break the input into every distinct sub-need. Go beyond the literal request.

```
[E1] SUB-NEED: [label] — [one-line description]
[E2] SUB-NEED: [label] — [one-line description]
...
```

Apply all decomposition lenses that yield results:

| Lens | Question |
|------|----------|
| **Surface** | What is the user literally asking for? |
| **Prerequisite** | What must be true or known before the surface task can succeed? |
| **Assumption** | What is the user assuming that might be wrong? |
| **Validation** | How would the user know the output is good? |
| **Emotion** | Is frustration, uncertainty, or overwhelm present? |
| **Scope** | Is the user scoping too narrowly or too broadly? |
| **Sequence** | Does this need to happen in a particular order? |
| **Downstream** | What will the user do with the result? |

---

## Phase 2: Skill Mapping

For each sub-need, identify candidate skills and assign a role:

| Role | Meaning | Priority Weight |
|------|---------|-----------------|
| **Primary** | Directly accomplishes the sub-need | Highest |
| **Preparatory** | Should run before the primary to improve its input | High |
| **Supporting** | Enhances or deepens the primary's output | Medium |
| **Validation** | Checks the primary's output for quality or correctness | Medium |
| **Recovery** | Useful if the primary fails or produces weak results | Low |

```
[E-N] SKILL: /skill-id → sub-need [E-ref] as [role] — [one sentence why]
```

---

## Phase 3: Prune and Prioritize

Remove weak matches. A match is weak if:
- The skill only tangentially relates to the sub-need
- A stronger skill already covers the same ground in the same role
- The skill requires context the user clearly does not have

Rank surviving skills by: `role_weight x sub-need_importance x fit_quality`

Group into tiers:
- **ESSENTIAL** — Skip these and the output quality drops significantly
- **RECOMMENDED** — Meaningful improvement, worth the time
- **OPTIONAL** — Useful if the user wants thoroughness

---

## Phase 4: Interaction Analysis

Identify skill pairs or sequences where order matters or effects compound.

```
[E-N] INTERACTION: [type] — /skill-a + /skill-b: [what happens and why order matters]
```

| Type | Description |
|------|-------------|
| **Amplifying** | Running both produces more than the sum |
| **Sequenced** | One must run first or the second's input is degraded |
| **Conflicting** | Running both without awareness creates tension |
| **Redundant** | High overlap; pick one unless depth warrants both |

---

## Phase 5: Output

```
PROMPT: [original input, quoted]

ESSENTIAL SKILLS (ordered by execution sequence):
1. /skill-id — ROLE: [role] — WHY: [one line] — INVOKE: /skill-id [suggested args]
2. ...

RECOMMENDED SKILLS:
3. /skill-id — ROLE: [role] — WHY: [one line] — INVOKE: /skill-id [suggested args]
...

OPTIONAL SKILLS:
- /skill-id — ROLE: [role] — WHY: [one line]

INTERACTION EFFECTS:
- [skill-a] → [skill-b]: [effect and recommended order]

SUGGESTED SEQUENCE:
[skill-a] → [skill-b] → [skill-c]
(brief rationale for ordering)
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Surface-only extraction** | Only the literal request mapped | Apply all 8 decomposition lenses |
| **Skill-name anchoring** | Picked skills whose names sound right | Verify by checking what the skill actually does |
| **Over-extraction** | 20 skills for a simple prompt | Prune ruthlessly; simple prompt = short output |
| **Role collapse** | Everything assigned "primary" | Force at least 2 distinct roles at 2x+ depth |
| **Flat ordering** | Skills listed alphabetically | Phase 4 interaction analysis must drive sequence |
| **Missing prerequisites** | Recommended skill needs input user hasn't produced | Check each skill's input requirements |
| **Ignoring emotional layer** | Only analytical skills extracted | Emotion lens catches frustration/uncertainty |

---

## Depth Scaling

| Depth | Min Sub-Needs | Min Skills | Min Interactions | Min Roles |
|-------|---------------|-----------|-----------------|-----------|
| 1x | 2 | 4 | 0 | 1 |
| 2x | 4 | 8 | 2 | 3 |
| 4x | 6 | 14 | 4 | 4 |
| 8x | 9 | 22 | 7 | 5 |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Every decomposition lens applied (not just surface)
- [ ] Each extracted skill has an explicit role assignment
- [ ] At least one non-obvious skill identified
- [ ] Interaction effects between top skills analyzed
- [ ] Suggested sequence reflects dependency and amplification order
- [ ] Invocation examples include concrete arguments from user's prompt
- [ ] No skill included without a specific "why" tied to a sub-need
- [ ] Over-extraction checked: every ESSENTIAL skill genuinely earns its tier

---

## Integration

- Use from: `/meta`, `/handle`, `/fonss`
- Routes to: any extracted skill via invocation suggestions
- Differs from `/wsib`: wsib picks ONE skill; extract maps the full landscape
- Differs from `/given`: given ranks by ROI for a goal; extract maps by coverage of sub-needs
- Differs from `/fonss`: fonss orders next skills; extract finds all relevant skills
