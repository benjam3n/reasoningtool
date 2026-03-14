---
name: "selifecycle - Systems Engineering Lifecycle Management"
description: Plan and manage the overall SE process for a project. The meta-skill that orchestrates all other SE skills — selects lifecycle model, tailors processes, defines reviews, and creates the SE Management Plan (SEMP).
output:
  format: "table"
---

# Systems Engineering Lifecycle Management

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Create an SE Management Plan for a new project**: The user is starting a project and needs to plan the overall SE approach — lifecycle model, processes, reviews, activities, and skill application across phases.
**Interpretation 2 — Tailor SE processes to project characteristics**: The user has a project with specific constraints (small team, rapid timeline, regulatory environment, high risk) and needs to right-size the SE effort.
**Interpretation 3 — Assess SE process health on an ongoing project**: The user has a project underway and wants to evaluate whether the SE processes are effective, identify gaps, and course-correct.

If ambiguous, ask: "I can help with creating an SE plan for a new project, tailoring SE processes to your project, or assessing SE health on an ongoing project — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/selifecycle 4x [input]").

| Depth | Min Phases Defined | Min Reviews Planned | Min SE Activities | Min Exit Criteria | Min Skills Mapped |
|-------|-------------------|--------------------|--------------------|-------------------|-------------------|
| 1x    | 4                 | 3                  | 10                 | 8                 | 8                 |
| 2x    | 6                 | 5                  | 20                 | 15                | 15                |
| 4x    | 8                 | 7                  | 35                 | 25                | 20                |
| 8x    | 10                | 10                 | 50                 | 40                | 20                |
| 16x   | 12                | 12                 | 70                 | 60                | 20                |

---

## The Process

### Step 1: Characterize the Project

Understand the project to select and tailor the right approach:

```
PROJECT CHARACTERIZATION:

BASICS:
- Project name: [name]
- Domain: [defense / aerospace / automotive / medical / IT / industrial / consumer]
- System type: [hardware / software / mixed / SoS]
- Project size: [small (<10 people) / medium (10-50) / large (50-200) / very large (>200)]
- Duration: [months]
- Budget: [order of magnitude]

COMPLEXITY ASSESSMENT:
| Factor | Rating | Evidence |
|--------|--------|---------|
| Technical complexity | [LOW/MED/HIGH/VERY HIGH] | [novel technology, heritage, TRL levels] |
| Integration complexity | [LOW/MED/HIGH/VERY HIGH] | [number of interfaces, external systems] |
| Requirements stability | [STABLE/EVOLVING/VOLATILE] | [customer maturity, regulatory certainty] |
| Organizational complexity | [LOW/MED/HIGH] | [number of orgs, distributed teams, subcontractors] |
| Regulatory/compliance burden | [NONE/LOW/MED/HIGH] | [applicable standards, certification needed] |
| Safety criticality | [NONE/LOW/MED/HIGH] | [SIL/DAL/ASIL level] |

CONSTRAINTS:
- Schedule: [fixed deadline / flexible / event-driven]
- Budget: [fixed / flexible / phased]
- Technology readiness: [all mature / some immature / significant R&D]
- Workforce: [experienced / mixed / developing]
- Customer involvement: [heavy / moderate / minimal / adversarial]

APPLICABLE STANDARDS:
| Standard | Applicability | Tailoring Allowed? |
|----------|--------------|-------------------|
| [ISO/IEC 15288] | [full/partial] | [yes/no] |
| [MIL-STD-881] | [full/partial] | [yes/no] |
| [DO-178C / ISO 26262 / IEC 62304] | [full/partial] | [yes/no] |
| [customer-specific] | [full/partial] | [yes/no] |
```

---

### Step 2: Select Lifecycle Model

Choose and justify the lifecycle model:

