---
name: "val - Validation"
description: "Verify that an output meets its requirements through systematic criteria checking, coverage scoring, and gap analysis."
---

# Validation

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Requirements validation**: The user has a deliverable and a set of requirements, and wants to verify the deliverable meets those requirements systematically.
**Interpretation 2 — Self-assessment**: The user has completed work and wants to check its quality against implicit or explicit standards before sharing it.
**Interpretation 3 — Acceptance testing**: The user is receiving work from someone else and wants a structured way to decide whether to accept or reject it.

If ambiguous, ask: "I can help with requirements validation, self-assessment of your own work, or acceptance testing of someone else's work — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Requirements before validation.** You cannot validate without knowing what to validate against. If requirements are missing, derive them from the deliverable's purpose. If the purpose is unclear, ask.

2. **"Met" requires evidence.** Checking a box without pointing to specific evidence in the deliverable is not validation — it's optimism. Every "met" finding must cite where and how the requirement is satisfied.

3. **Critical requirements are not negotiable.** A deliverable that meets 90% of requirements but misses a critical one has failed. Criticality weighting prevents the coverage score from hiding important gaps.

4. **Partial credit is information, not a pass.** "Partially met" means the requirement is addressed but not fully satisfied. This is useful diagnostic information — it tells you how much work remains — but it's not a pass.

5. **Validation is not improvement.** The job is to determine whether requirements are met, not to fix them. Recommendations come after validation, not during it. Keep the assessment clean before adding suggestions.

6. **Derived requirements need confirmation.** When requirements aren't stated, you must derive them from context. But derived requirements are hypotheses — confirm them with the user before treating them as ground truth.

---

## Procedure

### Phase 1: Gather Inputs

```
VALIDATION SETUP:
Target: [what is being validated]
Requirements source: [stated / derived / inferred]
Total requirements: [N]
Criticality levels: [which are critical / important / nice-to-have]
```

If requirements are not provided:
1. Identify the deliverable's purpose
2. Derive requirements from the purpose
3. Classify each as critical / important / nice-to-have
4. Confirm derived requirements are reasonable

### Phase 2: Check Each Requirement

For each requirement:

```
REQUIREMENT CHECK:

R[N]: [requirement text]
CRITICALITY: critical / important / nice-to-have
LOCATION: [where in the target this should be satisfied]
EVIDENCE: [specific evidence of satisfaction, or specific gap]
STATUS: met / partially met / not met
NOTES: [any qualifications]
```

**Status definitions:**
- **Met**: Requirement fully satisfied, evidence is clear and specific
- **Partially met**: Requirement addressed but incomplete — state what's present and what's missing
- **Not met**: Requirement not addressed, or addressed incorrectly — state what's expected vs what exists

### Phase 3: Calculate Coverage

```
COVERAGE CALCULATION:

| Status | Count | Weight | Score |
|--------|-------|--------|-------|
| Met | [N] | 1.0 | [N] |
| Partially met | [N] | 0.5 | [N*0.5] |
| Not met | [N] | 0.0 | 0 |

Raw coverage: [sum] / [total] = [%]

CRITICALITY-WEIGHTED COVERAGE:
Critical requirements met: [N] / [total critical] = [%]
Important requirements met: [N] / [total important] = [%]
Nice-to-have requirements met: [N] / [total nice-to-have] = [%]
```

### Phase 4: Determine Overall Result

**Pass criteria:**
- **PASS**: All critical requirements met AND overall coverage >= 90%
- **CONDITIONAL PASS**: All critical requirements met AND coverage 70-90% (gaps are non-critical)
- **PARTIAL**: Some critical requirements partially met OR coverage 50-70%
- **FAIL**: Any critical requirement not met OR coverage < 50%

```
VERDICT: [PASS / CONDITIONAL PASS / PARTIAL / FAIL]
RATIONALE: [why this verdict]
```

### Phase 5: Gap Analysis and Recommendations

For each gap (partially met or not met):

```
GAP ANALYSIS:

R[N]: [requirement]
STATUS: [partially met / not met]
GAP: [specific description of what's missing]
IMPACT: [what this gap means for the deliverable's purpose]
FIX: [specific action to close the gap]
EFFORT: [estimated effort — trivial / moderate / significant]
```

```
VALIDATION REPORT:

Target: [what was validated]
Verdict: [PASS / CONDITIONAL / PARTIAL / FAIL]
Coverage: [raw %] (critical: [%], important: [%])

REQUIREMENTS MET: [list with evidence pointers]

GAPS:
1. R[N]: [requirement] — [gap] — Fix: [action] — Effort: [level]
2. ...

RECOMMENDED ACTIONS (by priority):
1. [Critical gaps first]
2. [Important gaps second]
3. [Nice-to-have gaps last]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Validating without requirements** | "It seems good" without criteria | Derive requirements from purpose, then validate against them |
| **Evidence-free "met"** | Checkboxes ticked without pointing to specifics | Every "met" must cite where the requirement is satisfied |
| **Coverage hiding critical gaps** | 85% coverage but critical requirement not met | Use criticality-weighted scoring; any critical gap = FAIL regardless of overall score |
| **Derived requirements treated as given** | Requirements invented without confirmation | When deriving requirements, flag them as derived and confirm |
| **Fixing during validation** | Improving the work instead of assessing it | Validate first, recommend fixes second — keep phases separate |
| **Partial credit as pass** | "Partially met" counted as good enough | Partial credit is information; accumulate it but don't treat it as meeting the requirement |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Quick — check critical requirements only | Critical reqs checked, pass/fail verdict |
| **2x** | Standard — all requirements checked, coverage calculated | Full validation table, coverage score, verdict |
| **4x** | Thorough — all requirements with evidence, gap analysis, recommendations | Complete validation report with evidence, gaps, and fix actions |
| **8x** | Exhaustive — full validation + derived requirements confirmed + fix effort estimated + regression analysis | Complete report + derived reqs confirmed + effort estimates + risk of fixes |

---

## Pre-Completion Checklist

- [ ] Requirements identified (stated or derived with confirmation)
- [ ] Each requirement has criticality level assigned
- [ ] Each requirement checked with specific evidence
- [ ] Coverage calculated (raw and criticality-weighted)
- [ ] Verdict stated with rationale
- [ ] Gaps described specifically (not just "not met")
- [ ] Recommended actions are specific and prioritized by criticality
- [ ] No "met" without evidence

---

## Integration

- **Use from**: /evaluate (when evaluation requires formal requirements checking), /create (validate created content against criteria), /how (validate plan against objectives)
- **Routes to**: /how (when gaps need fixing — find the method), /fla (failure anticipation for unmet critical requirements), /mv (MECE check of requirements list)
- **Differs from**: /vp (full verification and testing procedure — more comprehensive, includes test design and execution), /evaluate (broader assessment, /val is specifically requirements-based), /ver (GOSM verification for individual claims, /val for deliverable-level validation)
- **Complementary**: /av (verify assumptions behind requirements), /mv (check if requirements are MECE), /pv (procedure validation as a complement to deliverable validation)
