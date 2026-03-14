---
name: "changemgmt - Change Management"
description: Manage changes to system requirements, design, or implementation in a controlled way. Assesses impact, evaluates alternatives, and ensures traceability through implementation.
output:
  format: "table"
---

# Change Management

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Process a specific change request**: The user has a proposed change (to requirements, design, or implementation) and needs to assess its impact and plan its implementation.
**Interpretation 2 — Establish a change management process**: The user needs to set up the change control framework for a project — board composition, procedures, criteria, and tools.
**Interpretation 3 — Audit change history for issues**: The user has experienced problems (scope creep, broken functionality, lost traceability) and wants to review and improve how changes have been managed.

If ambiguous, ask: "I can help with processing a specific change request, establishing a change management process, or auditing your change history — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/changemgmt 4x [input]").

| Depth | Min Impact Areas Assessed | Min Alternatives Evaluated | Min Affected Items Traced | Min Verification Checks |
|-------|--------------------------|---------------------------|--------------------------|------------------------|
| 1x    | 3                        | 2                         | 5                        | 3                      |
| 2x    | 5                        | 3                         | 12                       | 6                      |
| 4x    | 8                        | 4                         | 25                       | 12                     |
| 8x    | 10                       | 5                         | 50                       | 20                     |
| 16x   | 12                       | 6                         | 80                       | 30                     |

---

## The Process

### Step 1: Receive and Document Change Request

Capture the change request completely:

```
CHANGE REQUEST (CR):

CR Number: [CR-YYYY-NNN]
Date Submitted: [date]
Submitted By: [name, role, organization]
Priority: [EMERGENCY / HIGH / MEDIUM / LOW]

CHANGE IDENTIFICATION:
- Title: [concise description of the change]
- Category: [Requirements / Design / Implementation / Interface / Process / COTS/NDI]
- Affected baseline: [which configuration baseline is affected]
- Affected items: [list of CIs, documents, requirements, interfaces]

DESCRIPTION OF CHANGE:
- Current state: [what exists today]
- Proposed change: [what is being requested]
- Rationale: [why the change is needed]
- Originating source: [customer request / defect / new requirement / regulatory / improvement]

URGENCY JUSTIFICATION (if HIGH or EMERGENCY):
- Why can't this wait for the next planned release?
- What is the consequence of delay?
```

---

### Step 2: Assess Change Impact

Systematically evaluate impact across all dimensions:

#### 2A: Technical Impact

| Area | Current State | Impact of Change | Severity | Confidence |
|------|-------------|-----------------|----------|------------|
| Requirements | [affected requirements] | [new / modified / deleted] | [HIGH/MED/LOW] | [HIGH/MED/LOW] |
| Architecture | [affected components] | [structural change / interface change / none] | [severity] | [confidence] |
| Interfaces | [affected interfaces] | [new / modified / broken] | [severity] | [confidence] |
| Hardware | [affected HW] | [redesign / requalification / none] | [severity] | [confidence] |
| Software | [affected SW modules] | [new code / modified / regression risk] | [severity] | [confidence] |
| Data/databases | [affected data] | [schema change / migration needed] | [severity] | [confidence] |
| Performance | [affected parameters] | [improved / degraded / neutral] | [severity] | [confidence] |
| Reliability/Safety | [affected characteristics] | [impact on MTBF, safety margins] | [severity] | [confidence] |

#### 2B: Schedule Impact

| Phase | Current Plan | Impact | New Date | Slip (days) |
|-------|-------------|--------|----------|-------------|
| Design | [baseline date] | [rework / extension / none] | [new date] | [N] |
| Implementation | [baseline date] | [impact] | [new date] | [N] |
| Test | [baseline date] | [retest / new tests / none] | [new date] | [N] |
| Integration | [baseline date] | [impact] | [new date] | [N] |
| Delivery | [baseline date] | [impact] | [new date] | [N] |

Critical path affected: [Yes/No — explain]

#### 2C: Cost Impact

| Cost Category | Estimated Cost | Basis of Estimate | Confidence |
|---------------|---------------|-------------------|------------|
| Engineering (design) | [$] | [hours x rate] | [HIGH/MED/LOW] |
| Engineering (test) | [$] | [hours x rate] | [confidence] |
| Hardware/materials | [$] | [BOM change] | [confidence] |
| Software development | [$] | [LOC / function points] | [confidence] |
| Tooling/equipment | [$] | [new tools needed] | [confidence] |
| Documentation | [$] | [pages / documents affected] | [confidence] |
| Training | [$] | [curriculum changes] | [confidence] |
| Retrofit (fielded units) | [$] | [units x cost per unit] | [confidence] |
| **TOTAL** | **[$]** | | |

