---
name: "auto - Automatic Routing"
description: "Take any free-text input, classify it, and route to the correct sub-orchestrator. The automatic front door to all 597 skills."
output:
  format: "prose"
---

# Auto - Automatic Routing

**Input**: $ARGUMENTS

---

## Core Principles

1. **The user should never need to know skill names.** This skill exists so that any natural-language input gets routed to the correct analytical procedure. The user says what they're thinking; the system figures out what to do with it.

2. **Classification happens BEFORE action.** Never start generating a response until you have classified the input. Wrong classification produces structured-but-irrelevant output, which is worse than no structure at all.

3. **Misrouting must be survivable.** Even if classification is wrong, the sub-orchestrator it routes to contains "Is this actually a [X]?" checks that can reroute. This is defense-in-depth, not an excuse for sloppy classification.

4. **When unsure, present interpretations rather than guess.** A confident wrong route wastes the user's time. An honest "I see 2-3 ways to read this" lets the user correct course immediately.

5. **The simplest correct route wins.** If the input clearly maps to one sub-orchestrator, route there directly. Do not over-analyze clear inputs.

---

## Phase 1: Coarse Classification

Read the input and classify it into exactly ONE of these 5 types:

| Type | Signal | The user is... |
|------|--------|----------------|
| **CLAIM** | States something as true, asks "is X true?", presents a belief, asserts a fact, tests a proposition | ...making or examining an assertion about reality |
| **DECISION** | Asks "should I?", compares options, faces a choice, asks "what should I do?", weighs alternatives | ...choosing between courses of action |
| **EXPLORATION** | Asks "what/how/why?", seeks to understand, wants to map a space, asks about causes, asks for methods | ...trying to understand something or find a path |
| **EMOTION** | Expresses frustration, anxiety, doubt, excitement, overwhelm, says "I feel", vents, expresses confusion | ...experiencing and expressing a feeling |
| **ACTION** | Says "do X", "write X", "build X", "evaluate X", asks for execution, wants output produced | ...requesting that something be done |

```
[A1] RAW_INPUT: [the user's input, quoted]
[A2] COARSE_TYPE: [CLAIM | DECISION | EXPLORATION | EMOTION | ACTION]
[A3] COARSE_EVIDENCE: [which signals from the table matched]
[A4] COARSE_CONFIDENCE: [high | medium | low]
```

### Rerouting Rules (apply in order, first match wins)

These override the initial coarse classification when surface form misleads:

| Input pattern | Looks like... | Actually is... | Why |
|---------------|---------------|----------------|-----|
| "Should I X?" | CLAIM | **DECISION** | "Should" signals a choice, not an assertion |
| "I want X" | ACTION | **EXPLORATION** | Wanting is a goal to clarify, not an action to execute |
| "How do I feel about X?" | EXPLORATION | **EMOTION** | Asking about feelings is emotional processing |
| "Is this any good?" | CLAIM | **ACTION** (evaluate) | Requesting quality assessment is evaluation, not truth-testing |
| "What should I do?" | EXPLORATION | **DECISION** | "What should" signals a choice point |
| "Fix this" / "Debug this" | ACTION | **EXPLORATION** (diagnose) | Fixing requires diagnosis before action |
| "I think X, but..." | CLAIM | **CLAIM** (with objection) | Confirmed CLAIM, but route to /but handling |
| "I'm not sure about X" | EMOTION | **CLAIM** (uncertain) | Uncertainty about a proposition is claim-testing, not emotion |
| "Handle this" / "Deal with this" | ACTION | **(reclassify)** | Maximally ambiguous; needs Phase 1 applied to the referent, not the wrapper |
| "Tell me about X" | EXPLORATION | **EXPLORATION** | Confirmed; route to /search or /technical |
| "Compare X and Y" | EXPLORATION | **DECISION** | Comparison implies choosing |
| "Why did X happen?" | EXPLORATION | **EXPLORATION** (diagnose) | Causal "why" about a failure is diagnosis |
| "I'm frustrated that X" | EMOTION | **EMOTION** | Confirmed; but the X may contain a hidden claim or decision to surface after processing |
| "Is X viable?" / "Could X work?" | CLAIM | **CLAIM** (viability) | Tests workability, not truth |

