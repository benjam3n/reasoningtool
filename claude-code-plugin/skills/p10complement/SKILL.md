---
name: "p10complement - Pick 10 Complement"
description: "Find 10 skills that pair well with a specified skill, covering its gaps and extending its reach. Standalone implementation of the COMPLEMENT algorithm from /pick."
tier: "tier4"
categories: ["Meta & Navigation"]
tags: ["shortcut", "pick", "discovery", "complement", "pairing"]
output:
  format: "prose"
---

# Pick 10 Complement

**Input**: $ARGUMENTS

---

## Core Principles

1. **Complementarity is not similarity.** A complement covers what the target skill does NOT do. If the target skill analyzes, its complement plans. If it diverges, its complement converges. Picking similar skills is the opposite of complementing.

2. **Gaps define complements.** Every skill has blind spots — phases of thinking it skips, types of output it doesn't produce, failure modes it doesn't catch. The best complements are skills that directly address those blind spots.

3. **Function diversity over category diversity.** Two skills from the same category can complement each other if they serve different functions (one diagnoses, one treats). Two skills from different categories can fail to complement if they both analyze without acting.

4. **Workflow position matters.** A skill used BEFORE the target (preparing input) complements differently than one used AFTER (validating output). Both are valuable. The output should indicate position.

5. **Diminishing returns after 7.** The first 5 complements address real gaps. Complements 8-10 are increasingly marginal. Be honest about which are essential and which are nice-to-have.

---

## Phase 1: Target Skill Analysis

```
[A] TARGET: /[skill name from $ARGUMENTS]
[B] TARGET_FUNCTION: [what does this skill DO? — classify: analyze / decide / plan / create / validate / explore / diagnose]
[C] TARGET_CATEGORIES: [list from skills.json]
[D] TARGET_TAGS: [list from skills.json]
[E] TARGET_INVOKES: [skills it calls]
[F] TARGET_INVOKED_BY: [skills that call it]
```

Read the target skill's SKILL.md. Identify:

```
[G] TARGET_OUTPUTS: [what does it produce?]
[H] TARGET_BLIND_SPOTS:
    - Phases it skips: [list — e.g., "no validation step", "no implementation plan"]
    - Input types it doesn't handle: [list]
    - Failure modes it doesn't check: [list]
    - Perspectives it doesn't consider: [list]
[I] TARGET_PHASE: [where in a thinking workflow does this skill sit?]
    - Pre-analysis (framing, scoping)
    - Analysis (understanding, decomposing)
    - Synthesis (deciding, planning)
    - Execution (implementing, creating)
    - Validation (checking, testing)
```

---

## Phase 2: Complement Search

For each blind spot identified in Phase 1, search for skills that directly address it.

```
[J] COMPLEMENT_CANDIDATES:

Search strategy:
1. DIRECT_CONNECTIONS: Skills invoked by or invoking the target (already linked)
2. GAP_FILLERS: Skills whose primary function matches a target blind spot
3. PHASE_PARTNERS: Skills from adjacent workflow phases
4. CROSS_FUNCTION: Skills in the same category but different function

For each candidate, score:
    - GAP_COVERAGE: How directly does this address a target blind spot? (0-3)
    - PHASE_FIT: Is this from a different workflow phase? (+2 if yes)
    - FUNCTION_DIVERSITY: Does this do something the target doesn't? (+2 if yes)
    - REDUNDANCY_PENALTY: Does this overlap with another candidate? (-1 per overlap)
    - CONNECTION_BONUS: Is this already linked to the target? (+1)
```

---

## Phase 3: Selection and Ranking

```
[K] SCORING:

| Candidate | Gap Covered | Phase Fit | Function Diversity | Redundancy | Connection | Total |
|-----------|-------------|-----------|-------------------|------------|------------|-------|
| /[skill]  | [0-3]       | [0/2]     | [0/2]             | [0/-N]     | [0/1]      | [sum] |

Step 1: Rank by total score
Step 2: Take top 10
Step 3: Verify coverage:
    - Do the 10 complements cover at least 4 of the target's blind spots? [Y/N]
    - If N: swap lowest-scoring redundant pick for highest-scoring uncovered gap
Step 4: Classify each complement by workflow position:
    - BEFORE: Prepares input for the target skill
    - ALONGSIDE: Provides parallel/alternative analysis
    - AFTER: Validates, extends, or acts on the target's output
```

---

## Phase 4: Output

```
TARGET SKILL: /[name] — [title]
TARGET FUNCTION: [function]
IDENTIFIED BLIND SPOTS: [list]

PICKED 10 COMPLEMENTS:

BEFORE (use these first):
  1. /[id] — [title]
     Complements by: [specific gap it fills]
     Tier: [tier] | Category: [category]

ALONGSIDE (use in parallel):
  2. /[id] — [title]
     Complements by: [specific gap it fills]
     Tier: [tier] | Category: [category]

  [continue numbering...]

AFTER (use on target's output):
  N. /[id] — [title]
     Complements by: [specific gap it fills]
     Tier: [tier] | Category: [category]

COVERAGE: [X of Y blind spots addressed]
ESSENTIAL COMPLEMENTS: [top 5 — these fill real gaps]
NICE-TO-HAVE: [bottom 5 — diminishing returns]

SUGGESTED WORKFLOW:
  Step 1: /[before-skill] → produces [what]
  Step 2: /[target] → produces [what]
  Step 3: /[after-skill] → validates [what]

GAPS REMAINING: [what these 10 complements still don't cover]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Similarity masquerading as complement** | Picks share the same function as the target | Check: does this DO something the target doesn't? |
| **All picks from same phase** | Every complement is an "after" skill | Force distribution across before/alongside/after |
| **Ignoring direct connections** | Picks don't include skills the target already invokes | Check invokes/invoked_by first — these are proven partners |
| **Generic picks** | Complements that pair with everything, not specifically this target | Each pick must name the SPECIFIC blind spot it addresses |
| **Count fixation** | Padding to 10 with weak picks | Be honest: mark picks 8-10 as nice-to-have if they are |
| **Missing the obvious** | A natural partner is overlooked because it's too well-known | Scan invoked_by list — established connections matter |

---

## Depth Scaling

| Depth | Target Analysis | Candidate Search | Selection |
|-------|----------------|------------------|-----------|
| 1x | Function + blind spots from metadata only | Direct connections + same-category | Score and rank top 10 |
| 2x | Read target SKILL.md, extract detailed blind spots | Search across all categories for gap fillers | Score + verify coverage |
| 4x | Full target analysis + compare to exemplar workflows | Score all skills in library | Score + workflow design + gap analysis |
| 8x | Target + its invoked chain analyzed | Full library score + complement interaction effects | Optimal workflow with contingency paths |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Target skill read and its function identified
- [ ] At least 4 blind spots identified in the target
- [ ] Candidates scored on gap coverage, phase fit, and function diversity
- [ ] Exactly 10 skills returned
- [ ] Each pick names the specific blind spot it addresses
- [ ] Picks distributed across before/alongside/after positions
- [ ] Essential vs nice-to-have distinction made
- [ ] Suggested workflow provided

---

## Integration

- **Shortcut for**: `/pick 10 complement $ARGUMENTS`
- **Use when**: You have a skill you like and want to know what pairs with it
- **Routes to**: The 10 picked skills; `/to` for optimal execution ordering
- **Related**: `/p5similar` (finds similar, not complementary), `/p10diverse` (maximizes coverage broadly)
- **Differs from /p5similar**: similar finds overlap; complement finds gaps
- **Differs from /p10diverse**: diverse maximizes breadth; complement maximizes depth around one skill
