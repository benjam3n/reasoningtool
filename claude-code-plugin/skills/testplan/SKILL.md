---
name: "testplan - Test Planning & Verification Strategy"
description: Design comprehensive test strategy and plans for system verification and validation. Defines test levels, types, cases, environments, and criteria to ensure thorough coverage.
output:
  format: "table"
---

# Test Planning & Verification Strategy

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Create a test plan for a new system**: The user has a system or product under development and needs a comprehensive test strategy covering all test levels, types, environments, and criteria from scratch.
**Interpretation 2 — Audit an existing test plan for gaps**: The user has an existing test approach and wants to identify missing test coverage, weak areas, or risks in their current verification strategy.
**Interpretation 3 — Design test cases for specific requirements**: The user has a defined set of requirements and needs detailed test case specifications with procedures, expected results, and traceability.

If ambiguous, ask: "I can help with creating a full test plan for a new system, auditing an existing test plan for gaps, or designing detailed test cases for specific requirements — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/testplan 4x [input]").

| Depth | Min Test Cases | Min Test Levels | Min Test Types | Min Env Requirements | Min Risk Items |
|-------|---------------|-----------------|----------------|---------------------|---------------|
| 1x    | 10            | 3               | 3              | 2                   | 3             |
| 2x    | 25            | 4               | 5              | 4                   | 6             |
| 4x    | 50            | 5               | 7              | 6                   | 10            |
| 8x    | 100           | 5               | 9              | 8                   | 15            |
| 16x   | 200           | 5               | 12             | 12                  | 25            |

---

## The Process

### Step 1: Define Test Objectives and Scope

Establish what testing must accomplish and its boundaries:

```
TEST PLAN: [System Name]
VERSION: [version]
DATE: [date]

TEST OBJECTIVES:
1. Verify that [system] meets all specified requirements
2. Validate that [system] satisfies stakeholder needs and intended use
3. Identify defects before [milestone/release]
4. Demonstrate compliance with [standards/regulations]

SCOPE:
  IN SCOPE:
  - [features/subsystems to test]
  - [interfaces to verify]
  - [quality attributes to measure]

  OUT OF SCOPE:
  - [features not tested in this plan]
  - [third-party components accepted as-is]
  - [deferred testing areas]

  ASSUMPTIONS:
  - [what must be true for testing to proceed]
  - [availability of resources, environments, data]
```

---

### Step 2: Identify Test Levels

Define the test levels and what each verifies:

| Level | Purpose | Scope | Responsible | Entry Criteria | Exit Criteria |
|-------|---------|-------|-------------|----------------|---------------|
| **Unit Test** | Verify individual components work correctly in isolation | Single function, class, or module | Developer | Code complete, code review passed | 100% of unit tests pass, coverage target met |
| **Integration Test** | Verify interfaces between components work correctly | Component-to-component interactions | Dev/Test team | Unit tests pass, interface specs available | All interface tests pass, no critical defects |
| **System Test** | Verify the complete system meets requirements | End-to-end system behavior | Test team | Integration tests pass, system deployed to test env | All requirements verified, defect targets met |
| **Acceptance Test** | Validate the system meets stakeholder needs | User workflows, operational scenarios | User/customer | System tests pass, acceptance criteria defined | Customer sign-off, acceptance criteria met |
| **Regression Test** | Verify changes haven't broken existing functionality | Previously working features | Test team | Code change committed | All regression tests pass |

```
TEST LEVELS FOR [SYSTEM]:

| Level | Applies? | Justification | Estimated Effort |
|-------|----------|---------------|-----------------|
| Unit | YES/NO | [why or why not] | [hours/days] |
| Integration | YES/NO | [why or why not] | [hours/days] |
| System | YES/NO | [why or why not] | [hours/days] |
| Acceptance | YES/NO | [why or why not] | [hours/days] |
| Regression | YES/NO | [why or why not] | [hours/days] |
```

---

### Step 3: Define Test Types Needed

For each applicable test level, determine which test types apply:

