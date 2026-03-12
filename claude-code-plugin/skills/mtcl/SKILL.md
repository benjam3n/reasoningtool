---
name: "mtcl - Meta Claim Analysis"
description: Evaluate claims about claims. Analyze what level a claim operates at, check self-referential consistency, and assess impact on object-level analysis.
output:
  format: "prose"
---

# Meta Claim Analysis

**Input**: $ARGUMENTS

---

## Step 1: State the Meta-Claim

Extract the claim-about-a-claim and identify what it's saying about the discussion itself.

```
OBJECT-LEVEL CLAIM: [The original claim being discussed]
META-CLAIM: [The claim ABOUT the original claim or about the discussion]
META-CLAIM TYPE:
- [ ] Epistemic: About what we can know ("This question is unanswerable")
- [ ] Methodological: About how to analyze ("You're using the wrong framework")
- [ ] Rhetorical: About the discussion itself ("That's a straw man")
- [ ] Scope: About boundaries ("That's outside the scope of this discussion")
- [ ] Status: About the state of debate ("This is settled science" / "This is controversial")
- [ ] Reflexive: About itself ("All claims are biased, including this one")
```

Rules:
- A meta-claim operates one level up from the object-level discussion
- "Your argument is wrong" is object-level; "Your type of argument can never work" is meta
- People often shift to meta-claims when losing the object-level argument — note if this is happening
- Meta-claims can be legitimate and important — don't dismiss them just because they're meta

---

## Step 2: Identify What Level It Operates At

Map where this claim sits in the stack of abstraction.

```
LEVEL MAP:
Level 0 (Object): [The actual topic — e.g., "Should we use React?"]
Level 1 (Meta): [Claim about the topic — e.g., "Framework debates are pointless"]
Level 2 (Meta-meta): [Claim about the meta-claim — e.g., "Saying debates are pointless is itself a framework preference"]
Level 3+ (Higher): [If applicable]

THIS CLAIM OPERATES AT: Level [N]
DOES IT CORRECTLY IDENTIFY ITS OWN LEVEL? [YES / NO]
```

Rules:
- Most useful meta-claims operate at Level 1
- Level 2+ claims are often unproductive — flag if the discussion is spiraling upward
- A claim that thinks it's Level 1 but is actually Level 0 is confused, not meta
- The value of identifying the level is deciding whether to engage at that level or redirect

---

## Step 3: Check Self-Referential Consistency

Test whether the meta-claim applies to itself, and if so, whether it survives.

```
SELF-REFERENCE TEST:
- Does this claim apply to itself? [YES / NO / PARTIALLY]
- If YES: Is it consistent when applied to itself? [CONSISTENT / PARADOXICAL / UNDERMINING]

EXAMPLES:
- "All generalizations are false" — applies to itself, creates paradox
- "We should question all assumptions" — applies to itself, survives (questioning this assumption is fine)
- "Nobody can be objective" — applies to itself, partially undermines (is THIS claim objective?)

RESULT: [SELF-CONSISTENT / SELF-UNDERMINING / SELF-REFERENTIAL PARADOX / NOT SELF-REFERENTIAL]
```

Rules:
- Self-undermining claims aren't automatically wrong — but they need to account for the self-reference
- Paradoxes are interesting but usually signal that the claim needs to be reformulated
- "Not self-referential" is the most common result — most meta-claims about specific topics don't apply to themselves
- If self-undermining, ask: can the claim be reformulated to avoid the problem?

---

## Step 4: Test for Consistency

Check whether the meta-claim is consistent with other things the claimant believes or says.

```
CONSISTENCY CHECK:
THE META-CLAIM IMPLIES:
1. [Implication 1]: Does the claimant accept this? [YES / NO / UNCLEAR]
2. [Implication 2]: Does the claimant accept this? [YES / NO / UNCLEAR]
3. [Implication 3]: Does the claimant accept this? [YES / NO / UNCLEAR]

CONFLICTS WITH:
- [Other position the claimant holds]: [How it conflicts]

CONSISTENCY VERDICT: [CONSISTENT / SELECTIVELY APPLIED / INCONSISTENT]
```

Rules:
- "Selectively applied" is the most common finding — meta-principles used when convenient, ignored when not
- If someone says "we can't trust experts" but then cites experts, that's selective application
- Inconsistency doesn't mean the meta-claim is wrong — it might mean the other positions are wrong
- Check if the meta-claim is being used as a tool (to win an argument) rather than as a genuine principle

---

## Step 5: Assess Impact on Object-Level Analysis

Determine whether the meta-claim, if true, actually changes anything about the original question.

```
IMPACT ASSESSMENT:
IF THE META-CLAIM IS TRUE:
- Does it invalidate the object-level analysis? [YES / NO / PARTIALLY]
- Does it change what methods are appropriate? [YES / NO — how]
- Does it change what conclusions are reachable? [YES / NO — how]
- Does it make the object-level question unanswerable? [YES / NO]

IF THE META-CLAIM IS FALSE:
- Does the object-level analysis proceed unchanged? [YES / NO]
- What was the meta-claim protecting or attacking? [assessment]

FUNCTIONAL ASSESSMENT:
- Is this meta-claim advancing understanding or blocking it? [ADVANCING / BLOCKING / NEUTRAL]
- Is it being used to avoid engaging with the object-level question? [YES / NO]
- Recommended response: [ENGAGE AT META LEVEL / REDIRECT TO OBJECT LEVEL / ACKNOWLEDGE AND INTEGRATE]
```

Rules:
- Some meta-claims genuinely change the analysis — "you're measuring the wrong thing" can be transformative
- Other meta-claims are evasion tactics — "this is too complex to discuss" often means "I don't want to discuss it"
- The test: does accepting the meta-claim lead to a better analysis or no analysis at all?
- If the meta-claim blocks all analysis without offering an alternative, it's likely unproductive

---

## Step 6: Verdict

```
META-CLAIM VERDICT:
- Claim: [the meta-claim]
- Level: [what level it operates at]
- Self-consistent: [YES / NO]
- Consistently applied: [YES / NO]
- Impact on object-level: [SIGNIFICANT / MODERATE / MINIMAL / NONE]

OVERALL ASSESSMENT: [VALID AND IMPORTANT / VALID BUT MINOR / QUESTIONABLE / INVALID / EVASIVE]

RECOMMENDATION:
- [How to handle this meta-claim in the ongoing discussion]
- [Whether to adjust the object-level analysis based on it]
```

---

## Integration

Use with:
- `/fctl` -> If the meta-claim contains factual assertions, verify them
- `/ncl` -> If the meta-claim is normative ("you should argue differently"), analyze the "should"
- `/rlcl` -> If the meta-claim is about how claims relate, analyze the relationship
- `/icl` -> If the meta-claim implies intentions ("they're arguing in bad faith"), analyze the intentional claim
