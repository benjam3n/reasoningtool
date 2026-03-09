---
name: "hpat - Historical Pattern Analysis"
description: Learn from what happened before to predict what happens next. Identify recurring patterns, test causality, and project forward.
---

# Historical Pattern Analysis

**Input**: $ARGUMENTS

---

## Step 1: Collect Historical Data

Gather the relevant historical events, data points, or precedents.

```
HISTORICAL RECORD:
| # | Date/Period | Event/Data Point | Outcome | Context |
|---|------------|------------------|---------|---------|
| 1 | [when]     | [what happened]  | [result]| [relevant circumstances] |
| 2 | [when]     | [what happened]  | [result]| [relevant circumstances] |
| 3 | [when]     | [what happened]  | [result]| [relevant circumstances] |
...
```

Rules:
- Include at least 5 data points if possible — fewer than 3 is too little to identify patterns
- Record context, not just events — the same event in different contexts means different things
- Include failures and non-events, not just successes — survivorship bias is the default error
- If historical data is unavailable, state that explicitly and note what you're inferring from

---

## Step 2: Identify Recurring Patterns

Look for repetition, cycles, trends, and regularities.

```
PATTERNS IDENTIFIED:
1. [Pattern name]: [Description]
   - Occurrences: [which data points show this pattern]
   - Frequency: [how often it recurs]
   - Strength: [STRONG / MODERATE / WEAK]

2. [Pattern name]: [Description]
   - Occurrences: [which data points]
   - Frequency: [how often]
   - Strength: [STRONG / MODERATE / WEAK]
...
```

Rules:
- A pattern requires at least 2 occurrences — one instance is an anecdote
- Distinguish between patterns in the data vs. patterns you're imposing on the data
- Look for anti-patterns too — things that conspicuously DON'T happen
- Note the time intervals between occurrences — regular intervals suggest mechanism, irregular suggest coincidence

---

## Step 3: Test Causality vs. Coincidence

For each pattern, assess whether it's causal, correlational, or coincidental.

```
CAUSALITY ASSESSMENT:
1. [Pattern]:
   - Proposed mechanism: [Why would this pattern exist? What causes it?]
   - Alternative explanations: [What else could explain the pattern?]
   - Confounders: [What third factors could be driving both sides?]
   - Verdict: [LIKELY CAUSAL / CORRELATIONAL / POSSIBLY COINCIDENTAL]

2. [Pattern]:
   ...
```

Rules:
- Having a plausible mechanism is necessary but not sufficient for causality
- The more alternative explanations you can generate, the weaker the causal claim
- Small sample sizes make everything look more patterned than it is
- "We've always done it this way" is not evidence of a causal pattern

---

## Step 4: Project Patterns Forward

Use validated patterns to make predictions about what happens next.

```
FORWARD PROJECTIONS:
1. Based on [pattern]: [What the pattern predicts will happen next]
   - Expected timing: [when]
   - Confidence: [HIGH / MEDIUM / LOW]
   - Key assumption: [what must remain true for this projection to hold]

2. Based on [pattern]: [prediction]
   ...
```

Rules:
- Only project from patterns rated "likely causal" or "correlational" with strong evidence
- State confidence honestly — most historical projections deserve medium or low confidence
- Identify the key assumption — this is what to monitor
- Shorter time horizons deserve higher confidence than longer ones

---

## Step 5: Identify Where Patterns Might Break

The most valuable part — find conditions that would invalidate the patterns.

```
PATTERN BREAKERS:
1. [Pattern] could break if:
   - [Condition]: [Why this would disrupt the pattern]
   - [Condition]: [Why this would disrupt the pattern]
   - Current likelihood of breaking: [HIGH / MEDIUM / LOW]

2. [Pattern] could break if:
   ...

NOVEL FACTORS (things that have no historical precedent):
- [Factor]: [Why it might change everything]
```

Rules:
- Every pattern has breaking conditions — if you can't find any, you haven't looked hard enough
- Technology changes, regime changes, and structural shifts are the most common pattern breakers
- "Novel factors" are the most dangerous — they make all historical patterns unreliable
- If a novel factor is present, downgrade all projection confidence by one level

---

## Integration

Use with:
- `/pcl` -> Test a specific prediction derived from historical patterns
- `/fctl` -> Verify the factual claims underlying the historical record
- `/cscl` -> Rigorously test causal claims found in Step 3
- `/ltai` -> Use pattern analysis to calibrate AI capability forecasts
