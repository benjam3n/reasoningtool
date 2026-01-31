---
name: lps
description: "The foundational infrastructure for treating strategy selection as theorem proving."
---

# Logical Proof System

**Input**: $ARGUMENTS

---

## Overview

The foundational infrastructure for treating strategy selection as theorem proving. Core insight: Strategies should be DERIVED from problems, not SEARCHED for. A well-derived strategy feels self-evidently correct because it follows necessarily from the problem definition.

## Steps

### Step 1: Formalize Problem as Axioms
Convert the problem into precise logical statements:

1. **Given facts** (things known to be true):
   - G1: [fact]
   - G2: [fact]
   - ...

2. **Constraints** (things that must hold):
   - C1: [constraint]
   - C2: [constraint]

3. **Objectives** (what must be achieved):
   - O1: [objective]
   - O2: [objective]

4. **Definitions** (terms with precise meaning):
   - D1: [term] = [definition]

**Quality check:** Are the axioms:
- Complete? (Is anything important missing?)
- Consistent? (Do any contradict each other?)
- Minimal? (Are any redundant?)
- Precise? (Could they be interpreted differently?)

### Step 2: Derive Intermediate Theorems
From the axioms, derive what MUST be true:

```
Theorem T1: [statement]
Proof: From G1 and G2, by [inference rule], T1 follows.

Theorem T2: [statement]
Proof: From T1 and C1, by [inference rule], T2 follows.
```

**Inference rules to use:**
- **Modus ponens**: If A, and A implies B, then B
- **Elimination**: If A and B are both needed, and B is impossible, then the approach fails
- **Disjunction**: If either A or B must hold, and A fails, then B must hold
- **Constraint propagation**: If X must be in range [a,b], and Y depends on X, then Y is constrained
- **Contradiction**: If assuming P leads to contradiction, then not-P

### Step 3: Derive Strategy
The strategy emerges from the theorems:

```
Strategy derivation:
1. From T1: We need [action] (because [theorem] requires it)
2. From T2: The action must have property [X] (because [theorem] constrains it)
3. From T3: The timing must be [Y] (because [theorem] determines it)
4. Therefore: The strategy is [specific strategy]
```

A well-derived strategy should feel INEVITABLE — given the axioms, there's no other rational conclusion.

### Step 4: Identify Proof Strength

**Strongest proofs:**
- All premises are empirically verified
- All inference steps are deductively valid
- No alternative conclusions possible

**Moderate proofs:**
- Some premises are assumptions (not verified)
- Inference steps include inductive reasoning
- Alternative conclusions exist but are less supported

**Weakest proofs:**
- Key premises are uncertain
- Inference includes analogical reasoning
- Multiple alternative conclusions are equally supported

For each step in the proof:

| Step | Premise Strength | Inference Validity | Alternatives | Overall |
|------|-----------------|-------------------|-------------|---------|
| [step] | verified/assumed/uncertain | deductive/inductive/analogical | none/few/many | strong/moderate/weak |

### Step 5: Identify Critical Assumptions
Every proof has weakest links:

1. Which premises are ASSUMED rather than VERIFIED?
2. Which inferences are INDUCTIVE rather than DEDUCTIVE?
3. If any of these were wrong, would the strategy change?
4. Can the critical assumptions be tested?

```
CRITICAL ASSUMPTIONS:
| # | Assumption | If Wrong | Impact on Strategy | Testable? |
|---|-----------|----------|-------------------|-----------|
| 1 | [assumption] | [consequence] | [strategy changes/survives] | [Y/N] |
```

### Step 6: Compare to Alternative Derivations
Are there other valid derivations from the same axioms?

1. What if we prioritize different objectives?
2. What if we interpret constraints differently?
3. What if we add/remove an axiom?
4. Do alternative derivations reach different strategies?

### Step 7: Report
```
LOGICAL PROOF:
Axioms: [N] given facts, [N] constraints, [N] objectives

Derivation:
[step-by-step proof from axioms to strategy]

Derived strategy: [what follows necessarily]
Proof strength: [strong / moderate / weak]

Critical assumptions:
1. [assumption] — if wrong: [impact]

Weakest link: [which step is least certain]
Alternative derivations: [how many, how different]

Confidence: [high if strong proof with few assumptions,
             low if weak proof with many assumptions]
```

## When to Use
- When you need to formalize a problem as logical axioms
- When you need to derive strategies deductively
- When you need to validate logical soundness of a reasoning chain
- When you want strategies that feel "necessary" rather than "optional"
- → INVOKE: /dsd (deductive strategy derivation) for the derivation process
- → INVOKE: /tp (truth propagation) for tracking truth through the proof

## Verification
- [ ] Problem axioms are exhaustive (nothing important missing)
- [ ] Each inference step is explicitly justified
- [ ] Weakest links are identified
- [ ] Critical assumptions are marked
- [ ] Proof strength is honestly assessed
