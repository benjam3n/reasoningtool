---
name: "etc - Expand the Etcetera"
description: "Expand 'etc', 'and so on', and other list tails into explicit items by inferring the continuation rule, enumerating omitted items, and stopping at a defined completeness criterion."
output:
  format: "prose"
---

# ETC - Expand the Etcetera

**Input**: $ARGUMENTS

---

## Core Principles

1. **"Etc" is a claim of pattern continuation.** When someone writes "A, B, C, etc." they're asserting that a pattern exists and continues predictably. But the pattern they intend is often not the pattern that's obvious. "Red, blue, green, etc." — is the pattern primary colors? Colors of the rainbow? Colors in their CSS file? The continuation rule must be inferred, not assumed.

2. **The list head constrains the list tail.** The items explicitly stated define the category, granularity, and scope of what follows. "Apples, oranges, etc." means fruits — not "apples, oranges, trucks, democracy." The head establishes a membership test that every expanded item must pass.

3. **Omission is often strategic.** People don't write "etc" randomly. They include the items that seemed most important, representative, or top-of-mind, and omit the rest. The omitted items are often less obvious, less prototypical, or less favored — which is exactly why expanding them matters.

4. **Lists have finite completions.** Every "etc" has a point where the category is exhausted or continuing adds no value. The skill must define a stopping rule, not just keep generating. An unbounded expansion is as useless as the original "etc."

5. **Multiple valid continuations exist.** "Dogs, cats, etc." could expand to {hamsters, fish, birds} (common pets), {wolves, lions, tigers} (related wild animals), or {horses, cows, pigs} (domesticated animals). The continuation depends on the RULE, and the rule depends on CONTEXT. Surface the rule explicitly.

---

## Phase 1: Head Extraction

```
[E1] RAW_INPUT: [the full statement containing "etc" or equivalent, quoted]
[E2] LIST_HEAD: [the explicitly stated items, in order]
[E3] HEAD_COUNT: [how many items were explicit]
[E4] TAIL_MARKER: [what indicated continuation — "etc", "and so on", "...", ellipsis, "among others"]
[E5] CONTEXT: [surrounding text or situation that constrains interpretation]
```

---

## Phase 2: Rule Inference

What pattern connects the explicit items?

```
[E6] CANDIDATE_RULES: [list 2-3 possible continuation rules]
  RULE_1: [pattern] — FITS_HEAD: [yes/partial] — EVIDENCE: [what supports this]
  RULE_2: [pattern] — FITS_HEAD: [yes/partial] — EVIDENCE: [what supports this]
  RULE_3: [pattern] — FITS_HEAD: [yes/partial] — EVIDENCE: [what supports this]

[E7] SELECTED_RULE: [the most likely continuation rule]
  CONFIDENCE: [high | medium | low]
  WHY_THIS_RULE: [what makes this interpretation strongest]
  MEMBERSHIP_TEST: [how to determine if a candidate item belongs — the explicit inclusion criterion]
```

### Rule Inference Strategies

| Strategy | Method | When to Use |
|----------|--------|------------|
| **Category membership** | All items share a category | "Apples, oranges, etc." → fruits |
| **Property match** | All items share a property | "Red, blue, green, etc." → primary colors |
| **Sequence** | Items follow an ordered pattern | "Monday, Tuesday, etc." → days of the week |
| **Exemplar to class** | Items are examples of a broader class | "PostgreSQL, MySQL, etc." → relational databases |
| **Contextual** | Surrounding text defines the category | "We support etc." → context determines the domain |

If confidence is low, present multiple expansions under different rules.

---

## Phase 3: Expansion

Enumerate the omitted items:

```
[E-N] ITEM: [expanded item]
  WHY_INCLUDED: [how it satisfies the membership test]
  CONFIDENCE: [high | medium | low — how certain this belongs]
  WHY_OMITTED: [why the author likely didn't include it explicitly — less prototypical, less common, less important, or assumed obvious]
```

### Expansion Quality Rules

