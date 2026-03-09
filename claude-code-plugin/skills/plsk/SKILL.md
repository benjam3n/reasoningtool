---
name: "plsk - Plans"
description: Procedure for evaluating and improving plans. Checks if steps lead to goal, identifies missing or unnecessary steps, assesses sequencing and resources, and suggests improvements.
---

# Plans

**Input**: $ARGUMENTS

---

## Step 1: State the Plan's Goal

```
PLAN GOAL: [What the plan is supposed to achieve]
SUCCESS CRITERIA: [How you'd know the plan worked]
TIMEFRAME: [When the plan should be complete]
```

If the plan doesn't have a clear goal, flag this immediately — a plan without a goal can't be evaluated.

---

## Step 2: List the Steps

Extract or enumerate every step in the plan.

```
STEPS:
1. [Step]
2. [Step]
3. [Step]
4. [Step]
5. [Step]
...
```

---

## Step 3: Check Goal Alignment

For each step, does it actually lead toward the goal?

```
STEP AUDIT:
1. [Step] -> Leads to goal? [yes / partially / no] — [why]
2. [Step] -> Leads to goal? [yes / partially / no] — [why]
3. [Step] -> Leads to goal? [yes / partially / no] — [why]
...

STEPS THAT DON'T LEAD TO GOAL:
- [Step X]: [why it's off-track or unnecessary]
```

---

## Step 4: Find Missing Steps

```
MISSING STEPS:
- Before step [N]: need [missing step] because [reason]
- Between steps [N] and [M]: need [missing step] because [reason]
- After final step: need [missing step] because [reason]

ASSUMPTIONS NOT STATED:
- The plan assumes [assumption] — if wrong: [consequence]
- The plan assumes [assumption] — if wrong: [consequence]
```

---

## Step 5: Check Sequencing and Resources

```
SEQUENCING ISSUES:
- [Step X] should come before [Step Y] because [dependency]
- [Steps A and B] could run in parallel to save time

RESOURCE REQUIREMENTS:
- [Step]: needs [resource] — available? [yes/no]
- [Step]: needs [resource] — available? [yes/no]

WEAKEST STEP: [The step most likely to fail or cause delays]
WHY IT'S WEAKEST: [reason]
```

---

## Step 6: Improved Plan

```
IMPROVED PLAN:
1. [Step — with fixes applied]
2. [Step — with fixes applied]
3. [New step if needed]
4. [Step — resequenced if needed]
...

KEY CHANGES:
- [What was added and why]
- [What was removed and why]
- [What was reordered and why]

PLAN STRENGTH AFTER IMPROVEMENTS: [Weak / Moderate / Strong]
REMAINING RISK: [The biggest thing that could still go wrong]
```

---

## Integration

Use with:
- `/vldt` -> Validate the improved plan against criteria
- `/bldk` -> Execute the plan by building incrementally
- `/tmsk` -> Assess whether the team can execute the plan
- `/indv` -> Check if the plan works for the individual executing it
