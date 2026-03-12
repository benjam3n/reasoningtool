---
name: "dtsk - Data Analysis"
description: "Work with data systematically: assess what exists, evaluate quality, identify gaps, choose methods, interpret results, and communicate findings."
output:
  format: "prose"
---

# DTSK - Data Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify What Data Exists

```
DATA INVENTORY:
  1. [data source/set] — FORMAT: [type] — SIZE: [approximate]
     CONTAINS: [what variables or fields]
     TIMEFRAME: [period covered]
  2. [data source/set] — FORMAT: [type]
     CONTAINS: [variables]
     TIMEFRAME: [period]
```

Don't assume data exists just because it should. Inventory only what's actually available and accessible.

---

## Step 2: Assess Data Quality

For each data source:

```
QUALITY ASSESSMENT: [data source name]
  COMPLETENESS: [percentage or description of missing values]
  ACCURACY: [how was data collected? what error sources exist?]
  TIMELINESS: [how current is it? is staleness a problem?]
  CONSISTENCY: [are definitions and formats uniform?]
  PROVENANCE: [where did it come from? how trustworthy is the source?]
  OVERALL QUALITY: [high | adequate | questionable | unreliable]
  CAVEATS: [what limitations must be kept in mind during analysis]
```

Poor data quality is the most common source of wrong conclusions. Assess before analyzing.

---

## Step 3: Identify Missing Data

```
DATA GAPS:
  1. NEEDED: [what data would answer the question]
     WHY MISSING: [not collected | inaccessible | doesn't exist yet]
     IMPACT: [what conclusions become impossible without it]
     PROXY: [alternative data that could partially substitute, if any]
  2. NEEDED: [data]
     WHY MISSING: [reason]
     IMPACT: [limitation]
     PROXY: [substitute, if any]
```

The absence of data is itself data. What wasn't measured often matters as much as what was.

---

## Step 4: Choose Analysis Methods

```
QUESTION: [the specific question the data should answer]

METHOD: [chosen analysis approach]
  WHY THIS METHOD: [what makes it appropriate for this data and question]
  ASSUMPTIONS: [what the method assumes about the data]
  ASSUMPTIONS MET: [yes | partially | no — with specifics]
  ALTERNATIVES CONSIDERED: [other methods and why they were rejected]
  LIMITATIONS: [what this method cannot tell you]
```

Match the method to the question and the data, not the other way around. If the data doesn't support the method, change the method.

---

## Step 5: Interpret Results

```
FINDINGS:
  1. [finding] — CONFIDENCE: [high | medium | low]
     EVIDENCE: [what in the data supports this]
  2. [finding] — CONFIDENCE: [level]
     EVIDENCE: [supporting data]

CORRELATION VS CAUSATION CHECK:
  CORRELATIONS FOUND: [list]
  CAUSAL CLAIMS SUPPORTED: [which, if any, and what additional evidence exists]
  CONFOUNDERS: [potential third variables]
  DIRECTION: [is the causal direction clear?]

ALTERNATIVE EXPLANATIONS:
  1. [finding] could also be explained by [alternative]
  2. [finding] could also be explained by [alternative]
```

Default to correlation until you have strong evidence for causation: temporal precedence, plausible mechanism, and elimination of confounders.

---

## Step 6: Communicate Findings

```
DATA BRIEF
==========
QUESTION: [what we asked]
DATA USED: [sources, with quality notes]
KEY FINDINGS:
  1. [finding with confidence level]
  2. [finding with confidence level]
  3. [finding with confidence level]

WHAT THE DATA SAYS: [clear statement of conclusions]
WHAT THE DATA DOES NOT SAY: [common misinterpretations to prevent]
LIMITATIONS: [caveats the audience must understand]
RECOMMENDED NEXT STEPS: [what additional data or analysis would strengthen conclusions]
```

Communicate uncertainty explicitly. "The data suggests X with moderate confidence" is more honest and more useful than "X is true."

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Analyzing before assessing quality** | Jumping to method before checking data | Always do Step 2 before Step 4 |
| **Claiming causation from correlation** | "X causes Y" from observational data | State correlation; list confounders |
| **Ignoring missing data** | Conclusions based only on what's present | Missing data can bias everything — account for it |
| **Method-driven analysis** | Choosing a method first, then fitting data to it | Start with the question, then pick the method |
| **Overconfident communication** | Stating findings without uncertainty ranges | Always include confidence levels and limitations |
| **Cherry-picking** | Reporting only findings that support the desired conclusion | Report all findings, especially surprising ones |

---

## Integration

- Use with: `/agsk` to evaluate whether data-based arguments are sound
- Use with: `/cmpr` to check if the analysis is complete
- Use with: `/prvn` to validate needs using data evidence
- Use from: `/claim` when a claim needs data-based testing
- Differs from `/agsk`: dtsk works with empirical data; agsk works with logical arguments
