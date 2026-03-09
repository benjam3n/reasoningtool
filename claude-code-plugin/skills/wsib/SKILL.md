---
name: "wsib - What Skill Is Best"
description: "Choose the single best skill to run RIGHT NOW for a prompt, with confidence calibration, runner-up comparison, and fallback if first choice fails."
---

# WSIB - What Skill Is Best

**Input**: $ARGUMENTS

---

## Core Principles

1. **Best means best NOW, not best in general.** The right skill depends on current state — what's already been done, what's blocked, what the user knows. A skill that's perfect for step 3 is wrong if you're at step 1.

2. **Intent over keywords.** "I'm stuck" might need `/diagnose`, `/sbfow`, `/how`, or `/emotion` depending on what kind of stuck. Match the underlying need, not the surface words.

3. **One skill, not a workflow.** WSIB picks ONE skill. If the user needs a sequence, route to `/fonss`. The temptation to recommend three skills "just in case" dilutes the recommendation.

4. **Confidence must be calibrated.** HIGH means "this is clearly the right skill and alternatives are substantially worse." MEDIUM means "this fits but a close competitor exists." LOW means "best guess but the intent is ambiguous." Don't default to HIGH.

5. **The runner-up is diagnostic.** If the runner-up is from a completely different category than the best, the intent is probably ambiguous and you should say so. If runner-up is in the same category, your pick is probably right.

6. **Fallback is not second-best.** The fallback is what to run IF the best skill fails or produces weak output. It's a recovery route, not a preference ordering.

---

## Phase 1: Intent Extraction

Parse the prompt into structured intent:

```
[W1] SURFACE_REQUEST: [what the user literally said]
[W2] INTENT_TYPE: [goal | problem | question | decision | feeling | task | content | claim]
[W3] SPECIFICITY: [vague | moderate | specific]
[W4] URGENCY: [exploring | planning | ready-to-act | stuck | frustrated]
[W5] PRIOR_STATE: [fresh start | mid-process | iteration | recovery]
[W6] IMPLICIT_NEED: [what they probably also need but didn't say]
```

### Intent Classification Table

| If intent looks like... | Primary category | Check also |
|------------------------|-----------------|------------|
| "I want X" / "I need X" | Goal → `/want` | `/gu` if goal is vague |
| "How do I X?" | Method → `/how` | `/foht` if specific |
| "Should I X or Y?" | Decision → `/decide` | `/dcp` if binary |
| "What's wrong with X?" | Diagnostic → `/diagnose` | `/sbfow` if prior attempt failed |
| "I think X" | Claim → `/claim` | `/it` to decompose first |
| "Help me write/create X" | Content → `/create` | `/w` or `/wre` for writing |
| "I feel X" / "I'm frustrated" | Emotion → `/emotion` | `/cfr` for conflict |
| "Do X" / "Execute X" | Action → `/action` | `/handle` if vague |
| "Explore X" / "What about X?" | Search → `/search` | `/poa` for options |
| "Is X true?" / "Check X" | Validation → `/claim` | `/ver` for verification |
| "What should I do next?" | Sequence → `/next` | `/fonss` for multi-step |
| "Make this better" | Iteration → `/iterate` | `/evaluate` first |

---

## Phase 2: Candidate Generation

Generate top 3-5 candidate skills. For each:

```
[W7] CANDIDATE: /skill-id — FIT: [why it matches the intent] — WEAKNESS: [what it doesn't cover]
[W8] CANDIDATE: /skill-id — FIT: [why] — WEAKNESS: [what]
[W9] CANDIDATE: /skill-id — FIT: [why] — WEAKNESS: [what]
```

### Selection Criteria

Score each candidate on:

| Criterion | Question | Weight |
|-----------|----------|--------|
| **Intent match** | Does this skill address the core intent? | 3x |
| **State fit** | Is this the right skill for WHERE the user is? | 2x |
| **Completeness** | Will this skill resolve the need, or just start it? | 1x |
| **Specificity match** | Does the skill's scope match the request's specificity? | 1x |

