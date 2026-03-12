---
name: "oprc - Procedure Generation"
description: Generates step-by-step procedures with dependency ordering, decision points, and failure handling. Takes a goal and produces a complete, testable procedure.
output:
  format: "prose"
---

# Procedure Generation

**Input**: $ARGUMENTS

---

## Step 1: Identify the Goal

State what the procedure accomplishes when followed correctly.

```
GOAL: [what successful completion looks like]
SCOPE: [what the procedure covers / what it does not cover]
PREREQUISITES: [what must be true before starting]
ACTOR: [who performs this procedure]
```

---

## Step 2: List All Steps in Dependency Order

Enumerate every step required to reach the goal. Order by dependency, not by importance.

Rules:
- Each step should be a single action, not a compound task
- If a step contains "and", consider splitting it
- Steps must be in an order where each step's inputs are available from prior steps
- Number steps sequentially

```
STEPS:
1. [action verb] [what] [with what inputs]
2. [action verb] [what] [with what inputs]
3. [action verb] [what] [with what inputs]
...
```

---

## Step 3: Specify Inputs and Outputs

For each step, define what goes in and what comes out. This makes the procedure auditable and debuggable.

```
STEP [N]: [step description]
  INPUT: [what this step needs]
  OUTPUT: [what this step produces]
  DONE WHEN: [how to verify this step succeeded]
```

Rules:
- Every output should be consumed by a later step or be a final deliverable
- Every input should come from a prior step's output or from the prerequisites
- If an input has no source, the procedure has a gap

---

## Step 4: Add Decision Points

Identify where the procedure branches based on conditions.

```
STEP [N]: Check [condition]
  IF [condition A]: proceed to Step [X]
  IF [condition B]: proceed to Step [Y]
  IF [neither]: [what to do — escalate, retry, abort]
```

Rules:
- Decision points must be binary or have a small number of clear branches
- Every branch must eventually rejoin the main flow or reach a defined endpoint
- Include a default/fallback for unexpected conditions

---

## Step 5: Mental Walkthrough

Test the procedure by walking through it with a concrete example.

```
TEST SCENARIO: [a specific realistic case]

WALKTHROUGH:
- Step 1: [what happens with this input]
- Step 2: [what happens next]
- ...
- Result: [what the procedure produces]

ISSUES FOUND:
- [any gaps, ambiguities, or missing steps discovered]
```

Fix any issues found before proceeding.

---

## Step 6: Add Failure Handling

For each step that can fail, define what to do.

| Step | Failure mode | Response |
|------|-------------|----------|
| [N] | [what could go wrong] | [retry / skip / escalate / abort] |
| [N] | [what could go wrong] | [retry / skip / escalate / abort] |

Rules:
- Every step that interacts with external systems needs failure handling
- Define maximum retry counts where applicable
- Identify the point of no return (if any) after which rollback is not possible
- Include a full abort procedure if the process must be abandoned mid-way

---

## Step 7: Deliver

Present the complete procedure with:
- Goal and prerequisites at the top
- Numbered steps with inputs, outputs, and verification criteria
- Decision points clearly marked
- Failure handling included inline or as an appendix
- An estimated time or effort for the full procedure (if applicable)

```
PROCEDURE: [name]
GOAL: [what it accomplishes]
PREREQUISITES: [what must be true before starting]
ESTIMATED EFFORT: [time or effort estimate]

[The complete procedure]
```

---

## Integration

Use with:
- `/de` -> Design the system that the procedure operates within
- `/to` -> Break the procedure into a task outline for execution
- `/oart` -> Package the procedure as a reusable template
- `/pv` -> Validate the procedure against edge cases
