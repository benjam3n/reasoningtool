---
name: "aso - And So On"
description: "Continue a discovered pattern with bounded expansion rules — extract the generative rule, extend coherently, detect pattern decay, and stop at an explicit limit."
---

# ASO - And So On

**Input**: $ARGUMENTS

---

## Core Principles

1. **Patterns have generative rules.** "2, 4, 8, and so on" isn't just three numbers — it's a rule (double the previous) that can produce unlimited continuations. The rule is more valuable than any individual continuation. Extract the rule first, then generate from it.

2. **Patterns decay.** Most real-world patterns don't continue indefinitely. "Double your revenue each year" works for startups but hits physics eventually. The skill must detect WHERE the pattern breaks down, not just continue it blindly. Pattern decay is as important as pattern identification.

3. **Multiple rules can explain the same head.** "1, 2, 4, ..." could be powers of 2, or Fibonacci-adjacent, or "add the next prime." Short heads are underdetermined — they don't contain enough information to uniquely identify the rule. The skill must surface this ambiguity.

4. **Extension must stay within the pattern's domain.** A pattern observed in one context can't be extended beyond that context without justification. "We grew 10% per quarter for 3 quarters" doesn't mean 10% growth forever. Domain constraints limit how far the pattern can be extended.

5. **Bounded expansion is the whole point.** Unbounded continuation is useless — you could generate forever. The stopping condition is as much a part of the output as the continuation itself. The stop reason must be explicit: why HERE and not one more?

---

## Phase 1: Pattern Identification

```
[A1] RAW_INPUT: [the pattern head or sequence, quoted]
[A2] OBSERVED_ELEMENTS: [the explicit elements, in order]
[A3] ELEMENT_COUNT: [how many observed]
[A4] DOMAIN: [what domain these elements come from — numbers, events, behaviors, stages, etc.]
[A5] PATTERN_TYPE: [see classification below]
```

### Pattern Type Classification

| Type | Definition | Example |
|------|-----------|---------|
| **Arithmetic** | Constant additive difference | 3, 6, 9, ... (+3) |
| **Geometric** | Constant multiplicative ratio | 2, 4, 8, ... (×2) |
| **Structural** | Repeating structural template | AB, AABB, AAABBB, ... |
| **Procedural** | Each step follows from the previous via a procedure | Seed → grow → harvest → ... |
| **Categorical** | Members of a category in some order | Junior → Mid → Senior → ... |
| **Compositional** | Elements combine or build on each other | Foundation → walls → roof → ... |
| **Oscillating** | Pattern alternates or cycles | Up, down, up, down, ... |
| **Recursive** | Each element defined in terms of prior elements | Fibonacci: each = sum of previous two |

---

## Phase 2: Rule Extraction

```
[A6] CANDIDATE_RULES:
  RULE_1: [explicit generative rule] — PREDICTS: [what next 2-3 elements would be]
  RULE_2: [alternative rule] — PREDICTS: [different next elements]

[A7] SELECTED_RULE: [best-fit rule]
  CONFIDENCE: [high | medium | low]
  EVIDENCE: [why this rule over alternatives]
  FORMULATION: [the rule stated precisely enough that someone else could apply it independently]
```

### Rule Quality Test

The extracted rule must satisfy:
- **Reproductive**: It reproduces all observed elements, not just most
- **Generative**: It can produce the NEXT element without ambiguity
- **Minimal**: It doesn't invoke unnecessary complexity (Occam's razor)
- **Falsifiable**: The next generated element could be checked as right or wrong

---

## Phase 3: Bounded Extension

Generate continuations from the rule:

```
[A-N] EXTENSION: [next element]
  GENERATED_BY: [how the rule produces this]
  CONFIDENCE: [high | medium | low — does the pattern still hold cleanly?]
  DOMAIN_CHECK: [does this element still make sense in the original domain?]
```

### Decay Detection

At each extension, check for pattern decay:

```
[A-N] DECAY_CHECK:
  ELEMENT: [which extension]
  COHERENT: [yes | weakening | no]
  DECAY_SIGNAL: [if weakening/no — what indicates the pattern is breaking down]
  DECAY_TYPE: [see table below]
```

