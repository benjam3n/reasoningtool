---
name: "mets - Metric Selection"
description: Choose the right things to measure by evaluating candidate metrics for actionability, gaming resistance, and alignment with goals. Plans for Goodhart's Law.
---

# Metric Selection

**Input**: $ARGUMENTS

---

## Step 1: Identify What You're Trying to Achieve

Metrics serve goals. Start with the goal, not the data.

```
OBJECTIVE: [what you're trying to achieve — one sentence]
TIME HORIZON: [when would you judge success?]
WHO CARES: [who will use these metrics to make decisions?]
CURRENT STATE: [what are you measuring now, if anything?]
WHY CURRENT METRICS FAIL: [if applicable — why you need new ones]
```

---

## Step 2: List Candidate Metrics

Generate a broad list before narrowing. Think across dimensions.

```
CANDIDATE METRICS:

Output metrics (what you produce):
1. [metric]
2. [metric]

Outcome metrics (what changes because of what you produce):
1. [metric]
2. [metric]

Input metrics (what you invest):
1. [metric]
2. [metric]

Efficiency metrics (output per unit input):
1. [metric]
2. [metric]

Quality metrics (how good, not how much):
1. [metric]
2. [metric]

Satisfaction metrics (how stakeholders feel):
1. [metric]
2. [metric]
```

---

## Step 3: Evaluate Each Candidate

Score every candidate metric against five criteria.

```
METRIC EVALUATION:

| Metric | Actionable? | Gaming-resistant? | Measurable? | Timely? | Aligned? | Score |
|--------|------------|-------------------|-------------|---------|----------|-------|
| [metric 1] | Y/N | Y/N | Y/N | Y/N | Y/N | /5 |
| [metric 2] | Y/N | Y/N | Y/N | Y/N | Y/N | /5 |

CRITERIA DEFINITIONS:
- ACTIONABLE: Can you change behavior based on this number?
- GAMING-RESISTANT: Is it hard to improve the number without improving the real thing?
- MEASURABLE: Can you actually collect this data reliably?
- TIMELY: Does it move fast enough to be useful for decisions?
- ALIGNED: Does improving this metric actually advance the objective?
```

---

## Step 4: Select Primary and Secondary Metrics

Less is more. Pick a focused set.

```
PRIMARY METRIC (the one number that matters most):
[metric] — Because: [why this is the single best signal]

SECONDARY METRICS (provide context and guard against distortion):
1. [metric] — Guards against: [what the primary metric might miss]
2. [metric] — Guards against: [what the primary metric might miss]

COUNTER-METRICS (ensure the primary metric isn't gamed):
1. [metric] — Ensures: [what it protects]

DIAGNOSTIC METRICS (for investigation, not dashboards):
1. [metric] — Useful when: [condition]

TOTAL METRICS IN REGULAR USE: [number — flag if > 5]
```

---

## Step 5: Define Targets

Set targets that are meaningful, not arbitrary.

```
TARGETS:

| Metric | Current | Target | Basis for Target | Timeline |
|--------|---------|--------|-----------------|----------|
| [primary] | [value] | [value] | [benchmark / improvement rate / requirement] | [by when] |
| [secondary 1] | [value] | [value] | [basis] | [by when] |
| [secondary 2] | [value] | [value] | [basis] | [by when] |

TARGET-SETTING APPROACH:
- [ ] Benchmarked against peers/industry
- [ ] Based on historical improvement rate
- [ ] Derived from a business requirement
- [ ] Set as a stretch goal (with rationale)

REVIEW CADENCE: [how often targets are reassessed]
```

---

## Step 6: Plan for Goodhart's Law

"When a measure becomes a target, it ceases to be a good measure."

```
GOODHART'S LAW ANALYSIS:

For [primary metric]:
- HOW COULD SOMEONE HIT THE TARGET WITHOUT ACHIEVING THE GOAL?
  1. [gaming scenario]
  2. [gaming scenario]

- WHAT PERVERSE INCENTIVES DOES THIS METRIC CREATE?
  1. [behavior that optimizes the number but hurts the real objective]

- SAFEGUARDS:
  1. [counter-metric or qualitative check]
  2. [process control — e.g., auditing, peer review]
  3. [metric rotation — periodically change what you emphasize]

METRIC HEALTH CHECK SCHEDULE:
- Every [period], ask: "Are people optimizing for the metric or the goal?"
- Signs the metric has been corrupted: [what to watch for]
- Replacement plan: [what to measure instead if this metric stops working]
```

---

## Integration

Use with:
- `/dshb` -> Design a dashboard around the selected metrics
- `/abts` -> Design experiments to validate that a metric predicts outcomes
- `/cba` -> Cost-benefit analysis of measurement systems