#### 2D: Risk Impact

| Risk | Likelihood | Consequence | Risk Level | Mitigation |
|------|-----------|-------------|------------|------------|
| Change introduces new defects | [H/M/L] | [impact] | [H/M/L] | [testing strategy] |
| Change breaks existing functionality | [H/M/L] | [impact] | [H/M/L] | [regression testing] |
| Schedule estimate is wrong | [H/M/L] | [impact] | [H/M/L] | [buffer / phased approach] |
| Change is incomplete (more changes needed) | [H/M/L] | [impact] | [H/M/L] | [thorough analysis] |
| Ripple effects to other systems | [H/M/L] | [impact] | [H/M/L] | [interface review] |

---

### Step 3: Evaluate Alternatives

Always consider alternatives, including doing nothing:

```
ALTERNATIVES ANALYSIS:

ALTERNATIVE 0: Do Nothing
- Description: Accept current state, do not implement change
- Pros: [no cost, no risk, no schedule impact]
- Cons: [consequence of not changing — why this was requested]
- Feasibility: [can we live with the current state?]

ALTERNATIVE 1: Implement as Requested
- Description: [full implementation of the CR]
- Pros: [fully addresses the need]
- Cons: [cost, schedule, risk impacts from Step 2]
- Feasibility: [technical and programmatic feasibility]

ALTERNATIVE 2: Partial Implementation
- Description: [implement a subset or simplified version]
- Pros: [reduced cost/risk while addressing core need]
- Cons: [doesn't fully address need, may need follow-up]
- Feasibility: [assessment]

ALTERNATIVE 3: Different Approach
- Description: [achieve the same goal through a different mechanism]
- Pros: [potentially lower impact]
- Cons: [trade-offs]
- Feasibility: [assessment]

COMPARISON MATRIX:
| Criterion | Weight | Alt 0 (Do Nothing) | Alt 1 (As Requested) | Alt 2 (Partial) | Alt 3 (Different) |
|-----------|--------|--------------------|--------------------|----------------|-------------------|
| Addresses need | [W] | [score] | [score] | [score] | [score] |
| Technical risk | [W] | [score] | [score] | [score] | [score] |
| Cost | [W] | [score] | [score] | [score] | [score] |
| Schedule | [W] | [score] | [score] | [score] | [score] |
| Side effects | [W] | [score] | [score] | [score] | [score] |
| **Weighted Total** | | **[total]** | **[total]** | **[total]** | **[total]** |

RECOMMENDATION: [Alternative N] because [rationale]
```

---

### Step 4: Change Control Board Decision

```
CHANGE CONTROL BOARD (CCB) DISPOSITION:

CR Number: [CR-YYYY-NNN]
CCB Meeting Date: [date]

DECISION: [APPROVED / APPROVED WITH CONDITIONS / DEFERRED / REJECTED]

If APPROVED:
- Selected alternative: [N]
- Conditions: [any conditions on implementation]
- Implementation deadline: [date]
- Budget authorized: [$]
- Implementation lead: [name]

If APPROVED WITH CONDITIONS:
- Conditions that must be met: [list]
- Conditions review date: [date]

If DEFERRED:
- Defer until: [date / milestone / condition]
- Reason: [why deferring]

If REJECTED:
- Reason: [why rejected]
- Alternatives suggested to requester: [if any]

SIGNATORIES:
| Name | Role | Vote | Date |
|------|------|------|------|
| [name] | [SE lead / PM / customer / QA / etc.] | [approve/reject/abstain] | [date] |
```

---

### Step 5: Implement Change with Traceability

```
CHANGE IMPLEMENTATION PLAN:

CR Number: [CR-YYYY-NNN]
Implementation Lead: [name]
Target Completion: [date]

AFFECTED CONFIGURATION ITEMS:
| CI | Current Version | New Version | Change Description | Owner |
|----|----------------|-------------|-------------------|-------|
| [document/code/HW] | [v1.X] | [v1.Y] | [what changes] | [who] |

IMPLEMENTATION TASKS:
| Task # | Description | Assigned To | Start | Complete | Dependencies | Status |
|--------|-------------|-------------|-------|----------|-------------|--------|
| T1 | [update requirements] | [name] | [date] | [date] | [none] | [OPEN] |
| T2 | [modify design] | [name] | [date] | [date] | [T1] | [OPEN] |
| T3 | [implement code/HW change] | [name] | [date] | [date] | [T2] | [OPEN] |
| T4 | [update test procedures] | [name] | [date] | [date] | [T2] | [OPEN] |
| T5 | [execute verification] | [name] | [date] | [date] | [T3, T4] | [OPEN] |
| T6 | [update documentation] | [name] | [date] | [date] | [T3] | [OPEN] |
| T7 | [update training] | [name] | [date] | [date] | [T6] | [OPEN] |

TRACEABILITY:
| Changed Item | Traced To (upstream) | Traced To (downstream) | Verification Method |
|-------------|---------------------|----------------------|---------------------|
| [requirement R-123] | [stakeholder need SN-45] | [design D-67, test TC-89] | [test / inspection / analysis] |
```

