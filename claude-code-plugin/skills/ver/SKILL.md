---
name: "ver - GOSM Verification Procedure"
description: Verify claims using the GOSM verification standard. Every claim must be OBSERVED, TESTED, or DERIVED - never guessed.
---

# GOSM Verification Procedure

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Verify specific claims**: The user has one or more explicit claims they want verified to the GOSM standard (Observed, Tested, or Derived).
**Interpretation 2 — Verify output from a prior skill**: The user has output from /araw, /claim, or another skill and wants the claims in it verified against source evidence.
**Interpretation 3 — Verify before publishing**: The user has content they plan to share and wants every factual claim verified before it goes out.

If ambiguous, ask: "Do you want me to verify specific claims, check the claims in previous output, or audit content before publishing?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Three categories, no exceptions.** Every claim is OBSERVED (seen in source), TESTED (confirmed by execution), or DERIVED (logically follows from verified premises). There is no fourth category. "Probably true" and "widely believed" are not verification statuses.

2. **Unverified claims are excluded, not downgraded.** The temptation is to say "Confidence: LOW" and include the claim anyway. This is not verification — it's hedged guessing. If a claim can't be verified, it is excluded from output. Period.

3. **Derivation chains must be complete.** A DERIVED claim is only as strong as its weakest premise. Every premise in a derivation must itself be verified (O, T, or D). A derivation from unverified premises is not a derivation — it's speculation with extra steps.

4. **Observation means source, not memory.** "I know this is true" is not observation. OBSERVED requires identifying the specific source and pointing to the specific content. If you can't point to it, you haven't observed it.

5. **Testing means execution, not thought experiment.** "This would probably work" is not testing. TESTED requires actually running something and recording the result. The test must be reproducible.

6. **Verification is binary per claim.** Each claim is either verified or it isn't. There's no "partially verified." If a claim is too broad to verify fully, decompose it into narrower claims that can be.

---

## Verification Standard

### 1. OBSERVED [O: source]

Requirements for OBSERVED status:
- Source is identified and accessible
- Observation method is documented (how did you find this?)
- No interpretation is added to what was observed
- If quoting, the quote is verbatim
- Source is authoritative for this type of claim

```
CLAIM: [the claim]
STATUS: VERIFIED_OBSERVED
EVIDENCE: [what was seen, where]
MARKER: [O: specific source with location]
```

### 2. TESTED [T: N=count, result]

Requirements for TESTED status:
- Test conditions are documented
- Test was actually executed (not hypothetical)
- Result is documented exactly
- Test is reproducible by someone else
- Test actually measures what the claim asserts

```
CLAIM: [the claim]
STATUS: VERIFIED_TESTED
EVIDENCE: [test setup, execution, result]
MARKER: [T: N=X, result=Y]
```

### 3. DERIVED [D: premises -> conclusion]

Requirements for DERIVED status:
- ALL premises are themselves verified (O, T, or D)
- Inference is valid (modus ponens, modus tollens, etc.)
- No hidden premises (every step is explicit)
- Derivation chain is documented completely

```
CLAIM: [the claim]
STATUS: VERIFIED_DERIVED
EVIDENCE: [the derivation]
MARKER: [D: premise1 [O] + premise2 [T] -> conclusion]
```

---

## Verification Procedure

### Step 1: Extract Claims

From the input, extract every factual claim. Number them: V1, V2, V3...

For each claim, note:
- The claim text
- Where it appears in the input
- Its importance (load-bearing / supporting / incidental)

### Step 2: Attempt Verification (in order)

For each claim, try methods in this order:

**1. Attempt OBSERVED:**
- Can this be found in a source?
- Read the relevant file, document, or reference
- Find the specific line/section
- Quote exactly what you see
- If found: mark [O: source]

**2. Attempt TESTED:**
- Can this be executed or measured?
- Design a test that would verify this
- Run the test
- Record the result exactly
- If confirmed: mark [T: N=count, result]

