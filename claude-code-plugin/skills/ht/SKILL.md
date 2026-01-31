---
name: "ht - Hypothesis Testing"
description: "Systematic procedure for formulating testable hypotheses, designing tests, and updating beliefs based on evidence. Supports context-adaptive variants."
context: fork
---

# Hypothesis Testing

**Input**: $ARGUMENTS

---

## Overview

Systematic procedure for formulating testable hypotheses, designing tests, and updating beliefs based on evidence.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/ht 4x [input]").

| Depth | Min Hypotheses | Min Tests per Hypothesis | Min Competing Explanations | Min Falsification Attempts |
|-------|----------------|--------------------------|----------------------------|----------------------------|
| 1x    | 2              | 1                        | 1                          | 1                          |
| 2x    | 3              | 2                        | 2                          | 2                          |
| 4x    | 5              | 3                        | 3                          | 3                          |
| 8x    | 7              | 4                        | 5                          | 5                          |
| 16x   | 10             | 6                        | 7                          | 8                          |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## Step 0: Context Detection and Variant Selection

Before full analysis, assess context:

| Factor | Value | Notes |
|--------|-------|-------|
| Time Pressure | URGENT / NEAR / NORMAL | |
| Stakes | HIGH / MED / LOW | |
| Domain Expertise | EXPERT / INTERMEDIATE / NOVICE | |
| Test Cost | CHEAP / EXPENSIVE | |

### Variant Selection

| Context | Variant | Steps |
|---------|---------|-------|
| URGENT | HT-Lite | 1 (clarify claim), 4 (minimal test), 7 (quick conclude) |
| LOW stakes + CHEAP test | HT-Quick | 1, 4, 5, 7 |
| EXPERT + known domain | HT-Check | 2-4, 7 (skip basics, focus on test design) |
| CHEAP test + learning goal | HT-After | 1, 4, 7 + document learnings |
| HIGH stakes + EXPENSIVE test | HT-Full | All 7 steps + replication planning |
| Default | HT-Standard | All 7 steps |

**Selected variant**: [variant] because [reasoning]

---

## Steps

### Step 1: Clarify the claim and scope
Precisely specify what is being claimed:

1. STATE THE CLAIM CLEARLY
   - What exactly is being asserted?
   - Remove ambiguity and vagueness
   - Define all key terms

   Vague: "Exercise is good for you"
   Clear: "30 minutes of moderate aerobic exercise 3x/week
           reduces risk of cardiovascular disease"

2. IDENTIFY THE CLAIM TYPE

   Existential claims:
   - "X exists" or "There is an X"
   - Hard to falsify (can always say "not found yet")

   Universal claims:
   - "All X are Y" or "X always causes Y"
   - Falsifiable by one counterexample

   Statistical claims:
   - "X is associated with Y" or "X increases probability of Y"
   - Requires statistical evidence

   Causal claims:
   - "X causes Y"
   - Requires controlled comparison

3. SPECIFY SCOPE CONDITIONS
   - Under what conditions does the claim hold?
   - What are the boundary conditions?
   - What is the domain of application?

4. IDENTIFY COMPETING CLAIMS
   - What alternative explanations exist?
   - What would be true if this claim is false?
   - Are there multiple competing hypotheses?

5. ASSESS BACKGROUND PLAUSIBILITY
   - How well does this fit with established knowledge?
   - What theory supports or contradicts it?
   - What is your initial credence before testing?

### Step 2: Formulate testable hypotheses
Transform the claim into testable hypotheses:

1. STATE THE RESEARCH HYPOTHESIS (H1)

   Good hypotheses are:
   - Specific: Precise enough to test
   - Falsifiable: Could be proven wrong
   - Grounded: Based on theory or prior evidence
   - Predictive: Make specific predictions

   Format: "If [condition], then [prediction]"

