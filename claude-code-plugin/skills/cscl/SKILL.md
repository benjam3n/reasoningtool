---
name: "cscl - Causal Claim Analysis"
description: Test whether X actually causes Y. Check confounders, mechanisms, temporal ordering, and counterfactuals.
---

# Causal Claim Analysis

**Input**: $ARGUMENTS

---

## Step 1: State the Causal Claim

Extract and formalize the causal relationship being claimed.

```
CAUSAL CLAIM: [X] causes [Y]
DIRECTION: [X -> Y] (not Y -> X, not Z -> both)
CLAIMED MECHANISM: [How X supposedly produces Y]
CLAIM STRENGTH: [ALWAYS / USUALLY / SOMETIMES / CAN]
```

Rules:
- Distinguish "causes" from "is associated with" or "precedes"
- If the input contains an implicit causal claim (e.g., "remote work improves productivity"), make it explicit
- If multiple causal claims are embedded, separate and test each one
- Note the claimed strength — "X always causes Y" is a much stronger claim than "X can cause Y"

---

## Step 2: Check for Confounders

Identify third variables that could explain the apparent X->Y relationship.

```
POTENTIAL CONFOUNDERS:
1. [Confounder Z]: Could cause both [X] and [Y] because [reason]
   - Plausibility: [HIGH / MEDIUM / LOW]
2. [Confounder Z]: Could cause both [X] and [Y] because [reason]
   - Plausibility: [HIGH / MEDIUM / LOW]
...

CONFOUNDING RISK: [HIGH / MEDIUM / LOW]
```

Rules:
- Generate at least 3 potential confounders before assessing
- Common confounders: socioeconomic status, motivation, pre-existing conditions, selection effects
- If no confounders seem plausible, you probably haven't looked hard enough
- High confounding risk means the causal claim needs much stronger evidence

---

## Step 3: Check Temporal Ordering

Verify that the alleged cause actually precedes the alleged effect.

```
TEMPORAL ANALYSIS:
- Does X reliably precede Y? [YES / NO / UNCLEAR]
- Could Y cause X instead (reverse causation)? [YES / NO / POSSIBLE]
- Evidence for temporal ordering: [what shows X comes first]
- Lag time: [how long between X and Y]
```

Rules:
- If Y sometimes precedes X, the causal claim is severely weakened
- Reverse causation is more common than people think — always check
- Very long lag times make causation harder to establish (more room for confounders)
- Simultaneous X and Y could mean a common cause, not X->Y

---

## Step 4: Look for Mechanism

Assess whether there's a plausible pathway from X to Y.

```
MECHANISM ANALYSIS:
- Proposed pathway: [X] -> [intermediate step] -> ... -> [Y]
- Is each link in the chain plausible? [assessment]
- Are there known mechanisms that would block this pathway? [assessment]
- Mechanism strength: [WELL-ESTABLISHED / PLAUSIBLE / SPECULATIVE / UNKNOWN]
```

Rules:
- A correlation with a known mechanism is much more likely to be causal
- A correlation without any plausible mechanism should be treated with skepticism
- "We don't know the mechanism" is different from "there is no mechanism"
- Multiple plausible mechanisms for the same link increase confidence

---

## Step 5: Check Dose-Response

Test whether more X produces more (or less) Y.

```
DOSE-RESPONSE:
- Does increasing X increase Y? [YES / NO / NONLINEAR / UNKNOWN]
- Is there a threshold effect? [X must reach level N before Y appears]
- Is there a ceiling effect? [More X stops producing more Y after a point]
- Evidence: [what shows the dose-response relationship]
```

Rules:
- A clear dose-response relationship strengthens the causal claim significantly
- Absence of dose-response doesn't disprove causation (threshold effects are real)
- If dose-response is unknown, note the gap — it's important missing evidence

---

## Step 6: Test Counterfactual

Ask: if X hadn't happened, would Y still have occurred?

```
COUNTERFACTUAL TEST:
- If X were absent, would Y still occur? [LIKELY YES / UNCERTAIN / LIKELY NO]
- Are there cases where X is absent and Y occurs anyway? [evidence]
- Are there cases where X is present and Y doesn't occur? [evidence]
- Counterfactual support for causation: [STRONG / MODERATE / WEAK]
```

Rules:
- If Y happens frequently without X, then X is at most a contributing cause, not THE cause
- If X is present but Y doesn't occur, look for moderating variables
- Natural experiments (situations where X was randomly present/absent) are the best evidence

---

## Step 7: Assess Overall Causal Evidence

```
CAUSAL VERDICT:
- Claim: [X] causes [Y]
- Verdict: [STRONG CAUSAL EVIDENCE / MODERATE / WEAK / INSUFFICIENT / LIKELY NOT CAUSAL]
- Confidence: [HIGH / MEDIUM / LOW]

STRENGTH SUMMARY:
- Confounders controlled: [YES / PARTIALLY / NO]
- Temporal order confirmed: [YES / NO]
- Mechanism identified: [YES / PARTIALLY / NO]
- Dose-response present: [YES / NO / UNKNOWN]
- Counterfactual supported: [YES / PARTIALLY / NO]

ALTERNATIVE EXPLANATION: [The most plausible non-causal explanation for the X-Y relationship]
```

---

## Integration

Use with:
- `/fctl` -> If the underlying facts of the claim need verification first
- `/hpat` -> Check if the causal pattern holds across historical cases
- `/pcl` -> If the causal claim implies predictions, test those predictions
- `/rlcl` -> If the relationship might not be causal, analyze what type it actually is
