---
name: "dcm - Decomposition"
description: "Break complex goals into simpler, manageable sub-goals"
output:
  format: "prose"
---

# Decomposition

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Project breakdown**: You have a large goal or project and need to break it into manageable, assignable pieces with clear dependencies (e.g., "break this project into tasks" or "this is too big — where do I start?").
**Interpretation 2 — Complexity reduction**: You have something conceptually complex — a system, argument, or problem — and need to decompose it into simpler parts you can understand individually (e.g., "I can't wrap my head around this" or "simplify this into parts I can reason about").
**Interpretation 3 — Scope definition**: You're not sure what's actually included in a vague or sprawling goal, and need decomposition to reveal what's really involved and set boundaries (e.g., "what does 'improve the product' actually entail?" or "what am I really committing to here?").

If ambiguous, ask: "I can help with breaking a project into tasks, simplifying something complex into understandable parts, or clarifying what a vague goal actually involves — which fits?"
If clear from context, proceed with the matching interpretation.

## Overview
Break complex goals into simpler, manageable sub-goals

## Steps

### Step 1: Assess decomposition need
Determine if and why decomposition is needed:
- Is goal too big to tackle at once?
- Are there clearly distinct components?
- Would parallel work be beneficial?

### Step 2: Select decomposition strategy
Choose the most appropriate strategy:

**Functional**: Use when goal has distinct functions
- "Build a robot" → locomotion, sensing, control, power

**Temporal**: Use when goal has natural phases
- "Launch product" → research, build, test, launch

**Structural**: Use when goal has physical/logical parts
- "Build house" → foundation, framing, electrical, plumbing

**Stakeholder**: Use when different people need different things
- "Improve satisfaction" → customer needs, employee needs, partner needs

### Step 3: Identify sub-goals
Apply selected strategy to identify sub-goals:
1. List all components/phases/functions
2. Name each as a sub-goal
3. Ensure sub-goals cover the whole goal
4. Check for gaps (is anything missing?)

Sub-goal quality criteria:
- SIMPLER than parent (can be understood independently)
- COMPLETE (together achieve the parent)
- INDEPENDENT (minimal overlap)
- ACTIONABLE (can be worked on)
- MEASURABLE (can track progress)

### Step 4: Check completeness (MECE)
Verify decomposition is Mutually Exclusive, Collectively Exhaustive:

**Mutually Exclusive**: Sub-goals don't overlap
- If two sub-goals could both address the same work, merge or clarify

**Collectively Exhaustive**: Sub-goals cover everything
- If achieving all sub-goals wouldn't achieve parent, something is missing

### Step 5: Identify dependencies
For each pair of sub-goals, determine if:
- A depends on B (B must complete before A starts)
- A and B are independent (can happen in parallel)
- A and B are sequential (must happen in order)

Build dependency graph showing relationships.

### Step 6: Calculate critical path
Find the longest chain of dependent sub-goals:
1. Start from sub-goals with no dependencies
2. Follow dependency chains
3. Find longest path (this is your minimum time)

Critical path determines earliest possible completion.

### Step 7: Check for further decomposition
For each sub-goal, ask:
- Is this sub-goal still too complex?
- Should it be decomposed further?

If yes and within max_depth:
- Recursively apply decomposition to that sub-goal
- Note parent-child relationship


## When to Use
- Goal is too complex to tackle directly
- Need to break down work into phases
- Multiple parallel efforts needed
- Goal has multiple distinct components
- Team needs to divide work
- Complexity assessment shows "Complicated" or "Complex"

## Verification
- Sub-goals are simpler than original goal
- Sub-goals together achieve original goal (collective exhaustiveness)
- Sub-goals don't overlap significantly (mutual exclusiveness)
- Dependencies are identified and make sense
- Critical path is realistic

---