---

## Phase 3: Selection

```
[W10] BEST_NOW: /skill-id
[W11] CONFIDENCE: HIGH | MEDIUM | LOW
[W12] WHY_BEST: [one sentence — what makes this better than alternatives]
[W13] RUNNER_UP: /skill-id
[W14] WHY_NOT_RUNNER_UP: [one sentence — what specifically makes it second]
[W15] RUNNER_UP_DISTANCE: [CLOSE | MODERATE | FAR]
[W16] FALLBACK_IF_FAILS: /skill-id
[W17] FALLBACK_TRIGGER: [what would indicate the best skill failed]
```

### Confidence Calibration

| Confidence | Condition |
|------------|-----------|
| **HIGH** | Intent is clear, best skill is purpose-built for this, runner-up is FAR |
| **MEDIUM** | Intent is clear but 2+ skills fit well, or intent is slightly ambiguous |
| **LOW** | Intent is ambiguous, OR the best skill is a general router not a specific tool |

If CONFIDENCE is LOW, add:
```
[W18] AMBIGUITY: [what's ambiguous about the intent]
[W19] CLARIFYING_QUESTION: [what would resolve the ambiguity]
```

---

## Phase 4: Output

```
BEST_NOW: /skill-id
CONFIDENCE: HIGH | MEDIUM | LOW
WHY_BEST: [one sentence]
WHY_NOT_RUNNER_UP: [one sentence]
RUNNER_UP: /skill-id
RUNNER_UP_DISTANCE: CLOSE | MODERATE | FAR
FALLBACK_IF_FAILS: /skill-id
FALLBACK_TRIGGER: [when to switch]

→ INVOKE: /skill-id $ARGUMENTS
```

If CONFIDENCE is LOW, output the clarifying question INSTEAD of invoking.

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Router recursion** | BEST_NOW is another router (`/meta`, `/handle`) | Routers route to routers = lost. Pick the concrete skill the router would pick. |
| **Keyword matching** | "decision" → `/decide` without checking if it's actually a decision | Test against intent classification table, not just keywords |
| **Default to category** | Always picks `/want` or `/how` because they're broad | Category skills are for ambiguous inputs. If intent is clear, pick the specific skill. |
| **Overconfident HIGH** | Everything marked HIGH confidence | If runner-up distance is CLOSE, confidence can't be HIGH |
| **Missing state context** | Recommends `/gu` when user already understands their goal | Check PRIOR_STATE — mid-process users need different skills than fresh-start users |
| **Workflow in disguise** | Returns one skill but the user clearly needs a chain | If the need is sequential, say so and route to `/fonss` |

---

## Depth Scaling

| Depth | Candidates Generated | Selection Criteria Scored | Disambiguation |
|-------|---------------------|--------------------------|---------------|
| 1x | 3 | Intent match only | None |
| 2x | 5 | All 4 criteria | Clarifying question if LOW |
| 4x | 7 | All 4 + interaction check | Full ambiguity analysis |
| 8x | 10 | All 4 + prior-state deep check | Multi-path recommendation |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Intent extracted (not just keywords matched)
- [ ] Prior state considered (fresh start vs mid-process vs recovery)
- [ ] At least 3 candidates generated with fit AND weakness noted
- [ ] BEST_NOW selected with explicit reason it beats runner-up
- [ ] Confidence calibrated (not defaulting to HIGH)
- [ ] Fallback is a recovery route, not just second-best
- [ ] If LOW confidence: clarifying question provided instead of blind invocation
- [ ] Result is ONE skill, not a workflow (if workflow needed, route to `/fonss`)

---

## Integration

- Use from: `/meta`, `/handle`, `/next`
- Differs from `/extract`: extract finds ALL relevant skills; wsib picks the ONE best
- Differs from `/fonss`: fonss sequences multiple skills; wsib picks one
- Differs from `/given`: given ranks by ROI for a goal; wsib matches by intent fit
- Differs from `/fnd`: fnd is a registry lookup; wsib does intent analysis first
- Routes to: whatever skill is selected