---

### Step 6: Verify Change Did Not Break Existing Functionality

```
CHANGE VERIFICATION:

REGRESSION ANALYSIS:
| Existing Function | Could Be Affected? | Regression Test | Result | Status |
|-------------------|--------------------|-----------------|---------|----|
| [function] | [Yes/No — why] | [test ID] | [PASS/FAIL/NOT RUN] | [OK/ISSUE] |

VERIFICATION MATRIX:
| Requirement | Verification Method | Expected Result | Actual Result | Status |
|-------------|--------------------|-----------------|--------------|----|
| [changed req] | [test/analysis/inspection/demo] | [expected] | [actual] | [PASS/FAIL] |
| [adjacent req] | [regression test] | [expected] | [actual] | [PASS/FAIL] |

INTERFACE VERIFICATION:
| Interface | Verified With | Method | Result | Status |
|-----------|--------------|--------|--------|----|
| [interface to system X] | [system X team] | [integration test] | [result] | [PASS/FAIL] |

VERIFICATION SUMMARY:
- All changed requirements verified: [Yes/No]
- Regression tests passed: [Yes/No — exceptions]
- Interface compatibility confirmed: [Yes/No — exceptions]
- Ready for baseline update: [Yes/No]
```

---

### Step 7: Update All Affected Documentation

```
DOCUMENTATION UPDATE CHECKLIST:

| Document | Version | Section(s) Changed | Updated By | Reviewed By | Date | Status |
|----------|---------|-------------------|------------|-------------|------|--------|
| System Requirements Spec | [ver] | [sections] | [name] | [name] | [date] | [DONE/PENDING] |
| Design Description | [ver] | [sections] | [name] | [name] | [date] | [status] |
| Interface Control Document | [ver] | [sections] | [name] | [name] | [date] | [status] |
| Test Procedures | [ver] | [sections] | [name] | [name] | [date] | [status] |
| User Manual | [ver] | [sections] | [name] | [name] | [date] | [status] |
| Training Materials | [ver] | [sections] | [name] | [name] | [date] | [status] |
| Traceability Matrix | [ver] | [rows] | [name] | [name] | [date] | [status] |

BASELINE UPDATE:
- Previous baseline: [name/version]
- New baseline: [name/version]
- Baseline date: [date]
- All CIs at consistent revision: [Yes/No]
```

---

## Output Format

```
## CHANGE IMPACT ASSESSMENT: [CR Number] — [Title]

### Change Request Summary
[What, why, who, priority]

### Impact Assessment
[Technical, schedule, cost, risk impacts]

### Alternatives Evaluation
[Options considered with comparison matrix]

### Recommendation
[Selected alternative with rationale]

### Implementation Plan
[Tasks, assignments, timeline, traceability]

### Verification Plan
[How to confirm change works and nothing broke]

### Documentation Updates Required
[List of affected documents and sections]

### Open Items
[Unresolved questions, pending information, risks to monitor]
```

---

## Quality Checklist

Before completing:
- [ ] Change request fully documented with rationale
- [ ] Impact assessed across all dimensions (technical, schedule, cost, risk)
- [ ] "Do nothing" alternative explicitly evaluated
- [ ] At least one alternative approach considered
- [ ] Alternatives compared using weighted criteria
- [ ] Clear recommendation with rationale
- [ ] All affected configuration items identified
- [ ] Implementation tasks defined with owners and dependencies
- [ ] Traceability maintained (upstream and downstream)
- [ ] Regression testing planned for affected functions
- [ ] All affected documentation identified for update
- [ ] CCB decision documented with signatories

---

## Next Steps

After change management:
1. Use `/configmgmt` to update configuration baselines
2. Use `/tracematrix` to verify traceability is maintained
3. Use `/vv` to plan verification of the changed functionality
4. Use `/riskmgmt` to track risks introduced by the change
5. Use `/testplan` to define regression test coverage
6. Use `/iface` to verify interface compatibility after changes
