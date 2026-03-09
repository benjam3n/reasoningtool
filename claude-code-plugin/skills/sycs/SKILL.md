---
name: "sycs - So You Can See"
description: "Expand implications of a statement so the hidden conclusions are explicit, ordered by depth, and flagged by impact and testability."
---

# SYCS - So You Can See

**Input**: $ARGUMENTS

---

## Core Principles

1. **Implications branch exponentially.** Every statement implies multiple things, each of which implies multiple things. Without principled pruning, you drown in implications. The skill must bound the expansion while preserving the important branches.

2. **Depth degrades reliability.** First-order implications are usually solid. Second-order implications are plausible. Third-order and beyond are speculative. Track the depth and mark the reliability gradient.

3. **Not all implications are logical.** Some implications are logical necessities (if A then necessarily B). Others are empirical predictions (if A then probably B). Others are social/practical consequences (if A then people will likely do C). Each type has different confidence.

4. **The most important implications are non-obvious.** The obvious implication of "we're cutting the budget" is "we'll spend less." The non-obvious implication might be "we'll lose our best engineer who joined for the project budget enables." Surface the non-obvious ones.

5. **Testability makes implications useful.** An implication you can test is actionable. An implication you can't test is speculation. Flag which is which.

---

## Phase 1: Source Statement

```
[Y1] SOURCE: [the statement to expand, quoted]
[Y2] CONTEXT: [relevant context that affects implications]
[Y3] STATEMENT_TYPE: [claim | decision | observation | prediction | policy]
```

---

## Phase 2: First-Order Implications

Direct implications — what follows immediately from the source statement.

```
[Y4] IMPLICATION: [what follows] — TYPE: [logical | empirical | practical | social]
  CONFIDENCE: [high | medium | low]
  OBVIOUS: [yes | no]
  TESTABLE: [yes — how | no]
[Y5] IMPLICATION: [what follows] — TYPE: [type]
  CONFIDENCE: [level]
  OBVIOUS: [yes/no]
  TESTABLE: [yes/no]
...
```

### Implication Types

| Type | What It Means | Confidence Basis |
|------|--------------|-----------------|
| **Logical** | Necessarily follows from the statement | Deductive — if A then must B |
| **Empirical** | Usually follows based on evidence/experience | Inductive — if A then probably B |
| **Practical** | Follows as a consequence of action/policy | Consequential — if A then action B needed |
| **Social** | Follows from how people typically respond | Behavioral — if A then people will likely B |

---

## Phase 3: Second-Order Implications

For each high-confidence or high-impact first-order implication, expand one level deeper:

```
[Y-N] FROM [Y-ref]: [second-order implication]
  TYPE: [logical | empirical | practical | social]
  CONFIDENCE: [typically lower than parent]
  IMPACT: [high | medium | low]
  TESTABLE: [yes — how | no]
```

### Pruning Rules

Expand a first-order implication to second order ONLY if:
- Its confidence is medium or higher, AND
- Its impact is medium or higher, OR
- It's non-obvious (surprising implications deserve expansion even if low impact)

Do NOT expand if:
- First-order confidence is low (speculating on speculation)
- The implication is obvious and low-impact (not worth the depth)

---

## Phase 4: Impact Flagging

From all implications (first and second order), identify the highest-impact ones:

```
[Y-N] HIGH-IMPACT IMPLICATIONS:
  1. [Y-ref]: [implication] — IMPACT: [why this matters most]
     TESTABLE: [yes — test | no]
     ACTION_IF_TRUE: [what to do about it]
  2. [Y-ref]: [implication] — IMPACT: [why]
     TESTABLE: [yes/no]
     ACTION_IF_TRUE: [action]
  3. [Y-ref]: [implication] — IMPACT: [why]
     ...
```

### Non-Obvious Flag

```
[Y-N] NON-OBVIOUS IMPLICATIONS:
  1. [Y-ref]: [implication] — WHY_NON_OBVIOUS: [why most people would miss this]
  2. [Y-ref]: [implication] — WHY_NON_OBVIOUS: [why]
```

---

## Phase 5: Output

```
IMPLICATION EXPANSION
=====================

SOURCE: [quoted statement]
CONTEXT: [relevant context]

FIRST-ORDER (direct implications):
  [Y4] [implication] — [type] — Confidence: [level] — Testable: [yes/no]
  [Y5] [implication] — [type] — Confidence: [level] — Testable: [yes/no]
  ...

SECOND-ORDER (implications of implications):
  From [Y4]:
    [Y-N] [implication] — [type] — Confidence: [level]
  From [Y5]:
    [Y-N] [implication] — [type] — Confidence: [level]
  ...

HIGH-IMPACT (prioritized):
  1. [implication] — [why high impact] — Test: [how]
  2. [implication] — [why high impact] — Test: [how]

NON-OBVIOUS:
  1. [implication] — [why most people miss this]

READY FOR:
- /ht [implication] — to formulate a testable hypothesis
- /ar [implication] — to explore what follows if this implication is right
- /aw [implication] — to stress-test a high-impact implication
- /claim [implication] — to verify a specific implication
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Unbounded expansion** | 30+ implications listed with no pruning | Apply pruning rules at each depth level |
| **Only obvious implications** | Every implication is "well, duh" | Specifically search for non-obvious consequences |
| **Confidence not tracked** | All implications treated as equally likely | Mark confidence at each depth level |
| **Depth-blind** | Third-order implications treated with same confidence as first-order | Confidence typically decreases with depth |
| **Type conflation** | Logical necessity confused with empirical prediction | Apply type definitions — does B NECESSARILY follow from A? |
| **No testability check** | Implications listed without actionability | Flag testable vs not-testable for each |
| **Impact not prioritized** | Flat list with no high-impact flagging | Always identify the top 3 highest-impact implications |

---

## Depth Scaling

| Depth | Min First-Order | Max Depth | Min High-Impact | Min Non-Obvious |
|-------|----------------|-----------|----------------|-----------------|
| 1x | 3 | 1st order only | 1 | 0 |
| 2x | 5 | 2nd order | 2 | 1 |
| 4x | 8 | 3rd order | 4 | 2 |
| 8x | 12 | 4th order | 6 | 4 |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Source statement clearly identified with context
- [ ] First-order implications extracted with type and confidence
- [ ] Pruning rules applied before second-order expansion
- [ ] Second-order implications have lower confidence than parents
- [ ] High-impact implications flagged with reasoning
- [ ] Non-obvious implications specifically sought and identified
- [ ] Testability assessed for each implication
- [ ] Action recommendations for testable high-impact implications

---

## Integration

- Use from: any statement analysis, strategic planning
- Routes to: `/ht`, `/ar`, `/aw`, `/claim` for testing specific implications
- Complementary: `/aex` (extracts hidden assumptions — different from implications)
- Differs from `/aex`: aex finds what must be TRUE for a claim to hold; sycs finds what FOLLOWS from a claim
- Differs from `/ar`: ar explores what follows if something is RIGHT; sycs expands implications neutrally
