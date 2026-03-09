---
name: "p5deep - Pick 5 Deep"
description: "Pick 5 skills that together provide the most thorough analysis possible. Optimized for maximum analytical depth on a topic. Standalone implementation of the DEEP algorithm from /pick with N=5."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "deep", "thorough", "analysis"]
---

# Pick 5 Deep

**Input**: $ARGUMENTS

---

## Core Principles

1. **Deep means layered, not long.** Depth is not about spending more time on the same analysis. It is about applying multiple distinct analytical lenses to the same subject, where each lens reveals something the others miss.

2. **The canonical depth stack is: diverge, analyze, stress-test, validate, synthesize.** Five skills, five phases. Divergent exploration first, then structured analysis, then adversarial stress-testing, then empirical validation, then synthesis into actionable conclusions.

3. **Analytical skills must disagree with each other.** If all 5 skills produce the same conclusion, you haven't gone deep — you've confirmed your initial impression 5 times. Deep analysis includes at least one skill whose job is to find fault with the others.

4. **Topic relevance modifies the stack.** The base stack (diverge/analyze/stress-test/validate/synthesize) adjusts based on what the user provides in $ARGUMENTS. A technical topic gets different analysis tools than a strategic one.

5. **Five is the upper limit for depth without diminishing returns.** After 5 distinct analytical passes, additional passes primarily confirm existing findings. Five is the sweet spot between thoroughness and efficiency.

---

## Phase 1: Topic Assessment

```
[A] TOPIC: [from $ARGUMENTS, or "general" if no topic provided]
[B] TOPIC_DOMAIN: [technical / strategic / personal / creative / organizational / general]
[C] TOPIC_TYPE: [claim / decision / plan / system / idea / problem]
[D] DEPTH_NEEDS:
    What kind of depth does this topic need?
    - Logical depth (test reasoning) → stress-test skills
    - Empirical depth (test evidence) → validation skills
    - Creative depth (test alternatives) → divergent skills
    - Structural depth (test architecture) → decomposition skills
    - Adversarial depth (test robustness) → attack skills
```

---

## Phase 2: Stack Construction

### Base Stack (no topic or general topic)

```
[E] BASE_STACK:

Position 1 — DIVERGE: Start wide. Generate alternative framings.
    Default: /araw (Assume Right, Assume Wrong)
    Alternatives: /uaua, /se, /dd

Position 2 — ANALYZE: Structure the problem. Find components.
    Default: /rca (Root Cause Analysis) or /sya (Systems Analysis)
    Alternatives: /dcm, /fohw, /aex

Position 3 — STRESS-TEST: Attack the analysis. Find weaknesses.
    Default: /ht (Hypothesis Testing)
    Alternatives: /aw, /cor, /frq

Position 4 — VALIDATE: Check against reality. Verify findings.
    Default: /vbo (Validation by Observation)
    Alternatives: /val, /pv, /mv

Position 5 — SYNTHESIZE: Combine findings into conclusions.
    Default: /certainty (Maximum Effort Analysis)
    Alternatives: /araw, /cpra
```

### Topic-Adjusted Stack

```
[F] ADJUSTED_STACK:

IF topic is a CLAIM:
    Position 1: /aex (extract assumptions)
    Position 2: /ht (test the claim)
    Position 3: /aw (assume it's wrong)
    Position 4: /frq (check reasoning quality)
    Position 5: /val (validate conclusions)

IF topic is a DECISION:
    Position 1: /dd (decision decomposition)
    Position 2: /cba (cost-benefit analysis)
    Position 3: /ai (assumption inversion)
    Position 4: /pv (pre-validation)
    Position 5: /dcp (decision checkpoint)

IF topic is a PLAN:
    Position 1: /aex (extract plan assumptions)
    Position 2: /de (dependency extraction)
    Position 3: /ria (risk assessment)
    Position 4: /pv (pre-validation)
    Position 5: /iterate (improvement cycle)

IF topic is a SYSTEM:
    Position 1: /fohw (how it works)
    Position 2: /sya (systems analysis)
    Position 3: /rca (root cause analysis)
    Position 4: /vbo (observation-based validation)
    Position 5: /insd (inside the system)

IF topic is a PROBLEM:
    Position 1: /rca (find root cause)
    Position 2: /dbg (debug systematically)
    Position 3: /aex (check assumptions about the problem)
    Position 4: /ht (test hypotheses)
    Position 5: /cor (correction framework)
```

