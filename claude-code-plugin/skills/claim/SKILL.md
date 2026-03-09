---
name: "claim - Test a Claim"
description: Sub-orchestrator for claims and assertions. Routes to ARAW-based testing with appropriate depth, balance, and supplementary analysis skills.
---

# Claim

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Direct assertion**: The user states something as fact ("X is true", "Y causes Z") and it needs testing.
**Interpretation 2 — Uncertain belief**: The user holds a belief with some doubt ("I think X", "Is X true?") and wants it examined.
**Interpretation 3 — Received wisdom**: The user presents something they've heard or read ("People say X", "The conventional view is X") and wants to know if it holds up.

If ambiguous, ask: "Are you asserting this, questioning it, or reporting what others believe?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Claims are tested, not confirmed.** The default posture is skeptical curiosity, not validation. Testing means genuinely trying to break the claim, not finding reasons to agree with it.

2. **Bundled claims must be unbundled.** "Remote work is better" contains at least three claims: better for whom, better by what measure, and better under what conditions. Each gets tested separately. The most load-bearing claim goes first.

3. **Untestable claims are restated, not dismissed.** "Freedom is the highest value" can't be tested as-is, but its observable consequences can. Convert to testable predictions, then test those.

4. **The user's confidence determines the balance.** Confident assertions need harder adversarial testing (push AW). Uncertain doubts need harder supportive testing (push AR). Never match the user's emotional investment — counterbalance it.

5. **Verdicts are earned, not declared.** A claim is VALIDATED only when AR evidence reaches bedrock and AW doesn't find fatal flaws at bedrock. "Probably true" is not a verdict — it's a failure to test deeply enough.

6. **The most interesting finding is usually the condition.** Most claims are neither universally true nor universally false. The valuable output is: "True when A, false when B, and the crux is whether you're in A or B."

---

## Routing Decisions

### 1. Extract the Proposition

What is being claimed? State it as a single testable sentence.

If the input is vague, restate it precisely before proceeding. A claim must be falsifiable — it must be possible for it to be wrong.

### 2. Is This Actually a Claim?

- **"Should I X?"** → This is a decision, not a claim. → INVOKE: /decide $ARGUMENTS
- **"I want X"** → This is a goal. → INVOKE: /want $ARGUMENTS
- **"I'm frustrated that X"** → This is emotional. → INVOKE: /emotion $ARGUMENTS
- **"What are the options for X?"** → This is exploration. → INVOKE: /search $ARGUMENTS
- **"I think X"** (tentative, uncertain) → Use /it to formalize the claim first. → INVOKE: /it $ARGUMENTS
- **"X, but Y"** (claim with objection attached) → Use /but to separate and resolve. → INVOKE: /but $ARGUMENTS
- **"I'm not sure about X"** → Use /nsa to classify the uncertainty first. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
- **If it IS a claim** → continue.

### 3. Claim Shape Detection

- **Single claim**: proceed directly.
- **Multiple claims bundled**: unbundle into separate claims. Test the most load-bearing one first, then the others.
- **Claim with "etc" or "and so on"**: expand the implicit list first. → INVOKE: /etc or /aso on the claim tail, then test each expanded claim.
- **Claim that is a platitude** ("Move fast and break things", "Fail fast"): needs operationalization before testing. → INVOKE: /platitude $ARGUMENTS — then test the operationalized version.
- **Contradictory platitudes** ("Move fast" vs "Measure twice"): → INVOKE: /platitudes $ARGUMENTS
- **Hidden compound**: "X is better than Y" bundles "X has property A", "Y lacks property A", and "property A is the right measure." Unbundle all three.

### 4. Is the Claim Testable?

- **Testable** ("Remote work is more productive"): proceed to ARAW.
- **Untestable/definitional** ("Freedom is the highest value"): unpack what it would MEAN for this to be true — what observable consequences follow? Test those instead.
- **Ethical/moral claim** ("We should do X because it's right"): needs ethical analysis alongside truth-testing. → INVOKE: /eth $ARGUMENTS — then ARAW the factual components.

### 5. Determine Depth

- Fragment or single sentence with no qualifiers → 2x
- Sentence with context or qualifiers → 4x
- Paragraph with reasoning → 4x-8x
- User specifies depth → use that
- User wants maximum rigor → INVOKE: /certainty $ARGUMENTS instead

### 6. Set AR/AW Balance

- User says "I believe X" or asserts confidently → push AW harder (test the doubt side more). 60% AW.
- User says "I doubt X" or is skeptical → push AR harder (find what supports it). 60% AR.
- User says "Is X true?" with no lean → balanced 50/50.
- User reports received wisdom ("people say X") → push AW harder. 60% AW.
- Default: 50/50.

