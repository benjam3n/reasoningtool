---
name: uaua
description: UAUA Combined Exploration - Universalize → ARAW → Universalize → ARAW. Combines complete space mapping with rigorous validation.
---

# UAUA - Universalize → ARAW → Universalize → ARAW

**Input**: $ARGUMENTS

---

## What is UAUA?

UAUA combines two complementary exploration methods:
- **Universalization**: Map the complete possibility space (divergent, Type logic)
- **ARAW**: Test specific claims rigorously (convergent, Boolean logic)

[O:source araw_2026-01-28_araw-vs-universalization.md]

**Why both?**
- Universalization alone: Complete but unvalidated
- ARAW alone: Validated but may miss dimensions
- UAUA: Complete AND validated

---

## Quick Decision: When to Use What

| Situation | Use |
|-----------|-----|
| Testing a specific claim | `/araw` |
| Exploring options | `/universalization` |
| Complex problem, high stakes | `/uaua` |
| Need both breadth and depth | `/uaua` |

---

## The UAUA Pattern

```
U1: UNIVERSALIZE (Map the space)
    ↓
A1: ARAW (Test top candidates)
    ↓
U2: UNIVERSALIZE (Find edge cases of survivors)
    ↓
A2: ARAW (Final validation)
    ↓
SYNTHESIS (What survived all rounds?)
```

---

## STEP U1: Universalize (Map the Space)

**Purpose**: Find the complete possibility space before testing anything.

### Apply 12 Techniques to Input

| # | Technique | Question |
|---|-----------|----------|
| 1 | STATE SPACE | What states could this be in? |
| 2 | INSTANCE-TO-CATEGORY | What is this an instance of? |
| 3 | PARAMETER VARIATION | What if parameters varied? |
| 4 | ROLE REVERSAL | What if roles reversed? |
| 5 | EXISTENCE CHECK | Does this exist/is this true? |
| 6 | CAUSAL REVERSAL | What if cause/effect reversed? |
| 7 | TEMPORAL VARIATION | What if timing varied? |
| 8 | BOUNDARY DISSOLUTION | What if scope changed? |
| 9 | MODALITY SHIFT | What certainty level? |
| 10 | PERSPECTIVE ROTATION | Whose view? |
| 11 | SCALE VARIATION | At what level? |
| 12 | NEGATION REFRAME | Problem or opportunity? |

### Output Format

```
U1: SPACE MAPPING
=================
Input: [original]

Universalizations:
1. [State space] → [what states found]
2. [Category] → [what category, what siblings]
3. [Parameters] → [what variations]
...

CANDIDATES for A1 (top 5 most promising):
1. [Candidate 1]
2. [Candidate 2]
3. [Candidate 3]
4. [Candidate 4]
5. [Candidate 5]

[T:result] U1 produced [N] universalizations, [M] candidates
```

---

## STEP A1: ARAW (Test Top Candidates)

**Purpose**: Rigorously test the most promising candidates from U1.

### For Each Candidate

```
CANDIDATE: [name]
│
├── ASSUME RIGHT (this candidate is best/valid)
│   ├── What evidence supports this?
│   ├── What follows if true?
│   └── What must also be true?
│
└── ASSUME WRONG (this candidate is flawed/invalid)
    ├── What evidence contradicts this?
    ├── What's the failure mode?
    └── What's a better alternative?
```

### Verdict for Each

| Verdict | Meaning | Next Action |
|---------|---------|-------------|
| VALIDATED | AR stronger than AW | Proceed to U2 |
| REJECTED | AW stronger than AR | Drop, record why |
| UNCERTAIN | Both AR and AW have merit | Proceed to U2, mark for deeper investigation |

### Output Format

```
A1: CANDIDATE TESTING
=====================

CANDIDATE 1: [name]
├── AR: [summary of assume-right findings]
├── AW: [summary of assume-wrong findings]
└── VERDICT: [VALIDATED/REJECTED/UNCERTAIN]
    Reason: [why]

[repeat for each candidate]

SUMMARY:
- VALIDATED: [list]
- REJECTED: [list with reasons]
- UNCERTAIN: [list]

[T:result] A1: [V] validated, [R] rejected, [U] uncertain
```

---

## STEP U2: Universalize (Find Edge Cases)

**Purpose**: Find edge cases and boundary conditions for survivors.

### For Each VALIDATED/UNCERTAIN Candidate

