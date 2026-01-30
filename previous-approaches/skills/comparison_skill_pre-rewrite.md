---
name: comparison
description: "Evaluate each option against each criterion to identify viable candidates. Includes evidence-based scoring guidance for LLM consistency."
context: fork
---

# Comparison

**Input**: $ARGUMENTS

---

## Overview

Evaluate each option against each criterion to identify viable candidates. This procedure provides specific scoring guidance to ensure consistent LLM application.

---

## Step 0: Context Assessment

| Factor | Value | Notes |
|--------|-------|-------|
| Stakes | HIGH / MED / LOW | |
| Reversibility | EASY / HARD / IMPOSSIBLE | |
| Options count | Few (<5) / Many (5+) | |
| Evidence quality | STRONG / MIXED / WEAK | |

**If HIGH stakes + HARD/IMPOSSIBLE reversibility**: Include Step 7 (Empirical Validation)
**If WEAK evidence**: Note uncertainty ranges throughout

---

## Step 1: Prepare Evaluation Framework

Set up the comparison structure.

**Actions**:
1. List all options from input
2. List all criteria from matching/input
3. Group criteria by type: REQUIRED, EXCLUSION, PREFERRED, OPTIONAL
4. Confirm weights (default equal if not specified)
5. Create evaluation matrix

**Criteria types**:
| Type | Meaning | Scoring |
|------|---------|---------|
| REQUIRED | Must have to proceed | PASS/FAIL |
| EXCLUSION | Must NOT have | PASS/FAIL |
| PREFERRED | Better to have | 0-3 weighted |
| OPTIONAL | Nice to have | 0-1 bonus |

**Output format**:
```
EVALUATION FRAMEWORK
====================
Options: [list]

Criteria:
REQUIRED:
- [criterion 1] (weight: 1.0)
- ...

EXCLUSION:
- [criterion 1]
- ...

PREFERRED:
- [criterion 1] (weight: [w])
- ...

OPTIONAL:
- [criterion 1]
- ...
```

---

## Step 2: Apply REQUIRED Criteria

For each option, check each REQUIRED criterion.

**Scoring**: PASS / FAIL / UNCERTAIN

**LLM Scoring Guidance (REQUIRED)**:
| Score | Meaning | Evidence needed |
|-------|---------|-----------------|
| PASS | Clearly meets requirement | Direct statement or obvious inference |
| FAIL | Clearly does not meet | Direct contradiction or missing required element |
| UNCERTAIN | Cannot determine | No evidence either way |

**Process**:
1. State the requirement
2. Search for evidence in option description/context
3. Score with reasoning
4. If UNCERTAIN with HIGH stakes, flag for clarification

**Output format**:
```
REQUIRED CRITERIA EVALUATION
============================
Option: [name]

| Criterion | Score | Evidence |
|-----------|-------|----------|
| [criterion] | PASS/FAIL/UNCERTAIN | [what supports this score] |
| ... | ... | ... |

Result: [VIABLE / ELIMINATED / NEEDS CLARIFICATION]
If eliminated: [which criterion caused elimination]
```

**An option FAILS overall if it fails ANY required criterion.**
Mark failed options as eliminated but continue evaluating for learning.

---

## Step 3: Apply EXCLUSION Criteria

For each remaining option, check each EXCLUSION criterion.