2. STATE THE NULL HYPOTHESIS (H0)

   - The hypothesis of no effect, no difference, no relationship
   - What you would expect if the research hypothesis is false
   - Usually: "There is no difference/relationship/effect"

   Purpose: Provides a default to test against

3. STATE ALTERNATIVE HYPOTHESES

   - Other explanations for expected results
   - Competing theories that make different predictions
   - Important for distinguishing between explanations

4. DERIVE SPECIFIC PREDICTIONS

   From each hypothesis, derive:
   - Observable predictions: What should we see?
   - Quantitative predictions: How much/how large?
   - Conditions: Under what circumstances?

   More specific predictions = more informative tests

5. SPECIFY FALSIFICATION CRITERIA

   - What evidence would falsify H1?
   - What results would support H0?
   - Be concrete: "H1 would be falsified if..."

   Karl Popper's criterion: If nothing could prove it wrong,
   it's not scientific.

EXAMPLE:

Claim: "Mindfulness meditation reduces anxiety"

H1: Participants completing 8-week mindfulness program will show
    lower anxiety scores than waitlist control

H0: No difference in anxiety between groups

Alternative: Attention placebo explains any effect

Predictions:
- Mindfulness group: 5+ point reduction on GAD-7
- Control group: No significant change
- Effect persists at 3-month follow-up

Falsification: Would reject H1 if mindfulness group shows no
improvement or performs worse than control

### Step 3: Assess prior probability
Estimate the prior probability of the hypothesis:

1. CONSIDER BASE RATES
   - How often are similar claims true?
   - What is the prior success rate in this field?
   - Novel claims in low-reliability fields: lower priors

2. CONSIDER THEORETICAL SUPPORT
   - Is there a plausible mechanism?
   - Does it fit with established theory?
   - Strong mechanism + good theory = higher prior

3. CONSIDER PRIOR EVIDENCE
   - What previous studies suggest?
   - What is the consensus view?
   - Strong prior evidence = higher prior

4. CONSIDER EXTRAORDINARY CLAIMS
   - Extraordinary claims require extraordinary evidence
   - Claims that contradict well-established facts need very
     strong evidence to overturn
   - ESP, perpetual motion, etc.: very low priors

5. ASSIGN A PRIOR PROBABILITY

   Be explicit:
   - Point estimate: "I estimate P(H1) = 30%"
   - Range: "I estimate P(H1) between 20-40%"
   - Calibration: Check against known frequencies

   Priors should be:
   - Honest: Reflect genuine uncertainty
   - Defensible: Can explain reasoning
   - Not extreme: Avoid 0% or 100% (unfalsifiable)

6. CONSIDER SENSITIVITY TO PRIORS
   - How much does conclusion depend on prior?
   - Would different reasonable priors change conclusion?
   - Report sensitivity analysis

CALIBRATION GUIDELINES:
- 50%: Coin flip, genuinely uncertain
- 75%: Think it's probably true, would bet modest amount
- 90%: Quite confident, would be surprised if wrong
- 99%: Very strong belief, extraordinary evidence to change

Note: This is pre-experimental probability, before your test.

### Step 4: Design a severe test
Design a test that could actually falsify the hypothesis:

1. SEVERITY PRINCIPLE

   A test is severe if:
   - It has a good chance of revealing the hypothesis is false
     IF it actually is false
   - Passing the test provides strong evidence

   Weak tests: Would pass whether hypothesis true or false
   Strong tests: Would fail if hypothesis is false

2. INCREASE SEVERITY BY:

   High-risk predictions:
   - Predict specific outcomes, not vague trends
   - Predict surprising outcomes (if true)
   - Predict precise quantities

   Example:
   Weak: "Treatment will help some people"
   Severe: "Treatment will produce 10-point improvement
            in 60% of participants within 4 weeks"

   Good methodology:
   - Controls for alternative explanations
   - Adequate sample size for power
   - Reliable and valid measures
   - Blinding where possible

   Multiple tests:
   - Test different predictions from same hypothesis
   - Converging evidence from different methods
   - Replication across contexts

