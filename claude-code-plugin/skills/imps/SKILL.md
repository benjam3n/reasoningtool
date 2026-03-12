---
name: "imps - Improve Skill"
description: "Systematically improve a single skill by diagnosing its weaknesses against the quality standard, generating specific fixes, applying them, and verifying the result meets all structural and content requirements."
output:
  format: "prose"
---

# Improve Skill

**Input**: $ARGUMENTS

---

## Core Principles

1. **Read before diagnosing.** Never improve a skill you haven't read in full. The most common failure is proposing generic improvements to a skill whose actual content you don't understand. Read every line before generating a single critique.

2. **The quality standard is objective, not aesthetic.** A skill is good or bad relative to specific structural requirements: core principles, failure modes table, depth scaling table, pre-completion checklist, integration section. Missing elements are defects, not style choices.

3. **Content quality is domain-specific.** Generic principles ("be thorough", "consider alternatives") indicate a skill that doesn't understand its own domain. Good principles name specific failure modes and specific interventions that only apply to THIS skill's problem space.

4. **Improvement means closing gaps, not rewriting from scratch.** If a skill has strong content but missing structure, add the structure. If it has good structure but generic content, sharpen the content. Identify what's weak and fix THAT — don't destroy what works.

5. **The exemplar skills define the floor.** Skills like `/foht` (300 lines), `/sbfow` (279 lines), `/iterate` (373 lines), `/araw` (410 lines) represent the quality standard. Any improved skill must be comparable in depth, specificity, and structural completeness.

---

## Phase 1: Read and Baseline

Read the target skill completely.

```
[I1] SKILL: /[name]
[I2] CURRENT_LINES: [line count]
[I3] CURRENT_STRUCTURE: [list which standard elements exist and which are missing]
```

### Structural Audit

Check for each required element:

| Element | Present? | Quality |
|---------|----------|---------|
| Frontmatter (name, description) | | |
| Core Principles (3-6, domain-specific, non-generic) | | |
| Multi-phase structure with lettered findings | | |
| Failure Modes table (Failure / Signal / Fix) | | |
| Depth Scaling table (1x/2x/4x/8x with floors) | | |
| Pre-Completion Checklist (6+ binary items) | | |
| Integration section (use from, routes to, differs from) | | |

---

## Phase 2: Content Diagnosis

Evaluate content quality beyond structure.

```
[I4] PRINCIPLES_QUALITY: [are principles domain-specific or generic platitudes?]
     GENERIC_PRINCIPLES: [list any that could apply to ANY skill — these need replacement]
     MISSING_INSIGHTS: [what domain-specific knowledge is absent?]

[I5] PHASE_QUALITY: [do phases have concrete steps or vague instructions?]
     VAGUE_PHASES: [list any that say "analyze" or "consider" without specifying HOW]
     MISSING_PHASES: [what steps are implied but not explicit?]

[I6] FAILURE_MODES_QUALITY: [are failure modes specific to this skill's domain?]
     GENERIC_FAILURES: [list any that apply to everything — "didn't think hard enough"]
     MISSING_FAILURES: [what domain-specific failures are unaddressed?]

[I7] OUTPUT_QUALITY: [is the output format specific and useful?]
     MISSING_OUTPUT: [what should the output include that it doesn't?]
```

### Content Quality Tests

| Test | Pass Criteria |
|------|--------------|
| **Disagreement test** | Could a thoughtful person disagree with any principle? If not, it's too generic |
| **Domain test** | Would removing the skill name make the principles unrecognizable? They should be identifiable |
| **Specificity test** | Do phases say WHAT to do, not just "analyze this"? |
| **Failure test** | Are failure modes things that actually go wrong with THIS type of task? |
| **Actionability test** | Could someone follow this skill and produce output without improvising? |

---

## Phase 3: Improvement Plan

Generate specific fixes, not vague suggestions.

```
[I-N] FIX: [specific change]
     TYPE: [structural | content | integration | clarity]
     PRIORITY: [critical | important | nice-to-have]
     CURRENT: [what exists now — quote or describe]
     PROPOSED: [what should replace it — be specific]
     RATIONALE: [why this improves the skill]
```

### Fix Priority Rules

- **Critical**: Missing required structural element (no failure modes table, no depth scaling)
- **Critical**: Generic principles that could apply to any skill
- **Important**: Vague phases that don't specify concrete steps
- **Important**: Missing domain-specific failure modes
- **Nice-to-have**: Formatting improvements, better examples, additional integration links

---

## Phase 4: Apply Fixes

Write the improved skill. Apply all critical and important fixes. Apply nice-to-haves if they don't bloat.

### Application Rules

- Preserve existing content that's already good — don't rewrite what works
- Add missing structural elements in their standard positions
- Replace generic principles with domain-specific ones
- Ensure the improved skill is 150-300 lines (the quality range)
- Verify every phase has concrete, followable steps

---

## Phase 5: Verify

Re-run the structural audit and content diagnosis on the improved version.

```
[I-N] VERIFICATION:
     STRUCTURAL_GAPS_REMAINING: [should be zero]
     GENERIC_CONTENT_REMAINING: [should be zero]
     LINE_COUNT: [should be 150-300]
     ALL_TESTS_PASS: [disagreement, domain, specificity, failure, actionability]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Full rewrite of good content** | Existing strong sections get replaced with generic versions | Read carefully. Preserve what works. Only fix what's broken |
| **Generic improvements** | "Made the principles more thorough" without specifics | Every fix must be a specific change with current/proposed |
| **Structure without content** | Added all tables and sections but they're empty or generic | Structure is necessary but not sufficient. Content must be domain-specific |
| **Bloat** | Skill went from 20 lines to 400 lines of filler | Quality range is 150-300 lines. Density matters more than length |
| **Lost voice** | Original skill had a distinctive approach that was smoothed away | Identify what's distinctive about the skill and preserve it |
| **Improvement without diagnosis** | Jumped to rewriting without identifying what's actually wrong | Always diagnose first. The fix must match the actual problem |
| **Ceremonial checklist** | Pre-completion checklist items that are always true or unverifiable | Each item must be binary and falsifiable |

---

## Depth Scaling

| Depth | Diagnosis | Fixes | Verification |
|-------|----------|-------|-------------|
| 1x | Structural audit only | Critical fixes only | Quick check |
| 2x | Structural + content diagnosis | Critical + important | Full re-audit |
| 4x | Full diagnosis + comparison to exemplars | All fixes + domain research | Full + exemplar comparison |
| 8x | Full + user testing simulation | All + iterative refinement | Full + adversarial review |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Target skill read in full before any diagnosis
- [ ] Structural audit completed with all elements checked
- [ ] Content diagnosis identifies specific (not generic) issues
- [ ] Every fix has current/proposed/rationale
- [ ] Critical fixes all applied
- [ ] Improved skill has all required structural elements
- [ ] Improved skill principles pass the domain test
- [ ] Line count is in the 150-300 range
- [ ] Verification confirms zero structural gaps

---

## Integration

- Use from: skill maintenance, quality audits, skill expansion tasks
- Routes to: `/w` (if skill needs actual prose improvement), `/cs` (if skill needs structural rework)
- Complementary: `/impss` (improves multiple skills), `/imprt` (auto-identifies what to improve)
- Differs from `/cs`: cs creates new skills; imps improves existing ones
- Differs from `/impss`: impss handles batches; imps handles one skill deeply
- Differs from `/fmtsb`: fmtsb formalizes drafts into production; imps improves already-production skills
