---
name: rc5w
description: Adaptive root cause analysis. Ask "why" until you hit the root. Sometimes that's 2 levels, sometimes 12. Stop when you find the cause, not at a fixed number.
---

# Root Cause Analysis - Adaptive Why Chain

**Input**: $ARGUMENTS

---

## Core Principles

1. **Stop at the root, not at five.** "5 Whys" is a heuristic, not a rule. Some problems have shallow causes (2 whys). Some are deeply systemic (10+ whys). Keep going until you hit a cause that, if fixed, prevents recurrence.

2. **Root causes are systemic, not personal.** "Someone made a mistake" is never the root cause. Why did the system allow that mistake? Why wasn't it caught? What structural change prevents it?

3. **Multiple roots exist.** Most problems have more than one contributing cause. Branch when you find a fork — don't force a single chain.

4. **Read the chain forward.** After building the why-chain backward, read it forward (cause → effect). Does each step logically produce the next? If not, you've made a reasoning error.

---

## The Process

### 1. State the Problem

Be specific. Not "the system is slow" but "API response time exceeded 500ms for 30% of requests between 2-4pm on Tuesday."

```
PROBLEM: [Specific, observable, measurable if possible]
IMPACT: [What this causes / why it matters]
```

### 2. Ask Why (Adaptive Depth)

For each answer, ask: **"Why did this happen?"**

```
PROBLEM: [stated problem]
│
├── WHY 1: [direct cause]
│   ├── WHY 2: [cause of cause]
│   │   ├── WHY 3: [deeper cause]
│   │   │   └── ... [continue until root]
│   │   └── [BRANCH: alternative cause at this level]
│   └── [BRANCH: alternative cause at this level]
│
└── [BRANCH: alternative direct cause]
```

**At each level, check:**
- Is this the root? (Would fixing this prevent recurrence?)
- Are there alternative causes at this level? (Branch if yes)
- Is the causal link solid? (Does this actually cause the level above?)

### 3. Root Cause Test

For each candidate root cause, verify:

| Test | Question | Pass Condition |
|------|----------|---------------|
| **Prevention** | If we fix this, does the problem stop recurring? | Yes, reliably |
| **Depth** | Is there a deeper "why" that matters? | No — or the deeper why is outside our control |
| **Systemic** | Is this structural, not personal? | Yes — it's about the system, not an individual |
| **Actionable** | Can we actually change this? | Yes — with available resources |

If any test fails, keep going deeper or branch to an alternative cause.

### 4. Verify the Chain

Read the entire chain FORWARD (cause → effect):

```
[Root cause] → caused → [Level N-1] → caused → ... → caused → [Problem]
```

Each step must logically produce the next. If there's a gap, the chain is broken — investigate the gap.

### 5. Corrective Action

For each verified root cause:

```
ROOT CAUSE: [cause]
CORRECTIVE ACTION: [specific change]
PREVENTS RECURRENCE BY: [mechanism]
VERIFICATION: [how to confirm the fix works]
```

Corrective actions must address the ROOT, not the symptoms. "Add more servers" fixes the symptom (slow API). "Fix the N+1 query that causes load to scale quadratically" fixes the root.

---

## Common Patterns

| Surface Problem | Typical Shallow Fix | Actual Root (Often) |
|----------------|--------------------|--------------------|
| Bug in production | Fix the bug | No test coverage for that path |
| Missed deadline | Work harder next time | Scope wasn't defined, no check-in cadence |
| Customer complaint | Appease the customer | Process doesn't catch this class of issue |
| Performance issue | Add resources | Algorithmic complexity or architecture mismatch |
| Communication failure | Blame the person | No structural feedback loop |

---

## Pre-Completion Check

- [ ] Problem stated specifically (not vaguely)
- [ ] Why-chain continued until root cause test passes
- [ ] Branches explored where multiple causes exist
- [ ] Chain reads logically forward (cause → effect)
- [ ] Root cause is systemic, not personal
- [ ] Corrective action addresses root, not symptoms
- [ ] Verification method specified