```
LIFECYCLE MODEL SELECTION:

| Model | Fits Project? | Strengths for This Project | Weaknesses for This Project |
|-------|-------------|--------------------------|---------------------------|
| Waterfall (sequential) | [Yes/Partial/No] | [clear phases, documentation, contractual milestones] | [inflexible to change, late feedback] |
| Vee Model | [Yes/Partial/No] | [explicit V&V mapping, hardware-friendly] | [heavyweight, assumes stable requirements] |
| Spiral | [Yes/Partial/No] | [risk-driven, prototyping, uncertainty tolerance] | [complex to manage, requires risk expertise] |
| Incremental | [Yes/Partial/No] | [early delivery, phased capability, manageable scope] | [integration across increments, architecture must handle growth] |
| Agile / iterative | [Yes/Partial/No] | [rapid feedback, adaptive, collaborative] | [documentation gaps, regulatory challenges, HW constraints] |
| Hybrid | [Yes/Partial/No] | [best of multiple, tailored to subsystem needs] | [complexity, team must understand multiple models] |

SELECTED MODEL: [model]
RATIONALE: [why this model fits the project characterization]

LIFECYCLE PHASES:
| Phase | Purpose | Key Activities | Duration | Entry Criteria | Exit Criteria |
|-------|---------|---------------|----------|----------------|---------------|
| [Concept/Pre-MS A] | [explore needs, feasibility] | [ConOps, stakeholder analysis, feasibility] | [weeks/months] | [project authorization] | [concept approved] |
| [Development/Engineering] | [design the system] | [requirements, architecture, design] | [duration] | [concept approved] | [design reviewed] |
| [Implementation] | [build/code/fabricate] | [implementation, unit test] | [duration] | [design approved] | [built and unit tested] |
| [Integration & Test] | [assemble and verify] | [integration, system test, V&V] | [duration] | [components ready] | [verified system] |
| [Production/Deployment] | [produce and deliver] | [manufacturing, deployment, training] | [duration] | [system qualified] | [operational capability] |
| [Operations & Support] | [operate and maintain] | [operations, maintenance, upgrades] | [duration] | [deployed] | [end of life] |
| [Disposal] | [retire safely] | [decommission, data archival, disposal] | [duration] | [replacement ready] | [system retired] |
```

---

### Step 3: Define Technical Reviews and Decision Gates

```
TECHNICAL REVIEW PLAN:

| Review | Phase Boundary | Purpose | Key Questions Answered | Decision |
|--------|---------------|---------|----------------------|----------|
| SRR (System Requirements Review) | Concept -> Development | Are requirements complete, feasible, testable? | What must the system do? | Proceed to design |
| SFR (System Functional Review) | Functional analysis complete | Is the functional architecture sound? | How will functions be allocated? | Proceed to physical design |
| PDR (Preliminary Design Review) | Top-level design complete | Is the design approach sound? | Does the design meet requirements? | Proceed to detailed design |
| CDR (Critical Design Review) | Detailed design complete | Is the design ready to build? | Can we build this? | Proceed to implementation |
| TRR (Test Readiness Review) | Before system test | Is the system ready for formal testing? | Are test procedures and facilities ready? | Proceed to test |
| SVR (System Verification Review) | After system test | Has the system been verified? | Does it meet all requirements? | Proceed to validation |
| FCA/PCA (Functional/Physical Config Audit) | Before production | Does the product match its documentation? | Is the baseline consistent? | Authorize production |
| PRR (Production Readiness Review) | Before production | Can we produce at rate? | Are manufacturing processes ready? | Begin production |

REVIEW DETAILS (for each review):
| Element | Description |
|---------|-------------|
| Entrance criteria | [what must be true to hold this review] |
| Required attendees | [roles that must participate] |
| Required artifacts | [documents/data/demos needed] |
| Success criteria | [what constitutes passing] |
| Exit criteria | [what must be true to proceed] |
| Action item process | [how RIDs/action items are tracked] |
```

---

### Step 4: Plan SE Activities Across Phases

```
SE ACTIVITY PLAN:

| SE Activity | Concept | Development | Implementation | Integration & Test | Production | Operations |
|-------------|---------|-------------|----------------|-------------------|------------|------------|
| Requirements engineering | PRIMARY | Refine | Manage changes | Verify | — | Manage changes |
| Stakeholder analysis | PRIMARY | Update | — | — | — | Feedback |
| ConOps development | PRIMARY | Refine | — | Validate against | — | — |
| Architecture design | Start | PRIMARY | — | — | — | — |
| Functional analysis | Start | PRIMARY | — | — | — | — |
| Interface management | Identify | PRIMARY | Implement | Verify | — | Manage |
| Trade studies | PRIMARY | As needed | — | — | — | — |
| Risk management | Start | PRIMARY | Continue | Continue | Continue | Continue |
| V&V planning | Start | PRIMARY | — | Execute | — | — |
| Configuration mgmt | Establish | PRIMARY | Continue | Continue | Continue | Continue |
| Test planning | — | PRIMARY | Refine | Execute | — | — |
| System integration | — | Plan | — | PRIMARY | — | — |
| RAM analysis | Start | PRIMARY | — | Verify | Monitor | Monitor |
| HSI | Start | PRIMARY | — | Evaluate | — | Feedback |
| Change management | Establish | Continue | Continue | Continue | Continue | Continue |
| Technical performance | Define | Track | Track | Assess | Track | Track |
| Lifecycle cost | Estimate | Refine | Track | Assess | Track | Track |

PRIMARY = Main phase for this activity
```

