---
name: "dqnt - Data & Quantitative Analysis"
description: "Procedure for working with numbers and data. Clarifies questions, assesses data quality, performs analysis, checks for statistical traps, and communicates findings."
output:
  format: "prose"
---

# Data & Quantitative Analysis

**Input**: $ARGUMENTS

---

## Step 1: Clarify the Question

Data analysis without a clear question produces noise, not signal.

1. What specific question should the data answer?
2. What decision will this analysis inform?
3. What would a useful answer look like? (format, precision, timeframe)
4. What would change if the answer were X vs. Y?

```
QUESTION: [specific, answerable question]
DECISION IT INFORMS: [what action depends on this]
USEFUL ANSWER FORMAT: [e.g., "a percentage with confidence interval" or "a ranked list"]
```

If the question is vague ("analyze our data"), push back. A question like "are sales trending up?" is answerable. "Tell me about sales" is not.

---

## Step 2: Assess Data Availability and Quality

Before analysis, understand what you're working with.

1. **What data exists?** List available datasets/sources
2. **What's missing?** What data would you ideally have but don't?
3. **Quality checks**:
   - Completeness: What percentage of values are missing?
   - Accuracy: How was the data collected? Any known errors?
   - Timeliness: How current is the data?
   - Consistency: Are definitions and units consistent across the dataset?
   - Representativeness: Does the data represent the population you're asking about?

```
DATA AVAILABLE: [list of sources/datasets]
DATA MISSING: [what you wish you had]
QUALITY ASSESSMENT:
  Completeness:       [good / gaps / major gaps]
  Accuracy:           [high / moderate / uncertain]
  Timeliness:         [current / dated / stale]
  Consistency:        [consistent / some issues / inconsistent]
  Representativeness: [representative / biased / unknown]

PROCEED? [yes / yes with caveats / no — data insufficient]
```

If data quality is poor, state what conclusions CANNOT be drawn before proceeding. Poor data acknowledged is better than poor data ignored.

---

## Step 3: Choose Analysis Method

Match the method to the question type:

| Question Type | Methods |
|---|---|
| **"How much/many?"** | Descriptive stats (mean, median, range, distribution) |
| **"Is there a difference?"** | Comparison (t-test, ANOVA, chi-square, effect sizes) |
| **"Is there a relationship?"** | Correlation, regression |
| **"Is this trend real?"** | Time series, trend tests, regression with time |
| **"What predicts X?"** | Regression, classification, feature importance |
| **"Are these groups different?"** | Clustering, segmentation |
| **"Is this unusual?"** | Outlier detection, anomaly scores, z-scores |

```
CHOSEN METHOD: [method]
WHY: [matches the question because...]
ASSUMPTIONS REQUIRED: [what the method assumes about the data]
```

Check method assumptions against actual data. If assumptions are violated, note this and either choose a different method or proceed with documented caveats.

---

## Step 4: Perform the Analysis

Execute the chosen method. Document:

1. **Setup**: Any data transformations, filters, or exclusions applied
2. **Core results**: The numbers that answer the question
3. **Supporting details**: Sample sizes, confidence intervals, p-values, effect sizes
4. **Visualizations**: Describe what chart/graph would best communicate the finding

```
RESULTS:
- [primary finding with numbers]
- [confidence interval or uncertainty range]
- [sample size / degrees of freedom]
- [effect size if applicable]

BEST VISUALIZATION: [chart type and what it would show]
```

---

## Step 5: Check for Statistical Traps

Before trusting results, audit for common errors:

| Trap | Check | Status |
|---|---|---|
| **Small sample** | N >= 30 for parametric tests? Power adequate? | [ok / concern] |
| **Multiple comparisons** | Testing many hypotheses without correction? | [ok / concern] |
| **P-hacking** | Did you test multiple analyses and report the best? | [ok / concern] |
| **Confounders** | Could a third variable explain the relationship? | [ok / concern] |
| **Survivorship bias** | Are you only seeing data that "survived" some filter? | [ok / concern] |
| **Simpson's paradox** | Does the trend reverse when you split by subgroups? | [ok / concern] |
| **Base rate neglect** | Are you ignoring how common/rare the phenomenon is? | [ok / concern] |
| **Cherry-picked timeframe** | Would different start/end dates change the conclusion? | [ok / concern] |
| **Correlation as causation** | Are you implying X causes Y from correlation alone? | [ok / concern] |

```
TRAPS CHECKED: [count] of 9
CONCERNS FOUND: [list any concerns and their implications]
```

For each concern: state how it affects the conclusion and whether it can be mitigated.

---

## Step 6: Interpret Conservatively

Translate results into plain language, erring on the side of caution.

1. State what the data DOES support
2. State what the data does NOT support (even if tempting to claim)
3. Rate confidence: HIGH / MODERATE / LOW
4. State the uncertainty range in plain language

```
FINDING: [plain-language statement of what the data shows]
CONFIDENCE: [HIGH / MODERATE / LOW]
UNCERTAINTY: [what the range of plausible truths is]
DOES NOT SHOW: [what you cannot conclude from this data]
```

---

## Step 7: Communicate Findings

Structure the final communication:

1. **Headline**: One sentence, the key finding
2. **Context**: What was analyzed and why
3. **Key numbers**: 2-3 numbers that tell the story (not a data dump)
4. **Caveats**: What limits the conclusion (briefly)
5. **Recommendation**: What action the finding supports

```
REPORT:

HEADLINE: [one-sentence finding]

CONTEXT: [what was analyzed, data source, timeframe]

KEY NUMBERS:
- [number 1 with context]
- [number 2 with context]

CAVEATS: [most important limitation]

RECOMMENDATION: [what to do based on this]
```

---

## Integration

Use with:
- `/ht` -> Formally test a hypothesis the data suggests
- `/dcp` -> Feed quantitative findings into a decision
- `/cba` -> Use data to populate a cost-benefit analysis
- `/spec` -> Explore what the data might mean if trends continue
