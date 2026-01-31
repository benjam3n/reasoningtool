---
name: qg
description: "When you don't know something, the right question is worth more than hours of speculation."
---

# Question Generation

**Input**: $ARGUMENTS

---

## Overview

When you don't know something, the right question is worth more than hours of speculation. This procedure provides a taxonomy of question types, each designed to resolve a specific kind of uncertainty.

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/qg 4x [input]").

| Depth | Min Questions Generated | Min Question Types | Min Depth Levels | Min Priority Rankings |
|-------|-------------------------|--------------------|------------------|-----------------------|
| 1x    | 5                       | 2                  | 2                | 3                     |
| 2x    | 10                      | 3                  | 3                | 5                     |
| 4x    | 15                      | 5                  | 4                | 8                     |
| 8x    | 25                      | 7                  | 5                | 12                    |
| 16x   | 40                      | 9                  | 6                | 18                    |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## Steps

### Step 1: Identify the Uncertainty
What don't you know? Classify the type:

| Uncertainty Type | Description | Example |
|-----------------|-------------|---------|
| Factual | Don't know what's true | "How many users do we have?" |
| Definitional | Don't know what something means | "What counts as 'active'?" |
| Causal | Don't know why something happens | "Why do users churn?" |
| Preferential | Don't know what someone wants | "Does the client prefer speed or quality?" |
| Conditional | Don't know what would happen if | "What if we raised prices 20%?" |
| Threshold | Don't know where the line is | "How much latency is too much?" |
| Priority | Don't know what matters most | "Which feature should we build first?" |
| Scope | Don't know what's included/excluded | "Does this apply to enterprise clients?" |
| Contradiction | Two things seem true but can't both be | "Users say they want X but behavior shows Y" |

### Step 2: Select Question Type
Each uncertainty type has optimal question formats:

**Factual → Direct questions:**
- "What is [specific fact]?"
- "How many/much [quantity]?"
- "When did [event] happen?"

**Definitional → Boundary questions:**
- "What counts as [term]? What doesn't?"
- "Can you give me an example of [term] and a counter-example?"
- "Where is the line between [A] and [B]?"

**Causal → Mechanism questions:**
- "What causes [outcome]?"
- "If we changed [X], what would happen to [Y]?"
- "What's different between cases where [outcome] and cases where not?"

**Preferential → Trade-off questions:**
- "If you had to choose between [A] and [B], which?"
- "How important is [X] relative to [Y]?"
- "What would you give up to get [Z]?"

**Conditional → Scenario questions:**
- "What would happen if [condition]?"
- "Under what conditions would [outcome] occur?"
- "If [X] changed, would you still want [Y]?"

**Threshold → Quantification questions:**
- "How much [X] is too much/too little?"
- "At what point would you [action]?"
- "What's the minimum acceptable level of [quality]?"

**Priority → Forced ranking questions:**
- "If you could only have one, which?"
- "Rank these from most to least important"
- "What would you cut first if you had to?"

**Scope → Inclusion questions:**
- "Does this apply to [edge case]?"
- "Is [X] in scope or out of scope?"
- "What's the boundary of this?"

**Contradiction → Reconciliation questions:**
- "You said [A] but also [B] — help me understand how both are true"
- "What am I missing that would make these consistent?"
- "Under what conditions is [A] true and under what conditions is [B]?"

### Step 3: Refine the Question
Before asking, improve the question:

**Quality checklist:**
- [ ] Specific (not "how do you feel about X?" but "would you choose X over Y?")
- [ ] Answerable (the person CAN answer this)
- [ ] Actionable (the answer will change what you do)
- [ ] Unbiased (doesn't lead toward a particular answer)
- [ ] Single (asks one thing, not two disguised as one)

**Common question failures:**
| Failure | Example | Fix |
|---------|---------|-----|
| Too vague | "What do you think?" | Specify what dimension |
| Leading | "Don't you agree that...?" | Remove the suggested answer |
| Compound | "Do you like A and B?" | Split into two questions |
| Unanswerable | "What will happen in 5 years?" | Ask "what would need to be true for X?" |
| Unactionable | "Is the sky blue?" | Only ask if the answer changes behavior |

### Step 4: Sequence Questions
If multiple questions are needed:

1. Start with factual/definitional (establish shared understanding)
2. Then causal/conditional (understand mechanisms)
3. Then preferential/priority (understand values)
4. Then threshold/scope (pin down boundaries)
5. End with contradiction resolution (reconcile remaining tensions)

### Step 5: Generate Question Set
For the input's uncertainty:

```
QUESTION SET:
Primary uncertainty: [type]

Questions (in order):
1. [question] — type: [type] — resolves: [what uncertainty]
2. [question] — type: [type] — resolves: [what uncertainty]
3. [question] — type: [type] — resolves: [what uncertainty]

If answer to Q1 is [A]: skip Q2, go to Q3
If answer to Q1 is [B]: ask Q2 next

After all questions answered:
- Uncertainty resolved: [what we now know]
- Remaining uncertainty: [what we still don't know]
```

## When to Use
- Model uncertainty is high
- User preferences are unclear
- Assumptions need validation
- Contradictions need resolution
- → INVOKE: /qag (question and answer generation) for Q&A pairs
- → INVOKE: /bes (binary elimination search) for efficient narrowing

## Verification
- [ ] Uncertainty type identified correctly
- [ ] Question type matches uncertainty type
- [ ] Questions are specific, answerable, actionable, unbiased, single
- [ ] Questions sequenced logically
- [ ] Branching logic defined (what to ask based on answers)