| Test Type | What It Verifies | Typical Methods | Priority |
|-----------|-----------------|-----------------|----------|
| **Functional** | Correct behavior per requirements | Black-box, equivalence partitioning, boundary value | MUST |
| **Performance** | Response time, throughput, resource usage | Load testing, stress testing, benchmarking | HIGH |
| **Security** | Resistance to attacks, data protection | Penetration testing, vulnerability scanning, auth testing | HIGH |
| **Usability** | Ease of use, learnability, accessibility | User testing, heuristic evaluation, A/B testing | MEDIUM |
| **Reliability** | Mean time between failures, recovery | Endurance testing, failover testing, chaos testing | HIGH |
| **Compatibility** | Works across platforms, browsers, devices | Cross-platform testing, version compatibility | MEDIUM |
| **Regression** | No unintended side effects from changes | Automated test suite re-execution | MUST |
| **Installation** | Correct deployment and configuration | Install/uninstall, upgrade, migration testing | MEDIUM |
| **Compliance** | Meets regulatory and standards requirements | Audit, certification testing | VARIES |
| **Recovery** | Graceful handling of failures | Crash recovery, backup/restore, data integrity | HIGH |
| **Scalability** | Handles growth in users, data, transactions | Volume testing, capacity testing | MEDIUM |
| **Integration** | External system interfaces work correctly | API testing, protocol testing, contract testing | HIGH |

```
TEST TYPE MATRIX:

| Test Type | Unit | Integration | System | Acceptance | Tool/Method |
|-----------|------|-------------|--------|------------|-------------|
| Functional | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [tool] |
| Performance | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [tool] |
| Security | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [tool] |
| Usability | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [tool] |
| Reliability | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [tool] |
...
```

---

### Step 4: Create Test Case Specifications

For each requirement or feature, define specific test cases:

```
TEST CASE SPECIFICATION:

| TC-ID | Requirement | Test Level | Test Type | Description | Preconditions | Steps | Expected Result | Priority | Status |
|-------|-------------|-----------|-----------|-------------|---------------|-------|-----------------|----------|--------|
| TC-001 | [REQ-ID] | [level] | [type] | [what this tests] | [setup needed] | 1. [step] 2. [step] | [expected outcome] | HIGH/MED/LOW | Not Run |
| TC-002 | [REQ-ID] | [level] | [type] | [what this tests] | [setup needed] | 1. [step] 2. [step] | [expected outcome] | HIGH/MED/LOW | Not Run |
...
```

For each test case, apply boundary and edge case thinking:

| Technique | Application |
|-----------|------------|
| **Equivalence Partitioning** | Divide inputs into classes; test one from each |
| **Boundary Value Analysis** | Test at, just below, just above boundaries |
| **Error Guessing** | Test common failure modes based on experience |
| **Decision Table** | Test all combinations of conditions and actions |
| **State Transition** | Test valid and invalid state changes |
| **Negative Testing** | Test with invalid, missing, or unexpected inputs |

---

### Step 5: Define Test Environment and Data Requirements

```
TEST ENVIRONMENTS:

| Env Name | Purpose | Configuration | Availability | Owner |
|----------|---------|---------------|--------------|-------|
| DEV | Unit & developer testing | [hardware, OS, SW stack] | Always | Dev team |
| TEST | Integration & system testing | [hardware, OS, SW stack] | [schedule] | Test team |
| STAGING | Pre-production validation | [hardware, OS, SW stack — mirrors production] | [schedule] | Ops team |
| UAT | User acceptance testing | [hardware, OS, SW stack] | [schedule] | Business |

TEST DATA REQUIREMENTS:

| Data Set | Purpose | Source | Volume | Sensitivity | Refresh Frequency |
|----------|---------|--------|--------|-------------|-------------------|
| [name] | [what tests use it] | [synthetic/masked production/live] | [size] | [PII? classified?] | [how often refreshed] |
...

TOOLS AND INFRASTRUCTURE:

| Category | Tool | Purpose | License | Owner |
|----------|------|---------|---------|-------|
| Test Management | [tool] | Test case tracking, execution reporting | [type] | [who] |
| Automation | [tool] | Automated test execution | [type] | [who] |
| Performance | [tool] | Load/stress testing | [type] | [who] |
| Defect Tracking | [tool] | Bug reporting and tracking | [type] | [who] |
| CI/CD | [tool] | Continuous integration testing | [type] | [who] |
```

---

### Step 6: Define Entry and Exit Criteria

