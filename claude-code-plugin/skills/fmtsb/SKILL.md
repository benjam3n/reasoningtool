---
name: "fmtsb - Formalize Make This Skill Because"
description: "Formalize a skill draft into production quality by enforcing schema completeness, overlap detection, dependency mapping, and rollout readiness."
output:
  format: "prose"
---

# FMTSB - Formalize Make This Skill Because

**Input**: $ARGUMENTS

---

## Core Principles

1. **Drafts are hypotheses, not skills.** A skill draft from `/mts` is a guess about what the skill should be. Formalization tests that guess against quality standards, existing library topology, and usability requirements.

2. **Schema enforcement is quality enforcement.** The schema isn't bureaucracy — each required element exists because skills without it fail in predictable ways. Missing failure modes = blind spots. Missing integration = orphan skill. Missing depth scaling = inconsistent output quality.

3. **Overlap is the default.** With 367 skills, most new skills overlap something. The question isn't "does this overlap?" but "is the overlap acceptable?" Acceptable overlap: different angle on same problem. Unacceptable: same angle, same problem, different name.

4. **Adoption requires discoverability.** A skill nobody can find is a skill that doesn't exist. Formalization must verify naming, categorization, and integration paths that make the skill findable.

5. **Dependencies are bidirectional.** What does this skill need from others? What do others need from this skill? Both directions must be mapped.

---

## Phase 1: Draft Assessment

Receive or generate the draft skill (from `/mts` or direct input).

```
[F1] DRAFT_SOURCE: [/mts output | direct input | existing skill being upgraded]
[F2] DRAFT_STATUS: [skeleton | partial | near-complete]
[F3] SKILL_ID: [proposed id]
[F4] SKILL_NAME: [proposed full name]
[F5] STATED_PURPOSE: [what the draft says it does]
```

---

## Phase 2: Schema Enforcement

Check the draft against the required schema. Every element must be present and substantive (not placeholder).

