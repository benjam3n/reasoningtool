---
name: "mocl - Modal Claim Analysis"
description: Evaluate "could/would/might" claims. Identify the type of possibility, check constraints, and assess distance from actuality.
output:
  format: "prose"
---

# Modal Claim Analysis

**Input**: $ARGUMENTS

---

## Step 1: State the Modal Claim

Extract and classify the possibility claim.

```
ORIGINAL STATEMENT: [as stated]
MODAL CLAIM: [rewritten as a clear possibility statement]
MODAL OPERATOR: [could / would / might / must / can't / impossible]
POLARITY: [positive possibility / negative possibility (impossibility)]
```

Rules:
- "Could" implies possibility; "would" implies conditional certainty; "might" implies uncertainty
- "Can't" and "impossible" are strong claims that require strong evidence
- If the claim uses vague language, choose the most charitable interpretation
- Distinguish between "X could happen" (possibility) and "X would happen" (prediction)

---

## Step 2: Identify the Type of Possibility

Not all "coulds" are equal. Classify what kind of possibility is being claimed.

```
POSSIBILITY TYPE:
- [ ] Logical possibility: Not self-contradictory (weakest — almost everything is logically possible)
- [ ] Physical possibility: Compatible with laws of nature
- [ ] Technical possibility: Achievable with known technology/methods
- [ ] Practical possibility: Achievable given actual resources and constraints
- [ ] Political possibility: Achievable given social/organizational realities
- [ ] Likely possibility: Not just possible but plausible or probable

CLAIMED TYPE: [which type the speaker seems to mean]
ACTUAL TYPE: [which type the evidence supports]
```

Rules:
- Most disagreements about "could" are actually about which type of possibility is meant
- "We could colonize Mars" — logically? Yes. Technically? Maybe. Practically? Not yet.
- The further right on the list, the stronger and more useful the possibility claim
- If claimed type and actual type differ, that gap IS the analysis

---

## Step 3: Check Constraints

Identify what prevents the possibility from being actual.

```
CONSTRAINT ANALYSIS:
HARD CONSTRAINTS (cannot be overcome):
- [Constraint]: [Why it's a hard limit]

SOFT CONSTRAINTS (could be overcome with effort/resources):
- [Constraint]: [What would be needed to overcome it]
- Cost to overcome: [estimate]

ABSENT CONSTRAINTS (often assumed but not real):
- [Assumed constraint]: [Why it's not actually a barrier]
```

Rules:
- Hard constraints are physical laws, logical impossibilities, or irreversible facts
- Soft constraints are resource limits, political obstacles, skill gaps — these can change
- Many "impossibilities" are actually soft constraints disguised as hard ones
- Many "possibilities" ignore real hard constraints — check both directions

---

## Step 4: Identify Enabling Conditions

What would need to be true for the possibility to become actual?

```
ENABLING CONDITIONS:
REQUIRED (must be present):
1. [Condition]: Currently [MET / UNMET]
2. [Condition]: Currently [MET / UNMET]
3. [Condition]: Currently [MET / UNMET]

HELPFUL (increase likelihood):
1. [Condition]: Currently [PRESENT / ABSENT]
2. [Condition]: Currently [PRESENT / ABSENT]

TRIGGER (what would set it in motion):
- [Event or action that would initiate the transition from possible to actual]
```

Rules:
- If all required conditions are met, the possibility is "ready" — it just needs a trigger
- If key required conditions are unmet, the possibility is remote regardless of other factors
- Count the unmet conditions — more unmet = more distant from actuality
- Check if enabling conditions are trending toward being met or away

---

## Step 5: Assess Distance from Actuality

How far is this possibility from actually happening?

```
ACTUALITY DISTANCE:
- Current status: [ACTUAL / NEAR-ACTUAL / FEASIBLE / DISTANT / EXTREMELY REMOTE]
- Barriers remaining: [count and nature]
- Path from here to actual: [brief description of what would need to happen]
- Estimated probability of becoming actual: [percentage or range]

ASSESSMENT:
- Is the modal claim warranted? [YES / PARTIALLY / NO]
- More accurate phrasing: [how the claim should actually be stated]
- What the claim gets right: [the grain of truth]
- What the claim gets wrong: [the overreach or underreach]
```

Rules:
- ACTUAL = already happening
- NEAR-ACTUAL = all conditions met, just needs a trigger
- FEASIBLE = most conditions met, remaining ones are achievable
- DISTANT = several hard conditions unmet
- EXTREMELY REMOTE = logically possible but practically irrelevant
- Most "could" claims are either less possible or more possible than they sound

---

## Integration

Use with:
- `/pcl` -> If the modal claim implies a prediction, evaluate the prediction
- `/ncl` -> If the claim is "we could, therefore we should," analyze the normative leap
- `/cscl` -> If the claim involves causal possibility, test the causal mechanism
- `/fctl` -> Verify factual claims about constraints and enabling conditions
