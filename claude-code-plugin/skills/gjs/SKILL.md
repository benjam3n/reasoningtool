---
name: gjs
description: "A goal journey is NOT a narrative arc. It's a CHAIN OF GOALS. Integration hub for GOSM goal processing."
context: fork
---

# Goal Journey System

**Input**: $ARGUMENTS

---

## Overview

A goal journey is NOT a narrative arc. It's a **CHAIN OF GOALS**.

Every action serves a goal.
Every goal serves another goal.
The chain terminates at intrinsic goals (valued for themselves).

The journey IS the goal chain. Understanding the journey means
understanding what goals are being served all the way up to
intrinsic values.

**This skill is the integration hub** for GOSM goal processing. It orchestrates:
- Context-adaptive variant selection
- Clarification vs substitution checking
- Empirical validation integration
- Goal chain tracing

---

## Step 0: Context Detection and Variant Selection

Before deep analysis, assess context to select appropriate depth:

### Context Factors

| Factor | Options | Check |
|--------|---------|-------|
| **Time Pressure** | URGENT / NEAR / NORMAL | When must action happen? |
| **Stakes** | HIGH / MED / LOW | Cost of getting wrong? |
| **Domain Expertise** | EXPERT / INTERMEDIATE / NOVICE | User's familiarity? |
| **Action Cost** | CHEAP / EXPENSIVE | Reversibility? |
| **Information State** | RICH / MODERATE / SPARSE | What do we know? |

### Variant Selection

| Context | Variant | What It Does |
|---------|---------|--------------|
| URGENT (time critical) | GOSM-Lite | 5 steps: Critical assumptions only |
| LOW stakes + CHEAP action | GOSM-Quick | 2 steps: Sanity check + act |
| EXPERT + HIGH confidence | GOSM-Check | 3 steps: Expert validation |
| CHEAP action + SPARSE info | GOSM-After | 4 steps: Act-then-learn |
| MED stakes + NORMAL time | GOSM-Standard | 8 steps: Balanced analysis |
| HIGH stakes + EXPENSIVE + NOVEL | GOSM-Full | Full procedure_engine |

**Decision**:
```
Context: [URGENT/NEAR/NORMAL] time, [HIGH/MED/LOW] stakes,
         [EXPERT/INTERMEDIATE/NOVICE] user, [CHEAP/EXPENSIVE] action
→ Selected variant: [VARIANT]
→ Reasoning: [why this variant fits]
```

---

## Step 1: Parse Goal and Check for Substitution

Before analyzing, ensure we understand the ACTUAL goal:

### 1.1 Capture Original Goal Exactly

```
ORIGINAL GOAL (verbatim): "[user's exact words]"
```

### 1.2 Clarification vs Substitution Gate

→ GATE: clarification_vs_substitution [original_goal] [any_proposed_refinement]

If any interpretation or refinement is considered:
- **CLARIFICATION**: Proceed (same goal, clearer)
- **SUBSTITUTION**: Stop and get user consent
- **UNCLEAR**: Ask for clarification

**Substitution Red Flags** (check each):
- [ ] "Underlying need" replacing stated goal?
- [ ] "Achievable version" reducing ambition?
- [ ] "What you probably mean" imposing interpretation?
- [ ] "More realistic" substituting easier goal?

If any red flag triggered → Explicit consent required before proceeding.

---

## Step 2: Parse Claims and Classify

### 2.1 Extract Claims

List each claim embedded in the goal:
1. [claim 1]
2. [claim 2]
...

### 2.2 Classify OPEN vs CLOSED

| Claim | Type | Reasoning |
|-------|------|-----------|
| [claim] | OPEN/CLOSED | [has alternatives / foundational] |

- **CLOSED**: No alternatives exist. Accept as foundation.
- **OPEN**: Alternatives exist. Must explore.

---

## Step 3: ARAW Key Claims

For each OPEN claim, branch:

```
Claim: "[claim]"
├── ASSUME RIGHT → What follows if true?
│   └── [implications, next steps]
└── ASSUME WRONG → What alternatives exist?
    └── [other possibilities, reframes]
```

→ INVOKE: /assumeright_assumewrong_search [OPEN claims]

---

## Step 4: Fill Goal Journey Structure

Make guesses to fill the structure:

