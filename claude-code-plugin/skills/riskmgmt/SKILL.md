---
name: "riskmgmt - Risk Management"
description: Identify, assess, mitigate, and monitor risks throughout the system lifecycle. Produces a risk register, risk matrix, and risk mitigation plan with triggers and contingencies.
output:
  format: "table"
---

# Risk Management

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Identify and assess risks for a new project or system**: The user is starting a project and wants to systematically surface all risks — technical, schedule, cost, and programmatic — and build a risk management plan.
**Interpretation 2 — Reassess risks for an ongoing project**: The user has an existing risk register and wants to update it — re-evaluate likelihoods, retire closed risks, identify new risks that have emerged, and check mitigation effectiveness.
**Interpretation 3 — Develop mitigation strategy for specific identified risks**: The user has a known risk or set of risks and wants detailed mitigation plans, contingencies, and trigger definitions.

If ambiguous, ask: "I can help with identifying risks for a new project, reassessing risks on an ongoing project, or developing mitigation plans for specific risks — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/riskmgmt 4x [input]").

| Depth | Min Risks Identified | Min Risk Categories | Min Mitigations | Min Triggers Defined |
|-------|---------------------|--------------------|-----------------|--------------------|
| 1x    | 8                   | 3                  | 5               | 3                  |
| 2x    | 15                  | 5                  | 10              | 8                  |
| 4x    | 30                  | 6                  | 20              | 15                 |
| 8x    | 50                  | 8                  | 35              | 25                 |
| 16x   | 80                  | 10                 | 50              | 40                 |

---

## The Process

### Step 1: Risk Identification

Systematically surface risks across all categories:

```
RISK IDENTIFICATION BY CATEGORY:

TECHNICAL RISKS:
| ID | Risk | Description | Source |
|----|------|-------------|--------|
| TR-001 | [risk name] | [what could go wrong] | [how we identified it] |
...

SCHEDULE RISKS:
| ID | Risk | Description | Source |
|----|------|-------------|--------|
| SR-001 | [risk name] | [what could go wrong] | [how we identified it] |
...

COST RISKS:
| ID | Risk | Description | Source |
|----|------|-------------|--------|
| CR-001 | [risk name] | [what could go wrong] | [how we identified it] |
...

PROGRAMMATIC RISKS:
| ID | Risk | Description | Source |
|----|------|-------------|--------|
| PR-001 | [risk name] | [what could go wrong] | [how we identified it] |
...

EXTERNAL RISKS:
| ID | Risk | Description | Source |
|----|------|-------------|--------|
| ER-001 | [risk name] | [what could go wrong] | [how we identified it] |
...

RISK IDENTIFICATION PROMPTS:
| Prompt | Risks Found? |
|--------|-------------|
| "What technology are we using for the first time?" | |
| "What has the longest lead time?" | |
| "What depends on a single person or vendor?" | |
| "What has we estimated but never measured?" | |
| "What assumption would hurt most if wrong?" | |
| "What interface is least well-defined?" | |
| "What requirement is most likely to change?" | |
| "What's the most complex part of the system?" | |
| "What has failed on similar projects?" | |
| "What external event would disrupt this project?" | |
| "Where do we have the least expertise?" | |
| "What's the biggest unknown unknown we can imagine?" | |
```

---

### Step 2: Risk Assessment

Rate each risk on likelihood and impact:

