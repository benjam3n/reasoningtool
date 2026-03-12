---
name: "but - Contrast and Objection Handler"
description: "Handle 'but' statements by separating the main claim from the objection, classifying the tension type, and routing to the right resolution skill."
output:
  format: "prose"
---

# BUT - Contrast and Objection Handler

**Input**: $ARGUMENTS

---

## Core Principles

1. **"But" is a signal, not a problem.** When someone says "X, but Y," they're surfacing a tension they've noticed. The tension is valuable information. Don't resolve it prematurely — classify it first.

2. **Six types of "but."** Not all "buts" are the same: exception, contradiction, risk, tradeoff, scope limit, and emotional resistance. Each needs different handling. Routing a tradeoff to truth-testing wastes time. Routing an emotion to logic makes it worse.

3. **Sometimes the "but" IS the point.** In "This plan is great, but it requires $2M we don't have," the main claim is setup. The "but" is what matters. Don't assume the first clause is always primary.

4. **Both sides can be true.** "We need to move fast, but we also need quality" is not a contradiction — it's a tension. Tensions need navigation, not resolution. Not everything resolves into one side winning.

5. **The hidden "but."** Sometimes the user's real objection isn't stated. "I think we should do X" (unstated: "but I'm worried about Y"). If the stated objection feels too mild for the user's energy, look for the hidden one.

---

## Phase 1: Extraction

```
[B1] RAW_STATEMENT: [the full "but" statement, quoted]
[B2] CLAIM_A: [the part before "but" — stated neutrally]
[B3] CLAIM_B: [the part after "but" — stated neutrally]
[B4] PRIMARY_WEIGHT: [A is primary | B is primary | equal weight]
```

### Primary Weight Test

Which clause carries more weight?
- If removing A leaves the statement intact → B is primary, A is setup
- If removing B leaves the statement intact → A is primary, B is qualifier
- If removing either changes meaning → equal weight (genuine tension)

---

## Phase 2: Tension Classification

```
[B5] TENSION_TYPE: [exception | contradiction | risk | tradeoff | scope_limit | emotional_resistance]
[B6] CLASSIFICATION_EVIDENCE: [what makes it this type]
```

| Type | Pattern | Example | Resolution Approach |
|------|---------|---------|-------------------|
| **Exception** | A is generally true, B is a case where it's not | "This works, but not for edge case X" | Scope A; handle exception |
| **Contradiction** | A and B can't both be true | "Revenue is up, but we're losing money" | Test which is accurate |
| **Risk** | A is the plan, B is what could go wrong | "Let's launch, but what if it crashes?" | Risk assessment |
| **Tradeoff** | A and B are both desirable but compete | "I want speed, but also quality" | Tradeoff navigation |
| **Scope limit** | A is true but only within bounds | "This applies, but only in our market" | Define scope explicitly |
| **Emotional resistance** | A is logical, B is a feeling | "I know I should, but I don't want to" | Acknowledge emotion; examine source |

---

## Phase 3: Hidden Objection Check

```
[B7] HIDDEN_OBJECTION_CHECK:
  ENERGY_MATCH: [does the stated objection match the user's energy? yes/no]
  POSSIBLE_HIDDEN: [what might the real objection be?]
  EVIDENCE: [why suspect a hidden objection]
```

If ENERGY_MATCH is no:
```
[B8] LIKELY_HIDDEN_OBJECTION: [what the user might actually be worried about]
[B9] SURFACE_QUESTION: [question to surface the real objection]
```

---

## Phase 4: Resolution Routing

Based on tension type, route to the appropriate skill:

| Tension Type | Route | Why |
|-------------|-------|-----|
| **Exception** | → `/exc` or direct handling | Scope the claim; handle the exception |
| **Contradiction** | → `/claim` $B1 | Test which claim is accurate |
| **Risk** | → `/fla` or `/prm` | Assess risk; plan mitigation |
| **Tradeoff** | → `/decide` or `/vcd` | Navigate the tradeoff with criteria |
| **Scope limit** | → `/dd` or direct scoping | Define the boundary explicitly |
| **Emotional resistance** | → `/emotion` $B1 | Acknowledge and examine the feeling |
| **Hidden objection** | → Surface first, then re-classify | Can't route until real objection is known |

```
[B10] RECOMMENDED_ROUTE: /skill-id — [why this skill resolves this tension type]
[B11] INVOCATION: /skill-id [specific arguments]
[B12] ALTERNATIVE: /skill-id — [if first choice doesn't resolve]
```

---

## Phase 5: Output

```
"BUT" ANALYSIS
==============

ORIGINAL: [quoted statement]

CLAIM A: [before "but"]
CLAIM B: [after "but"]
PRIMARY: [A | B | equal]

TENSION TYPE: [type]
EVIDENCE: [why this type]

HIDDEN OBJECTION: [none detected | possible hidden objection described]

RESOLUTION:
  APPROACH: [what to do with this tension]
  → INVOKE: /skill-id [specific invocation]
  WHY: [why this resolves the tension]

  IF BOTH TRUE (tension, not contradiction):
  NAVIGATE: [how to hold both without forcing resolution]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Type misclassification** | Tradeoff treated as contradiction | Check: can both be true simultaneously? If yes, not a contradiction |
| **A always treated as primary** | "But" clause dismissed as qualifier | Apply primary weight test — sometimes B is the point |
| **Premature resolution** | Tension resolved before classification | Classify first, resolve second |
| **Logic for emotion** | Emotional resistance addressed with reasoning | If tension type is emotional, route to `/emotion`, not `/claim` |
| **Hidden objection missed** | User's energy doesn't match stated objection | Apply energy match check |
| **False contradiction** | Both-true tension treated as one-must-be-wrong | Check for tradeoff or scope limit before assuming contradiction |

---

## Depth Scaling

| Depth | Classification Rigor | Hidden Objection Check | Resolution Alternatives |
|-------|---------------------|----------------------|----------------------|
| 1x | Type only | No | 1 route |
| 2x | Type + evidence | Energy match check | 2 routes |
| 4x | Type + evidence + test | Full hidden check + surfacing question | 3 routes with conditions |
| 8x | Type + evidence + test + reframe | Full check + both-true navigation | All applicable routes |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Both claims extracted and stated neutrally
- [ ] Primary weight assessed (not assumed A is primary)
- [ ] Tension type classified with evidence
- [ ] Hidden objection check performed (energy match)
- [ ] Routing matches tension type (not one-size-fits-all)
- [ ] If both-true: navigation approach provided (not forced resolution)
- [ ] Invocation includes specific arguments

---

## Integration

- Use from: natural language parsing of user statements
- Routes to: `/claim`, `/decide`, `/fla`, `/emotion`, `/vcd`, `/dd` depending on tension type
- Complementary: `/it` (processes "I think" part), `/nsa` (processes uncertainty)
- Differs from `/claim`: claim tests truth; but classifies tension type first
- Differs from `/decide`: decide handles decisions; but handles the broader category of tensions
