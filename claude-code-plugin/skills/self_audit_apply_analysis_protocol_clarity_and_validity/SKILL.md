---
name: self_audit_apply_analysis_protocol_clarity_and_validity
description: "Use the analysis-protocol clarity question bank to audit a gate/procedure/document for interpretability, checkability, and stopping rules."
---

# Apply Analysis Protocol Clarity + Validity

## Overview
Use the analysis-protocol clarity question bank to audit a gate/procedure/document for interpretability, checkability, and stopping rules.

## Steps

### Step 1: Load the question bank
Load and use:
- library/procedures/core/goal_analysis/analysis_protocol_clarity_and_validity.yaml

Treat it as the canonical question list to apply.

### Step 2: Extract candidate lines to audit
From each target file, extract the lines that function as:
- questions
- checks / criteria
- decision hooks (pass/fail, promote/expand, etc.)

Keep anchors (file + line) so each issue is actionable.

### Step 3: Apply protocol clarity questions
Using the loaded question bank, answer these classes of questions about each target:
- What protocol is implicitly being run by this artifact?
- What are the steps and what does each step consume/produce?
- How do we know each step is complete?
- What is the stopping rule for one pass?
- Where do ambiguity and divergence enter?

Record only findings that produce a concrete edit.

### Step 4: Propose fixes with non-regression
For each rewrite candidate:
- State what the original line was trying to accomplish (intent).
- Propose a rewrite that preserves that intent.
- If the rewrite removes information, add it back as separate prompts instead.

Prefer:
- splitting bundled checks into separate lines
- defining terms used as if shared
- adding an answer-interface (definition/observation/provenance/measurement/decision)
- adding a stopping rule or continuation rule


## When to Use
- When a gate/procedure feels rigorous but is hard to execute
- When different executors interpret the same text differently
- When you want to convert interpretive prompts into checkable prompts

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.