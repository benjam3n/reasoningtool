---
name: "oart - Artifact Generation"
description: Generates reusable artifacts such as templates, checklists, frameworks, and tools. Takes a use case and produces a well-structured artifact with usage instructions and a tested example.
---

# Artifact Generation

**Input**: $ARGUMENTS

---

## Step 1: Identify Artifact Type

Determine what kind of artifact is needed.

| Type | What it is | Example |
|------|-----------|---------|
| **TEMPLATE** | A fill-in-the-blank structure | Project brief template, email template |
| **CHECKLIST** | A verification list | Launch checklist, review checklist |
| **FRAMEWORK** | A thinking model with categories | 2x2 matrix, decision tree, scoring rubric |
| **TOOL** | A reusable calculation or process | ROI calculator, sizing heuristic |
| **RUBRIC** | A scoring/evaluation guide | Quality rubric, grading criteria |
| **PLAYBOOK** | A situation-response guide | Incident response, sales objection handling |

```
ARTIFACT TYPE: [TEMPLATE / CHECKLIST / FRAMEWORK / TOOL / RUBRIC / PLAYBOOK]
ARTIFACT NAME: [descriptive name]
```

---

## Step 2: Define the Use Case

Establish who uses this artifact, when, and why.

```
USE CASE:
  WHO: [the person or role that will use this]
  WHEN: [the trigger or situation that calls for this artifact]
  WHY: [what problem it solves or what outcome it enables]
  FREQUENCY: [one-time / recurring / as-needed]
```

Rules:
- The artifact should solve a real, recurring need
- If the use case is too narrow, the artifact won't be reused
- If the use case is too broad, the artifact won't be specific enough to help

---

## Step 3: Design the Structure

Lay out the skeleton of the artifact before filling it in.

```
STRUCTURE:
1. [section or component 1] — [purpose]
2. [section or component 2] — [purpose]
3. [section or component 3] — [purpose]
...
```

Design principles:
- Follow the user's natural workflow order
- Group related items together
- Include only what is necessary — resist feature creep
- Make required vs optional elements clear
- Use consistent formatting throughout

---

## Step 4: Populate with Content

Fill the structure with actual content, instructions, or fields.

Rules:
- For templates: use clear placeholder text like `[PROJECT NAME]` or `[DESCRIBE THE PROBLEM]`
- For checklists: use actionable items with verifiable completion criteria
- For frameworks: define each category and how to use it
- For tools: include formulas, scales, or decision logic
- For rubrics: define each level with concrete examples
- For playbooks: pair each situation with a specific response

---

## Step 5: Test with a Real Example

Apply the artifact to a concrete case to verify it works.

```
TEST CASE: [a specific realistic scenario]

APPLIED:
[show the artifact filled in with test case data]

ISSUES FOUND:
- [any gaps, confusion, or missing elements]
```

Fix all issues found before finalizing.

---

## Step 6: Refine for Reusability

Make the artifact work across multiple situations, not just the test case.

Checks:
- Can someone unfamiliar with the context use this artifact?
- Are all jargon and assumptions explained?
- Does it work for edge cases (very small scope, very large scope)?
- Is the artifact self-contained or does it depend on external knowledge?

```
REFINEMENTS MADE:
- [change 1]
- [change 2]
```

---

## Step 7: Add Usage Instructions

Provide clear instructions so the artifact can be used independently.

```
USAGE INSTRUCTIONS:
  WHEN TO USE: [trigger or situation]
  HOW TO USE:
  1. [first step]
  2. [second step]
  3. [third step]
  TIPS: [common mistakes to avoid or best practices]
  ADAPT BY: [what to customize for different contexts]
```

---

## Deliver

Present the final artifact with:
- Name and type
- Usage instructions at the top
- The artifact itself
- The worked example as a reference

---

## Integration

Use with:
- `/oprc` -> Generate a procedure, then package it as a reusable artifact
- `/olst` -> Generate a checklist artifact from a comprehensive list
- `/orec` -> Turn recommendations into a playbook artifact
- `/de` -> Design a system, then create templates for operating it
