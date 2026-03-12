---
name: "orcs - Orchestrator Skill Design"
description: Guides the design of routing and orchestrating skills that classify input, map it to the right target skill, and handle edge cases and ambiguous inputs.
output:
  format: "prose"
---

# Orchestrator Skill Design

**Input**: $ARGUMENTS

---

## Step 1: Define the Orchestrator's Domain

An orchestrator routes — it doesn't analyze. Define what space it covers.

```
ORCHESTRATOR NAME: [abbreviation]
DOMAIN: [what kind of inputs it handles]
ROUTES TO: [how many target skills]
GOAL: [what the user gets — the right skill for their input]
```

Rule: An orchestrator should never produce its own analysis. Its only job is dispatching to the right skill.

---

## Step 2: Design the Classification Scheme

Define how inputs get categorized.

```
CLASSIFICATION SCHEME:

| Class | Signal Words / Patterns | Target Skill | Example Input |
|-------|------------------------|-------------|---------------|
| [class 1] | [what to look for] | /[skill] | [example] |
| [class 2] | [what to look for] | /[skill] | [example] |
| [class 3] | [what to look for] | /[skill] | [example] |
| [class 4] | [what to look for] | /[skill] | [example] |
| [class 5] | [what to look for] | /[skill] | [example] |
```

Aim for 4-8 classes. Fewer than 4 means the orchestrator is too narrow. More than 8 means it should be split into sub-orchestrators.

---

## Step 3: Design the Routing Logic

Define the decision process from input to dispatch.

```
ROUTING LOGIC:

1. SCAN: Read the input for signal words and patterns
2. CLASSIFY: Match to the strongest class
   - If clear match → route directly
   - If multiple matches → go to Step 4 (ambiguity handling)
   - If no match → go to Step 5 (fallback handling)
3. CONFIRM: State the classification and reasoning in one line
4. DISPATCH: → INVOKE: /[target_skill] [input]
```

Rule: Routing should take one pass. If classification requires deep analysis, the orchestrator scope is wrong.

---

## Step 4: Handle Ambiguous Inputs

Some inputs match multiple classes. Design the tiebreaker.

```
AMBIGUITY HANDLING:

STRATEGY: [pick one]
- PRIORITY: Use a fixed priority order (class 1 > class 2 > class 3)
- DECOMPOSE: Split the input and route parts separately
- ASK: Present the top 2 matches and let the user choose
- DEFAULT: Route to the most general skill

PRIORITY ORDER (if using PRIORITY):
1. [highest priority class] — because [reason]
2. [next class]
3. [next class]
...
```

---

## Step 5: Handle No-Match Inputs

Every input must go somewhere. No input should fall through.

```
FALLBACK HANDLING:

1. Check if input is malformed → ask user to rephrase
2. Check if input belongs to a different orchestrator → redirect
3. If genuinely novel → route to the most exploratory/general skill
4. Never return "I don't know what to do with this"

DEFAULT ROUTE: /[fallback skill]
REASON: [why this is the safest default]
```

---

## Step 6: Test With Diverse Inputs

Verify routing accuracy across input types.

```
ROUTING TEST:

| # | Input | Expected Class | Routed To | Correct? |
|---|-------|---------------|-----------|----------|
| 1 | [clear input for class 1] | [class 1] | /[skill] | [yes/no] |
| 2 | [clear input for class 2] | [class 2] | /[skill] | [yes/no] |
| 3 | [ambiguous input] | [class ?] | /[skill] | [yes/no] |
| 4 | [edge case input] | [class ?] | /[skill] | [yes/no] |
| 5 | [input from outside domain] | [fallback] | /[skill] | [yes/no] |
```

If accuracy is below 80%, revise the classification scheme.

---

## Step 7: Write the Orchestrator

Produce the complete SKILL.md.

```
ORCHESTRATOR FILE:

---
name: "[abbreviation] - [Full Name]"
description: [one sentence — routes X type of input to the right skill]
---

# [Full Name]

**Input**: $ARGUMENTS

## Classify
[classification table]

## Route
[routing logic with INVOKE statements]

## Integration
[list of all target skills]
```

---

## Integration

Use with:
- `/chns` -> Ensure target skills have compatible input contracts
- `/injc` -> Add injectable checks before routing (e.g., input validation)
- `/stnl` -> Verify each target skill works standalone after dispatch
