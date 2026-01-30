---
name: "ve - Value Elicitation"
description: "Value elicitation discovers what someone ACTUALLY values - their intrinsic goals."
---

# Value Elicitation

## Overview
Value elicitation discovers what someone ACTUALLY values - their intrinsic goals.

Most people state instrumental goals ("I want to start a business").
Value elicitation traces to intrinsic goals ("I want freedom" or "I want security").

Different people have different intrinsic goals.
The same stated goal can serve different intrinsic goals for different people.
People often have MULTIPLE intrinsic goals that may CONFLICT.

## Steps

### Step 1: State the goal
What is the stated goal?
Write it down exactly as expressed.

**Output**: stated_goal

### Step 2: Ask what's important
Ask: "What's important to you about [stated_goal]?"

Listen for the answer. It may be:
- Another instrumental goal → continue
- An intrinsic goal → check with step 4
- Confusion → rephrase question

**Output**: first_answer

### Step 3: Continue tracing
Take the answer from step 2.
Ask: "What's important to you about [answer]?"

Repeat until you detect circularity.

**Output**: chain_of_answers

### Step 4: Detect circularity (terminus)
Circularity is reached when the answer refers back to itself:

Circularity indicators:
- "Because that's what I value"
- "Because it's [X]" (tautology)
- "I just do"
- "That's the point"
- "That's what matters"
- Can't articulate further reason

If circularity detected: This is an intrinsic goal.
If not: Continue tracing (step 3).

**Output**: intrinsic_goal_1

### Step 5: Check for additional intrinsic goals
Ask: "Is there anything else important about [original_stated_goal]?"

If yes: Go back to step 2 with this new answer.
If no: Proceed to step 6.

People often have multiple intrinsic goals.
Don't stop at the first one.

**Output**: additional_answers (if any)

### Step 6: Trace additional chains
For each additional answer from step 5:
- Repeat steps 2-4
- Find additional intrinsic goals

Continue until person says "no" to step 5.

**Output**: all_intrinsic_goals

### Step 7: Check for conflicts
If multiple intrinsic goals found:
Ask: "Do these ever conflict for you?"

Common conflicts:
- Freedom vs Security
- Achievement vs Peace
- Connection vs Independence
- Meaning vs Pleasure

If conflicts exist, note them.
The person will need to prioritize or balance.

**Output**: conflicts (if any)

### Step 8: Document the value map
Create a value map showing:
- Stated goal
- All intrinsic goals found
- The chains from stated goal to each intrinsic goal
- Any conflicts between intrinsic goals

**Output**: value_map


## When to Use
- At the start of any goal-setting process
- When someone states a goal but the "why" is unclear
- When you suspect the stated goal is instrumental, not intrinsic
- When planning seems disconnected from what matters
- When verifying that actions serve actual values

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.