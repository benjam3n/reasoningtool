---
name: "agsk - Argument Analysis"
description: "Analyze and construct arguments by checking logical validity, premise truth, hidden assumptions, and evidence strength."
---

# AGSK - Argument Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify the Claim

```
CLAIM: [the central assertion being made]
CLAIM TYPE: [empirical | normative | definitional | causal | predictive]
SCOPE: [universal | general | specific | particular]
```

If the input contains multiple claims, identify the primary claim and list secondary claims separately. Analyze the primary claim through the remaining steps.

---

## Step 2: Identify the Premises

```
PREMISES:
  P1: [first supporting reason]
      STATUS: [stated explicitly | implied | reconstructed]
  P2: [second supporting reason]
      STATUS: [stated | implied | reconstructed]
  P3: [third supporting reason, if any]
      STATUS: [stated | implied | reconstructed]
```

Reconstruct the argument charitably. If a premise is implied but needed for the argument to work, include it and mark it as reconstructed.

---

## Step 3: Check Logical Validity

```
ARGUMENT STRUCTURE:
  IF [P1] AND [P2] THEN [CLAIM]?
  VALID: [yes | no]
  FORM: [deductive | inductive | abductive | analogical]
```

If **deductive**: Do the premises guarantee the conclusion? If any premise is true and the conclusion could still be false, the argument is invalid.

If **inductive**: Do the premises make the conclusion probable? How probable?

If **abductive**: Is this the best explanation? What alternatives exist?

If **analogical**: How strong is the analogy? Where does it break?

---

## Step 4: Check Premise Truth

For each premise:

```
P[N] ASSESSMENT:
  TRUTH: [true | false | uncertain | partially true]
  EVIDENCE FOR: [what supports this premise]
  EVIDENCE AGAINST: [what undermines this premise]
  VERDICT: [strong | adequate | weak | unsupported]
```

An argument can be logically valid but have false premises. Both checks are needed.

---

## Step 5: Identify Hidden Assumptions

```
HIDDEN ASSUMPTIONS:
  A1: [assumption the argument requires but doesn't state]
      PLAUSIBILITY: [high | medium | low]
      IF FALSE: [what happens to the argument]
  A2: [another hidden assumption]
      PLAUSIBILITY: [high | medium | low]
      IF FALSE: [consequence for the argument]
```

Common hiding places: definitions taken for granted, causal mechanisms assumed, scope limitations unstated, value judgments embedded as facts.

---

## Step 6: Assess Strength of Evidence

```
EVIDENCE ASSESSMENT:
  TOTAL EVIDENCE CITED: [count]
  TYPES: [anecdotal | statistical | expert | experimental | logical]
  STRONGEST PIECE: [which evidence and why]
  WEAKEST PIECE: [which evidence and why]
  MISSING EVIDENCE: [what evidence would strengthen or weaken the argument]
  OVERALL EVIDENCE QUALITY: [strong | adequate | weak | absent]
```

---

## Step 7: Find the Strongest Objection

```
STRONGEST OBJECTION:
  OBJECTION: [the single best counterargument]
  TARGETS: [which premise, assumption, or logical step it attacks]
  FORCE: [devastating | significant | moderate | minor]
  POSSIBLE RESPONSE: [how the arguer might reply]
  RESPONSE QUALITY: [strong | adequate | weak]
```

The strongest objection is not necessarily the most obvious one. It attacks the weakest load-bearing element of the argument.

---

## Step 8: Overall Assessment

```
ARGUMENT QUALITY
================
CLAIM: [restate]
VALIDITY: [valid | invalid | partially valid]
SOUNDNESS: [sound | unsound | uncertain]
EVIDENCE: [strong | adequate | weak]
STRONGEST POINT: [what the argument gets most right]
WEAKEST POINT: [where it's most vulnerable]
OVERALL GRADE: [compelling | reasonable | weak | fallacious]
VERDICT: [should the claim be accepted, rejected, or held pending more evidence?]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Straw-manning** | Weakening the argument before analyzing it | Reconstruct the strongest version first |
| **Missing the real claim** | Analyzing a subsidiary point | Ask: what is the arguer MOST committed to? |
| **Validity-only checking** | Ignoring premise truth | A valid argument with false premises proves nothing |
| **Listing fallacies** | Naming fallacies without explaining impact | Show HOW the fallacy undermines the specific argument |
| **No strongest objection** | Only finding minor issues | What would make a smart proponent of this argument worry? |

---

## Integration

- Use with: `/rlsk` to analyze arguments occurring within relationships
- Use with: `/cmpr` to check if the argument is complete
- Use with: `/difr` to differentiate this argument from similar ones
- Use from: `/claim` when testing a specific claim's argument structure
- Differs from `/ht`: agsk analyzes argument structure; ht tests hypotheses empirically
