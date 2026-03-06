---
name: "but - Contrast and Objection Handler"
description: Handle "but" statements by separating main claim from objection and resolving the tension explicitly.
---

# BUT

**Input**: $ARGUMENTS

---

## Steps

1. Extract primary claim.
2. Extract objection introduced by "but".
3. Classify objection type: risk, exception, conflict, uncertainty.
4. Resolve by routing:
   - /claim for truth conflict
   - /decide for tradeoff
   - /diagnose for blocker cause

## Output

Main claim, objection, tension type, and recommended next step.
