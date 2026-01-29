---
name: cross_domain_report
description: Discover what one field can learn from another by finding structural analogies, testing their transferability, and synthesizing actionable insights. Chains cross-domain analogy, assumption extraction, ARAW testing, and insight synthesis.
---

# Cross-Domain Report

**Input**: $ARGUMENTS

---

## Purpose

Most fields are siloed. Solutions that are standard practice in one domain are unknown in another. This skill systematically finds **structural analogies** between two fields and tests whether the insights actually transfer.

**What this produces**: A report of validated, transferable insights from Field B that Field A can apply, with concrete recommendations.

**This is a compound skill** -- it chains 4 skills in sequence.

---

## The Chain

```
Step 1: /cross_domain_analogy      -- Find structural matches between fields
Step 2: /assumption_extraction     -- What does Field A assume that Field B doesn't?
Step 3: /araw                      -- Test each analogy: structural or just surface similarity?
Step 4: /insight_synthesis         -- Combine into actionable recommendations
```

---

## Execution Procedure

### Step 1: Find Cross-Domain Analogies

-> INVOKE: /cross_domain_analogy $ARGUMENTS

Identify structural similarities between the two fields:
- What problems do both fields face?
- What solutions has Field B developed that Field A hasn't?
- Where are the structural parallels (not just surface)?
- What shared constraints or dynamics exist?

**Structural vs Surface test**:
- STRUCTURAL: Same underlying mechanism (aviation checklists -> surgical checklists = both manage human error in high-stakes sequential tasks)
- SURFACE: Same words but different mechanism (computer "virus" -> biological virus = metaphor, not transferable mechanism)

**Target**: 8-15 candidate analogies, clearly labeled structural vs surface.

**Output**: Candidate analogies with structural analysis.

---

### Step 2: Extract Assumption Differences

-> INVOKE: /assumption_extraction [Field A's approach to problems identified in Step 1]

For each structural analogy, what does Field A assume that Field B doesn't?
- What does Field A take for granted that Field B explicitly addresses?
- Where has Field B solved a problem that Field A still struggles with?
- What hidden beliefs prevent Field A from adopting Field B's approach?

**Output**: Assumption gaps between the fields, linked to specific analogies.

---

### Step 3: Test Transferability

-> INVOKE: /araw [each candidate analogy + assumption gaps]

For each analogy, test with ARAW:

**ASSUME RIGHT (analogy transfers)**:
- What would Field A gain by adopting this?
- What adaptation is needed?
- What evidence supports transfer?

**ASSUME WRONG (analogy doesn't transfer)**:
- What makes Field A fundamentally different here?
- What would go wrong if Field A copied Field B?
- What context-dependent factors break the analogy?

**Verdict for each**: TRANSFERS / PARTIALLY TRANSFERS / DOESN'T TRANSFER

**Output**: Each analogy with transfer verdict and reasoning.

---

### Step 4: Synthesize Actionable Insights

-> INVOKE: /insight_synthesis [all outputs from Steps 1-3]

Create the final report:

```
CROSS-DOMAIN REPORT: What [Field A] Can Learn From [Field B]
=============================================================

EXECUTIVE SUMMARY
- [Field B] has [N] practices that [Field A] could benefit from
- Top 3 transferable insights
- Key barriers to adoption

VALIDATED TRANSFERS (high confidence):
For each:
  - THE INSIGHT: What Field B does
  - WHY IT WORKS: The structural mechanism
  - HOW IT APPLIES: What Field A would do differently
  - ADAPTATION NEEDED: What changes for Field A's context
  - EXPECTED IMPACT: What would improve

PARTIAL TRANSFERS (needs adaptation):
For each:
  - What transfers and what doesn't
  - Required adaptations
  - Risks of naive adoption

NON-TRANSFERS (look similar but don't apply):
For each:
  - Why it looks like it would transfer
  - Why it actually doesn't
  - What's fundamentally different

IMPLEMENTATION ROADMAP:
  - Where to start (lowest risk, highest impact)
  - What to try next
  - What requires deeper investigation
```

-> COMPLETE

---

## Output Standards

- Readable by practitioners in EITHER field (no assumption of expertise in the other)
- Every claimed transfer includes the structural mechanism (not just "Field B does X, so should Field A")
- Non-transfers are explicitly identified (prevents naive copying)
- Implementation is concrete and actionable
- Validation status: "These analogies have not been validated by practitioners in either field"

---

## Quality Gates

After Step 1: If fewer than 3 structural analogies found, the fields may be too dissimilar. Consider a different Field B.

After Step 3: If most analogies are surface-only, the report should say so honestly rather than force transfers that don't exist.

---

## Example Usage

```
/cross_domain_report what software engineering can learn from aviation safety
/cross_domain_report what healthcare can learn from manufacturing quality control
/cross_domain_report what education can learn from game design
/cross_domain_report what business strategy can learn from evolutionary biology
/cross_domain_report what urban planning can learn from network engineering
```
