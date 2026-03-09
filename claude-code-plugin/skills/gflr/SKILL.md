---
name: "gflr - Gap-Filling Reasoning"
description: "Reason about what's missing and why it matters by identifying intended completeness, enumerating present elements, and prioritizing gaps by impact."
---

# GFLR - Gap-Filling Reasoning

**Input**: $ARGUMENTS

---

## Step 1: Identify the Intended Complete Set

```
SUBJECT: [what we're examining for gaps]
COMPLETE SET DEFINITION: [what "complete" looks like for this context]
SOURCE OF COMPLETENESS STANDARD:
  [standard | best practice | explicit specification | logical necessity | domain convention]
CONFIDENCE IN STANDARD: [high | medium | low]
```

You cannot find gaps without a reference for what "complete" means. If no standard exists, construct one and state your assumptions.

---

## Step 2: Enumerate What's Present

```
PRESENT ELEMENTS:
  1. [element] — STATUS: [complete | partial | placeholder]
  2. [element] — STATUS: [complete | partial | placeholder]
  3. [element] — STATUS: [complete | partial | placeholder]
  ...
```

List everything that currently exists. Be exhaustive — gaps become visible only when the present set is fully enumerated.

---

## Step 3: Identify What's Absent

```
ABSENT ELEMENTS:
  1. [missing element]
     EXPECTED BECAUSE: [why the completeness standard includes this]
     CATEGORY: [core | supporting | peripheral]
  2. [missing element]
     EXPECTED BECAUSE: [reason]
     CATEGORY: [core | supporting | peripheral]
  ...
```

Core elements are essential for function. Supporting elements improve quality. Peripheral elements are nice-to-have.

---

## Step 4: Assess Whether Absences Are Intentional

For each absence:

```
GAP ASSESSMENT: [missing element]
  INTENTIONAL: [yes | no | unclear]
  REASONING:
    IF INTENTIONAL: [why it was likely excluded — scope, cost, priority]
    IF OVERSIGHT: [why it was likely missed — blind spot, assumption, rush]
    IF UNCLEAR: [what information would determine intent]
```

Intentional gaps are often defensible. Oversights are where the real problems hide. Don't treat every gap as a problem — some are legitimate design choices.

---

## Step 5: Prioritize Gaps by Impact

```
GAP PRIORITY RANKING:
  1. [gap] — IMPACT: [what breaks or degrades without this]
     SEVERITY: [critical | significant | moderate | minor]
     URGENCY: [immediate | soon | eventual | optional]
  2. [gap] — IMPACT: [consequence]
     SEVERITY: [level]
     URGENCY: [level]
  ...
```

Prioritize by consequence, not by ease of filling. The hardest gap to fill is often the most important one.

---

## Step 6: Recommend Fills

```
RECOMMENDATIONS:
  1. FILL: [gap]
     HOW: [specific approach to closing this gap]
     EFFORT: [low | medium | high]
     VALUE: [what completing this adds]
     PRIORITY: [must-do | should-do | could-do]
  2. FILL: [gap]
     HOW: [approach]
     EFFORT: [level]
     VALUE: [benefit]
     PRIORITY: [level]

ACCEPTABLE GAPS (intentionally unfilled):
  1. [gap] — REASON TO LEAVE: [why filling this isn't worth it]
```

---

## Output Summary

```
GAP ANALYSIS
============
SUBJECT: [what was analyzed]
COMPLETENESS: [X of Y elements present — percentage]
CRITICAL GAPS: [count and list]
SIGNIFICANT GAPS: [count and list]
TOP PRIORITY: [the single most important gap to fill]
RECOMMENDED ACTIONS: [ordered list]
INTENTIONAL GAPS: [gaps that are acceptable as-is]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **No completeness standard** | Gaps found without reference to what "complete" means | Define the standard first |
| **Everything is a gap** | Huge list with no prioritization | Rank by impact, accept some gaps as intentional |
| **Assuming all gaps are oversights** | No assessment of intentionality | Check whether each absence was a deliberate choice |
| **Present-set is incomplete** | Gaps identified but present elements not fully listed | Enumerate present elements exhaustively first |
| **Impact not assessed** | Gaps listed without consequence analysis | Every gap must have an impact statement |

---

## Integration

- Use with: `/cmpr` to verify completeness claims more formally
- Use with: `/sysk` to find missing components in a system
- Use with: `/rlsk` to identify unmet needs in relationships
- Use from: `/evaluate` when assessing whether work is complete
- Differs from `/cmpr`: gflr focuses on what's missing and why; cmpr assesses whether something meets completeness criteria
