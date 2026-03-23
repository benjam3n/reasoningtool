---
name: "tradestudy - Trade Study / Trade-off Analysis"
description: Systematically evaluate alternatives against weighted criteria using a structured decision matrix. Includes pairwise comparison for weighting, multi-criteria scoring, sensitivity analysis, and documented decision rationale.
output:
  format: "table"
---

# Trade Study / Trade-off Analysis

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Evaluate defined alternatives**: The user has specific alternatives they want to compare and needs a structured evaluation framework with weighted criteria to select the best option.
**Interpretation 2 — Generate AND evaluate alternatives**: The user has a decision to make but hasn't fully defined the alternatives yet. Needs help identifying options and then evaluating them systematically.
**Interpretation 3 — Validate a previous decision**: The user has already made a selection and wants to retroactively verify it was the right choice — or understand under what conditions a different choice would be better.

If ambiguous, ask: "I can help with evaluating specific alternatives you've already identified, generating and evaluating alternatives for a decision, or validating a decision you've already made — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/tradestudy 4x [input]").

| Depth | Min Alternatives | Min Criteria | Min Sensitivity Checks | Min Risk Factors | Documentation Detail |
|-------|-----------------|-------------|----------------------|-----------------|---------------------|
| 1x    | 2               | 4           | 2                    | 3               | Summary             |
| 2x    | 3               | 6           | 4                    | 5               | Standard            |
| 4x    | 4               | 8           | 6                    | 8               | Detailed            |
| 8x    | 5               | 10          | 8                    | 12              | Comprehensive       |
| 16x   | 6               | 12          | 10                   | 16              | Exhaustive          |

---

## The Process

### Step 1: Define the Decision Context

```
DECISION: [What decision is being made]
OBJECTIVE: [What outcome we're optimizing for]
SCOPE: [What's in and out of scope for this trade study]
CONSTRAINTS: [Hard constraints that any alternative must satisfy]
TIMELINE: [When this decision must be made]
DECISION AUTHORITY: [Who makes the final call]
REVERSIBILITY: [How reversible is this decision — one-way door / two-way door]

MUST-HAVE CRITERIA (pass/fail — alternatives that fail these are eliminated):
| # | Criterion | Threshold | Rationale |
|---|-----------|-----------|-----------|
| 1 | [criterion] | [minimum acceptable value] | [why this is non-negotiable] |
...
```

---

### Step 2: Define Alternatives

```
ALTERNATIVES:

| # | Alternative | Description | Key Differentiator | Status |
|---|------------|-------------|-------------------|--------|
| A | [name] | [what this option is] | [why it's distinct from others] | [PASSES must-haves / ELIMINATED] |
| B | [name] | [what this option is] | [why it's distinct from others] | [PASSES / ELIMINATED] |
| C | [name] | [what this option is] | [why it's distinct from others] | [PASSES / ELIMINATED] |
...

MUST-HAVE SCREENING:

| Alternative | Criterion 1 | Criterion 2 | Criterion 3 | ... | Result |
|------------|-------------|-------------|-------------|-----|--------|
| A | PASS/FAIL | PASS/FAIL | PASS/FAIL | | PROCEED/ELIMINATED |
| B | PASS/FAIL | PASS/FAIL | PASS/FAIL | | PROCEED/ELIMINATED |
...

ALTERNATIVE COMPLETENESS CHECK:
- [ ] "Do nothing" or "status quo" option included
- [ ] At least one low-risk/conservative option
- [ ] At least one innovative/aggressive option
- [ ] Hybrid or partial alternatives considered
- [ ] Alternatives are genuinely distinct (not minor variations)
```

---

### Step 3: Define and Weight Evaluation Criteria

```
EVALUATION CRITERIA:

| # | Criterion | Description | Measurement Method | Scale |
|---|-----------|-------------|-------------------|-------|
| 1 | [criterion name] | [what it measures] | [how to score it] | [1-5 or specific scale] |
...

CRITERIA CATEGORIES:
- Technical: [performance, reliability, scalability, maintainability, security]
- Cost: [development cost, operational cost, total cost of ownership]
- Schedule: [time to deliver, time to value, implementation complexity]
- Risk: [technical risk, schedule risk, organizational risk]
- Strategic: [alignment with strategy, future flexibility, competitive advantage]
```

