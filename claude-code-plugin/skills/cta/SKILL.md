---
name: cta
description: Analyze a category of guesses to determine which apply to the user. System does the work by testing each guess against available evidence and generating sub-guesses for verification.
---

# Category Analysis

**Input**: $ARGUMENTS (category name and list of guesses in that category)

---

## Purpose

After `/guess_generation` produces guesses organized by category, this procedure analyzes each category to determine which guesses apply to the specific user.

**Principle**: The system does the work. Don't ask the user to verify - instead, generate verifiable implications and check them.

---

## Step 1: Identify Category Type

| Category Type | Analysis Approach |
|---------------|-------------------|
| **Factual** (current state) | Generate observable implications, check for evidence |
| **Causal** (X causes Y) | Check if mechanism is plausible, look for counterexamples |
| **Predictive** (future state) | Identify leading indicators, check track record |
| **Normative** (should/shouldn't) | Surface underlying values, check for contradictions |
| **Modal** (possible/impossible) | Test constraints, identify blockers |
| **Intentional** (wants/intends) | Check consistency with stated goals and behavior |
| **Constraint** (limits) | Verify constraint exists, check if absolute or flexible |
| **Method** (how to) | Check prerequisites, resources, fit with preferences |
| **Reason** (why) | Trace to deeper reasons, check if terminal or instrumental |

**Category type**: [TYPE]

---

## Step 2: For Each Guess, Generate Verification Tests

For each guess in the category:

```
GUESS: [the guess]
TYPE: [category type]
VERIFICATION APPROACH:
├── Observable implication 1: [if true, we'd expect to see X]
├── Observable implication 2: [if true, we'd expect to see Y]
├── Counter-evidence check: [if false, we'd expect to see Z]
└── Consistency check: [does this contradict other known facts?]

EVIDENCE AVAILABLE:
├── From user input: [what can be inferred]
├── From context: [what can be derived]
├── From defaults: [what is typical]
└── Unknown: [what we can't determine]

VERDICT: LIKELY / UNLIKELY / UNKNOWN / NEEDS_USER_INPUT
CONFIDENCE: HIGH / MEDIUM / LOW
DERIVATION: [D: from what evidence]
```

---

## Step 3: Cluster Related Guesses

Group guesses that imply each other:

```
CLUSTER: [name]
├── If [guess A] → then likely [guess B, C]
├── If [guess D] → then unlikely [guess E, F]
└── Independent: [guesses that don't cluster]
```

This reduces the number of things to verify - verifying one can verify/eliminate many.

---

## Step 4: Identify Discriminating Questions

Find questions where:
- The answer would verify/eliminate multiple guesses
- The answer is easily observable or statable
- The system can provide options rather than open-ended

```
DISCRIMINATING QUESTION: [question]
├── If answer is A: verifies [guesses], eliminates [guesses]
├── If answer is B: verifies [guesses], eliminates [guesses]
└── If answer is C: verifies [guesses], eliminates [guesses]

OPTIONS TO PRESENT:
├── Option A: [concrete choice]
├── Option B: [concrete choice]
├── Option C: [concrete choice]
└── Other: [user can specify]
```

---

## Step 5: Apply Category-Specific Analysis

### For CONSTRAINT Categories

| Constraint | Exists? | Absolute? | Workaround? |
|------------|---------|-----------|-------------|
| [constraint 1] | YES/NO/UNKNOWN | YES/NO | [if yes, what] |
| [constraint 2] | YES/NO/UNKNOWN | YES/NO | [if yes, what] |

### For METHOD Categories

| Method | Prerequisites Met? | Resources Available? | Fits Preferences? |
|--------|-------------------|---------------------|-------------------|
| [method 1] | YES/NO/PARTIAL | YES/NO/PARTIAL | YES/NO/UNKNOWN |
| [method 2] | YES/NO/PARTIAL | YES/NO/PARTIAL | YES/NO/UNKNOWN |

**Better option check**: For each method the user hasn't mentioned, check if it fits their preferences better than what they're considering.

### For REASON Categories

| Reason | Terminal? | Serves What? | Consistent? |
|--------|-----------|--------------|-------------|
| [reason 1] | YES/NO | [higher goal] | YES/NO |
| [reason 2] | YES/NO | [higher goal] | YES/NO |

Trace each reason until hitting a terminal value or circularity.

### For CAUSAL Categories

| Causal Claim | Mechanism? | Evidence? | Counterexamples? |
|--------------|------------|-----------|------------------|
| [claim 1] | [how it works] | [supporting] | [contradicting] |
| [claim 2] | [how it works] | [supporting] | [contradicting] |

### For FACTUAL Categories

| Factual Claim | Observable? | Observed? | Source? |
|---------------|-------------|-----------|---------|
| [claim 1] | YES/NO | YES/NO/NA | [O: source] |
| [claim 2] | YES/NO | YES/NO/NA | [O: source] |

### For ERROR Categories (Pre-Mortem)

| Error Type | Plausible Here? | Evidence For? | Evidence Against? |
|------------|-----------------|---------------|-------------------|
| [error 1] | YES/NO | [what suggests this error] | [what suggests not] |
| [error 2] | YES/NO | [what suggests this error] | [what suggests not] |

---

## Step 6: Generate Summary

```
## CATEGORY: [name]

### Verified Guesses (High Confidence)
[list with derivation markers]

### Likely Guesses (Medium Confidence)
[list with derivation markers]

### Unknown Guesses (Need Input)
[list with specific options to present]

### Eliminated Guesses (Low Probability)
[list with reasons for elimination]

### Clusters Identified
[list of guess clusters and their implications]

### Better Options Surfaced
[methods/approaches user may not have considered that fit their preferences]
```

---

## Step 7: Preference Integration

If user preferences are known (from `/preference_elicitation`):

| Guess | Matches Preference? | Which Preference? | Strength |
|-------|---------------------|-------------------|----------|
| [guess 1] | YES/NO/PARTIAL | [preference name] | STRONG/WEAK |
| [guess 2] | YES/NO/PARTIAL | [preference name] | STRONG/WEAK |

**Rank guesses by preference match.**

---

## Output Format

```
## CATEGORY ANALYSIS: [category name]

### Input
[list of guesses in this category]

### Analysis Type
[category type and analysis approach used]

### Results

VERIFIED (High Confidence):
1. [guess] [D: derivation]
2. [guess] [D: derivation]

LIKELY (Medium Confidence):
1. [guess] [D: derivation]

UNKNOWN (Need Input - Options Provided):
1. [guess]
   - If A: [implication]
   - If B: [implication]
   - If C: [implication]

ELIMINATED:
1. [guess] - [reason]

### Clusters
[cluster summaries]

### Better Options Identified
[options user may not have considered]

### Recommended Next
[which guess to verify first and how]
```

---

## Execution Checklist

- [ ] Category type identified
- [ ] Each guess has verification tests
- [ ] Clusters identified
- [ ] Discriminating questions generated with options
- [ ] Category-specific analysis applied
- [ ] Summary generated
- [ ] Better options surfaced

---

## Next Procedure

For each UNKNOWN guess with options:
→ INVOKE: /preference_elicitation to match options to user values

For better options identified:
→ INVOKE: /better_option_check to compare against user's current choice

---

**Execute now**: Analyze the category of guesses provided.
