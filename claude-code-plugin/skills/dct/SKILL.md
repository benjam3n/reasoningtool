---
name: dct
description: "Systematic procedure for structuring complex decisions with multiple branches, probabilities, and outcomes. Includes empirical validation for probability estimates."
context: fork
---

# Decision Tree Analysis

**Input**: $ARGUMENTS

---

## Overview

Systematic procedure for structuring complex decisions with multiple branches, probabilities, and outcomes.

---

## Step 0: Context Assessment

| Factor | Value | Notes |
|--------|-------|-------|
| Stakes | HIGH / MED / LOW | |
| Probability confidence | HIGH / MED / LOW | How confident are probability estimates? |
| Reversibility | EASY / HARD / IMPOSSIBLE | |

**If LOW probability confidence + HIGH stakes**: Include empirical validation of key probabilities before final decision.

---

## Steps

### Step 1: Define the decision problem
Clearly articulate what decision needs to be made:
1. State the core decision question
2. Identify who is making the decision
3. Determine the time horizon and decision deadline
4. Clarify the objective (maximize profit, minimize cost, etc.)
5. Identify constraints on available options

### Step 2: Identify decision points and options
Map all points where the decision maker must choose:
1. List the initial decision (root node)
2. Identify any subsequent decisions that depend on earlier outcomes
3. For each decision point, list all available options
4. Ensure options are mutually exclusive
5. Include "do nothing" or "wait" where applicable

### Step 3: Identify uncertainty and chance events
Map all points where chance affects outcomes:
1. List key uncertainties that influence results
2. For each uncertainty, define possible outcomes
3. Ensure outcomes at each chance node are exhaustive (cover all possibilities)
4. Determine where in the tree each chance event occurs
5. Identify any dependencies between chance events

### Step 4: Construct the tree structure
Build the decision tree connecting all nodes:
1. Start with root decision node (first choice)
2. Add branches for each option
3. After each branch, add relevant chance nodes or subsequent decisions
4. Continue until all paths reach terminal nodes
5. Review tree for completeness and logical consistency

### Step 5: Assign probabilities to chance events
Estimate probability for each branch at chance nodes:
1. Gather available data on historical frequencies
2. Consult experts for informed estimates
3. Use base rates from similar situations
4. Assign probability to each branch (0 to 1)
5. Verify probabilities sum to 1.0 at each chance node
6. Document rationale and uncertainty in estimates

### Step 6: Assign values to terminal nodes
Determine the payoff or value at each end state:
1. Identify all terminal nodes (end points)
2. Calculate or estimate value for each outcome
3. Use consistent units (dollars, utility points, etc.)
4. Include all relevant costs and benefits in each path
5. Account for time value of money if relevant

### Step 7: Calculate expected values (fold back the tree)
Solve the tree working from terminal nodes back to root:
1. Start at rightmost nodes (terminal values are known)
2. At each chance node: EV = sum(probability x value) for all branches
3. At each decision node: choose option with highest EV
4. Record the optimal choice at each decision node
5. Continue until root node has expected value

### Step 8: Perform sensitivity analysis
Test robustness of optimal strategy to assumptions:
1. Identify probabilities with highest uncertainty
2. Vary each probability within reasonable range
3. Recalculate optimal strategy for each variation
4. Find "crossover points" where optimal decision changes
5. Assess whether crossover points are plausible

### Step 9: Calculate value of information (optional)
Determine if gathering more information is worthwhile:
1. Identify information that could reduce uncertainty
2. Calculate EV with perfect information (EVPI)
3. Calculate EV with imperfect information if applicable
4. Value of information = EV(with info) - EV(without info)
5. Compare to cost of obtaining information

### Step 10: Empirical Validation of Key Probabilities (HIGH stakes)

**When to include**: HIGH stakes + LOW confidence in probability estimates.

Before committing to the optimal strategy:

1. **Identify critical probabilities**:
   - Which probabilities most affect the optimal decision?
   - (From sensitivity analysis: crossover points)
   - These are the ones worth validating

2. **Design probability validation**:
   - Historical data: What base rates exist?
   - Expert elicitation: What do domain experts estimate?
   - Small-scale tests: Can we observe a sample?
   - Reference class forecasting: What happened in similar situations?

3. **Log predictions for calibration**:
   ```
   Probability estimate: [event] has [X]% chance
   Confidence in estimate: HIGH/MED/LOW
   How we'd know: [observation that confirms/disconfirms]
   Review date: [when we'll know]
   ```

→ INVOKE: /emv [critical probability estimates]

4. **Update tree if estimates change significantly**:
   - Recalculate expected values
   - Check if optimal strategy changes
   - Document the update

---

## When to Use
- Decision has multiple sequential stages or phases
- Uncertain events will influence optimal choices
- Need to compare options with different risk-return profiles
- Want to calculate expected value of different strategies
- Stakeholders need visual representation of decision structure
- Decisions depend on outcomes of intermediate chance events
- Evaluating whether to gather information before deciding
- Comparing "act now" vs "wait and see" strategies

## Verification
- [ ] Tree structure is complete with all paths reaching terminal nodes
- [ ] Probabilities sum to 1.0 at each chance node
- [ ] Terminal values are consistently calculated
- [ ] Expected values correctly computed by folding back
- [ ] Sensitivity analysis performed on key probability estimates
- [ ] Optimal strategy clearly identified with decision rule
- [ ] Assumptions and limitations documented
- [ ] If HIGH stakes + LOW confidence: Probability validation completed
- [ ] Key predictions logged for calibration

---

## Integration Points
- Often invoked from: /pce, /cmp
- Routes to: /sel (final choice), /emv (probability validation)
- Related: /exv, /ria, /pbr