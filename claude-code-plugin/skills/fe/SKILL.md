---
name: "fe - Framework Extension"
description: "Systematic process for extending the GOSM framework with new procedures, gates, or capabilities."
---

# Framework Extension

## Overview
Systematic process for extending the GOSM framework with new procedures, gates, or capabilities.

## Steps

### Step 1: Gap Analysis
Search existing library for similar functionality:
1. Check INDEX.md for related procedures/gates
2. Search procedures/ directory for similar names
3. Review PROCEDURE_CONSOLIDATION.md for cluster overlap
4. Confirm this is genuinely new vs. enhancement of existing

### Step 2: Specification
Define the extension precisely:
1. Write purpose statement (1-2 sentences)
2. List inputs and outputs
3. Define 3-5 core steps
4. Identify integration points with existing framework

### Step 3: Template Selection
Choose appropriate template:
- Procedure: templates/procedure_template.yaml
- Gate: gates/core/requirement_verification_gates.yaml (as example)
- Domain handler: procedures/goal_approach_selections/ (as examples)

### Step 4: Implementation
Create the artifact following template:
1. Copy template to appropriate directory
2. Fill in all BRONZE fields (required)
3. Fill in SILVER fields (recommended)
4. Add at least one example

### Step 5: Schema Validation
Validate against procedure_schema.yaml:
1. Check all required fields present
2. Verify tier requirements met (Bronze minimum)
3. Confirm naming conventions followed

### Step 6: Integration Test
Test integration with framework:
1. Reference from a test project STATE.md
2. Verify procedure can be invoked
3. Check outputs match specification
4. Confirm no conflicts with existing procedures

### Step 7: Index Update
Update library indexes:
1. Add entry to INDEX.md in appropriate section
2. Update PROCEDURE_CONSOLIDATION.md if applicable
3. Add to EXTRACTED_PROCEDURES_INDEX.md if in extracted/

### Step 8: Documentation
Ensure discoverability:
1. Write clear description field
2. Add tags for searchability
3. Link related_procedures
4. Update any dependent documentation


## When to Use
- Adding a new procedure to the library
- Creating new gates or gate categories
- Extending GOSM capabilities (e.g., new goal approach selections)
- Improving existing framework components

## Verification
- New YAML file exists in correct directory
- INDEX.md contains new entry
- Schema validation passes
- At least one example provided

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.