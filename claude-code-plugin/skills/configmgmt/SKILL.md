---
name: "configmgmt - Configuration Management"
description: Establish and maintain consistency of system attributes with requirements and design throughout the lifecycle. Produces a CM plan with configuration item identification, baselines, change control procedures, status accounting, and audit planning.
output:
  format: "table"
---

# Configuration Management

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Establish a CM plan for a new project or system**: The user is starting a project and wants to set up configuration management from scratch — identifying what to control, defining baselines, and establishing change control processes.
**Interpretation 2 — Audit or improve existing CM practices**: The user has a system with some configuration management and wants to assess gaps, tighten controls, or recover from configuration drift.
**Interpretation 3 — Define change control for a specific change or set of changes**: The user has a proposed change to a baselined system and wants to process it through formal change control — impact analysis, approval, implementation, and verification.

If ambiguous, ask: "I can help with setting up CM for a new project, auditing existing CM practices, or processing a specific change through change control — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/configmgmt 4x [input]").

| Depth | Min Config Items | Min Baselines | Min Change Control Steps | Min Audit Checks |
|-------|-----------------|--------------|------------------------|-----------------|
| 1x    | 10              | 2            | 4                      | 5               |
| 2x    | 25              | 3            | 6                      | 10              |
| 4x    | 50              | 4            | 8                      | 15              |
| 8x    | 80              | 5            | 10                     | 20              |
| 16x   | 120             | 6            | 12                     | 30              |

---

## The Process

### Step 1: Configuration Item Identification

Identify everything that needs to be managed:

```
CONFIGURATION ITEM (CI) REGISTRY:

| CI ID | Name | Type | Description | Owner | Criticality | Controlled? |
|-------|------|------|-------------|-------|-------------|-------------|
| CI-001 | [name] | HW/SW/DOC/DATA/TOOL/IF | [what it is] | [person/team] | HIGH/MED/LOW | YES/NO |
| CI-002 | [name] | HW/SW/DOC/DATA/TOOL/IF | [what it is] | [person/team] | HIGH/MED/LOW | YES/NO |
...

CI TYPES:
- HW: Hardware items (boards, assemblies, components, FPGA/ASIC)
- SW: Software items (source code, executables, libraries, scripts, configs)
- DOC: Documents (requirements, design, test procedures, user manuals)
- DATA: Data items (databases, calibration data, test data, models)
- TOOL: Tools (compilers, test equipment, development tools)
- IF: Interface specifications (ICDs, API definitions, protocols)

CI SELECTION CRITERIA:
| Criterion | Include as CI? |
|-----------|---------------|
| Delivered to customer | YES |
| Required for system operation | YES |
| Required to reproduce/rebuild | YES |
| Subject to regulatory oversight | YES |
| Shared across teams or components | YES |
| Likely to change during lifecycle | YES |
| Single-use or disposable | Probably NO |
| Commercially available, unmodified | NO (track version only) |

CI HIERARCHY:
[System]
├── [Subsystem A]
│   ├── CI-001: [component]
│   ├── CI-002: [component]
│   └── CI-003: [software module]
├── [Subsystem B]
│   ├── CI-004: [component]
│   └── CI-005: [software module]
├── [Documentation]
│   ├── CI-006: [requirements spec]
│   ├── CI-007: [design document]
│   └── CI-008: [test procedures]
└── [Interfaces]
    ├── CI-009: [ICD A-B]
    └── CI-010: [external API spec]
```

---

### Step 2: Baseline Establishment

Define the configuration baselines:

```
BASELINES:

| Baseline | Name | Contents | Established When | Authority | Purpose |
|----------|------|----------|-----------------|-----------|---------|
| B-001 | Functional Baseline | Requirements, ConOps | After requirements review | [authority] | Defines WHAT the system must do |
| B-002 | Allocated Baseline | Architecture, interface specs | After design review | [authority] | Defines HOW requirements are allocated |
| B-003 | Product Baseline | As-built design, test results | After acceptance | [authority] | Defines WHAT was delivered |
| B-004 | Operational Baseline | Deployed config, runtime params | After deployment | [authority] | Defines WHAT is running |
...

BASELINE CONTENT MAPPING:
| CI ID | Functional BL | Allocated BL | Product BL | Operational BL |
|-------|-------------|-------------|-----------|---------------|
| CI-001 | — | v1.0 | v1.2 | v1.2 |
| CI-002 | — | v2.0 | v2.1 | v2.1 |
| CI-006 | v1.0 | v1.0 | v1.3 | v1.3 |
...

BASELINE RULES:
- No CI in a baseline may be changed without formal change control
- Each baseline is a snapshot — versions of all CIs at a point in time
- Baselines are cumulative — each includes all prior baseline content plus additions
- Baselines must be reproducible — given a baseline ID, you can reconstruct the exact configuration
```

