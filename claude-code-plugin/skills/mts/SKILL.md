---
name: "mts - Make This Skill"
description: "Create a new skill from a request by deriving purpose, naming, workflow, output format, quality checks, and integration points."
output:
  format: "prose"
---

# MTS - Make This Skill

**Input**: $ARGUMENTS

---

## Core Principles

1. **Purpose before structure.** A skill exists to solve a problem that currently requires improvisation. If you can't state what problem the skill solves in one sentence, it shouldn't exist.

2. **Naming is findability.** The skill ID must be guessable from the problem it solves. Bad names make skills invisible. The test: would someone looking for this skill try this name?

3. **Scope is a boundary, not a description.** Every skill must explicitly state what it does NOT do. Without scope boundaries, skills bloat until they overlap everything.

4. **Quality comes from criteria, not from length.** A 50-line skill with tight criteria beats a 300-line skill with vague steps. The question is "does each line earn its place?" not "is it long enough?"

5. **Integration is mandatory.** A skill that doesn't connect to other skills is an island. State what feeds into it and what it feeds into.

6. **Don't duplicate.** Before creating, check if an existing skill already covers this need. The library has 367 skills — the odds of genuine novelty are lower than expected.

---

## Phase 1: Intent Extraction

```
[M1] USER_REQUEST: [what the user asked for, quoted]
[M2] PROBLEM_SOLVED: [what problem this skill addresses — one sentence]
[M3] TRIGGER: [when would someone reach for this skill? What situation are they in?]
[M4] INPUT: [what the skill receives from the user]
[M5] OUTPUT: [what the skill produces — the deliverable]
[M6] NOT_THIS_SKILL: [what this skill explicitly does NOT do]
```

### Overlap Check

Before proceeding, check for existing skills that cover this need:
```
[M7] OVERLAP_CHECK:
  /[id] — [title] — OVERLAP: [none | partial | high] — [what's different]
  /[id] — [title] — OVERLAP: [level] — [what's different]
```

If OVERLAP is HIGH for any existing skill: STOP. Recommend using or updating the existing skill instead.

---

## Phase 2: Naming

```
[M8] PROPOSED_ID: [2-6 character abbreviation]
[M9] FULL_NAME: [descriptive name]
[M10] NAMING_RATIONALE: [why this ID is guessable from the problem]
```

### Naming Rules

| Rule | Rationale |
|------|-----------|
| 2-6 characters | Short enough to type, long enough to be distinct |
| Mnemonic preferred | `rca` for root cause analysis, `cmp` for compare |
| No collision | Must not conflict with existing skill IDs |
| Function over form | Name what it DOES, not what it IS |
| Guessable | Someone who needs this should guess this name |

---

## Phase 3: Skill Architecture

Design the skill's internal structure.

### Phase Structure

Every non-trivial skill needs phases. Determine which apply:

| Phase | When Needed |
|-------|------------|
| **Input parsing** | Always — validate and structure what the user gave |
| **Analysis/exploration** | When the skill needs to discover or evaluate |
| **Transformation** | When the skill converts input to a different form |
| **Validation** | When the output needs quality checking |
| **Output** | Always — structured deliverable |

```
[M11] PHASES:
  Phase 1: [name] — [what it does]
  Phase 2: [name] — [what it does]
  ...
```

### Finding Tracking

Choose a letter prefix for numbered findings:
```
[M12] FINDING_PREFIX: [letter] (e.g., "R" for root cause, "W" for writing)
```

### Core Principles

Draft 3-6 principles that capture what makes this skill's domain HARD:
```
[M13] PRINCIPLE 1: [name] — [what it means and why it matters]
[M14] PRINCIPLE 2: [name] — [what it means]
...
```

Principles must be:
- Specific to this skill (not generic advice)
- Counterintuitive or easy to violate (obvious principles don't need stating)
- Actionable (affect how the skill is executed)

---

## Phase 4: Quality Elements

### Failure Modes

```
[M15] FAILURE MODES:
| Failure | Signal | Fix |
|---------|--------|-----|
| [mode 1] | [how you'd notice] | [what to do instead] |
| [mode 2] | [signal] | [fix] |
```

Minimum 4 failure modes. Source them from:
- What goes wrong when this problem is solved ad-hoc?
- What's the most common bad version of this output?
- What does a beginner get wrong?

### Depth Scaling

```
[M16] DEPTH SCALING:
| Depth | [dimension 1] | [dimension 2] | Min Total Findings |
|-------|--------------|--------------|-------------------|
| 1x | [min] | [min] | [N] |
| 2x | [min] | [min] | [N] |
| 4x | [min] | [min] | [N] |
| 8x | [min] | [min] | [N] |
```

### Pre-Completion Checklist

```
[M17] CHECKLIST:
- [ ] [item 1]
- [ ] [item 2]
...
```

Minimum 6 items. Each must be binary-checkable.

---

## Phase 5: Draft Assembly

Assemble the full SKILL.md file with all components:

```
[M18] ASSEMBLED SKILL:
  - Frontmatter (name, description)
  - Core Principles
  - Phase structure with numbered findings
  - Output format
  - Failure modes table
  - Depth scaling table
  - Pre-completion checklist
  - Integration section
```

### Integration Section

```
[M19] INTEGRATION:
  - Use after: /[id] (what feeds into this skill)
  - Use before: /[id] (what this skill feeds into)
  - Differs from: /[id] (how — prevent confusion)
  - Complementary: /[id] (good to run alongside)
```

---

## Phase 6: Output

Produce the complete SKILL.md file content, ready to save.

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Duplicate skill** | High overlap with existing skill not caught | Run overlap check before designing |
| **Vague purpose** | Can't state problem solved in one sentence | Go back to Phase 1; if you can't state it, it shouldn't exist |
| **Generic principles** | "Be thorough" / "Consider all options" | Principles must be specific to this domain and counterintuitive |
| **No failure modes** | Skill has no failure modes table | Every domain has common mistakes. Find at least 4 |
| **Missing integration** | Skill is an island — nothing feeds in or out | Find at least 2 connection points |
| **Name collision** | ID conflicts with existing skill | Check the full skill registry |
| **Stub output** | Skeleton with placeholder steps | Each step must be executable, not "do the thing" |

---

## Depth Scaling

| Depth | Min Principles | Min Failure Modes | Min Checklist Items | Min Integration Points |
|-------|---------------|------------------|--------------------|-----------------------|
| 1x | 3 | 3 | 4 | 2 |
| 2x | 4 | 5 | 6 | 3 |
| 4x | 5 | 7 | 8 | 5 |
| 8x | 6 | 10 | 10 | 7 |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Problem solved is stated in one sentence
- [ ] Overlap check completed against existing skills
- [ ] No high-overlap duplicate exists
- [ ] ID is 2-6 characters and guessable from the problem
- [ ] Scope boundary explicit (what this skill does NOT do)
- [ ] Core principles are specific and counterintuitive
- [ ] Phase structure has numbered findings with prefix
- [ ] Failure modes table has at least 4 entries
- [ ] Depth scaling table exists
- [ ] Pre-completion checklist exists (in the output skill)
- [ ] Integration points specified
- [ ] Output is a complete, saveable SKILL.md

---

## Integration

- Use before: `/fmtsb` (to formalize the draft)
- Use after: `/dtse` (when skill doesn't exist and needs creation)
- Differs from `/cs`: cs has CREATE/UPDATE/GAP_SCAN modes; mts focuses purely on creation
- Differs from `/fmtsb`: fmtsb formalizes an existing draft; mts creates from scratch
- Differs from `/sc`: sc designs skill creation SYSTEMS; mts creates individual skills
