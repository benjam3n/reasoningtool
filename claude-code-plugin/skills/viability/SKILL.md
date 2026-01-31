---
name: "viability - Test an Idea"
description: Sub-orchestrator for ideas and proposals. Routes to ARAW viability testing with appropriate development and risk assessment.
---

# Viability

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Extract the Idea

What is being proposed? State it as "What if [idea]?" or "[Idea] could work because [reason]."

### 2. Is This Actually an Idea?

- **"X is true"** → This is a claim (testing truth, not viability). → INVOKE: /claim $ARGUMENTS
- **"Should I X?"** → This is a decision (choosing, not proposing). → INVOKE: /decide $ARGUMENTS
- **"I want X"** → This is a goal. → INVOKE: /want $ARGUMENTS
- **"How do I X?"** → This is method-seeking. → INVOKE: /how $ARGUMENTS
- **If it IS an idea/proposal** → continue.

### 3. Idea vs Claim

Key distinction:
- **Ideas** are tested for **viability** — would it work? What would it require? What could go wrong?
- **Claims** are tested for **truth** — is this actually the case?

"We should pivot to B2B" is an idea (viability). "B2B is more profitable than B2C" is a claim (truth).

### 4. How Developed Is the Idea?

- **Seed** ("What about X?", "What if we..."): underdeveloped. Needs AR first to flesh out what it would look like if right, THEN AW to find problems.
  → INVOKE: /ar [idea] — develop it first.
  → Then INVOKE: /aw [developed idea] — find the problems.
- **Developed** ("I think we should X because Y, and it would work by Z"): ready for balanced testing.
  → INVOKE: /araw [idea]
- **Fully formed** (detailed proposal with reasoning): this is evaluation, not idea testing.
  → INVOKE: /evaluate $ARGUMENTS

### 5. Risk Profile

- **Low risk** (easy to try, easy to reverse): lighter analysis. ARAW at 2x.
- **High risk** (expensive, irreversible, high stakes): deep analysis. ARAW at 4x+, plus:
  → INVOKE: /prm [idea] — imagine it failed, ask why
  → INVOKE: /fla [idea] — anticipate failure modes

### 6. Needs Comparison?

- **Yes** ("Should we do X or Y?"): this is actually a decision.
  → INVOKE: /decide $ARGUMENTS
- **No** ("Is X viable?"): test viability standalone.

---

## Execute

**Seed ideas:**
→ INVOKE: /ar [idea] — develop: what would this look like if right?
→ Then INVOKE: /aw [developed idea] — find problems

**Developed ideas:**
→ INVOKE: /araw [idea] — test both sides

**High-risk ideas, also:**
→ INVOKE: /prm [idea]
→ INVOKE: /fla [idea]

---

## After Completion

Report:
- The idea as stated
- Viability verdict (viable / conditional / blocked / eliminated)
- What it would require (prerequisites, resources, capabilities)
- What could go wrong (key failure modes)
- What it would foreclose (what you give up)
- Recommended next step (develop further / test more / build / abandon)
