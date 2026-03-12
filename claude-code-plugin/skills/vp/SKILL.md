---
name: "vp - Verification and Testing Procedures"
description: "Systematic testing and verification that systems, plans, or deliverables meet their requirements."
output:
  format: "prose"
---

# Verification and Testing Procedures

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Software/system verification**: The user has a software system or technical deliverable and wants to verify it meets requirements through structured testing.
**Interpretation 2 — Plan/process verification**: The user has a plan, process, or workflow and wants to verify it would achieve its objectives.
**Interpretation 3 — Requirements traceability**: The user has requirements and a deliverable and wants to verify complete coverage — every requirement is addressed.

If ambiguous, ask: "Are you verifying a technical system, a plan/process, or checking requirements coverage?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Verification and validation are different.** Verification asks: "Did we build the thing right?" (does it meet spec). Validation asks: "Did we build the right thing?" (does it meet need). This procedure covers both, but distinguishes them.

2. **Pass/fail criteria before testing.** Define what "pass" looks like BEFORE running tests. Post-hoc criteria are rationalization, not verification. If you can't state pass/fail criteria, the requirement isn't testable.

3. **Don't fix during testing.** Testing and fixing are separate activities. When a test fails, document the failure and move on. Fixing during testing contaminates the test run and hides the true failure rate.

4. **Coverage gaps are findings.** Untested requirements aren't "not yet verified" — they're risks. Explicitly identify what wasn't tested and why.

5. **Failed tests need root cause analysis.** A failed test could mean the system is wrong, the test is wrong, or the requirement is wrong. Determine which before declaring failure.

6. **The most dangerous test is the one not written.** Obvious tests get written. Edge cases, failure modes, and interactions between components are where real bugs hide. Actively design tests for what might be missed.

---

## Procedure

### Phase 1: Define Test Objectives

```
TEST SCOPE:
Subject: [what is being tested]
Type: verification / validation / both
Requirements source: [where requirements come from]
Total requirements: [N]
Test levels: [unit / integration / system / acceptance]
```

For each requirement:
1. State the requirement clearly
2. Classify as: functional / performance / reliability / usability / security
3. Determine test method: analysis / inspection / demonstration / test
4. Define pass/fail criteria explicitly

### Phase 2: Design Test Plan

For each requirement, design a test:

```
TEST CASE: TC-[N]
REQUIREMENT: [requirement ID and text]
METHOD: [analysis / inspection / demonstration / test]
PROCEDURE:
1. [Setup step]
2. [Action step]
3. [Observation step]
EXPECTED RESULT: [what constitutes pass]
TEST DATA: [inputs, including edge cases]
ENVIRONMENT: [what setup is needed]
PRIORITY: [P1 critical / P2 important / P3 nice-to-have]
```

**Test design considerations:**
- **Happy path**: Does it work under normal conditions?
- **Edge cases**: Boundary values, empty inputs, maximum loads
- **Error cases**: Invalid inputs, failure modes, recovery
- **Interactions**: Components that affect each other
- **Regression**: Could changes break existing functionality?

### Phase 3: Execute Tests

For each test case (P1 first):
1. Set up the test environment
2. Execute per procedure
3. Record actual result
4. Determine: PASS / FAIL / BLOCKED / SKIPPED
5. If FAIL: document expected vs actual clearly
6. Do NOT fix during testing — record and continue

```
TEST EXECUTION LOG:

| TC | Requirement | Expected | Actual | Status | Notes |
|----|------------|----------|--------|--------|-------|
| TC-1 | [req] | [expected] | [actual] | PASS/FAIL/BLOCKED | [notes] |
```

### Phase 4: Analyze Results

```
RESULTS ANALYSIS:

Pass rate: [passed] / [total] = [%]
Coverage: [tested] / [total requirements] = [%]

FAILURES:
| TC | Requirement | Root Cause | Severity | Fix Needed |
|----|------------|------------|----------|-----------|
| TC-[N] | [req] | system / test / requirement | H/M/L | [action] |

BLOCKED:
[Tests that couldn't run and why]

COVERAGE GAPS:
[Requirements without test cases and why]

REGRESSION RISK:
[Areas where fixes could break other things]
```

### Phase 5: Report

```
VERIFICATION REPORT
Subject: [what was tested]
Date: [date]
Type: [verification / validation / both]

SUMMARY:
Total requirements: [N]
Tested: [N] | Passed: [N] | Failed: [N] | Blocked: [N] | Skipped: [N]
Coverage: [%]

CRITICAL FAILURES (P1):
1. [requirement] — Expected: [X] — Actual: [Y] — Root cause: [cause]

OTHER FAILURES:
[P2 and P3 failures]

COVERAGE GAPS:
[Untested areas]

REGRESSION RISKS:
[What might break during fixing]

VERDICT: [release / fix critical and retest / major rework needed]

RECOMMENDED ACTIONS:
1. [Specific action with priority]
2. [Specific action with priority]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Post-hoc criteria** | Pass/fail decided after seeing results | Define criteria BEFORE testing — always |
| **Fix-during-test** | Issues fixed mid-test-run, inflating pass rate | Separate testing and fixing into distinct phases |
| **Missing edge cases** | Only happy-path tested | Explicitly design for boundaries, errors, and interactions |
| **Untraceable failures** | "It failed" without expected vs actual | Every failure must state what was expected and what happened |
| **Coverage illusion** | "All tests pass" but 40% of requirements untested | Track coverage as tested/total-requirements, not passed/total-tests |
| **Wrong root cause** | System blamed when the test was wrong | Analyze failures — is it the system, the test, or the requirement? |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Quick check — test P1 requirements only | P1 tests run, critical failures identified |
| **2x** | Standard — P1 and P2 tested, coverage calculated | Full test run, failure analysis, coverage report |
| **4x** | Thorough — all levels tested, edge cases, regression analysis | Complete test suite, root cause analysis, regression risk map |
| **8x** | Exhaustive — full V&V, interaction testing, failure mode testing, traceability matrix | Complete verification and validation with traceability to every requirement |

---

## Pre-Completion Checklist

- [ ] All requirements have test cases (or are explicitly noted as untestable)
- [ ] Pass/fail criteria defined BEFORE testing
- [ ] Tests executed and results recorded
- [ ] Failures have root cause analysis (system / test / requirement)
- [ ] Coverage gaps explicitly identified
- [ ] Regression risks noted
- [ ] Verdict stated with recommended actions
- [ ] P1 failures have specific fix recommendations

---

## Integration

- **Use from**: /evaluate (when evaluation requires formal verification), /how (when method needs testing before commitment), /de (when execution plan needs verification checkpoints)
- **Routes to**: /rca (root cause analysis for failures), /fla (failure anticipation for untested areas), /diagnose (when failures have unclear causes)
- **Differs from**: /val (validation checks against requirements, /vp is the full testing procedure), /ver (GOSM verification for individual claims, /vp for system-level testing), /evaluate (evaluation is assessment, /vp is structured testing)
- **Complementary**: /av (verify assumptions before testing), /fla (anticipate failures to design better tests), /mv (MECE-check the test plan for completeness)