---

### Step 5: Map SE Skills to Lifecycle Phases

Master table mapping all SE skills to when they are most relevant:

```
SE SKILL-TO-PHASE MAPPING:

| Skill | Command | Concept | Development | Implementation | I&T | Production | Operations | Disposal |
|-------|---------|---------|-------------|----------------|-----|------------|------------|----------|
| Requirements | /requirements | ★★★ | ★★ | ★ | ★ | — | ★ | — |
| ConOps | /conops | ★★★ | ★★ | — | ★ | — | ★ | — |
| Stakeholder Analysis | /stakeholder | ★★★ | ★ | — | — | — | ★ | — |
| System Architecture | /sysarch | ★★ | ★★★ | — | — | — | — | — |
| Functional Analysis | /funcanalysis | ★★ | ★★★ | — | — | — | — | — |
| Trade Studies | /tradestudy | ★★★ | ★★ | ★ | — | — | — | — |
| Interface Mgmt | /iface | ★ | ★★★ | ★★ | ★★ | — | ★ | — |
| V&V | /vv | ★ | ★★★ | ★ | ★★★ | — | — | — |
| Risk Management | /riskmgmt | ★★ | ★★★ | ★★ | ★★ | ★ | ★ | ★ |
| System Integration | /sysintegration | — | ★★ | ★ | ★★★ | ★ | — | — |
| Configuration Mgmt | /configmgmt | ★ | ★★ | ★★★ | ★★ | ★★ | ★★ | ★ |
| Test Planning | /testplan | — | ★★★ | ★ | ★★★ | ★ | — | — |
| System Decomposition | /sysdecomp | ★★ | ★★★ | — | — | — | — | — |
| Traceability Matrix | /tracematrix | ★ | ★★★ | ★★ | ★★★ | ★ | ★ | — |
| Lifecycle Cost | /lcca | ★★★ | ★★ | ★ | ★ | ★ | ★★ | ★★ |
| Technical Performance | /tpm | ★ | ★★★ | ★★ | ★★★ | ★ | ★ | — |
| RAM Analysis | /ram | ★★ | ★★★ | ★ | ★★ | ★ | ★★ | — |
| Human Systems Integration | /hsi | ★★ | ★★★ | ★ | ★★ | ★ | ★ | — |
| Change Management | /changemgmt | ★ | ★★ | ★★★ | ★★ | ★★ | ★★ | ★ |
| System of Systems | /sos | ★★★ | ★★ | — | ★★ | — | ★ | — |

★★★ = Primary phase (most effort here)
★★ = Significant activity
★ = Light activity or updates
— = Typically not active

SKILL SEQUENCING GUIDANCE:
- Start with: /stakeholder -> /conops -> /requirements
- Then: /sysarch -> /funcanalysis -> /sysdecomp
- In parallel: /tradestudy, /riskmgmt, /ram, /hsi
- Define: /iface, /vv, /testplan, /tracematrix
- Throughout: /configmgmt, /changemgmt, /tpm
- At SoS level: /sos before or alongside /sysarch
- For planning: /lcca at concept, refine throughout
- This skill (/selifecycle): at project start, revisit at each phase gate
```

---

### Step 6: Define Entrance and Exit Criteria

```
PHASE GATE CRITERIA:

CONCEPT PHASE EXIT / DEVELOPMENT PHASE ENTRANCE:
| Criterion | Evidence | Status |
|-----------|---------|--------|
| Stakeholder needs documented | Stakeholder analysis report | [MET/NOT MET/PARTIAL] |
| ConOps approved | ConOps document signed | [status] |
| System requirements baselined | Requirements spec v1.0 | [status] |
| Feasibility confirmed | Trade study results, prototyping | [status] |
| Top risks identified | Risk register initiated | [status] |
| Lifecycle cost estimated | ROM cost estimate | [status] |
| SEMP approved | This document | [status] |

DEVELOPMENT PHASE EXIT / IMPLEMENTATION ENTRANCE:
| Criterion | Evidence | Status |
|-----------|---------|--------|
| CDR completed successfully | CDR minutes, action items closed | [status] |
| All requirements allocated to design | Traceability matrix | [status] |
| Interfaces defined | ICDs baselined | [status] |
| Test plans approved | System test plan | [status] |
| RAM predictions meet requirements | RAM analysis report | [status] |
| Risks mitigated or accepted | Risk register current | [status] |

INTEGRATION & TEST EXIT / PRODUCTION ENTRANCE:
| Criterion | Evidence | Status |
|-----------|---------|--------|
| All verification complete | Verification cross-reference matrix | [status] |
| All test discrepancies resolved | Test deficiency reports closed | [status] |
| FCA/PCA complete | Audit reports | [status] |
| Configuration baseline established | CM records | [status] |
| Training materials ready | Training package | [status] |
| Support infrastructure ready | Maintenance plan, spares | [status] |
```

