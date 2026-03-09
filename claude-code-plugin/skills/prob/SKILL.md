---
name: "prob - Probabilistic Reasoning"
description: Reason under uncertainty using Bayesian thinking, base rates, confidence calibration, and expected value. Avoid base rate neglect, conjunction fallacy, overconfidence, and other probability traps.
---

# Probabilistic Reasoning

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Estimate a probability**: The user wants to assign a well-calibrated probability to a specific outcome or claim — not a gut guess, but a structured estimate that accounts for base rates and evidence.
**Interpretation 2 — Make a decision under uncertainty**: The user faces a choice where outcomes are uncertain and wants to reason through expected values, risk, and information value before committing.
**Interpretation 3 — Check probabilistic reasoning**: The user has encountered (or produced) reasoning that involves probabilities and wants to audit it for common errors — base rate neglect, conjunction fallacy, anchoring, overconfidence, etc.

If ambiguous, ask: "I can help with estimating a probability, making a decision under uncertainty, or auditing probabilistic reasoning for errors — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Base rates first.** Before considering any specific evidence, find the base rate. How often does this type of thing happen in this reference class? Ignoring base rates is the single most common probability error.

2. **Update incrementally, not narratively.** Evidence should shift your probability estimate by a specific amount determined by its diagnosticity — not by how vivid or emotionally compelling it is. A dramatic anecdote and a dry statistic both get weighted by likelihood ratio, nothing else.

3. **Probabilities are not feelings.** "I feel like this will work" is not a probability. Translate every vague confidence into a number, then check: would you bet at those odds? If not, your stated probability is wrong.

4. **Distinguish uncertainty from risk.** Risk means known probability distribution. Uncertainty means you do not even know the distribution. Label which one you are dealing with. Methods for risk (expected value) fail under true uncertainty (need robustness, optionality).

5. **Conjunction can only reduce.** P(A and B) is always less than or equal to P(A) alone. Any estimate that makes a more specific scenario seem MORE likely than a general one has committed the conjunction fallacy. Check every compound estimate.

6. **Calibration over precision.** A well-calibrated "60-80%" is more useful than a false-precision "73.2%". State ranges. Track whether your ranges actually contain the truth at the stated rate.

---

## Phase 1: STRUCTURE — Frame the Probabilistic Question

### Step 1: Define What You Are Estimating

```
QUESTION: [Precise statement of what probability is being estimated]
TYPE: [Single event / Frequency / Conditional / Comparative]
REFERENCE CLASS: [What is the relevant base rate population?]
TIME HORIZON: [By when? Over what period?]
RESOLUTION CRITERIA: [How will we know if this happened or not?]
```

Rules:
- If the question is vague ("will this work?"), make it precise before proceeding
- Identify whether this is P(A), P(A|B), P(A and B), or P(A or B) — structure matters
- If multiple questions are embedded, separate them

### Step 2: Establish the Base Rate

[P1] **Base rate identification**: Find the relevant reference class and its frequency.

Ask:
- What is the broadest reference class this belongs to?
- What is the narrowest reference class with reliable data?
- How often does this type of outcome occur in that class?

```
REFERENCE CLASS: [description]
BASE RATE: [X%] — source: [where this comes from]
CONFIDENCE IN BASE RATE: [High / Medium / Low]
ALTERNATIVE REFERENCE CLASSES:
  - [Class 2]: [Y%] — [why this class might be more/less appropriate]
  - [Class 3]: [Z%] — [why this class might be more/less appropriate]
```

If no base rate data exists, use comparison classes and state uncertainty explicitly.

---

## Phase 2: UPDATE — Incorporate Evidence

### Step 3: List Evidence and Assess Diagnosticity

For each piece of evidence, determine its likelihood ratio: how much more likely is this evidence if the hypothesis is true versus false?

```
EVIDENCE INVENTORY:

[P2] Evidence: [description]
  P(evidence | hypothesis true): [estimate]
  P(evidence | hypothesis false): [estimate]
  Likelihood ratio: [ratio]
  Direction: [supports / opposes / neutral]
  Quality: [strong / moderate / weak / unreliable]

[P3] Evidence: [description]
  P(evidence | hypothesis true): [estimate]
  P(evidence | hypothesis false): [estimate]
  Likelihood ratio: [ratio]
  Direction: [supports / opposes / neutral]
  Quality: [strong / moderate / weak / unreliable]

[Continue for all significant evidence]
```

### Step 4: Bayesian Update

Apply evidence to the base rate using Bayes' theorem (informally or formally):

```
PRIOR: [base rate from Step 2] = [X%]

UPDATE CHAIN:
  After [P2]: [X%] → [Y%] (likelihood ratio [N], [direction])
  After [P3]: [Y%] → [Z%] (likelihood ratio [N], [direction])
  [Continue for each piece of evidence]

POSTERIOR: [final estimate] = [W%]
CONFIDENCE INTERVAL: [low% — high%]
```

Check: Does the posterior feel right? If it feels wrong, that is diagnostic — either your evidence weights are off or your intuition is miscalibrated. Investigate which.

---

## Phase 3: AUDIT — Check for Probability Errors

### Step 5: Error Scan

Run the input and your estimates through each known trap:

[P4] **Base rate neglect**: Did you anchor on specific evidence and ignore how common/rare this is in general?