- **Every item must pass the membership test** from Phase 2
- **Maintain the same granularity** as the head items — if the head has "Python, Java," don't expand with "programming" or "Python 3.11"
- **Order by relevance** — most likely omissions first, edge cases last
- **Flag edge cases** — items that might or might not belong, depending on interpretation

---

## Phase 4: Completeness

Define when to stop:

```
[E-N] STOP_RULE: [the criterion for completeness]
  TYPE: [exhaustive | representative | threshold | diminishing]
  TOTAL_ITEMS: [head + expanded = N]
  REMAINING: [items deliberately excluded and why]
```

### Stopping Criteria

| Type | Definition | When to Use |
|------|-----------|------------|
| **Exhaustive** | Every member of the category is listed | Small, finite categories (days of week, US states) |
| **Representative** | Enough items to cover major subcategories | Large categories where exhaustive is impractical |
| **Threshold** | Items above a relevance/frequency threshold | When some members are too obscure to matter |
| **Diminishing** | Stop when new items add negligible information | Open-ended categories |

---

## Phase 5: Output

```
EXPANDED LIST
=============

ORIGINAL: [quoted input with "etc"]
RULE: [the continuation pattern]
CONFIDENCE: [level]

EXPLICIT (from author):
  1. [item]
  2. [item]
  3. [item]

EXPANDED (inferred):
  4. [item] — CONFIDENCE: [level]
  5. [item] — CONFIDENCE: [level]
  6. [item] — CONFIDENCE: [level]
  ...

EDGE CASES (might belong):
  - [item] — DEPENDS_ON: [what interpretation]

STOP: [completeness criterion] — TOTAL: [N items]

ALTERNATIVE RULE: [if a different continuation rule exists]
  WOULD PRODUCE: [different expansion under that rule]

READY FOR:
- /se [category] — to systematically enumerate instead of inferring
- /mv — to validate the expanded list is MECE
- /aso — to expand "and so on" patterns (related skill)
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Wrong rule** | Expanded items clearly don't match the author's intent | Generate multiple candidate rules and use context to select |
| **Granularity mismatch** | Head has "Python, Java" and expansion has "scripting languages" | Match the specificity level of the head items exactly |
| **No stop rule** | List keeps growing without bound | Define completeness criterion before expanding |
| **Only obvious items** | Expanded items are the first things anyone would think of | The value is in the non-obvious members. Push past the obvious |
| **Category drift** | Items get progressively less related to the head | Every item must pass the membership test. Check the last few items especially |
| **Single rule assumed** | Only one interpretation considered | Always generate 2+ candidate rules. If context is ambiguous, present multiple expansions |
| **Head items unchallenged** | Assuming all head items perfectly fit the rule | Sometimes the author's own examples are inconsistent. Note when head items don't all fit one clean rule |

---

## Depth Scaling

| Depth | Candidate Rules | Expansion Size | Edge Cases | Alternative Expansions |
|-------|----------------|---------------|-----------|----------------------|
| 1x | 1 (best fit) | 3-5 items | No | No |
| 2x | 2-3 | 5-8 items | Flagged | 1 alternative |
| 4x | 3+ | 8-12 items | Analyzed | 2 alternatives |
| 8x | All plausible | Exhaustive or representative | Full analysis | All alternatives |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] List head extracted with all explicit items
- [ ] Continuation rule inferred explicitly (not assumed)
- [ ] Membership test defined
- [ ] Multiple candidate rules considered
- [ ] Expanded items all pass the membership test
- [ ] Granularity matches the head items
- [ ] Stop rule defined and applied
- [ ] Edge cases flagged where appropriate
- [ ] At least one alternative interpretation noted (at 2x+)

---

## Integration

- Use from: encountering "etc", "and so on", "...", incomplete lists, vague enumerations
- Routes to: `/se` (systematic enumeration for thorough coverage), `/mv` (validate list structure)
- Complementary: `/aso` (handles "and so on" patterns — related but distinct trigger)
- Differs from `/se`: se generates lists from scratch; etc expands an existing partial list
- Differs from `/aso`: aso focuses on continuation patterns; etc focuses on category membership and completion
- Differs from `/list`: list builds lists with quality criteria; etc expands existing compressed lists