3. CHOOSE ALPHA LEVEL AND POWER

   Alpha (Type I error rate):
   - Conventional: 0.05
   - Stricter for extraordinary claims: 0.01 or 0.001

   Power (1 - Type II error rate):
   - Minimum: 0.80
   - Better: 0.90 or higher
   - Higher power = more severe test

4. SPECIFY DECISION RULE

   Before seeing results, specify:
   - What would count as support for H1?
   - What would count as support for H0?
   - What would be inconclusive?

   Example:
   - Support H1: p < .05 with d > 0.3
   - Support H0: p > .10 with d < 0.2
   - Inconclusive: Otherwise

5. PRE-REGISTER

   Commit to analysis plan before data collection:
   - Prevents p-hacking and HARKing
   - Distinguishes confirmatory from exploratory
   - Increases credibility of findings

### Step 5: Evaluate the evidence
Assess the strength of evidence from the test:

1. CLASSICAL HYPOTHESIS TESTING

   P-value interpretation:
   - P(data or more extreme | H0 is true)
   - Small p: Data unlikely under H0
   - Does NOT give probability H1 is true

   Standard thresholds (arbitrary conventions):
   - p < .05: "Statistically significant"
   - p < .01: "Highly significant"
   - p < .001: "Very highly significant"

   Effect size:
   - How large is the effect?
   - Cohen's d, r, odds ratio, etc.
   - Practical vs. statistical significance

2. BAYESIAN UPDATING

   Bayes' theorem:
   P(H|D) = P(D|H) × P(H) / P(D)

   Components:
   - P(H): Prior probability of hypothesis
   - P(D|H): Likelihood of data given hypothesis
   - P(D): Probability of data (normalizing constant)
   - P(H|D): Posterior probability after seeing data

   Bayes factor:
   - BF = P(D|H1) / P(D|H0)
   - How much more likely is data under H1 vs H0?
   - BF > 3: Substantial evidence for H1
   - BF > 10: Strong evidence for H1
   - BF > 100: Decisive evidence for H1

3. ASSESS EVIDENCE QUALITY

   Was the test actually severe?
   - Did methodology match plan?
   - Were there unexpected issues?
   - How many researcher degrees of freedom?

   Internal validity:
   - Are alternative explanations ruled out?
   - Were controls adequate?

   External validity:
   - Does this generalize?
   - Are there boundary conditions?

4. COMPARE TO PREDICTIONS

   Exactly as predicted: Strong support
   Partially as predicted: Moderate support
   Opposite of predicted: Strong disconfirmation
   Null result: Depends on power

   Note: High-powered null results are informative

### Step 6: Update beliefs appropriately
Revise probability estimates based on evidence:

1. CALCULATE POSTERIOR PROBABILITY

   Using Bayes' theorem:

   Posterior odds = Prior odds × Bayes factor

   Example:
   - Prior: P(H1) = 30% → Prior odds = 30/70 = 0.43
   - Bayes factor: 5 (evidence 5x more likely under H1)
   - Posterior odds: 0.43 × 5 = 2.14
   - Posterior: P(H1) = 2.14/(1+2.14) = 68%

   Strong evidence moves beliefs substantially
   Weak evidence moves beliefs modestly

2. CONSIDER REPLICATION

   Single study provides limited evidence:
   - Effect may not replicate
   - Publication bias inflates effects
   - Wait for replication before high confidence

   Rules of thumb:
   - One study: Tentative conclusion
   - Multiple replications: Stronger confidence
   - Failed replications: Reduce confidence

3. AVOID BELIEF UPDATING ERRORS

   Base rate neglect:
   - Don't ignore prior probability
   - A positive test doesn't mean condition is likely
     if condition is rare

   Confirmation bias:
   - Update symmetrically for confirming/disconfirming evidence
   - Disconfirming evidence should reduce belief

   Anchoring:
   - Don't under-update based on strong evidence
   - Allow beliefs to change substantially

   Motivated reasoning:
   - Don't give favorable evidence more weight
   - Apply same standards to all evidence

