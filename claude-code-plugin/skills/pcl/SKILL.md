---
name: "pcl - Predictive Claim Analysis"
description: Evaluate a prediction. Assess the model behind it, check track records, identify falsifiers, and estimate probability with calibration.
output:
  format: "prose"
---

# Predictive Claim Analysis

**Input**: $ARGUMENTS

---

## Step 1: State the Prediction Precisely

Rewrite the prediction so it can be unambiguously evaluated.

```
ORIGINAL PREDICTION: [as stated]
PRECISE PREDICTION: [rewritten with specific outcome, timeframe, and measurable criteria]
PREDICTION TYPE: [trend extrapolation / model-based / expert judgment / statistical / speculative]
DEADLINE: [when the prediction can be evaluated]
```

Rules:
- A prediction without a timeframe is not a prediction — add one or flag as untestable
- A prediction without measurable criteria is not a prediction — add criteria or flag
- "X will grow" is vague; "X will exceed Y by Z date" is testable
- If the prediction is conditional ("if A, then B"), state both parts clearly

---

## Step 2: Identify the Model

What mechanism or reasoning supports this prediction?

```
UNDERLYING MODEL:
- Theory/mechanism: [Why the predictor believes this will happen]
- Key assumptions: [What must be true for the model to work]
  1. [Assumption]
  2. [Assumption]
  3. [Assumption]
- Model type: [causal theory / trend extrapolation / analogy / gut feeling / statistical model]
- Model quality: [WELL-TESTED / REASONABLE / UNTESTED / DUBIOUS]
```

Rules:
- Every prediction has an implicit model, even if the predictor hasn't stated it
- Trend extrapolation assumes the future resembles the past — state that assumption explicitly
- If the model is "gut feeling" or "I just think so," the prediction deserves low confidence
- Check if the model has been tested in other contexts

---

## Step 3: Check Track Record

Assess how well similar predictions have performed.

```
TRACK RECORD:
- Has this predictor made similar predictions before? [YES / NO / UNKNOWN]
- Accuracy of past predictions: [if known]
- Have similar predictions by others been accurate? [examples]
- Base rate for this type of prediction: [how often predictions like this come true]
- Domain-specific accuracy: [are predictions in this domain generally reliable?]
```

Rules:
- Track record is the single best predictor of prediction quality
- Most people overestimate their prediction accuracy — check actual results, not claims
- Domain matters: weather predictions are well-calibrated; political predictions often aren't
- If no track record exists, this significantly limits confidence

---

## Step 4: Identify Falsifiers

What would prove this prediction wrong?

```
FALSIFICATION CONDITIONS:
- The prediction is WRONG if: [specific observable outcome]
- Early warning signs it's failing: [things to watch before the deadline]
- What the predictor would say if it fails: [predicted excuse / reinterpretation]
- Is the prediction structured to be unfalsifiable? [assessment]
```

Rules:
- If nothing could prove the prediction wrong, it's not a real prediction
- Watch for "moving the goalposts" — predictions that get reinterpreted after failure
- Early warning signs are actionable — they let you update before the deadline
- Vague predictions are easy to claim as "right" after the fact

---

## Step 5: Assess Base Rate

What's the prior probability before considering this specific prediction?

```
BASE RATE ANALYSIS:
- How often does [predicted outcome] happen in general? [rate]
- How often do predictions of this type come true? [rate]
- Does this prediction claim something common or rare?
- Base rate adjusted probability: [percentage estimate before considering specific evidence]
```

Rules:
- Rare events are predicted far more often than they occur — base rate matters
- If the base rate is 5% and the prediction claims certainty, demand very strong evidence
- "This time is different" is the most expensive phrase in prediction history — prove it

---

## Step 6: Estimate Probability

Synthesize everything into a calibrated probability estimate.

```
PROBABILITY ESTIMATE:
- Point estimate: [X]% likelihood of occurring
- Range: [low]% to [high]%
- Confidence in the estimate itself: [HIGH / MEDIUM / LOW]

CALIBRATION CHECK:
- If you say 80%, are you right 80% of the time about similar claims? [assessment]
- Common bias direction: [overconfident / underconfident / well-calibrated]
- Adjusted estimate after bias correction: [X]%

KEY UNCERTAINTIES:
1. [What you don't know that would most change the estimate]
2. [Second most important uncertainty]
```

Rules:
- Use the full probability range — 50% is a legitimate answer meaning "I don't know"
- 90%+ requires very strong evidence, track record, and a tested model
- State the range, not just the point estimate — precision implies false confidence
- If your confidence in the estimate itself is low, say so — an uncertain estimate is honest

---

## Integration

Use with:
- `/fctl` -> Verify the factual claims that the prediction is based on
- `/cscl` -> Test the causal model underlying the prediction
- `/hpat` -> Check historical patterns that inform the prediction
- `/mocl` -> If the prediction involves possibility claims, analyze those separately
