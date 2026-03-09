---
name: "ata - And Then Also"
description: "Expand a request with all implied adjacent actions that should also be done, ordered by dependency and necessity, without overwhelming the user."
---

# ATA - And Then Also

**Input**: $ARGUMENTS

---

## Core Principles

1. **Every action implies adjacent actions.** "Deploy the feature" implies testing, documentation, monitoring, and stakeholder notification. Most people think about the primary action and miss 2-5 adjacent ones that determine success.

2. **Adjacent ≠ equal.** Some adjacent tasks are prerequisites (must do first), some are follow-ups (do after), some are parallel (do alongside), and some are optional enhancements. The classification determines order and obligation.

3. **Cascade control.** Each adjacent task has its own adjacents, creating infinite expansion. The skill must expand ONE level by default and flag but not expand second-order adjacents.

4. **Don't overwhelm.** A user who asked to do one thing doesn't want a 20-item task list. The output must distinguish what's REQUIRED from what's OPTIONAL, and keep the required list short.

5. **Some adjacents are so obvious the user already planned for them.** Don't insult the user by listing things they've clearly already considered. Focus on the non-obvious ones they might miss.

---

## Phase 1: Primary Request Parse

```
[T1] PRIMARY_REQUEST: [what the user asked to do, stated clearly]
[T2] CONTEXT: [relevant context — project, domain, state]
[T3] IMPLICIT_QUALITY_STANDARD: [what level of thoroughness does the user expect?]
```

---

## Phase 2: Adjacent Task Discovery

For each adjacency type, generate candidates:

```
[T-N] ADJACENT: [task] — TYPE: [prerequisite | parallel | follow-up | optional]
  WHY_IMPLIED: [what about the primary request implies this task]
  OBVIOUS: [yes | no — would the user already have this on their list?]
```

### Discovery Lenses

| Lens | Question | Example |
|------|----------|---------|
| **Prerequisites** | What must be true before the primary task can succeed? | "Before deploying: run tests" |
| **Side effects** | What does the primary task change that needs handling? | "After API change: update docs" |
| **Stakeholders** | Who needs to know or approve? | "Notify users before migration" |
| **Validation** | How will you know it worked? | "After deploy: verify in production" |
| **Rollback** | What if it fails? | "Prepare rollback plan" |
| **Dependencies** | What else depends on this changing? | "Update dependent services" |
| **Cleanup** | What temporary state needs resolving? | "Remove feature flag after stable" |

---

## Phase 3: Classification and Ordering

```
[T-N] REQUIRED ADJACENT TASKS (must do — ordered):
  1. [task] — TYPE: [prerequisite] — BEFORE/AFTER/PARALLEL: [timing]
  2. [task] — TYPE: [follow-up] — TIMING: [after]
  ...

[T-N] OPTIONAL ADJACENT TASKS (should consider):
  1. [task] — VALUE: [what it adds] — COST: [effort level]
  2. [task] — VALUE: [value] — COST: [effort]
  ...

[T-N] SECOND-ORDER (flagged, not expanded):
  1. [task from adjacent that has its own adjacents] — NOTE: [what further adjacents it implies]
```

### Ordering Rules

| Type | Position |
|------|----------|
| **Prerequisite** | Before primary task |
| **Parallel** | Alongside primary task |
| **Follow-up** | After primary task |
| **Validation** | After primary task completes |
| **Cleanup** | Last |

---

## Phase 4: Output

```
AND THEN ALSO
=============

PRIMARY TASK: [what the user asked to do]

BEFORE (prerequisites):
  1. [task] — [why needed first]
  2. [task] — [why needed first]

DURING (parallel):
  1. [task] — [why alongside]

AFTER (follow-ups — required):
  1. [task] — [why needed after]

OPTIONAL (consider):
  1. [task] — VALUE: [what it adds] — COST: [effort]

EXECUTION ORDER:
  [prereq 1] → [prereq 2] → PRIMARY TASK (+ parallel tasks) → [follow-up 1] → [follow-up 2]

READY FOR:
- /de [task list] — to extract detailed dependencies
- /to [task list] — to sequence into execution plan
- /awtlytrn — to check if the expanded scope is feasible
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Obvious padding** | Listing things the user clearly already planned | Focus on NON-OBVIOUS adjacents; flag obvious ones as "likely already planned" |
| **Infinite cascade** | Adjacent tasks spawn more adjacents | Expand ONE level; flag second-order without expanding |
| **Everything required** | No optional items | Some adjacents are genuinely optional. Mark them |
| **Missing prerequisites** | Follow-ups listed but prerequisites missed | Always check prerequisites FIRST — they block the primary task |
| **Overwhelming list** | 15+ adjacent tasks | Required list should be 3-7 items. More = scope compression needed |
| **Context-blind** | Generic adjacents not tailored to the domain | Adjacent tasks depend on context — a personal project ≠ enterprise deployment |

---

## Depth Scaling

| Depth | Discovery Lenses | Max Required | Max Optional | Second-Order |
|-------|-----------------|-------------|-------------|-------------|
| 1x | 3 | 3 | 2 | Flagged only |
| 2x | 5 | 5 | 4 | Flagged with notes |
| 4x | 7 (all) | 8 | 6 | Partially expanded |
| 8x | 7 + domain-specific | 12 | 10 | Fully expanded |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Primary request clearly stated
- [ ] Adjacent tasks discovered from multiple lenses
- [ ] Each adjacent classified as prerequisite/parallel/follow-up/optional
- [ ] Obvious adjacents flagged (not padded into the list as if novel)
- [ ] Required list is manageable (3-7 items)
- [ ] Execution order respects dependencies
- [ ] Second-order adjacents flagged but not expanded
- [ ] Optional items have value/cost assessment

---

## Integration

- Use from: any task or action request
- Complementary: `/de` (dependency extraction), `/to` (sequencing)
- Differs from `/de`: de extracts dependencies between existing tasks; ata discovers tasks that should exist
- Differs from `/fonss`: fonss sequences skills; ata discovers adjacent tasks
- Routes to: `/awtlytrn` if expanded scope raises feasibility questions
