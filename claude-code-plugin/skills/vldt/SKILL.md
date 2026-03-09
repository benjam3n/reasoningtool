---
name: "vldt - Validate"
description: Systematic validation procedure. Defines criteria, runs checks, flags failures, and makes a pass/fail determination with reasoning.
---

# Validate

**Input**: $ARGUMENTS

---

## Step 1: State What's Being Validated

```
SUBJECT: [What is being validated — a claim, plan, output, design, code, etc.]
VALIDATION GOAL: [What "valid" means in this context]
STAKES: [What happens if this passes but shouldn't / fails but shouldn't]
```

---

## Step 2: Define Validation Criteria

List every criterion that must be met. Be specific and testable.

```
CRITERIA:
1. [Criterion] — test: [how to check it]
2. [Criterion] — test: [how to check it]
3. [Criterion] — test: [how to check it]
4. [Criterion] — test: [how to check it]
5. [Criterion] — test: [how to check it]
```

For each criterion, it must be clear what a pass looks like and what a fail looks like.

---

## Step 3: Run Each Check

Execute each validation test.

```
CHECK RESULTS:

1. [Criterion]: PASS / FAIL
   Evidence: [what was found]

2. [Criterion]: PASS / FAIL
   Evidence: [what was found]

3. [Criterion]: PASS / FAIL
   Evidence: [what was found]

4. [Criterion]: PASS / FAIL
   Evidence: [what was found]

5. [Criterion]: PASS / FAIL
   Evidence: [what was found]
```

---

## Step 4: Flag and Classify Failures

```
FAILURES FOUND: [count]

CRITICAL FAILURES (must fix — blocks validity):
- [Criterion X]: [why it's critical]

MINOR FAILURES (should fix — doesn't block validity):
- [Criterion Y]: [why it's minor]

WARNINGS (not a failure but worth noting):
- [Observation]: [why it matters]
```

If there are no failures, state that clearly and move to Step 5.

---

## Step 5: Determination

```
VERDICT: PASS / CONDITIONAL PASS / FAIL

REASONING: [1-3 sentences explaining the determination]

IF CONDITIONAL:
- Must fix before proceeding: [list]
- Can fix later: [list]

IF FAIL:
- Root cause: [the fundamental issue]
- To re-validate after fixing: [what to change and re-test]
```

---

## Step 6: Validation Summary

```
VALIDATED: [subject]
RESULT: [PASS / CONDITIONAL / FAIL]
CRITICAL ISSUES: [count]
MINOR ISSUES: [count]
CONFIDENCE: [How confident are you in this validation: high/medium/low]
CONFIDENCE CAVEAT: [What could you have missed]
```

---

## Integration

Use with:
- `/plsk` -> Validate a plan specifically
- `/prsk` -> Validate a product specifically
- `/thnk` -> Choose the right validation approach
- `/bldk` -> Validate at each build stage