```
LIKELIHOOD SCALE:
| Level | Label | Probability | Description |
|-------|-------|-------------|-------------|
| 5 | Near Certain | >80% | Expected to occur |
| 4 | Likely | 60-80% | Will probably occur |
| 3 | Possible | 40-60% | May occur |
| 2 | Unlikely | 20-40% | Could occur but not expected |
| 1 | Rare | <20% | Very unlikely to occur |

IMPACT SCALE:
| Level | Technical | Schedule | Cost | Description |
|-------|-----------|----------|------|-------------|
| 5 | System failure / mission loss | >6 month delay | >50% budget overrun | Catastrophic |
| 4 | Major performance degradation | 3-6 month delay | 25-50% budget overrun | Critical |
| 3 | Moderate performance reduction | 1-3 month delay | 10-25% budget overrun | Significant |
| 2 | Minor performance impact | 2-4 week delay | 5-10% budget overrun | Marginal |
| 1 | Negligible impact | <2 week delay | <5% budget overrun | Negligible |

RISK MATRIX:
                    IMPACT
                 1    2    3    4    5
LIKELIHOOD  5 |  5 | 10 | 15 | 20 | 25 |
            4 |  4 |  8 | 12 | 16 | 20 |
            3 |  3 |  6 |  9 | 12 | 15 |
            2 |  2 |  4 |  6 |  8 | 10 |
            1 |  1 |  2 |  3 |  4 |  5 |

RISK LEVELS:
- CRITICAL (20-25): Immediate action required, escalate to leadership
- HIGH (12-16): Mitigation plan required, active monitoring
- MEDIUM (6-10): Mitigation planned, periodic monitoring
- LOW (1-5): Accept or monitor, no active mitigation required
```

---

### Step 3: Risk Register

Consolidate all risks into a single register:

```
RISK REGISTER:

| Risk ID | Risk Title | Category | Likelihood (1-5) | Impact (1-5) | Risk Score | Level | Owner | Status |
|---------|-----------|----------|------------------|-------------|------------|-------|-------|--------|
| TR-001 | [title] | Technical | [L] | [I] | [LxI] | CRIT/HIGH/MED/LOW | [person] | OPEN/MITIGATING/WATCHING/CLOSED |
| SR-001 | [title] | Schedule | [L] | [I] | [LxI] | CRIT/HIGH/MED/LOW | [person] | OPEN/MITIGATING/WATCHING/CLOSED |
...

RISK DISTRIBUTION:
| Level | Count | Percentage |
|-------|-------|-----------|
| CRITICAL | [N] | [%] |
| HIGH | [N] | [%] |
| MEDIUM | [N] | [%] |
| LOW | [N] | [%] |
```

---

### Step 4: Mitigation Strategy

For each HIGH and CRITICAL risk, define a mitigation approach:

```
MITIGATION STRATEGIES:

STRATEGY TYPES:
- AVOID: Eliminate the risk by changing the approach
- TRANSFER: Shift the risk to another party (insurance, subcontract, etc.)
- MITIGATE: Reduce likelihood and/or impact through specific actions
- ACCEPT: Acknowledge the risk and prepare contingency

MITIGATION PLAN:

RISK: [Risk ID] — [Risk Title]
STRATEGY: AVOID / TRANSFER / MITIGATE / ACCEPT
OWNER: [person]

MITIGATION ACTIONS:
| # | Action | Reduces | Responsible | Due Date | Status | Cost |
|---|--------|---------|------------|----------|--------|------|
| 1 | [specific action] | Likelihood / Impact / Both | [person] | [date] | NOT STARTED/IN PROGRESS/COMPLETE | [cost] |
| 2 | [specific action] | Likelihood / Impact / Both | [person] | [date] | NOT STARTED/IN PROGRESS/COMPLETE | [cost] |
...

RESIDUAL RISK AFTER MITIGATION:
| Parameter | Before | After |
|-----------|--------|-------|
| Likelihood | [1-5] | [1-5] |
| Impact | [1-5] | [1-5] |
| Risk Score | [LxI] | [LxI] |
| Risk Level | [level] | [level] |
```

---

### Step 5: Risk Triggers and Contingencies

Define early warning signs and contingency plans:

