---
name: "hsi - Human Systems Integration"
description: Ensure system design accounts for human capabilities, limitations, and needs across all user populations. Addresses human factors, training, staffing, and accessibility.
output:
  format: "table"
---

# Human Systems Integration (HSI)

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Plan HSI for a new system design**: The user is developing a new system and wants to proactively integrate human considerations into the design from the start.
**Interpretation 2 — Evaluate HSI for an existing system**: The user has an existing system and wants to assess how well it accommodates human users — identifying usability problems, training gaps, or safety concerns.
**Interpretation 3 — Resolve a specific human-system issue**: The user has a known problem (high error rate, excessive training time, workload overload, accessibility gap) and wants targeted HSI recommendations.

If ambiguous, ask: "I can help with planning HSI for a new design, evaluating an existing system, or resolving a specific human-system problem — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/hsi 4x [input]").

| Depth | Min Interaction Points | Min User Populations | Min Human Factors Issues | Min Training Requirements | Min Accessibility Checks |
|-------|----------------------|---------------------|------------------------|--------------------------|-------------------------|
| 1x    | 5                    | 2                   | 5                      | 3                        | 3                       |
| 2x    | 12                   | 4                   | 10                     | 6                        | 6                       |
| 4x    | 25                   | 6                   | 20                     | 12                       | 10                      |
| 8x    | 40                   | 8                   | 35                     | 20                       | 15                      |
| 16x   | 60                   | 12                  | 50                     | 30                       | 20                      |

---

## The Process

### Step 1: Analyze User Populations

Characterize everyone who will interact with the system:

```
USER POPULATION ANALYSIS:

| Population | Role | Count | Environment | Interaction Frequency | Criticality |
|------------|------|-------|-------------|----------------------|-------------|
| [e.g., Operators] | [primary use] | [N] | [office/field/vehicle] | [continuous/hourly/daily] | [safety-critical/mission-critical/routine] |
| [Maintainers] | [maintain/repair] | [N] | [shop/field] | [weekly/monthly] | [level] |
| [Supervisors] | [monitor/decide] | [N] | [control room] | [continuous] | [level] |
| [Trainees] | [learning] | [N] | [classroom/OJT] | [initial period] | [level] |

FOR EACH POPULATION:

Physical Characteristics:
| Attribute | Range / Distribution | Design Implication |
|-----------|---------------------|-------------------|
| Age range | [min-max, typical] | [vision, hearing, strength] |
| Anthropometry | [percentile range to accommodate] | [reach, clearance, workspace] |
| Strength | [grip, lift, push/pull capabilities] | [force limits on controls] |
| Sensory | [vision, hearing, touch acuity] | [display, alert, feedback design] |
| Endurance | [shift length, fatigue onset] | [break scheduling, automation] |

Cognitive Characteristics:
| Attribute | Range / Assumption | Design Implication |
|-----------|-------------------|-------------------|
| Education level | [minimum expected] | [vocabulary, abstraction level] |
| Domain expertise | [novice to expert] | [guidance, defaults, shortcuts] |
| Language | [primary, secondary] | [localization, terminology] |
| Cognitive load capacity | [number of concurrent tasks] | [information density, automation] |
| Decision-making style | [analytical/intuitive/rule-based] | [decision support design] |
| Stress tolerance | [expected stress levels] | [error-proofing under stress] |
```

---

### Step 2: Identify Human-System Interaction Points

Map every point where humans interact with the system:

```
INTERACTION INVENTORY:

| ID | User Population | Task | Interaction Type | Interface | Frequency | Duration | Criticality |
|----|----------------|------|-----------------|-----------|-----------|----------|-------------|
| HSI-1 | [who] | [what they do] | [input/output/monitor/decide/maintain] | [display/control/tool] | [per hour/day] | [minutes] | [HIGH/MED/LOW] |
| HSI-2 | [who] | [what] | [type] | [interface] | [frequency] | [duration] | [criticality] |

INTERACTION CATEGORIES:
- Operations: [routine tasks during normal operation]
- Monitoring: [observing system status, detecting anomalies]
- Decision-making: [choosing among alternatives, responding to events]
- Maintenance: [inspection, repair, calibration, software updates]
- Emergency: [response to failures, alarms, degraded operations]
- Startup/Shutdown: [initialization, configuration, safe shutdown]
- Handover: [shift change, role transfer, information exchange]
```

