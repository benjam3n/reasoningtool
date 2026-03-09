---
name: "alebc - And Lists Each Big Change"
description: "Convert a change stream into high-level big-change bullets, filtering out low-level modifications and grouping related changes into coherent shifts."
---

# ALEBC - And Lists Each Big Change

**Input**: $ARGUMENTS

---

## Core Principles

1. **"Big" is relative to context.** A big change in a startup might be a small change in an enterprise. The threshold for "big" must be defined for the specific context, not assumed.

2. **Changes interact.** Two small changes can constitute one big shift when combined. Three big changes might all be part of one even bigger transformation. The skill must detect composed changes, not just individual ones.

3. **New things vs modified things.** A genuinely new capability is a different kind of big than a major modification to an existing one. Distinguish additions from transformations.

4. **Low-level details are noise for this skill.** Bug fixes, minor parameter changes, formatting updates, incremental adjustments — these are not big changes. Ruthlessly exclude them. If the list includes minor items, it has failed.

5. **The narrative matters.** Big changes aren't just items in a list — they tell a story about what shifted and why. Group and order them to make the narrative visible.

---

## Phase 1: Change Stream Intake

```
[A1] SOURCE: [where the changes come from — git log, project notes, conversation history, etc.]
[A2] TIME_RANGE: [what period is being summarized]
[A3] CONTEXT: [what project/system/domain]
[A4] BIGNESS_THRESHOLD: [what counts as "big" in this context]
```

### Defining "Big"

| Context | Big Means |
|---------|----------|
| **Software project** | New feature, architectural change, major API change, capability added/removed |
| **Business** | New revenue stream, market entry, team restructure, strategic pivot |
| **Skill library** | New skill category, framework redesign, major skill overhaul |
| **Personal project** | Fundamental approach change, major milestone, scope change |
| **Document** | New section, thesis change, structural reorganization |

---

## Phase 2: Raw Change Enumeration

List all changes, without filtering yet:

```
[A5] CHANGE: [description] — MAGNITUDE: [big | medium | small | trivial]
[A6] CHANGE: [description] — MAGNITUDE: [level]
...
```

---

## Phase 3: Filtering and Grouping

### Filter: Remove Non-Big

Remove everything below the bigness threshold:
```
[A-N] EXCLUDED: [change] — WHY: [below threshold — incremental/fix/formatting/minor]
```

### Group: Compose Related Changes

Related changes that together constitute one shift:
```
[A-N] GROUP: [composed big change name]
  COMPONENT CHANGES:
    - [change 1]
    - [change 2]
    - [change 3]
  NARRATIVE: [what this group of changes represents as a shift]
```

### Classify: Addition vs Transformation vs Removal

```
[A-N] BIG_CHANGE: [description]
  TYPE: [addition | transformation | removal | restructure]
  IMPACT: [what this changes for the user/project/system]
```

---

## Phase 4: Narrative Ordering

Order the big changes to tell a coherent story:

| Ordering Strategy | When to Use |
|------------------|------------|
| **Chronological** | When the sequence matters (this enabled that) |
| **Impact-first** | When importance varies and the biggest should lead |
| **Thematic** | When changes cluster into themes |
| **Dependency** | When changes build on each other |

```
[A-N] ORDERING: [strategy chosen] — [why this ordering tells the clearest story]
```

---

## Phase 5: Output

```
BIG CHANGES
============

[Context] — [Time Range]

1. [Big change title]
   TYPE: [addition | transformation | removal | restructure]
   WHAT: [one-sentence description]
   IMPACT: [what this changes for users/project/system]

2. [Big change title]
   TYPE: [type]
   WHAT: [description]
   IMPACT: [impact]

3. [Big change title]
   TYPE: [type]
   WHAT: [description]
   IMPACT: [impact]

...

EXCLUDED (for reference):
- [N] minor changes filtered out
- Categories excluded: [bug fixes, formatting, incremental adjustments, etc.]

NARRATIVE: [one paragraph summarizing the overall direction these big changes represent]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Everything is "big"** | 20+ items in the list | Raise the threshold. If everything is big, nothing is |
| **Minor items included** | Bug fixes or parameter changes in the list | Reapply filter — these should be in EXCLUDED |
| **Composition missed** | 5 related changes listed separately | Group related changes into composed shifts |
| **No impact stated** | Changes listed without explaining what they mean | Every big change must state its IMPACT |
| **Flat list** | No narrative ordering | Choose an ordering strategy and apply it |
| **Additions only** | Removals and transformations missed | Explicitly check for things removed or fundamentally changed |
| **Context-blind threshold** | Using one "big" definition for all contexts | Define bigness threshold for THIS specific context |

---

## Depth Scaling

| Depth | Min Changes Scanned | Min Big Changes | Grouping | Narrative |
|-------|-------------------|----------------|----------|-----------|
| 1x | 10 | 3 | No | Bullets only |
| 2x | 20 | 5 | Yes | Bullets + impact |
| 4x | 40 | 8 | Yes + composition | Bullets + impact + narrative paragraph |
| 8x | All available | All big | Full composition analysis | Full narrative + excluded summary |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Change source and time range identified
- [ ] Bigness threshold defined for this context
- [ ] All changes enumerated before filtering
- [ ] Minor changes explicitly excluded (not just ignored)
- [ ] Related changes grouped into composed shifts
- [ ] Each big change has type, description, and impact
- [ ] Ordering strategy chosen and applied
- [ ] No minor items in the big changes list
- [ ] Additions, transformations, AND removals checked

---

## Integration

- Use from: project reviews, `/wn` (what's new), progress reports
- Complementary: `/wn` (what's new — includes small changes; alebc filters to big only)
- Differs from `/wn`: wn shows everything new; alebc shows only big changes
- Differs from `/aar`: aar reviews what happened and why; alebc lists what changed
- Routes to: `/evaluate` if big changes need assessment
