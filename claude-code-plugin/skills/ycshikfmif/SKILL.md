---
name: "ycshikfmif - You Can See How I Keep Finding More It's Fun"
description: "Capture ideation expansion loops — when finding more ideas is exciting but unbounded — and structure them into manageable exploration batches with stop conditions."
---

# YCSHIKFMIF - You Can See How I Keep Finding More It's Fun

**Input**: $ARGUMENTS

---

## Core Principles

1. **Expansion loops are valuable AND dangerous.** The excitement of finding more ideas is a genuine signal that the space is rich. But unbounded expansion delays execution indefinitely. Both things are true simultaneously.

2. **Batch, don't stop.** The answer to "I keep finding more" isn't "stop finding" — it's "batch what you have, explore the next batch later." This preserves the expansion energy while creating execution boundaries.

3. **Not all new ideas are equal.** Some expand into rich territory. Others are dead ends wearing exciting costumes. The batch must be sorted by promise before exploration.

4. **The fun is real information.** Excitement about finding more ideas signals a rich possibility space. Don't dismiss it. But channel it — fun without structure becomes procrastination.

5. **Stop conditions prevent infinite exploration.** Every batch needs a "done exploring this batch" condition. Without it, each batch expands into its own unbounded loop.

---

## Phase 1: Expansion Capture

Capture the current state of the expansion loop:

```
[K1] EXPANSION_CONTEXT: [what the user was originally trying to do]
[K2] IDEAS_FOUND_SO_FAR: [list all ideas currently on the table]
[K3] IDEA_COUNT: [N ideas]
[K4] EXPANSION_RATE: [accelerating | steady | decelerating]
[K5] EXPANSION_SOURCE: [where new ideas are coming from — brainstorming, research, conversation, association]
[K6] TIME_IN_EXPANSION: [how long has the user been finding more?]
```

---

## Phase 2: Idea Assessment

For each idea, quick-score:

```
[K-N] IDEA: [description]
  PROMISE: [high | medium | low] — [why]
  NOVELTY: [genuinely new | variant of existing | redundant]
  EFFORT_TO_EXPLORE: [small | medium | large]
  DEPENDENCY: [standalone | depends on [other idea]]
```

### Quick Filters

| Signal | Action |
|--------|--------|
| Redundant with existing idea | Merge or drop |
| Variant of existing idea | Keep only if the variant matters |
| Exciting but huge effort | Flag for later batch, not this one |
| Small effort + high promise | Promote to current batch |

---

## Phase 3: Batching

Sort ideas into batches:

```
[K-N] BATCH 1 — EXPLORE NOW (current session):
  Size: [N ideas]
  Stop condition: [when this batch is "done"]
  Ideas:
    1. [idea] — PROMISE: [level] — EFFORT: [level]
    2. [idea] — PROMISE: [level] — EFFORT: [level]
    ...

[K-N] BATCH 2 — EXPLORE NEXT (deferred, not abandoned):
  Size: [N ideas]
  Trigger: [when to open this batch]
  Ideas:
    1. [idea] — PROMISE: [level]
    2. [idea] — PROMISE: [level]
    ...

[K-N] PARKED (interesting but not now):
  1. [idea] — WHY_PARKED: [reason]
  2. [idea] — WHY_PARKED: [reason]

[K-N] DROPPED (not worth pursuing):
  1. [idea] — WHY_DROPPED: [redundant | low promise | too expensive]
```

### Batch Size Rules

| Context | Max Batch 1 Size |
|---------|-----------------|
| Quick exploration session | 3-5 ideas |
| Dedicated brainstorming | 5-8 ideas |
| Multi-day project | 8-12 ideas |
| Research program | 12-20 ideas |

---

## Phase 4: Stop Conditions

```
[K-N] BATCH 1 STOP CONDITIONS:
  TIME_LIMIT: [stop after N minutes/hours]
  IDEA_LIMIT: [stop after exploring N ideas in this batch]
  DIMINISHING_RETURNS: [stop when new findings per idea drop below threshold]
  SUFFICIENT_COVERAGE: [stop when N% of the original question is covered]
  EXECUTION_READY: [stop when you have enough to act on]

[K-N] EXPANSION_LOOP_DETECTOR:
  IF during Batch 1 exploration, new ideas spawn at rate > [threshold]:
    → PAUSE exploration
    → Capture new ideas to Batch 2
    → Return to Batch 1 stop condition check
    → DO NOT expand Batch 1
```

---

## Phase 5: Output

```
EXPANSION MANAGEMENT
====================

ORIGINAL GOAL: [what the user was trying to do]
IDEAS FOUND: [N total]
EXPANSION RATE: [level]

BATCH 1 — EXPLORE NOW ([N] ideas):
  1. [idea] — Promise: [level] — Effort: [level]
  2. [idea] — Promise: [level] — Effort: [level]
  ...
  STOP WHEN: [condition]

BATCH 2 — EXPLORE NEXT ([N] ideas):
  1. [idea] — Promise: [level]
  ...
  OPEN WHEN: [trigger]

PARKED ([N] ideas): [listed for reference, not abandoned]
DROPPED ([N] ideas): [with reasons]

LOOP PROTECTION: If new ideas emerge during Batch 1, capture to Batch 2.
Do NOT expand Batch 1.

READY FOR:
- Execute Batch 1 ideas
- /iagca — if Batch 1 is still too large
- /awtlytrn — to estimate limits for batch execution
- /ro — to reorder ideas within a batch
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **No batching** | All ideas in one huge list | Enforce batch limits per context |
| **Batch 1 too large** | 15+ ideas in "explore now" | Reduce to context-appropriate max |
| **No stop conditions** | Batch 1 has no endpoint | Every batch needs at least one stop condition |
| **Dropped = lost** | Good ideas permanently deleted | PARKED exists — defer, don't delete promising ideas |
| **Fun dismissed** | "Stop finding more" as the advice | Expansion is valuable — the problem is bounding, not stopping |
| **Loop re-entry** | Exploring Batch 1 spawns new expansion loop | Loop detector must catch and redirect new ideas to Batch 2 |
| **All ideas kept** | Nothing dropped or parked | Some ideas genuinely aren't worth it. Drop at least one |

---

## Depth Scaling

| Depth | Min Ideas Assessed | Batches | Stop Conditions | Promise Assessment |
|-------|-------------------|---------|----------------|-------------------|
| 1x | 5 | 2 (now/later) | 1 | Binary (high/low) |
| 2x | 10 | 3 (now/next/parked) | 3 | Three-level with reasoning |
| 4x | 20 | 4 (now/next/parked/dropped) | 5 | Full with novelty/effort |
| 8x | All | 4 + sub-batches | All types | Full + dependency mapping |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All current ideas captured (not just some)
- [ ] Each idea assessed for promise, novelty, and effort
- [ ] Ideas sorted into batches with size limits
- [ ] Batch 1 has explicit stop conditions
- [ ] Batch 2 has explicit trigger conditions
- [ ] Parked ideas preserved (not deleted)
- [ ] Dropped ideas have reasons
- [ ] Loop detector specified for re-expansion during Batch 1
- [ ] Original goal is still visible (not lost in expansion)

---

## Integration

- Use from: brainstorming sessions, research, any ideation that's expanding
- Complementary: `/iagca` (when scope needs aggressive compression)
- Complementary: `/awtlytrn` (to estimate execution limits for batch)
- Differs from `/iagca`: iagca compresses scope urgently; ycshikfmif structures ongoing expansion
- Differs from `/ma`: ma generates ideas deliberately; ycshikfmif manages organic expansion
