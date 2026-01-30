---
name: "mv - MECE Validation"
description: Validate that a list is MECE (Mutually Exclusive, Collectively Exhaustive). Identifies overlaps and gaps.
---

# MECE Validation

**Input**: $ARGUMENTS

---

## Purpose

Validate that a list achieves **MECE** quality:
- **Mutually Exclusive (ME)**: No item belongs to multiple categories
- **Collectively Exhaustive (CE)**: All possible items are covered

This skill identifies overlaps (ME violations) and gaps (CE violations).

---

## MECE Spectrum

Perfect MECE is often impossible. This skill uses a **soft MECE** approach:

| Level | ME (Overlaps) | CE (Gaps) | When Acceptable |
|-------|---------------|-----------|-----------------|
| **Perfect MECE** | 0 overlaps | 0 gaps | Formal specifications |
| **Soft MECE** | < 5% overlap | < 10% gaps | Most business use |
| **Good Enough** | < 15% overlap | < 20% gaps | Brainstorming, early drafts |
| **Needs Work** | > 15% overlap | > 20% gaps | Requires revision |

---

## The Validation Process

### Step 1: Confirm Structure

Identify what you're validating:

```
VALIDATING: [list name/description]

STRUCTURE:
- Total items: [N]
- Categories: [list of categories if hierarchical]
- Dimensions covered: [if from space_enumeration]
- Target MECE level: [Perfect / Soft / Good Enough]
```

---

### Step 2: Check Mutual Exclusivity (ME)

For each item, check: Does it fit in multiple categories?

```
MUTUAL EXCLUSIVITY CHECK:

| Item | Primary Category | Also Fits? | Overlap? |
|------|------------------|------------|----------|
| [Item 1] | [Cat A] | No | [x] ME |
| [Item 2] | [Cat B] | [Cat C] | [!] OVERLAP |
| [Item 3] | [Cat A] | No | [x] ME |
...

OVERLAPS FOUND: [N]
OVERLAP RATE: [N / Total] = [X%]
```

**For each overlap**, decide:
1. **Assign to primary**: Pick one category, note secondary
2. **Split the item**: Create more specific sub-items
3. **Merge categories**: If overlap is systematic
4. **Accept overlap**: If categories are perspectives, not buckets

---

### Step 3: Check Collective Exhaustiveness (CE)

#### 3A: Dimension Coverage Check

If dimensions are known (from `/dd`):

```
DIMENSION COVERAGE:

| Dimension | Values | Items Found | Missing? |
|-----------|--------|-------------|----------|
| [Dim 1] | [v1, v2, v3] | [3, 2, 4] | No |
| [Dim 2] | [v1, v2] | [5, 0] | YES: v2 |
...

GAPS FOUND: [N]
GAP RATE: [Missing combinations / Total possible] = [X%]
```

#### 3B: Edge Case Check

Check for items that might be missing:

```
EDGE CASE PROBES:

| Probe | Found in List? | If No, Add? |
|-------|----------------|-------------|
| Extreme cases (max/min) | [Y/N] | [action] |
| Boundary cases | [Y/N] | [action] |
| Negative cases (what it's NOT) | [Y/N] | [action] |
| Historical cases (past examples) | [Y/N] | [action] |
| Future cases (emerging trends) | [Y/N] | [action] |
| Edge stakeholders | [Y/N] | [action] |
```

#### 3C: "What's Missing?" Brainstorm

Ask explicitly: What could be on this list but isn't?

```
WHAT'S MISSING BRAINSTORM:

Domain expert would add:
- [potential missing item 1]
- [potential missing item 2]

Contrarian would add:
- [unconventional item that belongs]

Adjacent domain has:
- [item from related field that applies]
```

---

### Step 4: Calculate MECE Score

