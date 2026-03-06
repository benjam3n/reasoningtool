---
name: "given - Rank Skills by ROI for a Given Goal"
description: Given a goal, rank relevant skills from highest to lowest expected ROI, including negative-ROI skills with reasons.
---

# Given

**Input**: $ARGUMENTS

---

## Purpose

Given a goal statement, produce a ranked skill list by expected ROI.
Include positive, neutral, and negative ROI skills when relevant.

## ROI Model

For each skill estimate:
- UPSIDE: expected progress contribution
- COST: time and complexity cost
- RISK: probability of misdirection or wasted effort
- TIMING_FIT: usefulness now vs later

Compute qualitative ROI class:
- HIGH
- MEDIUM
- LOW
- NEGATIVE

## Steps

### 1. Parse Goal

Restate goal in one sentence.
Extract constraints and urgency.

### 2. Select Candidate Skills

From available skills, include only skills plausibly relevant to the goal.
Do not include obviously irrelevant skills.

### 3. Score and Rank

Score each candidate with the ROI model.
Sort highest to lowest.

### 4. Keep Negative ROI Entries

Include negative ROI entries when they are tempting but likely harmful now.
State why they are negative now.

### 5. Build Execution Slice

Mark a short RUN_NOW subset at the top.

---

## Output Format

```text
GOAL: ...

RUN_NOW:
1. /skill-id - ROI: HIGH - WHY: ...
2. /skill-id - ROI: HIGH - WHY: ...
3. /skill-id - ROI: MEDIUM - WHY: ...

FULL_RANKING:
1. /skill-id - ROI: HIGH - UPSIDE: ... - COST: ... - RISK: ... - TIMING_FIT: ...
2. /skill-id - ROI: MEDIUM - UPSIDE: ... - COST: ... - RISK: ... - TIMING_FIT: ...
...

NEGATIVE_ROI_STILL_RELEVANT:
- /skill-id - WHY_NEGATIVE_NOW: ... - WHEN_IT_BECOMES_POSITIVE: ...
```