#### Pairwise Comparison for Weighting

Compare each criterion pair to determine relative importance:

```
PAIRWISE COMPARISON MATRIX:

Which criterion is MORE important? Score: 1 = equal, 3 = moderately more, 5 = strongly more, 7 = very strongly more, 9 = extremely more

| Criterion ↓ vs → | C1 | C2 | C3 | C4 | C5 | C6 | Row Sum | Weight |
|-------------------|----|----|----|----|----|----|---------|--------|
| C1: [name] | 1 | [score] | [score] | [score] | [score] | [score] | [sum] | [%] |
| C2: [name] | [1/score] | 1 | [score] | [score] | [score] | [score] | [sum] | [%] |
| C3: [name] | [1/score] | [1/score] | 1 | [score] | [score] | [score] | [sum] | [%] |
...
| **Total** | | | | | | | [total] | 100% |

CONSISTENCY CHECK:
- Verify no circular preferences (A > B > C > A)
- Verify weights sum to 100%
- Flag any surprising weights for stakeholder validation

WEIGHT INDEPENDENCE CHECK:
- Did you set these weights before or after you had a sense of which
  alternative would win? If after, re-derive weights by asking "which
  criterion matters most for the OBJECTIVE" without reference to how
  alternatives score.
```

---

### Step 4: Score Alternatives Against Criteria

```
SCORING RUBRIC:

For each criterion, define what each score means:

| Score | Meaning |
|-------|---------|
| 5 | Excellent — fully meets or exceeds the criterion |
| 4 | Good — meets the criterion with minor gaps |
| 3 | Adequate — meets the criterion at minimum acceptable level |
| 2 | Poor — partially meets the criterion with significant gaps |
| 1 | Unacceptable — fails to meet the criterion |

DETAILED SCORING:

Criterion 1: [Name] (Weight: [X]%)
| Alternative | Score | Evidence/Rationale |
|------------|-------|-------------------|
| A | [1-5] | [specific justification] |
| B | [1-5] | [specific justification] |
| C | [1-5] | [specific justification] |

Criterion 2: [Name] (Weight: [X]%)
| Alternative | Score | Evidence/Rationale |
|------------|-------|-------------------|
| A | [1-5] | [specific justification] |
| B | [1-5] | [specific justification] |
| C | [1-5] | [specific justification] |

[...repeat for all criteria...]

WEIGHTED DECISION MATRIX:

| Criterion | Weight | Alt A Raw | Alt A Weighted | Alt B Raw | Alt B Weighted | Alt C Raw | Alt C Weighted |
|-----------|--------|-----------|---------------|-----------|---------------|-----------|---------------|
| [C1] | [W1] | [score] | [score × W1] | [score] | [score × W1] | [score] | [score × W1] |
| [C2] | [W2] | [score] | [score × W2] | [score] | [score × W2] | [score] | [score × W2] |
...
| **TOTAL** | **100%** | | **[sum]** | | **[sum]** | | **[sum]** |
| **RANK** | | | **[rank]** | | **[rank]** | | **[rank]** |
```

---

### Step 5: Sensitivity Analysis

Test how robust the result is to changes in weights and scores:

```
SENSITIVITY ANALYSIS:

WEIGHT SENSITIVITY:
For each criterion, how much would the weight need to change to alter the winner?

| Criterion | Current Weight | Break-Even Weight | Sensitivity | Impact |
|-----------|---------------|-------------------|------------|--------|
| [C1] | [current %] | [weight at which winner changes] | [HIGH/MED/LOW] | [which alternative would win] |
...

SCORE SENSITIVITY:
For the winning alternative's lowest-scored criteria, what if that score dropped by 1?

| Scenario | Changed Score | New Winner? | New Ranking |
|----------|-------------|-------------|-------------|
| [criterion X] score drops from [N] to [N-1] | [new total] | [YES — Alt B wins / NO] | [new ranking] |
...

SCENARIO ANALYSIS:

| Scenario | Weight/Score Change | Winner | Margin | Confidence |
|----------|-------------------|--------|--------|-----------|
| Base case | (none) | [Alt A] | [margin over #2] | [HIGH/MED/LOW] |
| Emphasize cost | Cost weight +10% | [winner] | [margin] | |
| Emphasize performance | Performance weight +10% | [winner] | [margin] | |
| Pessimistic for winner | Winner's uncertain scores -1 | [winner] | [margin] | |
| Optimistic for runner-up | Runner-up's uncertain scores +1 | [winner] | [margin] | |

OVERALL ROBUSTNESS: [ROBUST — winner is clear / SENSITIVE — small changes alter the result / INCONCLUSIVE — alternatives are too close to distinguish]
```

