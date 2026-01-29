---
name: inference_space_search
description: "Information implies other information. But not all inferences are equal:"
---

# Inference Space Search

## Overview
Information implies other information. But not all inferences are equal:
- Some are logically valid, some aren't
- Some have true premises, some don't
- Some are useful, some are trivial

Generate the inference space, then filter by quality criteria.

## Goal
From given information, generate all possible inferences,
then search for those that are valid, sound, and useful.

## Steps

### Step 1: List Premises
Explicitly state all known facts/assumptions being used.
Number them for reference.
Note which are certain vs assumed.

**Output**: Numbered premise list

### Step 2: Generate Deductive Inferences
What follows necessarily from the premises?

Apply:
- Modus ponens (If A then B; A; therefore B)
- Modus tollens (If A then B; not B; therefore not A)
- Syllogisms
- Instantiation of universals

**Output**: Deductive inferences

### Step 3: Generate Inductive Inferences
What patterns can be generalized?
What trends can be extrapolated?

Look for:
- Repeated observations
- Statistical patterns
- Historical trends

**Output**: Inductive inferences

### Step 4: Generate Abductive Inferences
What would explain the premises?
What causes would produce these effects?

For each surprising/unexplained fact:
- What could cause it?
- Which cause is simplest?
- Which is most likely given background knowledge?

**Output**: Abductive inferences

### Step 5: Generate Analogical Inferences
What similar cases exist?
What can be transferred from them?

For each premise about X:
- What is similar to X?
- Does the similar thing have relevant properties?
- Would those properties transfer?

**Output**: Analogical inferences

### Step 6: Check Validity
For each inference, ask:
"If the premises were true, would the conclusion have to be true?"

Score:
- 10: Necessarily follows (deductive, valid)
- 7-9: Highly probable (strong inductive)
- 4-6: Plausible (weak inductive, abductive)
- 1-3: Speculative (analogical, weak)

**Output**: Validity scores

### Step 7: Check Soundness
For each inference, ask:
"Are all the premises actually true?"

Check each premise used:
- Evidence for premise
- Confidence level
- Alternative interpretations

**Output**: Soundness assessment

### Step 8: Check Usefulness
For each valid and sound inference, ask:
- Is it non-trivial? (tells us something new)
- Is it relevant? (matters for our purposes)
- Is it actionable? (suggests what to do)

**Output**: Usefulness scores

### Step 9: Rank and Select
Combine scores: Validity × Soundness × Usefulness
Rank inferences.
Select top inferences for use.

**Output**: Ranked inferences


## When to Use
- Drawing conclusions from evidence
- Reasoning about implications
- Finding hidden connections
- Building arguments
- Understanding consequences

## Verification
- Premises are explicitly stated
- Multiple inference types were attempted
- Validity was assessed for each
- Soundness was assessed for each
- Usefulness was considered
- Top inferences are actionable

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.