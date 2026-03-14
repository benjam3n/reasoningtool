---
name: "ram - Reliability, Availability, Maintainability Analysis"
description: Analyze and specify system reliability, availability, and maintainability characteristics. Models failure behavior, predicts system performance, and identifies improvement opportunities.
output:
  format: "table"
---

# Reliability, Availability, Maintainability (RAM) Analysis

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Define RAM requirements for a new system**: The user has a system concept and needs to establish quantitative RAM targets — MTBF, MTTR, availability goals — and allocate them to subsystems.
**Interpretation 2 — Predict RAM performance for an existing design**: The user has a system architecture and wants to calculate expected reliability, availability, and maintainability from component data.
**Interpretation 3 — Improve RAM for a fielded system**: The user has a system with known reliability or maintenance problems and wants to identify root causes and improvement strategies.

If ambiguous, ask: "I can help with setting RAM requirements for a new system, predicting RAM for an existing design, or improving RAM for a fielded system — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/ram 4x [input]").

| Depth | Min Components Analyzed | Min Failure Modes | Min Maintenance Tasks | Min Improvement Actions |
|-------|------------------------|-------------------|-----------------------|------------------------|
| 1x    | 5                      | 8                 | 4                     | 3                      |
| 2x    | 12                     | 15                | 8                     | 6                      |
| 4x    | 25                     | 30                | 15                    | 10                     |
| 8x    | 50                     | 60                | 30                    | 15                     |
| 16x   | 100                    | 100               | 50                    | 25                     |

---

## The Process

### Step 1: Define the System and Operating Context

Establish what is being analyzed and under what conditions:

```
SYSTEM: [name]
MISSION: [primary function]
DESIGN LIFE: [expected operational lifespan]

OPERATING CONTEXT:
- Environment: [temperature, humidity, vibration, corrosion, etc.]
- Duty cycle: [continuous / intermittent / on-demand]
- Operating hours per year: [N]
- Mission duration: [typical mission length]
- Deployment: [fixed / mobile / shipboard / airborne / space]

CRITICALITY:
- Safety-critical: [Yes/No — failure could cause injury/death]
- Mission-critical: [Yes/No — failure causes mission abort]
- Economic impact of downtime: [$/hour or qualitative]

APPLICABLE STANDARDS:
- [MIL-STD-882, IEC 61508, ISO 26262, ARP4761, etc.]
```

---

### Step 2: Define RAM Requirements

Establish quantitative targets:

```
RAM REQUIREMENTS:

RELIABILITY:
| Parameter | Target | Basis | Allocation Level |
|-----------|--------|-------|-----------------|
| System MTBF | [hours] | [customer spec / benchmark / derived] | System |
| Mission reliability R(t) | [probability] for [t hours] | [mission requirement] | System |
| Design life reliability | [probability] for [years] | [lifecycle requirement] | System |

AVAILABILITY:
| Parameter | Target | Definition Used |
|-----------|--------|----------------|
| Operational availability (Ao) | [%] | Ao = Uptime / (Uptime + Downtime) |
| Inherent availability (Ai) | [%] | Ai = MTBF / (MTBF + MTTR) |
| Achieved availability (Aa) | [%] | Includes preventive maintenance |

MAINTAINABILITY:
| Parameter | Target | Notes |
|-----------|--------|-------|
| MTTR (Mean Time To Repair) | [hours] | Corrective maintenance |
| MPMT (Mean Preventive Maintenance Time) | [hours] | Scheduled maintenance |
| MMH/OH (Maintenance Man-Hours per Operating Hour) | [ratio] | Total maintenance burden |
| Max corrective maintenance time (95th percentile) | [hours] | Worst-case repair |
| Fault detection coverage | [%] | Built-in test effectiveness |
| Fault isolation to LRU | [%] within [N] fault indications | Diagnostic capability |
```

---

### Step 3: System Reliability Modeling

Model the system reliability architecture:

#### 3A: Reliability Block Diagram (RBD)

```
RELIABILITY BLOCK DIAGRAM:

Configuration: [series / parallel / k-of-n / complex]

SERIES ELEMENTS (all must work):
  [A] → [B] → [C] → ... → [output]
  System R(t) = R_A(t) x R_B(t) x R_C(t)

PARALLEL/REDUNDANT ELEMENTS (at least one must work):
  ┌─ [A1] ─┐
  │        │
  ├─ [A2] ─┤  R_parallel = 1 - (1-R_A1)(1-R_A2)
  │        │
  └────────┘

K-OF-N ELEMENTS (at least k of n must work):
  [A1, A2, A3] — need [k] of [3] working
```

