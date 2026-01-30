---
name: "ipss - Interpretation Space Search"
description: "Ambiguity means multiple interpretations are possible."
---

# Interpretation Space Search

## Overview
Ambiguity means multiple interpretations are possible.
Instead of guessing, systematically:
1. Generate all plausible interpretations
2. Score each against criteria
3. Select the best-supported interpretation

## Goal
When input is ambiguous, generate all possible interpretations
and search for the best one using explicit criteria.

## Steps

### Step 1: Capture the Input
Record exactly what was said/observed.
Don't interpret yet - just capture.

**Output**: Raw input

### Step 2: Note the Context
Record all available context:
- Who/what is the source?
- What preceded this?
- What's the broader situation?
- What do we know about the source?

**Output**: Context summary

### Step 3: Generate Interpretations
Using generation methods, produce all plausible interpretations.
Be comprehensive - include interpretations you doubt.

For each interpretation, state:
- The interpretation in clear terms
- What assumptions it requires

**Output**: List of interpretations

### Step 4: Apply Obvious Filters
Remove interpretations that:
- Contradict known facts
- Are logically impossible
- Require absurd assumptions

Don't remove just because unlikely - keep for scoring.

**Output**: Filtered interpretations

### Step 5: Score Each Interpretation
For each interpretation, score on each criterion (1-10).
Be consistent across interpretations.

**Output**: Scored interpretations

### Step 6: Rank Interpretations
Sort by weighted total score.
Note the gap between #1 and #2.

**Output**: Ranked interpretations

### Step 7: Assess Confidence
Confidence based on:
- Score gap (large gap = high confidence)
- Absolute score (high score = good interpretation)
- Number of viable alternatives (fewer = higher confidence)

If confidence is low, consider:
- Seeking more information
- Testing interpretations
- Accepting ambiguity

**Output**: Confidence assessment

### Step 8: Select and Verify
Select best interpretation.
Verify it accounts for all key aspects of input.
Note what would change the interpretation.

**Output**: Selected interpretation with caveats


## When to Use
- Ambiguous communication
- Unclear requirements
- Multiple possible meanings
- Conflicting signals
- Need to understand intent

## Verification
- Multiple interpretations were generated (not just the obvious one)
- Interpretations cover literal, intent, and context variations
- Each interpretation is internally coherent
- Scoring was consistent across interpretations
- Confidence assessment accounts for score gaps
- Selected interpretation accounts for key input features

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.