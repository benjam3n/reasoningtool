---
name: "iagca - I Am Getting Carried Away"
description: "Detect idea sprawl, compress scope aggressively, and return to the highest-leverage next actions — preserving valuable ideas without letting them derail execution."
---

# IAGCA - I Am Getting Carried Away

**Input**: $ARGUMENTS

---

## Core Principles

1. **Sprawl feels like progress.** Generating ideas, exploring tangents, and building elaborate plans all feel productive. They are NOT productive if they delay execution. The skill must distinguish genuine exploration from execution avoidance.

2. **The highest-leverage action is rarely the most exciting one.** Exciting ideas draw attention. But the thing that moves the project forward most is often boring, concrete, and small. Find it.

3. **Defer, don't delete.** Loss aversion makes people resist cutting scope. The fix isn't deleting ideas — it's moving them to a "later" list. Everything of value is preserved. But only 2-3 things get done NOW.

4. **Sprawl signals richness.** Getting carried away means the space is interesting. That's good information. But richness needs structure or it becomes chaos.

5. **The scope compression is temporary.** You're not deciding what matters forever. You're deciding what to do in the next 1-3 actions. Everything else waits.

---

## Phase 1: Sprawl Assessment

```
[G1] ORIGINAL_GOAL: [what the user was originally trying to accomplish]
[G2] CURRENT_BRANCHES: [list every idea, tangent, and sub-project currently active]
[G3] BRANCH_COUNT: [N active branches]
[G4] SPRAWL_SEVERITY: [mild (5-8) | moderate (8-15) | severe (15+)]
[G5] SPRAWL_TYPE: [depth (going deeper on one thing) | breadth (spreading across many things) | both]
```

---

## Phase 2: Branch Scoring

For each branch, score on two dimensions:

```
[G-N] BRANCH: [description]
  NEAR_TERM_VALUE: [high | medium | low] — [what does this accomplish in the next 1-3 actions?]
  EXECUTION_READINESS: [ready | needs-prep | blocked | unclear]
  RELATIONSHIP_TO_GOAL: [direct | supporting | tangential | unrelated]
```

### Scoring Matrix

| Near-Term Value | Execution Readiness | Action |
|----------------|-------------------|--------|
| High | Ready | **DO NOW** |
| High | Needs prep | **PREP THEN DO** |
| High | Blocked | **UNBLOCK or DEFER** |
| Medium | Ready | **DO IF TIME** |
| Medium | Not ready | **DEFER** |
| Low | Any | **DEFER** |
| Any | Unclear | **CLARIFY or DEFER** |
| Tangential/Unrelated | Any | **DEFER** |

---

## Phase 3: Scope Compression

```
[G-N] DO NOW (maximum 3):
  1. [branch] — WHY_NOW: [why this is the highest-leverage action]
  2. [branch] — WHY_NOW: [reason]
  3. [branch] — WHY_NOW: [reason]

[G-N] DEFERRED (preserved, not deleted):
  1. [branch] — DEFERRED_BECAUSE: [reason] — REVISIT_WHEN: [condition]
  2. [branch] — DEFERRED_BECAUSE: [reason] — REVISIT_WHEN: [condition]
  ...

[G-N] EXECUTION ORDER:
  Step 1: [action] — [expected time]
  Step 2: [action] — [expected time]
  Step 3: [action] — [expected time]
```

### Compression Rules

- **Max 3 in DO NOW.** If you can't pick 3, the goal isn't clear enough — route to `/gu`.
- **Everything else is DEFERRED, not deleted.** The user keeps every idea. Just not now.
- **DO NOW items must be concrete actions**, not "explore X" or "think about Y."
- **If no branch scores high:** The sprawl might be a signal that the goal is wrong. Route to `/want`.

---

## Phase 4: Sprawl Source Check

Why did the user get carried away? Knowing the source prevents recurrence.

```
[G-N] SPRAWL_SOURCE: [one of the following]
```

| Source | Pattern | Prevention |
|--------|---------|-----------|
| **Rich space** | Domain has many genuine opportunities | Use `/ycshikfmif` to batch |
| **Avoidance** | Exploring is easier than executing | Name the avoided task; start with it |
| **Unclear goal** | Everything seems relevant because the goal is vague | Run `/gu` to clarify |
| **Perfectionism** | Need to cover everything before acting | Accept good enough; iterate later |
| **External triggers** | New inputs keep arriving (messages, ideas, requests) | Batch inputs; process on schedule |

---

## Phase 5: Output

```
SCOPE COMPRESSION
=================

ORIGINAL GOAL: [restated]
BRANCHES ACTIVE: [N]
SPRAWL SEVERITY: [level]
SPRAWL SOURCE: [identified pattern]

DO NOW (max 3):
  1. [concrete action] — [why this is highest leverage]
  2. [concrete action] — [why this is next]
  3. [concrete action] — [why this is third]

EXECUTION ORDER:
  [action 1] → [action 2] → [action 3]

DEFERRED (preserved — not lost):
  1. [idea] — Revisit when: [condition]
  2. [idea] — Revisit when: [condition]
  ...

SPRAWL PREVENTION:
  [what to do differently to avoid re-sprawl]

READY FOR:
- Execute the DO NOW list
- /ycshikfmif — if deferred ideas need batching
- /awtlytrn — if unsure about limits for DO NOW
- /gu — if sprawl source is unclear goal
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **DO NOW too large** | More than 3 items | Cut to 3. If you can't, the goal is unclear |
| **All deferred** | Nothing in DO NOW | If no branch is worth doing now, question the goal |
| **Ideas deleted** | User's ideas removed instead of deferred | Everything goes to DEFERRED or DO NOW. Nothing is deleted |
| **Vague actions** | DO NOW contains "explore X" or "think about Y" | Actions must be concrete — "write the first draft of X" |
| **Sprawl source ignored** | Compression without understanding why it happened | Identify the source or compression will be temporary |
| **Recurrence not addressed** | Same sprawl pattern repeats next session | Prevention recommendation must address the root source |

---

## Depth Scaling

| Depth | Min Branches Assessed | Scoring Dimensions | Sprawl Source | Prevention |
|-------|----------------------|-------------------|---------------|-----------|
| 1x | 5 | Value only | Not checked | No |
| 2x | 10 | Value + readiness | Identified | Basic |
| 4x | 15 | Value + readiness + goal relationship | Identified + tested | With specific strategy |
| 8x | All | Full scoring matrix | Full analysis | With monitoring plan |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All active branches listed (not just some)
- [ ] Each branch scored on near-term value and execution readiness
- [ ] DO NOW contains maximum 3 concrete actions
- [ ] Everything else is DEFERRED (not deleted)
- [ ] Deferred items have revisit conditions
- [ ] Sprawl source identified
- [ ] Prevention strategy provided
- [ ] DO NOW items are concrete actions, not vague explorations

---

## Integration

- Use from: any time the user recognizes they're sprawling
- Complementary: `/ycshikfmif` (structures ongoing expansion — less urgent)
- Complementary: `/awtlytrn` (estimates limits for the compressed scope)
- Differs from `/ycshikfmif`: ycshikfmif batches expansion; iagca compresses urgently
- Differs from `/awtlytrn`: awtlytrn estimates limits; iagca forces scope reduction
- Routes to: `/gu` if sprawl source is unclear goal, `/want` if no branch is worth doing
