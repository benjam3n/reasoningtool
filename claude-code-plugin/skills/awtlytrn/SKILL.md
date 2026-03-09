---
name: "awtlytrn - Also What's The Limit You Think Right Now"
description: "Estimate current practical limits for scope, throughput, and quality across multiple dimensions, then recommend a safe operating boundary that accounts for planning fallacy."
---

# AWTLYTRN - Also What's The Limit You Think Right Now

**Input**: $ARGUMENTS

---

## Core Principles

1. **Limits are contextual, not fixed.** The same person can process 5 skills in one session and 20 in another depending on complexity, energy, familiarity, and tooling. Estimate limits for THIS context, not in general.

2. **People overestimate consistently.** The planning fallacy is universal. Whatever the estimated limit is, apply a discount. The question isn't "what do you think the limit is?" but "what is the limit ACTUALLY, given what you think it is?"

3. **Three dimensions compete.** Scope (how much), quality (how good), and throughput (how fast) form a triangle. You can optimize two at the expense of the third. The skill must make this tradeoff explicit.

4. **Safe boundary ≠ maximum.** The safe operating boundary is below the theoretical maximum. It accounts for interruptions, errors, rework, and energy depletion. Operating at the theoretical max guarantees failure.

5. **Limits change.** Yesterday's limit isn't today's. Learning, tooling, and fatigue all shift the boundary. The estimate is a snapshot, not a permanent assessment.

---

## Phase 1: Context Assessment

```
[L1] SUBJECT: [what is being limited — a project, a session, a sprint, a task]
[L2] DIMENSION_PRIMARY: [scope | throughput | quality — which matters most?]
[L3] RESOURCES: [time available, energy level, tool availability, skill level]
[L4] COMPLEXITY: [how complex is each unit of work?]
[L5] PRIOR_EXPERIENCE: [has the user done similar work? At what scale?]
```

---

## Phase 2: Limit Estimation

Estimate limits across three dimensions:

```
[L6] SCOPE ESTIMATE:
  OPTIMISTIC: [maximum items/features/tasks if everything goes perfectly]
  REALISTIC: [what's achievable with normal interruptions and errors]
  PESSIMISTIC: [what's achievable if things go worse than expected]
  DISCOUNT: [optimistic × 0.6-0.8 = realistic — what discount factor?]

[L7] THROUGHPUT ESTIMATE:
  OPTIMISTIC: [items per hour/day if perfectly focused]
  REALISTIC: [items per hour/day with breaks, context switches, rework]
  PESSIMISTIC: [items per hour/day if blockers arise]
  DISCOUNT: [optimistic × factor = realistic]

[L8] QUALITY ESTIMATE:
  AT_CURRENT_SCOPE: [quality level achievable at current scope plan]
  AT_REDUCED_SCOPE: [quality level if scope is cut 30%]
  AT_EXPANDED_SCOPE: [quality level if scope is increased 30%]
```

### Planning Fallacy Corrections

| Bias | Correction |
|------|-----------|
| **"I'll be focused the whole time"** | Assume 60-70% effective focus time |
| **"Each item takes about X minutes"** | Multiply by 1.5 for items you've done before, 2-3x for novel items |
| **"I won't need to redo anything"** | Assume 15-20% rework rate |
| **"I know how to do this"** | Prior experience at smaller scale doesn't predict limits at larger scale |
| **"I can just push through"** | Quality degrades predictably with fatigue. Session 1 ≠ session 5 |

---

## Phase 3: Tradeoff Analysis

```
[L9] TRADEOFF TRIANGLE:
  CURRENT PLAN: [scope level] scope × [quality level] quality × [speed level] speed

  IF PRIORITIZE SCOPE: [more items, but quality drops to X or speed drops to Y]
  IF PRIORITIZE QUALITY: [fewer items, but each is higher quality]
  IF PRIORITIZE SPEED: [faster delivery, but scope or quality must give]

[L10] RECOMMENDED PRIORITY: [which dimension to optimize for, given context]
[L11] SACRIFICE: [which dimension takes the hit, and how much]
```

---

## Phase 4: Safe Operating Boundary

```
[L12] SAFE BOUNDARY:
  SCOPE: [N items — below the realistic estimate by a margin]
  THROUGHPUT: [N items per time unit — sustainable pace]
  QUALITY: [level — achievable at this scope and throughput]

  MARGIN: [how much buffer between safe and maximum]
  MARGIN_RATIONALE: [why this margin — based on complexity, experience, stakes]

[L13] DANGER ZONE:
  SCOPE_DANGER: [above N items, quality will degrade noticeably]
  THROUGHPUT_DANGER: [above N items/hour, errors will increase]
  QUALITY_DANGER: [below this level, output becomes unreliable]

[L14] CHECKPOINTS:
  AT_25%: [check these indicators to see if on track]
  AT_50%: [check these indicators]
  AT_75%: [if behind here, trigger scope reduction]
```

---

## Phase 5: Output

```
LIMIT ASSESSMENT
================

SUBJECT: [what]
CONTEXT: [resources, complexity, experience]

ESTIMATES:
  SCOPE: [optimistic → realistic → pessimistic]
  THROUGHPUT: [optimistic → realistic → pessimistic]
  QUALITY: [at current scope → at reduced → at expanded]

TRADEOFF: Prioritize [dimension] — sacrifice [dimension]

SAFE OPERATING BOUNDARY:
  SCOPE: [N items]
  THROUGHPUT: [N per time unit]
  QUALITY: [level]
  MARGIN: [X% below maximum]

DANGER ZONES:
  [what triggers quality/throughput degradation]

CHECKPOINTS:
  [when to check and what to look for]

READY FOR:
- /de [task list] — to extract dependencies within the safe scope
- /to [task list] — to sequence work within throughput limits
- /iagca — if scope needs aggressive compression
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **No discount applied** | Realistic estimate equals optimistic | Apply planning fallacy corrections — always discount |
| **Single dimension** | Only scope estimated, no quality/throughput | All three dimensions must be estimated |
| **No safe boundary** | Maximum treated as target | Safe boundary must be below maximum with explicit margin |
| **No checkpoints** | Plan to check only at the end | Place checkpoints at 25%, 50%, 75% |
| **Fixed limits** | "I can always do N" without context | Limits depend on complexity, energy, familiarity |
| **Bravado** | "I'll just push through" | Fatigue curves are real. Session 1 quality ≠ session 5 quality |

---

## Depth Scaling

| Depth | Dimensions Estimated | Planning Fallacy Checks | Checkpoints | Tradeoff Analysis |
|-------|---------------------|------------------------|-------------|------------------|
| 1x | 2 | 2 | 1 | Binary (which to prioritize) |
| 2x | 3 | 4 | 3 | Full triangle |
| 4x | 3 + sub-dimensions | All 5 | 4 with indicators | Triangle + scenario analysis |
| 8x | 3 + sub-dimensions | All + custom biases | 5 with contingencies | Full with fallback plans |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Context assessed (resources, complexity, experience)
- [ ] All three dimensions estimated (scope, throughput, quality)
- [ ] Optimistic/realistic/pessimistic ranges provided
- [ ] Planning fallacy discount applied
- [ ] Tradeoff triangle made explicit
- [ ] Safe boundary is below maximum with stated margin
- [ ] Danger zones identified
- [ ] Checkpoints placed with specific indicators

---

## Integration

- Use from: project planning, sprint planning, session planning
- Complementary: `/iagca` (when scope needs compression after limit found)
- Complementary: `/de` (dependency extraction within safe scope)
- Differs from `/iagca`: iagca compresses scope after sprawl; awtlytrn estimates limits before committing