Apply universalization to find:
- **BOUNDARY**: Where does this break?
- **SCALE**: At what scale does it fail?
- **TEMPORAL**: When doesn't it apply?
- **STAKEHOLDER**: Who would disagree?
- **CONTEXT**: Under what conditions does it fail?

### Also for REJECTED Candidates

- **WHEN WOULD THEY WORK?** Under what conditions would rejected options become valid?
- This prevents premature rejection of contextually-valid options.

### Output Format

```
U2: EDGE CASE DISCOVERY
=======================

FOR VALIDATED: [Candidate name]
Edge cases found:
1. [Edge case 1] - When: [condition]
2. [Edge case 2] - When: [condition]

FOR REJECTED: [Candidate name]
Would work if: [conditions]

NOVEL INSIGHTS (not found in U1):
- [Insight 1]
- [Insight 2]

[T:result] U2 found [N] edge cases, [M] novel insights
```

---

## STEP A2: ARAW (Final Validation)

**Purpose**: Test edge cases and produce final validated output.

### For Each Edge Case

```
EDGE CASE: [description]
├── ASSUME RIGHT (edge case matters)
│   └── How does this change our validated candidates?
│
└── ASSUME WRONG (edge case doesn't matter)
    └── Why can we ignore this?
```

### Final Verdict for Each Original Candidate

| Status | Meaning |
|--------|---------|
| FINAL VALIDATED | Survived all rounds |
| VALID WITH CONDITIONS | Survived but only under specific conditions |
| FINAL REJECTED | Failed edge case testing |

### Output Format

```
A2: FINAL VALIDATION
====================

EDGE CASE TESTING:
[Edge case 1]:
├── AR: [if matters, impact is...]
├── AW: [can ignore because...]
└── VERDICT: [MATTERS/IGNORE]

FINAL STATUS:

CANDIDATE 1: [name]
├── Original status: [from A1]
├── Edge cases that matter: [list]
├── Final status: [VALIDATED/WITH CONDITIONS/REJECTED]
└── If WITH CONDITIONS: [specify conditions]

[repeat]

[T:result] Final: [V] validated, [C] conditional, [R] rejected
```

---

## STEP SYNTHESIS: What Survived?

### Summary Format

```
UAUA SYNTHESIS
==============

Original input: [input]

JOURNEY:
- U1 found [N] candidates
- A1 validated [V], rejected [R], uncertain [U]
- U2 found [E] edge cases
- A2 validated [F] final, [C] conditional

FINAL ANSWER:
1. [Best option] - VALIDATED
   Why: [reasoning]
   Conditions: [if any]

2. [Second option] - [VALIDATED/WITH CONDITIONS]
   Why: [reasoning]
   Conditions: [if any]

KEY INSIGHTS:
- [What U1 found that ARAW alone wouldn't]
- [What A1 found that Universalization alone wouldn't]
- [What U2 found that first pass missed]
- [What A2 validated/invalidated]

REMAINING UNCERTAINTY:
- [What's still unknown]

VERIFICATION:
- [T:result] UAUA complete: [F] final validated from [N] initial candidates
- [D:derivation] Final options derived through 4-step UAUA process
```

---

## Depth Scaling (2x, 4x, 8x, 16x)

UAUA supports depth scaling like ARAW. Higher depth = more iterations, more candidates, more edge cases.

### Depth Requirements

| Depth | Pattern | Min Candidates (U1) | Min Edge Cases (U2) | Min ARAW Levels | Min Output Lines |
|-------|---------|---------------------|---------------------|-----------------|------------------|
| **1x** | U → A | 5 | 3 | 3 | 400 |
| **2x** | U → A → U → A | 8 | 5 | 4 | 800 |
| **4x** | U → A → U → A (deep) | 12 | 8 | 5 | 1600 |
| **8x** | U → A → U → A → U → A | 18 | 12 | 6 | 3200 |
| **16x** | U → A → U → A → U → A → U → A | 25 | 18 | 7 | 6400 |

### How to Achieve ARAW Depth in A1/A2

For the ARAW phases (A1, A2), achieve tree depth using this technique:

1. **Every ASSUME RIGHT gets sub-claims** - Ask "What follows from this?" or "What must also be true?"
2. **Every sub-claim gets ASSUME WRONG** - Ask "What if this sub-claim is wrong?" or "What's an alternative?"
3. **Recurse: AR→AW→AR→AW** until you hit:
   - **Foundation** (questioning becomes circular)
   - **Prediction** (testable claim - note as [CRUX])
   - **Decision** (not a claim - extract underlying claim first)

