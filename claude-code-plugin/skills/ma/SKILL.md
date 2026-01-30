---
name: "ma - Morphological Analysis (Morphological Box)"
description: "Invented by Fritz Zwicky. Break a problem into independent dimensions,"
---

# Morphological Analysis (Morphological Box)

## Overview
Invented by Fritz Zwicky. Break a problem into independent dimensions,
list possible values for each dimension, then systematically generate
all combinations. The structure guarantees exhaustive coverage.

## Goal
Generate all possible solutions by identifying independent dimensions
and systematically combining values across dimensions. Combination
generation is purely mechanical.

## Steps

### Step 1: Define the Problem
Clearly state what you're trying to create or solve.
This frames what dimensions are relevant.

**Output**: Problem statement

### Step 2: Identify Independent Dimensions
List the independent aspects/parameters of the solution.

Rules for good dimensions:
- Independent (changing one doesn't force change in another)
- Relevant (affects the solution quality)
- Variable (has multiple possible values)

Common dimension types:
- Physical: size, material, shape, color
- Functional: method, mechanism, process
- Contextual: user, location, time, frequency
- Economic: price point, cost structure

**Output**: List of 4-8 dimensions

### Step 3: List Values for Each Dimension
For each dimension, list all possible values.
Be exhaustive within reason (3-7 values per dimension typical).

Include:
- Obvious values
- Extreme values
- Novel values
- "None" or "opposite" if applicable

**Output**: Values for each dimension

### Step 4: Construct Morphological Box
Create matrix with dimensions as rows and values as columns.
This visualizes the solution space.

**Output**: Morphological box matrix

### Step 5: Calculate Combination Count
Total combinations = V1 × V2 × V3 × ... × Vn
where Vi is the number of values for dimension i.

If too large (>1000), either:
- Reduce values per dimension
- Use sampling instead of exhaustive
- Add constraints to eliminate combinations

**Output**: Combination count

### Step 6: Generate Combinations
Systematically generate all combinations.
Each combination picks one value from each dimension.

For small spaces: List all
For large spaces: Sample systematically or use constraints

**Output**: List of combinations

### Step 7: Apply Constraint Filter
Remove combinations that are:
- Physically impossible
- Logically contradictory
- Clearly inferior (dominated by another)
- Outside scope/budget

**Output**: Reduced combination list

### Step 8: Evaluate Viable Combinations
Score remaining combinations on:
- Feasibility (can we build it?)
- Value (does it solve the problem well?)
- Novelty (is it differentiated?)
- Cost (can we afford it?)

**Output**: Ranked combinations

### Step 9: Select Top Combinations
Select top 3-5 combinations for further development.
Consider diversity (don't pick all similar).

**Output**: Shortlist


## When to Use
- Designing new products/solutions
- Exploring solution space exhaustively
- Ensuring no combinations are missed
- Breaking creative blocks
- Systematic innovation

## Verification
- Dimensions are truly independent
- Values are mutually exclusive within each dimension
- Values are exhaustive (cover the space)
- Combination count is correct
- Constraints are justified
- Evaluation criteria are clear

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.