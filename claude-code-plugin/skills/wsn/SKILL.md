---
name: "wsn - What Skill Next"
description: "Determine the highest-value next skill to add to the reasoning toolkit by analyzing gaps, ROI, and user needs."
output:
  format: "prose"
---

# What Skill Next

**Input**: $ARGUMENTS

---

## Step 1: CURRENT STATE SNAPSHOT

Take a quick inventory of the existing toolkit:

```
CURRENT STATE:
Total skills: [count from skills/ directory]
Recent additions: [last 5-10 skills added]
Coverage summary: [which categories/dimensions are well-covered]
```

---

## Step 2: IDENTIFY CANDIDATES

Generate candidate skills from multiple sources:

### A. Gap Analysis (What's Missing?)

Check each dimension for underrepresentation:

| Dimension | Well-Covered | Sparse | Empty |
|-----------|-------------|--------|-------|
| **Sophistication** (simple → expert) | | | |
| **Speed** (instant → exhaustive) | | | |
| **User State** (exploring, stuck, recovering, executing) | | | |
| **Domain** (general → niche) | | | |
| **Thinking Mode** (divergent, convergent, lateral, systems) | | | |

List 3-5 candidates from gaps found.

### B. User Need Analysis (What's Requested?)

1. What problems do users bring most often?
2. What do users try to do that no skill handles well?
3. What user states are underserved?
4. What do users ask for that requires chaining 3+ skills (should be one)?

List 3-5 candidates from user needs.

### C. Intersection Analysis (What's at Valuable Crossroads?)

Check high-value intersections:

| Intersection | Exists? | Candidate |
|-------------|---------|-----------|
| Simple + Recovery | | |
| Fast + Decision | | |
| Easy + Validation | | |
| General + Creation | | |
| Quick + Diagnosis | | |

List 2-3 candidates from intersections.

### D. Input-Specific Candidates

If the user provided context (domain, problem type, recent work), generate 2-3 candidates specific to their situation.

---

## Step 3: SCORE EACH CANDIDATE

For each candidate, score on these dimensions:

```
CANDIDATE: /[abbreviation] — [full name]
PURPOSE: [one sentence]

BENEFIT (1-10):
  User frequency: [how often would this be used?] ___/10
  Gap severity: [how much is it missed?] ___/10
  Unique value: [does anything else do this?] ___/10
  BENEFIT SCORE: [average] ___/10

EFFORT (1-10):
  Build complexity: [how hard to write?] ___/10
  Dependency count: [other skills needed?] ___/10
  Testing difficulty: [hard to validate?] ___/10
  EFFORT SCORE: [average] ___/10

ROI = BENEFIT / EFFORT = ___
```

---

## Step 4: RANK AND RECOMMEND

Sort candidates by ROI (highest first):

```
WHAT SKILL NEXT — RANKED RECOMMENDATIONS
==========================================

#1 RECOMMENDED: /[skill] — [name]
   ROI: [score]
   Purpose: [what it does]
   User arrives: [what state they're in]
   User leaves: [what state after]
   Core mechanism: [the key technique — 2-3 sentences]
   Fills gap: [which gap from Step 2]

#2: /[skill] — [name]
   ROI: [score]
   Purpose: [what it does]
   Fills gap: [which gap]

#3: /[skill] — [name]
   ROI: [score]
   Purpose: [what it does]
   Fills gap: [which gap]

SKIP FOR NOW:
- /[skill] — reason: [too complex, low frequency, etc.]
```

---

## Step 5: BUILD SPEC (for #1 recommendation)

Provide enough detail to create the skill immediately:

```
BUILD SPEC FOR: /[recommended skill]
======================================
Name: "[abbrev] - [Full Name]"
Description: "[one sentence for frontmatter]"

Steps:
1. [first step — what input does the user provide?]
2. [core analysis/process step]
3. [key technique or framework]
4. [output generation]
5. [validation/quality check]

Integration:
- Invoked by: [which skills would route here]
- Invokes: [which skills this would call]
- Complements: [related skills]

Ready to build: [YES / NEEDS MORE SPEC]
```

---

## Quick Mode

If the user just wants a fast answer:

1. Scan the skill library for the most obvious gap
2. Name one skill
3. Give the one-sentence purpose
4. Say why it's highest ROI

Format: `/[skill]` — [purpose] — ROI: [high/medium] because [reason]

---

## Integration

Use with:
- `/skgap` -> Full gap analysis (more thorough, less action-oriented)
- `/roa` -> Detailed ROI calculation on a specific candidate
- `/spd` -> Discover the space of possible skills before choosing
- `/cs` or `/mts` -> Create the recommended skill once chosen
- `/imprt` -> Improve existing skills instead of creating new ones
- `/impss` -> Improve a specific existing skill
