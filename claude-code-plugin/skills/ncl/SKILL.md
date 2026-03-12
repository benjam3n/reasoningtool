---
name: "ncl - Normative Claim Analysis"
description: Evaluate a "should" claim. Identify underlying values, check if prescriptions serve those values, and assess competing considerations.
output:
  format: "prose"
---

# Normative Claim Analysis

**Input**: $ARGUMENTS

---

## Step 1: State the Normative Claim

Extract the "should" statement and make it explicit.

```
ORIGINAL STATEMENT: [as stated]
NORMATIVE CLAIM: [rewritten as a clear "X should Y" statement]
CLAIM SCOPE: [universal / contextual / personal]
PRESCRIBES: [what action or state of affairs is being recommended]
IMPLICIT AUDIENCE: [who is being told they "should"]
```

Rules:
- Many normative claims are disguised as factual claims — "it's important to X" means "you should X"
- Distinguish between moral "should," prudential "should," and aesthetic "should"
- Make the audience explicit — "one should" often means "you specifically should"
- If multiple "shoulds" are present, separate and analyze each

---

## Step 2: Identify the Underlying Value

Find the value or principle that makes the "should" feel compelling.

```
VALUE ANALYSIS:
- Primary value: [The value that drives this claim — e.g., fairness, efficiency, safety, autonomy]
- Value type: [moral / prudential / aesthetic / conventional / epistemic]
- Is the value stated or assumed? [STATED / ASSUMED]
- How widely shared is this value? [UNIVERSAL / WIDELY SHARED / CONTESTED / NICHE]
```

Rules:
- Every "should" is powered by at least one value — find it
- If the value is assumed rather than stated, the argument is weaker
- Universal values (reduce suffering, keep promises) are stronger foundations than niche ones
- Some claims stack multiple values — identify all of them

---

## Step 3: Check If the Value Is Shared

Assess whether the audience actually holds the underlying value.

```
VALUE AGREEMENT:
- Does the target audience hold this value? [YES / MOSTLY / SPLIT / NO]
- What would someone who REJECTS this value say? [steel-manned counter-position]
- Is the disagreement about the value itself or about facts? [VALUE DISAGREEMENT / FACTUAL DISAGREEMENT]
- If factual: what facts would resolve it?
- If value-based: is compromise possible?
```

Rules:
- If the audience doesn't share the value, the "should" has no force for them
- Many apparent value disagreements are actually factual disagreements in disguise
- "You should exercise" — is the disagreement about health's importance, or about exercise's effectiveness?
- Identifying the real source of disagreement is more useful than insisting on the "should"

---

## Step 4: Check If the Prescription Serves the Value

Test whether doing the recommended thing actually achieves the underlying value.

```
PRESCRIPTION EFFECTIVENESS:
- Does [prescribed action] actually achieve [underlying value]? [YES / PARTIALLY / NO / UNKNOWN]
- Evidence: [what shows the prescription works or doesn't]
- Unintended consequences: [does the prescription create new problems?]
- Alternative prescriptions: [other actions that might serve the same value better]
  1. [Alternative]: [how it serves the value]
  2. [Alternative]: [how it serves the value]
```

Rules:
- This is where many "should" claims fail — the value is right but the prescription is wrong
- "You should eat less fat" — even if health is the right value, the prescription might not serve it
- Always check for unintended consequences — prescriptions often create new problems
- If alternatives serve the value better, the original "should" is weakened

---

## Step 5: Identify Competing Values

Find values that conflict with the claim's underlying value.

```
VALUE TENSIONS:
1. [Competing value]: [How it conflicts with the primary value]
   - Which wins in this context? [assessment]
   - Can both be served? [YES — how / NO — which takes priority]

2. [Competing value]: [How it conflicts]
   - Which wins? [assessment]
   - Can both be served? [assessment]
```

Rules:
- Almost every "should" trades off against something else
- "You should be honest" competes with "you should be kind" in specific situations
- "You should move fast" competes with "you should be careful"
- The strength of a "should" depends on how it handles its competing values, not just its primary value

---

## Step 6: Assess the Strength of the "Should"

Deliver a final assessment.

```
NORMATIVE VERDICT:
- Claim: [the "should" statement]
- Underlying value: [identified value]
- Value strength: [STRONG / MODERATE / WEAK]
- Prescription effectiveness: [EFFECTIVE / PARTIALLY EFFECTIVE / INEFFECTIVE]
- Competing values addressed: [YES / PARTIALLY / NO]

OVERALL ASSESSMENT: [COMPELLING / REASONABLE / WEAK / UNFOUNDED]

STRONGEST VERSION: [How the claim would need to be modified to be as strong as possible]

KEY OBJECTION: [The single best argument against this "should"]
```

---

## Integration

Use with:
- `/fctl` -> Verify factual claims embedded in the normative argument
- `/cscl` -> Test causal claims about what the prescription will achieve
- `/mocl` -> If the claim involves "could" or "would," analyze those modal aspects
- `/icl` -> If the claim involves what someone intends, analyze credibility
