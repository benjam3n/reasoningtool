---
name: "fonss - Figure Out Next Skills"
description: "Determine which skills to run next (more than one), in order, with rationale, handoff prompts, and stop conditions."
output:
  format: "prose"
---

# FONSS - Figure Out Next Skills

**Input**: $ARGUMENTS

---

## Core Principles

1. **Sequence is not a list.** Each skill in the chain must have a reason it comes AFTER the previous one and BEFORE the next. If you can reorder without consequence, the sequence is arbitrary and wrong.

2. **State determines sequence.** The right next skills depend on what's been done, what's blocked, and what information exists now. Same goal, different state = different sequence.

3. **Handoffs are contracts.** Each skill must know what it receives from the previous one and what it must produce for the next. Vague handoffs ("then run /evaluate") produce garbage.

4. **Stop conditions prevent infinite chains.** Every skill in the sequence needs a condition under which you STOP the chain — either because you're done or because the chain is heading in the wrong direction.

5. **Parallel when independent, sequential when dependent.** If two skills don't need each other's output, they can run simultaneously. Forcing them into sequence wastes time. Forcing dependent skills into parallel produces errors.

6. **Fewer is better.** A 3-skill chain that covers 90% of the need is better than a 7-skill chain that covers 100%. Diminishing returns are real. Every additional skill is overhead.

---

## Phase 1: State Extraction

```
[F1] CURRENT_GOAL: [what the user is trying to achieve]
[F2] DONE_SO_FAR: [what has already been completed — skills run, outputs produced]
[F3] CURRENT_STATE: [what the user knows/has now]
[F4] BLOCKERS: [what is preventing progress]
[F5] DECISION_POINTS: [unresolved decisions that affect the path]
[F6] QUALITY_OF_CONTEXT: [rich | adequate | thin | missing]
```

If QUALITY_OF_CONTEXT is thin or missing:
```
[F7] CONTEXT_GAP: [what's missing]
[F8] GAP_RESOLUTION: Ask user | Infer from prompt | Run /gu first
```

---

## Phase 2: Candidate Generation

Generate candidate skills for the next steps. For each:

```
[F9] CANDIDATE: /skill-id — PURPOSE: [what it would accomplish] — DEPENDS_ON: [what input it needs]
[F10] CANDIDATE: /skill-id — PURPOSE: [what] — DEPENDS_ON: [what]
...
```

### Candidate Sources

| Source | How |
|--------|-----|
| **Blocker resolution** | What skill directly addresses each blocker? |
| **Goal decomposition** | What sub-goals remain? What skill handles each? |
| **Decision resolution** | What skill resolves each open decision point? |
| **Standard workflows** | Does this goal type have a known skill chain? |
| **Gap filling** | Is there information missing that a skill could provide? |

---

## Phase 3: Dependency Analysis

For each candidate, identify:

```
[F-N] DEPENDENCY: /skill-a REQUIRES output from /skill-b
[F-N] PARALLEL: /skill-a and /skill-b are independent — can run simultaneously
[F-N] CONDITIONAL: /skill-a only needed IF /skill-b produces [result]
```

Build the dependency graph:
```
[F-N] DEPENDENCY GRAPH:
  /skill-b → /skill-a (a needs b's output)
  /skill-c ∥ /skill-d (independent, can parallel)
  /skill-e ? /skill-f (e only if f produces X)
```

---

## Phase 4: Sequencing

Order the candidates into a chain. For each position, specify:

```
[F-N] SEQUENCE POSITION [1]:
  SKILL: /skill-id
  WHY_NOW: [why this runs at this position, not earlier or later]
  RECEIVES: [what input it gets — from user or prior skill]
  PRODUCES: [what output it generates for the next skill]
  HANDOFF_PROMPT: [exact invocation with arguments]
  EXPECTED_OUTPUT: [what good output looks like]
  STOP_CONDITION: [when to stop running this skill OR stop the whole chain]
```

### Sequencing Rules

| Rule | Rationale |
|------|-----------|
| Clarification before analysis | Don't analyze a vague goal |
| Analysis before decision | Don't decide without information |
| Decision before action | Don't act without deciding |
| Validation after creation | Don't ship without checking |
| Recovery skills are conditional | Only invoke if a prior skill fails |

---

## Phase 5: Output

```
CURRENT_GOAL: [restated]
CURRENT_STATE: [what's done, what's blocked]

NEXT_SKILLS_ORDERED:

1. /skill-id
   WHY_NOW: [why this runs first]
   HANDOFF: /skill-id [exact invocation with args]
   EXPECTED_OUTPUT: [what good output looks like]
   STOP_IF: [condition to stop chain here]

2. /skill-id
   WHY_AFTER_1: [why this follows skill 1]
   RECEIVES: [output from skill 1]
   HANDOFF: /skill-id [exact invocation]
   EXPECTED_OUTPUT: [description]
   STOP_IF: [condition]

3. /skill-id
   WHY_AFTER_2: [why this follows skill 2]
   RECEIVES: [output from skill 2]
   HANDOFF: /skill-id [exact invocation]
   EXPECTED_OUTPUT: [description]
   STOP_IF: [condition]

PARALLEL_OPPORTUNITIES:
- /skill-a ∥ /skill-b: [why these can run simultaneously]

CONDITIONAL_BRANCHES:
- IF [condition from skill N]: → /skill-x
- ELSE: → /skill-y

CHAIN_STOP_CONDITION: [when the entire sequence is done]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Arbitrary sequence** | Skills can be reordered without consequence | Each position must have a dependency-based reason |
| **Missing handoffs** | "Then run /evaluate" with no input specified | Every skill needs RECEIVES and PRODUCES |
| **Infinite chain** | 8+ skills with no stop conditions | Cap at 5 unless user requests more; add stop conditions |
| **All sequential** | No parallel opportunities identified | Check each pair for independence |
| **Router chains** | /meta → /want → /how (routers routing to routers) | Skip intermediate routers; go to concrete skills |
| **No conditionals** | Linear chain ignoring branching possibilities | Check if any skill's output could change the path |
| **Vague stop conditions** | "Stop when done" | Stop conditions must reference specific output properties |

---

## Depth Scaling

| Depth | Max Chain Length | Min Dependencies Analyzed | Parallel Check | Conditional Branches |
|-------|-----------------|--------------------------|----------------|---------------------|
| 1x | 3 | 2 | No | No |
| 2x | 5 | 4 | Yes | 1 |
| 4x | 7 | 6 | Yes | 3 |
| 8x | 10 | All pairs | Yes | All identified |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Current state extracted (not assumed)
- [ ] Candidates generated from multiple sources (not just the obvious one)
- [ ] Dependencies between candidates analyzed
- [ ] Sequence order justified by dependencies (not arbitrary)
- [ ] Each skill has RECEIVES, PRODUCES, HANDOFF_PROMPT
- [ ] Stop conditions are specific (not "when done")
- [ ] Parallel opportunities identified where they exist
- [ ] Conditional branches noted where output could change the path
- [ ] Chain length is reasonable (≤5 by default)
- [ ] No router-to-router chains

---

## Integration

- Use from: `/next` (when multi-step needed), `/extract` (after identifying skills, to sequence them)
- Differs from `/wsib`: wsib picks ONE skill; fonss sequences MULTIPLE
- Differs from `/extract`: extract finds all relevant skills; fonss orders the next ones to run
- Differs from `/next`: next picks ONE next step; fonss builds a chain
- Differs from `/to`: to orders generic tasks; fonss orders skills specifically