---

### Step 6: Document Decision Rationale

```
RECOMMENDATION: [Alternative Name]

DECISION SUMMARY:
- Winner: [Alternative] with weighted score of [X]
- Runner-up: [Alternative] with weighted score of [Y]
- Margin: [X - Y] ([percentage]%)
- Confidence: [HIGH/MEDIUM/LOW]

WHY THIS ALTERNATIVE:
- [Primary reason — strongest criterion performance]
- [Secondary reason]
- [Strategic alignment reason]

WHY NOT THE OTHERS:

| Rejected Alternative | Primary Reason for Rejection | Under What Conditions It Would Win |
|---------------------|-----------------------------|------------------------------------|
| [Alt B] | [key weakness] | [if criterion X were more important] |
| [Alt C] | [key weakness] | [if criterion Y were more important] |
...

RISKS OF SELECTED ALTERNATIVE:

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|-----------|
| 1 | [risk] | [HIGH/MED/LOW] | [HIGH/MED/LOW] | [how to address] |
...

IMPLEMENTATION CONSIDERATIONS:
- Prerequisites: [what must be in place before implementing]
- Key milestones: [major checkpoints]
- Reversibility: [how to change course if this proves wrong]
- Monitoring: [what to watch to confirm this was the right choice]

DECISION RECORD:
- Decision made: [date or TBD]
- Decision maker: [who]
- Stakeholders consulted: [who was involved]
- Review date: [when to revisit this decision]
```

---

## Output Format

```
## TRADE STUDY: [Decision Name]

### 1. Decision Context
[Objective, scope, constraints, timeline]

### 2. Alternatives
[List of alternatives with must-have screening results]

### 3. Evaluation Criteria and Weights
[Criteria definitions, pairwise comparison, final weights]

### 4. Weighted Decision Matrix
[Scores, weighted scores, totals, ranking]

### 5. Sensitivity Analysis
[Weight sensitivity, score sensitivity, scenario analysis, robustness assessment]

### 6. Recommendation
[Selected alternative with rationale, rejected alternatives with conditions for reconsideration]

### 7. Risks and Mitigations
[Risks of selected alternative with mitigations]

### 8. Decision Record
[Who, when, review date]
```

---

## Quality Checklist

Before completing:
- [ ] Decision context clearly defined with objective and constraints
- [ ] Must-have criteria used to screen alternatives before scoring
- [ ] Alternatives are genuinely distinct (not minor variations)
- [ ] "Do nothing" or status quo option considered
- [ ] Criteria cover technical, cost, schedule, risk, and strategic dimensions
- [ ] Weights derived from pairwise comparison (not arbitrary)
- [ ] Consistency of pairwise comparisons verified
- [ ] Every score has documented evidence or rationale
- [ ] Sensitivity analysis performed on weights and scores
- [ ] Robustness of result assessed
- [ ] Decision rationale documents why winner was chosen AND why others were not
- [ ] Risks of selected alternative identified with mitigations
- [ ] Conditions for revisiting the decision documented

---

## Next Steps

After trade study:
1. Use `/requirements` to derive requirements from the selected alternative
2. Use `/sysarch` to design architecture based on the selected approach
3. Use `/stakeholder` to communicate the decision to affected stakeholders
4. Use `/fla` to anticipate failure modes of the selected alternative
5. Use `/dcp` to create decision procedures for implementation choices
6. Use `/conops` to update operational concept based on the selection
