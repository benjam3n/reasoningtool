---
name: "cs - Create Skill"
description: "Create, update, or gap-scan skills. Three modes: CREATE produces a new SKILL.md, UPDATE improves an existing one, GAP_SCAN identifies missing skills."
output:
  format: "prose"
---

# CS - Create Skill

**Input**: $ARGUMENTS

---

## Core Principles

1. **Mode determines method.** CREATE, UPDATE, and GAP_SCAN are fundamentally different operations. CREATE starts from a problem. UPDATE starts from existing content. GAP_SCAN starts from the library topology. Don't blend them.

2. **CREATE requires a problem statement.** "Make a skill for X" is insufficient. What problem does the user currently solve by improvising? What goes wrong when they improvise? That failure pattern is the skill's reason to exist.

3. **UPDATE must preserve what works.** The most common update failure is breaking working elements while fixing broken ones. Read the existing skill thoroughly, identify what's good, protect it.

4. **GAP_SCAN requires library knowledge.** You can't find gaps without knowing what's there. A gap is not "I can't find it" — it's "the library provably lacks coverage for this need class."

5. **Output contracts are non-negotiable.** Every skill must specify what it produces. A skill without an output format is a suggestion, not a tool.

---

## Phase 1: Mode Detection

```
[C1] INPUT_TYPE: [new skill request | existing skill to improve | library analysis request]
[C2] MODE: CREATE | UPDATE | GAP_SCAN
[C3] MODE_EVIDENCE: [why this mode was selected]
```

### Mode Signals

| Signal | Mode |
|--------|------|
| "Make a skill for..." / "I need a skill that..." | CREATE |
| "This skill isn't good enough" / "Improve /skill" | UPDATE |
| "What skills am I missing?" / "What gaps exist?" | GAP_SCAN |
| Skill ID provided + complaint | UPDATE |
| Domain described + no existing skill matches | CREATE |

---

## Mode: CREATE

### Phase 2C: Problem Definition

```
[C4] PROBLEM: [what the user currently solves by improvising]
[C5] FAILURE_WITHOUT_SKILL: [what goes wrong without a structured approach]
[C6] TRIGGER: [when would someone reach for this skill?]
[C7] INPUT: [what the skill receives]
[C8] OUTPUT: [what the skill produces]
[C9] SCOPE_BOUNDARY: [what this skill does NOT do]
```

### Phase 3C: Overlap Check

```
[C10] OVERLAP SCAN:
| Existing Skill | Overlap | Distinct Because |
|---------------|---------|-----------------|
| /[id] | [level] | [reason] |
```

If HIGH overlap found: recommend UPDATE on existing skill instead of CREATE.

### Phase 4C: Skill Generation

Generate the complete SKILL.md following the quality schema:
- Frontmatter (name, description)
- Core Principles (3-6, specific to domain)
- Phase structure with numbered findings
- Output format
- Failure modes (≥4)
- Depth scaling (1x-8x)
- Pre-completion checklist (≥6)
- Integration section

```
[C11] GENERATED_SKILL: [complete SKILL.md content]
[C12] PROPOSED_ID: [2-6 char, guessable]
[C13] PROPOSED_NAME: [full name]
```

---

## Mode: UPDATE

### Phase 2U: Current State Assessment

```
[C14] SKILL_TO_UPDATE: /[id]
[C15] CURRENT_LINE_COUNT: [N lines]
[C16] CURRENT_QUALITY_TIER: [stub | partial | adequate | good | excellent]
```

### Phase 3U: Gap Analysis

Check the existing skill against schema requirements:

```
[C17] SCHEMA COMPLIANCE:
| Element | Status | Gap |
|---------|--------|-----|
| Core Principles | [present/missing/weak] | [what needs fixing] |
| Phase structure | [present/missing/weak] | |
| Failure modes | [present/missing/weak] | |
| Depth scaling | [present/missing/weak] | |
| Checklist | [present/missing/weak] | |
| Integration | [present/missing/weak] | |
```

### Phase 4U: Preservation + Improvement

```
[C18] PRESERVE (do not change):
  - [element] — [why it works]
  - [element] — [why it works]

[C19] IMPROVE:
  - [element] — [current state] → [target state]
  - [element] — [current state] → [target state]

[C20] ADD:
  - [element] — [why it's missing and needed]

[C21] UPDATED_SKILL: [complete updated SKILL.md content]
```

---

## Mode: GAP_SCAN

### Phase 2G: Library Analysis

```
[C22] SCAN_SCOPE: [full library | specific category | specific domain]
[C23] ANALYSIS_METHOD: [category coverage | user-need mapping | workflow gap | domain gap]
```

### Phase 3G: Gap Identification

```
[C24] GAPS FOUND:
| Gap | Need Class | Nearest Existing | Why Insufficient | Priority |
|-----|-----------|-----------------|-----------------|----------|
| [gap 1] | [need] | /[id] | [why] | [high/medium/low] |
| [gap 2] | [need] | /[id] | [why] | [priority] |
```

### Phase 4G: Recommendations

```
[C25] RECOMMENDATIONS:
1. CREATE /[proposed-id] — [purpose] — PRIORITY: [level]
2. CREATE /[proposed-id] — [purpose] — PRIORITY: [level]
...
```

---

## Output

For CREATE/UPDATE: complete SKILL.md content ready to save.
For GAP_SCAN: prioritized gap list with proposed skill specs.

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Mode confusion** | Applying CREATE logic to an UPDATE request | Phase 1 mode detection must be explicit |
| **No problem statement** | CREATE with "make a skill for X" and no failure pattern | Go back: what goes wrong without this skill? |
| **Update destroys content** | Working elements removed during improvement | Phase 4U PRESERVE list must be explicit |
| **Duplicate creation** | New skill overlaps existing one at HIGH level | Overlap check before generation |
| **Gap inflation** | GAP_SCAN finds 50 "gaps" — most are marginal | Prioritize ruthlessly; only HIGH priority gaps warrant new skills |
| **Stub output** | Generated skill is under 100 lines | Quality gate: ≥100 lines, all schema elements present |

---

## Depth Scaling

| Depth | Mode | Min Elements | Min Overlap Checks | Min Output Length |
|-------|------|-------------|--------------------|-----------------|
| 1x | Any | Schema basics | 3 | 80 lines |
| 2x | Any | Full schema | 5 | 120 lines |
| 4x | Any | Schema + quality | 8 | 180 lines |
| 8x | Any | Schema + quality + style | 12 | 250 lines |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Mode correctly identified with evidence
- [ ] For CREATE: problem statement exists (not just "make a skill for X")
- [ ] For CREATE: overlap check completed
- [ ] For UPDATE: existing skill read thoroughly
- [ ] For UPDATE: PRESERVE list explicit
- [ ] For GAP_SCAN: scan scope defined
- [ ] For GAP_SCAN: gaps prioritized (not just listed)
- [ ] Output skill meets schema requirements
- [ ] Output skill has ≥100 lines
- [ ] Integration section connects to existing skills

---

## Integration

- Use from: `/dtse` (when skill doesn't exist), `/pci` (when skill needs improvement)
- Differs from `/mts`: mts focuses on initial creation; cs handles CREATE/UPDATE/GAP_SCAN
- Differs from `/fmtsb`: fmtsb formalizes a draft; cs creates or updates the skill itself
- Differs from `/sc`: sc designs creation systems; cs executes creation/update for one skill