```
GOAL JOURNEY STRUCTURE
======================
CURRENT STATE:    [Where they are now]
DESIRED STATE:    [Where they want to be]
IMMEDIATE GOAL:   [What they're trying to do]
SERVES:           [What that goal serves] - GUESS? NEEDS VERIFICATION?
INTRINSIC GOAL:   [What they ultimately value] - NEEDS ELICITATION?
WHY NOW:          [What triggered this] - UNKNOWN?
SUCCESS CRITERIA: [How they'll know it worked] - UNKNOWN?
CONSTRAINTS:      [What limits exist] - UNKNOWN?
```

Mark uncertain items with `[GUESS]` or `[UNKNOWN]`.

---

## Step 5: Trace the Goal Chain

Build the complete chain from action to intrinsic value:

```
ACTION: [specific action being considered]
    ↓ serves
GOAL: [what that achieves]
    ↓ serves
GOAL: [what that enables]
    ↓ serves
GOAL: [deeper goal]
    ↓ serves
INTRINSIC: [terminal value - valued for itself]
```

### Chain Validation

- [ ] Each step clearly serves the next
- [ ] No gaps in reasoning
- [ ] Intrinsic goal is actually intrinsic (not instrumental)
- [ ] Chain doesn't assume substituted goals

If gaps exist → INVOKE: /value_elicitation to discover missing links

---

## Step 6: Dual Analysis

### Contrarian Analysis (from ASSUME WRONG branches)
- Is the stated goal actually necessary?
- What alternatives exist to the assumed approach?
- Is this the real goal or a proxy?

### Non-Contrarian Analysis (from ASSUME RIGHT branches)
- What options exist for achieving the goal?
- What are the next steps?
- What resources are available?

**Both analyses always done. Filter by user context.**

---

## Step 7: Identify Testable Predictions

Extract claims that can be empirically validated:

| Prediction | Testable? | How to Test | Priority |
|------------|-----------|-------------|----------|
| [claim from analysis] | YES/NO | [method] | HIGH/MED/LOW |

High-priority: Claims that, if wrong, change the entire approach.

→ INVOKE: /empirical_validation [testable predictions]

---

## Step 8: Generate Questions

Questions about uncertain items (prioritized):

| Question | About | Priority | Why It Matters |
|----------|-------|----------|----------------|
| [question] | [which uncertainty] | HIGH/MED/LOW | [changes what if answered] |

**HIGH priority**: Questions that determine goal chain validity
**MED priority**: Questions that affect approach
**LOW priority**: Questions about execution details

---

## Step 9: Route to Next Procedure

Based on analysis results:

| Condition | Route To |
|-----------|----------|
| Intrinsic goal unknown | → /value_elicitation |
| Goal needs refinement | → /goal_refinement |
| Multiple options identified | → /comparison |
| Ready to plan steps | → /steps_generation |
| Failure pattern detected | → /failure_journeys |
| Problem statement | → /problem_identification |

---

## Output Format

```
## Context Assessment
- Time: [URGENT/NEAR/NORMAL]
- Stakes: [HIGH/MED/LOW]
- Expertise: [EXPERT/INTERMEDIATE/NOVICE]
- Action cost: [CHEAP/EXPENSIVE]
→ Variant: [selected variant]

## Clarification/Substitution Check
- Original goal: [verbatim]
- Classification: CLARIFICATION / No refinement proposed
- Red flags: [none / list]

## Parsed Claims
| Claim | Type | Reasoning |
|-------|------|-----------|
[claims table]

## Goal Journey Structure
[filled structure with uncertainties marked]

## Goal Chain
[traced chain from action to intrinsic]

## Dual Analysis
CONTRARIAN: [key alternatives/reframes]
NON-CONTRARIAN: [key options/next steps]

## Testable Predictions
[predictions for empirical validation]

## Questions (Prioritized)
[questions about uncertainties]

## Next Procedure
→ INVOKE: /[next_procedure] [args]
```

---

## Niche Documentation

### Where This Skill Works Best
- Complex goals requiring goal chain analysis
- Goals where intrinsic values are unclear
- Goals that might contain hidden substitutions
- Goals needing context-adaptive depth

### Where This Skill Struggles
- Simple, immediate actions (use GOSM-Quick)
- Pure execution (no goal analysis needed)
- Time-critical situations (use GOSM-Lite)
- Expert users who know their goals (use GOSM-Check)

### Integration Points
- Receives from: /goal_understanding, /procedure_engine
- Routes to: /value_elicitation, /goal_refinement, /steps_generation, /comparison
- Gates: clarification_vs_substitution_gate, empirical_validation
- Related: /failure_journeys, /goal_reframing