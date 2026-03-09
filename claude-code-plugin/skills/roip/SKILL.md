---
name: "roip - ROI Optimization"
description: Find the highest-return action in any set of options. Lists options, estimates costs and benefits, calculates ROI, sensitivity-tests top candidates, and recommends the best path.
---

# ROI Optimization

**Input**: $ARGUMENTS

---

## Step 1: List All Options

Enumerate every viable option, including "do nothing."

```
CONTEXT: [what decision or allocation is being optimized]
GOAL: [what "return" means here]

OPTIONS:
1. [option] — brief description
2. [option] — brief description
3. [option] — brief description
...
N. Do nothing / status quo
```

SKIP: If options are already enumerated in the input, restate them briefly and proceed.

---

## Step 2: Estimate Cost of Each

Cost includes time, money, effort, opportunity cost, and risk.

```
COST ESTIMATES:
| Option | Time | Money | Effort | Opportunity Cost | Risk | Total Cost Score |
|--------|------|-------|--------|-----------------|------|-----------------|
| [opt 1] | [est] | [est] | [est] | [est] | [est] | [1-10] |
| [opt 2] | [est] | [est] | [est] | [est] | [est] | [1-10] |
...

COST ASSUMPTIONS:
- [assumption 1]
- [assumption 2]
```

---

## Step 3: Estimate Benefit of Each

Benefit includes direct value, indirect value, learning, and optionality.

```
BENEFIT ESTIMATES:
| Option | Direct Value | Indirect Value | Learning | Optionality | Total Benefit Score |
|--------|-------------|----------------|----------|-------------|-------------------|
| [opt 1] | [est] | [est] | [est] | [est] | [1-10] |
| [opt 2] | [est] | [est] | [est] | [est] | [1-10] |
...

BENEFIT ASSUMPTIONS:
- [assumption 1]
- [assumption 2]
```

---

## Step 4: Calculate ROI

```
ROI RANKING:
| Rank | Option | Benefit | Cost | ROI (Benefit/Cost) | Confidence |
|------|--------|---------|------|-------------------|------------|
| 1 | [option] | [score] | [score] | [ratio] | [HIGH/MED/LOW] |
| 2 | [option] | [score] | [score] | [ratio] | [HIGH/MED/LOW] |
...

TOP 3:
1. [option] — ROI: [ratio] — Why: [brief rationale]
2. [option] — ROI: [ratio] — Why: [brief rationale]
3. [option] — ROI: [ratio] — Why: [brief rationale]
```

---

## Step 5: Sensitivity-Test Top Candidates

Stress-test the top options by varying assumptions.

```
SENSITIVITY ANALYSIS:

[Top option 1]:
- If [optimistic assumption]: ROI becomes [value]
- If [pessimistic assumption]: ROI becomes [value]
- Break-even requires: [minimum condition]

[Top option 2]:
- If [optimistic assumption]: ROI becomes [value]
- If [pessimistic assumption]: ROI becomes [value]
- Break-even requires: [minimum condition]

ROBUSTNESS: [which option holds up best across scenarios?]
FRAGILITY: [which option is most dependent on specific assumptions?]
```

---

## Step 6: Recommend

```
RECOMMENDATION: [the option with the best risk-adjusted ROI]

WHY THIS OPTION:
- [reason 1]
- [reason 2]

KEY RISK: [biggest thing that could make this wrong]
MITIGATION: [how to reduce that risk]
NEXT STEP: [concrete first action]

ALTERNATIVE IF RISK-AVERSE: [safer option with rationale]
```

---

## Integration

Use with:
- `/cba` -> Detailed cost-benefit analysis on the top candidate
- `/dcp` -> Structure the final decision formally
- `/gapf` -> Ensure no options were missed before optimizing
