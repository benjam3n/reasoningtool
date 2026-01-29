---
name: procedure_improvement
description: "Systematically improve GOSM library procedures using schema-driven validation and tier-based progress tracking"
---

# Procedure Improvement

## Overview
Systematically improve GOSM library procedures using schema-driven validation and tier-based progress tracking

## Steps

### Step 1: Load schema and procedures
1. Read the procedure schema from schema_path
2. Parse all procedure files from procedure_paths
3. Create inventory of procedures to assess

### Step 2: Validate each procedure
For each procedure:
1. Check Bronze tier requirements (id, name, version, description, steps)
2. Check Silver tier requirements (inputs, outputs, when_to_use, examples)
3. Check Gold tier requirements (failure_modes, gosm_integration, verification)
4. Record current tier and missing fields

### Step 3: Calculate priority scores
For each procedure:
priority = usage_weight × severity_weight / effort_estimate

Usage weights:
- core: 3, meta: 3, extracted: 2, domain-specific: 1

Severity weights:
- failing_schema: 3, missing_examples: 2, missing_advanced: 1

Effort estimate:
- single_field: 1, section_add: 2, major_rewrite: 5

Sort procedures by priority (highest first)

### Step 4: Improve procedures
For each procedure in priority_queue (up to target count):
1. Read current content
2. Identify gaps from validation_results
3. Generate content for missing fields:
   - version: Add "1.0.0" if missing
   - inputs: Infer from steps and description
   - outputs: Infer from steps and purpose
   - when_to_use: Derive from purpose
   - examples: Create from procedure purpose
   - failure_modes: Identify common problems
   - gosm_integration: Determine workflow placement
4. Merge new content with original (preserve all original content)
5. Validate improved version
6. Verify no degradation (tier >= original tier)
7. Write improved file

### Step 5: Generate improvement report
Create summary document with:
1. Procedures analyzed
2. Tier distribution (before and after)
3. Improvements made per procedure
4. Remaining gaps for future work


## When to Use
- After adding new procedures to the library
- Periodically to improve library quality
- When procedures feel incomplete or inconsistent
- Before major GOSM version releases

## Verification
- All improvements are schema-justified (not arbitrary)
- No procedure degrades (tier before <= tier after)
- Original content preserved in all cases
- Priority algorithm applied consistently

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.