---
name: "wrps - Wrapper Skill Design"
description: Guides the design of skills that enhance other skills by accepting their output, adding a layer of analysis or validation, and returning enriched results.
---

# Wrapper Skill Design

**Input**: $ARGUMENTS

---

## Step 1: Define What Gets Wrapped

A wrapper skill takes another skill's output and makes it better.

```
WRAPPER NAME: [abbreviation]
WRAPS: [what kind of skill output it enhances]
ADDS: [what new layer it provides]
PRESERVES: [what it keeps unchanged from the original]
```

| Wrapper Type | What it adds | Example |
|-------------|-------------|---------|
| **Validator** | Checks the output for errors | "Verify all claims have evidence" |
| **Enricher** | Adds missing information | "Add confidence scores to each item" |
| **Challenger** | Stress-tests the output | "Find the weakest point in the analysis" |
| **Formatter** | Restructures for a new audience | "Turn analysis into executive summary" |
| **Synthesizer** | Combines outputs from multiple skills | "Merge perspectives into unified view" |

---

## Step 2: Define the Wrapping Contract

Specify what goes in and what comes out.

```
WRAPPING CONTRACT:
- Accepts: [types of skill output this wrapper can handle]
- Minimum input: [what must be present for the wrapper to work]
- Rejects: [what it can't wrap — be explicit]

OUTPUT:
- Original output: [preserved in full / summarized / referenced]
- Added layer: [what the wrapper contributes]
- Combined format: [how original + new layer are presented]
```

Rule: The original output must always be recoverable. A wrapper adds — it never destroys.

---

## Step 3: Design the Enhancement Layer

Define what the wrapper does to the wrapped output.

```
ENHANCEMENT STEPS:
1. RECEIVE: [accept the wrapped skill's output]
2. PARSE: [identify the key elements to enhance]
3. ANALYZE: [apply the wrapper's specific lens]
   - [sub-analysis 1]
   - [sub-analysis 2]
   - [sub-analysis 3]
4. ANNOTATE: [attach findings to the original output]
5. DELIVER: [present original + annotations together]
```

Constraint: Steps 2-4 should be completable without re-running the wrapped skill.

---

## Step 4: Handle Multiple Wrapped Skills

A good wrapper works with many different skill outputs.

```
COMPATIBILITY MATRIX:
| Wrapped Skill | What Wrapper Adds | Works Well? |
|--------------|-------------------|-------------|
| [skill 1] | [specific enhancement] | [yes/partial/no] |
| [skill 2] | [specific enhancement] | [yes/partial/no] |
| [skill 3] | [specific enhancement] | [yes/partial/no] |
| [skill 4] | [specific enhancement] | [yes/partial/no] |
```

If compatibility is "partial," note what's missing.
If compatibility is "no," the wrapper scope may be too narrow.

---

## Step 5: Preserve and Append

Design the output format that shows original and enhancement clearly.

```
OUTPUT FORMAT:

## Original Output
[The wrapped skill's complete output, unchanged]

## [Wrapper Name] Enhancement
[The wrapper's added analysis/validation/enrichment]

### Key Findings
- [finding 1]
- [finding 2]
- [finding 3]

### Recommendations
- [action 1 based on wrapper analysis]
- [action 2 based on wrapper analysis]
```

Rule: A reader should be able to ignore the enhancement and still use the original output.

---

## Step 6: Test With Multiple Skills

Verify the wrapper adds value across different skill outputs.

```
WRAP TEST 1:
- Wrapped skill: [name]
- Original output quality: [assessment]
- After wrapping: [what improved]
- Value added: [concrete benefit]

WRAP TEST 2:
- Wrapped skill: [name]
- Original output quality: [assessment]
- After wrapping: [what improved]
- Value added: [concrete benefit]

WRAP TEST 3:
- Wrapped skill: [name]
- Original output quality: [assessment]
- After wrapping: [what improved]
- Value added: [concrete benefit]
```

---

## Integration

Use with:
- `/chns` -> Design the wrapper as a chainable post-processing step
- `/injc` -> Consider if the wrapper could also work as a lightweight injectable
- `/stnl` -> Ensure the wrapper is also useful when given raw input (not just skill output)
