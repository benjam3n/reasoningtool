---
name: bes
description: Like playing 20 Questions - each yes/no question eliminates half the possibilities. For N options, at most log2(N) questions needed.
---

# Binary Elimination Search

## Overview
Like playing "20 Questions" - each yes/no question eliminates half
the possibilities. For a space of N options, at most log2(N) questions
needed. No intelligence required to FOLLOW - just ask the next question.

## Goal
Find the correct answer/option by asking binary questions that
cut the search space in half each time. Structure does all the work -
just follow the decision tree.

## Steps

### Step 1: Define Search Space
List ALL possible answers/options.
Be exhaustive - if the answer isn't in the list, you won't find it.

**Output**: Numbered list of all options

### Step 2: Identify Discriminating Attribute
Find an attribute/question that divides the remaining options
roughly in half.

Good question: Splits options ~50/50
Bad question: Splits options 90/10 (wastes a question)

**Output**: A yes/no question

### Step 3: Ask Question
Ask the binary question.
Answer must be clearly YES or NO.

**Output**: YES or NO

### Step 4: Eliminate Options
Based on the answer, eliminate all options that don't match.

If YES: Keep only options where the attribute is true
If NO: Keep only options where the attribute is false

**Output**: Reduced list of remaining options

### Step 5: Check Termination
If exactly 1 option remains → DONE, that's the answer
If 0 options remain → ERROR, answer wasn't in search space
If >1 options remain → Go to Step 2

**Output**: Continue or Done

### Step 6: Record Answer
Document the final answer and the path taken.

**Output**: Final answer with justification


## When to Use
- Diagnosing a problem from many possible causes
- Selecting from many options when criteria are clear
- Finding root cause
- Debugging
- Classification

## Verification
- Search space was exhaustive (answer was included)
- Each question was truly binary (yes/no)
- Questions divided space roughly in half
- Elimination was consistent with answers
- Single answer remained at end

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.