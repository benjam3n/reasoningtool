---
name: pv
description: Validate that a procedure is complete, executable, and all dependencies are satisfiable. Catches issues before execution.
---

# Procedure Validation

**Input**: $ARGUMENTS

---

## Purpose

Before executing a procedure, validate that:
1. All dependencies can be satisfied
2. No cycles exist
3. All required inputs are available
4. No steps are missing
5. The procedure achieves its goal

This catches issues before wasted effort.

---

## Validation Dimensions

| Dimension | Question | Failure Mode |
|-----------|----------|--------------|
| **Completeness** | Are all necessary steps included? | Missing steps |
| **Ordering** | Is the sequence valid? | Dependency violations |
| **Feasibility** | Can each step actually be done? | Impossible steps |
| **Inputs** | Are all required inputs available? | Missing prerequisites |
| **Outputs** | Does the procedure produce the goal? | Wrong outcome |
| **Consistency** | Do steps align with each other? | Contradictions |

---

## The Validation Process

### Step 1: State the Procedure

```
PROCEDURE TO VALIDATE: [name]

GOAL: [what this procedure should achieve]

STEPS:
1. [Step 1]
2. [Step 2]
3. [Step 3]
...
N. [Step N]

DECLARED DEPENDENCIES:
- Step 2 depends on Step 1
- Step 3 depends on Step 2
...

EXTERNAL INPUTS REQUIRED:
- [Input 1]: [source]
- [Input 2]: [source]
```

---

### Step 2: Completeness Check

Verify no steps are missing:

```
COMPLETENESS CHECK:

Goal decomposition:
To achieve [goal], we need:
[ ] [Sub-goal A]
[ ] [Sub-goal B]
[ ] [Sub-goal C]

Step coverage:
- Sub-goal A: Covered by [Step X] [x]
- Sub-goal B: Covered by [Step Y] [x]
- Sub-goal C: NOT COVERED [!]

GAPS FOUND:
- [Sub-goal C] has no corresponding step
  -> Add step: [proposed step]

GAP CHECK: [All covered / Gaps found]
```

---

### Step 3: Dependency Validation

Verify ordering respects dependencies:

```
DEPENDENCY VALIDATION:

For each step, check: Are its dependencies satisfied by earlier steps?

| Step | Dependencies | Earlier Steps | Valid? |
|------|--------------|---------------|--------|
| Step 1 | None | N/A | [x] |
| Step 2 | Step 1 | Step 1 | [x] |
| Step 3 | Step 2 | Steps 1, 2 | [x] |
| Step 4 | Step 5 | Steps 1, 2, 3 | [!] Step 5 not yet done |

ORDERING ERRORS:
- Step 4 requires Step 5, but Step 5 comes after Step 4
  -> Reorder: Move Step 5 before Step 4

CYCLE CHECK:
- Tracing dependencies... No cycles found [x]

DEPENDENCY CHECK: [Valid / Errors found]
```

---

### Step 4: Feasibility Check

Verify each step can actually be executed:

```
FEASIBILITY CHECK:

For each step, ask: Can this actually be done?

| Step | Feasibility | Issues |
|------|-------------|--------|
| Step 1 | [x] Feasible | None |
| Step 2 | [x] Feasible | None |
| Step 3 | [!] Conditional | Requires external approval |
| Step 4 | [!] Infeasible | Technology doesn't exist |

FEASIBILITY ISSUES:
- Step 3: External approval needed
  -> Mitigation: Add approval request step before
  -> Contingency: Define alternative if not approved

- Step 4: Technology doesn't exist
  -> Resolution: Replace with achievable alternative
  -> Or: Remove step, adjust goal

FEASIBILITY CHECK: [All feasible / Issues found]
```

---

### Step 5: Input Availability Check

Verify all required inputs exist or can be obtained:

```
INPUT AVAILABILITY CHECK:

Required inputs for procedure:
| Input | Needed By | Source | Available? |
|-------|-----------|--------|------------|
| [Input A] | Step 1 | [source] | [x] Available |
| [Input B] | Step 3 | [source] | [!] Need to request |
| [Input C] | Step 5 | Produced by Step 2 | [x] Internal |
| [Input D] | Step 6 | Unknown | [!] Source unclear |

INPUT ISSUES:
- Input B: Need to request from [source]
  -> Add step: "Request Input B from [source]"
  -> Add wait: Allow time for response

- Input D: Source unclear
  -> Resolution: Identify source
  -> Or: Determine if input is actually necessary

INPUT CHECK: [All available / Issues found]
```

---

### Step 6: Output Verification

