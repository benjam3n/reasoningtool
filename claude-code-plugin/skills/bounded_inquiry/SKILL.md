---
name: bounded_inquiry
description: "Unbounded inquiry cannot terminate - every answer opens new questions."
---

# Bounded Inquiry

## Overview
Unbounded inquiry cannot terminate - every answer opens new questions.
Bounded inquiry can terminate - closure is possible within scope.

This procedure establishes explicit boundaries for any inquiry,
enabling satisfying closure rather than infinite regress.

## Steps

### Step 1: Establish goal boundary
Before beginning inquiry, explicitly state:
- What are we trying to achieve?
- What would count as success?
- What would this achievement enable?

Be specific. "Understand X" is too vague.
"Be able to predict Y given Z" is specific.

**Output**: goal_statement

### Step 2: Establish scope boundary
Explicitly state:
- What is IN scope for this inquiry?
- What is OUT of scope?
- Where are the edges?

Questions outside scope are acknowledged but deferred:
"That's outside this inquiry. We can address it separately."

**Output**: scope_definition

### Step 3: Establish rules boundary
Explicitly state:
- What counts as valid reasoning here?
- What evidence standards apply?
- What would we accept as an answer?

This prevents moving goalposts and endless "but what if?"

**Output**: rules_definition

### Step 4: Establish stakes boundary
Explicitly state:
- Why does this inquiry matter?
- What depends on its completion?
- What's the cost of not terminating?

If there are no stakes, ask: Why are we doing this?

**Output**: stakes_definition

### Step 5: Conduct inquiry within boundaries
Pursue the inquiry, but check against boundaries:
- Is this question within scope?
- Does this answer serve the goal?
- Does this reasoning follow the rules?
- Are we respecting the stakes?

Out-of-scope questions: Acknowledge and defer.
Goal-irrelevant tangents: Note and return.
Rule-violating moves: Reject or flag.

**Output**: inquiry_process

### Step 6: Recognize termination
Inquiry terminates when:
- Goal is achieved (success)
- Goal is shown unachievable within scope (bounded failure)
- Stakes require decision now (practical closure)
- Remaining questions are out of scope (scoped completion)

State the termination explicitly:
"This inquiry is complete because [criterion]."

**Output**: termination_statement


---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.