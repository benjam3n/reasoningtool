---
name: specificity_gate
description: Transform vague capability claims into specific ones by requiring trigger, procedure, output, and validation for each claim.
---

# Specificity Gate

**Input**: $ARGUMENTS (a claim about what a system does or should do)

---

## Purpose

Vague claims sound good but cannot be implemented or verified. This procedure transforms vague claims into specific ones.

**Principle**: A claim is specific enough to implement when it answers: TRIGGER, PROCEDURE, OUTPUT, VALIDATION.

---

## Step 1: Identify the Claim Type

| Type | Pattern | Example |
|------|---------|---------|
| **Capability** | "System does X" | "System detects gaps" |
| **Requirement** | "System should X" | "System should learn from sessions" |
| **Behavior** | "When X, system Y" | "When user asks, system responds" |
| **Property** | "System is X" | "System is self-improving" |

**Claim identified**: [the claim]
**Type**: [Capability / Requirement / Behavior / Property]

---

## Step 2: Check for Four Elements

For the claim to be implementable, it must specify:

| Element | Question | Status |
|---------|----------|--------|
| **TRIGGER** | What causes this to happen? | SPECIFIED / MISSING |
| **PROCEDURE** | What exact steps occur? | SPECIFIED / MISSING |
| **OUTPUT** | What concrete result is produced? | SPECIFIED / MISSING |
| **VALIDATION** | How do we know it worked? | SPECIFIED / MISSING |

---

## Step 3: Extract What's Specified

For each SPECIFIED element, extract the concrete specification:

```
TRIGGER: [what's stated or implied]
PROCEDURE: [what's stated or implied]
OUTPUT: [what's stated or implied]
VALIDATION: [what's stated or implied]
```

---

## Step 4: Generate Questions for Missing Elements

For each MISSING element, generate the specific question that must be answered:

| Missing Element | Question to Answer |
|-----------------|-------------------|
| TRIGGER | [specific question about what initiates this] |
| PROCEDURE | [specific question about what steps occur] |
| OUTPUT | [specific question about what result is produced] |
| VALIDATION | [specific question about how success is measured] |

---

## Step 5: Provide Concrete Answer Options

For each question, provide 2-3 concrete answer options (not more vague claims):

| Question | Option A | Option B | Option C |
|----------|----------|----------|----------|
| [question 1] | [concrete answer] | [concrete answer] | [concrete answer] |
| [question 2] | [concrete answer] | [concrete answer] | [concrete answer] |

**Concreteness test for options**:
- Can a programmer implement this without asking clarifying questions?
- If NO, the option is still too vague.

---

## Step 6: Assemble Specific Claim

Once all four elements are specified:

```
SPECIFIC CLAIM:

TRIGGER: [concrete trigger]
  When: [exact condition]
  Detected by: [mechanism]

PROCEDURE: [concrete steps]
  1. [step with input/output]
  2. [step with input/output]
  3. [step with input/output]

OUTPUT: [concrete deliverable]
  Format: [data structure or file]
  Contains: [specific fields]

VALIDATION: [concrete test]
  Success if: [measurable condition]
  Measured by: [mechanism]
```

---

## Step 7: Verify Specificity

Apply the implementation test:

| Check | Pass/Fail |
|-------|-----------|
| Programmer can implement without clarifying questions | PASS / FAIL |
| Each step has defined input and output | PASS / FAIL |
| Output format is specified (not just described) | PASS / FAIL |
| Validation is measurable (not subjective) | PASS / FAIL |

If any FAIL: return to Step 4 and make more specific.

---

## Output Format

```
## SPECIFICITY GATE RESULT

### Original Claim
[the vague claim]

### Claim Type
[Capability / Requirement / Behavior / Property]

### Element Status
- TRIGGER: [SPECIFIED / MISSING]
- PROCEDURE: [SPECIFIED / MISSING]
- OUTPUT: [SPECIFIED / MISSING]
- VALIDATION: [SPECIFIED / MISSING]

### Questions to Answer (for missing elements)
1. [question]
   - Option A: [concrete answer]
   - Option B: [concrete answer]

### Specific Claim (once all answered)
TRIGGER: [concrete]
PROCEDURE: [concrete steps]
OUTPUT: [concrete format]
VALIDATION: [concrete test]

### Implementation Ready
[YES / NO - if NO, what's still vague]
```

---

## Examples

### Example: Vague Claim

**Input**: "System detects gaps"

**Result**:
- TRIGGER: MISSING - What causes gap detection to run?
- PROCEDURE: MISSING - What steps identify a gap?
- OUTPUT: MISSING - What does a detected gap look like?
- VALIDATION: MISSING - How do we know the gap is real?

Questions:
1. What triggers gap detection?
   - Option A: Every time procedure_engine runs
   - Option B: On demand via CLI command
   - Option C: Scheduled daily scan

2. What counts as a gap?
   - Option A: No procedure matches user input keywords
   - Option B: User explicitly says "I need a procedure for X"
   - Option C: Same input type appears 3+ times with no resolution

### Example: Specific Claim

**Input**: "When procedure_catalog.search() returns empty results for a user query, write the query to data/gaps.json with timestamp"

**Result**:
- TRIGGER: SPECIFIED - procedure_catalog.search() returns empty
- PROCEDURE: SPECIFIED - write to data/gaps.json
- OUTPUT: SPECIFIED - JSON entry with query and timestamp
- VALIDATION: SPECIFIED (implied) - gaps.json contains the entry

Implementation Ready: YES

---

## Execution Checklist

- [ ] Claim type identified
- [ ] All four elements checked
- [ ] Missing elements have questions
- [ ] Questions have concrete answer options
- [ ] Options pass concreteness test
- [ ] Final claim passes implementation test

---

**Execute now**: Transform the input claim into a specific, implementable specification.
