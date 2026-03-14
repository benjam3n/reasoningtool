---
name: "sysintegration - Systems Integration"
description: Plan and execute the integration of subsystems into a working whole. Produces an integration plan with strategy selection, dependency analysis, integration sequence, test cases, and issue tracking.
output:
  format: "table"
---

# Systems Integration

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Plan integration for a system under development**: The user has a multi-component system design and wants to plan how to bring all the pieces together — strategy, sequence, dependencies, tests, and environment.
**Interpretation 2 — Troubleshoot integration issues on an ongoing project**: The user is in the middle of integration and encountering problems — interface mismatches, unexpected behaviors, or failures — and needs to diagnose and resolve them.
**Interpretation 3 — Define integration strategy for a system of systems**: The user has multiple independently developed systems that need to work together and wants to plan the integration approach across organizational and technical boundaries.

If ambiguous, ask: "I can help with planning integration for a new system, troubleshooting integration issues, or planning system-of-systems integration — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/sysintegration 4x [input]").

| Depth | Min Components | Min Integration Steps | Min Integration Tests | Min Issue Scenarios |
|-------|---------------|---------------------|--------------------|-------------------|
| 1x    | 3             | 4                   | 5                  | 3                 |
| 2x    | 6             | 8                   | 12                 | 6                 |
| 4x    | 12            | 15                  | 25                 | 12                |
| 8x    | 20            | 25                  | 50                 | 20                |
| 16x   | 30            | 40                  | 80                 | 30                |

---

## The Process

### Step 1: Integration Scope and Architecture

Define what needs to be integrated:

```
SYSTEM: [name]
INTEGRATION GOAL: [what "fully integrated" means]

COMPONENT INVENTORY:
| ID | Component | Responsibility | Maturity | Owner | Dependencies |
|----|-----------|---------------|----------|-------|-------------|
| C-001 | [name] | [what it does] | DEV/TEST/VERIFIED/RELEASED | [team] | [depends on C-XXX] |
| C-002 | [name] | [what it does] | DEV/TEST/VERIFIED/RELEASED | [team] | [depends on C-XXX] |
...

INTERFACE MAP:
| Interface | From | To | Type | Status | Risk |
|-----------|------|----|------|--------|------|
| IF-001 | C-001 | C-002 | [DATA/CONTROL/PHYSICAL] | DEFINED/IMPLEMENTED/TESTED | HIGH/MED/LOW |
...

EXTERNAL DEPENDENCIES:
| Dependency | Type | Provider | Status | Fallback |
|-----------|------|----------|--------|----------|
| [what's needed] | HW/SW/SERVICE/DATA | [who provides it] | AVAILABLE/PENDING/AT RISK | [alternative] |
...
```

---

### Step 2: Integration Strategy Selection

Choose and justify the integration approach:

```
INTEGRATION STRATEGIES:

| Strategy | Description | Best When | Risks |
|----------|-------------|-----------|-------|
| Big Bang | Integrate all components at once | Few components, well-tested individually, tight schedule | Hard to isolate failures, high risk |
| Bottom-Up | Start with lowest-level components, build up | Infrastructure/utility components are stable | Need test drivers for upper layers |
| Top-Down | Start with top-level, stub lower components | UI/workflow critical, requirements uncertain | Need stubs, real behavior delayed |
| Incremental | Add one component at a time | Many components, want early feedback | Slower, need careful sequencing |
| Sandwich | Top-down and bottom-up simultaneously, meet in middle | Large system, parallel teams | Complex coordination, middle layer risk |
| Risk-Based | Integrate highest-risk interfaces first | Known high-risk areas, want early risk reduction | May not align with dependency order |
| Feature-Based | Integrate by feature/capability across layers | Agile/incremental delivery | May miss cross-feature interactions |

SELECTED STRATEGY: [strategy name]
RATIONALE: [why this strategy fits this system]

STRATEGY ADAPTATION:
- [any modifications to the pure strategy]
- [hybrid approaches if needed]
- [constraints that shaped the choice]
```

