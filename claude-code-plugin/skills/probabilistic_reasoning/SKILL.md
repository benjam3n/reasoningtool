---
name: probabilistic_reasoning
description: "Systematic procedure for estimating probabilities, updating beliefs with evidence, and making well-calibrated predictions"
---

# Probabilistic Reasoning

## Overview
Systematic procedure for estimating probabilities, updating beliefs with evidence, and making well-calibrated predictions

## Steps

### Step 1: Clarify the hypothesis
Make the uncertain proposition precise and verifiable:
1. State exactly what you're estimating probability of
2. Specify the time frame and conditions
3. Define how you would know if it happened
4. Ensure it's a specific outcome, not a vague concept

### Step 2: Establish the base rate (outside view)
Find the relevant base rate to anchor your estimate:
1. Identify 2-3 relevant reference classes
2. Find data on historical frequencies for each
3. Assess relevance of each reference class to current case
4. Compute weighted average as starting estimate
5. If no data, estimate from first principles

### Step 3: List specific evidence and factors
Identify what makes this case different from the base rate:
1. List all relevant evidence bearing on hypothesis
2. Categorize as supporting, opposing, or neutral
3. Note evidence quality and reliability
4. Identify missing evidence that would be informative
5. Watch for evidence that seems compelling but isn't diagnostic

### Step 4: Assess diagnosticity of evidence
Determine how much each piece of evidence should update the estimate:
1. For each evidence item, ask: "How likely is this evidence if hypothesis is TRUE?"
2. Then ask: "How likely is this evidence if hypothesis is FALSE?"
3. Calculate or estimate likelihood ratio (LR)
4. Note that evidence expected under both hypotheses has LR near 1 (not diagnostic)
5. Be especially careful with confirming evidence that's also expected under alternatives

### Step 5: Update from base rate
Combine base rate with evidence to form posterior estimate:
1. Convert base rate to odds
2. Apply likelihood ratios (multiply for independent evidence)
3. Be conservative about independence (correlations reduce update)
4. Convert back to probability
5. Sanity check: does result seem plausible?

### Step 6: Consider alternative hypotheses
Ensure you're not anchored on a single explanation:
1. Generate alternative hypotheses that could explain the evidence
2. Estimate prior probability of each alternative
3. Check if your evidence distinguishes between alternatives
4. Adjust if evidence is better explained by alternative
5. Allocate probability across hypotheses (should sum to 1)

### Step 7: Calibrate and reality check
Adjust for known biases and check calibration:
1. Ask: "Would I be comfortable betting at these odds?"
2. Consider: "Am I overconfident? Underconfident?"
3. Reference your past calibration record if available
4. Apply specific debiasing for known issues (planning fallacy, etc.)
5. Widen confidence interval if highly uncertain

### Step 8: Document and plan to track
Record the estimate and plan for verification:
1. Write down the precise prediction with probability
2. Note key assumptions and cruxes
3. Identify what would make you update significantly
4. Set date to check outcome
5. Plan to log for calibration tracking


## When to Use
- Estimating likelihood of uncertain future events
- Updating beliefs based on new evidence or information
- Making predictions that will be scored for accuracy
- Combining multiple sources of evidence into a judgment
- Diagnosing problems with uncertain causes
- Evaluating whether a pattern is signal or noise
- Assessing credibility of claims or hypotheses
- Making decisions that depend on probability estimates

## Verification
- Base rate established from relevant reference class
- Evidence assessed for diagnosticity, not just availability
- Likelihood ratios estimated for key evidence
- Update magnitude appropriate for evidence strength
- Alternative hypotheses genuinely considered
- Known biases explicitly addressed
- Prediction recorded for future calibration tracking

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.