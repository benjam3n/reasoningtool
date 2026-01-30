---
name: pss
description: "There are always multiple ways to achieve a goal."
---

# Plan Space Search

## Overview
There are always multiple ways to achieve a goal.
Instead of committing to the first plan that seems workable:
1. Generate diverse plans
2. Evaluate against comprehensive criteria
3. Select the optimal plan

This avoids local optima and premature commitment.

## Goal
Generate multiple possible plans to achieve a goal,
then search for the one that best satisfies optimization criteria.

## Steps

### Step 1: Define Goal and Constraints
Clearly state:
- What success looks like
- Hard constraints (must satisfy)
- Soft preferences (want to satisfy)
- Available resources

**Output**: Planning brief

### Step 2: Generate Plan via Forward Planning
Start from current state.
What actions lead toward goal?
Build sequence to goal.

**Output**: Forward plan

### Step 3: Generate Plan via Backward Planning
Start from goal state.
What must happen right before?
Work back to current state.

**Output**: Backward plan

### Step 4: Generate Analogical Plans
What similar goals have been achieved?
How were they achieved?
Adapt those plans.

**Output**: Analogical plans

### Step 5: Generate Radical Alternatives
What's a completely different approach?
Challenge assumptions:
- What if we did it in half the time?
- What if we had 10x budget?
- What if we had no budget?
- What if it had to be done by one person?

**Output**: Alternative plans

### Step 6: Validate Constraint Satisfaction
For each plan, check:
- Does it satisfy all hard constraints?
- If not, can it be modified?
- If not modifiable, discard.

**Output**: Valid plans

### Step 7: Estimate Resources
For each valid plan, estimate:
- Time required
- Money required
- People required
- Other resources

**Output**: Resource estimates

### Step 8: Score Each Plan
Score on criteria:
- Achieves goal
- Complete
- Resource efficient
- Time efficient
- Handles uncertainty
- Has fallbacks
- Simple to execute
- Few dependencies
- Exit possible

**Output**: Scored plans

### Step 9: Compare Plans
Create comparison table.
Identify which plan wins on which criteria.
Look for dominant plan.

**Output**: Plan comparison

### Step 10: Sensitivity Analysis
How robust is the ranking?
- What if time was more important?
- What if resources were scarcer?
- What if uncertainty was higher?

**Output**: Sensitivity assessment

### Step 11: Select and Refine
Select top plan.
Can it incorporate strengths from other plans?
Refine the plan with details.

**Output**: Final plan

### Step 12: Document Contingencies
For the selected plan:
- What could go wrong?
- What are the triggers for Plan B?
- What parts of rejected plans serve as fallbacks?

**Output**: Contingency documentation


## When to Use
- Planning a project
- Strategy development
- Resource allocation decisions
- Route/path finding
- Any situation with multiple approaches

## Verification
- Multiple plan generation methods used
- Plans satisfy hard constraints
- Resource estimates are realistic
- Scoring is consistent
- Sensitivity analysis performed
- Contingencies documented

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.