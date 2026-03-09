---
name: "list - Build High-Quality Lists"
description: "Create rigorous, useful lists with clear scope, inclusion rules, ordering logic, coverage checks, and concise rationale per item — avoiding the common failures of vagueness, gaps, and inconsistent granularity."
---

# List - Build High-Quality Lists

**Input**: $ARGUMENTS

---

## Core Principles

1. **Lists are claims about category membership.** Every list implicitly asserts: "these items belong together and nothing important is missing." Both claims need to be tested. An item that doesn't belong is a contamination. A missing item is a gap. Both undermine the list.

2. **Inclusion rules before items.** Generating items first and then trying to find what they have in common produces incoherent lists. Define the inclusion and exclusion criteria BEFORE generating items, then test each item against the criteria. This order is non-negotiable.

3. **Granularity must be consistent.** "Buy groceries, achieve world peace, call dentist" is three items at three different granularity levels. Every item in a list should be roughly the same scope, specificity, and abstraction level. Inconsistent granularity makes lists unusable.

4. **Order is not optional.** An unordered list forces the reader to determine what matters most. Every list should have an explicit ordering basis — by priority, by category, by dependency, by chronology — and the basis should be stated, not guessed.

5. **Coverage is testable.** "Am I missing anything?" has structured answers. Enumerate the subcategories of the list's domain, check that each is represented, and flag gaps. A list that hasn't been checked for coverage is a draft, not a deliverable.

---

## Phase 1: List Contract

Define what this list is before generating it:

```
[L1] LIST_GOAL: [what this list is for — what decision or action it supports]
[L2] AUDIENCE: [who will use this list and what they need from it]
[L3] DOMAIN: [what category or space this list covers]
[L4] DEPTH: [quick | standard | exhaustive]
[L5] ORDER_BASIS: [ranked | grouped | chronological | dependency | alphabetical]
```

---

## Phase 2: Inclusion Rules

Define membership before generating items:

```
[L6] INCLUDE_IF: [explicit criteria for an item to be on this list]
[L7] EXCLUDE_IF: [explicit criteria for an item to NOT be on this list]
[L8] GRANULARITY: [the scope/specificity level items should be at — with example]
[L9] OVERLAP_RULE: [how to handle items that partially overlap — merge, split, or keep both]
```

### Granularity Calibration

Pick a reference item and state: "All items should be roughly the same scope as [reference item]." This prevents mixing "strategic initiatives" with "send an email."

---

## Phase 3: Generation

Generate candidate items broadly, then filter:

```
[L-N] CANDIDATE: [item]
  PASSES_INCLUSION: [yes/no — how it satisfies the inclusion rule]
  GRANULARITY_MATCH: [yes/adjusted — is it the right scope?]
  STATUS: [included | excluded | merged with [other item] | split into [sub-items]]
```

### Generation Strategies

| Strategy | Method |
|----------|--------|
| **Brainstorm** | Rapid generation without filtering |
| **Categorical sweep** | Identify subcategories of the domain, generate from each |
| **Stakeholder sweep** | What would [each stakeholder type] add? |
| **Temporal sweep** | What's relevant now, soon, and later? |
| **Negative space** | What's conspicuously absent? |

---

## Phase 4: Order and Label

For each included item:

```
[L-N] ITEM: [item name or description]
  WHY_IT_MATTERS: [one sentence — why this item is on the list]
  POSITION: [rank number or group name]
  POSITION_REASON: [why here and not higher/lower — only for ranked lists]
```

### Ordering Validation

For ranked lists, verify:
- Top item truly outranks #2 on the stated ordering criterion
- Bottom item truly belongs below all others
- Adjacent items with close rankings have a stated distinguisher

---

## Phase 5: Coverage Check

Systematically check for gaps:

```
[L-N] COVERAGE_CHECK:
  SUBCATEGORIES_OF_DOMAIN: [list the major subcategories]
  REPRESENTED: [which subcategories have items]
  MISSING: [which subcategories have no items]
  VERDICT: [complete | gap found — adding items | intentionally excluded — why]
```

### Common Gap Patterns

| Gap Type | How to Detect |
|----------|--------------|
| **Category blind spot** | A major subcategory has zero items |
| **Recency bias** | Only recent/trendy items included |
| **Familiarity bias** | Only well-known items, no non-obvious entries |
| **Positive bias** | Only "good" items, no risks or negatives |
| **Scale bias** | Only items at one scale, missing micro or macro |

---

## Phase 6: Output

```
LIST
====

GOAL: [what this list supports]
DOMAIN: [what it covers]
ORDER: [ordering basis]
INCLUSION RULE: [what qualifies an item]

1. [item]
   WHY: [one sentence]
2. [item]
   WHY: [one sentence]
3. [item]
   WHY: [one sentence]
...

COVERAGE:
  Subcategories checked: [list]
  Gaps found: [none | list with resolution]

ASSUMPTIONS:
  - [any assumptions made during generation]

READY FOR:
- /ro — to reorder this list by a different objective
- /mv — to validate MECE structure
- /se — to exhaustively enumerate if coverage is critical
- /etc — to expand if the list was given with "etc"
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **No inclusion rule** | Items generated without criteria | Define include/exclude rules before generating |
| **Granularity inconsistency** | Items at wildly different scope levels | Set a reference item and match all items to its scope |
| **No ordering rationale** | Items numbered but order is arbitrary | State the ordering basis and justify position for each item |
| **Coverage unchecked** | No systematic check for gaps | Enumerate domain subcategories and verify representation |
| **Too many items** | List is exhaustive when user needs actionable | Match depth to stated goal. Quick = 5-7, standard = 8-15 |
| **Duplicates and overlaps** | Two items that are essentially the same | Apply the overlap rule — merge, split, or justify keeping both |
| **WHY missing** | Items listed without rationale | Every item needs a one-sentence justification for its inclusion |
| **Generated then filtered** | Inclusion rules written to match already-generated items | Rules must be written BEFORE items. If you catch yourself retrofitting rules, restart |

---

## Depth Scaling

| Depth | Item Count | Generation Strategy | Coverage Check | Ordering Rigor |
|-------|-----------|-------------------|---------------|---------------|
| 1x | 5-7 | Brainstorm | Basic category check | Ordered with basis stated |
| 2x | 8-15 | 2 strategies | Subcategory enumeration | Ordered with position reasons |
| 4x | 15-25 | 3+ strategies | Full with gap remediation | Pairwise comparison for top items |
| 8x | 25+ | All strategies | Exhaustive + negative space | Full ranking with confidence levels |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] List goal and audience defined
- [ ] Inclusion/exclusion rules stated BEFORE generation
- [ ] Granularity is consistent across all items
- [ ] Ordering basis stated explicitly
- [ ] Every item has a one-sentence rationale
- [ ] Coverage check performed against domain subcategories
- [ ] Gaps addressed (added items or justified exclusion)
- [ ] Overlaps resolved (merged, split, or justified)
- [ ] Depth matches the stated goal

---

## Integration

- Use from: any request to "list", "enumerate", "what are the...", "give me options"
- Routes to: `/ro` (reorder by different criteria), `/mv` (validate MECE), `/se` (exhaustive enumeration)
- Complementary: `/ro` (build list with /list, then optimize order with /ro)
- Differs from `/se`: se is exhaustive enumeration of a known space; list builds useful lists with quality criteria
- Differs from `/etc`: etc expands compressed lists; list builds from scratch
- Differs from `/o`: o ranks viable options from a decision context; list builds general-purpose lists
