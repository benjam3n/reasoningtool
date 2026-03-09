---
name: "rgc - Regulatory Compliance"
description: Assess compliance with applicable regulations by mapping requirements to current practices, identifying gaps, and prioritizing remediation.
---

# Regulatory Compliance

**Input**: $ARGUMENTS

---

## Step 1: Identify Applicable Regulations

Determine which regulations apply to this situation, organization, or activity.

```
ENTITY/ACTIVITY: [what is being assessed]
INDUSTRY: [sector]
JURISDICTION(S): [where it operates]

APPLICABLE REGULATIONS:
1. [regulation name] — Authority: [governing body]
   Scope: [what it covers]
   Key requirements: [summary]

2. [regulation name] — Authority: [governing body]
   Scope: [what it covers]
   Key requirements: [summary]

UPCOMING REGULATIONS (not yet effective):
- [regulation] — Effective: [date] — Impact: [summary]

VOLUNTARY STANDARDS THAT APPLY:
- [standard — e.g., ISO, SOC, industry codes]
```

---

## Step 2: Map Current Practices to Requirements

For each regulation, compare what is required to what is actually happening.

```
COMPLIANCE MAP:

Regulation: [name]
| Requirement | Current Practice | Status |
|------------|-----------------|--------|
| [requirement 1] | [what is actually done] | Compliant / Gap / Partial / Unknown |
| [requirement 2] | [what is actually done] | Compliant / Gap / Partial / Unknown |
| [requirement 3] | [what is actually done] | Compliant / Gap / Partial / Unknown |

DOCUMENTATION STATUS:
- [ ] Policies exist and are current
- [ ] Procedures are documented
- [ ] Training records are maintained
- [ ] Audit trail exists
```

---

## Step 3: Identify Gaps

List every gap between requirements and current practice.

```
GAPS IDENTIFIED:

1. GAP: [description]
   Regulation: [which one]
   Requirement: [specific requirement not met]
   Current state: [what exists now]
   Severity: [Critical / Major / Minor]

2. GAP: [description]
   Regulation: [which one]
   Requirement: [specific requirement not met]
   Current state: [what exists now]
   Severity: [Critical / Major / Minor]

UNKNOWN AREAS (cannot assess without more information):
- [area] — Information needed: [what]
```

---

## Step 4: Assess Risk of Non-Compliance

For each gap, evaluate the consequences.

```
RISK ASSESSMENT:

| Gap | Likelihood of Detection | Penalty/Consequence | Reputational Impact | Overall Risk |
|-----|------------------------|--------------------|--------------------|-------------|
| [gap 1] | Low/Med/High | [fine amount, license risk, etc.] | Low/Med/High | Low/Med/High/Critical |
| [gap 2] | Low/Med/High | [fine amount, license risk, etc.] | Low/Med/High | Low/Med/High/Critical |

WORST-CASE SCENARIO: [what happens if all gaps are discovered simultaneously]
RECENT ENFORCEMENT TRENDS: [is the regulator actively enforcing? recent actions?]
```

---

## Step 5: Prioritize Remediation

Rank gaps by urgency and create a remediation sequence.

```
REMEDIATION PRIORITY:

IMMEDIATE (fix now — critical risk or active violation):
1. [gap] — Fix: [action] — Owner: [who] — By: [date]
   Cost/effort: [estimate]

SHORT-TERM (fix within 30-90 days):
1. [gap] — Fix: [action] — Owner: [who] — By: [date]
   Cost/effort: [estimate]

MEDIUM-TERM (fix within 6 months):
1. [gap] — Fix: [action] — Owner: [who] — By: [date]
   Cost/effort: [estimate]

DEPENDENCIES: [any fixes that must happen in sequence]
```

---

## Step 6: Create Compliance Checklist

Build an ongoing compliance monitoring tool.

```
COMPLIANCE CHECKLIST:

DAILY:
- [ ] [check/action]

WEEKLY:
- [ ] [check/action]

MONTHLY:
- [ ] [check/action]

QUARTERLY:
- [ ] [check/action]

ANNUALLY:
- [ ] [check/action — e.g., policy review, training renewal, audit]

TRIGGER-BASED (when events occur):
- [ ] When [event]: [required action]

RESPONSIBLE PARTY: [who owns ongoing compliance]
ESCALATION PATH: [who to notify when issues arise]
```

---

## Integration

Use with:
- `/leg` -> Apply legal reasoning to complex regulatory questions
- `/rtas` -> Assess rights affected by regulatory requirements
- `/dshb` -> Design a compliance monitoring dashboard
