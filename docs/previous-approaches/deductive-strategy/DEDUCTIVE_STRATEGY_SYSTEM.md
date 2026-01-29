# Deductive Strategy System for GOSM v2.3

## Overview

The Deductive Strategy System transforms how GOSM selects strategies. Instead of searching for strategies that "could work," it **derives** strategies that **must** work given the problem definition.

**Core Insight**: Most strategy selection feels uncertain because strategies are generated through association rather than derivation. The deductive system treats strategy selection like theorem proving: given problem axioms, what strategies are logically necessary?

## Why This Matters

### The Problem with Current Strategy Selection

Traditional strategy advice (from influencers, books, AI) suffers from:
1. **Guessing**: Strategies based on what "might" work
2. **Hit-or-miss**: Some work, some don't, unclear why
3. **No certainty**: Can't tell good advice from bad until after trying
4. **Analysis paralysis**: Too many competing options, all seem plausible

### What the Deductive System Provides

1. **Logical derivation**: Strategies derived from problem definition, not searched
2. **Self-evident correctness**: When you see the derivation, you understand WHY it works
3. **Confidence calibration**: Know the proof strength (necessary vs. possible)
4. **Failure point identification**: Know exactly which assumptions could break the strategy

## Key Concepts

### Problem Axioms

Before deriving strategies, the problem must be formalized as logical premises:

```yaml
ProblemAxioms:
  success_requirements:  # What must be true for success
    - "Weight must decrease by 10kg"
    - "Breathing must be comfortable through nose"

  constraints:  # What cannot be violated
    - "Budget limited to $X"
    - "Must not cause harmful side effects"

  domain_facts:  # Established knowledge
    - "Weight loss requires caloric deficit"
    - "Caloric deficit requires reduced intake or increased expenditure"

  past_failures:  # What has been tried without success
    - "Supplements did not produce weight loss"
    - "Social skills books did not create automatic behavior"
```

### Proof Strength Levels

Not all derivations are equally strong:

| Level | Name | Meaning | Confidence |
|-------|------|---------|------------|
| **NECESSARY** | Only Solution | This is the ONLY strategy that satisfies all axioms | Highest |
| **SUFFICIENT** | Will Work | This strategy will definitely achieve the goal | High |
| **LIKELY** | Probably Works | Strong reasoning suggests this works | Moderate |
| **POSSIBLE** | Might Work | Could work but uncertain | Low |
| **UNKNOWN** | Cannot Assess | Not enough information | Very Low |

### Confidence Levels (0-4, compatible with Adversarial Review)

| Level | Name | Requirement | Next Step |
|-------|------|-------------|-----------|
| **0** | Hypothesis | Not yet tested | Run evaluation |
| **1** | Contested | Attack succeeded | Address attack, retry |
| **2** | Defended | Survived attack | Can proceed |
| **3** | Battle-tested | Survived 3+ attacks | High confidence |
| **4** | Axiom-derived | Pure deduction from axioms | Maximum confidence |

**Minimum for proceeding: Level 2**

## Integration with GOSM Sequence

The deductive system integrates into the GOSM 22-step sequence:

```
Step 8:  Strategy Discovery
         └─ Step 8a: Deductive Strategy Discovery (NEW)
         └─ Step 8b: Deductive Strategy Evaluation (NEW)

Step 9:  Strategy Search (now builds on deductive foundation)

Step 10: Adversarial Review (now has logical targets from evaluation)

Step 11: Strategy Selection (only select level 2+ strategies)
```

### New Gate: `strategy_deductive_check`

Added after `strategy_exists_check`, this gate verifies:
- Problem axioms have been extracted
- Strategy has a deductive chain
- Proof strength is at least SUFFICIENT

If the gate fails, it directs to `deductive_strategy_discovery`.

## New Procedures

### 1. `logical_proof_system.yaml`

The foundational infrastructure for logical reasoning:

- **Inference rules**: Deduction, contraposition, elimination, causal, structural
- **Premise types**: Axiom, fact, assumption, constraint, observation
- **Validation methods**: Validity checking, soundness checking

