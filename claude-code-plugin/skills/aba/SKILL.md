---
name: "aba - AI Biomedical Agent"
description: "Procedure for using AI to analyze biomedical research, evaluate studies, assess drug interactions, and interpret clinical data."
---

# AI Biomedical Agent

**Input**: $ARGUMENTS

---

## Overview

Systematic procedure for analyzing biomedical questions using structured evidence evaluation. Searches literature, assesses study quality, synthesizes findings, and identifies limitations. Does NOT provide medical advice — produces structured analysis for informed decision-making.

## Step 0: Scope and Safety Check

1. State the biomedical question precisely
2. Classify: basic science / clinical / pharmacological / epidemiological
3. **Safety gate**: If the question is "should I take/stop medication X?" — output is ANALYSIS ONLY, not recommendation. Flag explicitly.
4. Identify what kind of evidence would answer this (RCTs, meta-analyses, case studies, mechanistic)

## Steps

### Step 1: Define the Research Question
1. Convert to PICO format where applicable:
   - **P**opulation: Who/what is being studied?
   - **I**ntervention: What treatment/exposure?
   - **C**omparison: Compared to what?
   - **O**utcome: What result matters?
2. If not clinical, define: Subject, Mechanism, Evidence type needed
3. Identify key terms and synonyms for search

### Step 2: Search and Gather Evidence
1. Identify source hierarchy:
   - Systematic reviews / meta-analyses (highest)
   - Randomized controlled trials
   - Observational studies (cohort, case-control)
   - Case reports / expert opinion (lowest)
2. Search: key terms, MeSH terms, known databases
3. Note what you can and cannot access
4. Flag if evidence base is thin (<3 relevant studies)

### Step 3: Assess Evidence Quality
For each piece of evidence:
1. Study design strength
2. Sample size and statistical power
3. Bias risk: selection, performance, detection, attrition, reporting
4. Conflict of interest (funding, author affiliations)
5. Replication status
6. Assign tier: A (strong) / B (moderate) / C (weak) / D (very weak)

### Step 4: Synthesize Findings
1. What do highest-quality studies show?
2. Consensus or disagreement? If disagreement, what explains it?
3. Effect size (not just significance — how large?)
4. Confidence intervals
5. Dose-response relationship if applicable

### Step 5: Assess Drug Interactions (if applicable)
1. Identify all substances mentioned
2. Check interaction mechanisms: CYP450, protein binding, pharmacodynamic
3. Severity: major / moderate / minor / theoretical
4. Evidence basis for each interaction

### Step 6: Identify Limitations and Gaps
1. What questions remain unanswered?
2. What populations are understudied?
3. Where is evidence weakest?
4. What would change the conclusion if discovered?

### Step 7: Report
```
BIOMEDICAL ANALYSIS
Question: [PICO or structured question]
Evidence tier: [A/B/C/D overall]

Key findings:
1. [finding] — Evidence: [tier] — Source: [type]
2. [finding] — Evidence: [tier] — Source: [type]

Synthesis: [what the evidence overall suggests]
Confidence: [high/moderate/low] — [reasoning]

Limitations:
- [limitation 1]
- [limitation 2]

NOT medical advice. Analysis only.
```

## When to Use
- Evaluating biomedical research claims
- Understanding drug mechanisms or interactions
- Interpreting clinical study results
- Assessing evidence for health interventions

## Verification
- [ ] Question stated in structured format
- [ ] Evidence sources identified with quality tiers
- [ ] Study quality assessed (not just cited)
- [ ] Effect sizes reported (not just significance)
- [ ] Limitations explicitly stated
- [ ] No medical advice given — analysis only