**Scoring**: PASS (doesn't have exclusion) / FAIL (has exclusion)

**LLM Scoring Guidance (EXCLUSION)**:
| Score | Meaning | Evidence needed |
|-------|---------|-----------------|
| PASS | Does not have excluded characteristic | No evidence of exclusion found |
| FAIL | Has excluded characteristic | Direct evidence of exclusion |

**Process**:
1. State what the criterion excludes
2. Check if option has excluded characteristic
3. Score with evidence

**An option FAILS if it matches ANY exclusion criterion.**

---

## Step 4: Score PREFERRED Criteria

For each viable option, score each PREFERRED criterion.

**LLM Scoring Guidance (PREFERRED)** - **Use this scale consistently**:

| Score | Label | Meaning | Evidence Required |
|-------|-------|---------|-------------------|
| 0 | None | No support for this criterion | No evidence found in input |
| 1 | Partial | Weak or indirect support | Indirect evidence OR stated but not demonstrated |
| 2 | Good | Direct support with minor gaps | Direct evidence, mostly complete |
| 3 | Excellent | Strong support, exceeds expectations | Multiple lines of evidence, comprehensive |

**Uncertainty Handling**:
If evidence is ambiguous, use a **range** instead of point estimate:
- "1-2" means "between partial and good, uncertain"
- Always explain what would resolve the uncertainty

**Process per criterion**:
1. State the preference
2. Evaluate how well option satisfies it
3. Cite specific evidence for score
4. Apply weight: weighted_score = score * weight
5. Note uncertainty if applicable

**Output format**:
```
PREFERRED CRITERIA: [Option Name]
=================================
| Criterion | Weight | Raw Score | Evidence | Weighted |
|-----------|--------|-----------|----------|----------|
| [name] | [w] | [0-3 or range] | [what supports] | [score*w] |
| ... | ... | ... | ... | ... |

Total weighted score: [sum]
Uncertainty notes: [what would change scores]
```

---

## Step 5: Evaluate OPTIONAL Criteria

For each viable option, note OPTIONAL criteria satisfaction.

**Scoring**: YES (0.5 bonus) / NO (0 bonus)

**LLM Scoring Guidance (OPTIONAL)**:
| Score | Meaning |
|-------|---------|
| YES | Option has this characteristic |
| NO | Option does not have this characteristic |

**Optional criteria are tie-breakers**, not primary ranking factors.

---

## Step 6: Compile Comparison Results

Assemble final outputs.

**Process**:
1. Complete evaluation matrix
2. Calculate final scores for viable options
3. Rank by final score (highest first)
4. Compile elimination reasons
5. Write comparison summary

**Final Score Calculation**:
```
final_score = sum(preferred_weighted_scores) + sum(optional_bonuses)
```

**Output format**:
```
COMPARISON RESULTS
==================

RANKINGS (Viable Options):
| Rank | Option | Score | Key Strengths | Key Weaknesses |
|------|--------|-------|---------------|----------------|
| 1 | [name] | [score] | [top 2 criteria] | [bottom 2] |
| 2 | ... | ... | ... | ... |

ELIMINATED OPTIONS:
| Option | Eliminated By | Reason |
|--------|---------------|--------|
| [name] | [criterion] | [specific reason] |

COMPARISON SUMMARY:
- Total options evaluated: [N]
- Viable after REQUIRED: [N]
- Viable after EXCLUSION: [N]
- Top option margin: [score difference from #2]
- Key differentiators: [what separates top options]

UNCERTAINTY SUMMARY:
- High-confidence scores: [count]
- Uncertain scores (ranges): [count]
- What would resolve uncertainty: [list]
```

---

## Step 7: Empirical Validation (HIGH Stakes Only)

**Include when**: HIGH stakes + HARD/IMPOSSIBLE reversibility

**Purpose**: Test assumptions before committing.

### 7.1: Extract Testable Predictions

For top options, identify what we're assuming:
```
Option A predictions:
- If we choose A, we predict [X] will happen because [reasoning]
- A assumes [Y] is true - can we verify?
- Success of A depends on [Z] being correct
```

### 7.2: Identify Minimum Viable Tests

| Test | What it tests | Effort | Information value |
|------|---------------|--------|-------------------|
| [test] | [assumption] | LOW/MED/HIGH | HIGH/MED/LOW |

**Prioritize**: HIGH information value + LOW effort tests first

**Test types**:
- Small-scale pilot
- Historical analog check
- Expert review
- Prototype/mockup
- User feedback

### 7.3: Design Validation Checkpoints

After decision, what would indicate:
- **Working**: [observable signs of success]
- **Failing**: [observable signs of failure]
- **Reconsider trigger**: [what would make us switch]

### 7.4: Log Predictions for Calibration

```
PREDICTION LOG
==============
Date: [date]
Decision: [what was chosen]
Predictions:
1. [prediction] - confidence: [%] - check date: [when]
2. ...

Review scheduled: [date]
```

→ INVOKE: /empirical_validation [top options and key assumptions] (if available)

---

## Scoring Reference Card (Quick Reference)

**For LLM consistency, use these anchors**:

### REQUIRED/EXCLUSION
```
PASS = evidence clearly supports
FAIL = evidence clearly contradicts
UNCERTAIN = no clear evidence
```

### PREFERRED (0-3 Scale)
```
0 = "I found nothing supporting this"
1 = "I found weak/indirect support"
2 = "I found good support with minor gaps"
3 = "I found strong support from multiple sources"
```

### When Uncertain
```
Use range (e.g., "1-2") + explain what would resolve
Never guess - state uncertainty explicitly
```

### Evidence Documentation
```
Always cite: "Score [N] because [specific evidence from input]"
If no evidence: "Score 0 - no evidence found in input"
```

---

## When to Use

- After matching/generation has established criteria
- Multiple options need narrowing down
- Systematic elimination required
- Transparent, defensible decisions needed
- Options need ranking before selection
- Stakeholders need to understand filtering

---

## Verification Criteria

| Step | Verification |
|------|--------------|
| Step 1 | Framework complete (all options, criteria typed, weights set) |
| Step 2 | All REQUIRED criteria evaluated with evidence |
| Step 3 | All EXCLUSION criteria evaluated |
| Step 4 | All PREFERRED criteria scored with evidence |
| Step 5 | OPTIONAL criteria noted |
| Step 6 | Rankings complete with summary |
| Step 7 | If HIGH stakes: validation plan exists |

**Overall verification**:
- [ ] Every option evaluated against every criterion
- [ ] Scores have documented evidence (not just numbers)
- [ ] Eliminated options have specific reasons
- [ ] Viable options ranked with score breakdown
- [ ] Uncertainties explicitly noted
- [ ] If HIGH stakes: predictions logged

---

## Domain-Specific Examples

### Example 1: Software Architecture Comparison

```
EVALUATION FRAMEWORK
====================
Options: [Monolith, Microservices, Modular Monolith]

Criteria:
REQUIRED:
- Handles expected load (weight: 1.0)
- Team can maintain (weight: 1.0)

PREFERRED:
- Deployment flexibility (weight: 0.8)
- Development velocity (weight: 0.9)
- Operational simplicity (weight: 0.6)

REQUIRED CRITERIA EVALUATION
============================
Option: Microservices
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Handles load | PASS | Can scale individual services independently |
| Team can maintain | UNCERTAIN | Team has 3 devs, microservices often need 5+ |
Result: NEEDS CLARIFICATION (team size concern)

PREFERRED CRITERIA: Microservices
=================================
| Criterion | Weight | Raw Score | Evidence | Weighted |
|-----------|--------|-----------|----------|----------|
| Deploy flexibility | 0.8 | 3 | Each service deploys independently | 2.4 |
| Dev velocity | 0.9 | 1-2 | Initial overhead high, velocity improves later | 0.9-1.8 |
| Ops simplicity | 0.6 | 0 | Significantly more complex operations | 0 |

Total: 3.3-4.2 (range due to velocity uncertainty)
```

### Example 2: Career Decision Comparison

```
EVALUATION FRAMEWORK
====================
Options: [Stay current job, Accept new offer, Start consulting]

Criteria:
REQUIRED:
- Pays bills (weight: 1.0)
- Doesn't violate non-compete (weight: 1.0)

EXCLUSION:
- Requires relocation (user stated constraint)

PREFERRED:
- Learning opportunity (weight: 0.9)
- Work-life balance (weight: 0.8)
- Compensation (weight: 0.7)
- Career growth (weight: 0.85)

PREFERRED CRITERIA: Start consulting
=====================================
| Criterion | Weight | Raw Score | Evidence | Weighted |
|-----------|--------|-----------|----------|----------|
| Learning | 0.9 | 3 | Varied clients, new problems | 2.7 |
| Balance | 0.8 | 1-2 | Flexible but unpredictable | 0.8-1.6 |
| Compensation | 0.7 | 1-3 | Variable income | 0.7-2.1 |
| Growth | 0.85 | 2 | Builds skills, uncertain ladder | 1.7 |

Total: 5.9-8.1 (high variance - reflects consulting uncertainty)

UNCERTAINTY SUMMARY
===================
High-confidence: Learning (clear benefit)
Uncertain: Balance, Compensation (inherent consulting variability)
```

### Example 3: Product Selection Comparison

```
EVALUATION FRAMEWORK
====================
Options: [AWS, GCP, Azure] for cloud hosting

Criteria:
REQUIRED:
- Has required services (compute, storage, DB) - weight: 1.0
- Complies with data residency requirements - weight: 1.0

EXCLUSION:
- Vendor lock-in > 2 years to reverse

PREFERRED:
- Cost for our usage pattern (weight: 0.9)
- Team familiarity (weight: 0.7)
- Documentation quality (weight: 0.5)
- Integration with existing tools (weight: 0.8)

SCORING APPROACH
================
For cloud comparison, use:
- Cost: 3 = cheapest for our pattern, 0 = >50% more expensive
- Familiarity: 3 = team has production experience, 0 = no experience
- Documentation: 3 = comprehensive with examples, 0 = sparse/outdated
- Integration: 3 = native integration, 0 = manual/third-party needed
```

---

## Integration Points

- **Often invoked from**: /procedure_engine, /decision_trees, /multi_criteria_decision
- **Routes to**: /selection (final choice), /empirical_validation (high stakes), /criteria_weighting (if weights unclear)
- **Related**: /criteria_weighting, /evaluation_dimensions, /pairwise_comparison
