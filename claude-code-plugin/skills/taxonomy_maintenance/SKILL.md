---
name: taxonomy_maintenance
description: "Systematic process for creating, updating, and maintaining taxonomies and classification systems."
---

# Taxonomy Maintenance

## Overview
Systematic process for creating, updating, and maintaining taxonomies and classification systems.

## Steps

### Step 1: Scope Definition
Define taxonomy boundaries:
1. What entities are being classified?
2. What is in scope vs out of scope?
3. What level of granularity is needed?
4. Who are the users of this taxonomy?
5. What decisions will it inform?

Document: purpose statement, inclusion/exclusion criteria

### Step 2: Existing Structure Review
If updating existing taxonomy:
1. Review current categories and hierarchy
2. Identify known problems (gaps, overlaps, ambiguities)
3. Collect feedback from users
4. Note categories with edge cases

If creating new:
1. Research existing taxonomies in domain
2. Identify best practices
3. Decide: adopt, adapt, or create from scratch

### Step 3: Category Development
Develop/refine categories:

Principles:
- Mutually exclusive (items belong to one category)
- Collectively exhaustive (all items can be classified)
- Consistent granularity at each level
- Meaningful distinctions (categories differ in important ways)

For each category:
- Name (clear, descriptive)
- Definition (unambiguous criteria)
- Examples (typical cases)
- Non-examples (common misclassifications)
- Parent/child relationships

### Step 4: Hierarchy Design
Structure the taxonomy:

Hierarchy types:
- Strict hierarchy (each item has one parent)
- Polyhierarchy (items can have multiple parents)
- Faceted (multiple independent dimensions)

Design considerations:
- Depth (how many levels?)
- Breadth (how many siblings?)
- Balance (similar detail across branches)

Validate: Can all known entities be classified?

### Step 5: Consistency Validation
Check for problems:

Structural issues:
- Orphan categories (no parent)
- Empty categories (no instances)
- Overlapping categories (ambiguous classification)
- Missing categories (known items unclassifiable)

Definition issues:
- Vague criteria
- Circular definitions
- Inconsistent terminology

Test: Classify 20+ diverse examples, note difficulties

### Step 6: Versioning and Change Control
Establish maintenance process:

Version scheme:
- Major: Breaking changes (restructuring, removing categories)
- Minor: Additions (new categories)
- Patch: Clarifications (definition improvements)

Change process:
1. Propose change with rationale
2. Assess impact on existing classifications
3. Update definitions and examples
4. Update version number
5. Document in change log

Migration: How to handle items in changed categories?

### Step 7: Documentation
Create taxonomy documentation:

For users:
- Category list with definitions
- Decision tree for classification
- Examples and edge cases
- FAQ for common questions

For maintainers:
- Design rationale
- Known limitations
- Future considerations
- Change log

### Step 8: Periodic Review
Schedule regular maintenance:

Review triggers:
- Calendar (quarterly, annually)
- Threshold (X% items unclassifiable)
- Major domain change

Review checklist:
- Are definitions still clear?
- Are there new categories needed?
- Are any categories unused?
- Is the structure still appropriate?
- User feedback since last review?


## When to Use
- Creating a new classification system
- Updating existing taxonomy with new categories
- Resolving inconsistencies in classification
- Periodic taxonomy review and maintenance

## Verification
- All categories have clear definitions
- Test cases classify unambiguously
- No orphan or duplicate categories
- Version and change log maintained

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.