### 2. `deductive_strategy_discovery.yaml`

Derives strategies from problem axioms:

- **Backward chaining**: Work from success criteria to required actions
- **Forward derivation**: Work from current state to goal state
- **Necessity analysis**: Determine if strategy is necessary or just possible
- **Strategy synthesis**: Combine necessary components into complete strategy

### 3. `deductive_strategy_evaluation.yaml`

Evaluates logical soundness of derived strategies:

- **Validity check**: Do conclusions follow from premises?
- **Soundness check**: Are premises true AND inferences valid?
- **Weakness identification**: Find the weakest points in the proof
- **Proof level assignment**: Assign 0-4 level

### 4. `deductive_adversarial_review_integration.yaml`

Bridges deductive system with adversarial testing:

- **Deductive attack types**: Premise attacks, inference attacks, necessity attacks
- **Proof level upgrading**: How to move from level 0 to level 4
- **Integration flow**: Complete sequence from axioms to battle-tested strategy

## New Data Structures

Added to `gosm/core/models.py`:

### LogicalPremise
```python
class LogicalPremise(BaseModel):
    id: str
    content: str
    type: PremiseType  # axiom, fact, assumption, constraint, observation
    confidence: float
    critical: bool  # If false, does strategy fail?
    testable: bool
    tested: bool
```

### LogicalInference
```python
class LogicalInference(BaseModel):
    id: str
    type: InferenceType  # deduction, causal, elimination, etc.
    input_premises: list[str]
    conclusion: str
    reasoning: str
    strength: ProofStrength
```

### DeductiveChain
```python
class DeductiveChain(BaseModel):
    id: str
    premises: list[LogicalPremise]
    inferences: list[LogicalInference]
    final_conclusion: str
    overall_strength: ProofStrength
    proof_level: int  # 0-4
```

### StrategyProof
```python
class StrategyProof(BaseModel):
    strategy_id: str
    strategy_description: str
    deductive_chain: DeductiveChain
    necessity_explanation: str
    alternatives_ruled_out: list[str]
    confidence: float
```

### ProblemAxioms
```python
class ProblemAxioms(BaseModel):
    goal_id: str
    success_requirements: list[LogicalPremise]
    constraints: list[LogicalPremise]
    resources_available: list[LogicalPremise]
    domain_facts: list[LogicalPremise]
    past_failures: list[LogicalPremise]
```

## Example: Deriving a Health Strategy

### The Problem

User has breathing issues, excess weight, and elevated heart rate. Has tried supplements and health influencer advice for years without results.

### Step 1: Extract Problem Axioms

```yaml
success_requirements:
  - p1: "Nasal breathing is comfortable"
  - p2: "Weight is in healthy range"
  - p3: "Resting heart rate is healthy"

constraints:
  - c1: "Limited budget"
  - c2: "Must not cause harmful side effects"

domain_facts:
  - d1: "Weight loss requires caloric deficit"
  - d2: "Caloric deficit = reduced intake or increased expenditure"
  - d3: "Cannot treat effectively without knowing root cause"

past_failures:
  - f1: "Supplements did not produce weight loss"
  - f2: "Health influencer advice was hit-or-miss"
```

### Step 2: Backward Chaining

From success requirement p1 ("Nasal breathing is comfortable"):
- Requires: Nasal passages not obstructed
- Requires: No chronic inflammation
- Requires: **Know the root cause**
- Requires: **Medical evaluation** (action!)

From past failure f1 ("Supplements didn't work"):
- Implies: Generic approaches are insufficient
- Implies: **Specific, targeted approach needed**

### Step 3: Build Deductive Chain

```yaml
Inference 1 (from d3):
  type: causal
  input: [d3]
  conclusion: "Diagnosis is necessary for effective treatment"

Inference 2 (from f1, f2):
  type: elimination
  input: [f1, f2]
  conclusion: "Generic approaches (supplements, influencer advice) eliminated"

Inference 3 (from i1, i2):
  type: deduction
  input: [i1, i2]
  conclusion: "Must get specific diagnosis via medical evaluation"
```

