---
name: "omtx - Matrix Generation"
description: Generates comparison and analysis matrices. Takes items and dimensions, fills cells with evidence-based assessments, and highlights patterns across the matrix.
---

# Matrix Generation

**Input**: $ARGUMENTS

---

## Step 1: Identify Rows

Determine what is being compared. Rows are the items, options, or entities under analysis.

```
ROWS (items being compared):
1. [item 1]
2. [item 2]
3. [item 3]
...
```

Rules:
- Items should be at the same level of abstraction
- 3-7 rows is ideal; more than 10 becomes unwieldy
- If too many items, group or filter first

---

## Step 2: Identify Columns

Determine the dimensions or criteria for comparison.

```
COLUMNS (dimensions/criteria):
1. [criterion 1] — [what it measures]
2. [criterion 2] — [what it measures]
3. [criterion 3] — [what it measures]
...
```

Rules:
- Columns should be independent (not redundant)
- Each column must be assessable for every row
- Include both quantitative and qualitative dimensions where relevant
- Weight columns if some criteria matter more than others

```
WEIGHTS (if applicable):
- [criterion]: [weight or priority level]
```

---

## Step 3: Fill Cells

Populate each cell with an evidence-based assessment.

Rules:
- Use consistent scales (High/Medium/Low, 1-5, Yes/No, or specific values)
- State the basis for each assessment — no unsupported ratings
- Flag cells where data is uncertain or missing
- Avoid false precision: "~70%" is better than "72.3%" without data

```
SCALE: [the rating system used]

| | [Col 1] | [Col 2] | [Col 3] | ... |
|---|---|---|---|---|
| [Row 1] | [assessment] | [assessment] | [assessment] | |
| [Row 2] | [assessment] | [assessment] | [assessment] | |
| [Row 3] | [assessment] | [assessment] | [assessment] | |
```

---

## Step 4: Highlight Patterns

Analyze the completed matrix for structural insights:

| Pattern | What to look for |
|---------|-----------------|
| **Dominance** | One row scores best on most/all columns |
| **Trade-offs** | Rows that win on some columns but lose on others |
| **Clusters** | Groups of rows with similar profiles |
| **Outliers** | A row that scores very differently on one column |
| **Deal-breakers** | A single cell that eliminates a row regardless of other scores |
| **Parity** | Rows that are effectively identical across all columns |

```
PATTERNS FOUND:
- [pattern 1]: [description]
- [pattern 2]: [description]
...
```

---

## Step 5: Summarize Findings

Synthesize what the matrix reveals:

```
MATRIX SUMMARY:

STRONGEST OPTION: [row] — [why]
KEY TRADE-OFF: [row A] vs [row B] — [what you give up for what you gain]
SURPRISING FINDING: [anything the matrix revealed that wasn't obvious]
DECISION IMPLICATION: [what this matrix suggests you should do]
```

If no single option dominates, state that clearly and explain what additional information or criteria would break the tie.

---

## Integration

Use with:
- `/olst` -> Generate the list of items before building the matrix
- `/cmp` -> Deep-dive comparison on the top 2-3 options
- `/odec` -> Turn matrix findings into a decision recommendation
- `/cba` -> Add cost-benefit analysis to the matrix dimensions
