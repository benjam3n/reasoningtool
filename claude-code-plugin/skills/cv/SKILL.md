---
name: "cv - Convergent Validation"
description: "Solve the infinite critic problem by using multiple independent validation criteria — accept when they converge, investigate when they diverge."
---

# Convergent Validation

**Input**: $ARGUMENTS

---

## Overview

Any single critic can be criticized. The infinite regress of "but how do you validate the validator?" never terminates. The solution: don't rely on one criterion. Apply multiple INDEPENDENT validation methods. If they converge on the same answer, confidence is warranted. If they diverge, that's where the real questions are.

## Steps

### Step 1: State What's Being Validated
1. What claim, output, or decision needs validation?
2. What would "valid" mean concretely?

### Step 2: Identify Independent Validation Methods
Generate 3+ methods that rely on different assumptions:
- **Empirical**: Does evidence support it?
- **Logical**: Does the reasoning hold?
- **Predictive**: Does it predict correctly?
- **Expert consensus**: Do knowledgeable people agree?
- **Adversarial**: Does it survive attack? (→ /stc, /advr)
- **Internal consistency**: Does it contradict itself?
- **Cross-domain**: Does it hold in analogous situations?

Key: methods must be INDEPENDENT (one passing doesn't make another more likely to pass)

### Step 3: Apply Each Method
For each validation method:
1. Apply it to the subject
2. Result: PASS / FAIL / AMBIGUOUS
3. Confidence in this method's result: high / medium / low

### Step 4: Check Convergence

| Pattern | Meaning | Action |
|---------|---------|--------|
| All converge PASS | High confidence valid | Accept |
| All converge FAIL | High confidence invalid | Reject |
| Most PASS, one FAIL | Investigate the failure — is it the method or the subject? | Investigate |
| Mixed | Genuine uncertainty | Refine methods or accept uncertainty |
| All AMBIGUOUS | Methods aren't powerful enough for this subject | Find better methods |

### Step 5: Report
```
CONVERGENT VALIDATION:
Subject: [what was validated]

| Method | Result | Confidence |
|--------|--------|------------|
| [method] | PASS/FAIL | H/M/L |

Convergence: [all agree / mostly agree / mixed / divergent]
Verdict: [valid / invalid / uncertain]
Key divergence: [if any methods disagree, which and why]
```

## When to Use
- High-stakes decisions needing rigorous validation
- When "how do you know?" questions persist
- When single validation methods feel insufficient

## Verification
- [ ] 3+ independent methods used
- [ ] Methods genuinely independent (different assumptions)
- [ ] Convergence/divergence pattern analyzed
- [ ] Divergences investigated (not ignored)
