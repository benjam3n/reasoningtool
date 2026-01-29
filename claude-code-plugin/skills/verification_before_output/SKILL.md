---
name: verification_before_output
description: "This procedure is the culmination of the no-guessing philosophy."
---

# Verification Before Output

## Overview
This procedure is the culmination of the no-guessing philosophy.

Previous GOSM versions documented uncertainty well:
- "Confidence: LOW, needs validation"
- "Flagged for review"
- "Tacit knowledge inferred"

But documented uncertainty still propagated into outputs.
The system FLAGGED AND PROCEEDED.

This procedure changes the paradigm:
- VERIFY BEFORE INCLUDING
- NO FLAGGING AND PROCEEDING
- EXCLUDE WHAT CANNOT BE VERIFIED

The cost is speed. The benefit is zero guessing.

## Goal
Ensure that NOTHING in any GOSM output is a guess.

Every claim is either:
- DERIVED (logically follows from verified premises)
- OBSERVED (directly witnessed or stated by source)
- TESTED (executed and confirmed)

If something cannot be verified, it is EXCLUDED, not flagged.

## Steps

### Step 1: Identify All Claims
Extract every claim in the output:
- Factual assertions
- Confidence statements
- Causal claims
- Procedural steps
- Recommendations

Each claim must be verified individually.

**Output**: List of claims to verify

### Step 2: Attempt Verification - OBSERVED
For each claim, can it be OBSERVED?

Ask:
- Is there a source that directly states this?
- Did we witness this directly?
- Is there documentary evidence?

If YES:
- Document source and method
- Mark as [O: <source>]

If NO:
- Move to next verification type

**Output**: Claims marked [O] or moved to next step

### Step 3: Attempt Verification - TESTED
For each unverified claim, can it be TESTED?

Ask:
- Can we execute something to verify this?
- Is there historical test data?
- Can we run a simulation?

If YES:
- Run the test (or document existing test)
- Document conditions and result
- Mark as [T: N=<count>, <result>]

If NO:
- Move to next verification type

**Output**: Claims marked [T] or moved to next step

### Step 4: Attempt Verification - DERIVED
For each unverified claim, can it be DERIVED?

Ask:
- What premises would imply this?
- Are those premises themselves verified?
- Is the inference valid?

If YES:
- Document premises and inference
- Verify each premise is [O], [T], or [D]
- Mark as [D: <premises> → <conclusion>]

If NO:
- Claim is UNVERIFIABLE

**Output**: Claims marked [D] or flagged UNVERIFIABLE

### Step 5: Exclude Unverifiable Claims
For each UNVERIFIABLE claim:

Options:
1. GO VERIFY IT - Find observation, test, or derivation
2. EXCLUDE IT - Remove from output entirely
3. MARK AS UNKNOWN - "We do not know X" (honest uncertainty)

NOT acceptable:
- Include with "low confidence"
- Include with "needs review"
- Include with "probably"

The output must contain ONLY verified claims or
honest acknowledgments of what is unknown.

**Output**: Clean output with verified claims only

### Step 6: Verify Verification
Final check:

For each [O] marker:
- Is source actually documented?
- Is observation method clear?

For each [T] marker:
- Is test actually documented?
- Is result clear?

For each [D] marker:
- Are premises actually verified?
- Is inference actually valid?

If any marker lacks documentation → BLOCK

**Output**: Verified output ready for emission


## When to Use
- For ALL outputs in high-stakes contexts
- When user has requested no guessing
- When building foundations for other work
- When output will be acted upon without further review

## Common Cases
### Tacit Knowledge Inference
**Old behavior**: Mark 'confidence: LOW', include in output
**New behavior**: 1. Can we verify the tacit knowledge exists?
   - Ask the source directly
   - Test if procedure works without it
2. If verified → Include with [O] or [T]
3. If not verified → Exclude


### Gap Filling
**Old behavior**: Reconstruct missing steps, mark "MEDIUM confidence"
**New behavior**: 1. Can we verify the gap-fill is correct?
   - Ask the source what the missing step is
   - Test if procedure works with gap-filled step
2. If verified → Include with [O] or [T]
3. If not verified → Mark as [UNKNOWN GAP]


### Confidence Without Test
**Old behavior**: Assign confidence 0-100% based on feeling
**New behavior**: Confidence ONLY from:
- Test pass rate: confidence = successes / attempts
- Adversarial survival: confidence = attacks survived
- Precedent: confidence = historical success rate

No test data → No confidence claim → Mark as [UNTESTED]


### Default Assumptions
**Old behavior**: Use defaults when actual value unknown
**New behavior**: 1. Can we derive actual value? → Derive it
2. Can we test which value is appropriate? → Test it
3. If neither → Mark as [UNKNOWN VALUE, using default X for Y reason]

Default is documented as DEFAULT, not as verified value


### Expert Fill In
**Old behavior**: Allow "expert can figure it out"
**New behavior**: 1. Have expert demonstrate gap-filling on test case
2. Document what expert did to fill gap
3. Only then mark as adequate

"Expert can probably figure it out" → [UNVERIFIED]
"Expert demonstrated filling gap by X" → [T: expert test]


## Verification
- Every claim in output has verification marker
- Every marker has documentation
- No "flagged for review" without resolution
- No "low confidence" without actual test data
- Unknown items explicitly marked as unknown
- Defaults explicitly marked as defaults

## Output Format
```
Every output using this procedure has:

1. VERIFIED CLAIMS section
   - Each claim with [O], [T], or [D] marker
   - Each marker with documentation

2. UNKNOWN section (if any)
   - Honest acknowledgment of what we don't know
   - No pretense of knowledge

3. DEFAULTS section (if any)
   - Defaults used with explicit justification
   - Marked clearly as defaults, not verified values

4. EXCLUDED section (optional, for transparency)
   - What was excluded due to unverifiability
   - Why it couldn't be verified
```

## Step 7: Specificity Check for Capability Claims

For any claim about what a system DOES or SHOULD DO:

Apply the specificity gate:
1. Does it specify TRIGGER? (what causes this to happen)
2. Does it specify PROCEDURE? (what exact steps occur)
3. Does it specify OUTPUT? (what concrete result is produced)
4. Does it specify VALIDATION? (how do we know it worked)

If any element is missing:
- BLOCK the claim
- Generate questions for missing elements
- Only include when all 4 are specified

→ INVOKE: /specificity_gate [capability claim]

**Output**: Capability claims with all 4 elements specified

## Gates Invoked
- no_guessing_gate
- test_based_confidence_gate
- execution_verified_adequacy_gate
- specificity_gate (for capability claims)

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.