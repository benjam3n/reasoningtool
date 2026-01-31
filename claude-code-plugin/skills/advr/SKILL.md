---
name: advr
description: "Nothing is a fact until it survives an assassination attempt. Builder constructs claims, Breaker tries to destroy them."
---

# Adversarial Review

**Input**: $ARGUMENTS

---

## Overview

Nothing is a "fact" until it has survived an assassination attempt. The Builder constructs a claim; the Breaker tries to destroy it. Only conclusions that survive attack are trustworthy.

This prevents the passivity of accepting first-obvious answers.

## Steps

### Step 1: Builder — Construct the Claim
State the claim as precisely as possible:

1. What exactly is being claimed?
2. What evidence supports it?
3. What reasoning connects evidence to conclusion?
4. What is the confidence level?
5. What would change if this claim is wrong?

```
BUILDER'S CASE:
Claim: [precise statement]
Evidence:
1. [evidence 1] — strength: [H/M/L]
2. [evidence 2] — strength: [H/M/L]
Reasoning: [how evidence supports claim]
Confidence: [%]
Stakes: [what depends on this being true]
```

### Step 2: Breaker — Attack the Claim
Systematically attempt to destroy the claim:

**Attack the evidence:**
1. Is the evidence real? (Source reliable? Data accurate?)
2. Is the evidence relevant? (Does it actually bear on the claim?)
3. Is the evidence sufficient? (Could the claim be false despite this evidence?)
4. Is the evidence cherry-picked? (What evidence was NOT presented?)
5. Is the evidence current? (Could things have changed?)

**Attack the reasoning:**
1. Does the conclusion follow from the premises? (Valid inference?)
2. Are there hidden assumptions? (What's unstated but required?)
3. Are there logical fallacies? (Ad hominem, straw man, false dilemma, etc.)
4. Is correlation being mistaken for causation?
5. Is the reasoning reversible? (Could the same logic support the opposite?)

**Attack the claim itself:**
1. Is it falsifiable? (Can it be proven wrong in principle?)
2. Is it specific enough to test? (Or so vague it can't fail?)
3. Does it contradict known facts?
4. Is there a simpler explanation for the evidence?
5. What would a knowledgeable opponent say?

### Step 3: Score Each Attack
For each attack that landed:

| Attack | Target | Severity | Claim Survives? |
|--------|--------|----------|----------------|
| [attack description] | evidence/reasoning/claim | fatal/serious/minor | Y/N/weakened |

**Severity levels:**
- Fatal: Claim cannot survive this attack. Must be abandoned or fundamentally revised.
- Serious: Claim is significantly weakened. Needs major revision or additional evidence.
- Minor: Claim still holds but with reduced confidence or narrower scope.
- Missed: Attack doesn't actually undermine the claim.

### Step 4: Builder — Respond to Attacks
For each serious or fatal attack, the Builder can:

1. **Refute**: Show the attack is wrong (provide counter-evidence)
2. **Repair**: Modify the claim to survive the attack (narrow scope, add caveats)
3. **Reinforce**: Add new evidence or reasoning that survives the attack
4. **Concede**: Accept the attack and abandon/revise the claim

```
BUILDER'S RESPONSE:
Attack: [which]
Response type: [refute/repair/reinforce/concede]
Content: [the response]
Revised confidence: [new % if changed]
```

### Step 5: Final Verdict
After Builder-Breaker exchange:

| Outcome | Meaning | Action |
|---------|---------|--------|
| Claim survives all attacks | High confidence — treat as reliable | Accept |
| Claim survives with repairs | Moderate confidence — accept with caveats | Accept with noted limitations |
| Claim partially survives | Split confidence — some parts reliable, some not | Accept reliable parts, reject or investigate weak parts |
| Claim falls to attacks | Low confidence — do not rely on this | Reject or fundamentally revise |

### Step 6: Report
```
ADVERSARIAL REVIEW:
Original claim: [Builder's claim]
Confidence before review: [%]

Attacks:
| # | Attack | Severity | Builder Response | Result |
|---|--------|----------|-----------------|--------|
| 1 | [attack] | [level] | [response] | [survived/weakened/fell] |

Verdict: [survived / survived with repairs / partially survived / fell]
Confidence after review: [%]
Revised claim: [if modified]

Strongest surviving evidence: [what held up]
Weakest point: [most vulnerable aspect]
What would change verdict: [what new evidence/argument would matter]
```

## When to Use
- Before committing to any strategy
- When confidence seems too high for evidence
- When stakes are high
- When you notice you haven't considered alternatives
- → INVOKE: /stc (steelmanned counterarguments) for strongest possible opposition
- → INVOKE: /aw (assume wrong) for systematic wrongness analysis
- → INVOKE: /cv (convergent validation) for multi-method verification

## Verification
- [ ] Claim stated precisely (not vaguely)
- [ ] Breaker attacked evidence, reasoning, AND claim
- [ ] Attacks scored for severity honestly
- [ ] Builder responded to each serious attack
- [ ] Final confidence is calibrated (not just original + or - a bit)
- [ ] Strongest surviving evidence identified
