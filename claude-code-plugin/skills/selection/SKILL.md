---
name: "selection - Guess Selection & Evaluation"
description: Systematically evaluate and select from a set of guesses, options, or possibilities. Combines ARAW analysis with prioritization to determine which guesses are strong, weak, actionable, or eliminable.
output:
  format: "table"
---

# Guess Selection & Evaluation

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Filter guesses from /gg output**: The user has a large set of guesses (from /gg or similar) and wants to systematically evaluate which are worth pursuing, which are wrong, and which are critical.
**Interpretation 2 — Select best options from a list**: The user has enumerated options and wants to select the best one(s) based on criteria. Default: select top 20 unless user specifies a different number.
**Interpretation 3 — Triage a backlog**: The user has many items and wants to sort them into act-on / defer / eliminate buckets. Default: surface top 20 unless user specifies a different number.

If ambiguous, ask: "I can help with filtering guesses from an analysis, selecting the best options from a list, or triaging a backlog — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/selection 4x [input]").

| Depth | Min Guesses Evaluated | Min ARAW Depth per Critical | Min Selection Criteria | Min Elimination Justifications |
|-------|----------------------|-----------------------------|-----------------------|-------------------------------|
| 1x    | 20                   | Quick (1 AR + 1 AW)        | 3                     | 1-line                        |
| 2x    | 50                   | Standard (2 AR + 2 AW)     | 5                     | 2-3 lines                     |
| 4x    | 100                  | Deep (3 AR + 3 AW)         | 7                     | Paragraph                     |
| 8x    | 200                  | Full ARAW                  | 10                    | Full argument                 |
| 16x   | All                  | Full ARAW + subagent        | 12                    | Full argument + evidence      |

---

## The Process

### Step 1: Inventory

List all guesses/options being evaluated. Group by source dimension if from /gg output.

```
INVENTORY: [N] guesses to evaluate
Source: [/gg output, brainstorm, enumeration, etc.]

Groups:
- [Group 1]: [N] guesses
- [Group 2]: [N] guesses
...
```

---

### Step 2: Define Selection Criteria

Before evaluating, establish what "good" means:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Actionability** | HIGH | Can this be acted on? Is there a concrete next step? |
| **Impact** | HIGH | If true/chosen, how much does it change the outcome? |
| **Testability** | MED | Can this be verified or falsified? |
| **Novelty** | MED | Does this add information beyond what's already known? |
| **Independence** | MED | Is this distinct from other guesses, or redundant? |
| **Confidence** | LOW | How likely is this to be correct? (Low weight because low-confidence high-impact items are valuable) |

Add domain-specific criteria as needed.

---

### Step 3: Rapid Triage (All Guesses)

Sort every guess into one of four buckets:

| Bucket | Symbol | Meaning | Action |
|--------|--------|---------|--------|
| **CRITICAL** | ★ | High impact, must evaluate deeply | Full ARAW in Step 4 |
| **STRONG** | ✓ | Likely true/useful, worth keeping | Brief justification |
| **WEAK** | ~ | Low impact or likely wrong | Note why, set aside |
| **ELIMINATE** | ✗ | Redundant, contradicted, or irrelevant | Justify elimination |

```
RAPID TRIAGE:

★ CRITICAL ([N]):
- [Guess]: [1-line reason it's critical]
...

✓ STRONG ([N]):
- [Guess]: [1-line reason it's strong]
...

~ WEAK ([N]):
- [Guess]: [1-line reason it's weak]
...

✗ ELIMINATE ([N]):
- [Guess]: [1-line reason to eliminate]
...
```

---

### Step 4: Deep Evaluation (CRITICAL Guesses Only)

For each CRITICAL guess, run a compressed ARAW:

```
GUESS: [statement]

ASSUME RIGHT (what follows if this is true/correct):
- AR1: [implication]
- AR2: [implication]
- AR3: [what you'd build/do differently]

ASSUME WRONG (what follows if this is false/incorrect):
- AW1: [implication]
- AW2: [implication]
- AW3: [what you'd build/do differently]

DIVERGENCE: [How different are the AR vs AW paths?]
- HIGH: Completely different strategies → This is a true crux, must resolve
- MED: Different approaches, same general direction → Important but not blocking
- LOW: Minor adjustments → Demote from CRITICAL to STRONG

RESOLUTION PATH: [How to determine which is true]
- [Test, experiment, question to ask, evidence to gather]
```

---

### Step 5: Dependency Analysis

Check if any CRITICAL guesses depend on others:

```
DEPENDENCIES:
- [Guess A] depends on [Guess B]: [relationship]
- [Guess C] and [Guess D] are mutually exclusive
- [Guess E] is prerequisite for [Guess F, G, H]

RESOLUTION ORDER:
1. Resolve [Guess B] first (most dependencies downstream)
2. Then [Guess A]
3. [Guess C vs D] can be resolved independently
...
```

---

### Step 6: Selection Matrix

For CRITICAL and STRONG guesses, score against criteria:

```
SELECTION MATRIX:

| Guess | Actionability | Impact | Testability | Novelty | Independence | TOTAL | RANK |
|-------|---------------|--------|-------------|---------|--------------|-------|------|
| [G1]  | 5             | 5      | 3           | 4       | 5            | 22    | 1    |
| [G2]  | 4             | 5      | 4           | 3       | 4            | 20    | 2    |
...
```

---

### Step 7: Final Selection

Default to selecting the **top 20** items across all tiers unless the user specifies a different number (e.g., "best 10", "top 5"). The 20 should be distributed across tiers based on quality, not forced evenly.

```
SELECTED ([N]):

TIER 1 — Act on immediately:
1. [Guess]: [why selected, what to do next]
2. [Guess]: [why selected, what to do next]

TIER 2 — Act on after Tier 1 resolved:
3. [Guess]: [why selected, what depends on]
4. [Guess]: [why selected, what depends on]

TIER 3 — Keep in mind, revisit later:
5. [Guess]: [why kept, when to revisit]

ELIMINATED ([N]):
- [Guess]: [final elimination reason]
...

DEFERRED ([N]):
- [Guess]: [why deferred, trigger to revisit]
...
```

---

## Output Format

```
## SELECTION SUMMARY

Input: [what was evaluated]
Total evaluated: [N]
Critical: [N] | Strong: [N] | Weak: [N] | Eliminated: [N]

## TIER 1 SELECTIONS
[Ranked list with justifications and next actions]

## TIER 2 SELECTIONS
[Ranked list with dependencies]

## TIER 3 (MONITOR)
[Items to revisit]

## KEY CRUXES TO RESOLVE
[CRITICAL guesses with highest divergence, in resolution order]

## ELIMINATED WITH JUSTIFICATION
[What was cut and why]
```

---

## Quality Checklist

Before completing:
- [ ] All guesses triaged into buckets
- [ ] CRITICAL guesses received ARAW evaluation
- [ ] Dependencies identified
- [ ] Selection criteria defined and applied
- [ ] Tiers assigned with next actions
- [ ] Eliminations justified
- [ ] Resolution order for cruxes specified

---

## Next Steps

After selection:
1. Use `/dcp` to create decision procedure for top selections
2. Use `/to` to sequence actions from Tier 1
3. Use `/araw` for deeper analysis of unresolved cruxes
