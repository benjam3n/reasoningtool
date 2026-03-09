---
name: "impss - Improve Skills (Batch)"
description: "Systematically improve multiple skills by triaging them against the quality standard, prioritizing by severity and impact, and applying /imps to each in the optimal order."
---

# Improve Skills (Batch)

**Input**: $ARGUMENTS

---

## Core Principles

1. **Triage before treatment.** With multiple skills to improve, the first step is assessment — not jumping into the worst one. Some skills are stubs needing full expansion. Some are missing one structural element. Some are fine. Triage separates these categories before any work begins.

2. **Severity and impact determine order.** A stub skill used by 10 other skills is higher priority than a fully-developed skill with a minor formatting issue. Severity (how broken) × impact (how used) = priority. Not all improvements are equal.

3. **Batch improvement reveals systemic patterns.** If 15 skills are all missing failure modes tables, that's not 15 individual problems — it's one systemic gap. Identify patterns across the batch to work efficiently, but still fix each skill individually.

4. **Quality is measured against a known standard.** The exemplar skills (foht, sbfow, iterate, araw) define the floor. Every skill in the batch is measured against the same structural and content requirements. No grading on a curve.

5. **One at a time, in priority order.** Even in batch mode, each skill gets individual attention via `/imps`. Batch mode handles triage, prioritization, and tracking — not parallel shortcuts that sacrifice quality.

---

## Phase 1: Identify Targets

```
[B1] SOURCE: [how targets were identified — user specified, date range, category, quality scan]
[B2] TARGET_COUNT: [N skills to evaluate]
[B3] TARGET_LIST: [skill names]
```

If targets aren't specified, scan for skills matching criteria:
- Below line count threshold (< 100 lines)
- Missing required structural elements
- Created in a specific date range
- In a specific category

---

## Phase 2: Triage

For each target skill, perform a rapid assessment:

```
[B-N] SKILL: /[name]
     LINES: [count]
     SEVERITY: [stub | partial | structural-gap | content-gap | minor | fine]
     MISSING_ELEMENTS: [list of missing structural elements]
     CONTENT_QUALITY: [generic | adequate | strong]
     USED_BY: [how many other skills invoke this one]
     PRIORITY_SCORE: [severity × impact]
```

### Severity Classification

| Severity | Criteria | Typical Lines |
|----------|----------|--------------|
| **Stub** | Essentially a placeholder — title and 3-5 vague steps | < 30 |
| **Partial** | Some content but missing multiple structural elements | 30-80 |
| **Structural gap** | Good content but missing 1-2 required elements | 80-150 |
| **Content gap** | Has structure but content is generic/shallow | 100-200 |
| **Minor** | Mostly complete, needs polish or one small fix | 150-250 |
| **Fine** | Meets quality standard — no improvement needed | 150-300+ |

---

## Phase 3: Pattern Detection

Before fixing individual skills, identify systemic issues:

```
[B-N] PATTERN: [systemic issue across multiple skills]
     AFFECTED: [which skills share this issue]
     COUNT: [how many]
     FIX_APPROACH: [how to address this pattern efficiently]
```

### Common Patterns

| Pattern | Signal | Approach |
|---------|--------|---------|
| **Missing failure modes** | N skills have no failure modes table | Create a template, customize per skill |
| **Generic principles** | N skills have "be thorough" type principles | Replace with domain-specific principles one at a time |
| **No depth scaling** | N skills have no scaling table | Add standard 1x/2x/4x/8x table, customize thresholds |
| **Missing integration** | N skills don't say how they connect to others | Map the integration links for the batch |
| **Uniform era** | All were created on the same date | Likely same systemic weakness from that generation pass |

---

## Phase 4: Priority Queue

Order skills for improvement:

```
IMPROVEMENT QUEUE (priority order)
  1. /[skill] — SEVERITY: [level] — REASON: [why first]
  2. /[skill] — SEVERITY: [level] — REASON: [why second]
  ...

ESTIMATED_EFFORT:
  Stubs to expand: [N] — ~200 lines each
  Structural gaps: [N] — ~50 lines to add each
  Content gaps: [N] — rewrite of specific sections
  Minor fixes: [N] — quick edits
  Already fine: [N] — skip
```

---

## Phase 5: Execute

For each skill in priority order:

```
→ INVOKE: /imps [skill name]
```

After each skill is improved, update tracking:

```
[B-N] COMPLETED: /[skill]
     WAS: [severity level, line count]
     NOW: [line count, all elements present]
     FIXES_APPLIED: [summary]
```

---

## Phase 6: Batch Summary

```
BATCH IMPROVEMENT SUMMARY
=========================

TOTAL EVALUATED: [N]
IMPROVED: [N]
SKIPPED (already fine): [N]
SYSTEMIC PATTERNS FOUND: [N]

IMPROVEMENTS:
  /[skill]: [old lines] → [new lines] — [summary]
  /[skill]: [old lines] → [new lines] — [summary]
  ...

REMAINING ISSUES: [anything that couldn't be fixed in this pass]

READY FOR:
- /imprt — to auto-identify what else needs improvement
- /skgap — to find missing skills
- /imps [specific] — to deep-dive any individual skill further
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **No triage** | Jumped into fixing the first skill without assessing the batch | Always triage the full set before fixing any individual skill |
| **Parallel quality sacrifice** | Tried to fix 5 skills simultaneously, all came out mediocre | One at a time via /imps. Batch mode handles triage and tracking, not execution |
| **Pattern blindness** | Fixed the same issue 15 times without noticing it was systemic | Run pattern detection before individual fixes |
| **Wrong priority order** | Fixed minor issues in rarely-used skills while stubs remained | Severity × impact = priority. Stubs in high-use skills come first |
| **Scope creep** | Started improving skills not in the original target set | Stick to the identified targets. New discoveries go in a future batch |
| **Quantity over quality** | "Improved" 30 skills but none actually meet the standard | Each skill must pass the /imps verification. Don't count incomplete fixes |

---

## Depth Scaling

| Depth | Triage | Pattern Analysis | Execution | Verification |
|-------|--------|-----------------|-----------|-------------|
| 1x | Quick line-count scan | Skip | Critical fixes only | Spot check |
| 2x | Full structural audit | Basic patterns | All critical + important | Each skill verified |
| 4x | Full + content diagnosis | Full pattern analysis | All fixes | Full + cross-skill consistency |
| 8x | Full + exemplar comparison | Full + root cause | All + iterative refinement | Full + regression testing |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All target skills identified and listed
- [ ] Triage completed for every target (severity, missing elements, priority)
- [ ] Systemic patterns identified before individual fixes
- [ ] Priority queue ordered by severity × impact
- [ ] Each improved skill verified individually via /imps
- [ ] Batch summary includes before/after for each skill
- [ ] No skills "improved" without meeting the quality standard

---

## Integration

- Use from: quality audits, post-generation cleanup, era-based improvement sweeps
- Routes to: `/imps` (for each individual skill), `/imprt` (auto-identify improvement targets)
- Complementary: `/skgap` (finds missing skills; impss improves existing ones)
- Differs from `/imps`: imps handles one skill deeply; impss handles triage and batch orchestration
- Differs from `/imprt`: imprt auto-identifies what needs improvement; impss executes the improvements
- Differs from `/cs`: cs creates new skills; impss improves existing batches
