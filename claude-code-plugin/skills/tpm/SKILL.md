---
name: "tpm - Technical Performance Measures"
description: Define and track key technical metrics that indicate whether the system is on track to meet requirements. Sets planned profiles, tolerance bands, measurement methods, and escalation thresholds.
output:
  format: "table"
---

# Technical Performance Measures

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Define TPMs for a new system**: The user has a system under development and needs to identify critical technical parameters, set target profiles, and establish a tracking framework to provide early warning of requirement shortfalls.
**Interpretation 2 — Assess TPM status for an existing program**: The user has a system in development or operations and wants to evaluate current technical performance against planned values to determine if corrective action is needed.
**Interpretation 3 — Create TPM reporting for a review or milestone**: The user needs to prepare TPM status reporting for a program review, design review, or milestone decision and wants a structured dashboard with trends and risk assessment.

If ambiguous, ask: "I can help with defining TPMs for a new system, assessing current TPM status, or creating TPM reporting for a milestone review — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/tpm 4x [input]").

| Depth | Min TPMs Defined | Min Assessment Points | Min Risk Indicators | Min Measurement Methods | Min Reporting Elements |
|-------|-----------------|----------------------|--------------------|-----------------------|----------------------|
| 1x    | 3               | 2                    | 2                  | 3                     | 1                    |
| 2x    | 6               | 4                    | 4                  | 6                     | 2                    |
| 4x    | 12              | 6                    | 8                  | 12                    | 3                    |
| 8x    | 20              | 8                    | 12                 | 20                    | 4                    |
| 16x   | 30              | 12                   | 20                 | 30                    | 5                    |

---

## The Process

### Step 1: Identify Critical Technical Parameters

Select the technical parameters that are most important to system success. Focus on parameters that:
- Are tied to key requirements
- Have significant technical risk
- Drive design decisions
- Are difficult to achieve
- Have history of problems on similar systems

```
CRITICAL PARAMETER SELECTION:

| # | Parameter | Unit | Linked Requirement | Why Critical | Risk Level |
|---|-----------|------|--------------------|-------------|------------|
| 1 | [e.g., system response time] | [ms] | [REQ-001] | [drives user satisfaction, architecturally significant] | HIGH/MED/LOW |
| 2 | [e.g., weight] | [kg] | [REQ-015] | [constrained by platform, hard to reduce later] | HIGH/MED/LOW |
| 3 | [e.g., mean time between failures] | [hours] | [REQ-022] | [reliability requirement, expensive to fix late] | HIGH/MED/LOW |
| 4 | [e.g., throughput] | [tx/sec] | [REQ-008] | [scalability driver, architecture dependent] | HIGH/MED/LOW |
| 5 | [e.g., power consumption] | [watts] | [REQ-030] | [thermal/battery constraint] | HIGH/MED/LOW |
| 6 | [e.g., data accuracy] | [%] | [REQ-011] | [core mission capability] | HIGH/MED/LOW |
...
```

Selection criteria checklist:

| Criterion | Question | Apply? |
|-----------|----------|--------|
| **Requirement linkage** | Is this parameter directly tied to a key requirement? | |
| **Technical risk** | Is there significant uncertainty in achieving this value? | |
| **Design driver** | Does this parameter drive major design decisions? | |
| **Integration sensitivity** | Does this degrade when components are integrated? | |
| **Cost sensitivity** | Would failure to meet this drive significant rework cost? | |
| **Schedule sensitivity** | Would late discovery of shortfall impact schedule? | |
| **Stakeholder visibility** | Do stakeholders specifically ask about this parameter? | |

---

### Step 2: Set Planned Value Profiles

For each TPM, define the expected trajectory over the development timeline:

```
TPM PLANNED PROFILE: [Parameter Name]

Requirement threshold: [value] [unit] (MUST achieve)
Requirement objective: [value] [unit] (GOAL to achieve)
Current best estimate: [value] [unit]

| Milestone | Date | Planned Value | Tolerance Band (+/-) | Basis |
|-----------|------|--------------|--------------------| ------|
| System Requirements Review (SRR) | [date] | [value] | +/-[value] | Engineering estimate, analogy |
| Preliminary Design Review (PDR) | [date] | [value] | +/-[value] | Analysis, modeling |
| Critical Design Review (CDR) | [date] | [value] | +/-[value] | Detailed design analysis |
| Test Readiness Review (TRR) | [date] | [value] | +/-[value] | Component test data |
| System Verification Review (SVR) | [date] | [value] | +/-[value] | System test data |
| Operational Test | [date] | [value] | +/-[value] | Measured performance |
| Full Rate Production | [date] | [value] | +/-[value] | Production unit data |

PROFILE SHAPE:
- Tolerance band narrows as design matures and test data replaces estimates
- Planned value may shift as design evolves (within requirement threshold)
- Achievement curve should converge toward requirement threshold/objective
```

