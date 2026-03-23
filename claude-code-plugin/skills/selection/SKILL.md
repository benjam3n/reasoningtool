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

| Depth | Min Guesses Evaluated | Min ARAW Depth per Critical | Min Selection Criteria | Min Elimination Justifications | Pairwise Finals |
|-------|----------------------|-----------------------------|-----------------------|-------------------------------|-----------------|
| 1x    | 20                   | Quick (1 AR + 1 AW)        | 3                     | 1-line                        | No              |
| 2x    | 50                   | Standard (2 AR + 2 AW)     | 5                     | 2-3 lines                     | No              |
| 4x    | 100                  | Deep (3 AR + 3 AW)         | 7                     | Paragraph                     | No              |
| 8x    | 200                  | Full ARAW                  | 10                    | Full argument                 | Yes (top 15)    |
| 16x   | All                  | Full ARAW + subagent        | 12                    | Full argument + evidence      | Yes (top 15)    |
| 32x   | All                  | Full ARAW + partial right   | 12                    | Full argument + evidence      | Yes (top 15)    |

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

### Step 2: Knockout Filter

Before any evaluation, apply two knockout questions to every guess:

1. **Action divergence**: "If this guess is wrong, does anyone's action change?" If NO → **DEFER** (not eliminate — it may become relevant later).
2. **Reachability**: "Can this be investigated or acted on within the relevant timeframe?" If NO → **DEFER**.

Guesses that fail BOTH knockouts are moved to a DEFERRED list and excluded from further evaluation. Guesses that fail one knockout are flagged but proceed.

```
KNOCKOUT FILTER:
Passed: [N] guesses proceed
Deferred: [N] guesses (fail both knockouts)
Flagged: [N] guesses (fail one knockout — proceed with flag)
```

---

### Step 3: Cluster by Derivation

If guesses have derivation tags (e.g., `[D: AGENT]`, `[D: SCAMPER-S]`), group them by source. If no tags, cluster by theme.

```
CLUSTERS:
- [Cluster 1]: [N] guesses — [description]
- [Cluster 2]: [N] guesses — [description]
...
```

The final selection MUST include at least 1 item from each significant cluster (clusters with 3+ guesses). This prevents selecting 10 items from the same theme while ignoring others.

---

### Step 4: Define Selection Criteria

Before evaluating, establish what "good" means:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Actionability** | HIGH | Can this be acted on? Is there a concrete next step? |
| **Impact** | HIGH | If true/chosen, how much does it change the outcome? |
| **Testability** | MED | Can this be verified or falsified? |
| **Novelty** | MED | Does this add information beyond what's already known? |
| **Independence** | MED | Is this distinct from other guesses, or redundant? |
| **Downstream dependencies** | MED | Does resolving this guess unblock or clarify other guesses? |
| **Confidence** | LOW | How likely is this to be correct? (Low weight because low-confidence high-impact items are valuable) |

Add domain-specific criteria as needed. After rapid triage, check which criteria have low variance across CRITICAL/STRONG guesses (all score 4-5). Report non-differentiating criteria — they're included but didn't affect rankings.

---

### Step 5: Rapid Triage (All Guesses)

Sort every guess into one of four buckets:

| Bucket | Symbol | Meaning | Action |
|--------|--------|---------|--------|
| **CRITICAL** | ★ | High impact, must evaluate deeply | Full ARAW in Step 6 |
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

### Step 6: Deep Evaluation (CRITICAL Guesses Only)

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

### Step 7: Dependency Analysis

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

### Step 8: Selection Matrix

For CRITICAL and STRONG guesses, score against criteria.

**At depth ≤ 4x**: Use the standard scoring matrix (1-5 per criterion, sum for total).

**At depth ≥ 8x**: After matrix scoring, use **pairwise comparison** for items within 3 points of the cutoff. For each borderline pair, ask: "Given the specific purpose of this selection, is A or B more important?" Pairwise comparison is more reliable than absolute scoring for close items.

