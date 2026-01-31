---
name: dari
description: "Bridges the deductive strategy system with adversarial review testing for maximum strategy confidence."
---

# Deductive Adversarial Review Integration

**Input**: $ARGUMENTS

---

## Overview

Bridges the deductive strategy system with adversarial review testing. The deductive system provides logical derivations (proofs). Builder-breaker provides adversarial attacks. Together, they produce strategies that are both logically derived (not guessed) AND battle-tested (survived attacks).

This is the highest level of strategy confidence.

## Steps

### Step 1: Derive Strategy Deductively
First, derive the strategy using the logical proof system:

1. → INVOKE: /lps (logical proof system) with the input
2. Obtain:
   - The derived strategy
   - The axioms it rests on
   - The inference chain
   - The proof strength
   - The critical assumptions

```
DEDUCTIVE OUTPUT:
Strategy: [what was derived]
Proof strength: [strong / moderate / weak]
Critical assumptions:
1. [assumption] — confidence: [H/M/L]
2. [assumption] — confidence: [H/M/L]
Weakest inference: [which step is least certain]
```

### Step 2: Convert Weaknesses to Attack Targets
From the deductive analysis, identify what to attack:

| Attack Target | Source | Why It's Vulnerable |
|--------------|--------|-------------------|
| [assumption 1] | Critical assumption | If false, strategy collapses |
| [inference X] | Weakest step | Relies on [type of reasoning] |
| [axiom Y] | Problem definition | May not be complete/accurate |
| [missing factor] | Completeness gap | Not in the proof at all |

### Step 3: Run Adversarial Review
→ INVOKE: /advr (adversarial review) targeting the identified weaknesses:

**Builder presents:** The derived strategy with its proof chain
**Breaker attacks:** Each identified vulnerability, plus any additional weaknesses found

For each attack:
```
ATTACK: [description]
Target: [which part of the proof]
Severity: [fatal / serious / minor]
Builder response: [refute / repair / reinforce / concede]
Proof impact: [proof holds / proof weakened / proof collapses]
```

### Step 4: Update Proof Based on Attacks
After adversarial review, reassess the derivation:

| Original Assessment | After Attack | Change |
|-------------------|-------------|--------|
| Proof strength: [X] | Proof strength: [Y] | [stronger/same/weaker] |
| Assumption 1: [confidence] | Assumption 1: [new confidence] | [up/same/down] |
| Assumption 2: [confidence] | Assumption 2: [new confidence] | [up/same/down] |
| Strategy: [derived] | Strategy: [revised?] | [unchanged/modified/abandoned] |

### Step 5: Classify Final Confidence

| Level | Criteria | Description |
|-------|---------|-------------|
| **Proven** | Strong proof + survived all attacks | As confident as we can be |
| **Robust** | Moderate proof + survived most attacks | High confidence, some uncertainty |
| **Plausible** | Weak proof but survived key attacks | Reasonable but not certain |
| **Fragile** | Strong proof but fell to attacks | Logically sound but practically vulnerable |
| **Dubious** | Weak proof and fell to attacks | Low confidence — reconsider |
| **Refuted** | Proof collapsed under attack | Strategy should be abandoned |

### Step 6: Handle Each Outcome

**If Proven/Robust:** Proceed with the strategy. Document the proof and attacks it survived.

**If Plausible:** Proceed cautiously. Identify what additional evidence would upgrade confidence. Test the weakest assumptions first.

**If Fragile:** The logic is sound but reality may not cooperate. Design experiments to test the vulnerable assumptions. Have contingency plans.

**If Dubious/Refuted:** Do NOT proceed. Either:
- Find new axioms and re-derive
- Abandon this approach and try a different strategy
- Gather more information before re-attempting

### Step 7: Report
```
DEDUCTIVE-ADVERSARIAL INTEGRATION:
Strategy: [what was analyzed]

Deductive phase:
- Proof strength: [level]
- Critical assumptions: [N]
- Weakest inference: [which]

Adversarial phase:
- Attacks attempted: [N]
- Attacks survived: [N]
- Fatal attacks: [N]
- Strategy modified by attacks: [Y/N — how]

Final confidence: [Proven / Robust / Plausible / Fragile / Dubious / Refuted]

If proceeding:
- Strategy: [final version after modifications]
- Key risk: [weakest surviving point]
- Monitor: [what to watch for]

If not proceeding:
- Why: [which attacks were fatal]
- Alternative: [what to do instead]
```

## When to Use
- After deductive strategy discovery
- Before final strategy selection on high-stakes decisions
- When you need maximum confidence in a strategy
- → INVOKE: /lps (logical proof system) for the deductive phase
- → INVOKE: /advr (adversarial review) for the attack phase
- → INVOKE: /cv (convergent validation) for additional validation methods

## Verification
- [ ] Deductive derivation completed BEFORE adversarial review
- [ ] Weaknesses from derivation used as attack targets
- [ ] All attack types attempted (evidence, reasoning, completeness)
- [ ] Proof level updated based on attacks survived
- [ ] Final confidence level is honest assessment
- [ ] Next steps appropriate to confidence level
