---
name: root_cause_5_whys
description: "Developed by Sakichi Toyoda for Toyota. When a problem occurs,"
---

# Root Cause Analysis (5 Whys)

## Overview
Developed by Sakichi Toyoda for Toyota. When a problem occurs,
ask "Why?" repeatedly (typically 5 times) to drill past symptoms
to root causes. Fixing root causes prevents recurrence.

The number 5 is a guideline, not a rule. Sometimes 3 is enough,
sometimes 7 is needed.

## Goal
Find the root cause of a problem by repeatedly asking "Why?"
until you reach a cause that, if fixed, prevents recurrence.
Simple to follow; judgment needed to identify true root.

## Steps

### Step 1: State the Problem
Describe the problem clearly and specifically.
Focus on what happened, not why (yet).

Good: "The website was down for 2 hours on Tuesday"
Bad: "The website keeps having problems"

**Output**: Problem statement

### Step 2: Ask Why #1
Ask: "Why did [problem] happen?"
Answer with the immediate cause.
This is usually a symptom or proximate cause, not root.

**Output**: First why

### Step 3: Ask Why #2
Ask: "Why did [first cause] happen?"
Go one level deeper.

**Output**: Second why

### Step 4: Ask Why #3
Ask: "Why did [second cause] happen?"
Continue drilling down.

**Output**: Third why

### Step 5: Ask Why #4
Ask: "Why did [third cause] happen?"
Getting closer to root.

**Output**: Fourth why

### Step 6: Ask Why #5
Ask: "Why did [fourth cause] happen?"
Often this reaches root cause, but may need more.

**Output**: Fifth why

### Step 7: Check for Root Cause
Ask: "Is this the root cause?"

Root cause test:
- If we fix this, will the problem stop recurring?
- Is there a deeper "why" that makes sense?
- Is this something we can actually address?

If not root yet, continue asking why.
If circular, you've gone too far.

**Output**: Root cause determination

### Step 8: Verify the Chain
Read the chain forward (cause → effect):
"Because of [root cause], [cause 4] happened.
 Because of [cause 4], [cause 3] happened.
 ...
 Because of [cause 1], [problem] happened."

Does it make sense? Each step should logically cause the next.

**Output**: Verified causal chain

### Step 9: Identify Corrective Action
Ask: "What action would eliminate or mitigate the root cause?"

Good corrective actions:
- Address root, not symptoms
- Are specific and actionable
- Prevent recurrence
- Are within your control

**Output**: Corrective action

### Step 10: Check for Multiple Roots
Some problems have multiple root causes.
Go back to step 2 and ask "Why else?"
Explore parallel branches.

**Output**: Additional root causes (if any)


## When to Use
- Problem keeps recurring
- Symptoms are clear but cause is not
- After an incident or failure
- When initial fix didn't work
- To prevent future occurrences

## Verification
- Problem was stated specifically
- Each 'why' answer is a direct cause of the previous
- Chain reads sensibly forward (cause → effect)
- Root cause is actionable (can be addressed)
- Root cause is systemic (not 'person made mistake')
- Corrective action addresses root, not symptoms
- Multiple branches explored if applicable

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.