---
name: procedure_discovery
description: "Find or create the procedures needed to execute a plan"
---

# Procedure Discovery

## Overview
Find or create the procedures needed to execute a plan

## Steps

### Step 1: Catalog required operations
Analyze each operation from the plan to understand what's needed:

For each operation:
1. What is the operation's purpose?
2. What are the inputs and expected outputs?
3. What level of reliability is required?
4. How frequently will this be performed?
5. Are there variations or edge cases?

Categorize operations:
- Core: Essential for plan success
- Supporting: Helps but not critical
- Contingency: Only needed if something goes wrong

### Step 2: Search for direct matches
Search procedure library for exact matches:

1. For each operation, search by:
   - Operation name/type
   - Input/output signature
   - Domain tags
   - Use case descriptions

2. Evaluate match quality:
   - Perfect match: Procedure does exactly what's needed
   - Close match: Minor adaptation required
   - Partial match: Covers part of the operation

3. Document matches:
   - Which procedure
   - Match quality
   - Any gaps or adaptations needed

### Step 3: Explore procedure compositions
For unmatched operations, explore if combinations of procedures work:

1. Can the operation be decomposed into smaller steps?
2. Do procedures exist for each smaller step?
3. Can procedures be chained or composed?

Composition patterns:
- Sequential: A then B then C
- Parallel: A and B simultaneously
- Conditional: If X then A else B
- Loop: Repeat A until condition

Evaluate compositions:
- Does composition achieve the operation's goal?
- Are there interface mismatches between procedures?
- Is the composition efficient (not overly complex)?

### Step 4: Cross-domain transfer analysis
For remaining gaps, search for transferable procedures:

1. What would this operation look like in other domains?
   - Software engineering
   - Project management
   - Manufacturing
   - Science
   - Military
   - Nature/biology

2. Are there procedures in those domains?
   - Search library by analogy
   - Search external sources

3. How would we adapt them?
   - What's domain-specific vs universal?
   - What translation is needed?
   - What assumptions change?

### Step 5: Specify new procedures needed
For operations that need new procedures, create specifications:

For each new procedure:
1. Name and description
2. Inputs and outputs (detailed)
3. Success criteria
4. Key steps (high-level)
5. Verification approach
6. Estimated complexity (simple/moderate/complex)
7. Dependencies on other procedures
8. Reuse potential (one-time vs widely useful)

### Step 6: Prioritize procedure creation
Rank new procedures by creation priority:

Priority factors:
1. Criticality: Is it blocking a core operation?
2. Reuse: Will it be used beyond this plan?
3. Complexity: How hard is it to create?
4. Dependencies: Does it block other procedures?
5. Risk: What's the cost of not having it?

Scoring:
- High priority: Critical, blocks execution, relatively simple
- Medium priority: Important but has workarounds
- Low priority: Nice to have, complex, limited reuse

Create prioritized backlog with effort estimates

### Step 7: Compile coverage report
Create comprehensive coverage analysis:

1. Coverage summary:
   - Total operations
   - Directly matched
   - Covered by composition
   - Covered by adaptation
   - Require new procedures

2. Coverage metrics:
   - Overall coverage percentage
   - Critical operation coverage
   - Supporting operation coverage

3. Gap analysis:
   - Which domains have gaps?
   - Are gaps clustered (same type of operation)?
   - What's the pattern?

4. Recommendations:
   - Proceed with plan (if coverage sufficient)
   - Create procedures first (if critical gaps)
   - Reconsider strategy (if coverage too low)


## When to Use
- Plan requires procedures not currently in the library
- Verifying procedure availability before execution begins
- Creating new procedures to fill identified gaps
- Assessing feasibility of a strategy based on procedure coverage
- Periodic library audit to identify coverage gaps
- After strategy selection to ensure execution is possible
- When an execution step fails due to missing procedure
- Onboarding a new domain and building initial procedure set

## Verification
- All required operations have been analyzed for coverage
- Matches are accurate (procedure actually does what's claimed)
- Compositions are valid (interfaces align, no logical gaps)
- New procedure specifications are complete and actionable
- Priority ordering considers all relevant factors
- Coverage summary accurately reflects the analysis

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.