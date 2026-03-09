---
name: "decide - Make a Decision"
description: Sub-orchestrator for decisions. Routes to comparison, ARAW testing, dominance analysis, or goal clarification based on what the user knows and the stakes involved.
---

# Decide

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Binary choice**: The user faces a yes/no decision ("Should I X?") where the implicit alternative is "don't X."
**Interpretation 2 — Multi-option comparison**: The user has named options ("X or Y or Z?") and needs help choosing between them.
**Interpretation 3 — Open decision**: The user knows they need to decide something but hasn't identified the options yet ("What should I do about X?").

If ambiguous, ask: "Do you have specific options to choose between, or do you need help identifying what the options are?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Every decision is a bet on the future.** The question is never "which is right?" but "which has the best expected outcome given what I know and what I don't know?" Decisions under uncertainty require different tools than decisions under certainty.

2. **"Should I X?" always has a hidden comparator.** The alternative to doing X is not "nothing" — it's whatever the user would do instead. Make the comparator explicit. "Should I quit my job?" compares quitting to staying, but also to other changes that might address the same underlying need.

3. **Criteria must be explicit before comparison.** "Which is better?" is unanswerable without knowing "better for what?" If the user can't state criteria, they need /want first to clarify what they're optimizing for.

4. **Reversibility determines depth.** Reversible decisions (which framework, which restaurant) need light analysis. Irreversible decisions (quit job, major investment, move countries) need deep analysis with pre-mortem and failure anticipation.

5. **The best option is often "none of the above."** If all named options feel wrong, the framing is wrong. Look for the option the user hasn't considered — the reframe, the hybrid, the "wait and gather more information."

6. **Foreclosures matter as much as gains.** Every option gives something up. The user often focuses on what they get and ignores what they lose. Make foreclosures explicit for every option.

---

## Routing Decisions

### 1. Extract the Choice Point

What is being decided? State the options if visible. If only one option is stated ("Should I X?"), the implicit second option is "don't X."

### 2. Is This Actually a Decision?

- **"X is true"** → This is a claim. → INVOKE: /claim $ARGUMENTS
- **"I want X"** → This is a goal, not a choice. → INVOKE: /want $ARGUMENTS
- **"Should I even bother?"** → This is emotional. → INVOKE: /emotion $ARGUMENTS
- **"What about doing X?"** → This is an idea. → INVOKE: /viability $ARGUMENTS
- **"I think X"** (tentative belief) → This is a claim to formalize. → INVOKE: /it $ARGUMENTS
- **"X, but Y"** (decision with objection) → Separate the tension first. → INVOKE: /but $ARGUMENTS
- **"I'm not sure about X"** → Classify the uncertainty. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
- **If it IS a decision** → continue.

### 3. How Many Options?

- **Binary** ("Should I X?"): ARAW on doing X vs not doing X.
- **Multi-option** ("X or Y or Z?"): Compare first, then ARAW the top candidates.
  → INVOKE: /cmp [options] — then /araw on top candidates.
- **Open** ("What should I do about..."): Options unknown — enumerate first.
  → INVOKE: /search $ARGUMENTS — then return here with discovered options.
- **Dominated options present** ("X or Y or Z?" where one is clearly worse):
  → INVOKE: /dom $ARGUMENTS — eliminate dominated options first, then compare survivors.

### 4. Are Criteria Known?

- **Yes** (user states what matters): proceed with comparison using those criteria.
- **No** (user just says "which is better?"): need to clarify what "better" means.
  → INVOKE: /want $ARGUMENTS — clarify the underlying goal, then return with criteria.
- **Vague criteria** ("the best one", "whatever works"): → INVOKE: /obv $ARGUMENTS to check obvious criteria first.
- **Partial** (some criteria stated, others implied): state the implied criteria explicitly and confirm.

### 5. Stakes and Reversibility

- **Reversible** (which framework, which restaurant): lighter analysis, /cmp is sufficient.
- **Costly to reverse** (which job offer, which city): moderate analysis, /cmp + /araw on top choice.
- **Irreversible** (quit job, move countries, major investment): deepest analysis.
  → INVOKE: /araw on each option + /prm (pre-mortem) + /fla (failure anticipation).
- **Unsure about stakes**: → INVOKE: /ecal $ARGUMENTS to calibrate effort first.

### 6. Decision Quality Checks

Before finalizing, consider whether supplementary analysis would help:

