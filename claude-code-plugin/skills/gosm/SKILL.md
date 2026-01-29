---
name: gosm
description: Main GOSM entry point - Context-adaptive router that selects appropriate GOSM variant based on situation
context: fork
---

# GOSM - Goal-Oriented State Machine (Context-Adaptive)

**Input**: $ARGUMENTS

---

## Context Detection (Run First)

Before applying any GOSM variant, detect the context to select the right variant.

### Context Assessment

| Factor | Question | Options |
|--------|----------|---------|
| **Time Pressure** | How urgent is this? | URGENT (< 5 min) / NEAR (< 1 hour) / NORMAL (> 1 hour) |
| **Stakes** | What's at risk if wrong? | HIGH (major impact) / MED (significant) / LOW (minor) |
| **Domain Expertise** | Does user know this domain? | EXPERT / INTERMEDIATE / NOVICE |
| **Action Cost** | Is trying cheap or expensive? | CHEAP (reversible) / EXPENSIVE (one-shot) |
| **Information State** | How much is known? | RICH / MODERATE / SPARSE |

### Context Classification

```
CONTEXT ASSESSMENT
==================
Time: [URGENT/NEAR/NORMAL]
Stakes: [HIGH/MED/LOW]
Expertise: [EXPERT/INTERMEDIATE/NOVICE]
Action cost: [CHEAP/EXPENSIVE]
Information: [RICH/MODERATE/SPARSE]

DERIVED VARIANT: [see matrix below]
```

### Variant Selection Matrix

| Context Pattern | Variant | Why |
|-----------------|---------|-----|
| URGENT + any stakes | **GOSM-Lite** | No time for full analysis |
| LOW stakes + CHEAP action | **GOSM-Quick** | Overkill to analyze |
| EXPERT + HIGH confidence | **GOSM-Check** | Just validate, don't explore |
| CHEAP action + SPARSE info | **GOSM-After** | Learn by doing |
| HIGH stakes + EXPENSIVE + NOVICE | **GOSM-Full** | Need comprehensive analysis |
| MED stakes + NORMAL time | **GOSM-Standard** | Balanced approach |

### Override Conditions

User can explicitly request a variant:
- "Quick analysis" / "quick" → GOSM-Quick
- "Full analysis" / "full" / "comprehensive" → GOSM-Full
- "Just check this" / "validate" → GOSM-Check
- "I already did this" / "after" / "reflect" → GOSM-After
- "lite" / "fast" → GOSM-Lite

---

## GOSM-Lite (5 Essential Steps)

**For**: URGENT situations, time pressure
**Duration**: < 5 minutes
**Steps**: 5

```
GOSM-LITE
=========

1. WHAT IS IT?
   Type: [GOAL/PROBLEM/QUESTION/DECISION]
   Core claim: [One sentence]

2. CRITICAL ASSUMPTION?
   The ONE thing that if wrong changes everything:
   [assumption]
   Confidence: [HIGH/MED/LOW]

3. ASSUME WRONG (Quick)
   If [assumption] is wrong:
   - Best alternative: [one alternative]
   - Risk if we proceed: [one risk]

4. IMMEDIATE ACTION
   DO: [specific next action]
   WHY: [one-sentence justification]
   VERIFY: [how to know it worked]

5. REVISIT WHEN
   [ ] Time permits for deeper analysis
   [ ] New information arrives
   [ ] Action doesn't produce expected result
```

**Key insight**: Under time pressure, find the ONE critical assumption and test only that.

---

## GOSM-Quick (2 Steps)

**For**: LOW stakes, reversible decisions
**Duration**: < 2 minutes
**Steps**: 2

```
GOSM-QUICK
==========

1. SANITY CHECK
   - Does this violate any obvious constraints? [Y/N]
   - Is there a clearly better option I'm ignoring? [Y/N]
   - Will I regret not thinking harder? [Y/N]

   If all NO → Proceed
   If any YES → Flag which, decide if worth deeper analysis

2. ACTION
   DO: [action]
   UNDO IF: [condition for reversal]
```

**Key insight**: For low-stakes reversible decisions, the cost of analysis exceeds the value.

---

## GOSM-Check (Validation Only)

**For**: EXPERT domains, high confidence decisions
**Duration**: < 10 minutes
**Steps**: 3

```
GOSM-CHECK
==========

User's proposed approach: [their plan]

1. BLIND SPOT SCAN
   | Area | Checked? | Issue Found? |
   |------|----------|--------------|
   | Obvious failure modes | [ ] | [none / describe] |
   | Missing stakeholders | [ ] | [none / describe] |
   | Unrealistic assumptions | [ ] | [none / describe] |
   | Resource gaps | [ ] | [none / describe] |
   | Timeline issues | [ ] | [none / describe] |

2. CONTRARIAN CHALLENGE
   The strongest argument AGAINST this approach:
   [one paragraph]

   User's likely response:
   [anticipated]

   Is the challenge fatal? [Y/N + why]

3. VERDICT
   [ ] PROCEED - No issues found
   [ ] PROCEED WITH CAUTION - Minor issues: [list]
   [ ] PAUSE - Significant issue needs addressing: [describe]
   [ ] RETHINK - Fundamental problem: [describe]
```

