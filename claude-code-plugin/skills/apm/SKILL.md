---
name: "apm - Alphacode Pass 3 Meta"
description: "Third pass — meta-reasoning about solution correctness, confidence, and robustness. Catches what testing alone misses."
---

# Alphacode Pass 3 Meta

**Input**: $ARGUMENTS

---

## Overview

Pass 3 reasons about the solution from outside the solution. Catches bugs testing misses: incorrect problem interpretation, flawed greedy proofs, missed constraints, subtle off-by-one errors. Treats the solution as an artifact to audit.

**Prerequisite**: Complete Pass 1 (/ape) and ideally Pass 2 (/api).

## Steps

### Step 1: Re-read the Problem Statement
1. Read problem statement again, fresh
2. Compare your understanding to what's actually written
3. Did you solve the asked problem or a different one?
4. Common misreadings: "at most K" vs "exactly K", "distinct" vs "not necessarily distinct", 0-indexed vs 1-indexed, "non-decreasing" vs "strictly increasing"

### Step 2: Audit Algorithm Correctness
1. **Greedy**: State exchange argument explicitly. Can't state it? Greedy may be wrong.
2. **DP**: Verify recurrence — base cases, transitions cover all cases, no missing states
3. **Graph**: Verify assumptions — connected? directed? weighted? negative weights?
4. **Any**: Construct a case where it would fail IF wrong. Can't? Test harder.

### Step 3: Check Off-by-One Errors
1. Array indexing: 0-based vs 1-based consistency
2. Loop bounds: `< N` vs `<= N`
3. Binary search: `lo < hi` vs `lo <= hi`, `mid` vs `mid+1`
4. Interval endpoints: inclusive vs exclusive
5. Modular arithmetic: `(a - b) % MOD` can be negative

### Step 4: Stress Test with Adversarial Inputs
1. All elements equal / sorted / reverse sorted
2. Maximum values on all constraints simultaneously
3. Star graph, chain graph, complete graph
4. Single-character strings
5. Check: within time? Memory? Output format exact?

### Step 5: Consider Alternative Approaches
1. Completely different, simpler approach available?
2. Worth implementing as cross-check?
3. Two approaches agree → high confidence. Disagree → find which is wrong.

### Step 6: Confidence Assessment
```
META-REVIEW:
Problem interpretation: [verified / uncertain at X]
Algorithm correctness: [proven / argued / hoped]
Edge cases: [all covered / gaps at X]
Off-by-one audit: [clean / fixed N issues]
Stress test: [passed / failed at X]
Confidence: [high / medium / low]
Action: [submit / fix X first / rethink]
```

## When to Use
- Before submitting a competitive programming solution
- After Wrong Answer, to find the bug
- When solution passes examples but confidence is low

## Verification
- [ ] Problem re-read after solution written
- [ ] Correctness argued (not just tested)
- [ ] Off-by-one systematically checked
- [ ] Adversarial inputs tested
- [ ] Confidence honestly assessed
