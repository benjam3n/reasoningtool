---
name: "av - Assumption Verification"
description: "Systematically verify assumptions by classifying type, determining verification method, executing, and updating confidence."
---

# Assumption Verification

**Input**: $ARGUMENTS

---

## Overview

Assumptions are beliefs treated as true without verification. This extracts them, classifies by type, determines the right verification method, executes verification, and updates confidence. Different from /aex (extraction only) — this goes through to verification.

## Steps

### Step 1: Extract Assumptions
1. Identify the claim, plan, or argument to examine
2. Ask: "What must be true for this to work?"
3. List every assumption: explicit (stated), implicit (unstated but required), background (so obvious they're invisible)
4. Number each: A1, A2, A3...

### Step 2: Classify Each Assumption

| Type | Verification Method |
|------|-------------------|
| **Empirical** (facts, data) | Evidence, measurement, observation |
| **Logical** (if-then, definitions) | Logical analysis, proof |
| **Normative** (should, ought) | Value elicitation, stakeholder consensus |
| **Causal** (cause-effect) | Experiment, counterfactual analysis |
| **Statistical** (distributions, rates) | Data analysis, sampling |
| **Practical** (we can, they will) | Testing, prototyping, expert consultation |

### Step 3: Prioritize
Rate each:
1. **Criticality**: If wrong, does everything fail? (H/M/L)
2. **Confidence**: How sure it's true? (H/M/L)
3. **Verifiability**: Can we check? (easy/hard/impossible)
4. Priority = high criticality + low confidence + easy verification

### Step 4: Execute Verification
For each prioritized assumption:
1. Apply the method matched to its type
2. Record findings
3. Update status: VERIFIED / REFUTED / WEAKENED / UNVERIFIABLE / CONDITIONAL

### Step 5: Report
```
ASSUMPTION VERIFICATION REPORT
Subject: [what was examined]

| # | Assumption | Type | Critical | Status | Evidence |
|---|-----------|------|----------|--------|----------|
| A1 | [text] | [type] | [H/M/L] | [status] | [summary] |

Critical findings: [refuted/weakened high-criticality assumptions]
Impact: [what changes based on findings]
```

## When to Use
- Before committing to a plan or strategy
- When a decision rests on uncertain premises
- After /aex extracts assumptions that need checking

## Verification
- [ ] All assumptions extracted (explicit, implicit, background)
- [ ] Each classified by type
- [ ] Prioritized by criticality x confidence x verifiability
- [ ] Each has a status after verification
- [ ] High-criticality refuted assumptions flagged
