---
name: "ugav5 - Universal Goal Analysis v5 (Operational & Meta-Cognitive)"
description: "Goal analysis adding operational load assessment, meta-cognitive sustainability, and quality validation categories. Catches goals that are analytically sound but operationally unsustainable. Consolidated into /uga but usable standalone."
tier: "tier4"
categories: ["Goal Processing"]
tags: ["goal", "operational", "metacognitive", "sustainability", "quality"]
output:
  format: "prose"
---

# Universal Goal Analysis v5: Operational, Meta-Cognitive & Quality

**Input**: $ARGUMENTS

---

## Core Principles

1. **Sound strategy fails under unsustainable load.** v5 exists because v1-v4 could produce a perfect analysis of a goal that would burn out the executor in week three. Operational viability is not optional — it is a constraint as hard as budget or time.

2. **Cognitive load is a finite resource.** A goal that requires constant decision-making drains the same resource needed for execution. Goals that can pre-decide recurring choices are operationally cheaper than goals that require real-time judgment.

3. **The metric is not the goal.** When you measure progress, you create incentive to optimize the metric rather than the outcome. v5 explicitly checks for metric gaming: are you improving the dashboard or improving the reality?

4. **Attention allocation determines outcome.** The percentage of your attention directed at a goal, relative to your other goals, predicts progress better than strategy quality. A brilliant strategy receiving 5% attention loses to a mediocre strategy receiving 40%.

5. **Validation must be external.** "It feels like it's working" is not validation. v5 requires at least one validation method that could return a negative result even when the executor believes things are going well.

---

## Phase 1: Goal State Assessment

```
[A] GOAL: [stated goal]
[B] CURRENT_STATE: [where things stand right now]
[C] EXISTING_ANALYSIS: [has /uga, /ugav2, /ugav3, or /ugav4 been run? what did they find?]
[D] STRATEGY_IN_PLACE: [Y/N — if Y, summarize the strategy being assessed]
```

---

## Phase 2: Operational Load Assessment

### 2a. Capacity Audit

```
[E] CAPACITY:

Step 1: Estimate current capacity utilization
    - Hours/week available for this goal: [N]
    - Hours/week this goal actually needs: [M]
    - Other active goals competing for time: [list with hours each]
    - Total committed hours: [sum]
    - Total available hours: [realistic weekly capacity]
    - UTILIZATION: [committed / available] × 100 = [X]%

Step 2: Assess slack
    IF utilization > 85%:
        → WARNING: No slack. Any disruption causes cascade failure.
        → What would you cut to create 20% slack? [answer]
    IF utilization > 100%:
        → CRITICAL: Overcommitted. Something is being dropped already.
        → What is being dropped? [answer]
```

### 2b. Decision Load

```
[F] DECISION_LOAD:

Step 1: List recurring decisions this goal requires
    | Decision | Frequency | Can Pre-Decide? | Cost of Wrong Call |
    |----------|-----------|-----------------|-------------------|
    | [decision] | [daily/weekly/monthly] | [Y/N] | [H/M/L] |

Step 2: Count decisions per week: [N]
Step 3: Identify pre-decidable decisions (create rules/policies to eliminate them)

[G] PRE_DECISIONS:
    1. [decision] → RULE: [always/never do X when Y]
    2. [decision] → RULE: [always/never do X when Y]
    Decisions eliminated: [N] → remaining: [M]
```

### 2c. Interruption Cost

```
[H] INTERRUPTIONS:

Step 1: What interrupts work on this goal? [list]
Step 2: For each interruption:
    - Frequency: [per day/week]
    - Recovery time: [minutes to get back to focused work]
    - Total cost: frequency × recovery time = [hours/week]
Step 3: Sum interruption cost: [total hours/week lost]
Step 4: Can any interruptions be batched or blocked? [list solutions]
```

### 2d. Queue and Handoff Analysis

```
[I] QUEUES:

Step 1: Where does work on this goal wait for someone else? [list]
Step 2: For each queue:
    - Average wait time: [duration]
    - What information is lost while waiting? [list]
    - Can the queue be shortened? [how]
Step 3: Total queue time: [sum of waits]
```

---

## Phase 3: Meta-Cognitive Sustainability

```
[J] COGNITIVE_LOAD:

Step 1: Does this goal consume mental bandwidth outside of work hours?
    - Thinking about it during off-hours? [Y/N — frequency]
    - Worry/anxiety about it? [Y/N — severity: low/medium/high]
    - Is this sustainable for the required duration? [Y/N]

[K] ATTENTION_ALLOCATION:
    - What % of total attention goes to this goal? [X%]
    - What % SHOULD go to it (based on priority)? [Y%]
    - Mismatch: [over-attending / under-attending / matched]
    - If mismatched: what's pulling attention away? [list]

[L] BURNOUT_RISK:
    Step 1: Score burnout indicators:
        - Required effort duration: [weeks/months/years]
        - Intensity: [sustainable / sprinting / unsustainable]
        - Recovery built in? [Y/N]
        - Intrinsic motivation: [high / medium / low / gone]
        - Social support: [present / absent]
    Step 2: BURNOUT_RISK = [LOW / MEDIUM / HIGH / IMMINENT]
    Step 3: If HIGH or IMMINENT:
        → What must change for this to become sustainable? [answer]
```

