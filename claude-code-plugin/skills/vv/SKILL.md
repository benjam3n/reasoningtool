---
name: "vv - Verification & Validation"
description: Plan and execute verification (built right?) and validation (built the right thing?) activities. Produces a V&V plan with requirements traceability matrix, test cases, and acceptance criteria.
output:
  format: "table"
---

# Verification & Validation

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Create a V&V plan for a system under development**: The user has requirements and a design and wants to plan how every requirement will be verified and how the system will be validated against stakeholder needs.
**Interpretation 2 — Audit existing V&V coverage**: The user has an existing system with some testing and wants to identify gaps in verification coverage and validation completeness.
**Interpretation 3 — Define acceptance criteria and test cases**: The user has specific requirements or features and wants to produce detailed test cases, acceptance criteria, and pass/fail definitions.

If ambiguous, ask: "I can help with creating a full V&V plan, auditing existing test coverage, or defining specific test cases and acceptance criteria — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/vv 4x [input]").

| Depth | Min Requirements Traced | Min Test Cases | Min V&V Methods | Min Validation Scenarios |
|-------|------------------------|---------------|-----------------|------------------------|
| 1x    | 10                     | 10            | 2               | 3                      |
| 2x    | 25                     | 25            | 3               | 5                      |
| 4x    | 50                     | 50            | 4               | 8                      |
| 8x    | 80                     | 100           | 4               | 12                     |
| 16x   | 120                    | 200           | 4               | 20                     |

---

## The Process

### Step 1: Requirements Traceability Matrix

Map every requirement to its verification and validation approach:

```
REQUIREMENTS TRACEABILITY MATRIX:

| Req ID | Requirement Text | Type | V&V Method | Test Case ID | Acceptance Criteria | Status |
|--------|-----------------|------|-----------|-------------|--------------------|---------|
| R-001 | [requirement] | FUNC/PERF/SEC/REL/... | T/A/I/D | TC-XXX | [measurable criterion] | PLANNED/PASS/FAIL |
| R-002 | [requirement] | FUNC/PERF/SEC/REL/... | T/A/I/D | TC-XXX | [measurable criterion] | PLANNED/PASS/FAIL |
...

V&V METHODS:
- T = Test: Execute the system and observe behavior (most rigorous)
- A = Analysis: Use models, calculations, or simulations to verify (when testing is impractical)
- I = Inspection: Visually examine or review artifacts (for physical or documentation requirements)
- D = Demonstration: Show capability in a controlled setting (for qualitative requirements)

COVERAGE SUMMARY:
| Method | Count | Percentage |
|--------|-------|-----------|
| Test | [N] | [%] |
| Analysis | [N] | [%] |
| Inspection | [N] | [%] |
| Demonstration | [N] | [%] |
| UNVERIFIED | [N] | [%] ← must be 0 |
```

---

### Step 2: Verification Plan

#### 2A: Method Selection Rationale

For each requirement, justify the chosen V&V method:

```
METHOD SELECTION:

| Req ID | Selected Method | Rationale | Alternatives Considered |
|--------|----------------|-----------|------------------------|
| R-001 | Test | Behavior directly observable; pass/fail criteria clear | Analysis possible but less definitive |
| R-002 | Analysis | Destructive testing impractical; mathematical model sufficient | Demonstration considered but not repeatable |
...

METHOD SELECTION CRITERIA:
| Criterion | Favors Test | Favors Analysis | Favors Inspection | Favors Demonstration |
|-----------|-------------|----------------|-------------------|---------------------|
| Requirement clarity | Quantitative, measurable | Complex, multi-variable | Visual/physical | Qualitative |
| System availability | System exists/can be built | System unavailable | Artifacts available | Prototype available |
| Cost constraint | Low-medium cost | High cost to test | Very low cost | Medium cost |
| Risk level | HIGH risk reqs | Medium risk | LOW risk | Medium risk |
| Repeatability need | Must repeat exactly | Repeatable via model | One-time sufficient | Semi-repeatable |
```

#### 2B: Verification Levels

```
VERIFICATION LEVELS:

| Level | Scope | What It Verifies | When |
|-------|-------|-----------------|------|
| Unit/Component | Single component | Component requirements met | During development |
| Integration | Component interactions | Interfaces work correctly | After component verification |
| System | Whole system | System requirements met | After integration |
| Acceptance | System in context | Stakeholder needs satisfied | Before delivery |

LEVEL MAPPING:
| Req ID | Unit | Integration | System | Acceptance |
|--------|------|-------------|--------|-----------|
| R-001 | TC-001 | TC-050 | TC-100 | TC-200 |
| R-002 | — | TC-051 | TC-101 | TC-201 |
...
```

---

### Step 3: Test Case Specification

For each test case:

```
TEST CASE: TC-[XXX]
TITLE: [descriptive name]
TRACES TO: R-[XXX], R-[YYY]
LEVEL: UNIT/INTEGRATION/SYSTEM/ACCEPTANCE
METHOD: TEST/ANALYSIS/INSPECTION/DEMONSTRATION
PRIORITY: HIGH/MED/LOW

PRECONDITIONS:
- [system state before test]
- [required configuration]
- [required test data]

TEST STEPS:
| Step | Action | Expected Result | Actual Result | Pass/Fail |
|------|--------|----------------|---------------|-----------|
| 1 | [what to do] | [what should happen] | [fill during execution] | |
| 2 | [what to do] | [what should happen] | | |
...

ACCEPTANCE CRITERIA:
- [specific, measurable criterion 1]
- [specific, measurable criterion 2]

PASS CONDITION: [all criteria met / N of M criteria met]
FAIL CONDITION: [any criterion not met / specific failure definition]

POST-CONDITIONS:
- [required cleanup]
- [system state after test]

TEST DATA:
| Input | Value | Source |
|-------|-------|--------|
| [parameter] | [value] | [where it comes from] |
...

ENVIRONMENT:
- Hardware: [required hardware]
- Software: [required software/config]
- Tools: [test tools needed]
```

