---
name: "categorize - Categorize"
description: "Organize items, files, folders, or output into discovered categories. Discovers dimensions from the data itself, not from theory. Handles large inputs by sampling."
output:
  format: "prose"
---

# Categorize

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches:

**Interpretation 1 — Inventory**: The user has a path, glob, or directory and wants to know what's in it and how it organizes.
**Interpretation 2 — Prior output**: The user wants to categorize something from the conversation (skill output, a list, findings).
**Interpretation 3 — Concept**: The user wants to categorize an abstract space ("categorize approaches to X"). → INVOKE: /gg to generate items first, then categorize the output.

If ambiguous, ask: "Are you categorizing files/items, prior output, or want me to generate items first?"

---

## Core Principles

1. **Dimensions emerge from data.** Never start with predetermined categories. Let the items tell you how they cluster.
2. **A dimension must be surprising.** If someone could guess the categories without looking at the data, the dimension is trivial. The point of categorization is to reveal structure that isn't already obvious.
3. **A category name IS the explanation.** If you need to describe what a category contains, the name is wrong. Pick a name that's self-evident.
4. **Orthogonality over quantity.** Two dimensions that tell you different things beat five that overlap.
5. **Uncategorized is signal, not failure.** Items that don't fit reveal the limits of your dimensions.
6. **Counts over lists.** Show distribution, not inventory. Lists only on drill-down.

---

## Step 1: Gather Items

**Files:**

| Count | Strategy |
|-------|----------|
| ≤ 50 | Read all names. Sample content of each (first 50 lines, frontmatter) |
| 51–500 | All names. Sample 20% contents across distribution |
| 501–5,000 | All names. Sample 50 across distribution |
| 5,001+ | Tree structure first. Sample 100. Names → content-validate |

**Lists/output:** Extract every discrete item (bullets, findings, claims, entries).

Per item extract what's available: name, size, type/extension, content sample, metadata, relationships.

---

## Step 2: Discover Dimensions

Check ALL six sources below. Collect every candidate dimension. Then apply the quality filter to pick the best 1-3.

### Sources

1. **Name patterns** — prefixes, suffixes, separators, naming conventions, numbering
2. **Content patterns** — recurring themes, topics, structures within the items
3. **Structural patterns** — relationships, imports, links, references, hierarchy
4. **Type/format patterns** — extension, file type, medium
5. **Scale patterns** — size clusters, complexity differences
6. **Temporal patterns** — date clusters, creation order, recency

### Dimension Quality Filter

Every candidate dimension must pass ALL THREE tests. If it fails any, reject it.

**Test 1 — Discriminating**: Does it split items into 2+ groups with >3 items each?
- FAIL example: "file format" when everything is .md

**Test 2 — Orthogonal**: Does it tell you something different from other candidate dimensions?
- FAIL example: "skill-generated vs manual" mirrors "has date prefix vs doesn't"

**Test 3 — Non-obvious**: Would someone learn something they didn't already know?
- FAIL example: "project" when items are already in separate project folders
- FAIL example: "file extension" when the user can see the file listing
- FAIL example: restating the input's existing structure as a "discovery"
- The test: "If I told someone these categories, would they say 'huh, interesting' or 'yeah, obviously'?"

Pick 1-3 dimensions that pass all three tests. If no dimension passes all three, say so — forced categorization is worse than honest "these items don't have hidden structure."

---

## Step 3: Assign and Name Categories

### Assignment
- Categories emerge from clusters in the data, not from theory
- Items can appear in multiple categories across different dimensions
- If >60% falls in one category, the dimension probably isn't discriminating enough

### Naming
- Category names must be self-explanatory — NO descriptions after names
- **The 2-word test**: can you name it in 2-3 words? If you need a sentence, the category is too vague or too complex — split it or rethink it.
- **The stranger test**: would someone unfamiliar with the data understand what belongs in this category from the name alone?
- 1-item categories are suspicious — either an outlier worth calling out, or too granular (merge up)
- Avoid abstract/academic names ("epistemic artifacts," "meta-cognitive outputs") — use concrete names ("analysis docs," "brainstorm outputs")

---

## Step 4: Output

**Per dimension:**

```
DIMENSION: [name]

  [category]: ████████████ [N] ([%])
  [category]: ██████ [N] ([%])
  [category]: ██ [N] ([%])
```

No descriptions. No item lists. Sorted by count descending.

**Cross-reference matrix** (only when 2+ dimensions are genuinely orthogonal — if they aren't independent, the matrix is misleading):

```
                  | [B1]  | [B2]  | [B3]  |
[A1]              |  12   |   3   |   0   |
[A2]              |   1   |  28   |   7   |
```

Note empty cells (structural gaps) and dominant cells (concentrations).

---

## Step 5: Patterns

After categorizing, note ONLY what's non-obvious:
- **Outliers**: items that bridge categories or don't fit any
- **Gaps**: categories you'd expect to exist but don't
- **Concentrations**: >50% in one category — why?
- **Surprises**: anything that contradicts initial assumptions

If nothing is non-obvious, say "no non-obvious patterns." Don't manufacture insight.

---

## Step 6: Summary

```
Items: [N] | Dimensions: [N] | Categories: [N] | Uncategorized: [N]

[primary dimension]:
  [category]: [N]
  [category]: [N]
  ...

KEY INSIGHT: [one sentence — what's the most useful thing this categorization reveals?]
```

---

## Depth Scaling

| Depth | Gathering | Dimensions | Output |
|-------|-----------|------------|--------|
| 1x | Names only | 1 obvious | Flat category list |
| 2x | Names + type + size | 1–2 with quality filter | Distribution bars |
| 4x | + sampled content | 2–3 + cross-reference | + patterns |
| 8x | Full content scan | All discoverable, ranked | + validation + recommendations |
| 16x | + relationships + history | + sub-dimensions | Hierarchical + structural analysis |

Default: 2x.

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Trivial dimension** | Categories restate what's visible in the file listing | You're describing, not discovering. Find what cuts ACROSS the obvious structure. |
| **Everything in one category** | >80% in single group | Dimension isn't discriminating. Try a different one. |
| **More categories than items per category** | avg <2 items per category | Too granular. Merge until categories have 3+. |
| **Category needs explanation** | You're writing descriptions after names | Name is wrong. Pick a better name. |
| **Forcing a taxonomy** | Categories feel academic/theoretical | Start over. Read actual items. What piles do THEY form? |
| **Surface-only** | Categories come from names alone, not content | Sample content to validate. Name clusters ≠ content clusters. |
| **Dimension overlap** | Two dimensions produce similar groupings | Keep the more useful one. Drop the other. |
| **Manufactured insight** | "Patterns" section feels forced | Say "no non-obvious patterns." |

---

## Large Input Tactics

**Thousands of files:**
1. Tree structure first — the tree IS categorization data
2. Extension partition — free, almost always valid
3. Name clustering — prefixes, suffixes, conventions
4. Strategic sampling — 3–5 files per name-cluster to validate
5. Incremental refinement — go deep where interesting, not everywhere equally

**Large text outputs:**
1. Use existing structure (headings, numbers) as initial grouping
2. Dedup near-duplicates first
3. Chunk into 100s, categorize chunks, merge

**Multiple directories:**
1. Categorize each separately first
2. Then categorize across — differences between distributions are more interesting than the distributions themselves

---

## Integration

- `/gg` → categorize generated guesses for coverage gaps
- `/cls` → filter within categories by criteria
- `/cmp` → compare two categorizations
- `/perceive` → process large body of work then categorize the output
- `/improve` → enhance categorization quality after initial pass

---

**Execute now.**