| Decay Type | Description | Example |
|-----------|-------------|---------|
| **Saturation** | Pattern hits a ceiling | Growth rate can't exceed 100% market share |
| **Domain exit** | Continuation leaves the valid domain | Extrapolating startup advice to governments |
| **Granularity collapse** | Steps become too fine or too coarse to be useful | Breaking days into microseconds |
| **Resource exhaustion** | Pattern requires resources that don't exist at scale | "Double team size every quarter" |
| **Meaning loss** | Elements become abstract to the point of uselessness | Pattern continues formally but stops meaning anything |

---

## Phase 4: Stop Condition

```
[A-N] STOP:
  AFTER_ELEMENT: [which element to stop at]
  REASON: [why stop here — see criteria below]
  TOTAL_EXTENDED: [how many elements beyond the original head]
  COULD_CONTINUE: [yes/no — is the pattern still valid beyond the stop?]
  WHY_NOT: [if could continue — why stopping anyway]
```

### Stop Criteria

| Criterion | When to Use |
|-----------|------------|
| **Exhaustion** | Category fully enumerated — no more elements exist |
| **Decay** | Pattern has degraded past usefulness |
| **Sufficiency** | Enough elements to establish the rule — more adds no information |
| **Scope** | User-defined limit on extension depth |
| **Diminishing value** | Each new element adds less than the previous |
| **Domain boundary** | Pattern hits the edge of its valid context |

---

## Phase 5: Output

```
AND SO ON
=========

PATTERN: [quoted input]
RULE: [the generative rule, stated precisely]
CONFIDENCE: [level]

OBSERVED:
  1. [element] (given)
  2. [element] (given)
  3. [element] (given)

EXTENDED:
  4. [element] — CONFIDENCE: [level]
  5. [element] — CONFIDENCE: [level]
  6. [element] — CONFIDENCE: [level]
  ...

STOP: After element [N] — REASON: [why]

PATTERN DECAY: [where the pattern starts to weaken, if applicable]
  DECAY AT: [element or threshold]
  TYPE: [decay type]

ALTERNATIVE RULE: [if another rule fits the head]
  WOULD PRODUCE: [different continuation]

READY FOR:
- /etc [list] — to expand a category-based "etc" (complementary skill)
- /se [category] — to systematically enumerate the full space
- /ar [rule] — to explore what follows if the rule continues
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Rule not extracted** | Elements generated "by feel" without an explicit rule | State the rule precisely enough that someone else could apply it |
| **Unbounded expansion** | No stop condition, list keeps growing | Define the stop criterion BEFORE extending |
| **Blind extrapolation** | Pattern extended past its domain without noting decay | Check domain validity at each extension step |
| **Single rule assumed** | Only one interpretation considered | Generate 2+ candidate rules, especially with short heads |
| **Overfitting** | Rule too complex to be useful — fits head perfectly but doesn't generalize | Apply Occam's razor. Simpler rules are more likely correct |
| **No decay detection** | Pattern treated as eternal | Every real-world pattern decays. State where, even if it's far out |
| **Continuation without generation** | Items added that don't follow from the rule | Every extended element must be derivable from the stated rule |

---

## Depth Scaling

| Depth | Candidate Rules | Extension Length | Decay Analysis | Alternative Continuations |
|-------|----------------|-----------------|---------------|--------------------------|
| 1x | 1 | 3-5 elements | Binary (decays/doesn't) | No |
| 2x | 2 | 5-8 elements | Typed with threshold | 1 alternative |
| 4x | 3 | 8-12 elements | Full with signals | 2 alternatives |
| 8x | All plausible | Full to exhaustion or decay | Full + prediction | All alternatives |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Pattern head extracted with all observed elements
- [ ] Generative rule stated explicitly and precisely
- [ ] Rule satisfies quality test (reproductive, generative, minimal, falsifiable)
- [ ] Multiple candidate rules considered
- [ ] Extensions all derivable from the stated rule
- [ ] Domain validity checked at each extension
- [ ] Decay detected or explicitly noted as absent
- [ ] Stop condition defined with explicit reason
- [ ] At least one alternative rule noted (at 2x+)

---

## Integration

- Use from: continuing sequences, extending patterns, predicting next steps, expanding "and so on"
- Routes to: `/se` (systematic enumeration), `/ar` (explore implications of the rule)
- Complementary: `/etc` (expands category-based "etc" tails — overlapping but distinct trigger)
- Differs from `/etc`: etc focuses on category membership and completion; aso focuses on generative rules and pattern continuation
- Differs from `/se`: se enumerates a known space; aso extends from observed pattern heads
- Differs from `/gen`: gen generates diverse options; aso continues a specific pattern
