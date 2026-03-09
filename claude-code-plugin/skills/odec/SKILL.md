---
name: "odec - Decision Output"
description: Generates structured decision recommendations. Takes a decision context and produces a clear recommendation with rationale, confidence level, and conditions for revision.
---

# Decision Output

**Input**: $ARGUMENTS

---

## Step 1: State the Decision

Frame the decision clearly and precisely.

```
DECISION: [the specific choice to be made]
DECISION OWNER: [who makes this decision]
DEADLINE: [when the decision must be made, if applicable]
REVERSIBILITY: [easily reversible / costly to reverse / irreversible]
```

Rules:
- The decision must be actionable — it should result in a concrete choice
- If the decision is vague, sharpen it before proceeding
- State what is NOT being decided (scope boundaries)

---

## Step 2: Present Options

List all viable options with their pros and cons.

```
OPTION A: [name / description]
  PROS:
  - [advantage 1]
  - [advantage 2]
  CONS:
  - [disadvantage 1]
  - [disadvantage 2]
  COST: [resource cost — time, money, effort]
  RISK: [what could go wrong]

OPTION B: [name / description]
  PROS: ...
  CONS: ...
  COST: ...
  RISK: ...

...
```

Rules:
- Include at least 2 options; 3-5 is ideal
- Always include "do nothing" or "status quo" if it is a real option
- Pros and cons should be specific, not generic
- Distinguish between certain costs and uncertain risks

---

## Step 3: Present the Recommendation

State the recommended option clearly.

```
RECOMMENDATION: [Option X]
```

Rules:
- Commit to one option — do not hedge with "it depends"
- If genuinely unable to recommend one option, state what information would break the tie

---

## Step 4: State the Rationale

Explain why this option is recommended over the alternatives.

```
RATIONALE:
1. [primary reason — the strongest argument for this option]
2. [secondary reason]
3. [what this option avoids that others don't]

WHY NOT [Option B]: [the key reason it was rejected]
WHY NOT [Option C]: [the key reason it was rejected]
```

Rules:
- The rationale should be traceable to the pros/cons analysis
- Address the strongest argument against the recommendation
- Be explicit about the trade-offs being accepted

---

## Step 5: State Confidence Level

Quantify certainty in the recommendation.

```
CONFIDENCE: [HIGH / MEDIUM / LOW]

HIGH: Strong evidence, clear winner, low risk of being wrong
MEDIUM: Good evidence but some uncertainty; recommendation could change with new data
LOW: Limited evidence, close call; recommendation is a best guess

KEY UNCERTAINTY: [the single biggest unknown that affects this decision]
```

---

## Step 6: State Reversal Conditions

Define when the recommendation should change.

```
RECONSIDER IF:
- [condition 1 — a new fact or change that would flip the recommendation]
- [condition 2]
- [condition 3]

REVIEW BY: [date or trigger for re-evaluating this decision]
```

Rules:
- Reversal conditions should be specific and observable
- Include both external changes (market, requirements) and internal signals (metrics, feedback)

---

## Step 7: State Next Steps

Define what happens immediately after the decision is made.

```
NEXT STEPS:
1. [first action to implement the decision]
2. [second action]
3. [who to communicate the decision to]
4. [what to monitor after implementation]
```

---

## Integration

Use with:
- `/omtx` -> Build a comparison matrix before generating the decision
- `/cba` -> Add cost-benefit analysis to the options
- `/dcp` -> Apply a full decision-making process upstream
- `/onar` -> Present the decision in narrative form for stakeholders
