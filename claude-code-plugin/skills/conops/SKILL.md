---
name: "conops - Concept of Operations"
description: Develop a structured Concept of Operations (ConOps) document that defines operational scenarios, user interactions, mission context, and operational modes for a system. Bridges the gap between stakeholder needs and system requirements.
output:
  format: "document"
---

# Concept of Operations (ConOps)

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Develop ConOps for a new system**: The user has a system concept or mission need and wants to define how the system will be used operationally — who uses it, when, how, and under what conditions.
**Interpretation 2 — Revise ConOps for an evolving system**: The user has an existing system whose operational concept is changing — new users, new missions, new environments — and needs to update the ConOps accordingly.
**Interpretation 3 — Validate ConOps against requirements**: The user has both a ConOps and requirements and wants to verify they are consistent — that every operational scenario maps to requirements and vice versa.

If ambiguous, ask: "I can help with developing a new ConOps, revising an existing one for changed conditions, or validating a ConOps against requirements — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/conops 4x [input]").

| Depth | Min Scenarios | Min User Roles | Min Operational Modes | Min Constraints | Min Success Criteria |
|-------|--------------|----------------|----------------------|-----------------|---------------------|
| 1x    | 3            | 2              | 2                    | 3               | 3                   |
| 2x    | 6            | 4              | 3                    | 6               | 6                   |
| 4x    | 10           | 6              | 4                    | 10              | 10                  |
| 8x    | 16           | 10             | 6                    | 16              | 16                  |
| 16x   | 25           | 15             | 8                    | 25              | 25                  |

---

## The Process

### Step 1: Identify Mission and Purpose

Define the fundamental reason the system exists:

```
SYSTEM: [name]
MISSION STATEMENT: [one sentence describing what the system accomplishes]

PROBLEM BEING SOLVED:
- [What gap or pain exists today]
- [Why current solutions are insufficient]
- [What changes if this system succeeds]

MISSION OBJECTIVES:
| # | Objective | Measurable Outcome | Priority |
|---|-----------|-------------------|----------|
| 1 | [what the system must achieve] | [how you know it achieved it] | PRIMARY/SECONDARY |
| 2 | [what the system must achieve] | [how you know it achieved it] | PRIMARY/SECONDARY |
...

OPERATIONAL CONTEXT:
- Environment: [where the system operates — physical, digital, organizational]
- Timeframe: [when the system operates — 24/7, business hours, campaign-based]
- Geography: [where — single site, distributed, mobile]
- Lifecycle: [expected operational life — months, years, decades]
```

---

### Step 2: Define Operational Scenarios

Describe concrete scenarios showing how the system is used end-to-end:

```
SCENARIO [N]: [Descriptive Name]

Trigger: [What initiates this scenario]
Actors: [Who is involved]
Preconditions: [What must be true before this scenario begins]

SEQUENCE OF EVENTS:
| Step | Actor | Action | System Response | Duration |
|------|-------|--------|----------------|----------|
| 1 | [who] | [does what] | [system does what] | [how long] |
| 2 | [who] | [does what] | [system does what] | [how long] |
...

Postconditions: [What is true after this scenario completes]
Success Criteria: [How you know this scenario succeeded]
Frequency: [How often this scenario occurs — per hour/day/week/year]
Criticality: [MISSION-CRITICAL / IMPORTANT / ROUTINE]
```

Scenario types to consider:
- **Nominal**: The normal, expected use case
- **Off-nominal**: Expected deviations and edge cases
- **Emergency**: Failure responses and safety-critical situations
- **Maintenance**: How the system is maintained and updated
- **Startup/Shutdown**: How the system is brought online and taken offline

---

### Step 3: Define User Roles and Interactions

```
USER ROLES:

| # | Role | Responsibility | Interaction Mode | Frequency | Skill Level | Access Level |
|---|------|---------------|-----------------|-----------|-------------|-------------|
| 1 | [role name] | [what they do with the system] | [how they interact — GUI, CLI, API, physical] | [how often] | [novice/intermediate/expert] | [what they can access] |
...

USER INTERACTION MATRIX:

| Role → Scenario | Scenario 1 | Scenario 2 | Scenario 3 | ... |
|-----------------|-----------|-----------|-----------|-----|
| Role 1 | [initiator/participant/observer/none] | | | |
| Role 2 | | | | |
...

TRAINING REQUIREMENTS:

| Role | Training Needed | Duration | Recertification |
|------|----------------|----------|-----------------|
| [role] | [what training] | [how long] | [how often] |
...
```

---

### Step 4: Define Operational Modes

