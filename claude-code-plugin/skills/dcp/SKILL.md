---
name: dcp
description: Create a mechanical, step-by-step decision procedure for a recurring decision type. Like a flowchart anyone can follow without expertise. Chains dimension discovery, enumeration, assumption extraction, steps generation, failure anticipation, and validation.
---

# Decision Procedure

**Input**: $ARGUMENTS

---

## Purpose

Some decisions are made repeatedly by many people, and most people navigate them poorly because they lack expertise. This skill creates a **mechanical procedure** -- a flowchart or decision tree that takes someone from "I have this decision to make" to "here is my answer" without requiring them to understand the underlying domain.

**What this produces**: A step-by-step procedure (like a medical diagnostic flowchart or troubleshooting guide) that anyone can follow to make a specific type of decision.

**This is a compound skill** -- it chains 6 skills in sequence.

---

## The Chain

```
Step 1: /dimension_discovery       -- What dimensions matter for this decision?
Step 2: /space_enumeration         -- What are all the options within each dimension?
Step 3: /assumption_extraction     -- What assumptions does the standard approach make?
Step 4: /steps_generation          -- Create the step-by-step procedure
Step 5: /failure_anticipation      -- What goes wrong when following this procedure?
Step 6: /procedure_validation      -- Is every step executable without interpretation?
```

---

## Execution Procedure

### Step 1: Discover Decision Dimensions

-> INVOKE: /dimension_discovery $ARGUMENTS

Map all the dimensions that matter for this decision:
- What factors determine the right choice?
- What information do you need before deciding?
- What constraints narrow the options?
- What are the axes of variation?

**Target**: 8-15 dimensions that collectively determine the right answer.

**Output**: Named dimensions with descriptions and why each matters.

---

### Step 2: Enumerate Options per Dimension

-> INVOKE: /space_enumeration [dimensions from Step 1]

For each dimension, enumerate the possible values:
- What states can each dimension be in?
- What are the common cases vs edge cases?
- Are there dimensions that interact (if X=A, then Y must be B)?

**Output**: Complete option space organized by dimension.

---

### Step 3: Surface Hidden Assumptions

-> INVOKE: /assumption_extraction [standard approach to this decision]

What does the conventional wisdom about this decision assume?
- What do experts know implicitly that novices miss?
- What assumptions could lead someone to the wrong answer?
- Where do people commonly go wrong?

**Output**: Assumptions that the procedure needs to address or protect against.

---

### Step 4: Generate the Procedure

-> INVOKE: /steps_generation [dimensions, options, assumptions from Steps 1-3]

Create the actual step-by-step procedure:

**Format requirements**:
- Written for someone with NO domain expertise
- Every step is a concrete action or observation (not "consider" or "think about")
- Decision points are binary or small multiple choice ("Is X true? If yes, go to Step N. If no, go to Step M.")
- No jargon without definition
- Include "what you should see" at each step so the user knows they're on track

**Structure**:
```
STEP 0: What type of [decision] is this?
  [Classification table pointing to sections]

SECTION A: [Type 1]
  Step A1: [concrete action]
  Step A2: [observation or check]
  Step A3: [decision point] -> if yes: A4, if no: A5
  ...

SECTION B: [Type 2]
  ...

QUICK REFERENCE: [Summary cards]
```

**Output**: The procedure document.

---

### Step 5: Anticipate Failures

-> INVOKE: /failure_anticipation [procedure from Step 4]

How can following this procedure go wrong?
- Where might someone misidentify their situation?
- Where might the procedure give the wrong answer?
- What edge cases aren't covered?
- What are the most common mistakes?

For each failure mode:
- How to recognize you're in it
- What to do instead

**Output**: Failure modes added to the procedure as warnings and overrides.

---

### Step 6: Validate Executability

-> INVOKE: /procedure_validation [complete procedure from Steps 4-5]

Check every step:
- Can someone with NO expertise execute this step?
- Is there any ambiguity in what to do?
- Are all decision points clear (not "use your judgment")?
- Does every path lead to a concrete output?
- Are there dead ends or loops?

Fix any issues found.

-> COMPLETE

---

## Output Standards

- The procedure must be followable by someone who has ZERO understanding of the domain
- Plain language only -- define any technical terms inline
- Every decision point must be binary or explicit multiple choice
- Include worked examples showing the procedure applied to real cases
- Include a "Common Mistakes" section
- Include a "When to Override This Procedure" section (when to seek expert help)
- Validation status: "This procedure has not been validated by domain experts"

---

## Output Format

```
[DECISION TYPE] PROCEDURE
=========================

STEP 0: What type of [decision] is this?
[Classification table]

SECTION [A-Z]: [Each type]
[Numbered steps with decision points]

QUICK REFERENCE CARDS
[Summary of key formulas/rules/tables]

COMMON MISTAKES
[Numbered list of what goes wrong]

WHEN TO OVERRIDE
[When this procedure isn't enough]

WORKED EXAMPLES
[2-3 examples walking through the procedure]
```

---

## Example Usage

```
/decision_procedure choosing a software architecture
/decision_procedure debugging any software bug
/decision_procedure evaluating a job offer
/decision_procedure choosing a college major
/decision_procedure deciding whether to start a business
```