| Situation | Also invoke |
|-----------|------------|
| Obvious bad outcomes being ignored | → /obo (obvious bad outcomes) |
| Obvious good outcomes being missed | → /ogo (obvious good outcomes) |
| Decision involves ethical dimensions | → /eth (ethics analysis) |
| Decision involves safety risks | → /saf (safety analysis) |
| Decision could be reframed | → /iaw (in another way) |
| User might be self-deceiving | → /sdc (self-deception check) |
| Decision involves future predictions | → /fut (future analysis) |
| User wants maximum rigor | → /certainty $ARGUMENTS |

### 7. Scope Control

- **User is expanding scope** ("and also what about..."): → INVOKE: /iagca to compress back to the decision.
- **User wants adjacent tasks identified**: → INVOKE: /ata $ARGUMENTS
- **Decision has unresolved sub-decisions**: → INVOKE: /tbd (to be determined)

---

## Execute

**For binary decisions:**
→ INVOKE: /araw [doing X vs not doing X]

**For multi-option with known criteria:**
→ INVOKE: /cmp [options with criteria]

**For multi-option where dominance might simplify:**
→ INVOKE: /dom [options] — then /cmp on survivors

**For open decisions (options unknown):**
→ INVOKE: /search $ARGUMENTS — discover options
→ Then INVOKE: /cmp [discovered options]

**For high-stakes decisions, also:**
→ INVOKE: /prm [chosen option] — imagine it failed, trace back why
→ INVOKE: /fla [chosen option] — anticipate failure modes

**For decisions where criteria are unclear:**
→ INVOKE: /want $ARGUMENTS — find the underlying goal
→ Then return to /decide with clarified criteria

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **False binary** | "Should I X?" tested as yes/no only | Look for the third option — the reframe, the hybrid, the delay |
| **Criteria-free comparison** | "X is better" without stating better-for-what | Stop and clarify criteria before proceeding |
| **Analysis paralysis** | Reversible decision getting deep analysis | Match depth to stakes — reversible decisions need light analysis |
| **Insufficient depth** | Irreversible decision getting light analysis | Irreversible decisions need /araw + /prm + /fla minimum |
| **Foreclosure blindness** | Only looking at what options gain, not what they give up | Map foreclosures explicitly for every option |
| **Framing lock** | All options feel wrong but analysis continues | Step back — wrong options usually mean wrong framing. Reframe what's actually being decided |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Quick — state options, criteria, recommendation | Options listed, criteria applied, quick verdict |
| **2x** | Standard — /cmp with explicit criteria, foreclosures noted | Full comparison table, foreclosures for each, recommendation with confidence |
| **4x** | Thorough — /cmp + /araw on top candidate + assumption check | Comparison + stress test of winner + assumptions surfaced |
| **8x** | Deep — /araw each option + /prm + /fla + alternative framing check | Full analysis of all options, failure modes mapped, foreclosures, reframe explored |

---

## Pre-Completion Checklist

- [ ] All options explicitly stated (including hidden "do nothing" or "do something else")
- [ ] Criteria for "better" made explicit
- [ ] Each option assessed against criteria
- [ ] Foreclosures mapped for each option (what you give up)
- [ ] Depth matched to stakes (reversible = light, irreversible = deep)
- [ ] Pre-mortem done for high-stakes decisions
- [ ] Recommendation stated with confidence level
- [ ] What would change the recommendation is explicit

---

## After Completion

Report:
- The decision as framed
- Options considered (and any dominated options eliminated early)
- Criteria used (stated or derived)
- Comparison results
- Foreclosures for each option
- Recommendation with confidence level
- What would change the recommendation
- First action if the recommendation is followed

### Follow-Up Routing

After the decision is made, the user may need:
- **"How do I do this?"** → INVOKE: /how $ARGUMENTS
- **"What's the plan?"** → INVOKE: /action $ARGUMENTS
- **"What could go wrong?"** → INVOKE: /fla or /dys
- **"What are the implications?"** → INVOKE: /sycs
- **"What's left to decide?"** → INVOKE: /tbd

---

## Integration

- **Use from**: /viability (after idea tested, need to decide whether to pursue), /search (after options discovered, need to choose), /emotion (after feeling processed, implicit decision surfaces)
- **Routes to**: /cmp (multi-option comparison), /araw (stress-test each option), /prm (pre-mortem), /fla (failure anticipation), /dom (dominance elimination), /want (when criteria unclear), /search (when options unknown)
- **Differs from**: /claim (decide compares options, claim tests a single proposition), /viability (decide chooses between options, viability tests one idea), /evaluate (decide is forward-looking choice, evaluate is backward-looking assessment)
- **Complementary**: /aex (surface assumptions behind each option), /cba (cost-benefit analysis), /dcp (decision criteria prioritization), /obo (obvious bad outcomes), /ogo (obvious good outcomes)
