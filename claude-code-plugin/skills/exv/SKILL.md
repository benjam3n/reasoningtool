---
name: exv
description: "Systematic procedure for calculating expected value, adjusting for risk, and determining optimal resource allocation under uncertainty"
---

# Expected Value Analysis

## Overview
Systematic procedure for calculating expected value, adjusting for risk, and determining optimal resource allocation under uncertainty

## Steps

### Step 1: Define the decision and options
Clearly specify what you're deciding and available alternatives:
1. State the decision question
2. List all available options (including do nothing)
3. Ensure options are mutually exclusive
4. Identify any constraints on choices

### Step 2: Map outcomes for each option
Identify all possible outcomes for each option:
1. For each option, list what could happen
2. Ensure outcomes are exhaustive (cover all possibilities)
3. Make outcomes mutually exclusive
4. Include best case, worst case, and likely scenarios

### Step 3: Assign probabilities
Estimate probability for each outcome:
1. Use available data where possible
2. Apply base rates and reference classes
3. Adjust for case-specific factors
4. Verify probabilities sum to 1.0 for each option
5. Document uncertainty in estimates

### Step 4: Assign values to outcomes
Determine the value (gain or loss) of each outcome:
1. Calculate monetary value where applicable
2. Include all costs and benefits in each outcome
3. Account for time value of money if relevant
4. For non-monetary outcomes, assign utility scores
5. Be consistent in units across all options

### Step 5: Calculate expected value
Compute EV for each option:
1. For each option: EV = sum(probability x value) across outcomes
2. Subtract any fixed costs from EV
3. Rank options by expected value
4. Calculate variance for each option
5. Note the margin between top options

### Step 6: Assess risk and downside
Evaluate the risk profile of each option:
1. Identify worst-case outcome for each option
2. Calculate probability of loss or negative outcomes
3. Assess whether you can afford the worst case
4. Consider correlation with existing risks
5. Evaluate whether EV-maximizing is appropriate here

### Step 7: Apply risk adjustment if needed
Adjust for risk if pure EV is inappropriate:
1. If risk-averse, calculate certainty equivalents
2. For investment sizing, apply Kelly criterion
3. Consider fractional Kelly for conservative approach
4. Adjust for correlation with other risks
5. Compute risk-adjusted recommendation

### Step 8: Make recommendation
Synthesize analysis into a clear recommendation:
1. State the recommended option
2. Report EV and risk-adjusted value
3. Specify recommended sizing/commitment level
4. Note key assumptions and sensitivities
5. Describe what would change the recommendation


## When to Use
- Comparing options with different probabilities and payoffs
- Determining whether a bet or investment is favorable
- Calculating fair prices for uncertain outcomes
- Deciding how much to stake on favorable opportunities
- Evaluating insurance, hedging, or risk mitigation
- When you can make similar decisions repeatedly (EV dominates)
- Justifying resource allocation under uncertainty

## Verification
- All outcomes identified with probabilities summing to 1.0
- Expected value correctly calculated for each option
- Costs included in outcome values
- Variance calculated to understand risk
- Kelly criterion applied appropriately for sizing
- Risk tolerance considered in recommendation
- Downside explicitly evaluated for survivability

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.