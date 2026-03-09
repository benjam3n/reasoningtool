---
name: "anst - Analysis Stage"
description: Structured deep analysis after exploration. Selects what to analyze, applies frameworks, finds patterns, tests hypotheses, and synthesizes findings.
---

# Analysis Stage

**Input**: $ARGUMENTS

---

## Step 1: Select What to Analyze

Not everything found during exploration deserves deep analysis. Choose deliberately.

```
ANALYSIS TARGETS:
- From exploration: [what exploration/orientation surfaced]
- Selected for analysis:
  1. [target 1] — reason: [why this matters most]
  2. [target 2] — reason: [why this matters]
  3. [target 3] — reason: [why this matters]
- Deliberately excluded: [what we're NOT analyzing and why]
```

Rule: Analyze no more than 3 targets. Depth beats breadth at this stage.

---

## Step 2: Choose Analytical Frameworks

Match the right lens to each target.

```
FRAMEWORK SELECTION:

| Target | Framework | Why This Framework |
|--------|-----------|-------------------|
| [target 1] | [framework] | [what it reveals] |
| [target 2] | [framework] | [what it reveals] |
| [target 3] | [framework] | [what it reveals] |

AVAILABLE FRAMEWORKS:
- Causal: What causes what? (root cause, dependencies)
- Comparative: How does X differ from Y? (tradeoffs, alternatives)
- Structural: How is this organized? (components, relationships)
- Temporal: How does this change over time? (trends, phases)
- Constraint: What limits this? (bottlenecks, boundaries)
```

SKIP: If the target clearly calls for one framework, state it and move on.

---

## Step 3: Apply the Analysis

Run each target through its chosen framework.

For each target:

```
ANALYSIS: [target name]
Framework: [chosen framework]

FINDINGS:
1. [finding 1 — specific, evidenced]
2. [finding 2 — specific, evidenced]
3. [finding 3 — specific, evidenced]

KEY INSIGHT: [the single most important thing this analysis revealed]

CONFIDENCE: [high / medium / low] — because [basis for confidence level]
```

---

## Step 4: Look for Patterns

Search across all analysis targets for recurring themes.

```
CROSS-TARGET PATTERNS:
1. [pattern]: Appears in [target A] and [target B]
   Significance: [what this pattern means]
2. [pattern]: Appears in [target A] and [target C]
   Significance: [what this pattern means]

CONTRADICTIONS:
- [target A] suggests [X] but [target B] suggests [Y]
  Resolution: [how to reconcile, or "unresolved"]
```

SKIP: If analyzing only one target, skip cross-target patterns.

---

## Step 5: Test Hypotheses

State and test the key claims emerging from analysis.

```
HYPOTHESIS TESTING:

Hypothesis 1: [statement]
- Supporting evidence: [what backs this up]
- Contradicting evidence: [what challenges this]
- Verdict: [supported / weakened / inconclusive]

Hypothesis 2: [statement]
- Supporting evidence: [what backs this up]
- Contradicting evidence: [what challenges this]
- Verdict: [supported / weakened / inconclusive]
```

---

## Step 6: Synthesize Findings

Combine everything into a coherent picture.

```
SYNTHESIS:

SITUATION: [one sentence — what's going on]
KEY FINDINGS:
1. [most important finding]
2. [second most important]
3. [third most important]

REMAINING UNCERTAINTIES:
- [what we still don't know]
- [what would change the analysis if learned]

RECOMMENDED NEXT STEP: [what should happen next based on these findings]
```

---

## Integration

Use with:
- `/exps` -> Explore the space before analyzing it
- `/dcst` -> Move from analysis to decision
- `/ht` -> Test specific hypotheses more rigorously
- `/rca` -> If analysis reveals a root cause problem
