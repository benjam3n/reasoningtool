---
name: "difr - Differentiation Reasoning"
description: "Reason about what makes things different by identifying similarities first, then classifying differences by significance and contextual relevance."
output:
  format: "prose"
---

# DIFR - Differentiation Reasoning

**Input**: $ARGUMENTS

---

## Step 1: Identify the Things Being Compared

```
ITEM A: [first thing]
ITEM B: [second thing]
ADDITIONAL ITEMS: [if comparing more than two]
COMPARISON CONTEXT: [why these are being compared — what decision or understanding depends on the differences]
```

Context determines which differences matter. Two things can be "the same" in one context and "completely different" in another.

---

## Step 2: List All Similarities

```
SIMILARITIES:
  1. [similarity] — DIMENSION: [what aspect this covers]
  2. [similarity] — DIMENSION: [aspect]
  3. [similarity] — DIMENSION: [aspect]
  ...
```

Start with similarities deliberately. This prevents the common error of treating superficially different things as fundamentally different. If two things share 90% of their properties, the remaining 10% is what actually distinguishes them.

---

## Step 3: Identify Differences

```
DIFFERENCES:
  1. [difference]
     A IS: [how item A handles this]
     B IS: [how item B handles this]
     DIMENSION: [what aspect this difference covers]
  2. [difference]
     A IS: [description]
     B IS: [description]
     DIMENSION: [aspect]
  ...
```

Be precise. "A is better" is not a difference — it's a judgment. "A processes 1000 requests/second, B processes 200" is a difference.

---

## Step 4: Classify Differences

For each difference:

```
CLASSIFICATION: [difference]
  LEVEL: [trivial | significant | fundamental]
  CRITERIA:
    TRIVIAL: cosmetic, matters of taste, easily changed
    SIGNIFICANT: affects outcomes, requires adaptation, hard to change
    FUNDAMENTAL: defines the nature of the thing, cannot be changed without becoming something else
```

Fundamental differences are rare. Most differences people think are fundamental are actually significant or trivial. Be rigorous about this classification.

---

## Step 5: Determine Which Differences Matter

```
CONTEXTUAL RELEVANCE:
  CONTEXT: [restate the comparison context from Step 1]

  DIFFERENCES THAT MATTER:
    1. [difference] — WHY IT MATTERS: [how this affects the decision or understanding]
       WEIGHT: [high | medium | low]
    2. [difference] — WHY IT MATTERS: [impact on context]
       WEIGHT: [level]

  DIFFERENCES THAT DON'T MATTER:
    1. [difference] — WHY IRRELEVANT: [why this doesn't affect the decision]
    2. [difference] — WHY IRRELEVANT: [reason]
```

---

## Output Summary

```
DIFFERENTIATION ANALYSIS
========================
COMPARING: [A] vs [B]
CONTEXT: [why this comparison matters]

SHARED: [key similarities that establish common ground]

KEY DIFFERENCES (ranked by relevance):
  1. [most important difference] — [why it matters most]
  2. [second most important] — [why]
  3. [third] — [why]

FUNDAMENTAL DIFFERENCES: [if any — differences in kind, not degree]
TRIVIAL DIFFERENCES: [differences to ignore]

BOTTOM LINE: [one-sentence statement of what truly distinguishes these things in this context]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Skipping similarities** | Jumping straight to differences | Similarities first — they frame what differences mean |
| **Everything is fundamental** | No trivial or significant differences found | Most differences are not fundamental — reclassify |
| **Context-free differencing** | Differences listed without relevance to a purpose | Differences only matter relative to a context |
| **Judgment as difference** | "A is better than B" stated as a difference | State the factual difference, then judge separately |
| **Missing asymmetric differences** | Only finding differences where both have something | Also check for things one has that the other lacks entirely |

---

## Integration

- Use with: `/agsk` to analyze how different arguments differ in structure
- Use with: `/cmpr` to check if the comparison is complete
- Use with: `/dtsk` to differentiate data sets or data sources
- Use from: `/decide` when choosing between similar options
- Differs from `/cmp`: difr focuses on what makes things different; cmp compares to choose between them
