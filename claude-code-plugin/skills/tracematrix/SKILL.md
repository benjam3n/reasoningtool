---
name: "tracematrix - Requirements Traceability Matrix"
description: Create and maintain bidirectional traceability from stakeholder needs through requirements to design, implementation, and test. Identifies orphan requirements, gold-plating, and coverage gaps.
output:
  format: "table"
---

# Requirements Traceability Matrix

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Build a traceability matrix from scratch**: The user has requirements, design artifacts, code, and/or tests and needs to establish traceability links across all levels from stakeholder needs down to verification evidence.
**Interpretation 2 — Audit an existing traceability matrix for gaps**: The user has a traceability matrix and wants to find orphan requirements, missing links, gold-plating, and coverage holes.
**Interpretation 3 — Trace a specific requirement end-to-end**: The user wants to follow one or more specific requirements through the full chain (need → requirement → design → code → test) to verify completeness.

If ambiguous, ask: "I can help with building a traceability matrix from scratch, auditing an existing matrix for gaps, or tracing specific requirements end-to-end — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/tracematrix 4x [input]").

| Depth | Min Items Traced | Min Trace Levels | Min Gap Checks | Min Reports Generated | Min Link Types |
|-------|-----------------|------------------|---------------|----------------------|---------------|
| 1x    | 10              | 3                | 3             | 1                    | 2             |
| 2x    | 25              | 4                | 5             | 2                    | 3             |
| 4x    | 50              | 5                | 8             | 3                    | 4             |
| 8x    | 100             | 5                | 12            | 4                    | 5             |
| 16x   | 200             | 6                | 15            | 5                    | 6             |

---

## The Process

### Step 1: Establish Traceability Levels and Link Types

Define the levels of abstraction and the link types that connect them:

```
TRACEABILITY ARCHITECTURE:

Level 1: STAKEHOLDER NEEDS (why the system exists)
    ↓ [derived from]
Level 2: SYSTEM REQUIREMENTS (what the system must do)
    ↓ [satisfied by]
Level 3: DESIGN ELEMENTS (how the system does it)
    ↓ [implemented by]
Level 4: CODE/IMPLEMENTATION (the actual build artifacts)
    ↓ [verified by]
Level 5: TEST CASES & RESULTS (evidence it works)
```

Link type definitions:

| Link Type | From → To | Meaning | Example |
|-----------|-----------|---------|---------|
| **Derived From** | Requirement → Need | This requirement exists to satisfy this stakeholder need | REQ-001 derived from NEED-003 |
| **Satisfied By** | Requirement → Design | This design element satisfies this requirement | REQ-001 satisfied by DES-005 |
| **Implemented By** | Design → Code | This code module implements this design element | DES-005 implemented by MOD-auth.py |
| **Verified By** | Requirement → Test | This test case verifies this requirement is met | REQ-001 verified by TC-012 |
| **Depends On** | Requirement → Requirement | This requirement depends on another | REQ-005 depends on REQ-001 |
| **Conflicts With** | Requirement → Requirement | These requirements are in tension | REQ-003 conflicts with REQ-007 |
| **Refines** | Requirement → Requirement | Child requirement refines a parent | REQ-001.1 refines REQ-001 |

---

### Step 2: Build the Forward Traceability Matrix (Needs → Tests)

Trace from stakeholder needs forward through the chain:

```
FORWARD TRACEABILITY MATRIX:

| Need ID | Need Description | Req IDs | Design IDs | Code Modules | Test Case IDs | Status |
|---------|-----------------|---------|-----------|-------------|---------------|--------|
| N-001 | [stakeholder need] | REQ-001, REQ-002 | DES-001, DES-003 | mod_a.py, mod_b.py | TC-001, TC-005 | COMPLETE |
| N-002 | [stakeholder need] | REQ-003 | DES-004 | mod_c.py | — | MISSING TESTS |
| N-003 | [stakeholder need] | — | — | — | — | ORPHAN NEED |
...
```

---

### Step 3: Build the Backward Traceability Matrix (Tests → Needs)

Trace from test cases and code backward to find gold-plating:

```
BACKWARD TRACEABILITY MATRIX:

| Test Case ID | Test Description | Verifies Req | Req Traces to Need | Status |
|-------------|-----------------|-------------|-------------------|--------|
| TC-001 | [what it tests] | REQ-001 | N-001 | LINKED |
| TC-002 | [what it tests] | REQ-004 | N-002 | LINKED |
| TC-003 | [what it tests] | — | — | GOLD-PLATED TEST |
...

| Code Module | Module Purpose | Implements Design | Design Traces to Req | Status |
|------------|---------------|------------------|---------------------|--------|
| mod_a.py | [purpose] | DES-001 | REQ-001 | LINKED |
| mod_d.py | [purpose] | — | — | GOLD-PLATED CODE |
...
```

---

### Step 4: Identify Orphan Requirements

Requirements that lack a parent (no stakeholder need) or lack children (no design, code, or test):

```
ORPHAN ANALYSIS:

UPWARD ORPHANS (no parent need):
| Req ID | Description | Issue | Action Needed |
|--------|-------------|-------|---------------|
| REQ-005 | [description] | No stakeholder need traced | Find the need or question the requirement |
| REQ-008 | [description] | No stakeholder need traced | Find the need or question the requirement |

DOWNWARD ORPHANS (no children):
| Req ID | Description | Missing Link | Action Needed |
|--------|-------------|-------------|---------------|
| REQ-003 | [description] | No design element | Create design or mark as deferred |
| REQ-006 | [description] | No test case | Write test case |
| REQ-009 | [description] | No code implementation | Implement or mark as future |

STATISTICS:
  Total requirements: [N]
  Fully traced (need → req → design → code → test): [N] ([%])
  Missing upward trace: [N] ([%])
  Missing design trace: [N] ([%])
  Missing code trace: [N] ([%])
  Missing test trace: [N] ([%])
```

