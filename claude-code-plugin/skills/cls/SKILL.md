---
name: cls
description: "The simplest possible search: enumerate items, check each against"
---

# Checklist Search

## Overview
The simplest possible search: enumerate items, check each against
criteria, return those that pass. Intelligence is in creating the
checklist, not in following it.

## Goal
Find items that match criteria by checking each item against
a defined checklist. Pure mechanical matching - no judgment required.

## Steps

### Step 1: Define Criteria Checklist
List all criteria that items must meet.
Each criterion must be:
- Observable (can be checked)
- Binary (pass/fail) or Scorable (1-10)
- Independent (checking one doesn't affect another)

**Output**: Numbered criteria list

### Step 2: Enumerate Items
List all items to be checked.
Include everything - filtering happens via criteria.

**Output**: Numbered item list

### Step 3: Check Each Item
For each item, check each criterion.
Record PASS (✓) or FAIL (✗) for each.
No judgment - just mechanical checking.

**Output**: Results matrix

### Step 4: Aggregate Results
Based on mode:
- all_must_pass: Item passes only if ALL criteria pass
- any_must_pass: Item passes if ANY criterion passes
- weighted_score: Calculate weighted sum, threshold for pass

**Output**: Final pass/fail for each item

### Step 5: Return Passing Items
List all items that passed.
Optionally rank by number of criteria met or weighted score.

**Output**: Filtered list


## When to Use
- Filtering options by requirements
- Audit/compliance checking
- Quality assurance
- Finding items that meet specifications
- Any search with explicit pass/fail criteria

## Verification
- All criteria are observable and checkable
- Each criterion was checked for each item
- Pass/fail was recorded with evidence
- Aggregation mode was applied correctly
- Results are reproducible (another checker would get same result)

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.