---
name: "viability - Test an Idea"
description: Sub-orchestrator for ideas and proposals. Routes to ARAW viability testing with appropriate development, risk assessment, and supplementary analysis for outcome projection and reframing.
output:
  format: "prose"
---

# Viability

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Seed idea**: The user has an underdeveloped idea ("What about X?", "What if we...") that needs fleshing out before it can be tested.
**Interpretation 2 — Developed proposal**: The user has a reasoned proposal ("I think we should X because Y, and it would work by Z") ready for balanced testing.
**Interpretation 3 — Fully formed plan**: The user has a detailed proposal with reasoning — this is evaluation, not idea testing.

If ambiguous, ask: "Is this a rough idea you want explored, or a developed proposal you want stress-tested?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Ideas are tested for viability, not truth.** The question is "would this work?" not "is this true?" Viability means: is it achievable, sustainable, and worth the cost?

2. **Seed ideas need development before adversarial testing.** Attacking an underdeveloped idea is unfair and useless. First develop it (AR), then stress-test it (AW).

3. **Every idea has prerequisites.** "We should build X" requires resources, skills, time, market conditions, etc. Surfacing prerequisites is as important as testing the idea itself.

4. **Every idea forecloses alternatives.** Pursuing idea A means not pursuing ideas B, C, D. Make foreclosures explicit.

5. **Risk profile determines depth.** Low-risk, reversible ideas need light testing. High-risk, irreversible ideas need deep testing with pre-mortem and failure anticipation.

---

## Routing Decisions

### 1. Extract the Idea

What is being proposed? State it as "What if [idea]?" or "[Idea] could work because [reason]."

### 2. Is This Actually an Idea?

- **"X is true"** → This is a claim (testing truth, not viability). → INVOKE: /claim $ARGUMENTS
- **"Should I X?"** → This is a decision (choosing, not proposing). → INVOKE: /decide $ARGUMENTS
- **"I want X"** → This is a goal. → INVOKE: /want $ARGUMENTS
- **"How do I X?"** → This is method-seeking. → INVOKE: /how $ARGUMENTS
- **"I think X might work"** → Formalize the belief. → INVOKE: /it $ARGUMENTS
- **"X could work, but Y"** → Idea with objection. → INVOKE: /but $ARGUMENTS
- **"I'm not sure if X would work"** → Classify the uncertainty. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
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
  → INVOKE: /obo [idea] — check for obvious bad outcomes
  → INVOKE: /saf [idea] — if safety-relevant
- **Unsure about risk**: → INVOKE: /ecal $ARGUMENTS to calibrate effort.

### 6. Needs Comparison?

- **Yes** ("Should we do X or Y?"): this is actually a decision.
  → INVOKE: /decide $ARGUMENTS
- **No** ("Is X viable?"): test viability standalone.

### 7. Outcome Projection

For ideas with significant consequences, consider projecting outcomes:

| Situation | Also invoke |
|-----------|------------|
| Need best-case scenario | → /utp (utopia analysis) |
| Need worst-case scenario | → /dys (dystopia analysis) |
| Need good outcome identification | → /gop (good outcome analysis) |
| Need future trajectory | → /fut (future analysis) |
| Idea has obvious upsides being missed | → /ogo (obvious good outcomes) |
| Idea has obvious downsides being ignored | → /obo (obvious bad outcomes) |

### 8. Idea Quality Enhancement

| Situation | Also invoke |
|-----------|------------|
| Idea could be reframed | → /iaw (in another way) |
| Idea is a platitude | → /platitude (operationalize) |
| Idea has "etc" or implied scope | → /etc or /aso |
| Idea scope expanding | → /iagca (scope compression) |
| Need to trace implications | → /sycs (so you can see) |
| Idea involves ethical dimensions | → /eth (ethics analysis) |
| Need to differentiate from similar ideas | → /difr |
| Need narrative to make idea vivid | → /story |

### 9. Depth and Mode Selection

| Situation | Mode |
|-----------|------|
| User wants quick gut check | → /ezy (easy mode) |
| User wants maximum rigor | → /hrd (hard mode) or /certainty |
| User wants general principle | → /genl (what general pattern does this idea follow?) |
| User wants specific application | → /spcf (apply known framework to this idea) |
| User wants sophisticated multi-layer analysis | → /soph |

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
→ INVOKE: /obo [idea]

### Supplementary Analysis (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Idea might be self-deception | → /sdc (self-deception check) |
| Idea has hidden assumptions | → /aex (assumption extraction) |
| Idea could be tested empirically | → /abts (A/B test design) |
| Idea has unresolved sub-decisions | → /tbd (to be determined) |
| Adjacent implications should be surfaced | → /ata (and then also) |
| User wants debate format | → /deb (debate structure) |

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Premature attack** | Seed idea critiqued before being developed | Develop first (AR), then attack (AW) |
| **Viability confusion** | Testing truth instead of workability | Ask "would this work?" not "is this true?" |
| **Risk mismatch** | High-risk idea getting light analysis | Match depth to risk — high stakes need /prm + /fla |
| **Foreclosure blindness** | Only analyzing what the idea enables, not what it prevents | Map what pursuing this idea gives up |
| **Enthusiasm bias** | User is excited and analysis matches their enthusiasm | Counterbalance — excited user needs harder AW |

---

## Depth Scaling

| Depth | Scope | Floor |
|-------|-------|-------|
| **1x** | Quick check — one AR/AW pass, verdict | 5 findings |
| **2x** | Standard — develop, test, prerequisites, verdict | 12 findings |
| **4x** | Thorough — full ARAW, failure modes, prerequisites, foreclosures | 25 findings |
| **8x** | Deep — everything above plus pre-mortem, comparison to alternatives, risk matrix | 45 findings |

---

## Pre-Completion Checklist

- [ ] Idea stated clearly
- [ ] Development level assessed (seed / developed / fully formed)
- [ ] Risk profile assessed
- [ ] AR completed (what the idea looks like if right)
- [ ] AW completed (what could go wrong)
- [ ] Prerequisites identified
- [ ] Foreclosures identified
- [ ] Verdict stated with confidence level

---

## After Completion

Report:
- The idea as stated
- Viability verdict (viable / conditional / blocked / eliminated)
- What it would require (prerequisites, resources, capabilities)
- What could go wrong (key failure modes)
- What it would foreclose (what you give up)
- Recommended next step (develop further / test more / build / abandon)

### Follow-Up Routing

After viability is assessed, the user may need:
- **"How do I do this?"** → INVOKE: /how $ARGUMENTS
- **"Should I do this?"** → INVOKE: /decide
- **"What could go wrong?"** → INVOKE: /fla or /dys
- **"What are the implications?"** → INVOKE: /sycs
- **"What else should I consider?"** → INVOKE: /ata
- **"What skill should I run next?"** → INVOKE: /next or /fonss

---

## Integration

- **Use from**: /emotion (excitement → test the idea), /search (after options found, test the most promising), /decide (when a decision option needs viability testing)
- **Routes to**: /ar (develop seed ideas), /aw (attack developed ideas), /araw (balanced testing), /prm (pre-mortem), /fla (failure anticipation), /evaluate (if fully formed)
- **Differs from**: /claim (viability tests workability, claim tests truth), /evaluate (viability tests proposed ideas, evaluate assesses existing work), /decide (viability tests one idea, decide compares options)
- **Complementary**: /obo (obvious bad outcomes), /gop (good outcomes), /fut (future projections), /iaw (alternative framings), /aex (hidden assumptions)
