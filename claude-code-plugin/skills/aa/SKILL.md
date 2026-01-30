---
name: aa
description: Surface and rigorously test a field's hidden assumptions. Compound skill that chains extraction, inversion, research, ARAW testing, cross-domain perspective, and synthesis into a complete audit.
---

# Assumption Audit

**Input**: $ARGUMENTS

---

## Purpose

Every field, practice, or belief system rests on hidden assumptions that practitioners rarely question. This compound skill systematically surfaces those assumptions and stress-tests them.

**What this produces**: A ranked report of a field's hidden assumptions with validation status (validated, challenged, or overturned), cross-domain perspective, and actionable implications.

**This is a compound skill** -- it chains 6 skills in sequence. Each step builds on the previous.

---

## The Chain

```
Step 1: /aex    -- Surface hidden assumptions
Step 2: /ai     -- Ask "what if the opposite is true?"
Step 3: /lr        -- Check what's already known about these assumptions
Step 4: /araw 8x                  -- Rigorously test each assumption (Assume Right / Assume Wrong)
Step 5: /cda     -- How do other fields handle similar assumptions?
Step 6: /ins        -- Combine all findings into ranked report
```

---

## Execution Procedure

### Step 1: Extract Hidden Assumptions

-> INVOKE: /aex $ARGUMENTS

Extract all hidden assumptions from the field/practice/belief. For each assumption, identify:
- What type it is (causal, existence, stability, access, capability, value, knowledge, resources, permission, timing)
- How critical it is (HIGH / MED / LOW)
- Whether practitioners are aware of it

**Target**: 15-25 assumptions for a meaningful audit.

**Output of this step**: Numbered list of assumptions with type and criticality rating.

---

### Step 2: Invert Each Assumption

-> INVOKE: /ai [assumptions from Step 1]

For each assumption, ask: "What if the opposite is true?" This reveals:
- Alternative worldviews that practitioners miss
- Failure modes hiding behind the assumption
- Opportunities that the assumption conceals

**Output of this step**: Each assumption paired with its inversion and what the inversion would mean.

---

### Step 3: Research Existing Critiques

-> INVOKE: /lr [key assumptions and inversions]

Before running ARAW, check what's already known:
- Has this assumption been challenged before?
- What evidence exists for and against?
- Are there fields that already operate on the opposite assumption?

This prevents rediscovering known critiques and grounds the audit in existing work.

**Output of this step**: Evidence summary for/against each major assumption.

---

### Step 4: ARAW Testing

-> INVOKE: /araw 8x [assumptions with evidence from Steps 1-3]

For each HIGH and MED criticality assumption, run full ARAW:
- ASSUME RIGHT: What follows if this assumption holds? What must also be true?
- ASSUME WRONG: What follows if this assumption fails? What's the alternative?

Recurse to depth 6+. Each sub-claim gets its own AR/AW branch.

**Output of this step**: Each assumption classified as VALIDATED, CHALLENGED, or OVERTURNED with reasoning.

---

### Step 5: Cross-Domain Perspective

-> INVOKE: /cda [challenged and overturned assumptions]

For assumptions that were CHALLENGED or OVERTURNED:
- What do other fields do differently?
- Are there domains that explicitly reject this assumption and succeed?
- What can this field learn from those domains?

**Output of this step**: Cross-domain insights for each challenged assumption.

---

### Step 6: Synthesize Findings

-> INVOKE: /ins [all outputs from Steps 1-5]

Combine everything into a final audit report:

```
ASSUMPTION AUDIT: [Field/Practice/Belief]
==========================================

EXECUTIVE SUMMARY (1 page)
- X assumptions surfaced, Y challenged, Z overturned
- Top 3 findings
- Key implications

FULL FINDINGS (by criticality)

OVERTURNED ASSUMPTIONS:
[For each]: What it is, why it's wrong, what the evidence says,
what other fields do instead, what to do about it

CHALLENGED ASSUMPTIONS:
[For each]: What it is, why it's uncertain, evidence both ways,
what other fields suggest, what to investigate further

VALIDATED ASSUMPTIONS:
[For each]: What it is, why it holds, supporting evidence

CROSS-DOMAIN INSIGHTS:
[Transferable lessons from other fields]

IMPLICATIONS:
[What practitioners should do differently based on findings]
```

-> COMPLETE

---

## Output Standards

- All outputs readable WITHOUT knowledge of GOSM, ARAW, or UAUA
- The method is invisible; the findings are the product
- Include validation status: "This audit has not been reviewed by domain experts"
- For high-stakes fields (medical, legal, financial): include disclaimer
- Produce both executive summary AND full report

---

## Quality Gates

Between Steps 3 and 4: If literature review reveals the assumptions are already well-studied and consensus exists, note this and focus ARAW on areas of genuine uncertainty.

Between Steps 4 and 5: If all assumptions are VALIDATED, the audit may not be very interesting. Consider whether the extraction (Step 1) went deep enough.

Between Steps 5 and 6: If cross-domain insights are superficial (surface analogy, not structural), re-examine whether the analogy is transferable.

---

## Example Usage

```
/aa software project estimation
/aa higher education as career preparation
/aa venture capital as startup funding model
/aa agile methodology in large organizations
```
