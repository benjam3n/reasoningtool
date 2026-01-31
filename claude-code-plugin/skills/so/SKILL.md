---
name: so
description: "Standardized output format for GOSM projects."
---

# Structured Output Format

**Input**: $ARGUMENTS

---

## Overview

Standardized output format for GOSM projects. Problem: Current outputs are markdown files — good for reading, hard to analyze. Solution: Structured format that enables cross-project synthesis.

Like ARAW uses databases for synthesis, GOSM needs structured project records.

## Steps

### Step 1: Identify Output Type
What kind of output is being produced?

| Output Type | Key Fields | Example |
|------------|-----------|---------|
| Analysis | claim, evidence, confidence, caveats | ARAW result |
| Decision | options, criteria, scores, selection | DCP result |
| Plan | goals, steps, dependencies, timeline | Project plan |
| Diagnosis | symptoms, causes, evidence, fix | RCA result |
| Evaluation | subject, dimensions, scores, verdict | Evaluation result |
| Review | findings, severity, recommendations | Audit result |

### Step 2: Apply Standard Structure
Every output includes these sections:

```
HEADER:
  type: [analysis|decision|plan|diagnosis|evaluation|review]
  skill: [which procedure produced this]
  input: [what was analyzed]
  date: [when]
  confidence: [overall confidence: high|medium|low]

SUMMARY:
  one_line: [single sentence result]
  verdict: [the bottom line]
  key_finding: [most important thing discovered]

BODY:
  [type-specific fields — see Step 3]

METADATA:
  assumptions: [what was assumed]
  limitations: [what this analysis can't address]
  follow_ups: [what should be investigated next]
  related: [links to related analyses]
```

### Step 3: Type-Specific Body Fields

**Analysis body:**
```
claims:
  - claim: [statement]
    evidence_for: [supporting evidence]
    evidence_against: [contradicting evidence]
    confidence: [H/M/L]
    status: [supported|refuted|uncertain]
```

**Decision body:**
```
options:
  - name: [option]
    pros: [advantages]
    cons: [disadvantages]
    score: [weighted score]
selected: [chosen option]
rationale: [why this one]
```

**Plan body:**
```
goal: [what we're trying to achieve]
steps:
  - step: [description]
    depends_on: [prerequisites]
    output: [what this step produces]
    risk: [what could go wrong]
```

**Diagnosis body:**
```
symptoms: [what was observed]
hypotheses:
  - cause: [possible cause]
    evidence: [supporting/contradicting]
    probability: [H/M/L]
root_cause: [most likely cause]
fix: [recommended action]
```

**Evaluation body:**
```
subject: [what was evaluated]
dimensions:
  - dimension: [evaluation criterion]
    score: [rating]
    evidence: [basis for score]
overall: [aggregate assessment]
```

**Review body:**
```
findings:
  - finding: [what was found]
    severity: [critical|major|minor|info]
    recommendation: [what to do]
    status: [new|known|resolved]
```

### Step 4: Cross-Output Synthesis
Structured outputs enable:
1. **Trend analysis**: Compare confidence levels across analyses
2. **Decision tracking**: Review past decisions and outcomes
3. **Assumption auditing**: Find shared assumptions across projects
4. **Gap identification**: What hasn't been analyzed?
5. **Contradiction detection**: Where do analyses disagree?

### Step 5: Convert Current Output
If applying to existing output:
1. Read the unstructured output
2. Extract fields for the appropriate type
3. Identify anything that doesn't fit standard fields → add to metadata
4. Fill in any missing standard fields (especially limitations and assumptions)
5. Output in structured format

### Step 6: Report
Format the input according to the appropriate structured output template. If the input is a request to format something, apply the template. If it's a question about the format, explain the relevant section.

## When to Use
- When producing output from any GOSM procedure
- When standardizing existing outputs for synthesis
- When designing new output formats
- When comparing results across multiple analyses

## Verification
- [ ] Output type correctly identified
- [ ] All standard header fields present
- [ ] Summary is genuinely one line (not a paragraph)
- [ ] Confidence level justified
- [ ] Assumptions and limitations explicitly stated
- [ ] Follow-ups identified
