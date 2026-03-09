---
name: "sc - Skill Creation System"
description: "Design skill creation pipelines at scale, including quality gates, templates, naming conventions, batch generation, review processes, and rollout strategy."
---

# SC - Skill Creation System

**Input**: $ARGUMENTS

---

## Core Principles

1. **Systems, not individual skills.** This skill designs the FACTORY, not the product. `/mts` makes one skill. `/sc` designs the process for making many skills consistently.

2. **Quality gates prevent stub proliferation.** Without gates, batch creation produces stubs — 10-line files that look like skills but lack substance. The Mar 6 batch problem: 34 skills at 10-21 lines each. Gates must catch this.

3. **Templates constrain variance, not creativity.** A good template ensures structural consistency (every skill has principles, phases, failure modes) while allowing content to vary. Templates that constrain content produce cookie-cutter skills.

4. **Naming conventions scale.** With 367 skills, naming is a system problem. Conventions must handle abbreviation rules, collision detection, guessability testing, and alias support.

5. **Review is not optional.** Batch-created skills have lower average quality than individually crafted ones. The review pipeline must catch defects before deployment, not after.

---

## Phase 1: System Definition

```
[S1] CREATION_OBJECTIVE: [why are we creating skills? What gap in the library?]
[S2] VOLUME_TARGET: [how many skills? In what timeframe?]
[S3] QUALITY_TARGET: [what quality tier? What's the minimum acceptable standard?]
[S4] SOURCE_MATERIAL: [where do skill concepts come from? Extraction? User requests? Gap analysis?]
```

---

## Phase 2: Schema and Template

### Schema Definition

Define what every skill MUST contain:

```
[S5] REQUIRED SCHEMA:
| Element | Required | Min Threshold |
|---------|----------|--------------|
| Frontmatter (name, description) | Yes | Name + 1-sentence description |
| Core Principles | Yes | 3 minimum, each specific to domain |
| Phase structure | Yes | 2+ phases with numbered findings |
| Finding prefix | Yes | Unique letter, no collisions |
| Output format | Yes | Structured, not prose |
| Failure modes | Yes | 4 minimum, with signal and fix |
| Depth scaling | Yes | 4 tiers (1x/2x/4x/8x) |
| Pre-completion checklist | Yes | 6 minimum, binary-checkable |
| Integration | Yes | 2+ connection points |
```

### Template

```
[S6] TEMPLATE STRUCTURE:
  ---
  name: "[id] - [Full Name]"
  description: "[one-sentence description]"
  ---

  # [Full Name]

  **Input**: $ARGUMENTS

  ---

  ## Core Principles
  [3-6 principles, specific to domain, counterintuitive]

  ## Phase 1: [Name]
  [numbered findings with prefix]

  ## Phase N: Output
  [structured format]

  ## Failure Modes
  [table with 4+ entries]

  ## Depth Scaling
  [1x/2x/4x/8x table]

  ## Pre-Completion Checklist
  [6+ binary items]

  ## Integration
  [connection points]
```

---

## Phase 3: Naming Convention

```
[S7] NAMING RULES:
  - Length: 2-6 characters
  - Type: mnemonic abbreviation of function
  - Collision check: against full registry before assignment
  - Guessability test: would someone with this problem try this name?
  - Alias support: [yes/no — if yes, how stored]

[S8] NAMING ANTI-PATTERNS:
  - Phrase-based names (e.g., "awtlytrn", "ycshikfmif") — not guessable
  - Generic names (e.g., "it", "but", "list") — collision-prone, not findable
  - Internal jargon — not guessable by new users
```

---

## Phase 4: Generation Pipeline

```
[S9] PIPELINE STAGES:
  1. CONCEPT: Define problem, trigger, input, output (from /mts)
  2. DRAFT: Generate full SKILL.md using template (from /mts)
  3. FORMALIZE: Enforce schema, overlap check, dependencies (from /fmtsb)
  4. REVIEW: Quality gate check (this phase)
  5. DEPLOY: Save to skills directory, update registry
```