```
MECE SCORE:

Mutual Exclusivity:
- Overlaps: [N] / [Total] = [X%]
- ME Score: [100 - X]%

Collective Exhaustiveness:
- Gaps identified: [N]
- Estimated coverage: [Y%]
- CE Score: [Y]%

OVERALL MECE: (ME Score + CE Score) / 2 = [Z%]

ASSESSMENT:
- [ ] Perfect MECE (>95%)
- [x] Soft MECE (80-95%)
- [ ] Good Enough (60-80%)
- [ ] Needs Work (<60%)
```

---

### Step 5: Generate Recommendations

Based on findings:

```
MECE VALIDATION RESULTS: [list name]

STATUS: [Perfect MECE / Soft MECE / Good Enough / Needs Work]

OVERLAPS TO RESOLVE:
1. [Item X] overlaps [Cat A] and [Cat B]
   -> Recommendation: [assign/split/merge/accept]

GAPS TO FILL:
1. [Dimension Y, Value Z] has no items
   -> Recommendation: [add specific items]

2. [Edge case] not covered
   -> Recommendation: [add item]

ACTIONS:
- [ ] [Specific action 1]
- [ ] [Specific action 2]
```

---

## Example: Validating "Types of Machine Learning"

### Input List
1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning
4. Deep Learning
5. Neural Networks
6. Semi-supervised Learning

### Step 1: Structure
- Total items: 6
- Target: Soft MECE

### Step 2: ME Check

| Item | Primary | Also Fits? | Overlap? |
|------|---------|------------|----------|
| Supervised | Learning paradigm | No | [x] |
| Unsupervised | Learning paradigm | No | [x] |
| Reinforcement | Learning paradigm | No | [x] |
| Deep Learning | Architecture | Learning paradigm | [!] OVERLAP |
| Neural Networks | Architecture | Deep Learning | [!] OVERLAP |
| Semi-supervised | Learning paradigm | No | [x] |

**Overlaps**: 2 (Deep Learning, Neural Networks)
**Analysis**: List mixes two dimensions - paradigm and architecture

### Step 3: CE Check

**Dimension coverage**:
- Paradigms: Supervised, Unsupervised, Reinforcement, Semi-supervised [x]
- Missing: Self-supervised learning

**Edge cases**:
- Transfer learning? Not covered
- Online learning? Not covered

### Step 4: Score

- ME: 4/6 clean = 67%
- CE: Missing ~3 items from ~10 possible = 70%
- Overall: 68% = **Good Enough (Needs Work)**

### Step 5: Recommendations

```
STATUS: Good Enough - Needs Work

OVERLAPS TO RESOLVE:
1. "Deep Learning" and "Neural Networks" are architecture, not paradigm
   -> Split list into: A) Learning Paradigms, B) Architectures
   OR -> Remove Deep Learning/Neural Networks (different dimension)

GAPS TO FILL:
1. Self-supervised learning (emerging paradigm)
2. Transfer learning (important paradigm)
3. Online/incremental learning (paradigm)

RECOMMENDED REVISED LIST:
Learning Paradigms:
- Supervised
- Unsupervised
- Semi-supervised
- Self-supervised
- Reinforcement
- Transfer learning
- Online learning
```

---

## Quick MECE Check (Abbreviated)

For fast validation:

```
QUICK MECE: [list name]

[ ] Any item fits 2+ categories? -> If yes, overlap issue
[ ] Any obvious gaps? -> If yes, CE issue
[ ] Would domain expert add anything? -> If yes, gap
[ ] Would domain expert remove anything? -> If yes, scope issue

QUICK VERDICT: [MECE / Mostly MECE / Needs Work]
```

---

## Quality Checklist

Before completing:
- [ ] Structure confirmed
- [ ] All items checked for overlaps
- [ ] Dimension coverage verified
- [ ] Edge cases probed
- [ ] "What's missing" brainstormed
- [ ] MECE score calculated
- [ ] Specific recommendations provided

---

## Integration

Use with:
- `/dd` -> Identify dimensions first
- `/se` -> Generate the list
- `/mv` -> Validate the list (this skill)