Verify the procedure produces the intended goal:

```
OUTPUT VERIFICATION:

Goal: [stated goal]

Trace outputs:
- Step 1 produces: [output 1]
- Step 2 produces: [output 2]
- ...
- Final step produces: [final output]

Does [final output] = [goal]?

OUTPUT ANALYSIS:
- Final output: [description]
- Goal: [description]
- Match: [Yes / Partial / No]

If Partial or No:
- Gap: [what's missing between output and goal]
- Resolution: [additional steps needed]

OUTPUT CHECK: [Goal achieved / Gap exists]
```

---

### Step 7: Consistency Check

Verify steps don't contradict each other:

```
CONSISTENCY CHECK:

Scanning for contradictions...

| Step A | Step B | Relationship | Issue? |
|--------|--------|--------------|--------|
| Step 2: "Use Python" | Step 5: "Use Java" | Contradiction | [!] |
| Step 3: "Save to DB" | Step 6: "Read from DB" | Consistent | [x] |

CONTRADICTIONS FOUND:
- Steps 2 and 5 specify different technologies
  -> Resolution: Standardize on one
  -> Or: Clarify they're for different components

CONSISTENCY CHECK: [Consistent / Contradictions found]
```

---

### Step 8: Generate Validation Report

```
===============================================
PROCEDURE VALIDATION REPORT
===============================================

Procedure: [name]
Goal: [goal]
Steps: [N]

VALIDATION RESULTS:

| Dimension | Status | Issues |
|-----------|--------|--------|
| Completeness | [x] / [!] | [count] |
| Dependencies | [x] / [!] | [count] |
| Feasibility | [x] / [!] | [count] |
| Inputs | [x] / [!] | [count] |
| Outputs | [x] / [!] | [count] |
| Consistency | [x] / [!] | [count] |

OVERALL STATUS: [VALID / NEEDS REVISION / INVALID]

===============================================

ISSUES REQUIRING RESOLUTION:

1. [Issue 1]
   Severity: [Critical / Major / Minor]
   Resolution: [proposed fix]

2. [Issue 2]
   Severity: [Critical / Major / Minor]
   Resolution: [proposed fix]

===============================================

RECOMMENDED ACTIONS:

[ ] [Action 1]
[ ] [Action 2]
[ ] [Action 3]

After fixes applied, re-validate procedure.

===============================================
```

---

## Quick Validation (Abbreviated)

For simple procedures:

```
QUICK VALIDATION: [procedure name]

[ ] All steps present for goal? [Y/N]
[ ] Dependencies in correct order? [Y/N]
[ ] All steps feasible? [Y/N]
[ ] All inputs available? [Y/N]
[ ] Final output matches goal? [Y/N]
[ ] No contradictions? [Y/N]

QUICK VERDICT: [VALID / NEEDS WORK]
If NEEDS WORK: [main issue]
```

---

## Example: Validating a Deployment Procedure

### Input Procedure
Goal: Deploy new version to production

Steps:
1. Run tests locally
2. Create PR
3. Merge to main
4. Deploy to staging
5. Run staging tests
6. Deploy to production

### Validation

**Completeness**: [x] Covers test, review, stage, deploy

**Dependencies**:
- Step 3 (merge) should depend on Step 2 (PR) + approval
- Missing: PR approval step
- [!] Issue found

**Feasibility**: [x] All steps are standard practice

**Inputs**:
- Code changes: [x] Available
- Test suite: [x] Available
- Staging environment: [!] Need to verify access

**Outputs**: [x] Production deployment matches goal

**Consistency**: [x] No contradictions

### Report

```
OVERALL STATUS: NEEDS REVISION

Issues:
1. Missing step between 2 and 3: "Get PR approval"
   Severity: Major
   Resolution: Add approval step

2. Staging environment access unverified
   Severity: Minor
   Resolution: Verify access before starting

Revised procedure:
1. Run tests locally
2. Create PR
3. GET PR APPROVAL (added)
4. Merge to main
5. Deploy to staging
6. Run staging tests
7. Deploy to production
```

---

## Quality Checklist

Before completing:
- [ ] Procedure clearly stated
- [ ] Completeness checked against goal
- [ ] Dependencies validated
- [ ] Feasibility verified
- [ ] Inputs confirmed available
- [ ] Outputs traced to goal
- [ ] Consistency checked
- [ ] Report generated
- [ ] Resolutions proposed for all issues

---

## Integration

Use with:
- `/de` -> Get dependencies first
- `/to` -> Generate valid order
- `/pv` -> Validate final procedure (this skill)
