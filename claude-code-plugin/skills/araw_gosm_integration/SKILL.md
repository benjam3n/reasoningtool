---
name: araw_gosm_integration
description: "Systematic procedure for translating ARAW exploration outputs"
---

# ARAW to GOSM Integration

## Overview
Systematic procedure for translating ARAW exploration outputs
into GOSM execution inputs.

ARAW = Exploration engine (maps possibility space)
GOSM = Execution engine (turns insights into action)

This bridge ensures ARAW findings automatically populate GOSM structures.

## Steps

### Step 1: Run ARAW synthesis
If multiple ARAW databases exist:
  python synthesize.py *.db --find-tensions --extract-actions actions.json

This produces:
- Summary of each database
- Cross-database themes
- Tensions and contradictions
- Consolidated action items (DO_FIRST, DO_SECOND, crux nodes)

### Step 2: Extract MUST_VERIFY items
From synthesis output, identify:

MUST_VERIFY (before strategy commitment):
- All crux nodes
- All DO_FIRST actions
- All unresolved tensions

These become GOSM gates that must pass before proceeding.

### Step 3: Populate Assumption Register
For each crux node:

assumption:
  id: [from ARAW]
  claim: [original claim text]
  confidence: [ARAW probability estimate]
  criticality: CRITICAL | HIGH | MEDIUM | LOW
  validation_method: [how to test]
  validation_status: UNVALIDATED
  if_false_action: [contingency]
  source: ARAW:[database_name]

### Step 4: Populate Risk Register
For each claim with probability < 0.7:

risk:
  id: [generated]
  description: [claim might be false]
  probability: [1 - ARAW probability]
  impact: [from leverage score]
  mitigation: [if applicable]
  contingency: [ARAW ASSUME_WRONG branch]
  source: ARAW:[database_name]

### Step 5: Identify Strategy Candidates
From ARAW branches, extract:
- High-leverage ASSUME_RIGHT branches = Strategy candidates
- High-leverage ASSUME_WRONG branches = Alternative approaches

Feed into Strategy Discovery phase.

### Step 6: Create Decision Tree Branches
For each ARAW tension:

decision_point:
  id: [generated]
  question: [tension summary]
  option_a: [one side of tension]
  option_b: [other side of tension]
  resolution_criteria: [how to decide]
  current_choice: UNRESOLVED
  source: ARAW_TENSION

### Step 7: Mark High-Confidence Foundations
For themes appearing in 2+ ARAW runs:

foundation:
  claim: [theme summary]
  confidence: HIGH (cross-verified)
  sources: [list of ARAW databases]
  validation_needed: MINIMAL

These can be treated as near-axioms for planning.


## When to Use
- After ARAW exploration on a problem/goal
- Before starting GOSM planning phase
- When ARAW identifies tensions or crux nodes

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.