---

## Phase 3: Stack Validation

```
[G] VALIDATION:

Step 1: Do the 5 skills cover distinct analytical functions?
    Function check: [list the function of each — must be 5 different functions]
    IF duplicates: swap duplicate for a different-function skill

Step 2: Is there at least 1 adversarial skill (finds fault)?
    [Y/N — if N, add one]

Step 3: Is the execution order correct?
    [Divergent before convergent? Analysis before validation?]

Step 4: Does the stack match the topic type?
    [Y/N — if N, use adjusted stack]
```

---

## Phase 4: Output

```
ALGORITHM: DEEP
TOPIC: [topic or "general"]
TOPIC TYPE: [claim/decision/plan/system/idea/problem]
PICKED: 5

DEPTH STACK:
  1. /[id] — [title] — DIVERGE
     Role: [what analytical lens this applies]
     Produces: [what this step surfaces that others can't]
     Tier: [tier]

  2. /[id] — [title] — ANALYZE
     Role: [what analytical lens]
     Receives: [from step 1] | Produces: [what]
     Tier: [tier]

  3. /[id] — [title] — STRESS-TEST
     Role: [what analytical lens]
     Receives: [from step 2] | Produces: [what]
     Tier: [tier]

  4. /[id] — [title] — VALIDATE
     Role: [what analytical lens]
     Receives: [from step 3] | Produces: [what]
     Tier: [tier]

  5. /[id] — [title] — SYNTHESIZE
     Role: [what analytical lens]
     Receives: [all prior] | Produces: [final output]
     Tier: [tier]

DEPTH GUARANTEE:
  Distinct functions: [5/5]
  Adversarial skill present: [Y]
  Order: divergent → convergent: [Y]

EXPECTED OUTPUT: After running all 5, you will have:
  - [what the combined analysis produces]
  - [what failure modes it catches]
  - [what confidence level it provides]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Confirmation stack** | All 5 skills approach from the same angle | At least 1 must be adversarial (its job is to disagree) |
| **Redundant skills** | Two skills in the stack do essentially the same thing | Check: does each produce a UNIQUE output? |
| **Wrong order** | Validation before analysis, or synthesis before stress-testing | Follow: diverge → analyze → stress-test → validate → synthesize |
| **Topic mismatch** | General stack used for a specific topic type | Check topic type and use adjusted stack |
| **Depth theater** | Five skills selected but none goes deeper than surface | Verify: are these the DEEPEST skills available, not the broadest? |
| **Missing adversarial** | No skill challenges the emerging conclusion | Mandatory: at least 1 skill whose purpose is to find flaws |

---

## Depth Scaling

| Depth | Topic Analysis | Stack Construction | Validation |
|-------|---------------|-------------------|-----------|
| 1x | Type identification only | Base stack | Function check |
| 2x | Type + domain + depth needs | Adjusted stack for topic type | Function + adversarial + order check |
| 4x | Full topic analysis + similar topic comparison | Custom stack with skill-reading to verify fit | Full validation + alternative stacks |
| 8x | Deep topic modeling | Stack designed from first principles for this exact topic | Validation + simulation of running the stack |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Topic type identified (claim/decision/plan/system/idea/problem)
- [ ] Stack adjusted for topic type (not generic base stack used blindly)
- [ ] Exactly 5 skills selected
- [ ] All 5 serve different analytical functions
- [ ] At least 1 adversarial/stress-testing skill included
- [ ] Execution order goes divergent to convergent
- [ ] Expected combined output described

---

## Integration

- **Shortcut for**: `/pick 5 deep $ARGUMENTS`
- **Use when**: You want maximum analytical depth on a specific topic
- **Routes to**: The 5 stack skills in sequence; `/certainty` for even deeper single-pass
- **Related**: `/p10goal` (breadth over depth), `/p5qm` (question-driven), `/araw` (core deep analysis)
- **Differs from /p10goal**: goal maximizes capability coverage; deep maximizes analytical depth
- **Differs from /p5qm**: qm uses questions to narrow; deep uses layered analysis to deepen
- **Differs from /certainty**: certainty is one skill at max depth; deep is 5 skills at normal depth
