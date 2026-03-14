---
name: "acaus - Assume Causation"
description: "Force the assumption that X actually causes Y (not just correlates). Trace the mechanism, test the claim, and identify what must be true for causation to hold."
output:
  format: "prose"
---

# Assume Causation

**Input**: $ARGUMENTS

---

## Core Move

Take a suspected causal relationship and **assume it's real causation**, not correlation, coincidence, or confounding. Then trace what that requires and what it predicts.

The most common reasoning error is mistaking correlation for causation. This skill forces you to take causation seriously and see what it demands.

---

## Procedure

### Step 1: State the Causal Claim
```
CAUSE (X): [what supposedly causes]
EFFECT (Y): [what supposedly results]
CLAIM: X causes Y
```

### Step 2: Force the Assumption
"X genuinely causes Y. The causal arrow runs from X to Y."

### Step 3: Trace Causal Requirements
If X causes Y, then ALL of these must hold (Bradford Hill criteria, adapted):

| Criterion | Assessment |
|-----------|------------|
| **Mechanism** | How does X produce Y? What's the pathway? |
| **Temporal order** | Does X precede Y? Always? |
| **Dose-response** | More X → more Y? |
| **Consistency** | Does X→Y hold across different contexts? |
| **Specificity** | Does X cause Y specifically, or everything? |
| **Strength** | How strong is the association? |
| **Coherence** | Does X→Y fit with what else we know? |
| **Experiment** | Manipulating X changes Y? |
| **Reversibility** | Removing X removes Y? |

### Step 4: Test Alternative Explanations
If NOT causation, what else?

1. **Reverse causation**: Y causes X
2. **Common cause**: Z causes both X and Y
3. **Coincidence**: No real connection
4. **Mediation**: X → Z → Y (X doesn't directly cause Y)
5. **Selection bias**: We only see X and Y together due to how we're looking

### Step 5: Synthesize
```
CAUSAL CLAIM: X causes Y
ASSUMING CAUSATION:
  Mechanism: [pathway]
  Strongest evidence: [which criteria met]
  Weakest point: [which criteria fail]
  Best alternative explanation: [most plausible non-causal account]
CAUSATION CONFIDENCE: [high/medium/low]
DECISIVE TEST: [what would settle it]
```

---

## When to Use
- Testing whether a correlation is actually causal
- Designing interventions (need real causation, not correlation)
- Evaluating claims of the form "X causes Y"

## Integration
- Pair with `/arel` for general relationship analysis
- Follow with `/ht` to design a causal test
- Use `/aop` to assume the opposite (X does NOT cause Y)