Planned value profile table for all TPMs:

| TPM | Unit | Requirement | SRR Est. | PDR Est. | CDR Est. | TRR Measured | SVR Measured | Status |
|-----|------|-------------|----------|----------|----------|-------------|-------------|--------|
| [param 1] | [unit] | [threshold] | [value+/-tol] | [value+/-tol] | [value+/-tol] | [value+/-tol] | [value+/-tol] | ON TRACK / AT RISK / BREACH |
| [param 2] | [unit] | [threshold] | [value+/-tol] | [value+/-tol] | [value+/-tol] | [value+/-tol] | [value+/-tol] | ON TRACK / AT RISK / BREACH |
...

---

### Step 3: Define Current Estimates and Tolerance Bands

For each TPM at the current point in time:

```
CURRENT TPM STATUS:

| TPM | Requirement | Planned Value (now) | Current Estimate | Margin | Tolerance Band | Status |
|-----|-------------|--------------------|-----------------|---------| --------------|--------|
| [param 1] | <= [threshold] | [planned] | [current] | [planned - current] | +/-[tol] | GREEN / YELLOW / RED |
| [param 2] | >= [threshold] | [planned] | [current] | [current - planned] | +/-[tol] | GREEN / YELLOW / RED |
...

STATUS DEFINITIONS:

| Status | Meaning | Condition |
|--------|---------|-----------|
| GREEN | On track | Current estimate within tolerance band of planned value |
| YELLOW | At risk | Current estimate outside tolerance band but within requirement threshold |
| RED | Breach | Current estimate does not meet requirement threshold |

MARGIN DEFINITIONS:

| Margin Type | Calculation | Purpose |
|------------|-------------|---------|
| Design margin | Requirement threshold - current best estimate | How much room remains |
| Margin consumption rate | Margin lost per time period | Trend indicator |
| Required margin at this milestone | Planned value - requirement threshold | Expected margin at this point |
| Margin ratio | Actual margin / Required margin | >1.0 is healthy, <1.0 is concerning |
```

---

### Step 4: Establish Measurement Methods

Define how each TPM will be measured at each lifecycle stage:

```
MEASUREMENT METHODS:

| TPM | Lifecycle Stage | Measurement Method | Data Source | Accuracy | Frequency |
|-----|----------------|-------------------|-------------|----------|-----------|
| [param 1] | Concept | Engineering estimate | Similar system data | +/-50% | Once |
| [param 1] | Design | Analysis/modeling | Simulation results | +/-25% | Per design iteration |
| [param 1] | Development | Component test | Lab measurement | +/-10% | Per test event |
| [param 1] | Integration | System test | Integrated test | +/-5% | Per integration build |
| [param 1] | Operations | Field measurement | Operational data | +/-2% | Continuous |
...

MEASUREMENT MATURITY LEVELS:

| Level | Source | Typical Accuracy | Confidence |
|-------|--------|-----------------|------------|
| 1 | Expert opinion / rough analogy | +/-50% | LOW |
| 2 | Parametric model / detailed analogy | +/-30% | LOW-MED |
| 3 | Engineering analysis / simulation | +/-20% | MEDIUM |
| 4 | Component or subsystem test data | +/-10% | MED-HIGH |
| 5 | System-level test data | +/-5% | HIGH |
| 6 | Operational measurement data | +/-2% | VERY HIGH |
```

---

### Step 5: Define Reporting and Escalation Thresholds