---

## Phase 4: Quality Validation

```
[M] VALIDATION_METHOD:

Step 1: How do you currently know your work on this goal is correct?
    - Feeling-based? ("it feels right") → INSUFFICIENT
    - Metric-based? ("numbers are going up") → CHECK FOR GAMING
    - External-based? ("someone else verifies") → ACCEPTABLE
    - Outcome-based? ("the actual thing I wanted is happening") → IDEAL

Step 2: Design a validation that could return NEGATIVE:
    - What would you check? [specific measure]
    - How often? [frequency]
    - What result would mean "this isn't working"? [threshold]
    - What would you do if you got that result? [contingency]

[N] CONSISTENCY_CHECK:
    - Are you applying the same quality standards across similar decisions? [Y/N]
    - Where might you be applying double standards? [identify]

[O] SIMPLIFICATION_OPPORTUNITY:
    - Is there a simpler approach that achieves 80% of the result? [describe]
    - What is the cost of the last 20%? [effort vs value]
    - Would the simpler approach be good enough? [Y/N — why]

[P] METRIC_GAMING_CHECK:
    - What metric are you tracking? [metric]
    - What outcome does the metric represent? [real thing]
    - Could the metric improve while the outcome worsens? [Y/N — how]
    - Are you optimizing the metric or the outcome? [honest assessment]
```

---

## Phase 5: Report

```
UGA v5 OPERATIONAL & META-COGNITIVE ANALYSIS:
Goal: [goal]

OPERATIONAL:
  Capacity utilization: [X]%
  Slack: [Y]% — [adequate / WARNING / CRITICAL]
  Decisions/week: [N] — pre-decidable: [M]
  Interruption cost: [hours/week]
  Queue time: [hours/week]

META-COGNITIVE:
  Cognitive load: [sustainable / unsustainable]
  Attention: [X]% actual vs [Y]% needed — [matched / over / under]
  Burnout risk: [LOW / MEDIUM / HIGH / IMMINENT]
  Sustainability: [this pace is / is not maintainable for required duration]

QUALITY:
  Validation: [method] — can return negative: [Y/N]
  Simplification: [opportunity identified / none]
  Metric gaming risk: [LOW / MEDIUM / HIGH]

OPERATIONAL RECOMMENDATIONS:
  1. [specific change to improve sustainability]
  2. [specific pre-decision to reduce decision load]
  3. [specific interruption fix]

SUSTAINABILITY VERDICT:
  [SUSTAINABLE / NEEDS ADJUSTMENT / UNSUSTAINABLE]
  Required change: [if not sustainable, what must change]
```

→ INVOKE: /uga $ARGUMENTS (for full analysis incorporating operational findings)

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Capacity denial** | Utilization calculated at 60% when person is clearly overwhelmed | Include ALL active commitments, not just this goal |
| **Feelings as validation** | Validation method is "I'll know it when I see it" | Require a method that can return NEGATIVE |
| **Metric gaming blindness** | Metric is improving but real outcome is flat or declining | Ask: could metric improve while outcome worsens? |
| **Burnout normalization** | High burnout risk accepted as "just how it is" | Flag: is this sprint or marathon? Sprints end. Marathons need sustainability |
| **Ignoring attention mismatch** | Goal receives 10% attention but requires 40% | Name the competing demands explicitly |
| **Skipping pre-decisions** | All recurring decisions left as real-time judgment calls | Force: for each recurring decision, can a rule replace judgment? |

---

## Depth Scaling

| Depth | Operational | Meta-Cognitive | Quality |
|-------|------------|----------------|---------|
| 1x | Capacity utilization estimate | Burnout risk score | Single validation method |
| 2x | Full capacity + decision load + interruptions | Attention allocation + sustainability | Validation + metric gaming check |
| 4x | All operational categories + queue analysis | Full meta-cognitive with trend analysis | All quality checks + simplification analysis |
| 8x | Operational simulation (model week-by-week load) | Cognitive load diary design | Validation system design with feedback loops |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Capacity utilization calculated with all commitments included
- [ ] Decision load counted and pre-decidable decisions identified
- [ ] Interruption cost quantified in hours/week
- [ ] Burnout risk scored with indicators
- [ ] Attention allocation actual vs needed compared
- [ ] Validation method designed that can return negative
- [ ] Metric gaming explicitly checked
- [ ] Sustainability verdict issued with required changes if unsustainable

---

## Integration

- **Consolidated into**: `/uga` (which uses v5's categories in Steps 14-16)
- **Use standalone when**: Strategy exists but sustainability is in question
- **Routes to**: `/uga` (full analysis), `/pre` (energy/sustainability check)
- **Invoked by**: Users with a plan that feels unsustainable
- **Differs from /uga**: /uga runs all 17 steps; ugav5 focuses on operational viability
- **Differs from /ugav4**: ugav4 focuses on leverage and communication
- **Differs from /pre**: /pre assesses personal energy broadly; ugav5 assesses operational load for a specific goal
