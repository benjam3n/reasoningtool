---
name: "cmp - Comparison - Impression-Informed Option Evaluation"
description: Compare options using gestalt impression + structured evaluation. Impression first, then criteria, then check for divergence.
---

# Comparison - Impression-Informed Option Evaluation

**Input**: $ARGUMENTS

---

## Core Principles

1. **Impression before scoring.** State your overall sense of which option is best BEFORE structured evaluation. This captures qualitative judgment that scoring can miss.

2. **Tiers, not scores.** Rate options as clearly better / slightly better / equivalent / slightly worse / clearly worse — not 2.3 vs 2.1. False precision obscures real differences.

3. **Criteria serve the purpose.** Don't evaluate against generic criteria. Ask: "What does this need to accomplish?" The answer defines what matters.

4. **Divergence is data.** When your impression says "B is better" but your scoring says "A wins," investigate. The divergence often reveals a missing criterion or a misjudged weight.

5. **Kill clearly bad options early.** Don't waste effort scoring options that fail hard requirements. Eliminate first, then compare survivors.

---

## The Process

### 1. State the Impression

Before any structured evaluation:

```
OPTIONS: [List all options]
IMPRESSION: [Which seems best, at first glance? Why?]
CONFIDENCE: [HIGH / MEDIUM / LOW]
```

### 2. Define Purpose and Criteria

What must this accomplish? Derive criteria from purpose.

**REQUIRED** — Must have. Failure = eliminated.
```
- [Criterion]: [What "pass" looks like]
```

**IMPORTANT** — Strongly preferred. Failure = significant penalty.
```
- [Criterion]: [What good looks like]
```

**NICE-TO-HAVE** — Bonus value. Absence acceptable.
```
- [Criterion]: [What it adds]
```

### 3. Eliminate on Required Criteria

For each option, check required criteria. PASS or FAIL.

```
| Option | [Req 1] | [Req 2] | [Req 3] | Status |
|--------|---------|---------|---------|--------|
| A      | PASS    | PASS    | PASS    | Survives |
| B      | PASS    | FAIL    | PASS    | Eliminated |
| C      | PASS    | PASS    | PASS    | Survives |
```

Eliminated options stop here. Record why. Note: under what conditions would they pass? (prevents premature rejection)

### 4. Compare Survivors on Important Criteria

For each important criterion, compare survivors in TIERS:

```
[Criterion name]:
- A: [Evidence/reasoning] → TIER
- C: [Evidence/reasoning] → TIER

Tiers: CLEARLY BETTER / SLIGHTLY BETTER / EQUIVALENT / SLIGHTLY WORSE / CLEARLY WORSE
```

### 5. Overall Assessment

```
CRITERION SUMMARY:
| Criterion | A | C | Edge |
|-----------|---|---|------|
| [Crit 1]  | Slightly better | — | A |
| [Crit 2]  | — | Clearly better | C |
| [Crit 3]  | Equivalent | Equivalent | — |

OVERALL: [Which option wins on the criteria that matter most?]
```

### 6. Divergence Check

```
IMPRESSION said: [option X seems best]
ANALYSIS says: [option Y scores best]

DIVERGENCE? [YES/NO]
If YES: What criterion is the impression weighting that the analysis isn't?
        → [Investigate. Often reveals a missing important criterion.]
```

### 7. Recommendation

```
RECOMMENDATION: [Option]
CONFIDENCE: [HIGH / MEDIUM / LOW]
REASONING: [2-3 sentences explaining why, incorporating both analysis and impression]
RISKS: [What could go wrong with this choice?]
REVERSIBILITY: [How easy to change course if wrong?]
```

---

## Handling Difficult Cases

| Situation | Approach |
|-----------|----------|
| Two options very close | Focus on REVERSIBILITY — pick the easier one to undo |
| Many options (5+) | Eliminate on required criteria first, then compare top 3 |
| No clear winner | Ask: "What additional information would make this clear?" |
| Impression and analysis diverge strongly | The divergence IS the finding — investigate what's behind it |
| All options are bad | Say so. Suggest reframing the choice. |

---

## When Called by Other Skills

Comparison is a primitive. When called by decision_procedure, UAUA, or other skills:
- Accept options and context from the caller
- Return: impression, elimination results, tier comparison, divergence check, recommendation
- Be direct about which option wins and why

---

## Pre-Completion Check

- [ ] Impression stated before analysis
- [ ] Criteria derived from purpose (not generic)
- [ ] Required criteria used for elimination
- [ ] Survivors compared in tiers (not numeric scores)
- [ ] Divergence between impression and analysis checked
- [ ] Recommendation includes reasoning and risk