After applying rerouting rules:
```
[A5] REROUTE_APPLIED: [yes/no — which rule triggered]
[A6] FINAL_COARSE_TYPE: [the type after rerouting]
```

---

## Phase 2: Fine Routing

Based on the final coarse type, route to the specific sub-orchestrator:

### CLAIM routes:

| Sub-signal | Route to |
|------------|----------|
| Assertion of fact, "X is true", belief to test | → `/claim` |
| "Is X viable?", "Could X work?", "Is X feasible?" | → `/viability` |
| If input is actually a decision (caught in rerouting) | → `/decide` |

### DECISION routes:

| Sub-signal | Route to |
|------------|----------|
| "Should I X?", "X or Y?", comparing options, choosing | → `/decide` |
| If user wants maximum rigor on the decision | → `/certainty` |

### EXPLORATION routes:

| Sub-signal | Route to |
|------------|----------|
| "What are the options?", mapping a space, enumerating | → `/search` |
| "How do I X?", seeking a method, step-by-step | → `/how` |
| "I want X", stating a goal, desired outcome | → `/want` |
| "What's causing X?", "Why is X broken?", diagnosing | → `/diagnose` |
| Domain-specific technical question | → `/technical` |
| "What skills exist?", meta-question about the system | → `/meta` |
| Analyzing a complex system or problem | → `/analyze` |

### EMOTION routes:

| Sub-signal | Route to |
|------------|----------|
| Any expressed feeling: frustration, anxiety, doubt, excitement, overwhelm | → `/emotion` |

### ACTION routes:

| Sub-signal | Route to |
|------------|----------|
| "Do X", clear task to execute, next step needed | → `/action` |
| "Write X", "Create X", content to produce | → `/create` |
| "Is this good?", "Review this", quality assessment | → `/evaluate` |
| "What's next?", "What should I do next?" | → `/next` (if context is clear) or `/decide` (if context is unclear) |
| Iterating on existing work | → `/iterate` |

```
[A7] FINE_ROUTE: /[skill-name]
[A8] FINE_EVIDENCE: [what sub-signal matched]
[A9] FINE_CONFIDENCE: [high | medium | low]
```

---

## Phase 3: Confidence Check

### If COARSE_CONFIDENCE is high AND FINE_CONFIDENCE is high:

Route directly. No further analysis needed.

```
→ INVOKE: /[skill-name] $ARGUMENTS
```

### If either confidence is medium:

State the route and briefly note the alternative:

```
[A10] PRIMARY_ROUTE: /[skill-name] — [why this matches]
[A11] ALTERNATIVE_ROUTE: /[alt-skill-name] — [why this might also apply]
[A12] ROUTING_NOTE: [one sentence on why primary was chosen over alternative]
```

Then route to the primary:
```
→ INVOKE: /[skill-name] $ARGUMENTS
```

### If either confidence is low:

Present 2-3 interpretations to the user. Do NOT route automatically.

```
[A10] INTERPRETATION_1: "[restatement of input as Type A]"
  → Would route to: /skill-a
  → This interpretation means: [what the response would address]

[A11] INTERPRETATION_2: "[restatement of input as Type B]"
  → Would route to: /skill-b
  → This interpretation means: [what the response would address]

[A12] INTERPRETATION_3 (if applicable): "[restatement of input as Type C]"
  → Would route to: /skill-c
  → This interpretation means: [what the response would address]

Which interpretation matches what you meant? (Or say more and I'll re-classify.)
```

Wait for user response. Then re-enter Phase 1 with the clarified input.

---

## Phase 4: Post-Route Verification

After invoking the sub-orchestrator, verify the route was correct by checking:

```
[A13] OUTPUT_TYPE_MATCH: [does the sub-orchestrator's output type match what the user wanted?]
  - User wanted an answer → did the skill produce an answer (not just a process)?
  - User wanted a decision → did the skill produce a recommendation (not just analysis)?
  - User wanted action → did the skill produce concrete steps (not just exploration)?
  - User wanted emotional support → did the skill acknowledge the feeling (not just analyze it)?
```

