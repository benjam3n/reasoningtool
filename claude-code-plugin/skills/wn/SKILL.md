---
name: "wn - What's New"
description: "Summarize what is new in a project or codebase, grouped by configurable views (day, category, skill, iteration), filtering out unchanged items."
---

# WN - What's New

**Input**: $ARGUMENTS

---

## Core Principles

1. **New means new.** Not modified, not improved, not unchanged — genuinely NEW additions that didn't exist before. The skill must distinguish new items from changes to existing items.

2. **View determines grouping.** The same set of new items tells different stories depending on how you group them: by time (what happened when), by category (what kind of things were added), by component (where in the system), or by theme (what pattern connects them).

3. **Recency bias is real.** Recent additions feel more important than they are. The skill should present new items neutrally, not weighted by how recently they appeared.

4. **Context determines scope.** "What's new" in a 3-day sprint is different from "what's new" in a 6-month project. The time range must be explicit.

5. **New items have different sizes.** A new architecture pattern and a new configuration option are both "new" but vastly different in significance. The output should make relative significance visible.

---

## Phase 1: Scope Definition

```
[W1] PROJECT: [what project or system]
[W2] TIME_RANGE: [from when to when — or "since last review"]
[W3] SOURCE: [where to look — git log, file system, conversation history, notes]
[W4] VIEW: [by_time | by_category | by_component | by_theme | by_significance]
```

---

## Phase 2: New Item Discovery

Scan the source for genuinely new additions:

```
[W-N] NEW: [item description]
  ADDED: [when]
  CATEGORY: [what kind of thing]
  COMPONENT: [where in the system]
  SIGNIFICANCE: [major | moderate | minor]
  EVIDENCE: [how we know this is new, not modified]
```

### New vs Modified

| Signal | Classification |
|--------|---------------|
| Didn't exist before the time range | **New** |
| Existed but changed substantially | **Modified** (not included in /wn — use /alebc for changes) |
| Existed and changed minor details | **Updated** (excluded) |
| Existed and didn't change | **Unchanged** (excluded) |

---

## Phase 3: Grouping

Group new items by the selected view:

### By Time
```
[W-N] DAY/PERIOD: [date range]
  - [item] — SIGNIFICANCE: [level]
  - [item] — SIGNIFICANCE: [level]
```

### By Category
```
[W-N] CATEGORY: [category name]
  - [item] — ADDED: [when] — SIGNIFICANCE: [level]
  - [item] — ADDED: [when] — SIGNIFICANCE: [level]
```

### By Component
```
[W-N] COMPONENT: [component name]
  - [item] — CATEGORY: [type] — SIGNIFICANCE: [level]
```

### By Significance
```
[W-N] MAJOR:
  - [item] — [what it is] — [when added]
MODERATE:
  - [item] — [what it is] — [when added]
MINOR:
  - [item] — [what it is] — [when added]
```

---

## Phase 4: Summary

```
[W-N] SUMMARY:
  TOTAL_NEW: [N items]
  MAJOR: [N items]
  MODERATE: [N items]
  MINOR: [N items]
  MOST_ACTIVE_CATEGORY: [category with most new items]
  MOST_ACTIVE_PERIOD: [time period with most additions]
  PATTERN: [any visible pattern in what's being added — optional]
```

---

## Phase 5: Output

```
WHAT'S NEW
==========

PROJECT: [name]
PERIOD: [time range]
VIEW: [grouping method]

[grouped items per selected view]

SUMMARY:
  [N] new items ([N] major, [N] moderate, [N] minor)
  Most active: [category/period]
  Pattern: [if any]

NOT INCLUDED:
  - [N] modified items (use /alebc for changes)
  - [N] unchanged items

READY FOR:
- /alebc — to see big changes (not just new items)
- /iterate [component] — to improve a specific area
- /evaluate [new item] — to assess quality of something new
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Modified items included** | Changes to existing items listed as "new" | Apply new vs modified test strictly |
| **No time range** | "What's new" without scope | Always define the period explicitly |
| **Flat list** | No grouping applied | Use the selected view to structure output |
| **Significance ignored** | Major and minor items presented equally | Flag significance for each item |
| **Missing source** | Guessing what's new without checking | Specify and scan the actual source |
| **Everything is new** | Time range too long, includes entire history | Narrow the time range |

---

## Depth Scaling

| Depth | Source Scanning | Grouping Views | Significance Assessment | Pattern Analysis |
|-------|----------------|---------------|------------------------|-----------------|
| 1x | Single source | 1 view | Binary (major/minor) | No |
| 2x | 2 sources | 2 views | Three-level | Basic pattern |
| 4x | 3+ sources | 3 views | Three-level + evidence | Pattern + trends |
| 8x | All available | All views | Full + cross-reference | Full analysis |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Time range explicitly defined
- [ ] Source specified and scanned
- [ ] New items distinguished from modified items
- [ ] Significance assessed for each item
- [ ] Items grouped by selected view
- [ ] Summary with counts and patterns
- [ ] Modified items excluded (noted for reference)

---

## Integration

- Complementary: `/alebc` (big changes — includes modifications, not just new items)
- Differs from `/alebc`: alebc shows big changes; wn shows all new additions regardless of size
- Use from: project reviews, sprint retrospectives, onboarding ("what's new since I last looked")
- Routes to: `/evaluate`, `/iterate` for assessing or improving new items
