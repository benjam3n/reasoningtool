---
name: "nsa - Not Sure About"
description: "Convert uncertainty statements into typed uncertainty with confidence ranges, cost-of-uncertainty analysis, and concrete evidence-gathering actions."
output:
  format: "prose"
---

# NSA - Not Sure About

**Input**: $ARGUMENTS

---

## Core Principles

1. **Uncertainty has types.** Epistemic uncertainty (don't know the answer), aleatory uncertainty (inherently random), model uncertainty (using the wrong framework), and question uncertainty (not sure what the question is). Each type needs different handling.

2. **Not all uncertainty needs reducing.** Reducing uncertainty costs time and effort. If the decision is the same regardless of the uncertain factor, investigating is waste. Always check: does this uncertainty MATTER?

3. **Confidence is a range, not a point.** "Not sure" can mean 10% or 90%. Forcing an explicit range ("somewhere between 30-60%") makes the uncertainty tractable and comparable.

4. **The cheapest evidence first.** Don't commission a study when a 5-minute search would resolve the uncertainty. Order evidence-gathering by cost, not by rigor.

5. **Acting under uncertainty is sometimes optimal.** If the cost of delay exceeds the cost of being wrong, act now and correct later. The skill must identify when investigation is the right move AND when it isn't.

---

## Phase 1: Uncertainty Extraction

```
[U1] RAW_STATEMENT: [what the user is uncertain about, quoted]
[U2] SUBJECT: [what is uncertain — the specific thing]
[U3] STAKES: [what depends on this — what changes if the answer is X vs Y?]
```

### Multiple Uncertainties

If the statement contains multiple uncertainties, decompose:
```
[U4] UNCERTAINTY_1: [subject] — STAKES: [what depends on it]
[U5] UNCERTAINTY_2: [subject] — STAKES: [what depends on it]
...
```

---

## Phase 2: Uncertainty Classification

For each uncertainty:

```
[U-N] TYPE: [epistemic | aleatory | model | question]
[U-N] EVIDENCE: [why this type]
```

| Type | What It Means | Example | Resolution Strategy |
|------|--------------|---------|-------------------|
| **Epistemic** | Answer exists but you don't know it | "Not sure what the API rate limit is" | Find the answer — research, ask, test |
| **Aleatory** | Inherently random, no definitive answer | "Not sure if it'll rain tomorrow" | Estimate probabilities; plan for variance |
| **Model** | Using wrong framework to think about it | "Not sure if this is a marketing or product problem" | Reframe — try different models |
| **Question** | Not sure what you're actually uncertain about | "Something feels off but I don't know what" | Clarify the question first |

---

## Phase 3: Confidence Range

```
[U-N] CONFIDENCE_RANGE: [lower bound]% to [upper bound]%
[U-N] RANGE_REASONING: [what drives the bounds]
[U-N] WHAT_WOULD_MOVE_IT:
  UPWARD: [what evidence would increase confidence]
  DOWNWARD: [what evidence would decrease confidence]
```

### Calibration Checks

| Bias | Signal | Correction |
|------|--------|-----------|
| **Narrow range** | "I'm 70-75% sure" | Real uncertainty is wider. Are you genuinely that precise? |
| **Symmetric range** | "50% — could go either way" | Do you really have zero evidence? Usually there's asymmetry |
| **Round numbers** | "About 50%" / "About 80%" | These are anchors, not calibration. What specific evidence drives the number? |
| **Stated vs revealed** | Says "not sure" but acts with full confidence | Behavior reveals true confidence. Which is it? |

---

## Phase 4: Cost-of-Uncertainty Analysis

```
[U-N] DECISION_SENSITIVITY: [does this uncertainty change the decision? yes/no/partially]
[U-N] COST_OF_BEING_WRONG: [what happens if you act on wrong assumption? severity: low/medium/high/catastrophic]
[U-N] COST_OF_DELAY: [what happens if you investigate instead of acting? severity: low/medium/high/catastrophic]
[U-N] REVERSIBILITY: [if you act and are wrong, can you undo it? easily/with effort/no]
```

### Action Decision Matrix

| Decision Sensitivity | Cost of Wrong | Cost of Delay | Action |
|---------------------|--------------|---------------|--------|
| No (same decision either way) | Any | Any | **Stop investigating** — uncertainty doesn't matter |
| Yes | Low | High | **Act now** — correct if wrong later |
| Yes | High | Low | **Investigate** — the risk warrants evidence |
| Yes | High | High | **Partial action** — act on what's known, investigate the rest |
| Yes | Catastrophic | Any | **Investigate** — must reduce uncertainty before acting |

```
[U-N] RECOMMENDED_POSTURE: [investigate | act now | partial action | stop — uncertainty doesn't matter]
```

---

## Phase 5: Evidence-Gathering Plan

If RECOMMENDED_POSTURE is "investigate":

```
[U-N] EVIDENCE PLAN (ordered by cost, cheapest first):
  1. [action] — COST: [low/medium/high] — EXPECTED_RESOLUTION: [how much this reduces uncertainty]
  2. [action] — COST: [level] — EXPECTED_RESOLUTION: [amount]
  3. [action] — COST: [level] — EXPECTED_RESOLUTION: [amount]

[U-N] STOP_INVESTIGATING_WHEN: [condition — when is enough evidence enough?]
```

---

## Phase 6: Output

```
UNCERTAINTY ANALYSIS
====================

ORIGINAL: [quoted statement]

UNCERTAINTIES:
1. [subject]
   TYPE: [epistemic | aleatory | model | question]
   CONFIDENCE: [X%] to [Y%]
   STAKES: [what depends on this]
   DECISION_SENSITIVITY: [yes/no]
   COST_OF_WRONG: [level]
   COST_OF_DELAY: [level]

   RECOMMENDATION: [investigate | act now | partial action | doesn't matter]

   IF INVESTIGATE:
     1. [cheapest action first]
     2. [next cheapest]
     STOP WHEN: [condition]

   IF ACT NOW:
     ACT: [what to do]
     CORRECTION_PLAN: [what to do if wrong]

READY FOR:
- /ht [claim] — to formalize a testable hypothesis
- /ver [claim] — to verify against evidence
- /decide [decision] — if uncertainty feeds a decision
- /ar [assumption] — to explore what follows if the uncertain thing is true
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Type confusion** | Epistemic treated as aleatory (or vice versa) | Apply type definitions strictly — does an answer exist? |
| **Investigate everything** | Every uncertainty gets an evidence plan | Check decision sensitivity first — some don't matter |
| **Act on everything** | Uncertainty dismissed, action taken without checking | Check cost of being wrong — some uncertainties are catastrophic |
| **Vague confidence** | "Not very sure" without a range | Force a numeric range — even a wide one is better than nothing |
| **Missing cost analysis** | Evidence plan without cost ordering | Cheapest evidence first — always |
| **Infinite investigation** | No stop condition on evidence gathering | Always specify when enough is enough |
| **Question uncertainty ignored** | Treating "something feels off" as epistemic | If the question itself is unclear, clarify the question before seeking answers |

---

## Depth Scaling

| Depth | Min Uncertainties Analyzed | Calibration Checks | Cost Analysis | Evidence Actions |
|-------|--------------------------|-------------------|---------------|-----------------|
| 1x | 1 | 1 | Decision sensitivity only | 2 |
| 2x | 3 | 3 | Full matrix | 3 |
| 4x | 5 | All biases checked | Full matrix + reversibility | 5 |
| 8x | All identified | All + cross-uncertainty interactions | Full + scenario analysis | 8 |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Each uncertainty identified and separated
- [ ] Type classified (epistemic/aleatory/model/question)
- [ ] Confidence range specified (not vague)
- [ ] Calibration biases checked
- [ ] Decision sensitivity assessed (does this uncertainty matter?)
- [ ] Cost of wrong and cost of delay compared
- [ ] Recommended posture derived from cost analysis (not assumed)
- [ ] If investigating: evidence actions ordered by cost
- [ ] Stop condition specified for investigation

---

## Integration

- Use from: `/it` (when confidence is very low), natural language uncertainty detection
- Routes to: `/ht`, `/ver`, `/decide`, `/ar` depending on uncertainty type and posture
- Complementary: `/it` (handles "I think"), `/but` (handles objections)
- Differs from `/it`: it handles all "I think" claims; nsa specifically handles uncertainty
- Differs from `/ht`: ht formulates hypotheses; nsa analyzes the uncertainty itself
