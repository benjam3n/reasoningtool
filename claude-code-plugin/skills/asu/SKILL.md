---
name: asu
description: "Plans and beliefs rest on assumptions that are often invisible."
---

# Assumption Surfacing

## Overview
Plans and beliefs rest on assumptions that are often invisible.
These hidden assumptions can cause spectacular failures when violated.
This procedure uses systematic prompts to surface assumptions that
would otherwise remain hidden.

## Goal
Systematically identify hidden assumptions in a plan, belief, or
strategy using structured prompts. Prompts do most of the work;
recognition requires some insight.

## Steps

### Step 1: State the Subject
Clearly describe the plan, belief, or strategy being examined.
Be specific about what it claims or proposes.

**Output**: Subject description

### Step 2: Apply Assumption Prompts
Go through each category of prompts systematically.
For each prompt, ask: "What am I assuming about this?"
Record all assumptions, even obvious ones.

**Output**: Raw assumption list

### Step 3: Consolidate and Deduplicate
Combine similar assumptions.
Remove true duplicates.
Clarify vague assumptions.

**Output**: Clean assumption list

### Step 4: Assess Criticality
For each assumption, ask:
"If this assumption is wrong, does the plan still work?"

Critical = Plan fails if assumption is wrong
Important = Plan degraded if wrong
Minor = Doesn't significantly affect plan

**Output**: Prioritized assumptions

### Step 5: Assess Confidence
For each critical assumption:
- How confident are you it's true?
- What's the evidence?
- Has it been tested?

High risk = Critical + Low confidence

**Output**: Confidence assessment

### Step 6: Plan Validation
For high-risk assumptions (critical + low confidence):
- How could you test this?
- What would prove it wrong?
- What's the cheapest test?

**Output**: Validation plan

### Step 7: Consider Alternatives
For each critical assumption:
"If this is wrong, what's the alternative plan?"
Having contingencies reduces risk.

**Output**: Contingency plans


## When to Use
- Before committing to a plan
- When a strategy seems too good
- When there's unexpected disagreement
- When adapting a solution to new context
- To stress-test thinking

## Verification
- All prompt categories were considered
- Assumptions are clearly stated (not vague)
- Criticality was assessed for each
- High-risk assumptions have validation plans
- Contingencies exist for critical assumptions

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.