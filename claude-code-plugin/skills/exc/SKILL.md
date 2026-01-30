---
name: exc
description: "Systematically check if a solution or similar solution already exists before investing effort in creation"
---

# Existence Check

## Overview
Systematically check if a solution or similar solution already exists before investing effort in creation

## Steps

### Step 1: Clarify search target
Define precisely what we're looking for:
1. State the core need in one sentence
2. List must-have characteristics (non-negotiable)
3. List nice-to-have characteristics (desirable)
4. Identify what would make something "close enough"
5. Define the threshold for acceptable adaptation effort

### Step 2: Search for exact matches
Search for solutions that match exactly:
1. Search within current project/organization (local scope)
2. Search public repositories and package managers
3. Search commercial solutions and SaaS offerings
4. Search academic papers and research implementations
5. Document each match with: name, source, fit assessment

### Step 3: Search for similar matches
If no exact matches, search for near matches (90%+ overlap):
1. Relax one must-have at a time and re-search
2. Search for solutions to slightly different problems
3. Look for solutions with different interfaces but same function
4. Check for solutions in different languages/frameworks
5. For each match, document: what's missing, adaptation effort

### Step 4: Search for partial and analogous matches
Broaden search further:
1. Search for partial solutions (50-90% overlap)
   - What addresses part of the problem?
   - What could be extended to cover our needs?
2. Search for analogous solutions from other domains
   - How do other fields solve similar problems?
   - What patterns exist that could be applied?
3. Search for component building blocks
   - What pieces exist that could be assembled?
   - What libraries/tools handle sub-problems?

### Step 5: Evaluate findings
Assess all findings against our needs:
1. Rank all matches by fit score (exact > similar > partial > analogous)
2. For each viable option, estimate:
   - Time to use/adapt vs time to build from scratch
   - Risk of using existing vs building new
   - Maintenance burden of each approach
3. Consider combinations (multiple partial solutions)
4. Identify what's truly missing that requires new creation

### Step 6: Generate recommendation
Based on evaluation, recommend approach:
- use_existing: Exact or near-exact match found, use as-is
- adapt_existing: Good match found, adaptation effort acceptable
- combine_multiple: No single solution, but combination works
- build_new: Nothing suitable exists, must create
- hybrid_approach: Use existing for some parts, build others

Provide clear rationale for recommendation.


## When to Use
- Before creating something new (feature, document, process, tool)
- At the start of research phase in any project
- When looking for reusable solutions to avoid reinventing the wheel
- Before writing code that might already exist in libraries
- When exploring market or competitive landscape
- Before designing a system that might have established patterns
- When considering building vs buying/using existing
- At strategy discovery to find proven approaches
- When time or resources are limited and reuse is valuable
- Before patent/IP work to understand prior art

## Verification
- Multiple search sources were checked (not just one)
- Search scope was appropriate (not too narrow, not wastefully broad)
- Each match type was attempted before concluding "not found"
- Findings include source URLs or references for verification
- Adaptation effort estimates are realistic (not overly optimistic)
- Recommendation rationale addresses build vs use tradeoffs
- Cross-domain search was attempted for analogous solutions

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.