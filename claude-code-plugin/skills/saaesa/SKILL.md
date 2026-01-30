---
name: "saaesa - Apply Evidence Standard Application"
description: "Audit a document as if it claimed an evidence standard, and require checkable verification (or pointers to verification) for any “verified” claims."
---

# Apply Evidence Standard Application

## Overview
Audit a document as if it claimed an evidence standard, and require checkable verification (or pointers to verification) for any “verified” claims.

## Steps

### Step 1: Load the question bank
Load and use:
- library/procedures/core/goal_analysis/evidence_standard_application.yaml

Treat it as the canonical audit question list to apply.

### Step 2: Define the evidence labels used in the target
For each target:
- Identify whether it uses evidence labels (e.g., Verified/Assumption/Unknown).
- If it does not, state what label set it implicitly relies on (or write 'none').
- Apply the verified_definition for this audit.

### Step 3: Inventory and audit “verified” claims
For each target:
- List the claims it treats as “verified” or uses as premises for conclusions.
- For each claim, identify what check would verify it.
- If the document provides no check and no pointer, flag it.

Repairs:
- add missing check
- add pointer to an existing procedure/gate that supplies the check
- weaken or relabel the claim

### Step 4: Confirm downstream usage does not smuggle certainty
Check whether any Assumption/Unknown claims are used as if they were Verified.
For each case:
- add a check
- change the conclusion
- or change the label and propagate the change


## When to Use
- When a procedure/gate uses labels like Verified/Assumption/Unknown
- When a document sounds rigorous but does not specify how to verify claims
- When you want to turn “verified” into a repeatable content audit

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.