---

### Step 4: Validation Planning

Validation answers "did we build the right thing?" — distinct from verification:

```
VALIDATION APPROACH:

STAKEHOLDER VALIDATION MATRIX:
| Stakeholder | Validation Method | Scenario | Success Criteria | Status |
|-------------|------------------|----------|-----------------|--------|
| [end user] | Usability test | [real-world scenario] | [satisfaction metric] | PLANNED |
| [operator] | Operational trial | [operational scenario] | [performance metric] | PLANNED |
| [customer] | Acceptance review | [acceptance scenario] | [contractual criteria] | PLANNED |
...

VALIDATION SCENARIOS:
| ID | Scenario | Description | Stakeholders | Duration |
|----|----------|-------------|-------------|----------|
| VS-001 | [name] | [realistic usage scenario] | [who participates] | [time] |
| VS-002 | [name] | [edge case scenario] | [who participates] | [time] |
| VS-003 | [name] | [stress/degraded scenario] | [who participates] | [time] |
...

VALIDATION vs VERIFICATION DISTINCTION:
| Aspect | Verification | Validation |
|--------|-------------|-----------|
| Question | Built it right? | Built the right thing? |
| Basis | Requirements & design specs | Stakeholder needs & mission |
| Who | Engineering team | Stakeholders & users |
| When | Throughout development | At milestones & delivery |
| Evidence | Test results, analysis reports | User feedback, operational data |
```

---

### Step 5: V&V Schedule and Resources

```
V&V SCHEDULE:

| Phase | Activity | Start | End | Dependencies | Resources |
|-------|----------|-------|-----|-------------|-----------|
| Unit V | Component testing | [date] | [date] | Components built | [people, tools] |
| Integration V | Interface testing | [date] | [date] | Unit V complete | [people, tools, environment] |
| System V | System testing | [date] | [date] | Integration V complete | [people, tools, environment] |
| Validation | Stakeholder validation | [date] | [date] | System V complete | [stakeholders, environment] |
| Acceptance | Formal acceptance | [date] | [date] | Validation complete | [customer, documentation] |

RESOURCE REQUIREMENTS:
| Resource | Quantity | Availability | Lead Time |
|----------|---------|-------------|-----------|
| Test environment | [description] | [when available] | [setup time] |
| Test tools | [list] | [when available] | [procurement time] |
| Test personnel | [roles, count] | [when available] | [training time] |
| Test data | [description] | [when available] | [generation time] |

RISK TO V&V:
| Risk | Impact on V&V | Mitigation |
|------|-------------|-----------|
| Environment not ready | Delays system testing | Parallel environment setup |
| Requirements change late | Rework test cases | Change control process |
| Test tool failure | Blocks automated testing | Manual fallback procedures |
...
```

---

### Step 6: Results Tracking and Reporting

```
V&V RESULTS DASHBOARD:

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Requirements verified | 100% | [%] | ON TRACK/AT RISK/BEHIND |
| Test cases executed | 100% | [%] | ON TRACK/AT RISK/BEHIND |
| Test cases passed | >95% | [%] | ON TRACK/AT RISK/BEHIND |
| Defects found | — | [N] | [trend] |
| Critical defects open | 0 | [N] | ON TRACK/AT RISK/BEHIND |
| Validation scenarios complete | 100% | [%] | ON TRACK/AT RISK/BEHIND |

DEFECT TRACKING:
| Defect ID | Req ID | Severity | Description | Status | Resolution |
|-----------|--------|----------|-------------|--------|------------|
| D-001 | R-XXX | CRIT/HIGH/MED/LOW | [description] | OPEN/INVESTIGATING/FIXED/VERIFIED | [resolution] |
...
```

---

## Output Format

```
## V&V PLAN: [System Name]

### Document Control
Version: [X.Y]
Date: [date]
Status: [DRAFT/REVIEW/APPROVED]

### Requirements Traceability Matrix
[Complete RTM with every requirement mapped to V&V method, test cases, and acceptance criteria]

### Verification Plan
[Method selection rationale, verification levels, test case inventory]

### Test Case Specifications
[Detailed test cases with steps, expected results, pass/fail criteria]

### Validation Plan
[Stakeholder validation matrix, validation scenarios]

### Schedule and Resources
[V&V timeline, resource requirements, risks to V&V]

### Results Tracking
[Dashboard template, defect tracking template]

### Coverage Gaps
[Any requirements without V&V coverage — must be zero at completion]

### Open Items
[Pending decisions, TBDs, stakeholder input needed]
```

---

## Quality Checklist

Before completing:
- [ ] Every requirement has at least one V&V method assigned
- [ ] Every requirement has at least one test case or analysis
- [ ] V&V method selection is justified for each requirement
- [ ] Test cases have specific, measurable acceptance criteria
- [ ] Pass and fail conditions are unambiguous
- [ ] Verification covers all levels (unit, integration, system, acceptance)
- [ ] Validation scenarios include real stakeholders and realistic conditions
- [ ] Schedule accounts for environment setup and tool procurement
- [ ] Coverage gaps are identified and have a plan to close
- [ ] No requirements remain unverified (coverage = 100%)

---

## Next Steps

After V&V planning:
1. Use `/iface` to verify interface specifications are testable
2. Use `/riskmgmt` to assess risks that could derail V&V activities
3. Use `/sysintegration` to align integration sequence with V&V levels
4. Use `/requirements` to verify requirements are testable and measurable
5. Use `/configmgmt` to baseline test artifacts and manage test configuration