If OUTPUT_TYPE_MATCH is false, note the mismatch for future routing improvement but do NOT interrupt the user's flow.

---

## Edge Cases

### Compound inputs (multiple types in one message)

If the input contains multiple types ("I'm frustrated about X and I need to decide whether to Y"):
1. Identify the DOMINANT type (usually the one stated first or with the most emotional weight)
2. Route to the dominant type's sub-orchestrator
3. Note the secondary type for the sub-orchestrator to surface after handling the primary

```
[A14] COMPOUND: yes
[A15] DOMINANT_TYPE: [type] → /[skill]
[A16] SECONDARY_TYPE: [type] — surface after primary is handled
```

### Meta-inputs (about the routing itself)

If the user asks "What would you do with this?" or "How would you classify this?":
→ INVOKE: /meta $ARGUMENTS

### Empty or trivial inputs

If the input is too short or vague to classify ("help", "hi", "?"):
```
What are you working on? I can help with:
- Testing a claim or belief
- Making a decision
- Exploring a question or topic
- Processing a feeling
- Getting something done

Say what's on your mind and I'll route to the right analytical tool.
```

### Inputs that don't fit any category

If the input genuinely does not fit (jokes, greetings, translation requests, simple factual lookups):
- Respond naturally without routing to a skill
- Mention that analytical skills are available if they have a deeper question

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Routing collapse** | >60% of inputs go to 2-3 categories | Check rerouting rules; underused categories may need better trigger descriptions |
| **False confidence** | Routes confidently to the wrong skill; structured but irrelevant output | Apply the post-route verification check (Phase 4) |
| **Over-classification** | Simple inputs get elaborate classification analysis | If input is clear, skip to the route. Classification analysis is internal, not output |
| **Rerouting loops** | Input bounces between sub-orchestrators ("Is this a claim?" → "Is this a decision?" → ...) | First reroute wins. If the sub-orchestrator reroutes, follow it once. No second reroute |
| **Compound paralysis** | Multi-type input leads to analysis of the types instead of addressing the content | Pick the dominant type and go. The sub-orchestrator handles the nuance |
| **Ignoring emotion** | Emotional input classified as CLAIM or EXPLORATION because it contains a proposition | If the input EXPRESSES a feeling, it is EMOTION. If it DESCRIBES a feeling analytically, it is CLAIM |

---

## Depth Scaling

| Depth | Classification Rigor | Confidence Threshold |
|-------|---------------------|---------------------|
| 1x | Coarse type only, route immediately | Route if any signal matches |
| 2x | Coarse + fine + rerouting check | Route if medium+ confidence |
| 4x | Full classification + alternative noted | Route if high confidence; present alternatives if medium |
| 8x | Full classification + all interpretations explored | Present interpretations even at medium confidence |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Input read and coarse type identified
- [ ] Rerouting rules applied (first match wins)
- [ ] Fine route selected with evidence
- [ ] Confidence assessed for both coarse and fine
- [ ] If low confidence: interpretations presented instead of auto-routing
- [ ] If compound input: dominant type identified, secondary noted
- [ ] Sub-orchestrator invoked with full original input as arguments
- [ ] Post-route verification noted (does output type match user want?)

---

## Integration

- **Use from**: This is the entry point. Users invoke `/auto` when they don't know which skill to use, or it can be the default handler for all input.
- **Routes to**: Any of the 15 sub-orchestrators: `/claim`, `/viability`, `/decide`, `/search`, `/how`, `/want`, `/diagnose`, `/technical`, `/meta`, `/analyze`, `/emotion`, `/action`, `/create`, `/evaluate`, `/iterate`, `/next`, `/certainty`
- **Differs from `/handle`**: `/handle` assumes the input is "handle this" — maximally vague delegation. `/auto` handles ANY input, including clear and specific inputs that just need routing.
- **Differs from `/wsib`**: `/wsib` recommends a skill for the user to invoke. `/auto` classifies and invokes directly.
- **Differs from `/meta`**: `/meta` provides orientation about the skill system. `/auto` uses the skill system on behalf of the user.
- **Complementary**: `/fonss` (find optimal next skill in sequence), `/dtse` (determine task-skill equivalence)
