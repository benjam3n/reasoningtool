---
name: gee
description: "Systematic execution of GOSM gates with enforcement."
---

# Gate Execution Engine

**Input**: $ARGUMENTS

---

## Overview

Systematic execution of GOSM gates with enforcement. Current problem: Gates are YAML documents (advice), not automated checks. Rigor depends entirely on user discipline.

This procedure makes gates mandatory checkpoints that must pass before proceeding to next phase.

## Steps

### Step 1: Identify Gates to Execute
1. What project/process is being gated?
2. What phase is being completed?
3. Which gate(s) apply at this transition?
4. What are the gate criteria?

If no formal gates exist, derive them:
- What MUST be true before proceeding?
- What would make proceeding dangerous?
- What has gone wrong at this transition in the past?

### Step 2: Prepare Gate Evidence
For each gate criterion, gather:

| Criterion | Evidence Required | Evidence Available | Gap |
|-----------|------------------|-------------------|-----|
| [what must be true] | [what would prove it] | [what we have] | [what's missing] |

Rules:
- No self-certification ("I think it's fine" is not evidence)
- Evidence must be EXTERNAL to the person requesting passage
- Absence of evidence is not evidence of absence — "no bugs found" ≠ "no bugs exist"

### Step 3: Execute Gate Check
For each criterion, evaluate:

```
GATE CHECK:
Criterion: [statement]
Evidence: [what supports it]
Result: PASS | FAIL | CONDITIONAL | INSUFFICIENT
Confidence: high | medium | low
Notes: [any caveats]
```

**Result definitions:**
- PASS: Evidence clearly supports the criterion
- FAIL: Evidence contradicts the criterion
- CONDITIONAL: Passes with specific conditions/limitations
- INSUFFICIENT: Cannot determine — need more evidence

### Step 4: Make Gate Decision

| Pattern | Decision | Action |
|---------|----------|--------|
| All PASS | OPEN gate | Proceed to next phase |
| Any FAIL | HOLD gate | Fix failures, re-check |
| All PASS + CONDITIONAL | CONDITIONAL OPEN | Proceed with conditions tracked |
| Any INSUFFICIENT | HOLD for evidence | Gather missing evidence, re-check |
| Mix of PASS and FAIL | HOLD gate | Fix failures, don't proceed on partial pass |

**Anti-patterns to watch for:**
- "We'll fix it in the next phase" — if the gate catches it, fix it NOW
- "It's close enough" — gates are binary, not gradients
- "We don't have time" — schedule pressure is not a gate criterion
- "The important ones pass" — ALL criteria matter or remove the criterion

### Step 5: Document Gate Record

```
GATE RECORD:
Project: [name]
Gate: [which gate]
Phase transition: [from] → [to]
Date: [when executed]

Results:
| # | Criterion | Result | Evidence | Notes |
|---|-----------|--------|----------|-------|
| 1 | [criterion] | PASS/FAIL | [evidence] | [notes] |

Decision: OPEN / HOLD / CONDITIONAL
Conditions (if conditional): [list]
Failures (if hold): [list with required fixes]
Next review date (if hold): [when]
```

### Step 6: Enforce Follow-Through
If gate is HOLD:
1. Assign each failure to someone responsible
2. Define what "fixed" looks like (concrete, testable)
3. Schedule re-check
4. Do NOT allow workarounds that bypass the gate

If gate is CONDITIONAL:
1. Track each condition as an open item
2. Define when each condition must be resolved
3. Define what happens if condition isn't met by deadline

## When to Use
- At any phase transition in a project
- Before releasing software, hardware, or deliverables
- Before making irreversible decisions
- When discipline is needed to prevent cutting corners
- → INVOKE: /gaca (gate auditing) for gate quality checks
- → INVOKE: /mcg (mention completeness gate) for specific gate types

## Verification
- [ ] All gate criteria identified
- [ ] Evidence gathered for each criterion (not self-certification)
- [ ] Each criterion scored PASS/FAIL/CONDITIONAL/INSUFFICIENT
- [ ] Gate decision follows the decision table (no exceptions)
- [ ] Failures assigned with clear fix criteria
- [ ] Gate record documented
