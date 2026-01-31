---
name: "claim - Test a Claim"
description: Sub-orchestrator for claims and assertions. Routes to ARAW-based testing with appropriate depth and balance.
---

# Claim

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Extract the Proposition

What is being claimed? State it as a single testable sentence.

If the input is vague, restate it precisely before proceeding.

### 2. Is This Actually a Claim?

- **"Should I X?"** → This is a decision, not a claim. → INVOKE: /decide $ARGUMENTS
- **"I want X"** → This is a goal. → INVOKE: /want $ARGUMENTS
- **"I'm frustrated that X"** → This is emotional. → INVOKE: /emotion $ARGUMENTS
- **"What are the options for X?"** → This is exploration. → INVOKE: /search $ARGUMENTS
- **If it IS a claim** → continue.

### 3. Single or Bundled?

- **Single claim**: proceed directly.
- **Multiple claims bundled**: unbundle into separate claims. Test the most load-bearing one first, then the others.

### 4. Is the Claim Testable?

- **Testable** ("Remote work is more productive"): proceed to ARAW.
- **Untestable/definitional** ("Freedom is the highest value"): unpack what it would MEAN for this to be true — what observable consequences follow? Test those instead.

### 5. Determine Depth

- Fragment or single sentence with no qualifiers → 2x
- Sentence with context or qualifiers → 4x
- Paragraph with reasoning → 4x-8x
- User specifies depth → use that

### 6. Set AR/AW Balance

- User says "I believe X" or asserts confidently → push AW harder (test the doubt side more). 60% AW.
- User says "I doubt X" or is skeptical → push AR harder (find what supports it). 60% AR.
- User says "Is X true?" with no lean → balanced 50/50.
- Default: 50/50.

---

## Execute

→ INVOKE: /araw $ARGUMENTS

Use the depth and balance determined above. If the claim had many hidden assumptions, also invoke /aex on the claim after ARAW completes.

---

## After Completion

Report:
- The claim as tested
- Verdict from ARAW (viable / conditional / eliminated / uncertain)
- Key AR findings and key AW findings
- What would change the verdict
