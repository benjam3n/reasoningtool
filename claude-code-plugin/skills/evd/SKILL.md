---
name: evd
description: "Universal dimensions for evaluating any claim, problem, or solution."
---

# Evaluation Dimensions

**Input**: $ARGUMENTS

---

## Overview

Universal dimensions for evaluating any claim, problem, or solution. Use external grounding to assess claims on these dimensions when ARAW alone cannot determine them.

External grounding helps:
1. Find problems/solutions ARAW wouldn't find (blind spots)
2. Verify ARAW outputs on these dimensions
3. Calibrate confidence in ARAW findings

## Steps

### Step 1: Identify What's Being Evaluated
1. Is it a CLAIM (something asserted to be true)?
2. Is it a PROBLEM (something needing solution)?
3. Is it a SOLUTION (something proposed to address a problem)?
4. Is it a PLAN (something proposed to achieve a goal)?
5. Is it an OUTPUT (something produced)?

### Step 2: Apply Universal Dimensions

**Truth / Accuracy:**
- Is it factually correct?
- Are the claims verifiable?
- What evidence supports it? What contradicts?
- What's the confidence level?
- → Check with external sources, data, domain experts

**Completeness:**
- Does it address everything it should?
- What's missing?
- Are edge cases covered?
- Are limitations acknowledged?
- → Compare against known frameworks, checklists, standards

**Consistency:**
- Does it contradict itself internally?
- Does it contradict established knowledge?
- Does it contradict other claims by the same source?
- → Cross-reference across the output and against known facts

**Relevance:**
- Does it address the actual question/problem?
- Is everything included actually necessary?
- Is the scope appropriate (not too broad, not too narrow)?
- → Compare the output against the original objective

**Feasibility:**
- Can it actually be done?
- With available resources?
- In the available time?
- Given real-world constraints?
- → Check against physical, financial, organizational, and technical reality

**Robustness:**
- Does it work under normal conditions only, or also under stress?
- What happens when assumptions are violated?
- How sensitive is it to small changes in inputs?
- → Stress-test with edge cases, adversarial inputs, changed assumptions

**Originality / Value-Add:**
- Does it say anything new or just restate known things?
- Does it provide insight beyond the obvious?
- Is the framing itself valuable even if content is known?
- → Compare against what's already known/available

**Actionability:**
- Can someone act on this?
- Are next steps clear?
- Is it specific enough to guide action?
- → Ask: "What would I do differently after reading this?"

**Fairness / Balance:**
- Are all perspectives represented?
- Is evidence selectively presented?
- Are counterarguments acknowledged?
- → Look for what's conspicuously absent

**Clarity:**
- Can the target audience understand it?
- Are terms defined?
- Is the structure logical?
- → Show to a representative reader and check comprehension

### Step 3: Score Each Dimension

| Dimension | Score (1-5) | Key Evidence | Improvement Needed? |
|-----------|------------|-------------|-------------------|
| Truth/Accuracy | | | |
| Completeness | | | |
| Consistency | | | |
| Relevance | | | |
| Feasibility | | | |
| Robustness | | | |
| Originality | | | |
| Actionability | | | |
| Fairness | | | |
| Clarity | | | |

**Not all dimensions are equally important for every evaluation.** Weight by context:
- For claims: Truth, Consistency, and Fairness matter most
- For solutions: Feasibility, Robustness, and Actionability matter most
- For plans: Completeness, Feasibility, and Clarity matter most
- For outputs: Clarity, Relevance, and Accuracy matter most

### Step 4: Identify Critical Gaps
1. Which dimensions score below 3?
2. For each low score: is this fixable or fundamental?
3. Which low scores are most important given the evaluation type?
4. What would it take to raise each critical dimension?

### Step 5: Report
```
EVALUATION DIMENSIONS:
Subject: [what was evaluated]
Type: [claim/problem/solution/plan/output]

| Dimension | Score | Weight | Weighted | Key Finding |
|-----------|-------|--------|----------|-------------|
| [dim] | [1-5] | [H/M/L] | [score] | [finding] |

Overall: [weighted average or qualitative summary]
Critical gaps: [dimensions below 3 that matter]
Improvement path: [what would most improve the evaluation]

External grounding used: [what sources/methods supplemented ARAW]
ARAW blind spots found: [what external grounding caught that ARAW missed]
```

## When to Use
- Evaluating any claim, solution, or output
- When ARAW has been applied but you want dimensional verification
- When you need to communicate evaluation results systematically
- → INVOKE: /cv (convergent validation) for multi-method verification
- → INVOKE: /evaluate (category skill) for routing to appropriate evaluation

## Verification
- [ ] Evaluation type correctly identified
- [ ] All 10 dimensions considered
- [ ] Dimensions weighted by relevance to evaluation type
- [ ] External grounding used (not just internal reasoning)
- [ ] Critical gaps identified with improvement paths
