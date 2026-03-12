---
name: "cand - Candidate Evaluation"
description: Systematically evaluates candidates for any role, position, or slot. Scores on requirements, checks for disqualifiers, and ranks by fit.
output:
  format: "prose"
---

# Candidate Evaluation

**Input**: $ARGUMENTS

---

## Step 1: Define Role Requirements

Specify what the role/position/slot needs. Be explicit about must-haves versus nice-to-haves.

```
ROLE: [What is being filled]
CONTEXT: [Why this role matters, what environment it operates in]

MUST-HAVE REQUIREMENTS:
1. [Requirement 1] — weight: [1-5]
2. [Requirement 2] — weight: [1-5]
3. [Requirement 3] — weight: [1-5]

NICE-TO-HAVE REQUIREMENTS:
1. [Requirement 1] — weight: [1-3]
2. [Requirement 2] — weight: [1-3]

DISQUALIFIERS (automatic rejection):
- [Disqualifier 1]
- [Disqualifier 2]
```

---

## Step 2: List Candidates

Enumerate all candidates under consideration.

```
CANDIDATES:
1. [Candidate 1] — brief description
2. [Candidate 2] — brief description
3. [Candidate 3] — brief description
...

CANDIDATE SOURCE: [Where did these candidates come from?]
COMPLETENESS CHECK: [Are there obvious candidates missing from this list?]
```

---

## Step 3: Score Each Candidate

Rate each candidate against each requirement.

```
SCORECARD:

[Candidate 1]:
  Must-haves:
  - [Req 1] (wt 5): [1-5 score] — evidence: [why this score]
  - [Req 2] (wt 3): [1-5 score] — evidence: [why this score]
  Nice-to-haves:
  - [Req 1] (wt 2): [1-5 score] — evidence: [why this score]
  DISQUALIFIER CHECK: [PASS/FAIL] — [details if fail]
  WEIGHTED TOTAL: [sum of score * weight]

[Candidate 2]:
  [Same structure]

[Repeat for all candidates]
```

---

## Step 4: Rank by Fit

Sort candidates and identify the top pick.

```
RANKING:
1. [Candidate] — score: [total] — strengths: [top 2]
2. [Candidate] — score: [total] — strengths: [top 2]
3. [Candidate] — score: [total] — strengths: [top 2]
...

DISQUALIFIED:
- [Candidate] — reason: [disqualifier triggered]
```

---

## Step 5: Recommend

State the top candidate with rationale and a backup option.

```
TOP CANDIDATE: [Name]
RATIONALE: [Why this candidate wins — not just highest score, but the story]
KEY RISK: [The biggest concern with this choice]

BACKUP CANDIDATE: [Name]
BACKUP RATIONALE: [When you'd choose the backup instead]

DECISION CONFIDENCE: [HIGH/MEDIUM/LOW]
WHAT WOULD CHANGE THE ANSWER: [New information that could flip the ranking]
```

---

## Integration

Use with:
- `/cmp` -> Detailed head-to-head comparison of top two candidates
- `/skev` -> Evaluate a candidate's specific skill or method
- `/ratn` -> Build a persuasive rationale for the recommendation
