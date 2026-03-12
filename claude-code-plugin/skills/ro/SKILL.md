---
name: "ro - Reorder a List Expertly"
description: "Reorder an existing list using an explicit objective, multi-dimensional scoring, dependency awareness, and sanity checks — producing a defensible best-to-worst order with confidence flags."
output:
  format: "ranked-list"
---

# RO - Reorder a List Expertly

**Input**: $ARGUMENTS

---

## Core Principles

1. **Order implies priority, and priority implies criteria.** Putting item A before item B is a claim that A matters more on some dimension. If you can't state the dimension, the ordering is arbitrary. Every reorder must be grounded in an explicit, stated objective.

2. **Multi-dimensional scoring exposes tradeoffs that intuitive ordering hides.** "This feels like it should be first" collapses multiple dimensions (impact, effort, urgency, risk) into a gut feeling. Decomposing into dimensions makes the tradeoffs visible and debatable.

3. **Dependencies override scores.** An item that scores lower but must come first (because other items depend on it) should come first. Dependency order trumps priority order when the list represents a sequence of execution, not just a ranking of importance.

4. **The hardest placements are in the middle.** Top and bottom items are usually obvious. The contentious placements are items 3-7 in a 10-item list. These deserve the most scrutiny and are where scoring dimensions provide the most value.

5. **Confidence is not uniform.** Some placements are certain ("this is definitely #1"), others are judgment calls ("this could be #3 or #6"). Flagging low-confidence placements is as important as the ordering itself — it tells the user where to apply their own judgment.

---

## Phase 1: Input Parsing

```
[R1] ORIGINAL_LIST: [the list as provided, preserving original order]
[R2] ITEM_COUNT: [N items]
[R3] OBJECTIVE: [what the reordering should optimize for — if not stated, infer and declare]
[R4] CONSTRAINTS: [any fixed positions, grouping requirements, or hard rules]
[R5] CONTEXT: [time horizon, audience, resource constraints — what shapes the optimal order]
[R6] LIST_TYPE: [priority ranking | execution sequence | preference order | severity order | other]
```

### Objective Inference

If the user doesn't state an objective:
1. Examine the list content for implicit purpose
2. State the inferred objective explicitly
3. Flag that it was inferred, not stated

---

## Phase 2: Scoring Dimensions

Select 3-6 dimensions tied to the objective:

```
[R7] DIMENSIONS:
  D1: [dimension name] — WEIGHT: [high | medium | low] — WHY: [connection to objective]
  D2: [dimension name] — WEIGHT: [high | medium | low] — WHY: [connection to objective]
  D3: [dimension name] — WEIGHT: [high | medium | low] — WHY: [connection to objective]
  ...
```

### Common Dimension Sets

| Objective | Suggested Dimensions |
|-----------|---------------------|
| **Impact maximization** | Impact magnitude, Feasibility, Time to impact, Reversibility |
| **Risk reduction** | Severity, Likelihood, Detectability, Mitigation cost |
| **Learning efficiency** | Prerequisite coverage, Difficulty curve, Transferability |
| **Execution planning** | Dependencies, Effort, Blocking potential, Quick wins |
| **User priority** | User value, Development cost, Strategic alignment, Urgency |

### Dimension Quality Rules

- Dimensions must be **independent** — scoring high on D1 shouldn't automatically mean scoring high on D2
- Dimensions must be **relevant** — each must connect to the stated objective
- Dimensions must be **discriminating** — if every item scores the same on a dimension, it's not useful

---

## Phase 3: Scoring

Score each item on each dimension:

```
[R-N] ITEM: [item name]
  D1: [score] — [brief justification]
  D2: [score] — [brief justification]
  D3: [score] — [brief justification]
  TOTAL: [weighted aggregate]
  CONFIDENCE: [high | medium | low]
```

### Scoring Scale

Use a consistent scale across all dimensions:
- **3-point scale** (low/medium/high) for quick assessments
- **5-point scale** (1-5) for standard assessments
- **Relative scale** (rank items within each dimension) for when absolute scoring is difficult

### Dependency Check

Before finalizing score-based order:

```
[R-N] DEPENDENCIES:
  [item A] REQUIRES: [item B] — must come after B regardless of score
  [item C] ENABLES: [items D, E] — placing C early unlocks more items
  [item F] INDEPENDENT: no dependencies
```

---

## Phase 4: Reordered Output

```
[R-N] REORDERED_LIST:
  1. [item] — SCORE: [total] — REASON: [why #1]
  2. [item] — SCORE: [total] — REASON: [why #2]
  3. [item] — SCORE: [total] — REASON: [why #3]
  ...
```

### Position Changes

