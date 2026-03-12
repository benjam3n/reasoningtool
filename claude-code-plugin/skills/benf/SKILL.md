---
name: "benf - Benefit Estimation"
description: Estimates the benefits of an action or investment. Lists direct, indirect, and downstream benefits, quantifies where possible, and calculates expected value.
output:
  format: "prose"
---

# Benefit Estimation

**Input**: $ARGUMENTS

---

## Step 1: Identify All Potential Benefits

Cast a wide net. Include direct, indirect, and downstream effects.

```
ACTION/INVESTMENT: [What is being evaluated for benefits]

DIRECT BENEFITS (immediate, obvious results):
1. [Benefit 1] — who gains: [beneficiary]
2. [Benefit 2] — who gains: [beneficiary]

INDIRECT BENEFITS (second-order effects):
1. [Benefit 1] — mechanism: [how it arises from the direct benefits]
2. [Benefit 2] — mechanism: [how it arises from the direct benefits]

DOWNSTREAM BENEFITS (long-term, compounding effects):
1. [Benefit 1] — timeline: [when it materializes]
2. [Benefit 2] — timeline: [when it materializes]

TOTAL BENEFITS IDENTIFIED: [count]
```

---

## Step 2: Quantify Where Possible

Put numbers on benefits that can be measured. Be honest about precision.

```
QUANTIFIABLE BENEFITS:
1. [Benefit] — estimated value: [number + unit]
   Basis: [How did you arrive at this number?]

2. [Benefit] — estimated value: [number + unit]
   Basis: [How did you arrive at this number?]

NON-QUANTIFIABLE BENEFITS:
1. [Benefit] — qualitative impact: [HIGH/MEDIUM/LOW]
   Description: [Why it matters even though you can't put a number on it]

2. [Benefit] — qualitative impact: [HIGH/MEDIUM/LOW]
   Description: [Why it matters even though you can't put a number on it]
```

---

## Step 3: Estimate Probability

Not all benefits are certain. Assess the likelihood of each materializing.

```
BENEFIT PROBABILITIES:
1. [Benefit] — probability: [0-100%] — confidence in probability: [HIGH/MEDIUM/LOW]
   Rationale: [Why this probability]

2. [Benefit] — probability: [0-100%] — confidence in probability: [HIGH/MEDIUM/LOW]
   Rationale: [Why this probability]

CORRELATED BENEFITS: [Which benefits rise and fall together?]
INDEPENDENT BENEFITS: [Which benefits materialize regardless of others?]
```

---

## Step 4: Calculate Expected Value

For quantifiable benefits, compute expected value. For non-quantifiable, provide a qualitative roll-up.

```
EXPECTED VALUE (quantifiable):
1. [Benefit]: [value] x [probability] = [expected value]
2. [Benefit]: [value] x [probability] = [expected value]

TOTAL EXPECTED VALUE: [sum]

QUALITATIVE EXPECTED VALUE:
- High-probability, high-impact: [list]
- High-probability, low-impact: [list]
- Low-probability, high-impact: [list — these are the wildcards]
```

---

## Step 5: State Total Benefit

```
TOTAL QUANTIFIED BENEFIT: [number with units]
CONFIDENCE RANGE: [low end] to [high end]
CONFIDENCE LEVEL: [50% / 80% / 90%]

KEY QUALITATIVE BENEFITS: [Top 2-3 that matter but can't be numbered]

BIGGEST UPSIDE RISK: [What could make benefits much larger than estimated?]
BIGGEST DOWNSIDE RISK: [What could make benefits fail to materialize?]

TIME TO REALIZE: [When do benefits start showing up?]
BENEFIT HALF-LIFE: [How long do the benefits last before they decay?]
```

---

## Integration

Use with:
- `/efrt` -> Pair with effort for a full ROI picture
- `/cba` -> Formal cost-benefit analysis using this benefit estimate
- `/ratn` -> Build a rationale around the benefits for stakeholders
