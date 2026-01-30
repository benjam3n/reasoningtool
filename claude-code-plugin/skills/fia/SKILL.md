---
name: "fia - Field Analysis"
description: Comprehensive analysis of a field's key tensions, hidden assumptions, and blind spots. Chains assumption extraction, deep ARAW testing, cross-domain perspective, evaluation dimensions, and insight synthesis into a complete field report.
---

# Field Analysis

**Input**: $ARGUMENTS

---

## Purpose

Every field has unquestioned orthodoxies, unresolved tensions, and blind spots that insiders can't see. This skill produces a comprehensive analysis of a field by combining assumption extraction, rigorous testing, outside perspective, and multi-dimensional evaluation.

**What this produces**: A comprehensive report covering a field's hidden assumptions, key tensions, blind spots, what other fields know that this one doesn't, and actionable recommendations.

**This is a compound skill** -- it chains 5 skills in sequence. It is the most comprehensive single-field analysis available.

---

## The Chain

```
Step 1: /aex     -- Surface the field's hidden beliefs
Step 2: /araw 8x                   -- Deep test of each assumption
Step 3: /cda      -- What do other fields see that this one doesn't?
Step 4: /evaluation_dimensions     -- Evaluate the field across multiple dimensions
Step 5: /ins         -- Combine into comprehensive report
```

---

## Execution Procedure

### Step 1: Extract the Field's Hidden Assumptions

-> INVOKE: /aex $ARGUMENTS

Go beyond surface beliefs. Extract:
- **Foundational assumptions**: What the field takes as given (often unstated in textbooks)
- **Methodological assumptions**: How the field thinks knowledge is produced
- **Value assumptions**: What the field considers important or good
- **Boundary assumptions**: What the field considers in-scope vs out-of-scope
- **Historical assumptions**: Beliefs inherited from the field's origins that may no longer hold

**Target**: 20-30 assumptions across all five categories.

**Output**: Categorized assumptions with criticality ratings.

---

### Step 2: Deep ARAW Testing

-> INVOKE: /araw 8x [assumptions from Step 1, grouped by criticality]

For HIGH and MED criticality assumptions, run deep ARAW:
- 6+ levels deep for each assumption
- Each sub-claim gets its own AR/AW branch
- Track which assumptions support each other (cluster analysis)
- Identify keystone assumptions (many others depend on them)

**Output**: Each assumption rated VALIDATED / CHALLENGED / OVERTURNED, with full reasoning trees. Keystone assumptions identified.

---

### Step 3: Cross-Domain Perspective

-> INVOKE: /cda [the field + its challenged/overturned assumptions]

Bring in outside perspectives:
- Which other fields face similar problems but answer them differently?
- Where does this field's orthodoxy look strange from outside?
- What would a practitioner from [adjacent field] find surprising about this field's assumptions?

**Target**: 5-10 cross-domain insights.

**Output**: Outside perspectives on the field's blind spots.

---

### Step 4: Multi-Dimensional Evaluation

-> INVOKE: /evaluation_dimensions [the field as a whole]

Evaluate the field across universal dimensions:
- **Epistemic health**: How well does the field update on evidence?
- **Internal coherence**: Do the field's claims contradict each other?
- **External validity**: Do the field's claims match observable reality?
- **Practical utility**: Does the field's knowledge actually help practitioners?
- **Innovation capacity**: Can the field generate novel insights?
- **Self-correction**: Does the field fix its own errors?
- **Inclusivity of evidence**: Does the field consider all relevant evidence sources?
- **Transparency**: Are the field's methods and assumptions visible?

**Output**: Scorecard with evidence for each dimension.

---

### Step 5: Synthesize Complete Analysis

-> INVOKE: /ins [all outputs from Steps 1-4]

Create the comprehensive field analysis:

```
FIELD ANALYSIS: [Field Name]
============================

EXECUTIVE SUMMARY (1-2 pages)
- The field's greatest strength
- The field's biggest blind spot
- Top 3 recommendations

PART 1: WHAT THE FIELD ASSUMES
- Foundational assumptions (rated)
- Methodological assumptions (rated)
- Value assumptions (rated)
- Boundary assumptions (rated)
- Historical assumptions (rated)
- Keystone assumptions (others depend on these)

PART 2: WHAT TESTING REVEALED
- Assumptions that held up under scrutiny
- Assumptions that are genuinely uncertain
- Assumptions that appear wrong
- Clusters of related assumptions

PART 3: WHAT OUTSIDERS SEE
- Cross-domain insights
- What looks strange from outside
- What other fields do differently and why

PART 4: FIELD HEALTH SCORECARD
- Epistemic health: [rating + evidence]
- Internal coherence: [rating + evidence]
- External validity: [rating + evidence]
- Practical utility: [rating + evidence]
- Innovation capacity: [rating + evidence]
- Self-correction: [rating + evidence]

PART 5: KEY TENSIONS
- [Tension 1]: The field wants X but this requires assuming Y, which conflicts with Z
- [Tension 2]: ...

PART 6: RECOMMENDATIONS
- For practitioners: [What to do differently based on findings]
- For researchers: [What to investigate based on gaps found]
- For the field as a whole: [Structural changes that would improve field health]
```

-> COMPLETE

---

## Output Standards

- Readable by both insiders and outsiders of the field
- Every claim supported by reasoning (not just assertions)
- Balanced: acknowledges what the field gets right, not just criticism
- Constructive: recommendations are actionable
- Honest about limitations: "This analysis was produced without domain expert review"
- Both executive summary and full report included

---

## Quality Gates

After Step 1: If fewer than 15 assumptions found, the extraction wasn't deep enough. Consider the 5 assumption categories and ensure each has at least 2-3 entries.

After Step 2: If everything is VALIDATED, either the field is unusually well-founded or the testing wasn't adversarial enough. Check that ASSUME WRONG branches were genuinely explored.

After Step 4: If all dimensions score high, consider whether the evaluation was rigorous or just surface-level.

---

## Example Usage

```
/fia software engineering
/fia clinical psychology
/fia economics
/fia education
/fia nutrition science
/fia venture capital
/fia machine learning research
```