#### 3B: Component Reliability Data

| Component | Quantity | Failure Rate (lambda) | MTBF | Distribution | Data Source | Confidence |
|-----------|----------|----------------------|------|--------------|-------------|------------|
| [name] | [N] | [failures/hr] | [hrs] | [exponential/Weibull] | [MIL-HDBK-217/field data/vendor] | [HIGH/MED/LOW] |
| [name] | [N] | [failures/hr] | [hrs] | [exponential/Weibull] | [source] | [HIGH/MED/LOW] |

#### 3C: Reliability Predictions

| Level | MTBF (hrs) | R(t) at mission time | R(t) at design life | Meets Requirement? |
|-------|-----------|---------------------|--------------------|--------------------|
| System | [calculated] | [calculated] | [calculated] | [YES/NO — gap] |
| Subsystem A | [calculated] | [calculated] | [calculated] | [YES/NO] |
| Subsystem B | [calculated] | [calculated] | [calculated] | [YES/NO] |

#### 3D: Reliability Improvement Techniques

| Technique | Applied To | Improvement Factor | Cost Impact | Trade-off |
|-----------|-----------|-------------------|-------------|-----------|
| Redundancy (active) | [component] | [factor] | [cost] | Weight, power, complexity |
| Redundancy (standby) | [component] | [factor] | [cost] | Switching reliability |
| Derating | [component] | [factor] | [cost] | Size, weight |
| Better components | [component] | [factor] | [cost] | Lead time, availability |
| Environmental control | [subsystem] | [factor] | [cost] | Power, weight |
| Simplified design | [subsystem] | [factor] | [cost] | Reduced functionality |

---

### Step 4: Failure Mode Analysis

Connect to FMEA — identify critical failure modes:

```
CRITICAL FAILURE MODES:

| ID | Component | Failure Mode | Effect on System | Severity | Occurrence | Detection | RPN | Mitigation |
|----|-----------|-------------|-----------------|----------|------------|-----------|-----|------------|
| FM-1 | [component] | [how it fails] | [system impact] | [1-10] | [1-10] | [1-10] | [S*O*D] | [action] |
| FM-2 | [component] | [how it fails] | [system impact] | [1-10] | [1-10] | [1-10] | [S*O*D] | [action] |

SINGLE POINTS OF FAILURE:
| Component | Failure Effect | Criticality | Mitigation Strategy |
|-----------|---------------|-------------|---------------------|
| [name] | [what happens] | [CRITICAL/MAJOR] | [redundancy / monitoring / design-out] |
```

---

### Step 5: Maintainability Analysis

Analyze ease of maintenance:

#### 5A: Maintenance Concept

```
MAINTENANCE LEVELS:
| Level | Location | Capability | Typical Actions |
|-------|----------|------------|-----------------|
| Organizational (O-level) | [field/user site] | [tools, skills] | [remove & replace, operational checks] |
| Intermediate (I-level) | [depot/shop] | [test equipment] | [diagnose, repair assemblies] |
| Depot (D-level) | [factory/OEM] | [full capability] | [overhaul, remanufacture] |
```

#### 5B: Maintenance Task Analysis

| Task ID | Task | Level | Frequency | Duration (hrs) | Personnel | Skill Level | Special Tools | Access Difficulty |
|---------|------|-------|-----------|---------------|-----------|-------------|---------------|-------------------|
| CM-1 | [corrective task] | [O/I/D] | [per 1000 hrs] | [mean / 95th] | [N people] | [basic/intermediate/expert] | [list] | [EASY/MODERATE/DIFFICULT] |
| PM-1 | [preventive task] | [O/I/D] | [interval] | [mean / 95th] | [N people] | [level] | [list] | [EASY/MODERATE/DIFFICULT] |

#### 5C: Maintainability Design Features

| Feature | Status | Impact on MTTR | Notes |
|---------|--------|---------------|-------|
| Built-in test (BIT) | [Yes/No/Partial] | [reduction in diagnostic time] | |
| Modular / LRU design | [Yes/No/Partial] | [reduction in repair time] | |
| Tool-less access panels | [Yes/No] | [reduction in access time] | |
| Color-coded connectors | [Yes/No] | [reduction in error rate] | |
| Standardized fasteners | [Yes/No] | [reduction in tool count] | |
| Visible status indicators | [Yes/No] | [reduction in fault detection time] | |
| Maintenance manuals / IETM | [Yes/No] | [reduction in skill requirement] | |
| Remote diagnostics | [Yes/No] | [reduction in response time] | |

