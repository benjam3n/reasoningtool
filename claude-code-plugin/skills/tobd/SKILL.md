---
name: "tobd - To Be Determined (Operational)"
description: "Sequence unresolved TBDs by dependency and impact for operational resolution, identifying parallel tracks, blockers, and the critical resolution path."
output:
  format: "prose"
---

# TOBD - To Be Determined (Operational)

**Input**: $ARGUMENTS

---

## Core Principles

1. **Resolution order matters.** Resolving TBD-A might make TBD-B trivial or eliminate it entirely. Resolving in the wrong order wastes effort on decisions that would have been unnecessary.

2. **Dependencies create a critical path.** Some TBDs block everything downstream. Others are independent. The critical path determines the minimum time to clear all TBDs.

3. **Parallel resolution is faster.** Independent TBDs can be resolved simultaneously. Forcing them into a sequence when they don't depend on each other wastes time.

4. **Some TBDs resolve others.** A design decision might eliminate three downstream parameter decisions. Identify these "resolution cascades" — they're high-leverage.

5. **Operational means assignable.** Each resolution step should specify who does it, how, and by when. Abstract resolution plans don't get executed.

---

## Phase 1: TBD Inventory

If coming from `/tbd`, use its output. Otherwise, scan the input:

```
[O1] TBD_LIST:
  [O1a] TBD: [description] — TYPE: [type from /tbd] — BLOCKING: [what]
  [O1b] TBD: [description] — TYPE: [type] — BLOCKING: [what]
  ...
[O2] TBD_COUNT: [N items]
```

---

## Phase 2: Dependency Analysis

For each pair of TBDs, check:

```
[O-N] DEPENDENCY: [TBD-X] depends on [TBD-Y] — REASON: [why Y must be resolved first]
[O-N] INDEPENDENT: [TBD-X] and [TBD-Z] — REASON: [no dependency, can parallel]
[O-N] CASCADE: Resolving [TBD-X] eliminates [TBD-Y, TBD-Z] — REASON: [why]
```

### Dependency Types

| Type | Meaning | Implication |
|------|---------|------------|
| **Information dependency** | Y's answer provides information X needs | Resolve Y first |
| **Design dependency** | X's options depend on Y's decision | Resolve Y first |
| **Resource dependency** | Same person/resource needed for both | Sequence, don't parallel |
| **Cascade** | Y's resolution eliminates X | Resolve Y first (high leverage) |
| **Independent** | No connection between X and Y | Can resolve in parallel |

---

## Phase 3: Critical Path

```
[O-N] DEPENDENCY GRAPH:
  [TBD-Y] → [TBD-X] → [TBD-W]     (sequential chain)
  [TBD-Z] ∥ [TBD-V]                 (parallel, independent)
  [TBD-A] ⇒ eliminates [TBD-B, C]   (cascade)

[O-N] CRITICAL PATH: [the longest chain of dependent TBDs]
  Length: [N sequential resolutions]
  Estimated time: [time to resolve the chain]
  Bottleneck: [which TBD takes longest to resolve]

[O-N] PARALLEL TRACKS:
  Track 1: [TBD-Y] → [TBD-X] → [TBD-W]
  Track 2: [TBD-Z] ∥ [TBD-V]
  (tracks are independent and can run simultaneously)
```

---

## Phase 4: Resolution Plan

Order TBDs for operational resolution:

```
[O-N] RESOLUTION SEQUENCE:

ROUND 1 (resolve first — high leverage):
  1. [TBD] — WHO: [owner] — HOW: [method] — BY: [deadline]
     WHY_FIRST: [cascade or critical path position]
     EXPECTED_OUTCOME: [what resolving this unlocks]
  2. [TBD] (parallel with #1) — WHO: [owner] — HOW: [method] — BY: [deadline]

ROUND 2 (resolve after Round 1 completes):
  3. [TBD] — WHO: [owner] — HOW: [method] — BY: [deadline]
     DEPENDS_ON: [which Round 1 TBD]
     IF_CASCADED: [note if Round 1 resolution might eliminate this]

ROUND 3 (resolve after Round 2):
  4. [TBD] — WHO: [owner] — HOW: [method] — BY: [deadline]
  ...
```