---

### Step 5: Identify Gold-Plating

Implementation or tests that exist without a driving requirement:

```
GOLD-PLATING ANALYSIS:

| Item Type | Item ID | Description | Traces to Requirement? | Disposition |
|-----------|---------|-------------|----------------------|-------------|
| Code | mod_x.py | [what it does] | NO | Remove / Create requirement / Document as infrastructure |
| Design | DES-012 | [what it describes] | NO | Remove / Create requirement |
| Test | TC-015 | [what it tests] | NO | Remove / Create requirement |
| Feature | [feature] | [what it does] | NO | Remove / Create requirement |

GOLD-PLATING SUMMARY:
  Untraced code modules: [N]
  Untraced design elements: [N]
  Untraced test cases: [N]
  Total gold-plated items: [N]

NOTE: Not all untraced items are bad. Infrastructure code (logging frameworks, build
scripts) may not trace to a specific requirement. Mark these as "infrastructure" and
document separately.
```

---

### Step 6: Verify Completeness of Coverage

Run systematic coverage checks:

```
COVERAGE REPORT:

| Coverage Metric | Target | Actual | Status |
|----------------|--------|--------|--------|
| Needs → Requirements | 100% of needs have ≥1 requirement | [N]% | PASS/FAIL |
| Requirements → Design | 100% of requirements have ≥1 design element | [N]% | PASS/FAIL |
| Design → Code | 100% of design elements implemented | [N]% | PASS/FAIL |
| Requirements → Tests | 100% of requirements have ≥1 test case | [N]% | PASS/FAIL |
| Tests → Results | 100% of test cases have been executed | [N]% | PASS/FAIL |
| MUST requirements fully traced | 100% | [N]% | PASS/FAIL |
| SHOULD requirements fully traced | ≥90% | [N]% | PASS/FAIL |

COVERAGE HEAT MAP:

| Requirement | Need | Design | Code | Test | Result | Completeness |
|-------------|------|--------|------|------|--------|-------------|
| REQ-001 | Y | Y | Y | Y | PASS | 100% |
| REQ-002 | Y | Y | Y | N | — | 80% |
| REQ-003 | Y | N | N | N | — | 20% |
| REQ-004 | N | Y | Y | Y | PASS | 80% (no need) |
...
```

---

### Step 7: Generate Traceability Reports

Produce reports for different audiences:

```
REPORT 1 — EXECUTIVE SUMMARY:
  Total stakeholder needs: [N]
  Total requirements: [N]
  Fully traced requirements: [N] ([%])
  Orphan requirements: [N]
  Gold-plated items: [N]
  Test coverage: [N]%
  Overall traceability health: GREEN / YELLOW / RED

REPORT 2 — GAP REPORT (for project managers):
  [List of all gaps, prioritized by requirement priority]

  | Gap ID | Type | Item | Missing Link | Priority | Owner | Due Date |
  |--------|------|------|-------------|----------|-------|----------|
  | G-001 | Missing test | REQ-003 | No test case | HIGH | [who] | [when] |
  | G-002 | Orphan code | mod_x.py | No requirement | LOW | [who] | [when] |
  ...

REPORT 3 — REQUIREMENT TRACE (for auditors/certifiers):
  [For each requirement, the complete chain from need to test evidence]

  REQ-001: [description]
    ← Derived from: N-001 [need description]
    → Satisfied by: DES-001 [design description]
    → Implemented by: mod_a.py [module description]
    → Verified by: TC-001 [test description] — RESULT: PASS [date]

REPORT 4 — CHANGE IMPACT (for change management):
  If [item] changes, these items are affected:
  [item] → [linked items in both directions]
```

---

## Output Format

```
## TRACEABILITY MATRIX: [System Name]

### Traceability Architecture
[Levels and link types used]

### Forward Traceability (Needs → Tests)
[Full forward matrix]

### Backward Traceability (Tests → Needs)
[Full backward matrix]

### Gap Analysis
  Orphan requirements (no parent): [N]
  Requirements without design: [N]
  Requirements without tests: [N]
  Gold-plated items: [N]

### Coverage Summary
  Overall: [N]% fully traced
  MUST requirements: [N]% fully traced
  Test coverage: [N]%

### Action Items
[Prioritized list of gaps to close]

### Change Impact Map
[Key dependencies for change management]
```

---

## Quality Checklist

Before completing:
- [ ] All traceability levels defined (need, requirement, design, code, test)
- [ ] Forward traceability complete (needs → requirements → design → code → test)
- [ ] Backward traceability complete (tests → code → design → requirements → needs)
- [ ] Orphan requirements identified (requirements without parent needs)
- [ ] Gold-plating identified (code/tests without requirements)
- [ ] Coverage metrics calculated per level
- [ ] MUST-have requirements have 100% traceability
- [ ] Gap report generated with owners and due dates
- [ ] Traceability matrix is bidirectional (can navigate both ways)
- [ ] Infrastructure items distinguished from gold-plating

---

## Next Steps

After building the traceability matrix:
1. Use `/requirements` to improve any poorly specified requirements found during tracing
2. Use `/testplan` to create test cases for requirements that lack verification
3. Use `/sysdecomp` to verify component-to-requirement allocation
4. Use `/tpm` to identify which traced requirements need ongoing performance tracking
5. Use `/de` to understand dependencies between traced items for change impact analysis