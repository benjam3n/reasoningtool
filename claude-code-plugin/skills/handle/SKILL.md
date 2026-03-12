---
name: "handle - Handle This"
description: "Convert maximally ambiguous 'handle this' requests into a classified task type, a concrete first action, and an ordered next-skill sequence."
output:
  format: "prose"
---

# Handle - Handle This

**Input**: $ARGUMENTS

---

## Core Principles

1. **"Handle this" is maximally ambiguous.** The user is delegating without specification. This means EITHER they trust the system to figure it out, OR they don't know what they need. Both require classification before action.

2. **"This" can be anything.** A problem, a task, a situation, a feeling, a question, a document, a decision, a mess. The first job is identifying WHAT "this" is, not how to handle it.

3. **First action matters most.** The wrong first action wastes the most time and creates the most confusion. Get the first action right even if the rest of the chain is approximate.

4. **Some things shouldn't be "handled."** They need understanding first. "Handle my confusion about X" shouldn't produce an action — it should produce clarity. Route to analysis when analysis is needed, not action.

5. **The user might not know what they want.** This is different from knowing but not saying. If the user doesn't know, the first action is helping them figure it out, not guessing and acting.

---

## Phase 1: Referent Identification

What does "this" refer to?

```
[H1] RAW_INPUT: [what the user said, quoted]
[H2] REFERENT: [what "this" points to — the specific thing to be handled]
[H3] REFERENT_TYPE: [problem | task | situation | feeling | question | document | decision | ambiguous]
[H4] CLARITY: [clear | somewhat clear | ambiguous | opaque]
```

If CLARITY is ambiguous or opaque:
```
[H5] BEST_GUESS: [most likely referent]
[H6] ALTERNATIVE_INTERPRETATION: [what else "this" might mean]
[H7] CLARIFICATION_QUESTION: [what to ask to disambiguate]
```

If opaque: ask the clarification question INSTEAD of proceeding. Don't guess.

---

## Phase 2: Task Type Classification

```
[H8] TASK_TYPE: [see table below]
[H9] EVIDENCE: [what signals this type]
[H10] CONFIDENCE: [high | medium | low]
```

| Task Type | Signals | Route |
|-----------|---------|-------|
| **Problem to solve** | Something is broken, wrong, or failing | → `/diagnose` |
| **Decision to make** | Options exist, choice needed | → `/decide` |
| **Goal to achieve** | Desired future state, outcome wanted | → `/want` |
| **Question to answer** | Uncertainty, curiosity, "what/why/how" | → `/how` or `/search` |
| **Content to produce** | Writing, creating, building something | → `/create` |
| **Task to execute** | Clear action, just needs doing | → `/action` |
| **Feeling to process** | Frustration, anxiety, overwhelm | → `/emotion` |
| **Situation to navigate** | Complex context, multiple stakeholders | → `/sya` or `/want` |
| **Work to evaluate** | Output exists, quality check needed | → `/evaluate` |
| **Mess to sort** | Too many things, no structure | → `/iagca` |

---

## Phase 3: First Action Selection

```
[H11] FIRST_ACTION: [specific, concrete action — not vague]
[H12] FIRST_ACTION_SKILL: /skill-id
[H13] WHY_THIS_FIRST: [why this action before anything else]
[H14] EXPECTED_RESULT: [what good output from this first action looks like]
```

### First Action Rules

- If uncertain about task type → first action is CLASSIFICATION, not execution
- If task type is clear → first action is the appropriate skill
- If user seems overwhelmed → first action is scope compression (`/iagca`)
- If context is missing → first action is context gathering (`/gu` or ask user)
- NEVER make the first action a broad plan — make it a specific next step

---

## Phase 4: Skill Chain

After the first action, what follows?

```
[H15] SKILL_CHAIN (2-5 steps):
  1. /skill-id [args] — [what this step accomplishes]
  2. /skill-id [args] — [what this step accomplishes]
  3. /skill-id [args] — [what this step accomplishes]

[H16] CHAIN_CONDITIONAL:
  IF first action reveals [X]: → modify chain to [alternative]
  IF first action reveals [Y]: → stop here, goal accomplished
```

---

## Phase 5: Output

```
HANDLE THIS
===========

INPUT: [what the user said]
THIS = [what "this" refers to]
TYPE: [task type]
CONFIDENCE: [level]

FIRST ACTION:
  → INVOKE: /skill-id [specific arguments]
  WHY_FIRST: [reason]
  EXPECTED_RESULT: [what good output looks like]

THEN:
  2. /skill-id [args] — [purpose]
  3. /skill-id [args] — [purpose]

IF_UNEXPECTED:
  [what to do if first action reveals something different than expected]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Acting on ambiguity** | First action taken when "this" is opaque | Ask clarification question first |
| **Wrong classification** | Task type misidentified, wrong skill chain follows | Check against multiple type signals, not just one |
| **Vague first action** | "Start by thinking about it" | First action must be specific and invocable |
| **Over-planning** | 7-step chain when the task is simple | Cap at 5 steps; simple tasks need 1-2 |
| **Always /action** | Every request routed to /action regardless of type | Check classification table — most requests aren't pure execution |
| **Feelings treated as tasks** | Emotional input routed to analytical skills | If signals match "feeling," route to `/emotion` first |
| **Guessing when opaque** | Proceeding with best guess when input is truly unclear | If opaque, ask — don't guess |

---

## Depth Scaling

| Depth | Classification Rigor | Chain Length | Conditional Branches |
|-------|---------------------|-------------|---------------------|
| 1x | Type only | 2 steps | None |
| 2x | Type + evidence + confidence | 3 steps | 1 conditional |
| 4x | Full classification + alternative | 5 steps | 2 conditionals |
| 8x | Full + multi-referent analysis | 5 steps + parallel tracks | Full branching |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] "This" referent identified explicitly
- [ ] If ambiguous/opaque: clarification question provided (not guessed past)
- [ ] Task type classified with evidence
- [ ] First action is specific and invocable (not vague)
- [ ] First action matches task type
- [ ] Skill chain is 2-5 steps (not over-planned)
- [ ] Conditional handling specified for unexpected results
- [ ] Emotional inputs routed appropriately (not analytically)

---

## Integration

- Use from: user says "handle this", "deal with this", "take care of this"
- Routes to: any skill depending on classification
- Differs from `/next`: next picks one step given clear context; handle classifies ambiguous input
- Differs from `/wsib`: wsib picks best skill for a clear prompt; handle handles unclear prompts
- Differs from `/meta`: meta provides orientation; handle provides action