### 7. Does the Claim Need Context First?

Before testing, some claims need additional framing:

- **Claim about the future** ("AI will replace programmers by 2030"): → also INVOKE: /fut $ARGUMENTS for temporal context.
- **Claim about what's obvious** ("Obviously we should X"): → also INVOKE: /obv $ARGUMENTS to check if the "obvious" holds up.
- **Claim that something is safe/dangerous**: → also INVOKE: /saf $ARGUMENTS for safety-specific analysis.
- **Claim with hidden assumptions**: → also INVOKE: /aex $ARGUMENTS to surface them before testing.

---

## Execute

→ INVOKE: /araw $ARGUMENTS

Use the depth and balance determined above.

**For bundled claims:**
→ Unbundle first, then INVOKE: /araw on the most load-bearing claim
→ Then INVOKE: /araw on remaining claims if needed

**For untestable claims:**
→ Restate as testable prediction first
→ Then INVOKE: /araw on the restated claim

### Supplementary Analysis (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Claim is an argument with premises | → /agsk (argument analysis) |
| Claim involves predictions | → /fut (future analysis) |
| Claim involves best/worst outcomes | → /gop, /obo, /ogo |
| Claim seems too easy or obvious | → /obv (obvious check) |
| You suspect self-deception | → /sdc (self-deception check) |
| Claim involves safety | → /saf (safety analysis) |
| Claim involves ethics | → /eth (ethics analysis) |
| Claim could be tested empirically | → /abts (A/B test design) |

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Confirmation testing** | AR much deeper than AW; all claims VALIDATED | Push AW harder — find the genuine weaknesses |
| **Unbundling failure** | Compound claim tested as single unit | Decompose into atomic claims, test each |
| **Vague verdict** | "It's complicated" or "it depends" without specifics | State exactly what it depends ON — name the conditions |
| **Testing the wrong claim** | Lots of analysis but the user's actual question isn't answered | Re-read the input; are you testing what they asked? |
| **Definitional dodge** | Claim restated until trivially true | Test the version that has real-world implications, not the safe version |
| **Balance mismatch** | Testing aligns with user's confidence instead of counterbalancing | If user is confident, push AW. If doubtful, push AR. |

---

## Depth Scaling

| Depth | Scope | Floor |
|-------|-------|-------|
| **1x** | Quick test — one AR/AW pass on the main claim | 5 claims, 12 findings |
| **2x** | Standard — unbundle, test main claim, note conditions | 7 claims, 20 findings |
| **4x** | Thorough — all claims tested, assumptions surfaced | 12 claims, 35 findings |
| **8x** | Deep — full unbundling, all claims to bedrock, alternatives derived | 18 claims, 55 findings |

---

## Pre-Completion Checklist

- [ ] Claim extracted and stated as testable sentence
- [ ] Bundled claims unbundled into separate propositions
- [ ] AR/AW balance set based on user's confidence level
- [ ] ARAW executed at appropriate depth
- [ ] Verdict derived from evidence (not asserted)
- [ ] Conditions identified (when true / when false)
- [ ] What would change the verdict is stated
- [ ] Hidden assumptions surfaced (via /aex if needed)

---

## After Completion

Report:
- The claim as tested (restated precisely)
- Whether it was unbundled (and which sub-claim was most load-bearing)
- Verdict from ARAW (validated / conditional / damaged / rejected / uncertain)
- Key AR findings and key AW findings
- Conditions (true when X, false when Y)
- What would change the verdict
- If supplementary skills were used, their findings integrated

### Follow-Up Routing

After the claim is tested, the user may need:
- **"What should I do about this?"** → INVOKE: /decide or /how
- **"What are the implications?"** → INVOKE: /sycs $ARGUMENTS
- **"What's the worst case?"** → INVOKE: /dys $ARGUMENTS
- **"What skill should I run next?"** → INVOKE: /next or /fonss

---

## Integration

- **Use from**: /emotion (doubt about self becomes testable claim), /evaluate (core claims extracted and tested), /diagnose (suspected cause tested as claim), /decide (each option's premises tested)
- **Routes to**: /araw (primary — the testing engine), /aex (assumption extraction), /it (claim formalization), /but (claim-objection separation), /eth (ethical claims), /fut (future claims)
- **Differs from**: /viability (claim tests truth, viability tests workability), /evaluate (claim tests a proposition, evaluate assesses a piece of work), /decide (claim tests one statement, decide compares options)
- **Complementary**: /aex (surface hidden assumptions), /se (enumerate alternative claims), /ver (GOSM verification for empirical claims), /obv (test "obvious" claims)