---

### Step 3: Change Control Process

Define how changes are proposed, evaluated, approved, and implemented:

```
CHANGE CONTROL PROCESS:

CHANGE REQUEST (CR) TEMPLATE:
| Field | Description |
|-------|-------------|
| CR ID | [auto-generated unique ID] |
| Title | [short description of change] |
| Requestor | [who is requesting] |
| Date | [date submitted] |
| Priority | EMERGENCY/HIGH/MEDIUM/LOW |
| CIs Affected | [list of CI IDs] |
| Baselines Affected | [list of baseline IDs] |
| Description | [detailed description of the change] |
| Justification | [why the change is needed] |
| Impact Analysis | [see below] |
| Risk Assessment | [risks introduced by the change] |
| Estimated Effort | [hours/days/weeks] |
| Estimated Cost | [cost] |

IMPACT ANALYSIS TEMPLATE:
| Impact Area | Assessment | Details |
|-------------|-----------|---------|
| Requirements | NONE/MINOR/MAJOR | [which requirements affected] |
| Design | NONE/MINOR/MAJOR | [which design elements affected] |
| Interfaces | NONE/MINOR/MAJOR | [which interfaces affected] |
| Test | NONE/MINOR/MAJOR | [which tests need updating] |
| Documentation | NONE/MINOR/MAJOR | [which docs need updating] |
| Schedule | NONE/MINOR/MAJOR | [schedule impact] |
| Cost | NONE/MINOR/MAJOR | [cost impact] |
| Other CIs | NONE/MINOR/MAJOR | [ripple effects to other CIs] |

CHANGE CONTROL WORKFLOW:
| Step | Activity | Responsible | Output |
|------|----------|------------|--------|
| 1 | Submit CR | Requestor | CR form submitted |
| 2 | Log and classify | CM Manager | CR logged, priority assigned |
| 3 | Impact analysis | Engineering lead | Impact assessment completed |
| 4 | Review and disposition | Change Control Board (CCB) | APPROVED/REJECTED/DEFERRED |
| 5 | Plan implementation | Assigned engineer | Implementation plan |
| 6 | Implement change | Assigned engineer | CIs modified |
| 7 | Verify change | V&V team | Test results |
| 8 | Update baseline | CM Manager | Baseline updated |
| 9 | Close CR | CM Manager | CR closed, status accounting updated |

CHANGE CONTROL BOARD (CCB):
| Role | Responsibility | Authority |
|------|---------------|-----------|
| Chair | Run CCB meetings, final disposition | Approve/reject changes |
| Systems Engineering | Technical impact assessment | Recommend disposition |
| Project Management | Schedule and cost impact | Recommend disposition |
| Quality Assurance | Process compliance | Recommend disposition |
| Test Engineering | Test impact assessment | Recommend disposition |
| Customer Representative | Requirements alignment | Concurrence required for requirement changes |

CHANGE CLASSIFICATION:
| Class | Description | Approval Authority | Process |
|-------|-------------|-------------------|---------|
| Class I | Affects form, fit, function, or interfaces | Full CCB | Formal CR with full impact analysis |
| Class II | Does not affect form, fit, function, or interfaces | Engineering lead | Abbreviated CR |
| Emergency | Critical operational or safety issue | CCB Chair (post-hoc CCB ratification) | Expedited CR |
```

---

### Step 4: Configuration Status Accounting

Track the status of all CIs and changes:

```
CONFIGURATION STATUS ACCOUNTING:

CI STATUS REPORT:
| CI ID | Name | Current Version | Baseline | Last Change | CR ID | Status |
|-------|------|----------------|----------|------------|-------|--------|
| CI-001 | [name] | [version] | [baseline ID] | [date] | CR-XXX | CURRENT/SUPERSEDED/WITHDRAWN |
...

CHANGE REQUEST STATUS:
| CR ID | Title | Status | Priority | Submitted | Approved | Implemented | Verified | Closed |
|-------|-------|--------|----------|-----------|----------|-------------|----------|--------|
| CR-001 | [title] | SUBMITTED/ANALYZING/APPROVED/IMPLEMENTING/VERIFYING/CLOSED/REJECTED | [priority] | [date] | [date] | [date] | [date] | [date] |
...

CONFIGURATION STATUS METRICS:
| Metric | Value | Trend | Target |
|--------|-------|-------|--------|
| Total CIs under control | [N] | [↑↓→] | Stable after baseline |
| Open CRs | [N] | [↑↓→] | Decreasing over time |
| CR cycle time (avg) | [days] | [↑↓→] | Per SLA |
| Overdue CRs | [N] | [↑↓→] | 0 |
| Baseline currency | [% CIs at latest version] | [↑↓→] | 100% |
| Unauthorized changes detected | [N] | [↑↓→] | 0 |

VERSION HISTORY:
| CI ID | Version | Date | CR ID | Description of Change | Author |
|-------|---------|------|-------|----------------------|--------|
| CI-001 | 1.0 | [date] | — | Initial baseline | [author] |
| CI-001 | 1.1 | [date] | CR-005 | [change description] | [author] |
| CI-001 | 1.2 | [date] | CR-012 | [change description] | [author] |
...
```

