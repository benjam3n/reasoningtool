---
name: spe
description: "Extends the search paradigm to non-obvious domains. Identifies which search methods should become procedures."
---

# Search Paradigm Extensions and Procedure Candidates

**Input**: $ARGUMENTS

---

## Overview

Many activities not traditionally framed as "search" can be productively reinterpreted through the search lens. This procedure:
1. Extends the search paradigm to non-obvious domains
2. Identifies which search methods should become procedures
3. Prioritizes by "intelligence reduction" — which structures do all the work

## Steps

### Step 1: Reframe as Search
Take the input domain/activity and ask:
1. What is being "found"? (the target)
2. What is the space being searched? (the possibilities)
3. What guides the search? (the heuristic)
4. What stops the search? (the termination criterion)
5. What makes one result better than another? (the objective function)

**Non-obvious search domains:**
- Writing = searching language space for sequences that achieve goals
- Therapy = searching belief/behavior space for healthier configurations
- Dating = searching person space for compatible partners
- Career = searching role space for fulfilling positions
- Design = searching artifact space for solutions that satisfy constraints
- Diagnosis = searching cause space for explanations that fit symptoms
- Negotiation = searching agreement space for mutually acceptable terms
- Teaching = searching explanation space for ones the student understands
- Leadership = searching action space for moves that align the group
- Law = searching precedent space for cases that support your argument

### Step 2: Evaluate Search Reframing Quality
For the input's reframing, assess:

| Criterion | Score (1-5) | Notes |
|-----------|------------|-------|
| Does the search frame reveal hidden structure? | | |
| Does it suggest new methods? | | |
| Does it clarify what "progress" means? | | |
| Does it identify what makes the problem hard? | | |
| Does it connect to methods from other domains? | | |

If total score ≥ 15: The search reframing is highly productive
If total score 10-14: Useful but partial — some aspects don't map cleanly
If total score < 10: The search frame doesn't add much here

### Step 3: Identify Intelligence-Reducing Structures
The most valuable procedures are those that reduce the intelligence needed to succeed:

1. **What makes this search hard without structure?**
   - Space too large → Need pruning / heuristics
   - No gradient → Need random exploration + selection
   - Deceptive landscape → Need diversity / restarts
   - Dynamic target → Need adaptive methods
   - Multi-objective → Need Pareto methods

2. **What structure would make it easier?**
   - Decomposition (break into sub-searches)
   - Ordering (search promising regions first)
   - Caching (remember what you've tried)
   - Abstraction (search at higher level first)
   - Constraint propagation (eliminate before searching)

3. **How much intelligence does the structure replace?**
   - High: Turns expert task into mechanical task
   - Medium: Guides novice to competent performance
   - Low: Reminds expert of steps they'd do anyway

### Step 4: Procedure Candidacy Assessment
For each identified structure, evaluate whether it should become a formal procedure:

| Factor | Weight | Score |
|--------|--------|-------|
| Frequency of use (how often needed) | 3x | 1-5 |
| Intelligence reduction (how much easier) | 3x | 1-5 |
| Transferability (works across domains) | 2x | 1-5 |
| Teachability (can be written as steps) | 2x | 1-5 |
| Current gap (no existing procedure covers it) | 1x | 1-5 |

Weighted score ≥ 40: Strong procedure candidate
Weighted score 25-39: Worth developing if resources available
Weighted score < 25: Not worth formalizing

### Step 5: Design Procedure Skeleton
For top candidates:
1. Name and abbreviation
2. One-line description
3. Input: what it takes
4. Output: what it produces
5. Steps: high-level (3-7 steps)
6. Key insight: what makes this procedure valuable vs ad hoc

### Step 6: Report
```
SEARCH PARADIGM EXTENSION:
Domain: [input domain]
Search reframing: Searching [space] for [target] using [heuristic]
Reframing quality: [score/25]

Intelligence-reducing structures found:
1. [structure] — reduces [difficulty] by [mechanism]

Procedure candidates:
| Name | Score | Key Insight |
|------|-------|-------------|
| [name] | [score/55] | [one line] |

Top recommendation: [which to develop first and why]
```

## When to Use
- Exploring whether a domain can benefit from search-based thinking
- Looking for new procedures to develop
- Trying to understand what makes a problem hard
- → INVOKE: /smc (search methods catalog) for the full method inventory

## Verification
- [ ] Domain reframed as search (all 5 components identified)
- [ ] Reframing quality assessed honestly
- [ ] Intelligence-reducing structures identified
- [ ] Procedure candidates scored
- [ ] Top candidates have skeleton designs
