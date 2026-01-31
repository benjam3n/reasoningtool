---
name: "ch - Crisis Handler"
description: "Systematic procedure for handling crises — stabilize, diagnose, communicate, resolve, and learn."
---

# Crisis Handler

**Input**: $ARGUMENTS

---

## Overview

Crises demand a different mode than normal work. Structured triage: stabilize, understand, communicate, resolve, learn. Speed matters but panic makes things worse.

## Step 0: Severity Assessment

| Factor | Options | Implication |
|--------|---------|-------------|
| Impact scope | Individual / team / org / public | Communication breadth |
| Reversibility | Reversible / partial / irreversible | Action urgency |
| Time pressure | Minutes / hours / days | Triage depth |
| Escalation risk | Stable / growing / cascading | Containment priority |

- **CRITICAL** (irreversible + cascading + minutes): Skip to Step 2 NOW
- **HIGH** (significant + growing): Steps 1-6 rapid
- **MODERATE** (contained + hours): Steps 1-6 standard
- **LOW** (manageable + days): May not need crisis procedure

## Steps

### Step 1: Situational Awareness (2 min max)
1. What happened? (facts only)
2. What is currently happening? (ongoing?)
3. Who/what is affected?
4. What's been tried?
5. What resources are available now?

### Step 2: Stabilize / Contain
1. What prevents further damage RIGHT NOW?
2. Execute minimum viable containment: isolate, activate fallbacks, restrict access
3. Verify containment worked
4. If fails → escalate immediately

### Step 3: Communicate
1. Who needs to know right now? (key stakeholders only)
2. Communicate: what happened, current status, what's being done, when next update
3. Do NOT communicate: speculation, blame, time promises
4. Set cadence (every N minutes/hours)

### Step 4: Diagnose
1. What changed before the crisis?
2. What does evidence point to?
3. → INVOKE: /rca [crisis] if time allows
4. If cause clear → fix. If not → rapid 5-Whys.

### Step 5: Resolve
1. Design the fix (not a patch)
2. Assess fix risk: could it make things worse?
3. High risk → test in isolation, prepare rollback
4. Implement and verify (original problem resolved, no new problems)

### Step 6: Stand Down and Debrief
1. Confirm fully resolved
2. Remove temporary measures (or document why they stay)
3. Communicate resolution to all stakeholders
4. Schedule post-mortem within 48 hours
5. → INVOKE: /aar [crisis summary]

## Anti-Patterns
- Panic-driven action without understanding
- Hero mode (one person handling everything)
- Blame focus instead of fixing
- Premature all-clear before verification
- No debrief (crisis resolved but nothing learned)

## When to Use
- System outages, security incidents, PR crises, project derailments
- Any disruption requiring immediate action

## Verification
- [ ] Severity assessed before acting
- [ ] Stabilized before diagnosing
- [ ] Stakeholders informed with facts
- [ ] Root cause identified
- [ ] Fix verified
- [ ] Post-mortem scheduled