---

### Step 3: Apply Human Factors Principles

For each critical interaction point, evaluate against human factors principles:

#### 3A: Cognitive Load Assessment

| Interaction | Information Items | Decisions Required | Time Pressure | Memory Load | Cognitive Load Rating |
|-------------|------------------|--------------------|---------------|-------------|----------------------|
| [HSI-1] | [count of things to track] | [count] | [HIGH/MED/LOW] | [items to remember] | [OVERLOAD/HIGH/MODERATE/LOW] |

For OVERLOAD or HIGH ratings:
| Interaction | Reduction Strategy | Expected Improvement |
|-------------|-------------------|---------------------|
| [HSI-1] | [automation / simplification / chunking / decision aid] | [reduced from X to Y items] |

#### 3B: Error Analysis and Error-Proofing

| Interaction | Likely Errors | Error Type | Consequence | Prevention Strategy | Recovery Strategy |
|-------------|--------------|------------|-------------|--------------------|--------------------|
| [HSI-1] | [what could go wrong] | [slip/lapse/mistake/violation] | [severity] | [constraint/confirmation/undo] | [how to recover] |

Error-proofing techniques applied:
| Technique | Applied To | Description |
|-----------|-----------|-------------|
| Forcing function | [interaction] | [prevents action unless precondition met] |
| Confirmation | [interaction] | [requires explicit confirmation for critical actions] |
| Undo capability | [interaction] | [allows reversal of action] |
| Defaults | [interaction] | [safe defaults reduce decision errors] |
| Visibility | [interaction] | [system state always visible] |
| Mapping | [interaction] | [controls map naturally to effects] |
| Constraints | [interaction] | [physical/logical limits on inputs] |

#### 3C: Feedback and Situation Awareness

| System State | How User Knows | Modality | Latency | Adequacy |
|-------------|---------------|----------|---------|----------|
| [normal operation] | [indicator/display] | [visual/auditory/haptic] | [ms/sec] | [GOOD/POOR] |
| [degraded mode] | [alert/alarm] | [modality] | [latency] | [GOOD/POOR] |
| [failure] | [alarm/shutdown] | [modality] | [latency] | [GOOD/POOR] |
| [action effect] | [confirmation] | [modality] | [latency] | [GOOD/POOR] |