```
SELECTION MATRIX:

| Guess | Actionability | Impact | Testability | Novelty | Independence | Deps | TOTAL | RANK |
|-------|---------------|--------|-------------|---------|--------------|------|-------|------|
| [G1]  | 5             | 5      | 3           | 4       | 5            | 3    | 25    | 1    |
| [G2]  | 4             | 5      | 4           | 3       | 4            | 2    | 22    | 2    |
...
```

**Stability check**: After scoring, identify items where a 1-point change on ANY criterion would move them in/out of the selection. Mark these as BORDERLINE.

```
STABILITY:
Stable selections (rank holds under ±1 perturbation): [list]
Borderline (effectively tied — rank is fragile): [list]
```

---

### Step 9: Final Selection

Default to selecting the **top 20** items across all tiers unless the user specifies a different number (e.g., "best 10", "top 5"). The 20 should be distributed across tiers based on quality, not forced evenly.

**Cluster coverage check**: Before finalizing, verify that each significant cluster (from Step 3) has at least 1 representative in the selection. If a cluster is missing, swap in its highest-scoring member for the lowest-scoring redundant item from an over-represented cluster.

**Framing**: Detect whether the selected guesses are primarily hypotheses/unknowns or actions/changes. If hypotheses: frame tiers as "Test first / Test after / Monitor." If actions: frame as "Act on immediately / Act on after / Revisit later."

```
SELECTED ([N]):

TIER 1 — [Test first / Act on immediately] (max 5):
1. [Guess]: [why selected, what to do next]
2. [Guess]: [why selected, what to do next]

TIER 2 — [Test after Tier 1 / Act on after Tier 1 resolved]:
3. [Guess]: [why selected, what depends on]
4. [Guess]: [why selected, what depends on]

TIER 3 — [Monitor / Revisit later]:
5. [Guess]: [why kept, when to revisit]

ELIMINATED ([N]):
- [Guess]: [final elimination reason]
...

DEFERRED ([N]) (includes knockout-deferred from Step 2):
- [Guess]: [why deferred, trigger to revisit]
...
```

---

## Output Format

```
## SELECTION SUMMARY

Input: [what was evaluated]
Total evaluated: [N] | Knockout-deferred: [N] | Proceeded to triage: [N]
Clusters: [N] clusters identified
Critical: [N] | Strong: [N] | Weak: [N] | Eliminated: [N]

## TIER 1 SELECTIONS [Test first / Act immediately]
[Ranked list with justifications and next actions]

## TIER 2 SELECTIONS
[Ranked list with dependencies]

## TIER 3 (MONITOR)
[Items to revisit]

## RANKING STABILITY
Stable: [items whose rank holds under ±1 perturbation]
Borderline: [items that are effectively tied — rank is fragile]
Non-differentiating criteria: [criteria that didn't vary across selections]

## CLUSTER COVERAGE
[Which clusters are represented in the selection, which are not, and why]

## KEY CRUXES TO RESOLVE
[CRITICAL guesses with highest divergence, in resolution order]

## ELIMINATED WITH JUSTIFICATION
[What was cut and why]
```

---

## Quality Checklist

Before completing:
- [ ] Knockout filter applied — deferred guesses listed with triggers
- [ ] Guesses clustered by derivation/theme
- [ ] All guesses triaged into buckets
- [ ] CRITICAL guesses received ARAW evaluation
- [ ] Dependencies identified (with downstream count per guess)
- [ ] Selection criteria defined and applied; non-differentiating criteria noted
- [ ] Stability check performed — stable vs borderline items identified
- [ ] Cluster coverage verified — every significant cluster represented
- [ ] Tiers assigned with next actions (framed as test or act)
- [ ] Eliminations justified
- [ ] Resolution order for cruxes specified

---

## Next Steps

After selection:
1. Use `/dcp` to create decision procedure for top selections
2. Use `/to` to sequence actions from Tier 1
3. Use `/araw` for deeper analysis of unresolved cruxes