| Element | Status | Issue |
|---------|--------|-------|
| **Frontmatter** (name, description) | [PASS/FAIL/PARTIAL] | [if not PASS, what's wrong] |
| **Core Principles** (3-6, specific) | [PASS/FAIL/PARTIAL] | |
| **Phase structure** (numbered findings) | [PASS/FAIL/PARTIAL] | |
| **Finding prefix** (unique letter) | [PASS/FAIL/PARTIAL] | |
| **Output format** (structured) | [PASS/FAIL/PARTIAL] | |
| **Failure modes table** (≥4 entries) | [PASS/FAIL/PARTIAL] | |
| **Depth scaling table** (1x-8x) | [PASS/FAIL/PARTIAL] | |
| **Pre-completion checklist** (≥6 items) | [PASS/FAIL/PARTIAL] | |
| **Integration section** | [PASS/FAIL/PARTIAL] | |

```
[F6] SCHEMA_SCORE: [N of 9 elements PASS]
[F7] CRITICAL_GAPS: [list of FAIL elements]
[F8] QUALITY_GAPS: [list of PARTIAL elements]
```

### Quality Checks (beyond schema)

```
[F9] PRINCIPLES_CHECK: Are principles specific to this skill (not generic advice)? [YES/NO]
[F10] FAILURE_MODES_CHECK: Are failure modes based on real failure patterns (not hypothetical)? [YES/NO]
[F11] CHECKLIST_CHECK: Is every checklist item binary-checkable? [YES/NO]
[F12] DEPTH_CHECK: Does depth scaling specify measurable minimums? [YES/NO]
```

---

## Phase 3: Overlap Detection

Check the proposed skill against the existing library.

```
[F13] OVERLAP ANALYSIS:
| Existing Skill | Overlap Level | What Overlaps | What's Different |
|---------------|--------------|---------------|-----------------|
| /[id] | [none/low/medium/high/duplicate] | [area] | [area] |
| /[id] | [level] | [area] | [area] |
```

### Overlap Verdicts

- **DUPLICATE**: Same problem, same angle → REJECT: use or update existing skill
- **HIGH**: Same problem, different angle → JUSTIFY: explain why both should exist
- **MEDIUM**: Adjacent problem, some shared territory → ACCEPTABLE: note boundary
- **LOW/NONE**: Different problem → PROCEED

```
[F14] OVERLAP_VERDICT: [proceed | justify | reject]
[F15] OVERLAP_RATIONALE: [why this skill deserves to exist alongside overlapping ones]
```

---

## Phase 4: Dependency Mapping

```
[F16] INBOUND DEPENDENCIES (what feeds INTO this skill):
  - /[id] → this skill: [what it provides]
  - /[id] → this skill: [what it provides]

[F17] OUTBOUND DEPENDENCIES (what this skill feeds INTO):
  - this skill → /[id]: [what it provides]
  - this skill → /[id]: [what it provides]

[F18] COMPLEMENTARY SKILLS (good to use alongside):
  - /[id]: [why they complement each other]

[F19] FINDING_PREFIX_COLLISION: [does the prefix collide with existing skills? YES/NO]
```

---

## Phase 5: Rollout Readiness

```
[F20] DISCOVERABILITY:
  - Guessable name? [YES/NO — if NO, suggest alternatives]
  - In the right category? [which category]
  - Listed in CLAUDE.md tables? [which table it belongs in]
  - Integration pointers from related skills? [which skills should link to this one]

[F21] ADOPTION BARRIERS:
  - [barrier 1] — [how to address]
  - [barrier 2] — [how to address]

[F22] VALIDATION PLAN:
  - Test case 1: [input] → expected [output type]
  - Test case 2: [input] → expected [output type]
```

---

## Phase 6: Output

```
FORMALIZATION REPORT
====================

SKILL: /[id] — [name]
DRAFT_SOURCE: [source]

SCHEMA COMPLIANCE: [N/9] elements pass
CRITICAL_GAPS: [list or "none"]
QUALITY_GAPS: [list or "none"]

OVERLAP_VERDICT: [proceed | justify | reject]
OVERLAP_DETAIL: [key findings]

DEPENDENCIES:
  INBOUND: [list]
  OUTBOUND: [list]

ROLLOUT_READINESS: [ready | needs work]
BLOCKERS: [list or "none"]

FORMALIZED_SKILL: [complete SKILL.md content if ready, or gap list if not]

STATUS: READY_FOR_DEPLOY | NEEDS_REVISION
REVISION_ITEMS:
- [item 1]
- [item 2]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Rubber stamp** | Everything passes without scrutiny | Schema check must be element-by-element with evidence |
| **Overlap ignored** | No overlap analysis performed | Check at least 5 potentially overlapping skills |
| **Generic principles accepted** | "Be thorough" passes as a principle | Each principle must be specific to this skill's domain |
| **Placeholder elements** | "TBD" or "TODO" in schema elements | Every element must be substantive, not placeholder |
| **Missing dependencies** | Skill exists in isolation | Find at least 2 inbound and 2 outbound connections |
| **Name not tested** | ID accepted without guessability check | Ask: would someone looking for this skill try this name? |

---

## Depth Scaling

| Depth | Schema Elements Checked | Overlap Skills Compared | Dependencies Mapped | Test Cases |
|-------|------------------------|------------------------|--------------------|-----------|
| 1x | 5 | 3 | 2 | 1 |
| 2x | 9 (all) | 5 | 4 | 2 |
| 4x | 9 + quality checks | 8 | 6 | 3 |
| 8x | 9 + quality + style | 12 | All identified | 5 |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Draft assessed with source identified
- [ ] All 9 schema elements checked individually
- [ ] Quality checks performed (principles specific, failure modes real, checklist binary)
- [ ] Overlap analysis against at least 5 candidates
- [ ] Overlap verdict justified
- [ ] Inbound and outbound dependencies mapped
- [ ] Finding prefix checked for collisions
- [ ] Discoverability assessed (naming, categorization, integration links)
- [ ] Validation test cases defined
- [ ] Status is binary: READY_FOR_DEPLOY or NEEDS_REVISION with specific items

---

## Integration

- Use after: `/mts` (to formalize a draft)
- Use after: `/cs CREATE` (to quality-check a created skill)
- Differs from `/mts`: mts creates from scratch; fmtsb formalizes an existing draft
- Differs from `/pci`: pci improves many skills systematically; fmtsb formalizes one skill thoroughly
- Routes to: deployment (save to skills directory) or back to revision