```
ENTRY CRITERIA (must be met before testing begins):

| Criterion | Verification Method | Required For |
|-----------|-------------------|--------------|
| Requirements reviewed and approved | Review sign-off | All levels |
| Test plan reviewed and approved | Review sign-off | All levels |
| Test environment set up and verified | Env smoke test | All levels |
| Test data prepared and loaded | Data validation | System, Acceptance |
| Code complete and build successful | CI/CD green | All levels |
| Unit tests passing at [X]% | Test report | Integration+ |
| Previous level exit criteria met | Test report | Each subsequent level |

EXIT CRITERIA (must be met before testing is considered complete):

| Criterion | Target | Measurement |
|-----------|--------|-------------|
| Test case execution | 100% of planned tests executed | Test management tool |
| Pass rate | >= [X]% of test cases pass | Test management tool |
| Critical defects | 0 open critical/blocker defects | Defect tracker |
| Major defects | <= [N] open major defects | Defect tracker |
| Requirements coverage | 100% of requirements have at least one test | Traceability matrix |
| Performance targets | All performance requirements met | Performance test results |
| Security scan | No high/critical vulnerabilities | Security scan report |
```

---

### Step 7: Plan Test Schedule and Resources

```
TEST SCHEDULE:

| Phase | Start Date | End Date | Duration | Dependencies | Milestone |
|-------|-----------|----------|----------|--------------|-----------|
| Test Planning | [date] | [date] | [N days] | Requirements complete | Test Plan Approved |
| Test Design | [date] | [date] | [N days] | Test Plan Approved | Test Cases Ready |
| Env Setup | [date] | [date] | [N days] | Infrastructure available | Env Validated |
| Unit Testing | [date] | [date] | [N days] | Code complete | Unit Test Report |
| Integration Testing | [date] | [date] | [N days] | Unit tests pass | Integration Test Report |
| System Testing | [date] | [date] | [N days] | Integration tests pass | System Test Report |
| Acceptance Testing | [date] | [date] | [N days] | System tests pass | Acceptance Sign-off |
| Regression Testing | [ongoing] | [ongoing] | [per cycle] | Code changes | Regression Report |

RESOURCE ALLOCATION:

| Role | Person/Team | Allocation | Phase |
|------|------------|------------|-------|
| Test Lead | [name] | [%] | All phases |
| Test Designer | [name] | [%] | Design, Execution |
| Test Executor | [name] | [%] | Execution |
| Automation Engineer | [name] | [%] | Design, Execution |
| Performance Tester | [name] | [%] | System Testing |
| Security Tester | [name] | [%] | System Testing |
| Environment Admin | [name] | [%] | Setup, Maintenance |

RISK ASSESSMENT:

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Test environment not ready on time | [H/M/L] | [H/M/L] | [action] |
| Insufficient test data | [H/M/L] | [H/M/L] | [action] |
| Requirements changes during testing | [H/M/L] | [H/M/L] | [action] |
| Resource unavailability | [H/M/L] | [H/M/L] | [action] |
| Defect backlog overwhelms schedule | [H/M/L] | [H/M/L] | [action] |
| Third-party dependency delays | [H/M/L] | [H/M/L] | [action] |
```

---

## Output Format

```
## TEST PLAN: [System Name]

### 1. Objectives and Scope
[Objectives, in/out scope, assumptions]

### 2. Test Levels
[Table of applicable test levels with entry/exit criteria]

### 3. Test Types
[Matrix of test types vs test levels]

### 4. Test Cases
[Table of test case specifications with traceability to requirements]

### 5. Test Environment and Data
[Environment specs, data requirements, tools]

### 6. Entry/Exit Criteria
[Tables of entry and exit criteria per level]

### 7. Schedule and Resources
[Timeline, resource allocation, risk assessment]

### 8. Defect Management
[Severity definitions, workflow, escalation]

### 9. Reporting
[What reports, frequency, audience]

### Summary
Total Test Cases: [N]
Test Levels: [N]
Test Types: [N]
Estimated Duration: [N days/weeks]
Key Risks: [top 3]
```

---

## Quality Checklist

Before completing:
- [ ] All requirements have at least one test case (coverage is complete)
- [ ] All test levels identified and justified
- [ ] All relevant test types included
- [ ] Entry and exit criteria are specific and measurable
- [ ] Test environments and data defined
- [ ] Schedule is realistic with dependencies identified
- [ ] Risks identified with mitigations
- [ ] Negative/edge case tests included (not just happy path)
- [ ] Test case priorities assigned
- [ ] Resource needs identified

---

## Next Steps

After test planning:
1. Use `/requirements` to verify requirements are testable before designing test cases
2. Use `/tracematrix` to build traceability from requirements to test cases
3. Use `/tpm` to define technical performance measures that testing must verify
4. Use `/fla` to anticipate test execution failures and plan contingencies
5. Use `/de` to map dependencies between test activities