---
name: verify
description: Verify claims using the GOSM verification standard. Every claim must be OBSERVED, TESTED, or DERIVED - never guessed.
disable-model-invocation: false
---

# GOSM Verification Procedure

Verify: **$ARGUMENTS**

## Verification Standard

Every claim must be one of:

### 1. OBSERVED [O: source]
- Source identified and accessible
- Observation method documented
- No interpretation added
- Verbatim if quoting

### 2. TESTED [T: N=count, result]
- Test conditions documented
- Test result documented
- Test is reproducible
- Test matches claim

### 3. DERIVED [D: premises → conclusion]
- All premises are themselves verified
- Inference is valid (modus ponens, etc.)
- No hidden premises
- Derivation chain documented

## Verification Steps

1. **Attempt OBSERVED**: Can this be directly witnessed or found in source?
   - Read the relevant file
   - Find the specific line/section
   - Quote exactly what you see

2. **Attempt TESTED**: Can this be executed to confirm?
   - Write a test that would verify this
   - Run the test
   - Report the result

3. **Attempt DERIVED**: Can this be logically proven from verified premises?
   - List the premises
   - Verify each premise is [O], [T], or [D]
   - Show the derivation

4. **If none apply**: Mark as UNVERIFIED and EXCLUDE from output

## Output Format

For each claim:
```
CLAIM: [the claim]
STATUS: VERIFIED_OBSERVED | VERIFIED_TESTED | VERIFIED_DERIVED | UNVERIFIED
EVIDENCE: [the evidence]
MARKER: [O: source] | [T: N=X, result] | [D: premise1 + premise2 → conclusion]
```

## NOT Acceptable
- "Confidence: LOW" (exclude instead)
- "Needs validation" (validate first)
- "Probably true" (verify or exclude)
- "Expert can fill in" (demonstrate first)
