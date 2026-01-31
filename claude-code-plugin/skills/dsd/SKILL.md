---
name: dsd
description: "Derive strategies by working backward from success criteria to required actions."
---

# Deductive Strategy Discovery

**Input**: $ARGUMENTS

---

## Overview

Derive strategies by working backward from success criteria to required actions. Instead of brainstorming "what could work?" this procedure asks: "What MUST be done to satisfy the problem axioms?"

The output is strategies with explicit logical derivations showing WHY they are necessary, not just possible.

## Steps

### Step 1: Extract Problem Axioms
Convert the problem/goal into formal axioms:

**Success criteria** (what must be true when done):
- S1: [condition that must hold]
- S2: [condition that must hold]

**Constraints** (what cannot be violated):
- C1: [limitation]
- C2: [limitation]

**Givens** (facts about the current situation):
- G1: [what's true now]
- G2: [what's true now]

**Quality check:** Are the axioms complete? Ask: "If all success criteria are met and no constraints are violated, is the goal achieved?" If not, axioms are incomplete.

### Step 2: Derive Necessary Requirements
From each success criterion, work backward:

```
S1 requires: [what must be done to make S1 true]
  which requires: [predecessor condition]
    which requires: [predecessor condition]
      ...until you reach something you can DO
```

For each requirement chain:
- Is this requirement NECESSARY (can't achieve S without it)?
- Or just SUFFICIENT (one way to achieve S, but not the only way)?
- Mark each: [NECESSARY] or [SUFFICIENT]

### Step 3: Identify Strategy Space
From the requirement chains, map the choice points:

```
STRATEGY SPACE:
To achieve S1:
  Path A: [requirement chain A] — NECESSARY
  Path B: [requirement chain B] — SUFFICIENT (alternative exists)
    Alternative B1: [variant]
    Alternative B2: [variant]
```

Where chains are NECESSARY: no choice — must do it.
Where chains have alternatives: these are strategy choice points.

### Step 4: Apply Elimination Reasoning
For each choice point, eliminate options:

1. Does option violate any constraint? → ELIMINATE
2. Does option require a resource not available? → ELIMINATE (or flag for /cnw)
3. Does option conflict with another necessary requirement? → ELIMINATE
4. Does option have strictly lower merit than another on all dimensions? → ELIMINATE (dominated)

After elimination: what remains?
- One option → Strategy is determined
- Multiple options → Need evaluation (/dse)
- No options → Problem may be infeasible — revisit axioms

### Step 5: Build Strategy Proofs
For each surviving strategy, construct the full proof:

```
STRATEGY PROOF:
Theorem: Strategy [X] achieves goal [G]

Proof:
1. Goal requires S1, S2, S3 [by definition]
2. S1 requires R1 [derived in Step 2]
3. R1 is achieved by action A1 [only viable option after elimination]
4. S2 requires R2 [derived in Step 2]
5. R2 is achieved by action A2 [chosen from alternatives because...]
6. S3 requires R3 [derived in Step 2]
7. R3 is achieved by action A3 [necessary — no alternative]
8. A1, A2, A3 do not violate C1, C2 [checked in Step 4]
9. Therefore: Strategy {A1, A2, A3} achieves {S1, S2, S3} ∎

Proof strength: [NECESSARY / SUFFICIENT / CONTINGENT]
Key assumption: [weakest link in the proof]
```

### Step 6: Classify Strategy Confidence

| Level | Criteria | Meaning |
|-------|---------|---------|
| **Proven necessary** | All steps are necessary, all premises verified | Only possible strategy |
| **Proven sufficient** | Steps will achieve goal, premises verified | Will work, but alternatives exist |
| **Contingent** | Steps will achieve goal IF assumptions hold | Depends on untested assumptions |
| **Plausible** | Reasoning is sound but premises are uncertain | Probably works |
| **Speculative** | Significant gaps in reasoning | Might work |

### Step 7: Report
```
DEDUCTIVE STRATEGY DISCOVERY:
Goal: [what]
Axioms: [N] success criteria, [N] constraints, [N] givens

Derivation:
[Key reasoning steps]

Strategy: [the derived approach]
Proof strength: [level]
Key assumption: [weakest link]

Necessary actions: [things that MUST be done regardless of strategy choice]
Choice points: [where alternatives exist]
Eliminated options: [what was ruled out and why]

Confidence: [level with justification]
What would upgrade confidence: [what evidence/test would help]
```

## When to Use
- At the start of strategy discovery
- When existing strategies feel like "guesses"
- When you want strategies that feel self-evidently correct
- When you need high confidence before committing resources
- → INVOKE: /dse (deductive strategy evaluation) for evaluating derived strategies
- → INVOKE: /lps (logical proof system) for formal proof infrastructure
- → INVOKE: /dari (deductive adversarial review integration) for adversarial testing

## Verification
- [ ] All success criteria traced to required actions
- [ ] Constraints checked against all strategies
- [ ] Necessity vs sufficiency explicitly stated for each requirement
- [ ] Critical assumptions identified
- [ ] At least one strategy has proof strength of SUFFICIENT or higher