```
OPERATIONAL MODES:

| Mode | Description | Trigger | Available Capabilities | Restricted Capabilities | Transition To |
|------|------------|---------|----------------------|------------------------|--------------|
| NORMAL | [full operational capability] | [system startup complete] | [all] | [none] | DEGRADED, MAINTENANCE, EMERGENCY |
| DEGRADED | [reduced capability] | [partial failure] | [subset] | [what's lost] | NORMAL, EMERGENCY |
| EMERGENCY | [safety-critical response] | [critical failure or threat] | [safety functions only] | [non-essential functions] | DEGRADED, SHUTDOWN |
| MAINTENANCE | [system being serviced] | [scheduled or triggered] | [diagnostic functions] | [operational functions] | NORMAL |
| STARTUP | [system coming online] | [power on / initialization] | [self-test functions] | [operational functions] | NORMAL |
| SHUTDOWN | [system going offline] | [commanded or emergency] | [safe-state functions] | [all operational] | OFF |

MODE TRANSITION DIAGRAM:

[STARTUP] → [NORMAL] ↔ [DEGRADED]
                ↕              ↕
          [MAINTENANCE]   [EMERGENCY]
                ↕              ↕
           [SHUTDOWN] ← [SHUTDOWN]

TRANSITION RULES:
| From | To | Condition | Authority | Duration |
|------|----|-----------|-----------|----------|
| NORMAL | DEGRADED | [what triggers] | [automatic/manual] | [how long to transition] |
| DEGRADED | NORMAL | [what triggers recovery] | [who authorizes] | [how long] |
...
```

---

### Step 5: Define Operational Constraints

```
OPERATIONAL CONSTRAINTS:

| # | Category | Constraint | Rationale | Impact if Violated |
|---|----------|-----------|-----------|-------------------|
| 1 | Physical | [e.g., operates in -20°C to 50°C] | [why] | [what breaks] |
| 2 | Temporal | [e.g., must respond within 100ms] | [why] | [what breaks] |
| 3 | Regulatory | [e.g., must comply with HIPAA] | [why] | [legal/safety consequence] |
| 4 | Organizational | [e.g., max 2 operators per shift] | [why] | [operational impact] |
| 5 | Interface | [e.g., must interoperate with System X] | [why] | [what breaks] |
| 6 | Resource | [e.g., max 500W power consumption] | [why] | [what breaks] |
...

DEPENDENCY MAP:

| Dependency | Type | Criticality | Backup/Alternative |
|-----------|------|-------------|-------------------|
| [external system or resource] | [data/power/network/human] | [CRITICAL/IMPORTANT/MINOR] | [what happens if unavailable] |
...
```

---

### Step 6: Define Success Criteria

```
MISSION SUCCESS CRITERIA:

| # | Criterion | Metric | Target | Measurement Method | Acceptable Range |
|---|-----------|--------|--------|-------------------|-----------------|
| 1 | [what success looks like] | [how measured] | [target value] | [how you measure it] | [min acceptable] |
...

OPERATIONAL EFFECTIVENESS MEASURES:

| Measure | Description | Target | Current Baseline |
|---------|------------|--------|-----------------|
| Availability | [system uptime] | [e.g., 99.9%] | [current or N/A] |
| Reliability | [mean time between failures] | [e.g., 1000 hrs] | [current or N/A] |
| Throughput | [units processed per time] | [e.g., 100/hr] | [current or N/A] |
| Response Time | [time to complete key function] | [e.g., <2 sec] | [current or N/A] |
| User Satisfaction | [qualitative measure] | [e.g., >4.0/5.0] | [current or N/A] |

OPERATIONAL SUITABILITY MEASURES:

| Measure | Description | Target |
|---------|------------|--------|
| Training Time | [time to train a new user] | [target] |
| Maintenance Burden | [hours of maintenance per operational hour] | [target] |
| Staffing Requirement | [number of personnel needed] | [target] |
| Interoperability | [systems it must work with] | [target] |
```

---

## Output Format

```
## CONCEPT OF OPERATIONS: [System Name]

### 1. Mission and Purpose
[Mission statement, objectives, operational context]

### 2. Operational Scenarios
[Numbered scenarios with sequences, actors, conditions]

### 3. User Roles and Interactions
[Role table, interaction matrix, training requirements]

### 4. Operational Modes
[Mode definitions, transition rules, transition diagram]

### 5. Operational Constraints
[Constraint table, dependency map]

### 6. Success Criteria
[Effectiveness measures, suitability measures]

### 7. Assumptions and Risks
[Key assumptions underlying this ConOps]
[Risks if assumptions prove wrong]

### 8. Open Questions
[Items requiring stakeholder input or further analysis]
```

---

## Quality Checklist

Before completing:
- [ ] Mission and purpose clearly stated
- [ ] All operational scenarios cover nominal, off-nominal, emergency, maintenance, and startup/shutdown
- [ ] All user roles identified with interaction modes and skill levels
- [ ] All operational modes defined with transition rules
- [ ] Operational constraints are specific and measurable
- [ ] Success criteria are quantified with measurable targets
- [ ] Dependencies and external interfaces identified
- [ ] Assumptions explicitly stated
- [ ] Open questions listed for stakeholder resolution

---

## Next Steps

After ConOps:
1. Use `/stakeholder` to perform detailed stakeholder analysis
2. Use `/requirements` to derive system requirements from operational scenarios
3. Use `/sysarch` to design architecture that supports the operational concept
4. Use `/funcanalysis` to decompose system functions identified in scenarios
5. Use `/fla` to anticipate operational failures