---

### Step 5: Configuration Audits

Plan audits to verify configuration integrity:

```
CONFIGURATION AUDITS:

AUDIT TYPES:
| Audit | Purpose | When | Scope |
|-------|---------|------|-------|
| Functional Configuration Audit (FCA) | Verify CIs meet requirements | Before product baseline | All functional/performance requirements vs test results |
| Physical Configuration Audit (PCA) | Verify as-built matches as-designed | Before product baseline | Design docs vs actual product |
| Configuration Verification | Verify CM process compliance | Periodic | CM procedures, baselines, change records |
| Deployment Audit | Verify deployed config matches baseline | After deployment | Operational system vs product baseline |

FCA CHECKLIST:
| Check | Status | Evidence |
|-------|--------|---------|
| Every requirement has a verification record | PASS/FAIL/N/A | [test report reference] |
| All verification results are current (not outdated by changes) | PASS/FAIL/N/A | [version check] |
| All waivers and deviations are documented and approved | PASS/FAIL/N/A | [waiver records] |
| All open defects are documented with disposition | PASS/FAIL/N/A | [defect tracker] |

PCA CHECKLIST:
| Check | Status | Evidence |
|-------|--------|---------|
| As-built matches design documents | PASS/FAIL/N/A | [comparison record] |
| All changes reflected in documentation | PASS/FAIL/N/A | [CR records] |
| Part numbers and versions match BOM | PASS/FAIL/N/A | [inspection record] |
| Build/manufacturing instructions are sufficient to reproduce | PASS/FAIL/N/A | [build record] |

AUDIT SCHEDULE:
| Audit | Planned Date | Scope | Auditor | Status |
|-------|-------------|-------|---------|--------|
| FCA | [date] | [scope] | [who] | PLANNED/IN PROGRESS/COMPLETE |
| PCA | [date] | [scope] | [who] | PLANNED/IN PROGRESS/COMPLETE |
...

AUDIT FINDINGS:
| Finding ID | Audit | Severity | Description | Corrective Action | Due Date | Status |
|-----------|-------|----------|-------------|-------------------|----------|--------|
| AF-001 | [audit] | MAJOR/MINOR/OBSERVATION | [what was found] | [what to do] | [date] | OPEN/IN PROGRESS/CLOSED |
...
```

---

## Output Format

```
## CONFIGURATION MANAGEMENT PLAN: [System/Project Name]

### Document Control
Version: [X.Y]
Date: [date]
Status: [DRAFT/REVIEW/APPROVED]

### Configuration Item Registry
[Complete CI inventory with types, owners, criticality]

### CI Hierarchy
[Tree structure showing CI relationships]

### Baselines
[Baseline definitions, content, and establishment criteria]

### Change Control Process
[CR template, impact analysis template, workflow, CCB composition, change classification]

### Configuration Status Accounting
[Status tracking templates, metrics, version history format]

### Configuration Audits
[Audit types, checklists, schedule]

### Tools and Infrastructure
[CM tools, repositories, access controls]

### Roles and Responsibilities
[CM roles, authorities, training requirements]

### Open Items
[Pending CI identification, tool decisions, process gaps]
```

---

## Quality Checklist

Before completing:
- [ ] All deliverable items identified as CIs
- [ ] CI selection criteria applied consistently
- [ ] CI hierarchy reflects system architecture
- [ ] Baselines defined for each lifecycle phase
- [ ] Baseline content fully mapped to CIs
- [ ] Change control process covers all change types (Class I, Class II, Emergency)
- [ ] Impact analysis template covers all relevant areas
- [ ] CCB composition defined with clear authorities
- [ ] Status accounting tracks CI versions, CRs, and baseline currency
- [ ] Audit types, checklists, and schedule defined
- [ ] No CIs under control lack an identified owner
- [ ] Unauthorized change detection mechanism exists

---

## Next Steps

After configuration management planning:
1. Use `/requirements` to ensure all requirements are captured as CIs
2. Use `/iface` to identify interface specifications that need configuration control
3. Use `/vv` to align V&V artifacts with CM baselines
4. Use `/riskmgmt` to assess risks of configuration drift or unauthorized changes
5. Use `/sysintegration` to coordinate CI versions during integration
6. Use `/de` to map dependencies between configuration items
