---
name: br
description: Reasoning from conclusions back to premises. Given a conclusion, what journey led here? Reveals purpose and enables evaluation.
---

# Backward Reasoning

## Overview
Typical reasoning goes "forward" - from premises to conclusions.
This procedure goes "backward" - from conclusions to premises.

Given a conclusion, what came before? What journey led here?

This is harder than forward reasoning but reveals PURPOSE and enables
evaluation of the journey, not just the endpoint.

## Steps

### Step 1: Start with the endpoint
Take the conclusion, statement, or position as given.
Don't question it yet - treat it as the END of a journey.

Ask: "Someone arrived at this. What journey brought them here?"

**Output**: endpoint_statement

### Step 2: Ask "What goal does this serve?"
This conclusion was reached for a REASON.
What is the statement trying to achieve?

Not: What are its logical implications?
But: What PURPOSE does it serve?

**Output**: immediate_purpose

### Step 3: Ask "What problem generated that goal?"
Goals arise from problems/needs.
What problem would make this goal relevant?

Example:
Goal: Establish something certain
Problem: Everything seems doubtable

**Output**: generating_problem

### Step 4: Ask "What context created that problem?"
Problems arise in contexts.
What situation would make this problem salient?

Example:
Problem: Everything seems doubtable
Context: Skepticism is challenging previous beliefs

**Output**: generating_context

### Step 5: Continue tracing until reaching foundational goals
Keep asking backward:
- What led to this context?
- What underlying values are at play?
- What would have to be true/desired for this journey to make sense?

Stop when reaching intrinsic goals (apply intrinsic_goal_termination_gate).

**Output**: full_backward_trace

### Step 6: Construct the forward story
Now reverse the trace to construct the "story":

Chapter 1: Foundational goal/value
Chapter 2: Context that made it relevant
Chapter 3: Problem that arose
Chapter 4: Goal that addressed the problem
...
Final: The conclusion

This is the journey that (hypothetically) led to the endpoint.

**Output**: reconstructed_story

### Step 7: Evaluate the story
Apply story_coherence_gate:
- Does the story cohere?
- Are the goals legitimate?
- Does the conclusion serve the goals?
- Was the journey necessary?
- Is this a valid path?

If coherent: You've understood WHY this conclusion exists.
If not coherent: Either the conclusion is confused OR your reconstruction is wrong.

**Output**: story_evaluation


## When to Use
- Evaluating a philosophical claim or position
- Understanding why someone believes something
- Analyzing a criticism or objection
- Making sense of an unfamiliar argument
- Finding the PURPOSE behind any statement

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.