---

### Step 3: Integration Sequence

Define the step-by-step order:

```
INTEGRATION SEQUENCE:

| Step | Phase | Components Integrated | New Interfaces Active | Predecessor Steps | Verification |
|------|-------|----------------------|----------------------|-------------------|-------------|
| S-01 | Foundation | C-001 + C-002 | IF-001 | None | IT-001, IT-002 |
| S-02 | Core | + C-003 | IF-002, IF-003 | S-01 | IT-003, IT-004 |
| S-03 | Extended | + C-004, C-005 | IF-004, IF-005, IF-006 | S-02 | IT-005, IT-006 |
| S-04 | External | + ExtSys-001 | IF-007 | S-03 | IT-007 |
| S-05 | Full System | All components | All interfaces | S-04 | IT-008, IT-009 |
...

DEPENDENCY GRAPH (textual):
C-001 ──→ C-003 ──→ C-005
  │                    ↑
  └──→ C-002 ──→ C-004─┘
                   │
              ExtSys-001

CRITICAL PATH: [sequence of steps that determines minimum integration time]
PARALLEL OPPORTUNITIES: [steps that can be done simultaneously]

SEQUENCE RATIONALE:
| Step | Why This Order |
|------|---------------|
| S-01 | [reason — e.g., foundation components with no dependencies] |
| S-02 | [reason — e.g., core business logic depends on S-01] |
...
```

---

### Step 4: Integration Test Cases

Define tests that verify integration, not individual components:

```
INTEGRATION TEST CASES:

TEST CASE: IT-[XXX]
TITLE: [descriptive name]
INTEGRATION STEP: S-[XX]
INTERFACES TESTED: IF-[XXX], IF-[YYY]
COMPONENTS INVOLVED: C-[XXX], C-[YYY]

PURPOSE: [what integration aspect this verifies — data flow, timing, error propagation, etc.]

PRECONDITIONS:
- [prior integration steps completed]
- [configuration state]
- [test data available]

TEST PROCEDURE:
| Step | Action | Expected Behavior | Check |
|------|--------|-------------------|-------|
| 1 | [trigger in component A] | [expected response in component B] | [how to verify] |
| 2 | [observe data at interface] | [correct format, timing, content] | [how to verify] |
...

PASS CRITERIA:
- [specific measurable criterion]
- [specific measurable criterion]

FAILURE INDICATORS:
- [what would indicate integration failure]
- [what would indicate partial failure]

INTEGRATION-SPECIFIC CHECKS:
| Check | Description | Pass/Fail |
|-------|-------------|-----------|
| Data flows end-to-end | Data from A arrives at B correctly | |
| Timing constraints met | Response within specified latency | |
| Error propagation correct | Errors in A handled correctly by B | |
| Resource contention absent | No deadlocks, race conditions, or resource conflicts | |
| State consistency | Shared state remains consistent across components | |
```

---

### Step 5: Integration Environment

```
INTEGRATION ENVIRONMENT:

ENVIRONMENT TIERS:
| Tier | Purpose | Fidelity | Availability |
|------|---------|----------|-------------|
| Dev Integration | Early interface check | Low — stubs and mocks | Always available |
| Test Integration | Formal integration testing | Medium — real components, synthetic data | Scheduled access |
| Staging | Pre-production validation | High — production-like | Limited access |
| Production | Deployment | Full fidelity | Controlled release |

ENVIRONMENT SPECIFICATION:
| Element | Requirement | Status | Owner |
|---------|------------|--------|-------|
| Hardware | [specific HW needed] | AVAILABLE/ORDERED/PENDING | [who] |
| Network | [topology, bandwidth, latency] | AVAILABLE/CONFIGURED/PENDING | [who] |
| Software | [OS, middleware, tools] | AVAILABLE/INSTALLED/PENDING | [who] |
| Test Data | [data sets needed] | AVAILABLE/GENERATED/PENDING | [who] |
| Simulators/Stubs | [what needs to be simulated] | AVAILABLE/DEVELOPED/PENDING | [who] |
| Monitoring | [logging, tracing, metrics] | AVAILABLE/CONFIGURED/PENDING | [who] |

ENVIRONMENT RISKS:
| Risk | Impact | Mitigation |
|------|--------|-----------|
| [environment risk] | [delay or quality impact] | [what to do about it] |
...
```

