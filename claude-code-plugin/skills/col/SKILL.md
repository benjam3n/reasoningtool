---
name: "col - Collaboration Design"
description: Designs how a group of people should work together — roles, communication, decisions, handoffs, and accountability.
---

# Collaboration Design

**Input**: $ARGUMENTS

---

## Step 1: Define the Goal

What is this group trying to accomplish together?

```
GOAL: [one sentence — the shared objective]
TIMELINE: [when does this need to be done?]
CONSTRAINTS: [budget, tools, geography, org structure, etc.]
SUCCESS LOOKS LIKE: [concrete outcome that means "we did it"]
```

---

## Step 2: Map Roles

Identify every person or role involved. For each, define what they own.

Use RACI where helpful:
- **R** (Responsible) — does the work
- **A** (Accountable) — makes the call, owns the outcome
- **C** (Consulted) — gives input before a decision
- **I** (Informed) — told after a decision

```
ROLES:
| Role/Person | Responsible For | Decision Rights | Key Deliverable |
|-------------|----------------|-----------------|-----------------|
| [name/role] | [what they do] | [what they can decide alone] | [what they produce] |
| ... | ... | ... | ... |
```

SKIP: If there are only 2 people, a simple "who does what" split is enough.

---

## Step 3: Communication Design

Define how and when people talk to each other.

```
COMMUNICATION CADENCE:
| Type | Frequency | Who | Format | Purpose |
|------|-----------|-----|--------|---------|
| Standup/check-in | [daily/weekly/etc.] | [who] | [sync/async] | [why] |
| Decision review | [as needed/weekly] | [who] | [sync/async] | [why] |
| Progress update | [frequency] | [who] | [format] | [why] |

DEFAULT CHANNEL: [where most communication happens]
ESCALATION PATH: [who to go to when stuck, and how]
```

Rule: Every meeting/touchpoint must have a purpose. If you can't state it, cut it.

---

## Step 4: Decision Rights

Who decides what? This is where most collaboration breaks down.

```
DECISION MAP:
| Decision Type | Who Decides | Who Must Be Consulted | Tiebreaker |
|--------------|-------------|----------------------|------------|
| [type] | [person/role] | [person/role] | [person/role] |
| ... | ... | ... | ... |

DEFAULT RULE: If a decision isn't listed, [who] decides.
```

---

## Step 5: Handoff Procedures

Where does work pass from one person to another? Each handoff is a failure point.

```
HANDOFFS:
1. [Person A] -> [Person B]: [what gets handed off]
   - FORMAT: [how — document, PR, email, ticket, etc.]
   - DEFINITION OF DONE: [when A's part is complete]
   - ACCEPTANCE: [how B confirms receipt and readiness]

2. [Person A] -> [Person C]: [what gets handed off]
   ...
```

---

## Step 6: Accountability

How does the group know if collaboration is working?

```
ACCOUNTABILITY:
- CHECK-IN CADENCE: [how often the group reviews if the process is working]
- LEADING INDICATOR: [early sign that collaboration is healthy or breaking]
- FAILURE SIGNAL: [what tells you the process needs to change]
- ADJUSTMENT RULE: [when and how to change the process if it's not working]
```

---

## Integration

Use with:
- `/conr` -> When collaboration has broken down and needs conflict resolution
- `/to` -> When the collaboration plan needs a detailed task breakdown
- `/pri` -> When the group needs to prioritize what to work on together
- `/de` -> When the collaboration is for a project that needs full design
