---
name: "certainty - Maximum Effort Resolution"
description: Continues analysis until the answer is thoroughly resolved. Chains multiple skills iteratively, escalating depth until no unresolved branches, untested assumptions, or competing conclusions remain.
output:
  format: "prose"
---

# Certainty

**Input**: $ARGUMENTS

---

## Core Principle

**Do not stop until the answer is thoroughly satisfying.** This skill runs at maximum depth, chains across multiple skills, evaluates its own output between iterations, and continues until resolution criteria are met. It is the "give me everything you've got" mode.

---

## Phase 1: Classify and Set Resolution Criteria

### 1. What Is the Question?

Extract the core question to resolve. State it precisely.

### 2. What Does "Resolved" Mean?

Define what a satisfying answer looks like:

- **Factual question**: answer is verified, sourced, and no credible counter-evidence remains.
- **Analytical question**: all major branches explored, each tested with AR/AW, synthesis accounts for all findings.
- **Decision question**: clear recommendation with justified confidence, alternatives considered and rejected for stated reasons, risks identified.
- **Problem question**: root cause confirmed, prevention derived, no competing explanations unaddressed.

If the user didn't specify, ask: "What would make the answer satisfying to you?" If unclear, default to: **no remaining unresolved branches, untested assumptions, or competing conclusions.**

### 3. Classify the Input

Use the taxonomy to determine starting mode:

| If the question is... | Start with |
|----------------------|------------|
| A claim to test | → /claim at 8x |
| A decision to make | → /decide at 8x |
| A diagnostic question | → /diagnose at 8x |
| An exploration | → /search at 8x |
| A method question | → /how at 8x |
| A goal to clarify | → /want at 8x |
| An idea to test | → /viability at 8x |
| Something to evaluate | → /evaluate at 8x |
| An emotional input | → /emotion at 8x (will route to appropriate analysis) |
| A technical/domain question | → /technical at 8x |
| Content to produce | → /create at 8x (with full analytical foundation) |
| A problem to analyze | → /analyze at 8x |

### 4. Enhanced Classification Signals

Some input patterns route to newer skills before the main analysis:

| Input pattern | Pre-route to | Then |
|--------------|-------------|------|
| "I think X" (tentative) | → /it (formalize) | then main skill at 8x |
| "X, but Y" (tension) | → /but (separate) | then main skill at 8x on each part |
| "I'm not sure about X" | → /nsa (classify uncertainty) | then main skill at 8x on the classified question |
| Platitude-shaped input | → /platitude (operationalize) | then main skill at 8x on the operationalized version |

---

## Phase 2: Iterative Resolution

### Iteration Loop

```
ITERATION 1:
  1. Run the starting category skill at 8x depth.
  2. Collect all findings.
  3. Self-evaluate: → INVOKE /evaluate on own output.
     - Are there unresolved branches? → explore them.
     - Are there untested assumptions? → test them with /claim.
     - Are there competing conclusions? → stress-test each with /araw.
     - Are there gaps in the space? → fill with /search.
     - Are there obvious things missed? → check with /obv.
     - Are there obvious bad outcomes ignored? → check with /obo.
     - Is self-deception present? → check with /sdc.
     - Are there ethical dimensions unaddressed? → check with /eth.
     - Are there safety concerns unaddressed? → check with /saf.
  4. If unresolved items found → continue to Iteration 2.
     If resolved → proceed to Final Synthesis.

ITERATION 2:
  1. Address each unresolved item from Iteration 1.
     - Unresolved branch → /search or /claim on that branch.
     - Untested assumption → /claim [assumption].
     - Competing conclusions → /claim [conclusion A] then /claim [conclusion B].
     - Gap → /search [gap area].
  2. Collect new findings.
  3. Self-evaluate again.
  4. If unresolved items found → continue to Iteration 3.
     If resolved → proceed to Final Synthesis.

ITERATION 3+:
  Continue the pattern. Each iteration should have FEWER unresolved items.
  If an iteration produces no new findings or progress, that's the natural stopping point.
```

