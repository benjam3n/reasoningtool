---
name: dse
description: "Evaluate strategies based on the logical soundness of their derivation."
---

# Deductive Strategy Evaluation

**Input**: $ARGUMENTS

---

## Overview

Evaluate strategies based on the logical soundness of their derivation. Determines whether a strategy is logically valid (conclusions follow), sound (premises true AND inferences valid), complete (no gaps), and necessary vs sufficient.

Strategies that pass deductive evaluation have the highest confidence because their correctness follows from the problem definition itself.

## Steps

### Step 1: Check Logical Validity
For each inference step in the strategy's derivation:

| Step | Premise(s) | Inference | Conclusion | Valid? |
|------|-----------|-----------|-----------|--------|
| 1 | [what's assumed] | [rule applied] | [what follows] | Y/N |
| 2 | | | | |

**Validity check:** Does the conclusion NECESSARILY follow from the premises using the stated inference rule?
- If yes → Valid step
- If no → Identify the gap: what additional premise would make it valid?

### Step 2: Check Soundness
For each premise used in the derivation:

| Premise | Type | Truth Status | Evidence |
|---------|------|-------------|---------|
| [premise] | axiom/observation/assumption/definition | true/uncertain/false | [source] |

**Soundness = validity + true premises.** A valid argument with false premises produces unreliable conclusions.

### Step 3: Identify Weaknesses
Categorize each weakness found:

| Weakness | Type | Impact | Fixable? |
|----------|------|--------|---------|
| [weakness] | invalid step / uncertain premise / missing step / scope error | strategy collapses / weakened / unaffected | Y/N |

**Weakness types:**
- Invalid inference: Conclusion doesn't follow from premises
- Uncertain premise: Premise truth is unknown or debated
- Missing step: Gap in reasoning chain
- Scope error: Conclusion is broader than premises support
- Equivocation: Same term used with different meanings
- Circular reasoning: Conclusion is also a premise

### Step 4: Assess Necessity Level
How strong is the connection between strategy and success?

| Level | Description | Test |
|-------|------------|------|
| **Necessary and sufficient** | This is the ONLY strategy that works, AND it guarantees success | No alternative exists AND no failure mode exists |
| **Sufficient** | This strategy guarantees success, but alternatives exist | Will work, others might too |
| **Necessary** | Must include this, but it alone isn't enough | Required but not complete |
| **Contributory** | Increases probability of success but doesn't guarantee | Helps but not decisive |
| **Irrelevant** | No logical connection to success | Doesn't help |

### Step 5: Assign Proof Level
Based on Steps 1-4:

| Proof Level | Criteria |
|------------|---------|
| **Level 4 — Proven** | All steps valid, all premises true, no gaps, necessary and sufficient |
| **Level 3 — Strong** | All steps valid, most premises true, minor gaps, sufficient |
| **Level 2 — Supported** | Most steps valid, key premises plausible, some gaps, contributory |
| **Level 1 — Suggestive** | Logic is reasonable, premises uncertain, significant gaps |
| **Level 0 — Unproven** | Logic has errors, premises unverified, or major gaps |

### Step 6: Provide Upgrade Path
For strategies below Level 4, specify what would raise them:

```
UPGRADE PATH:
Current level: [X]
To reach Level [X+1]:
1. [specific action] — fixes: [weakness] — cost: [effort]
2. [specific action] — fixes: [weakness] — cost: [effort]

Most cost-effective upgrade: [which action gives most level-improvement per effort]
```

### Step 7: Report
```
DEDUCTIVE STRATEGY EVALUATION:
Strategy: [what was evaluated]

Validity: [N] of [N] steps valid
Soundness: [N] of [N] premises verified
Completeness: [no gaps / minor gaps / significant gaps]
Necessity level: [necessary and sufficient / sufficient / necessary / contributory]

Proof level: [0-4] — [label]

Weaknesses:
| # | Weakness | Type | Impact | Fix |
|---|----------|------|--------|-----|
| 1 | [weakness] | [type] | [impact] | [fix] |

Upgrade path: [what would raise the proof level]
Overall confidence: [high / moderate / low — with justification]
```

## When to Use
- After deductive strategy discovery (/dsd)
- Before committing to a strategy
- When comparing strategies on logical strength
- When identifying weakest points in strategy reasoning
- → INVOKE: /dsd (deductive strategy discovery) to derive the strategy first
- → INVOKE: /dari (deductive adversarial review) for adversarial testing

## Verification
- [ ] Every inference step explicitly checked for validity
- [ ] Every premise categorized and assessed for truth
- [ ] Weaknesses prioritized by impact
- [ ] Proof level assigned with explicit justification
- [ ] Upgrade path provided for sub-Level 4 strategies
