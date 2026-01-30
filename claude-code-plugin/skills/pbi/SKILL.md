---
name: "pbi - Problem Identification"
description: "Before solving, identify the RIGHT problem at the RIGHT level. Includes clarification vs substitution checking to prevent problem drift."
context: fork
---

# Problem Identification

**Input**: $ARGUMENTS

---

## Overview

Before solving, identify:
- Is this the RIGHT problem? (not the obvious one)
- At the RIGHT level? (not too surface, not too abstract)
- At the RIGHT time? (now vs later vs never)
- In the RIGHT order? (dependencies, prerequisites)
- With RIGHT prioritization? (effort/impact)

ARAW is a tool for problem identification:
- ASSUME RIGHT: This IS the problem → what follows?
- ASSUME WRONG: This ISN'T the real problem → what is?

---

## CRITICAL: Problem Reframing vs Problem Substitution

This skill often REFRAMES problems. Reframing is a form of substitution that requires awareness.

### Step 0: Capture Original Problem Statement

```
ORIGINAL PROBLEM (verbatim): "[user's exact words]"
```

When we identify a "real" problem that differs from the stated problem, check:

**Is this Clarification or Substitution?**

| Clarification (Same Problem) | Substitution (Different Problem) |
|------------------------------|----------------------------------|
| Making the problem more specific | Changing what problem we're solving |
| Identifying root cause of STATED problem | Identifying a DIFFERENT problem |
| "Your problem is actually more specific" | "Your REAL problem is something else" |

**The Test**: If we solve the reframed problem but NOT the original, would user feel:
- "That's what I meant" → CLARIFICATION (proceed)
- "But I still have my original problem" → SUBSTITUTION (get consent)

### Reframing Consent Template

If reframing to a different problem:

```
PROBLEM REFRAME PROPOSAL
========================
You stated this problem: "[original]"

I'm identifying a different problem: "[reframed]"

This is a DIFFERENT problem because:
- Solving the reframe [does/doesn't] solve the original
- [Specific difference]

Options:
1. [ ] Solve the reframed problem (I understand it's different)
2. [ ] Focus on my original problem
3. [ ] Explore both problems
```

---

## Core Principle

The obvious problem is often not the real problem.
The real problem is often:
- One level upstream (what caused this symptom?)
- One level downstream (why does this symptom matter?)
- In a different domain (system issue, not local issue)
- Not actually a problem (assumption we haven't questioned)

**BUT**: Identifying a "better" problem without consent is substitution.

---

## Steps

### Step 1: State the obvious problem
Write down what seems to be the problem, without filtering

**Capture verbatim** - this is what we check reframes against.

### Step 2: Question the framing
Apply ARAW: ASSUME WRONG that this is the real problem
What alternative framings exist?
What's upstream of this symptom?

### Step 3: Identify the level
Is this symptom, proximate cause, root cause, systemic, or assumption?
What level should we solve at?

### Step 4: Verify problem is actual
Is this ACTUAL (happening now)?
Or ANTICIPATED (will happen if...)?
Or IMAGINED (might maybe happen)?

### Step 5: Check timing
Should we solve now, later, or never?
What's the cost of waiting?
Are we ready to solve it?

### Step 6: Check order
What must be solved first?
What does solving this unlock?
Are there dependencies?

### Step 7: Prioritize
What's the effort/impact?
Is this compounding?
What's the risk tolerance?

### Step 8: Decide
SOLVE NOW: Right problem, right level, right time, high priority
DEFER: Right problem, wrong time or blocked by dependencies
REFRAME: Wrong problem or wrong level, go back to step 1 **WITH CONSENT CHECK**
DROP: Not actually a problem, or too low priority

### Step 9: Verify No Silent Substitution

Before concluding:

| Check | Pass? |
|-------|-------|
| Final problem statement compared to original? | |
| If different: classified as clarification or substitution? | |
| If substitution: user consent obtained? | |
| User would recognize final problem as "their problem"? | |

---

## Verification
- [ ] Original problem captured verbatim
- [ ] ARAW applied (both ASSUME RIGHT and ASSUME WRONG)
- [ ] Problem level identified (symptom/proximate/root/systemic)
- [ ] Timing assessed (now/later/never)
- [ ] If reframed: clarification vs substitution checked
- [ ] If substitution: consent obtained
- [ ] Final decision made (SOLVE/DEFER/REFRAME/DROP)

---

## Integration Points
- Often invoked from: /pce, /gu
- Routes to: /rca (if solving), /rc5w
- Gate: clarification_vs_substitution_gate (when reframing)
- Related: /lpd, /sya