---

### Step 6: Issue Tracking and Resolution

```
INTEGRATION ISSUE TRACKING:

ISSUE LOG:
| Issue ID | Date | Step | Components | Description | Severity | Root Cause | Resolution | Status |
|----------|------|------|-----------|-------------|----------|-----------|------------|--------|
| II-001 | [date] | S-[XX] | C-XXX, C-YYY | [what went wrong] | BLOCKER/MAJOR/MINOR | [cause] | [fix] | OPEN/INVESTIGATING/RESOLVED |
...

COMMON INTEGRATION ISSUE CATEGORIES:
| Category | Symptoms | Typical Root Cause | Investigation Steps |
|----------|----------|-------------------|-------------------|
| Interface mismatch | Data corruption, parse errors | Schema/format disagreement | Compare ICD with implementation |
| Timing issue | Timeouts, race conditions | Async assumptions differ | Add instrumentation, trace timing |
| Configuration drift | Works in dev, fails in integration | Environment differences | Compare configs across environments |
| Resource contention | Deadlocks, performance degradation | Shared resource conflicts | Monitor resource usage, check locks |
| Version incompatibility | Unexpected behavior | Different component versions | Verify version matrix |
| Missing error handling | Cascade failures | Error paths not implemented | Inject faults, trace error flow |

INTEGRATION METRICS:
| Metric | Value | Trend | Target |
|--------|-------|-------|--------|
| Issues found this step | [N] | [↑↓→] | Decreasing per step |
| Blockers open | [N] | [↑↓→] | 0 to proceed |
| Mean time to resolve | [hours/days] | [↑↓→] | Decreasing |
| Steps completed on schedule | [N/total] | [↑↓→] | 100% |
| Regression failures | [N] | [↑↓→] | 0 |
```

---

## Output Format

```
## INTEGRATION PLAN: [System Name]

### Document Control
Version: [X.Y]
Date: [date]
Status: [DRAFT/REVIEW/APPROVED]

### Integration Scope
[Component inventory, interface map, external dependencies]

### Integration Strategy
[Selected strategy with rationale]

### Integration Sequence
[Step-by-step sequence with dependencies and parallel opportunities]

### Integration Sequence Diagram
[Textual dependency graph showing integration order]

### Integration Test Cases
[Test cases for each integration step]

### Integration Environment
[Environment tiers, specifications, readiness]

### Issue Tracking
[Issue log template, common issue categories, metrics]

### Schedule
[Timeline for each integration step with milestones]

### Risks
[Integration-specific risks with mitigations]

### Open Items
[Pending decisions, environment readiness gaps, unresolved dependencies]
```

---

## Quality Checklist

Before completing:
- [ ] All components inventoried with maturity and ownership
- [ ] All interfaces mapped between components
- [ ] Integration strategy selected with rationale
- [ ] Integration sequence respects all dependencies
- [ ] Critical path identified
- [ ] Integration test cases defined for each step
- [ ] Tests focus on integration aspects (not component function)
- [ ] Environment requirements specified with readiness status
- [ ] Issue tracking process defined with severity levels
- [ ] Rollback plan exists for each integration step
- [ ] No circular dependencies in integration sequence

---

## Next Steps

After integration planning:
1. Use `/iface` to verify all interface specifications before integration
2. Use `/vv` to align integration tests with the overall V&V plan
3. Use `/riskmgmt` to assess integration-specific risks
4. Use `/configmgmt` to manage component versions and baselines during integration
5. Use `/de` to verify dependency analysis is complete
6. Use `/to` to optimize the integration sequence
