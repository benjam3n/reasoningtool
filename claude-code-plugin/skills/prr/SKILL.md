---
name: "prr - Procedure Registry Review"
description: "Review and improve the procedure registry schema using explicit definitions, evidence alignment, and non-regression."
---

# Procedure Registry Review

## Overview
Review and improve the procedure registry schema using explicit definitions, evidence alignment, and non-regression.

## Steps

### Step 1: Read the registry policy
Read the policy section in the registry.

Extract:
- evidence_signals sources and meanings
- terms and definitions
- derived_states definitions and logic
- projections and their conditions

Write a short summary of what the registry claims it measures.

### Step 2: Naming clarity review
For each key and label in policy.derived_states:
- Write the meaning in plain language.
- Write one plausible wrong interpretation a reader could make.
- If the wrong interpretation is likely, propose a rename and update the definition.

Do the same for any domain terms in policy.terms.

### Step 3: Evidence alignment review
For each derived state:
- List the exact evidence fields used by its logic.
- Check that every word in the label is supported by those fields.
- If a label claims too much, narrow the label.
- If evidence exists but the label is too weak, strengthen the label.

Repeat for each projection rule in policy.projections.

### Step 4: Non-regression review
For each proposed change:
- Identify what value the old version provided.
- State how the new version preserves that value.
- If a change removes information, propose an alternative that preserves it.

### Step 5: Apply changes and validate
Apply the proposed edits.

Regenerate the registry using:
- python3 scripts/update_procedure_registry.py

Spot-check at least three entries:
- one that is required by core gates
- one that has multiple usage logs
- one that is not listed in the catalog


## When to Use
- After changing registry schema, naming, or derived state logic
- When the registry output feels unclear to read
- When adding a new evidence source or new derived state

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.