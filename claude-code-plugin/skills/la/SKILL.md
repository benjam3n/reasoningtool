---
name: "la - Limitation Analysis"
description: "Systematically identify limitations across multiple dimensions,"
---

# Limitation Analysis

## Overview
Systematically identify limitations across multiple dimensions,
assess their impact, and prioritize which to address.

Key insight: Most systems have many limitations, but only a few
matter enough to fix. This procedure separates identification
from prioritization to avoid premature filtering.

## Core Principle
1. Enumerate ALL limitations first (don't filter while listing)
2. Categorize by type (what kind of limitation)
3. Assess impact (what happens if we don't fix it)
4. Assess effort (what would fixing require)
5. Apply effort/impact gate to prioritize
6. Identify which limitations are INHERENT vs FIXABLE

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/la 4x [input]").

| Depth | Min Limitations Found | Min Categories Checked | Min Severity Assessments | Min Mitigation Plans |
|-------|----------------------|----------------------|------------------------|---------------------|
| 1x    | 5                    | 2                    | 3                      | 1                   |
| 2x    | 8                    | 3                    | 5                      | 2                   |
| 4x    | 12                   | 5                    | 8                      | 3                   |
| 8x    | 18                   | 7                    | 12                     | 5                   |
| 16x   | 25                   | 10                   | 18                     | 7                   |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## Steps

### Step 1: Define scope
Clearly state what system/method/process you're analyzing.
Include: purpose, current state, context of use.

### Step 2: Enumerate limitations freely
List ALL limitations you can think of without filtering.
Use the analysis_questions.enumerate prompts.
Don't worry about categorization or priority yet.
Aim for completeness over precision.

### Step 3: Categorize each limitation
For each limitation, assign a category from limitation_categories.
Mark whether it's INHERENT (can't be fixed) or FIXABLE.
Note if it's a TRADEOFF (fixing it would break something else).

### Step 4: Assess impact of each
Rate impact: CRITICAL / HIGH / MEDIUM / LOW / NEGLIGIBLE

CRITICAL: Blocks core use case, causes harm
HIGH: Significantly degrades value
MEDIUM: Noticeable but workable
LOW: Minor inconvenience
NEGLIGIBLE: Theoretical only

### Step 5: Assess effort to fix each
Rate effort: TRIVIAL / LOW / MEDIUM / HIGH / MASSIVE

TRIVIAL: < 1 hour, no dependencies
LOW: < 1 day, minimal dependencies
MEDIUM: Days to weeks, some coordination
HIGH: Weeks to months, significant resources
MASSIVE: Months+, major restructuring

### Step 6: Apply effort/impact prioritization
Create priority matrix:

DO FIRST:  TRIVIAL/LOW effort  + HIGH/CRITICAL impact
DO SECOND: MEDIUM/HIGH effort  + HIGH/CRITICAL impact
MAYBE:     TRIVIAL/LOW effort  + LOW/MEDIUM impact
AVOID:     MEDIUM/HIGH effort  + LOW/NEGLIGIBLE impact
ACCEPT:    INHERENT limitations (can't fix, work around)

### Step 7: Identify quick wins
From DO FIRST, identify the single most impactful fix.
Ask: "If we could only fix ONE thing, what would it be?"

### Step 8: Document workarounds
For limitations we won't fix, document:
- How to work around it
- When it matters vs when it doesn't
- Who needs to know about it


---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.