4. DOCUMENT BELIEF CHANGE

   Record:
   - Prior probability
   - Evidence summary
   - Posterior probability
   - Reasoning for update

   Be willing to say:
   - "I was wrong"
   - "The evidence changed my mind"
   - "I'm now more/less confident"

5. IDENTIFY REMAINING UNCERTAINTY

   What would further increase/decrease confidence?
   What additional evidence is needed?
   What are the key remaining uncertainties?

### Step 7: Draw conclusions and decide
Formulate appropriate conclusions and next steps:

1. STATE THE CONCLUSION

   Based on posterior probability:
   - Strong support (>90%): "Evidence strongly supports H1"
   - Moderate support (70-90%): "Evidence supports H1"
   - Uncertain (40-70%): "Evidence is inconclusive"
   - Moderate against (10-40%): "Evidence does not support H1"
   - Strong against (<10%): "Evidence strongly refutes H1"

   Be appropriately hedged:
   - Acknowledge uncertainty
   - Note limitations
   - Specify conditions

2. DISTINGUISH TYPES OF CONCLUSIONS

   Epistemic conclusions (about knowledge):
   - "We have evidence that X"
   - "X is more/less likely than we thought"

   Practical conclusions (about action):
   - "We should act as if X"
   - "More research is needed before acting"

   Evidence can be insufficient for knowledge
   but sufficient for practical decision

3. CONSIDER IMPLICATIONS

   If hypothesis is supported:
   - What does this mean for theory?
   - What practical applications follow?
   - What should we investigate next?

   If hypothesis is refuted:
   - What alternative explanations remain?
   - What should we conclude instead?
   - Was the hypothesis worth testing?

   If inconclusive:
   - What would resolve uncertainty?
   - Is more powerful test possible?
   - Should we suspend judgment?

4. SPECIFY NEXT STEPS

   Additional research:
   - Replication needed?
   - Extension to new conditions?
   - Address limitations?

   Practical actions:
   - What decisions follow?
   - What should change based on this evidence?

   Theory development:
   - How should theory be revised?
   - What new hypotheses emerge?

5. DOCUMENT FOR FUTURE REFERENCE

   Create record:
   - Hypothesis and predictions
   - Test conducted
   - Results obtained
   - Conclusions drawn
   - Next steps identified

   Enable cumulative knowledge building


## When to Use
- Developing research hypotheses from theory or observation
- Designing tests of specific claims or predictions
- Deciding between competing explanations
- Evaluating evidence for or against a claim
- Updating probability estimates based on new evidence
- Making decisions under uncertainty
- Evaluating scientific or pseudoscientific claims

## Verification
- [ ] Context assessed and appropriate variant selected
- [ ] Hypothesis is specific, testable, and falsifiable
- [ ] Prior probability is explicit and justified
- [ ] Test is severe enough to potentially falsify hypothesis
- [ ] Evidence evaluated using appropriate statistical methods
- [ ] Belief updating follows from evidence appropriately
- [ ] Conclusion is appropriately hedged given evidence strength
- [ ] Predictions logged for future calibration (→ /emv)

---

## Niche Documentation

### Where This Skill Works Best
- Claims that CAN be tested empirically
- Situations where evidence CAN change beliefs
- Decisions where being wrong has significant consequences
- Scientific or quasi-scientific claims
- Situations with time to design and run tests

### Where This Skill Struggles
- Unfalsifiable claims (use /qaf instead)
- Time-critical decisions (use HT-Lite or skip to action)
- Low-stakes reversible decisions (just try it)
- Pure value judgments (no empirical test possible)
- Situations where test cost exceeds action cost

### Integration Points
- Invokes: /emv (for prediction logging)
- Related: /assumption_verification, /exd
- Routes to: /dct (if multiple hypotheses), /vbo