---
name: "val - Validation"
description: "Verify that an output meets its requirements"
---

# Validation

## Overview
Verify that an output meets its requirements

## Steps

### Step 1: Gather inputs
Collect the validation target and its requirements.
If acceptance_criteria not provided, derive from requirements.

### Step 2: Check each requirement
For each requirement:
1. State the requirement clearly
2. Identify where in the target this should be satisfied
3. Check if acceptance criteria are met
4. Document finding: met, partially met, or not met

### Step 3: Calculate coverage
Count requirements by status:
- met: count as 1.0
- partially met: count as 0.5
- not met: count as 0.0
Calculate: coverage = sum / total_requirements

### Step 4: Determine overall result
Based on coverage and criticality:
- pass: All requirements met (coverage = 1.0)
- partial: Some requirements met (0 < coverage < 1.0)
- fail: Critical requirements not met (coverage = 0 or critical gap)

### Step 5: Generate recommendations
For each gap (partial or not met):
1. Identify what's missing
2. Suggest specific action to address
3. Estimate effort if possible


## When to Use
- After completing a deliverable to verify it meets requirements
- Before accepting work from others
- At phase gates to confirm phase objectives achieved
- When transitioning from planning to execution
- To close out a goal or project

## Verification
- All requirements examined (none skipped)
- Evidence provided for each "met" determination
- Gaps clearly explained for each "not met" determination
- Recommendations are actionable (not vague)

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.