---

### Step 6: Availability Calculation

```
AVAILABILITY MODEL:

INPUTS:
- MTBF: [hours] (from Step 3)
- MTTR: [hours] (from Step 5)
- MPMT (Mean Preventive Maintenance Time): [hours]
- Preventive maintenance interval: [hours]
- Mean Logistics Delay Time (MLDT): [hours]
- Mean Administrative Delay Time (MADT): [hours]

CALCULATIONS:

Inherent Availability:
  Ai = MTBF / (MTBF + MTTR)
  Ai = [value] / ([value] + [value]) = [result]

Achieved Availability:
  Aa = MTBM / (MTBM + M_bar)
  where MTBM includes preventive maintenance
  Aa = [result]

Operational Availability:
  Ao = MTBM / (MTBM + MDT)
  where MDT = MTTR + MLDT + MADT
  Ao = [result]

AVAILABILITY COMPARISON:
| Metric | Target | Predicted | Margin | Status |
|--------|--------|-----------|--------|--------|
| Ai | [%] | [%] | [+/- %] | [MEETS/SHORTFALL] |
| Aa | [%] | [%] | [+/- %] | [MEETS/SHORTFALL] |
| Ao | [%] | [%] | [+/- %] | [MEETS/SHORTFALL] |

SENSITIVITY ANALYSIS:
| Parameter Changed | Change | Effect on Ao | Elasticity |
|-------------------|--------|-------------|------------|
| MTBF +10% | [new MTBF] | [new Ao] | [% change in Ao / % change in MTBF] |
| MTTR -10% | [new MTTR] | [new Ao] | [% change] |
| MLDT -50% | [new MLDT] | [new Ao] | [% change] |
```

---

### Step 7: RAM Improvement Opportunities

```
RAM IMPROVEMENT PLAN:

| # | Opportunity | RAM Parameter Improved | Current | Target | Action Required | Cost Estimate | Priority |
|---|-------------|----------------------|---------|--------|----------------|---------------|----------|
| 1 | [description] | [MTBF/MTTR/Ao/etc.] | [current value] | [improved value] | [specific action] | [cost] | HIGH/MED/LOW |
| 2 | [description] | [parameter] | [current] | [improved] | [action] | [cost] | HIGH/MED/LOW |

IMPROVEMENT CATEGORIES:
- Design improvements: [list actions that change the design]
- Process improvements: [list actions that change maintenance processes]
- Logistics improvements: [list actions that reduce supply delays]
- Training improvements: [list actions that improve technician capability]

ROI ANALYSIS:
| Improvement | Implementation Cost | Annual Savings (reduced downtime) | Payback Period |
|-------------|--------------------|---------------------------------|----------------|
| [action] | [$] | [$] | [months] |
```

---

## Output Format

```
## RAM ANALYSIS REPORT: [System Name]

### System & Operating Context
[Environment, duty cycle, criticality, standards]

### RAM Requirements
[Targets for MTBF, MTTR, Ao with rationale]

### Reliability Model
[RBD, component data, predictions vs. requirements]

### Critical Failure Modes
[Top failure modes with RPN, single points of failure]

### Maintainability Assessment
[Maintenance concept, task analysis, design features]

### Availability Predictions
[Ai, Aa, Ao calculations with sensitivity analysis]

### RAM Shortfalls & Improvements
[Gaps between predicted and required, improvement plan with ROI]

### Open Items
[Data gaps, assumptions requiring validation, trades to resolve]
```

---

## Quality Checklist

Before completing:
- [ ] Operating context and duty cycle defined
- [ ] Quantitative RAM requirements established with rationale
- [ ] Reliability block diagram constructed
- [ ] Component failure rates sourced and documented
- [ ] System reliability predicted and compared to requirements
- [ ] Single points of failure identified
- [ ] Maintenance concept defined (levels, tasks, intervals)
- [ ] MTTR predicted from task analysis
- [ ] Availability calculated (Ai, Aa, Ao) and compared to targets
- [ ] Sensitivity analysis performed
- [ ] Improvement opportunities identified with ROI
- [ ] Data source confidence levels noted

---

## Next Steps

After RAM analysis:
1. Use `/riskmgmt` to manage risks from RAM shortfalls
2. Use `/tradestudy` to evaluate redundancy vs. cost trade-offs
3. Use `/testplan` to define reliability demonstration tests
4. Use `/lcca` to incorporate maintenance costs into lifecycle cost
5. Use `/hsi` to ensure maintenance tasks match human capabilities
6. Use `/tpm` to track RAM parameters during development