**3. Attempt DERIVED:**
- Can this be logically proven from verified premises?
- List every premise
- Verify each premise is [O], [T], or [D]
- Show the complete derivation chain
- If derivation is valid: mark [D: premises -> conclusion]

**4. If NONE apply:**
- Mark as UNVERIFIED
- EXCLUDE from verified output
- Note why verification failed

### Step 3: Compile Verification Report

```
GOSM VERIFICATION REPORT

VERIFIED CLAIMS:
V[N]: [claim]
  STATUS: VERIFIED_OBSERVED / VERIFIED_TESTED / VERIFIED_DERIVED
  EVIDENCE: [evidence]
  MARKER: [marker]

UNVERIFIED (EXCLUDED):
V[N]: [claim]
  REASON: [why verification failed]
  NOTE: [what would be needed to verify]

SUMMARY:
Total claims: [N]
Verified: [N] (Observed: [N], Tested: [N], Derived: [N])
Unverified (excluded): [N]
Verification rate: [%]

LOAD-BEARING UNVERIFIED:
[Any unverified claims that are load-bearing — these are critical gaps]
```

---

## NOT Acceptable

These are NOT verification and must never appear:
- "Confidence: LOW" (exclude instead of hedging)
- "Needs validation" (validate it now or exclude)
- "Probably true" (verify or exclude)
- "Expert can fill in" (demonstrate with evidence first)
- "Widely accepted" (accepted by whom? cite the source or exclude)
- "Common knowledge" (not a verification status — cite or exclude)
- "In my understanding" (understanding is not observation — cite or exclude)

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Hedged inclusion** | "Low confidence" claims kept in output | Unverified = excluded. No exceptions |
| **Memory-as-observation** | "I know this" treated as [O] | Observation requires pointing to a specific, accessible source |
| **Thought-experiment-as-test** | "This would work" treated as [T] | Testing requires actual execution and recorded results |
| **Incomplete derivation** | Derivation skips premises or uses unverified ones | Every premise must be verified; every step explicit |
| **Broad claims** | "X is generally true" — too broad to verify | Decompose into specific, verifiable sub-claims |
| **Authority-as-evidence** | "Experts say X" without citing specific experts or claims | Name the expert, cite the source, or exclude |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Quick — verify load-bearing claims only | Load-bearing claims verified or excluded |
| **2x** | Standard — all explicit claims verified | Full claim list, each verified or excluded |
| **4x** | Thorough — all claims including implicit ones, full derivation chains | Complete verification with explicit derivation chains |
| **8x** | Exhaustive — all claims, cross-verified where possible, alternative sources checked | Multiple verification paths per claim, highest confidence output |

---

## Pre-Completion Checklist

- [ ] All claims extracted and numbered
- [ ] Each claim attempted in order: Observed, Tested, Derived
- [ ] Every [O] has a specific, accessible source
- [ ] Every [T] has documented test conditions and results
- [ ] Every [D] has complete derivation chain with verified premises
- [ ] Unverified claims are EXCLUDED, not hedged
- [ ] Load-bearing unverified claims are flagged as critical gaps
- [ ] No "probably", "likely", "in my understanding", or "widely accepted" in output

---

## Integration

- **Use from**: /araw (verify claims from ARAW output), /claim (verify the claim being tested), /create (verify factual claims in content before publishing), /fb (filtered feedback uses GOSM markers)
- **Routes to**: /araw (when verification reveals claims that need stress-testing), /diagnose (when verification failures suggest the wrong thing is being measured)
- **Differs from**: /av (assumption verification — tests beliefs, /ver tests factual claims), /val (deliverable validation against requirements, /ver is claim-by-claim verification), /vp (testing procedures for systems, /ver is for individual claims)
- **Complementary**: /aex (surface hidden claims that need verification), /fb (filtered feedback requires GOSM grounding), /av (verify assumptions after verifying claims)