### Quality Gate (Stage 4)

Every skill must pass before deployment:

```
[S10] QUALITY GATE:
| Check | Criterion | Pass/Fail |
|-------|-----------|-----------|
| Line count | ≥100 lines | |
| Principles | ≥3, each specific to domain | |
| Phases | ≥2, with numbered findings | |
| Failure modes | ≥4, with real signals | |
| Depth scaling | 4 tiers specified | |
| Checklist | ≥6 binary items | |
| Overlap | No HIGH-overlap duplicates | |
| Integration | ≥2 connection points | |
| Naming | Guessable, no collision | |
| Content density | Steps are executable, not "do the thing" | |
```

A skill that fails ANY gate item goes back to DRAFT stage.

---

## Phase 5: Review Process

```
[S11] REVIEW_TYPE: [self-review | peer-review | automated]

[S12] REVIEW CRITERIA:
  - Does each principle pass the "is this specific?" test?
  - Does each failure mode come from real observed failures?
  - Is each checklist item binary-checkable?
  - Is the output format structured enough to be parsed?
  - Would a user who needs this skill find it?
```

### Batch Review Efficiency

For batch creation, review in priority order:
1. Skills with highest expected usage
2. Skills that feed into other skills (dependency hubs)
3. Skills in underserved categories
4. Skills with the most overlap risk

---

## Phase 6: Output

```
SKILL CREATION SYSTEM
=====================

OBJECTIVE: [why]
VOLUME: [how many]
QUALITY_TARGET: [what standard]

SCHEMA: [summary of required elements]
TEMPLATE: [reference to template]
NAMING: [convention summary]

PIPELINE:
  CONCEPT → DRAFT → FORMALIZE → REVIEW → DEPLOY

QUALITY GATE: [N checks, all must pass]

REVIEW PROCESS: [type and criteria]

READY_TO_EXECUTE: [yes/no]
BLOCKERS: [list if any]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Stub production** | Batch creates 10-line files | Quality gate must enforce ≥100 lines |
| **Template monotony** | Every skill reads identically | Template constrains structure, not content |
| **Naming chaos** | Unguessable abbreviations proliferate | Naming convention with guessability test |
| **No review** | Skills deployed without quality check | Review stage is mandatory, not optional |
| **Overlap flood** | Multiple skills cover same problem | Overlap check in formalization stage |
| **Registry staleness** | New skills not added to registry/CLAUDE.md | Deploy stage must include registry update |

---

## Depth Scaling

| Depth | Pipeline Detail | Gate Checks | Review Criteria | Naming Rules |
|-------|----------------|-------------|----------------|-------------|
| 1x | 3 stages | 5 | 3 | Basic |
| 2x | 5 stages | 10 (all) | 5 | Full convention |
| 4x | 5 + parallel tracks | 10 + quality checks | 8 | Convention + alias support |
| 8x | Full with feedback loops | 10 + style review | 12 | Convention + migration plan |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Creation objective stated (not just "make more skills")
- [ ] Volume target specified
- [ ] Quality target defined with measurable criteria
- [ ] Schema defined with minimum thresholds per element
- [ ] Template exists and produces consistent structure
- [ ] Naming convention defined with anti-patterns listed
- [ ] Pipeline has all stages including quality gate
- [ ] Quality gate has specific, binary checks
- [ ] Review process defined (not skipped)
- [ ] Deploy stage includes registry update

---

## Integration

- Feeds into: `/mts` (individual skill creation), `/fmtsb` (formalization)
- Use after: `/pci` (when systematic improvement needed, sc designs the system)
- Differs from `/mts`: mts creates one skill; sc designs the creation system
- Differs from `/fmtsb`: fmtsb formalizes one skill; sc designs the formalization pipeline
- Differs from `/pci`: pci improves existing skills; sc creates new ones at scale