Situation Awareness Assessment:
| SA Level | Question | Supported? | Gap |
|----------|----------|-----------|-----|
| SA-1 Perception | What is the current state? | [Yes/Partial/No] | [what's missing] |
| SA-2 Comprehension | What does the state mean? | [Yes/Partial/No] | [what's missing] |
| SA-3 Projection | What will happen next? | [Yes/Partial/No] | [what's missing] |

---

### Step 4: Workload and Staffing Analysis

```
WORKLOAD ANALYSIS:

TASK TIMELINE (for critical operational scenario):

| Time | Operator Tasks | Cognitive Load | Physical Load | Concurrent Tasks | Workload Rating |
|------|---------------|---------------|---------------|------------------|----------------|
| T+0 | [task list] | [LOW/MED/HIGH] | [LOW/MED/HIGH] | [count] | [1-7 Bedford scale] |
| T+5min | [task list] | [level] | [level] | [count] | [rating] |
| T+10min | [task list] | [level] | [level] | [count] | [rating] |

WORKLOAD PEAKS:
| Scenario | Peak Workload | Duration | Exceeds Capacity? | Mitigation |
|----------|-------------|----------|-------------------|------------|
| [normal ops] | [rating] | [duration] | [Yes/No] | [if yes, how to reduce] |
| [high tempo] | [rating] | [duration] | [Yes/No] | [mitigation] |
| [emergency] | [rating] | [duration] | [Yes/No] | [mitigation] |

STAFFING REQUIREMENTS:
| Role | Count | Shift Pattern | Justification | Backup/Cross-training |
|------|-------|--------------|---------------|----------------------|
| [role] | [N] | [8hr/12hr/on-call] | [workload basis] | [who can cover] |
```

---

### Step 5: Training Requirements Analysis

```
TRAINING REQUIREMENTS:

| Population | Knowledge/Skill | Current Proficiency | Required Proficiency | Gap | Training Method | Duration |
|------------|----------------|--------------------|--------------------|-----|----------------|----------|
| [operators] | [system operation] | [none/basic/intermediate] | [intermediate/expert] | [size of gap] | [classroom/simulator/OJT/CBT] | [hours] |
| [maintainers] | [diagnosis/repair] | [none/basic] | [intermediate] | [gap] | [method] | [hours] |

TRAINING PROGRAM:
| Phase | Content | Method | Duration | Assessment | Recurrence |
|-------|---------|--------|----------|------------|------------|
| Initial | [what's taught] | [how] | [hours/days] | [test/demo/observation] | [one-time] |
| Qualification | [proficiency demo] | [practical exercise] | [hours] | [pass/fail criteria] | [annual] |
| Continuation | [skill maintenance] | [refresher/drill] | [hours] | [criteria] | [quarterly/annual] |

TRAINING SUPPORT:
- Simulators needed: [Yes/No — fidelity level, quantity]
- Training materials: [manuals, CBT, videos, job aids]
- Instructor requirements: [N instructors, qualifications]
- Training facility: [classroom, lab, field site]
```

---

### Step 6: Accessibility and Inclusivity Assessment

```
ACCESSIBILITY ASSESSMENT:

| Standard | Requirement | Status | Gap | Remediation |
|----------|------------|--------|-----|-------------|
| Visual | [contrast, font size, color-blind safe] | [MEETS/PARTIAL/FAILS] | [what's missing] | [fix] |
| Auditory | [volume range, visual alternatives to audio] | [status] | [gap] | [fix] |
| Motor | [input alternatives, reach, force limits] | [status] | [gap] | [fix] |
| Cognitive | [plain language, consistency, progressive disclosure] | [status] | [gap] | [fix] |
| Language | [localization, terminology, reading level] | [status] | [gap] | [fix] |

INCLUSIVITY CONSIDERATIONS:
| Factor | Addressed? | Design Decision |
|--------|-----------|----------------|
| Left-handed users | [Yes/No] | [ambidextrous design / options] |
| Aging workforce | [Yes/No] | [larger text, higher contrast, reduced fine motor] |
| Varied body sizes | [Yes/No] | [adjustable, 5th-95th percentile accommodation] |
| Neurodiverse users | [Yes/No] | [customizable interfaces, reduced sensory overload] |
| Cultural differences | [Yes/No] | [icons vs. text, color meaning, reading direction] |
| Temporary impairments | [Yes/No] | [gloves, noise, fatigue, injury] |
```

---

## Output Format

```
## HSI ASSESSMENT: [System Name]

### User Populations
[Populations, characteristics, design implications]

### Human-System Interaction Map
[All interaction points with criticality]

### Human Factors Assessment
[Cognitive load, error analysis, feedback, situation awareness]

### Workload & Staffing
[Workload timeline, peaks, staffing requirements]

### Training Requirements
[Training program, support needs, recurrence]

### Accessibility & Inclusivity
[Standards compliance, gaps, remediation]

### HSI Design Recommendations
[Priority-ranked list of design changes]

### HSI Risks
[Risks from unresolved HSI issues]

### Open Items
[Questions requiring user research, testing, or stakeholder input]
```

---

## Quality Checklist

Before completing:
- [ ] All user populations identified and characterized
- [ ] Human-system interaction points mapped
- [ ] Cognitive load assessed for critical tasks
- [ ] Error modes identified with prevention strategies
- [ ] Feedback and situation awareness evaluated
- [ ] Workload peaks identified and mitigated
- [ ] Staffing justified from workload analysis
- [ ] Training requirements defined with methods and durations
- [ ] Accessibility assessed against applicable standards
- [ ] Inclusivity considerations addressed
- [ ] Recommendations prioritized by safety and mission impact

---

## Next Steps

After HSI assessment:
1. Use `/requirements` to incorporate HSI requirements into system spec
2. Use `/ram` to verify maintenance tasks match human capabilities
3. Use `/riskmgmt` to manage risks from unresolved HSI issues
4. Use `/testplan` to plan usability testing and human factors evaluations
5. Use `/tradestudy` to evaluate automation vs. manual operation trade-offs
6. Use `/conops` to validate operational scenarios account for human roles
