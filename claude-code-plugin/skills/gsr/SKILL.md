---
name: gsr
description: "Given any conclusion, statement, or claim, reconstruct the goal-structure. Includes detection of goal drift and substitution in chains."
context: fork
---

# Goal-Structure Reconstruction

**Input**: $ARGUMENTS

---

## Overview

Given any conclusion, statement, or claim, reconstruct the goal-structure
(the "story") that led to it. This reveals WHY the conclusion exists,
enabling evaluation of purpose rather than just logic.

---

## Context-Adaptive Variants

### Reconstruction-Lite (URGENT)
- Steps 1, 2, 5 only
- Quick chain, quick evaluation
- Focus on "does this conclusion serve a legitimate goal?"

### Reconstruction-Standard
- All steps
- Full chain reconstruction

### Reconstruction-Full (HIGH stakes)
- All steps + substitution detection at each link
- Multiple possible chains compared
- Empirical validation of key causal claims

---

## Steps

### Step 1: Identify the conclusion
State the conclusion, claim, or statement to be reconstructed.

Be precise. The exact wording matters.

**Output**: conclusion_statement

### Step 2: Ask "What goal does this serve?"
What is the IMMEDIATE goal of this statement?
Not assumptions, not implications - the GOAL.

What state is the speaker trying to bring about?
What need is this serving?

**Output**: immediate_goal

### Step 3: Ask "What goal led to pursuing that goal?"
Why pursue the immediate goal?
What deeper need does achieving that goal serve?

Continue asking until you reach either:
- An intrinsic goal (valued for itself)
- A practical necessity (required for functioning)
- A transcendental condition (required for any goal-pursuit)

**Output**: goal_chain

### Step 4: Map the story
Organize the goal chain as a "story" with chapters:

Chapter 1: The foundational/intrinsic goal
Chapter 2: What problem or need arises from that goal
Chapter 3: What approach addresses that problem
...
Final Chapter: The conclusion

Each chapter should connect to the next.

**Output**: story_structure

### Step 5: Evaluate the story
Ask of the story:

1. Does it cohere? (Do the chapters connect logically?)
2. Are the goals legitimate? (Would reasonable people share them?)
3. Does the conclusion serve the goals? (Does the ending fit?)
4. Is this the best way? (Are there better paths to the same goal?)
5. Was the journey necessary? (Did the goal need pursuing at all?)

**NEW - Goal Drift Detection**:
6. Did goal substitution occur? Check each link in the chain:
   - Does each goal genuinely serve the next?
   - Or did the chain drift to a different outcome?
   - Would achieving each step lead to the stated parent goal?

If drift detected, note where and what was substituted.

**Output**: evaluation


## When to Use
- Evaluating philosophical claims or foundations
- Understanding why someone made a statement
- Finding the purpose behind a criticism
- Determining if a conclusion is meaningful or arbitrary
- Terminating n+1 regress by reaching intrinsic goals

## Output Format
```
## Goal-Structure Reconstruction: [Conclusion]

**Conclusion**: [The statement being analyzed]

**Goal Chain**:
1. [Immediate goal]
2. [Next level goal]
...
N. [Foundational/intrinsic goal]

**Story**:
- Chapter 1: [Foundational goal]
- Chapter 2: [Problem/need]
...
- Final: [Conclusion]

**Evaluation**:
- Coherence: [Yes/No + explanation]
- Goals legitimate: [Yes/No + explanation]
- Conclusion serves goals: [Yes/No + explanation]
- Best way: [Assessment]
- Journey necessary: [Assessment]
```

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.