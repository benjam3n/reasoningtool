---
name: "m - Matching"
description: "Define criteria for filtering options"
---

# Matching

## Overview
Define criteria for filtering options

## Steps

### Step 1: Extract goal requirements
Analyze the goal to identify implicit requirements:
- What must be true for the goal to be achieved?
- What would make a solution unacceptable?
- What constraints exist (time, money, resources)?

### Step 2: Identify stakeholder needs
For each stakeholder (or stakeholder type):
- What do they need from the solution?
- What would they reject?
- What would delight them?

### Step 3: Categorize criteria by type
Sort all requirements into criteria categories:

MUST-HAVE (Required):
- Non-negotiable requirements
- Constraint-driven criteria
- Safety/legal requirements

MUST-NOT-HAVE (Exclusions):
- Automatic disqualifiers
- Known failure patterns
- Incompatible characteristics

SHOULD-HAVE (Preferred):
- Strongly desired features
- Significant value-add
- Differentiating factors

NICE-TO-HAVE (Optional):
- Bonus features
- Future-proofing
- Convenience factors

### Step 4: Define evaluation method for each criterion
For each criterion, specify HOW to evaluate it:
- Binary (yes/no): Clear pass/fail
- Scalar (1-10): Degree of satisfaction
- Threshold (>X): Minimum acceptable value
- Comparative (better than Y): Relative assessment

Also specify:
- What evidence is needed?
- Who can make this judgment?
- How long does evaluation take?

### Step 5: Check for conflicts and gaps
Review criteria set for issues:

Conflicts:
- Do any criteria contradict each other?
- Are there impossible combinations?
- Will trade-offs be needed?

Gaps:
- Are there obvious criteria missing?
- Does the set cover all stakeholder needs?
- Are there blind spots?

Feasibility:
- Can all criteria actually be evaluated?
- Do we have access to needed information?

### Step 6: Finalize criteria set
Produce final criteria list:
1. Resolve or document conflicts
2. Add any missing criteria from gap analysis
3. Assign weights if needed (for Optimization step)
4. Calculate completeness estimate
5. Count required criteria


## When to Use
- After Generation, before Comparison
- When you need to establish what "good enough" means
- When stakeholders need to agree on requirements
- When filtering will be done by someone else (criteria as contract)
- When options vary widely and need systematic filtering
- When past decisions lacked clear criteria (learning from mistakes)

## Verification
- All must-have criteria are truly non-negotiable
- Criteria are evaluable (not vague or subjective)
- No redundant criteria (each adds information)
- Criteria derive from goal (not arbitrary)
- Conflicts are documented, not hidden

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.