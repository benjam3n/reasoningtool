---
name: "iaw - In Another Way"
description: "Re-express a goal, claim, or plan in genuinely alternative forms that preserve intent while changing approach, then rank alternatives by fit."
---

# IAW - In Another Way

**Input**: $ARGUMENTS

---

## Core Principles

1. **Intent and approach are different things.** "I want to grow revenue" (intent) can be achieved by raising prices, selling more, entering new markets, or reducing churn (approaches). Users often fuse their intent with their first-thought approach. This skill separates them.

2. **Synonyms are not alternatives.** "Grow the team" rephrased as "expand headcount" is a synonym, not an alternative. A genuine alternative would be "automate instead of hiring" or "partner instead of building." Alternatives must change the approach, not the wording.

3. **The best alternative often reframes the problem.** "How do I make meetings shorter?" → alternative: "How do I eliminate the need for this meeting?" The reframe dissolves the original constraint.

4. **Alternatives have different consequences.** Equivalent intent doesn't mean equivalent side effects. Each alternative forecloses different options, costs different amounts, and risks different failures. Surface these.

5. **Generating alternatives is easier than evaluating them.** The skill must do both — generate genuinely different approaches AND rank them so the user can choose, not just browse.

---

## Phase 1: Intent Extraction

```
[W1] ORIGINAL: [what the user said — the goal, claim, or plan, quoted]
[W2] SURFACE_APPROACH: [the approach embedded in the original statement]
[W3] UNDERLYING_INTENT: [what the user actually wants — separate from how]
[W4] INPUT_TYPE: [goal | claim | plan | strategy | method]
```

### Separation Test

Ask: "If I could achieve the intent without this specific approach, would the user be satisfied?"
- If YES → the approach is a means, not the goal. Generate alternatives to the approach.
- If NO → the approach IS the goal. Generate alternative framings of the goal instead.

---

## Phase 2: Alternative Generation

Generate genuinely different alternatives using multiple lenses:

```
[W-N] ALTERNATIVE: [description]
  LENS: [which generation method produced this]
  PRESERVES: [which aspects of the intent are preserved]
  CHANGES: [what's fundamentally different from the original]
```

### Generation Lenses

| Lens | Method | Example |
|------|--------|---------|
| **Means substitution** | Same goal, different method | "Grow revenue" → "Grow revenue by reducing churn instead of acquiring" |
| **Inversion** | Do the opposite of the original approach | "Add features" → "Remove features (simplify to increase value)" |
| **Elimination** | Remove the need for the goal entirely | "Faster meetings" → "Eliminate this meeting" |
| **Level shift** | Operate at a different level | "Teach this concept" → "Create an environment where they discover it" |
| **Stakeholder shift** | Different actor does it | "I'll build it" → "Partner with someone who already built it" |
| **Temporal shift** | Different timing or sequence | "Launch then iterate" → "Iterate then launch" |
| **Constraint change** | Accept different tradeoffs | "Fast and cheap" → "Slow and excellent" |
| **Decomposition** | Achieve the intent in parts | "Big launch" → "Soft launch in one segment, then expand" |

---

## Phase 3: Alternative Assessment

For each alternative:

```
[W-N] ASSESSMENT: [alternative ref]
  INTENT_PRESERVED: [fully | mostly | partially]
  FEASIBILITY: [high | medium | low]
  CONSEQUENCES: [what's different about the side effects]
  FORECLOSES: [what options this alternative removes]
  ADVANTAGE: [what this alternative does BETTER than the original]
  DISADVANTAGE: [what this alternative does WORSE than the original]
```

---

## Phase 4: Ranking

```
[W-N] RANKING (by fit to intent + feasibility):
  1. [alternative] — FIT: [level] — FEASIBILITY: [level] — KEY_ADVANTAGE: [what]
  2. [alternative] — FIT: [level] — FEASIBILITY: [level] — KEY_ADVANTAGE: [what]
  3. [alternative] — FIT: [level] — FEASIBILITY: [level] — KEY_ADVANTAGE: [what]
  ...
  ORIGINAL: [where does the original approach rank?] — [why]
```

---

## Phase 5: Output

```
IN ANOTHER WAY
==============

ORIGINAL: [quoted]
INTENT: [underlying intent, separated from approach]

ALTERNATIVES (ranked by fit):
  1. [alternative]
     PRESERVES: [what stays the same]
     CHANGES: [what's different]
     ADVANTAGE: [why this might be better]
     DISADVANTAGE: [what's worse]

  2. [alternative]
     PRESERVES: [what stays the same]
     CHANGES: [what's different]
     ADVANTAGE: [advantage]
     DISADVANTAGE: [disadvantage]

  3. [alternative]
     ...

ORIGINAL RANK: [where the original approach falls and why]

REFRAME: [if a reframe exists that dissolves the original problem, state it here]

READY FOR:
- /cmp [top alternatives] — to compare the best alternatives rigorously
- /decide [alternatives] — to choose between them
- /ar [specific alternative] — to explore what follows if this alternative is right
- /aw [specific alternative] — to stress-test a promising alternative
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Synonym generation** | "Alternatives" are just rewordings | Each alternative must change the APPROACH, not the wording |
| **Intent lost** | Alternatives don't preserve the underlying goal | Check: does this alternative achieve what the user actually wants? |
| **Only obvious alternatives** | First-thought variants only | Use all generation lenses, especially inversion and elimination |
| **No ranking** | Flat list of alternatives without evaluation | Each alternative must be assessed and ranked |
| **Consequences ignored** | Alternatives listed without side-effect analysis | Every alternative has different consequences — surface them |
| **Original not ranked** | Alternatives listed but original not compared | The original might still be best — it should appear in the ranking |
| **Reframe missed** | No attempt to dissolve the problem | Always check: can the need for this be eliminated? |

---

## Depth Scaling

| Depth | Min Alternatives | Generation Lenses | Assessment Depth | Ranking |
|-------|-----------------|-------------------|-----------------|---------|
| 1x | 3 | 3 | Fit only | Simple rank |
| 2x | 5 | 5 | Fit + feasibility + consequences | Ranked with advantages |
| 4x | 8 | 7 | Full assessment | Ranked with full comparison |
| 8x | 12 | All 8 | Full + second-order effects | Ranked with scenario analysis |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Intent separated from approach
- [ ] Alternatives change the approach, not just the wording
- [ ] Multiple generation lenses used (not just means substitution)
- [ ] Reframe/elimination option explored
- [ ] Each alternative assessed for consequences and tradeoffs
- [ ] Alternatives ranked by fit and feasibility
- [ ] Original approach included in ranking
- [ ] Advantages AND disadvantages stated for each alternative

---

## Integration

- Use from: when current approach feels stuck, when exploring options
- Routes to: `/cmp`, `/decide`, `/ar`, `/aw` for evaluating top alternatives
- Complementary: `/poa` (possibility analysis — broader exploration)
- Differs from `/poa`: poa explores what's possible; iaw re-expresses a specific thing differently
- Differs from `/ma`: ma generates from scratch; iaw generates alternatives to something specific
- Differs from `/va`: va asks "what's the opposite?"; iaw generates multiple alternatives, not just inversion