**Example at 4x depth (5 levels):**
```
Candidate: X is the best approach
├── AR: X is best
│   ├── Sub-claim: X has property Y
│   │   ├── AR: Y is valuable
│   │   │   ├── Sub-claim: Y enables Z
│   │   │   │   └── AW: What if Z isn't needed? [LEVEL 5]
│   │   │   └── AW: Y might not be valuable because...
│   │   └── AW: X might not have Y because...
│   └── AW: Something else might have Y better
└── AW: X is not best because...
```

### Depth Detection

If user message contains depth signal, use that depth:
- "uaua 2x this problem" → 2x depth
- "uaua 8x" → 8x depth
- Just "uaua" → default 2x

### What Changes at Higher Depth

| Component | At 2x | At 8x |
|-----------|-------|-------|
| **U1 Techniques** | Apply 6-8 of 12 | Apply all 12 exhaustively |
| **U1 Candidates** | 5-8 candidates | 18+ candidates |
| **A1 Tree Depth** | 3-4 levels deep | 6-8 levels deep |
| **U2 Edge Cases** | 3-5 per candidate | 8-12 per candidate |
| **A2 Validation** | Key edge cases | All edge cases |
| **Iterations** | 1 full cycle | 3+ full cycles |

### Pre-Completion Check

Before finishing any UAUA, verify:
- [ ] Candidates count meets minimum for depth
- [ ] Edge cases count meets minimum for depth
- [ ] ARAW tree depth meets minimum
- [ ] Output length meets minimum
- [ ] All 4 steps (U1, A1, U2, A2) completed

**If ANY requirement not met: Continue analysis, do NOT submit.**

### Save Requirement

Every UAUA at 2x+ depth must be saved to `library/araw/sessions/uaua_[date]_[topic].md`

---

## Example: "Should I take this job offer?"

### U1: Map the Space

```
Input: "Should I take this job offer?"

Universalizations:
1. Instance-to-category: "career decision" → siblings: stay, negotiate, other jobs
2. Parameter variation: salary, role, location, timing all variable
3. Temporal: now vs later vs never
4. Stakeholder: family, current employer, future self

CANDIDATES:
1. Accept the offer as-is
2. Negotiate the offer
3. Decline and stay at current job
4. Decline and seek other offers
5. Request time to decide
```

### A1: Test Candidates

```
CANDIDATE 1: Accept as-is
├── AR: Growth opportunity, higher pay
├── AW: May be leaving money on table, unknown culture
└── VERDICT: UNCERTAIN (should try negotiating first)

CANDIDATE 2: Negotiate
├── AR: Higher compensation likely, shows confidence
├── AW: Could lose offer if aggressive
└── VERDICT: VALIDATED (low downside, high upside)

[etc.]
```

### U2: Edge Cases

```
FOR VALIDATED: Negotiate
Edge cases:
1. Offer rescinded → rare but possible
2. They don't negotiate → accept anyway?
3. Counter lower than expected → accept floor?
```

### A2: Final Validation

```
EDGE CASE: Offer rescinded during negotiation
├── AR (matters): Would be devastating
├── AW (ignore): Very rare, professional negotiation is expected
└── VERDICT: IGNORE (standard practice)

FINAL STATUS:
- Negotiate → VALIDATED (standard professional behavior)
- Accept as-is → VALID WITH CONDITIONS (only if negotiation fails)
```

### Synthesis

```
FINAL ANSWER:
1. NEGOTIATE the offer - this is expected professional behavior with high upside
2. If negotiation fails, ACCEPT as-is - the opportunity is valuable
3. Define your walkaway number before negotiating

KEY INSIGHT: Binary "accept/decline" framing missed the negotiate option that UAUA found.
```

---

## When UAUA is Overkill

Don't use UAUA for:
- Simple, reversible decisions → Use ARAW-Lite
- Pure exploration with no validation needed → Use Universalization only
- Pure validation with known options → Use ARAW only

**UAUA is for**: Complex decisions where you need BOTH complete option coverage AND rigorous validation.

---

## Verification Checklist

Before completing UAUA:

- [ ] U1 applied at least 6 of 12 universalization techniques
- [ ] U1 generated at least 5 candidates
- [ ] A1 tested all candidates with full AR/AW
- [ ] U2 found at least 2 edge cases
- [ ] A2 tested edge cases
- [ ] Synthesis explains what each step added
- [ ] Final answer has clear validation rationale

[T:result] Checklist complete: all verification items satisfied
