---
name: "boc - Better Option Check"
description: Prevent user from settling on suboptimal option by systematically checking if better options exist that match their preferences. System surfaces what user may not have considered.
---

# Better Option Check

**Input**: $ARGUMENTS (user's current choice and preference profile)

---

## Purpose

Users often choose the first viable option, not the best option. This procedure systematically checks if better options exist.

**Principle**: Before committing, verify no better option is being missed. Surface what the user doesn't know exists.

---

## Step 1: Identify Current Choice

```
USER'S CURRENT CHOICE: [what they're considering]

Evidence of commitment:
├── Stated directly: [quote if available]
├── Implied by behavior: [what suggests this choice]
├── Assumed by default: [if no explicit choice, what's implied]
└── Commitment level: EXPLORING / LEANING / DECIDED

Why this choice:
├── [reason 1]
├── [reason 2]
└── [unknown - not stated]
```

---

## Step 2: Extract Preferences from Choice

What does choosing this option reveal about preferences?

| Inferred Preference | How Inferred | Strength |
|--------------------|--------------|----------|
| [preference 1] | [current choice has this property] | STRONG/WEAK |
| [preference 2] | [current choice has this property] | STRONG/WEAK |
| [preference 3] | [what's sacrificed suggests anti-preference] | STRONG/WEAK |

---

## Step 3: Generate Full Option Space

List ALL options in the category, not just obvious ones:

```
OPTION SPACE FOR: [category]

Commonly Known Options:
├── [option 1] - [brief description]
├── [option 2] - [brief description]
└── [option 3] - [brief description]

Less Known Options:
├── [option 4] - [why overlooked]
├── [option 5] - [why overlooked]
└── [option 6] - [why overlooked]

Hybrid Options:
├── [combination 1] - [elements combined]
├── [combination 2] - [elements combined]
└── [combination 3] - [elements combined]

Non-Obvious Options:
├── [option 7] - [why not obvious]
├── [option 8] - [why not obvious]
└── [option 9] - [why not obvious]

Options User Likely Doesn't Know About:
├── [option 10] - [why likely unknown]
├── [option 11] - [why likely unknown]
└── [option 12] - [why likely unknown]

TOTAL: [count] options generated
```

**Minimum**: Generate 20+ options before comparison.

---

## Step 4: Score All Options Against Preferences

| Option | Pref 1 | Pref 2 | Pref 3 | Pref 4 | Pref 5 | Total | Rank |
|--------|--------|--------|--------|--------|--------|-------|------|
| Current choice | ✓/✗/~ | ✓/✗/~ | ✓/✗/~ | ✓/✗/~ | ✓/✗/~ | [N]/5 | [R] |
| [option 2] | ✓/✗/~ | ✓/✗/~ | ✓/✗/~ | ✓/✗/~ | ✓/✗/~ | [N]/5 | [R] |
| [option 3] | ✓/✗/~ | ✓/✗/~ | ✓/✗/~ | ✓/✗/~ | ✓/✗/~ | [N]/5 | [R] |

Key:
- ✓ = matches preference
- ✗ = conflicts with preference
- ~ = neutral/unknown

---

## Step 5: Identify Better Options

```
OPTIONS THAT RANK HIGHER THAN CURRENT CHOICE:

1. [option name]
   Score: [X]/5 vs current [Y]/5
   Better because: [specific advantages]
   Why user might not have considered: [reason]

2. [option name]
   Score: [X]/5 vs current [Y]/5
   Better because: [specific advantages]
   Why user might not have considered: [reason]

3. [option name]
   Score: [X]/5 vs current [Y]/5
   Better because: [specific advantages]
   Why user might not have considered: [reason]
```

---

## Step 6: Analyze Why User Chose Suboptimally

If better options exist, why is user choosing current option?

| Reason for Suboptimal Choice | Evidence | Addressable? |
|------------------------------|----------|--------------|
| **Didn't know better option exists** | [not mentioned] | YES - inform |
| **Assumed constraint that doesn't exist** | [stated belief] | YES - verify |
| **Used wrong criteria** | [stated reasons] | YES - reframe |
| **Satisficing (first viable)** | [stopped searching] | YES - show better |
| **Emotional attachment** | [signs of attachment] | MAYBE - understand why |
| **Sunk cost** | [prior investment] | MAYBE - reframe |
| **Social pressure** | [others' expectations] | MAYBE - surface values |
| **Status quo bias** | [defaulting to familiar] | YES - show concrete benefit |
| **Actually optimal (we're wrong)** | [hidden info] | NO - update our understanding |

---

## Step 7: Generate "Before You Commit" Summary

```
## BEFORE COMMITTING TO: [current choice]

### Options That Match Your Preferences Better

1. **[Better Option 1]**
   - Matches: [preferences it satisfies]
   - Why you might not have considered it: [reason]
   - Compared to your current choice: [specific comparison]
   - Worth exploring if: [condition]

2. **[Better Option 2]**
   - Matches: [preferences it satisfies]
   - Why you might not have considered it: [reason]
   - Compared to your current choice: [specific comparison]
   - Worth exploring if: [condition]

### What Your Current Choice Sacrifices

- [preference X] - your choice doesn't provide this
- [preference Y] - your choice works against this

### Recommendation

[PROCEED / EXPLORE_ALTERNATIVES / STOP_AND_RECONSIDER]

Reason: [why this recommendation]
```

---

## Step 8: Present Without Overwhelming

If many better options exist, prioritize:

| Priority | Option | Why Prioritized |
|----------|--------|-----------------|
| 1 | [option] | Highest preference match + most overlooked |
| 2 | [option] | Second highest match |
| 3 | [option] | Interesting alternative frame |

**Maximum 3 alternatives to present** - more causes decision paralysis.

---

## Output Format

```
## BETTER OPTION CHECK

### Current Choice
[what user is considering]
Commitment level: [EXPLORING/LEANING/DECIDED]
Preference match score: [X]/[total]

### Full Option Space
[count] options identified
[list grouped by category]

### Options That Rank Higher
1. [option]: Score [X]/[total]
2. [option]: Score [X]/[total]
3. [option]: Score [X]/[total]

### Why User May Be Settling
[analysis of suboptimal choice reasons]

### Before You Commit
[3 prioritized alternatives to consider]

### Recommendation
[PROCEED / EXPLORE / RECONSIDER]
[reason]
```

---

## Execution Checklist

- [ ] Current choice identified with commitment level
- [ ] Preferences extracted from choice
- [ ] 20+ options generated in full space
- [ ] All options scored against preferences
- [ ] Better options identified
- [ ] Reasons for suboptimal choice analyzed
- [ ] Top 3 alternatives prioritized
- [ ] Recommendation generated

---

## Next Procedure

If EXPLORE_ALTERNATIVES:
→ INVOKE: /cta on the better options

If RECONSIDER:
→ INVOKE: /ve to clarify what user actually wants

---

**Execute now**: Check if better options exist for the user's current choice.
