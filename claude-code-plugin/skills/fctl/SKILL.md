---
name: "fctl - Factual Claim Testing"
description: Test whether a factual claim is true. Assess evidence quality, check for common errors, and deliver a verdict with confidence level.
---

# Factual Claim Testing

**Input**: $ARGUMENTS

---

## Step 1: State the Claim Precisely

Rewrite the claim so it's unambiguous and testable.

```
ORIGINAL CLAIM: [as stated by the user]
PRECISE CLAIM: [rewritten with specific scope, timeframe, and definitions]
CLAIM TYPE: [empirical / statistical / historical / definitional]
```

Rules:
- Remove weasel words ("many," "often," "significant") and replace with specifics where possible
- If the claim is vague, state the most charitable precise interpretation
- If multiple interpretations exist, test each separately
- A claim that can't be made precise can't be tested — flag this

---

## Step 2: Identify Truth Conditions

Define what would make the claim true and what would make it false.

```
TRUE IF:
- [Condition 1]
- [Condition 2]

FALSE IF:
- [Condition 1]
- [Condition 2]

UNCLEAR / UNTESTABLE IF:
- [Condition — e.g., key data doesn't exist]
```

Rules:
- Truth conditions must be observable or measurable in principle
- If nothing could falsify the claim, it's not a factual claim — reclassify it
- "Unclear" is a legitimate outcome — not everything is decidable

---

## Step 3: Find Evidence

Gather the best available evidence for and against.

```
EVIDENCE FOR:
1. [Evidence]: [Source] — Strength: [STRONG / MODERATE / WEAK]
2. [Evidence]: [Source] — Strength: [STRONG / MODERATE / WEAK]

EVIDENCE AGAINST:
1. [Evidence]: [Source] — Strength: [STRONG / MODERATE / WEAK]
2. [Evidence]: [Source] — Strength: [STRONG / MODERATE / WEAK]

EVIDENCE ABSENT (expected evidence that doesn't exist):
- [What you'd expect to find if the claim were true but can't find]
```

Rules:
- Actively look for evidence against, not just evidence for
- Absent evidence matters — if the claim were true, what evidence should exist but doesn't?
- Rate source quality: peer-reviewed > institutional > journalistic > anecdotal > unsourced
- Note if evidence is outdated — facts change

---

## Step 4: Check for Common Errors

Scan for the most frequent ways factual claims go wrong.

```
ERROR CHECK:
- [ ] Selection bias: Is the evidence cherry-picked?
- [ ] Survivorship bias: Are failures/negatives missing from the data?
- [ ] Outdated data: Has the underlying reality changed since the evidence was collected?
- [ ] Ecological fallacy: Is a group-level claim being applied to individuals (or vice versa)?
- [ ] Base rate neglect: Is the claim ignoring how common the baseline is?
- [ ] Conflation: Is the claim conflating two different things?
- [ ] Precision mismatch: Is the claim more precise than the evidence supports?

ERRORS FOUND:
- [Error type]: [How it affects the claim]
```

Rules:
- Check every item on the list — don't skip because the claim "feels right"
- Finding an error doesn't automatically make the claim false — it weakens the evidence
- Multiple small errors compound — three weak errors together can undermine a claim

---

## Step 5: Verdict

Deliver a judgment with calibrated confidence.

```
VERDICT: [TRUE / MOSTLY TRUE / MIXED / MOSTLY FALSE / FALSE / UNDETERMINED]

CONFIDENCE: [HIGH / MEDIUM / LOW]

REASONING: [2-3 sentences explaining the verdict]

CAVEATS:
- [Important qualification 1]
- [Important qualification 2]

WHAT WOULD CHANGE THE VERDICT:
- [Specific new evidence or analysis that could flip the conclusion]
```

Rules:
- Use the full range of verdicts — most claims are not cleanly true or false
- Confidence reflects evidence quality, not how sure you feel
- HIGH confidence = strong evidence, multiple sources, tested against errors
- LOW confidence = thin evidence, single source, or significant errors found
- Always state what would change your mind

---

## Integration

Use with:
- `/cscl` -> If the claim is causal, use causal claim analysis instead
- `/pcl` -> If the claim is a prediction, use predictive claim analysis instead
- `/ncl` -> If the claim is a "should" statement, use normative claim analysis instead
- `/hpat` -> Check historical patterns relevant to the factual claim