```
RISK TRIGGERS AND CONTINGENCIES:

| Risk ID | Trigger | Detection Method | Contingency Plan | Contingency Cost |
|---------|---------|-----------------|-----------------|-----------------|
| TR-001 | [observable sign that risk is materializing] | [how you'll detect it] | [what to do if risk occurs] | [estimated cost] |
| SR-001 | [observable sign] | [detection method] | [contingency] | [cost] |
...

TRIGGER EXAMPLES BY CATEGORY:
- Technical: Prototype fails test, performance below threshold, integration defect rate rising
- Schedule: Milestone slip >1 week, critical path task delayed, resource unavailable
- Cost: Actual spend >10% over plan, vendor price increase, scope creep detected
- External: Regulatory change announced, key vendor acquired, market shift
```

---

### Step 6: Risk Monitoring Plan

```
RISK MONITORING:

REVIEW CADENCE:
| Risk Level | Review Frequency | Review Forum | Escalation Path |
|-----------|-----------------|-------------|-----------------|
| CRITICAL | Weekly | Project leadership | Executive sponsor |
| HIGH | Bi-weekly | Project team | Project manager |
| MEDIUM | Monthly | Risk review meeting | Project team lead |
| LOW | Quarterly | Status report | Risk owner |

RISK DASHBOARD METRICS:
| Metric | Current | Trend | Target |
|--------|---------|-------|--------|
| Total open risks | [N] | [↑↓→] | Decreasing over time |
| Critical risks | [N] | [↑↓→] | 0 at delivery |
| Risks mitigated this period | [N] | [↑↓→] | Per plan |
| New risks identified | [N] | [↑↓→] | Decreasing over time |
| Overdue mitigation actions | [N] | [↑↓→] | 0 |
| Risks materialized | [N] | [↑↓→] | Below plan |

TOP RISKS WATCHLIST:
| Rank | Risk ID | Title | Score | Trend | Next Action | Due |
|------|---------|-------|-------|-------|------------|-----|
| 1 | [ID] | [title] | [score] | [↑↓→] | [action] | [date] |
| 2 | [ID] | [title] | [score] | [↑↓→] | [action] | [date] |
...
```

---

## Output Format

```
## RISK MANAGEMENT PLAN: [System/Project Name]

### Document Control
Version: [X.Y]
Date: [date]
Status: [DRAFT/REVIEW/APPROVED]

### Risk Identification
[All identified risks by category with descriptions]

### Risk Assessment
[Likelihood and impact scales, risk matrix]

### Risk Register
[Complete risk register with scores, levels, owners, status]

### Mitigation Plans
[Detailed mitigation for each HIGH and CRITICAL risk]

### Triggers and Contingencies
[Early warning triggers, detection methods, contingency plans]

### Monitoring Plan
[Review cadence, dashboard metrics, escalation paths]

### Risk Summary
Total: [N] | Critical: [N] | High: [N] | Medium: [N] | Low: [N]
Top risk: [title and score]

### Open Items
[Risks needing further analysis, pending stakeholder input]
```

---

## Quality Checklist

Before completing:
- [ ] All risk categories covered (technical, schedule, cost, programmatic, external)
- [ ] Risk identification prompts applied to surface hidden risks
- [ ] Every risk has likelihood and impact assessed with justification
- [ ] Risk matrix populated and risk levels assigned
- [ ] Every CRITICAL and HIGH risk has a mitigation plan with specific actions
- [ ] Mitigation actions have owners, due dates, and costs
- [ ] Residual risk assessed after mitigation
- [ ] Triggers defined for all HIGH and CRITICAL risks with detection methods
- [ ] Contingency plans defined for all HIGH and CRITICAL risks
- [ ] Monitoring cadence and escalation paths established
- [ ] Risk register has no unowned risks

---

## Next Steps

After risk management:
1. Use `/vv` to verify that risk mitigations are effective
2. Use `/iface` to check high-risk interfaces in detail
3. Use `/sysintegration` to sequence integration to address highest risks first
4. Use `/de` to map dependencies between risks and project elements
5. Use `/fla` to stress-test mitigation plans against failure scenarios
6. Use `/configmgmt` to baseline risk register and track changes