### Stopping Conditions

Stop when ANY of these is true:
- **No unresolved branches remain** — every significant avenue has been explored.
- **No untested assumptions remain** — every load-bearing assumption has been AR/AW tested.
- **No competing conclusions remain** — contradictions have been resolved.
- **Diminishing returns** — an iteration produced no new substantive findings.
- **Natural bedrock** — the analysis reached fundamental axioms or empirical facts that can't be broken down further.

### Anti-Stopping Conditions

Do NOT stop if:
- There are branches marked "uncertain" or "needs investigation."
- Two conclusions contradict each other and neither has been eliminated.
- Key assumptions are marked "unknown" status.
- The user's resolution criteria haven't been met.

---

## Phase 3: Final Synthesis

After all iterations:

```
CERTAINTY RESOLUTION:

QUESTION: [the original question]
RESOLUTION CRITERIA: [what "resolved" means]

ITERATIONS COMPLETED: [N]
TOTAL FINDINGS: [N across all iterations]

ANSWER:
[The thoroughly resolved answer — comprehensive, backed by findings from all iterations]

CONFIDENCE: [high / medium with stated reason]

KEY EVIDENCE:
1. [Most important finding supporting the answer]
2. [Second most important]
3. [Third most important]

WHAT WAS TESTED AND SURVIVED:
- [Claim/assumption that was AR/AW tested and held]
- [Claim/assumption that was AR/AW tested and held]

WHAT WAS TESTED AND ELIMINATED:
- [Claim/assumption that was tested and failed]
- [Claim/assumption that was tested and failed]

REMAINING UNCERTAINTY:
- [Anything that couldn't be fully resolved, with explanation of why]

WHAT WOULD CHANGE THIS ANSWER:
- [New evidence or conditions that would alter the conclusion]
```

---

## Phase 4: Extended Analysis Tools

During any iteration, draw on these skills when they would resolve open questions:

| Situation | Invoke |
|-----------|--------|
| Need to trace implications | → /sycs (so you can see) |
| Need future projections | → /fut (future analysis) |
| Need best-case scenario | → /utp (utopia analysis) |
| Need worst-case scenario | → /dys (dystopia analysis) |
| Need good outcome identification | → /gop |
| Need to differentiate between options | → /difr |
| Need to extract general principles | → /genl |
| Need to apply principle to specific case | → /spcf |
| Need sophisticated multi-layer analysis | → /soph |
| Need argument structure analysis | → /agsk |
| Need debate format | → /deb |
| Need narrative framing | → /story |
| Need to surface hidden assumptions | → /aex |
| Need A/B test design for empirical claims | → /abts |
| Need to reframe the question | → /iaw |
| Unresolved sub-decisions identified | → /tbd + /tobd |
| Need to check situation identification | → /sid |
| Need to check mental model | → /rmm |

---

## Depth

This skill always runs at maximum depth. There is no 1x/2x mode for /certainty. If you want lighter analysis, use the specific category skill directly.

---

## After Completion

### Follow-Up Routing

After certainty resolution, the user may need:
- **"What should I do?"** → INVOKE: /action or /how
- **"What are the implications?"** → INVOKE: /sycs
- **"What skill should I run next?"** → INVOKE: /next or /fonss
- **"What's still unresolved?"** → INVOKE: /tbd
- **"Iterate on this"** → INVOKE: /iterate

---

## Integration

- **Use from**: Any router (when the user asks for maximum effort), /ecal (when effort calibration says maximum depth warranted)
- **Routes to**: All category skills at 8x, plus extended analysis tools listed in Phase 4
- **Differs from**: Individual category skills (certainty chains across multiple skills iteratively; category skills run once), /iterate (certainty resolves a question to completion; iterate improves an existing output)
- **Complementary**: /ecal (determine whether certainty is warranted), /evaluate (used within certainty for self-evaluation between iterations)
