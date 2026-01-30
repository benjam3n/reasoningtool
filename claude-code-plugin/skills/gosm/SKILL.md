---
name: "gosm - Goal-Oriented State Machine"
description: Goal-Oriented State Machine. Context-adaptive dispatcher that routes to the right analysis depth based on urgency, stakes, and expertise.
context: This is the default entry point. When a user needs help thinking through something and hasn't specified a skill, GOSM selects the appropriate depth.
---

# GOSM - Goal-Oriented State Machine

**Input**: $ARGUMENTS

---

## Principle

Match analysis depth to the situation. Don't overthink low-stakes decisions. Don't underthink high-stakes ones.

---

## Context Assessment

Assess these five factors to select the right variant:

| Factor | Options |
|--------|---------|
| **Urgency** | URGENT (minutes) / SOON (hours) / NORMAL (days+) |
| **Stakes** | HIGH (major impact) / MEDIUM / LOW (minor) |
| **Expertise** | EXPERT (user knows domain) / INTERMEDIATE / NOVICE |
| **Action Cost** | CHEAP (reversible) / EXPENSIVE (one-shot) |
| **Information** | RICH (lots known) / MODERATE / SPARSE |

---

## Variant Selection

| Context | Variant | What It Does |
|---------|---------|-------------|
| URGENT + any | **Lite** | Find the ONE critical assumption. Test it. Act. |
| LOW stakes + CHEAP | **Quick** | Sanity check. If nothing's obviously wrong, proceed. |
| EXPERT + HIGH confidence | **Check** | Validate the user's plan. Find blind spots. |
| Post-action / reflecting | **After** | Learn from what happened. Update model. |
| MEDIUM stakes + NORMAL time | **Standard** | Balanced analysis: key claims, brief ARAW, action. |
| HIGH stakes + EXPENSIVE + NOVICE | **Full** | Comprehensive: invoke `/pce` |

User can override: "quick", "full", "just check this", "reflect on what happened".

---

## Lite (< 5 minutes)

For urgent situations. Find the ONE assumption that matters most.

1. **What's the core claim?** (one sentence)
2. **What's the critical assumption?** (the one thing that changes everything if wrong)
3. **Quick ASSUME WRONG**: If that assumption is wrong, what's the best alternative? What's the risk?
4. **Action**: What to do right now. How to verify it worked.
5. **Revisit when**: Time permits / new info arrives / action didn't work.

---

## Quick (< 2 minutes)

For low-stakes, reversible decisions. Don't overthink.

1. **Sanity check**: Any obvious constraints violated? Any clearly better option being ignored? Will I regret not thinking harder?
2. If all clear → **Proceed**. Note the undo condition.
3. If anything flagged → Decide if it's worth deeper analysis.

---

## Check (< 10 minutes)

For experts who have a plan. Don't explore — validate.

1. **Blind spot scan**: Obvious failure modes? Missing stakeholders? Unrealistic assumptions? Resource gaps? Timeline issues?
2. **Strongest argument against**: What's the best case for NOT doing this?
3. **Verdict**: PROCEED / PROCEED WITH CAUTION (issues noted) / PAUSE (significant issue) / RETHINK (fundamental problem)

---

## After (< 15 minutes)

For reflecting on actions already taken.

1. **Expected vs actual**: What did you think would happen? What did happen? What's the gap?
2. **What this reveals**: For each learning — what to do differently.
3. **Updated model**: What did you believe before? What do you believe now?
4. **Next action**: Based on what was learned.

---

## Standard (15-30 minutes)

Balanced analysis for medium-stakes situations.

1. **Classify**: GOAL / PROBLEM / QUESTION / DECISION / SITUATION
2. **Key claims**: Surface + hidden assumptions (2-4 claims)
3. **ARAW the most important claim**: Assume Right → what follows? Assume Wrong → what alternatives?
4. **Goal journey**: Current state → desired state → what serves this?
5. **Contrarian view**: What's the strongest challenge?
6. **Actionable filter**: What can the user actually do?
7. **Crux question**: The one question that matters most.
8. **Recommended action**: Specific, with verification.

---

## Full (30-60+ minutes)

For high-stakes, expensive, novel situations. Invokes the full procedure engine.

→ `/pce $ARGUMENTS`

---

## Pre-Completion Check

- [ ] Context assessed (urgency, stakes, expertise, cost, information)
- [ ] Variant matches context (or user override applied)
- [ ] Output depth matches variant (Lite = focused, Full = comprehensive)
- [ ] Specific action recommended