```
ESCALATION FRAMEWORK:

| Threshold | Condition | Action Required | Escalation To |
|-----------|-----------|----------------|---------------|
| WATCH | Margin consumption rate increasing | Monitor more frequently, investigate root cause | Technical lead |
| WARNING | Current estimate within [X]% of tolerance band edge | Root cause analysis, identify corrective actions | Project manager |
| ACTION | Current estimate outside tolerance band (YELLOW) | Implement corrective action plan, report to management | Program manager |
| BREACH | Current estimate violates requirement threshold (RED) | Formal corrective action, requirement re-negotiation or redesign | Sponsor / customer |

REPORTING CADENCE:

| Report Type | Audience | Frequency | Content |
|-------------|----------|-----------|---------|
| TPM Dashboard | Project team | Weekly/Bi-weekly | All TPM status, trends, margin |
| TPM Summary | Program management | Monthly | Status changes, escalations, actions |
| TPM Detail | Design review board | Per milestone | Full profile history, measurement data, forecasts |
| TPM Alert | Management chain | As needed (on threshold breach) | Specific TPM, impact, corrective action plan |

CORRECTIVE ACTION TEMPLATE:

| Field | Content |
|-------|---------|
| TPM affected | [parameter name] |
| Current status | [RED/YELLOW] |
| Requirement threshold | [value] |
| Current estimate | [value] |
| Shortfall | [delta] |
| Root cause | [analysis] |
| Corrective actions | 1. [action, owner, due date] 2. [action, owner, due date] |
| Expected result | [estimated value after correction] |
| Fallback plan | [if corrective action fails] |
| Decision needed by | [date] |
```

---

### Step 6: Track Actuals vs Planned

Create the tracking dashboard:

```
TPM TRACKING DASHBOARD:

Date: [current date]
Program phase: [current phase]
Next milestone: [milestone name, date]

SUMMARY:
  Total TPMs tracked: [N]
  GREEN (on track): [N]
  YELLOW (at risk): [N]
  RED (breached): [N]

DETAILED STATUS:

| TPM | Req | Planned | Current | Margin | Trend | Status | Action |
|-----|-----|---------|---------|--------|-------|--------|--------|
| [param 1] | [val] | [val] | [val] | [val] | up/stable/down | GREEN | None |
| [param 2] | [val] | [val] | [val] | [val] | down | YELLOW | [CAP-001] |
| [param 3] | [val] | [val] | [val] | [val] | down | RED | [CAP-002] |
...

TREND HISTORY:

TPM: [parameter name]
| Date | Planned | Actual/Estimate | Margin | Measurement Level | Notes |
|------|---------|----------------|--------|-------------------|-------|
| [date 1] | [value] | [value] | [value] | 1-Expert | Initial estimate |
| [date 2] | [value] | [value] | [value] | 2-Parametric | Updated with model |
| [date 3] | [value] | [value] | [value] | 3-Analysis | PDR analysis |
| [date 4] | [value] | [value] | [value] | 4-Component test | First test data |
| [date 5] | [value] | [value] | [value] | 5-System test | Integration result |

MARGIN BURNDOWN:
  Starting margin (SRR): [value]
  Current margin: [value]
  Margin consumed: [value] ([%])
  Margin consumption rate: [value per month]
  Projected margin at IOC: [value] -- SUFFICIENT / INSUFFICIENT
```

---

## Output Format

```
## TPM TRACKING PLAN: [System Name]

### Critical Technical Parameters
[Table of selected TPMs with justification]

### Planned Value Profiles
[For each TPM: requirement, planned trajectory, tolerance bands]

### Current Status Dashboard
  GREEN: [N] | YELLOW: [N] | RED: [N]
[Detailed status table with margin and trend]

### Measurement Plan
[Table of methods per TPM per lifecycle stage]

### Escalation Framework
[Thresholds, actions, reporting cadence]

### Active Corrective Actions
[Any current YELLOW/RED items with action plans]

### Trend History
[Historical tracking data for each TPM]

### Risk Assessment
[TPMs most likely to breach, mitigation strategies]
```

---

## Quality Checklist

Before completing:
- [ ] TPMs linked to specific requirements
- [ ] Only critical parameters selected (not everything -- typically 6-15 TPMs)
- [ ] Planned value profiles defined with narrowing tolerance bands
- [ ] Requirement threshold and objective values stated
- [ ] Margin calculated and margin consumption rate tracked
- [ ] Measurement methods defined for each lifecycle stage
- [ ] Measurement maturity level noted (estimate vs test data)
- [ ] Escalation thresholds are specific and actionable
- [ ] Reporting cadence and audience defined
- [ ] Trend direction indicated (improving, stable, degrading)

---

## Next Steps

After defining TPMs:
1. Use `/requirements` to ensure TPM-linked requirements are well-specified and measurable
2. Use `/testplan` to design test events that will measure TPMs at each milestone
3. Use `/tracematrix` to verify TPMs trace to requirements, design, and test
4. Use `/sysdecomp` to allocate TPMs to responsible components/subsystems
5. Use `/lcca` to understand cost impact of TPM shortfalls and corrective actions
6. Use `/fla` to anticipate failure modes that could cause TPM breaches