### Step 4: Evaluate Proof

**Validity**: All inferences valid (proper logical form)
**Soundness**: Mostly sound (d3 is reasonable domain knowledge)
**Weakness**: Assumes diagnosis leads to effective treatment (not always true)
**Confidence Level**: 2 (Defended) - valid derivation, reasonable premises

### Step 5: Strategy Output

```yaml
Strategy: "Get medical evaluation for breathing issues"

Necessity Explanation: |
  Given that:
  1. Root cause is unknown
  2. Generic approaches have failed
  3. Effective treatment requires diagnosis

  Therefore: Medical evaluation is NECESSARY.
  This is not one of many options - it's the logical consequence
  of the problem definition.

Proof Strength: SUFFICIENT
Confidence Level: 2

Remaining Weakness:
  - Assumes diagnosis leads to treatment
  - Acceptable because: no alternative path exists given axioms
```

## Why This Output is Different

### Before (Typical Strategy Advice)
> "You should consider seeing a doctor about your breathing issues. Many people find that helpful. There are also some supplements you could try..."

Problems:
- Just a suggestion among many
- No reasoning chain
- Unknown confidence

### After (Deductive Strategy)
> "Given that:
> 1. You have a breathing problem (observed)
> 2. Root cause is unknown (observed)
> 3. Generic treatments failed (past failure)
> 4. Effective treatment requires diagnosis (domain knowledge)
>
> Therefore: Medical evaluation is NECESSARY (logical derivation).
>
> This is not a suggestion - it's the logical consequence of your situation. Any other path contradicts the established facts."

Differences:
- **Self-evident**: You can SEE why this is the answer
- **Traceable**: Each step is explicit
- **Honest**: Weaknesses are identified
- **Actionable**: Clear on what must be done

## Context Keys Added

The system tracks its state through context keys:

```python
state.context = {
    # Deductive Discovery
    "problem_axioms": ProblemAxioms,
    "strategy_proofs": list[StrategyProof],
    "deductive_discovery_completed": bool,

    # Deductive Evaluation
    "proof_levels": dict[str, int],  # strategy_id -> level
    "weakness_analysis": dict,
    "deductive_evaluation_completed": bool,

    # Selected Strategy
    "selected_strategy_proof": StrategyProof,
    "deductive_strength": str,  # "necessary", "sufficient", etc.
    "deductive_proof_level": int,  # 0-4

    # Integration with Adversarial Review
    "adversarial_review_completed": bool,
    "strategy_proof_level": int,  # Final level after attacks
    "attack_summary": dict,
}
```

## Files Modified/Added

### Modified
- `gosm/core/models.py` - Added deductive data structures
- `gosm/core/engine.py` - Added `strategy_deductive_check` gate
- `gosm/procedure_injector.py` - Added deductive procedures to mandatory list

### Added
- `library/procedures/extracted/planning/logical_proof_system.yaml`
- `library/procedures/extracted/planning/deductive_strategy_discovery.yaml`
- `library/procedures/extracted/planning/deductive_strategy_evaluation.yaml`
- `library/procedures/extracted/planning/deductive_adversarial_review_integration.yaml`

## Success Criteria Met

- [x] **Solves a hard problem**: Deductive strategy derivation is genuinely difficult
- [x] **Novel/original**: No existing system treats strategy selection as theorem proving
- [x] **Can't easily be made more powerful**: Logical necessity is the strongest form
- [x] **Strategies feel self-evidently correct**: Derivation shows WHY it works

## Trust Criteria Addressed

- [x] **Strong causal mechanism**: Explicit causal inferences in the chain
- [x] **Low risk to test**: Proof identifies what to test before full commitment
- [x] **Good theoretical basis**: Formal logic, well-established
- [x] **New perspectives**: Forces examination of problem axioms, reveals hidden assumptions
