---
name: "grf - Goal Refinement"
description: "Transform vague or incomplete goals into SMART goals with explicit clarification vs substitution distinction"
---

# Goal Refinement

## Overview
Transform vague or incomplete goals into SMART goals.

**CRITICAL DISTINCTION**: This procedure distinguishes between:
- **CLARIFICATION**: Making the SAME goal clearer (preserves intent)
- **SUBSTITUTION**: Proposing a DIFFERENT goal that's achievable (changes intent)

Substitution requires explicit user consent. Default is to clarify, not substitute.

---

## Step 0: Clarification vs Substitution Check (NEW - Run First)

Before refining, determine the refinement type:

### Clarification Indicators (Same Goal, Clearer)
- Adding specificity to vague terms
- Setting concrete metrics for abstract outcomes
- Defining timeline for open-ended goal
- Breaking down into sub-goals that together = original goal

### Substitution Indicators (Different Goal)
- Changing the core outcome
- "Underlying need" analysis that replaces stated goal
- Making the goal "achievable" by reducing ambition
- Pivoting to related but different goal

### Classification

```
REFINEMENT TYPE CHECK
=====================
Original goal: [user's stated goal]
Proposed refinement: [what we're considering]

Is the refined version the SAME goal, just clearer?
[ ] YES → CLARIFICATION (proceed without consent)
[ ] NO → SUBSTITUTION (requires consent)

Substitution test:
If user achieved refined goal but NOT original goal, would they feel:
- "That's what I meant" → CLARIFICATION
- "That's not what I asked for" → SUBSTITUTION
```

### If Substitution Detected

```
SUBSTITUTION CONSENT REQUEST
============================
Your stated goal: "[original goal]"

I notice that achieving this exactly as stated may not be possible because:
[reason]

I could help you with a related goal instead:
"[proposed substitute goal]"

This is a DIFFERENT goal that:
- CAN achieve: [what it accomplishes]
- CANNOT achieve: [what it doesn't accomplish vs original]

Options:
1. [ ] Accept substitute goal
2. [ ] Explore why original goal is impossible
3. [ ] Find a different substitute
4. [ ] Attempt original goal anyway (may fail)

Which would you prefer?
```

### Honest Rejection Option

Some goals are genuinely impossible. If so:

```
HONEST REJECTION
================
Your goal: "[goal]"

This goal cannot be achieved because:
[specific, factual reason]

I will NOT substitute a different goal without your consent.

Options:
1. [ ] Accept impossibility
2. [ ] Challenge my assessment (show me what I'm missing)
3. [ ] Explore substitute goals
4. [ ] Reframe the goal differently
```

---

## Steps

### Step 1: Parse original goal
Extract and identify components from the original goal statement:
1. Identify the core action or outcome desired
2. Extract any explicit constraints mentioned
3. Note any metrics or success indicators
4. Identify time references or deadlines
5. List any stakeholders mentioned
6. Flag ambiguous terms or undefined concepts

### Step 2: Assess SMART criteria gaps
Evaluate the goal against each SMART criterion:

Specific:
- Is the outcome clearly defined?
- Is the scope bounded?
- Are key terms defined?

Measurable:
- Are there quantifiable metrics?
- How will completion be verified?
- What evidence demonstrates success?

Achievable:
- Is this realistic with available resources?
- Are there known blockers?
- Has similar been done before?

Relevant:
- Why does this matter?
- How does it connect to larger objectives?
- Is the timing right?

Time-bound:
- Is there a deadline?
- Are there intermediate milestones?
- Is the timeline realistic?

### Step 3: Generate clarifying questions
For each critical gap and ambiguity, formulate questions:
1. Questions that would make the goal more specific
2. Questions about how to measure success
3. Questions about feasibility and resources
4. Questions about relevance and priority
5. Questions about timeline and milestones

Prioritize questions by:
- Impact on goal clarity
- Likelihood of changing the approach
- Risk of proceeding without answer

### Step 4: Make reasonable assumptions
For gaps that can be reasonably filled:
1. Identify what assumption would be most reasonable
2. State the assumption explicitly
3. Note confidence level in assumption
4. Identify what would invalidate the assumption

Only make assumptions when:
- A reasonable default exists
- The assumption can be validated later
- Proceeding without it would block progress

### Step 5: Identify dependencies
Analyze the goal for dependencies:
1. Prerequisites: What must exist before starting?
2. Resources: What is needed for execution?
3. External dependencies: What do we not control?
4. Temporal dependencies: What sequence is required?
5. Knowledge dependencies: What must we know first?

### Step 6: Formulate refined goal
Construct the refined SMART goal statement:
1. Start with specific action verb
2. Include measurable outcome
3. Reference timeline or deadline
4. Ensure scope is bounded
5. Make success criteria explicit

Format: "[Action] [specific outcome] by [deadline], measured by [metrics],
resulting in [value/relevance]"

### Step 7: Define success criteria
Create explicit, verifiable success criteria:
1. Primary criteria (must be met for goal completion)
2. Secondary criteria (should be met for quality)
3. Stretch criteria (exceeds expectations)

Each criterion should be:
- Observable or measurable
- Unambiguous in evaluation
- Connected to the goal outcome


## When to Use
- User provides a vague or ambiguous goal statement
- Goal fails SMART assessment (missing any of the five criteria)
- Need to clarify success criteria before strategy selection
- Goal contains undefined terms or scope boundaries
- Multiple interpretations of the goal are possible
- Dependencies or prerequisites are unclear
- Time horizon or deadline is not specified
- Measurable outcomes are not defined
- Goal seems too large or complex without decomposition hints

## Verification
- [ ] Refinement type determined (CLARIFICATION vs SUBSTITUTION)
- [ ] If SUBSTITUTION: user consent obtained
- [ ] Refined goal addresses all five SMART criteria explicitly
- [ ] Success criteria are measurable and unambiguous
- [ ] Assumptions are stated explicitly with confidence levels
- [ ] Critical clarifying questions are identified and prioritized
- [ ] Dependencies are catalogued and blocking items flagged
- [ ] Original intent is preserved (refinement, not replacement)
- [ ] If honest rejection: reason is factual and specific

### Verification Questions for Clarification vs Substitution

| Question | Clarification | Substitution |
|----------|---------------|--------------|
| Would user recognize this as "their goal"? | YES | NO/UNCERTAIN |
| Does achieving this achieve the original? | YES | ONLY PARTIALLY |
| Did we change what's being achieved? | NO | YES |
| Did we just add specificity? | YES | NO |
| Would user feel redirected? | NO | YES |

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.