### Resolution Methods

| TBD Type | Typical Method |
|----------|---------------|
| **Decision** | Meeting, decision framework, `/decide` |
| **Information** | Research, expert consultation, experiment |
| **Design** | Prototyping, design review, `/foht` |
| **Resource** | Budgeting, negotiation, allocation |
| **Scope** | Stakeholder discussion, prioritization |

---

## Phase 5: Output

```
OPERATIONAL TBD RESOLUTION
===========================

TBDs: [N total]
CRITICAL PATH: [N sequential steps, estimated time]
PARALLEL TRACKS: [N independent tracks]
CASCADE OPPORTUNITIES: [N high-leverage TBDs that eliminate others]

RESOLUTION PLAN:

ROUND 1 — [N TBDs, can parallel]:
  1. [TBD] — WHO: [owner] — HOW: [method] — BY: [deadline]
     UNLOCKS: [what becomes possible]
  2. [TBD] (∥ with #1) — WHO: [owner] — HOW: [method] — BY: [deadline]

ROUND 2 — [N TBDs, after Round 1]:
  3. [TBD] — DEPENDS_ON: [Round 1 item] — WHO: [owner] — BY: [deadline]

ROUND 3 — [N TBDs, after Round 2]:
  4. [TBD] — WHO: [owner] — BY: [deadline]

MIGHT_BE_ELIMINATED:
  [TBDs that cascade resolution might remove — check after each round]

READY FOR:
- Execute Round 1
- /decide [specific TBD] — for decision-type TBDs
- /foht [specific TBD] — for design-type TBDs
- /nsa [specific TBD] — for information-type TBDs with high uncertainty
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **All sequential** | No parallel tracks identified | Check each pair for independence — some are always parallel |
| **No cascades found** | Every TBD treated as independent | Ask: does resolving X change the options for Y? If yes, cascade |
| **No owners** | "Someone should decide" | Every resolution step needs a named owner |
| **Wrong order** | High-leverage cascade TBDs resolved last | Cascade TBDs should be in Round 1 (they eliminate others) |
| **Ignored dependencies** | TBDs sequenced by urgency, not dependency | A TBD might be urgent but unresolvable until its dependency is met |
| **No deadlines** | "Resolve soon" | Specific deadlines, even if approximate |

---

## Depth Scaling

| Depth | Dependency Pairs Checked | Cascade Detection | Parallel Tracks | Resolution Detail |
|-------|------------------------|--------------------|----------------|------------------|
| 1x | Key pairs only | 1 | 1 | Owner + deadline |
| 2x | All adjacent pairs | 2 | 2 | Owner + method + deadline |
| 4x | All pairs | Full cascade analysis | All tracks | Full with contingencies |
| 8x | All pairs + second-order | Full + cascade chains | All + optimization | Full + risk analysis |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All TBDs inventoried (from /tbd or fresh scan)
- [ ] Dependencies between TBDs analyzed
- [ ] Cascade opportunities identified (high-leverage TBDs)
- [ ] Critical path identified with estimated time
- [ ] Parallel tracks specified
- [ ] Resolution rounds ordered by dependency (not urgency alone)
- [ ] Each resolution step has owner, method, and deadline
- [ ] Cascaded TBDs flagged as "might be eliminated"

---

## Integration

- Use after: `/tbd` (which identifies and classifies TBDs)
- Routes to: `/decide`, `/foht`, `/nsa` for specific TBD resolution
- Differs from `/tbd`: tbd identifies and classifies; tobd sequences for resolution
- Differs from `/de`: de extracts dependencies between tasks; tobd extracts dependencies between decisions
- Differs from `/to`: to sequences tasks; tobd sequences decisions