---

### Step 7: Create SE Management Plan (SEMP) Outline

```
SYSTEMS ENGINEERING MANAGEMENT PLAN (SEMP):

1. INTRODUCTION
   1.1 Purpose
   1.2 Scope
   1.3 Applicable documents and standards

2. SE ORGANIZATION AND RESPONSIBILITIES
   2.1 SE team structure
   2.2 Roles and responsibilities
   2.3 Interfaces with program management, engineering, customer

3. LIFECYCLE MODEL
   3.1 Selected model and rationale (from Step 2)
   3.2 Phase definitions
   3.3 Phase durations and milestones

4. TECHNICAL PROCESSES
   4.1 Requirements engineering process
   4.2 Architecture and design process
   4.3 Interface management process
   4.4 Integration process
   4.5 Verification and validation process
   4.6 Transition/deployment process

5. TECHNICAL MANAGEMENT PROCESSES
   5.1 Decision analysis / trade studies
   5.2 Technical risk management
   5.3 Configuration management
   5.4 Change management
   5.5 Technical performance measurement
   5.6 Technical data management

6. TECHNICAL REVIEWS
   6.1 Review schedule (from Step 3)
   6.2 Review procedures
   6.3 Entrance and exit criteria (from Step 6)
   6.4 Action item tracking

7. SE SCHEDULE AND MILESTONES
   7.1 SE activity timeline (from Step 4)
   7.2 Deliverables schedule
   7.3 Dependencies and critical path

8. SE RESOURCE PLAN
   8.1 Staffing (SE roles, FTEs by phase)
   8.2 Tools (modeling, requirements mgmt, CM, test)
   8.3 Facilities (labs, test ranges, integration areas)
   8.4 Budget allocation across SE activities

9. TAILORING RATIONALE
   9.1 Standards tailored and justification
   9.2 Processes scaled and justification
   9.3 Reviews adjusted and justification

APPENDICES:
A. SE Skill-to-Phase Mapping (from Step 5)
B. Entrance/Exit Criteria Details (from Step 6)
C. Acronyms and Definitions
```

---

## Output Format

```
## SE MANAGEMENT PLAN: [Project Name]

### Project Characterization
[Domain, size, complexity, constraints, standards]

### Lifecycle Model
[Selected model with rationale, phase definitions]

### Technical Review Plan
[Reviews, gates, entrance/exit criteria]

### SE Activity Plan
[Activities mapped to phases with primary/secondary indicators]

### SE Skill Mapping
[Master table of all SE skills to phases]

### Phase Gate Criteria
[Entrance and exit criteria for each phase transition]

### SEMP Outline
[Structured outline ready for expansion into full document]

### Tailoring Decisions
[What was scaled up/down and why]

### Open Items
[Decisions pending, resources TBD, stakeholder approvals needed]
```

---

## Quality Checklist

Before completing:
- [ ] Project characterized (domain, size, complexity, constraints)
- [ ] Lifecycle model selected with rationale
- [ ] Lifecycle model appropriate to requirements stability and risk
- [ ] All phases defined with purpose and key activities
- [ ] Technical reviews planned with entrance/exit criteria
- [ ] SE activities mapped across all phases
- [ ] All 20 SE skills mapped to lifecycle phases
- [ ] Skill sequencing guidance provided
- [ ] Phase gate criteria are specific and verifiable
- [ ] SEMP outline addresses all required sections
- [ ] Tailoring decisions documented with rationale
- [ ] SE resource needs identified (people, tools, facilities)

---

## Next Steps

After creating the SEMP:
1. Use `/stakeholder` to identify all project stakeholders
2. Use `/conops` to develop the operational concept
3. Use `/requirements` to begin requirements engineering
4. Use `/riskmgmt` to establish the project risk register
5. Use `/configmgmt` to establish configuration management
6. Use `/lcca` to develop the lifecycle cost estimate
7. Use each mapped skill (`/sysarch`, `/funcanalysis`, `/tradestudy`, etc.) as the project enters the relevant phase