```
[R-N] MOVEMENT:
  [item] — WAS: #[old] → NOW: #[new] — WHY: [what caused the change]
  [item] — WAS: #[old] → NOW: #[new] — WHY: [what caused the change]
  UNCHANGED: [items that stayed in their original position]
```

---

## Phase 5: Sanity Check

Verify the ordering makes sense:

```
[R-N] SANITY_CHECK:
  TOP_3_TEST: Do the top 3 items genuinely outrank everything below on the objective? [yes/no + reasoning]
  BOTTOM_3_TEST: Are the bottom 3 items genuinely lowest priority? [yes/no + reasoning]
  ADJACENCY_TEST: For any items scored within 1 point, is the tiebreak defensible? [yes/no + reasoning]
  DEPENDENCY_TEST: Does the order respect all identified dependencies? [yes/no]
  ADJUSTMENTS: [any changes made after sanity check]
```

### Confidence Flags

```
[R-N] CONFIDENCE_MAP:
  HIGH_CONFIDENCE: [items whose placement is very certain]
  LOW_CONFIDENCE: [items that could reasonably be placed 2+ positions differently]
  MOST_DEBATABLE: [the single item whose placement is most uncertain]
```

---

## Phase 6: Output

```
REORDERED LIST
==============

OBJECTIVE: [what the ordering optimizes for]
DIMENSIONS: [d1 (weight), d2 (weight), d3 (weight)]
SCALE: [scoring scale used]

REORDERED:
  1. [item]
     SCORE: [total] — REASON: [why this position]
  2. [item]
     SCORE: [total] — REASON: [why this position]
  3. [item]
     SCORE: [total] — REASON: [why this position]
  ...

KEY MOVEMENTS:
  [item]: #[old] → #[new] — [why]
  [item]: #[old] → #[new] — [why]

CONFIDENCE:
  MOST CERTAIN: [item at position N]
  LEAST CERTAIN: [item at position M] — COULD ALSO BE: [alternative positions]

DEPENDENCIES RESPECTED: [yes/no — details if no]

READY FOR:
- /cmp [item A] vs [item B] — to compare specific close-ranked items
- /list — to rebuild the list from scratch if scope changed
- /mv — to validate the reordered list is MECE
- /o — to rank as decision options with full tradeoff analysis
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **No objective stated** | Items reordered without saying what "better order" means | State the objective before scoring. If not given, infer and declare |
| **Vibes-based ordering** | "This feels right" without scoring | Decompose into dimensions, score each, then aggregate |
| **Uniform confidence** | Every placement marked as high confidence | Middle placements are almost always lower confidence. Be honest |
| **Dependencies ignored** | High-scoring item placed first but depends on a lower item | Run dependency check before finalizing order |
| **Dimensions not independent** | Two dimensions that always correlate | Replace correlated dimensions with a single combined dimension |
| **Score-only ordering** | Rigid score ordering ignoring practical considerations | Sanity check can override scores — but must state why |
| **Original order preserved** | Reorder produces the same order (may be correct, but verify) | If order unchanged, explicitly confirm the original was already optimal |
| **Tiebreaks hidden** | Adjacent items with same score, no stated tiebreak logic | All ties must have explicit tiebreak criteria |

---

## Depth Scaling

| Depth | Dimensions | Scoring Detail | Sanity Checks | Confidence Analysis |
|-------|-----------|---------------|--------------|-------------------|
| 1x | 3 | Quick (3-point) | Top/bottom only | Flag lowest confidence |
| 2x | 4 | Standard (5-point) with justification | Top 3, bottom 3, adjacency | Full confidence map |
| 4x | 5 | Detailed with evidence | All items reviewed | Confidence + sensitivity analysis |
| 8x | 6 | Full pairwise comparison | Complete + alternative orderings | Full + "what changes if weights shift" |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Objective stated explicitly (not assumed)
- [ ] Scoring dimensions defined with weights and rationale
- [ ] Every item scored on every dimension with brief justification
- [ ] Dependencies identified and respected in final order
- [ ] Sanity check performed on top 3, bottom 3, and close-ranked items
- [ ] Low-confidence placements flagged
- [ ] Position changes from original order shown with reasons
- [ ] Tiebreaks resolved explicitly

---

## Integration

- Use from: "reorder this", "prioritize this list", "what should I do first", "rank these"
- Routes to: `/cmp` (compare close-ranked items), `/list` (rebuild if scope changed), `/mv` (validate structure)
- Complementary: `/list` (build list with /list, optimize order with /ro)
- Differs from `/o`: o ranks options in a decision context with full tradeoff analysis; ro reorders an existing list by scoring dimensions
- Differs from `/list`: list builds from scratch with coverage checks; ro takes an existing list and reorders it
- Differs from `/op`: op determines execution order for procedures; ro ranks by any stated objective
