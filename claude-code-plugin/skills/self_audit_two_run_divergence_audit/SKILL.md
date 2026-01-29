---
name: self_audit_two_run_divergence_audit
description: "Run the same gate/procedure twice on the same fixed input, compare outputs, and treat divergences as evidence that the text needs clearer interfaces and stopping rules."
---

# Two-Run Divergence Audit

## Overview
Run the same gate/procedure twice on the same fixed input, compare outputs, and treat divergences as evidence that the text needs clearer interfaces and stopping rules.

## Steps

### Step 1: Define what “the run” means
State:
- What artifact is being run (target_path).
- What counts as its output (expected sections, fields, or decisions).
- What is held fixed (fixed_input, run_instructions).
- The stopping rule for this audit: two runs, one comparison, one rewrite queue.

### Step 2: Run A
Run the target on fixed_input.
Produce the output in the target’s own expected format.

### Step 3: Run B (fresh)
Run the same target again on the same fixed_input.
Do not reuse Run A content; produce a fresh output.

### Step 4: Compare outputs and isolate divergences
Compare Run A and Run B and list divergences as concrete differences:
- different decisions (pass/fail, recommended actions)
- different definitions of the same term
- different claims treated as “verified”
- different next steps chosen
- different stopping points

For each divergence, point to the most likely text cause:
- undefined term
- bundled check
- missing answer-interface
- ambiguous stopping rule
- implicit conditional

### Step 5: Use protocol clarity questions on the divergences
Apply:
- library/procedures/core/goal_analysis/analysis_protocol_clarity_and_validity.yaml

Focus on:
- which step caused divergence
- what input was missing or underspecified
- what output is not defined precisely enough
- what would make “done” checkable
- what the stopping rule should be

Produce a rewrite queue of specific edits.


## When to Use
- When you want repeatable results across executors (human, AI, future you)
- When a gate/procedure is used for enforcement decisions
- When outputs feel inconsistent across runs

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.