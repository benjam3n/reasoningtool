---
name: atgb
description: "Bridges ARAW exploration outputs to GOSM planning inputs."
---

# ARAW to GOSM Bridge

## Overview
Bridges ARAW exploration outputs to GOSM planning inputs.
Converts discovered assumptions/claims into actionable GOSM items:
- Assumption verification tasks
- Strategy constraints
- Risk factors
- Decision dependencies

## Core Principle
ARAW explores possibility space → finds claims that matter
GOSM plans execution → needs to know which claims to validate first

This bridge ensures ARAW insights become GOSM action items,
and GOSM outcomes update ARAW assumptions.

## Steps

### Step 1: Run ARAW synthesis
Run synthesis across relevant ARAW databases:

python synthesize.py *.db --find-tensions --extract-actions actions.json

This produces:
- Summary of each database
- Cross-database themes
- Tensions and contradictions
- Consolidated action items

### Step 2: Identify critical assumptions
From synthesis output, extract:

MUST_VERIFY (before proceeding):
- All crux nodes
- DO_FIRST actions
- Unresolved tensions

SHOULD_VERIFY (during execution):
- DO_SECOND actions
- High-leverage unexplored

NICE_TO_VERIFY (if time permits):
- Medium-leverage unexplored
- Common themes (for confidence)

### Step 3: Create verification tasks
For each MUST_VERIFY item, create a GOSM task:

- task: "Verify: [claim summary]"
  type: assumption_verification
  source: [araw_db_name]
  original_claim: [full claim text]
  verification_method: [how to check]
  pass_criteria: [what counts as verified]
  fail_action: [what to do if false]
  effort: [from ARAW scoring]
  impact: [from ARAW scoring]

### Step 4: Map to GOSM decision tree
For each tension/contradiction:

Create a decision node in GOSM:
- decision: "Resolve tension: X vs Y"
  option_a: [one side of tension]
  option_b: [other side]
  evidence_needed: [what would resolve]
  default: [if can't resolve, which way to lean]

### Step 5: Set up feedback loop
Create feedback mechanism:

When GOSM verification task completes:
1. Record outcome (verified/falsified/inconclusive)
2. If falsified: Mark ARAW node as WRONG, prune downstream
3. If verified: Mark ARAW node as CONFIRMED, boost leverage
4. If inconclusive: Add to SHOULD_VERIFY for later

CAUTION: Assumption updates can cascade.
Only update with high-confidence outcomes.
Mark update source (evidence vs inference).

### Step 6: Generate GOSM input file
Export bridge output as GOSM-compatible format:

assumptions:
  must_verify: [list]
  should_verify: [list]
  nice_to_verify: [list]

decisions:
  unresolved_tensions: [list with options]

constraints:
  from_araw: [list of discovered constraints]

out_of_scope:
  drifted_topics: [list of rejected/drifted claims]


---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.