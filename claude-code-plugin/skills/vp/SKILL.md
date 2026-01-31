---
name: "vp - Verification and Testing Procedures"
description: "Systematic testing and verification that systems meet requirements."
---

# Verification and Testing Procedures

**Input**: $ARGUMENTS

---

## Overview

Verification answers: "Did we build the thing right?" Validation answers: "Did we build the right thing?" This procedure covers both through structured test planning, execution, and analysis.

## Steps

### Step 1: Define Test Objectives
1. What requirements need verification?
2. What level of testing? (unit, integration, system, acceptance)
3. What is the pass/fail criteria for each requirement?
4. What are the priorities? (test critical requirements first)

### Step 2: Design Test Plan
For each requirement:
1. Test method: analysis, inspection, demonstration, or test
2. Test procedure: step-by-step instructions
3. Expected result: what constitutes pass
4. Test environment: what setup is needed
5. Test data: what inputs to use (including edge cases)

### Step 3: Execute Tests
1. Set up test environment
2. Execute each test per procedure
3. Record: actual result, pass/fail, any observations
4. If fail: document the failure clearly (expected vs actual)
5. Don't fix during testing — record and continue

### Step 4: Analyze Results
1. How many requirements verified? How many failed?
2. For failures: root cause? Is it the code or the test?
3. Test coverage: are there untested requirements?
4. Regression risk: could fixes break other things?

### Step 5: Report
```
TEST REPORT:
Total requirements: [N]
Tested: [N] | Passed: [N] | Failed: [N] | Blocked: [N]

Failures:
1. [requirement] — Expected: [X] — Actual: [Y] — Severity: [H/M/L]

Coverage gaps: [untested areas]
Recommendation: [release / fix and retest / major issues]
```

## When to Use
- Before releasing software or hardware
- After changes to verify nothing broke
- Acceptance testing with stakeholders

## Verification
- [ ] All requirements have test procedures
- [ ] Pass/fail criteria defined before testing
- [ ] Tests executed and results recorded
- [ ] Failures analyzed for root cause
- [ ] Coverage gaps identified