[P5] **Conjunction fallacy**: Did you estimate P(A and B) higher than P(A)? Adding detail makes scenarios feel more plausible but mathematically less probable.

[P6] **Availability bias**: Are you overweighting evidence that is vivid, recent, or emotionally salient? What evidence is absent but relevant?

[P7] **Anchoring**: Did your first number dominate? Would you have reached a different estimate starting from a different anchor?

[P8] **Overconfidence**: Is your confidence interval too narrow? People who say "90% sure" are wrong about 40% of the time. Widen ranges.

[P9] **Neglect of priors**: Are you treating this as if it is the first time anyone has encountered this type of question? What does the outside view say?

[P10] **Independence assumption**: Are you treating events as independent when they are correlated? Correlated risks cluster — things fail together.

[P11] **Survivorship bias**: Are you only looking at cases where the outcome was visible? What about the cases that disappeared, failed silently, or were never recorded?

```
ERROR SCAN RESULTS:

| Error | Detected? | Impact on Estimate | Correction |
|-------|-----------|-------------------|------------|
| Base rate neglect | [Yes/No] | [How it distorts] | [Fix] |
| Conjunction fallacy | [Yes/No] | [How it distorts] | [Fix] |
| Availability bias | [Yes/No] | [How it distorts] | [Fix] |
| Anchoring | [Yes/No] | [How it distorts] | [Fix] |
| Overconfidence | [Yes/No] | [How it distorts] | [Fix] |
| Neglect of priors | [Yes/No] | [How it distorts] | [Fix] |
| Independence error | [Yes/No] | [How it distorts] | [Fix] |
| Survivorship bias | [Yes/No] | [How it distorts] | [Fix] |

CORRECTED ESTIMATE: [revised probability if any errors found]
```

---
## Phase 4: DECIDE — Expected Value and Action

### Step 6: Expected Value Calculation (if decision involved)

```
OUTCOMES:

| Outcome | Probability | Value/Cost | Expected Value |
|---------|------------|------------|----------------|
| [Outcome A] | [P(A)] | [+/- value] | [P * V] |
| [Outcome B] | [P(B)] | [+/- value] | [P * V] |
| [Outcome C] | [P(C)] | [+/- value] | [P * V] |

TOTAL EXPECTED VALUE: [sum]

VARIANCE: [how spread out are the outcomes?]
WORST CASE: [outcome and its probability]
RUIN RISK: [is there an outcome that is catastrophic and non-recoverable?]
```

If ruin risk exists: expected value is insufficient. Use a ruin-avoidance frame instead — no bet is worth taking if it includes a non-trivial chance of total loss.

### Step 7: Information Value

Before acting, ask: would getting more information change the decision?

```
INFORMATION VALUE:
- What information would most change your estimate? [describe]
- How much would it shift the probability? [estimate]
- What does that information cost to get? [time/money/effort]
- Is the expected value of that information greater than its cost? [yes/no]

RECOMMENDATION: [Act now / Gather information first / Wait and observe]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Neglecting base rates** | Jumping to evidence without establishing how common this is | Always start with "how often does this happen in general?" |
| **Fake precision** | Stating 73.2% when your real uncertainty spans 50-90% | Use ranges. State confidence intervals. Drop false decimals. |
| **Narrative probability** | "The story makes sense so it must be likely" | Stories always make sense. Check the math, not the plot. |
| **Symmetric updates** | Confirming evidence moves you +20% but disconfirming only -5% | Apply the same likelihood ratio logic in both directions. |
| **Ignoring correlation** | Treating risks as independent when they share causes | Map common causes. Correlated risks mean wider tails. |
| **Expected value worship** | Using EV when ruin risk exists | If an outcome is catastrophic, no positive EV justifies the bet. |

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/prob 4x [input]").

| Depth | Min Evidence Items | Min Error Checks | Min Reference Classes | Min Outcomes (if decision) |
|-------|-------------------|-------------------|-----------------------|---------------------------|
| 1x    | 2                 | 3                 | 1                     | 2                         |
| 2x    | 4                 | 5                 | 2                     | 3                         |
| 4x    | 6                 | 7                 | 3                     | 5                         |
| 8x    | 10                | 8                 | 4                     | 8                         |

These are floors. Go deeper where insight is dense. Compress where it is not.

---

## Pre-Completion Checklist

- [ ] Base rate identified from a defensible reference class
- [ ] Each piece of evidence assessed for diagnosticity, not just direction
- [ ] Posterior probability derived from prior + evidence, not from narrative
- [ ] Error scan completed — at least conjunction, base rate neglect, and overconfidence checked
- [ ] Confidence interval stated (not a point estimate)
- [ ] If decision: expected value calculated with ruin risk check
- [ ] If compound event: conjunction rule verified (P(A&B) <= P(A))
- [ ] Information value assessed before recommending action

---

## Integration

- **Use from**: `/ht` (hypothesis testing needs probability estimates), `/dcp` (decisions under uncertainty), `/cba` (expected value in cost-benefit)
- **Routes to**: `/ht` (when estimate needs empirical testing), `/aex` (when assumptions behind probability need extraction)
- **Differs from**: `/ht` focuses on designing tests; `/prob` focuses on estimating and calibrating probabilities correctly
- **Complementary**: `/aex` (surface assumptions behind estimates), `/rca` (when you need to understand why a probability is what it is)