**Key insight**: Experts don't need exploration; they need validation and blind-spot checking.

---

## GOSM-After (Reflection Mode)

**For**: Action-first contexts, learning by doing
**Duration**: < 15 minutes (after action)
**Steps**: 4

```
GOSM-AFTER
==========

Action taken: [what was done]
Result: [what happened]

1. EXPECTATION vs REALITY
   Expected: [what you thought would happen]
   Actual: [what actually happened]
   Gap: [describe discrepancy]

2. WHAT THIS REVEALS
   | Revealed | Implication |
   |----------|-------------|
   | [learning 1] | [what to do differently] |
   | [learning 2] | [what to do differently] |
   | [learning 3] | [what to do differently] |

3. UPDATED MODEL
   Before: [old assumption/model]
   After: [revised assumption/model]
   Confidence: [HIGH/MED/LOW]

4. NEXT ACTION
   Based on what was learned:
   DO: [next specific action]
   TEST: [what this will reveal]
```

**Key insight**: When action is cheap, learn by doing rather than analyzing first.

---

## GOSM-Standard (Balanced)

**For**: MED stakes, NORMAL time
**Duration**: 15-30 minutes
**Steps**: 8

```
GOSM-STANDARD
=============

1. CLASSIFY INPUT
   Type: [GOAL/PROBLEM/QUESTION/DECISION/SITUATION/FEELING]

2. PARSE KEY CLAIMS
   Surface claims:
   1. [claim 1]
   2. [claim 2]

   Bundled guesses (hidden assumptions):
   - [hidden 1]
   - [hidden 2]

3. ARAW (Key Claims Only)
   Claim: [most important claim]
   ASSUME RIGHT: [implications]
   ASSUME WRONG: [alternatives]

4. GOAL JOURNEY (Brief)
   Current → [state] → Desired: [state]
   Serves: [higher goal]

5. DUAL ANALYSIS
   CONTRARIAN: [key challenge]
   NON-CONTRARIAN: [key path forward]

6. FILTER BY ACTIONABLE
   What can user actually do? [list]

7. CRUX QUESTIONS
   The one question that matters most:
   [question]

8. RECOMMENDED ACTION
   DO: [specific action]
   SERVES: [which goal]
   VERIFY: [success indicator]
```

---

## GOSM-Full (Comprehensive)

**For**: HIGH stakes, EXPENSIVE action, NOVEL domain
**Duration**: 30-60+ minutes
**Steps**: 12 (full procedure_engine)

→ INVOKE: /procedure_engine $ARGUMENTS

Use the complete 12-step procedure engine for maximum thoroughness.

---

## Variant Comparison Table

| Variant | Steps | Time | When | Key Focus |
|---------|-------|------|------|-----------|
| **GOSM-Lite** | 5 | <5min | URGENT | One critical assumption |
| **GOSM-Quick** | 2 | <2min | LOW stakes | Sanity check only |
| **GOSM-Check** | 3 | <10min | EXPERT | Validate, find blind spots |
| **GOSM-After** | 4 | <15min | Post-action | Learn from results |
| **GOSM-Standard** | 8 | 15-30min | BALANCED | Key claims, brief analysis |
| **GOSM-Full** | 12 | 30-60min | HIGH stakes | Comprehensive exploration |

---

## Niche Documentation

### Where GOSM Works Best

| Condition | Why It Helps |
|-----------|--------------|
| **High stakes** | Cost of error justifies analysis |
| **Novel domain** | Can't rely on intuition/expertise |
| **Expensive action** | One-shot decisions need pre-analysis |
| **Propositional content** | ARAW works on claims |
| **Time abundance** | Full exploration is possible |
| **Complex trade-offs** | Multiple factors need balancing |

### Where GOSM Struggles

| Condition | Better Alternative |
|-----------|-------------------|
| **Time pressure** | GOSM-Lite or heuristics |
| **Low stakes** | GOSM-Quick or just act |
| **Expert domain** | GOSM-Check or intuition |
| **Cheap action** | GOSM-After or trial-and-error |
| **Non-propositional** | Intuition, images, embodied |
| **Well-understood** | Apply known solution |

### When NOT to Use GOSM

1. **Trivial decisions** - "What should I have for lunch?" → Just pick
2. **Rote execution** - Clear procedure exists → Follow it
3. **Pure skill domains** - Sports, music → Practice, not analysis
4. **Emotional support needed** - User needs empathy → Provide it first
5. **Emergency response** - House on fire → Act, don't analyze

---

## Execution Flow

1. Run **Context Detection** (always first)
2. Select variant based on matrix
3. Check for user override
4. Execute selected variant
5. Note if variant seemed appropriate (for learning)

**Begin now**: Assess context for input.
