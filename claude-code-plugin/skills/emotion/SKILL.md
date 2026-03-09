---
name: "emotion - Process a Feeling"
description: Sub-orchestrator for emotional inputs. Acknowledges the emotion, identifies the implicit request, and routes to the appropriate analytical skill — with expanded routing for reframing, scope control, and self-check skills.
---

# Emotion

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Frustration/anger**: Something is broken or not working and the user is emotionally invested in it.
**Interpretation 2 — Overwhelm**: The user feels overloaded, scattered, or unable to start.
**Interpretation 3 — Stuck**: The user has been trying but can't make progress.
**Interpretation 4 — Doubt/insecurity**: The user questions their own capability or worth.
**Interpretation 5 — Excitement**: The user has energy around an idea and wants to channel it.
**Interpretation 6 — Anxiety/fear**: The user is worried about what might go wrong.
**Interpretation 7 — Burnout/exhaustion**: The user has been pushing too hard and is running out of energy.

If ambiguous, ask: "What's the strongest feeling right now?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Acknowledge first, route second.** Never skip straight to analysis. Brief, genuine acknowledgment — one or two sentences. Not performative. Then transition to the implicit request.

2. **Emotions carry information.** Frustration means something is broken. Overwhelm means something is too complex. Stuck means the approach isn't working. Doubt means a belief needs testing. Excitement means an idea needs testing. Anxiety means risks need mapping.

3. **Don't fix the emotion — address the cause.** The goal is not to make the user feel better. The goal is to help them with the thing that's causing the feeling.

4. **Self-directed emotions need special handling.** "I'm not good enough" is a testable claim. "I can't do this" is a capability assessment. These need /claim, not comfort.

---

## Routing Decisions

### 1. Identify the Emotion

| Emotion | Signals |
|---------|---------|
| **Frustration** | "Nothing works", "I've tried everything", "this is broken" |
| **Overwhelm** | "I don't know where to start", "too much", "everything at once" |
| **Stuck** | "I'm stuck", "can't figure this out", "hit a wall" |
| **Doubt** | "I don't think I can", "maybe I should give up", "is this even worth it" |
| **Excitement** | "I have this great idea!", "what if we...", "I just realized..." |
| **Anxiety** | "What if it fails?", "I'm worried about...", "this could go wrong" |
| **Burnout** | "I'm exhausted", "I can't keep doing this", "what's the point" |
| **Confusion** | "I don't understand", "this makes no sense", "I'm lost" |

### 2. Acknowledge First

**Always acknowledge the emotion before routing.** Never skip straight to analysis.

Brief, genuine acknowledgment — one or two sentences. Not performative. Then transition to the implicit request.

### 3. What's the Implicit Request?

The emotion points to a need. Identify it:

| Emotion | Usually means | Primary route | Alternative routes |
|---------|--------------|---------------|-------------------|
| **Frustration** | Something's broken, need to find why | → /diagnose | → /sid (wrong problem?), /rmm (wrong model?) |
| **Overwhelm** | Too complex, need to break it down | → /how with /dcm | → /iagca (compress scope), /ezy (easy mode), /awtlytrn (find limits) |
| **Stuck** | Need a new approach | → /how (find methods) | → /iaw (reframe), /rmm (wrong mental model), /kta (knowledge-to-action) |
| **Doubt** | Questioning a belief about themselves | → /claim "I can't do X" | → /sdc (self-deception check), /obv (obvious check) |
| **Excitement** | Have an idea, want to test it | → /viability | → /ycshikfmif (structure the expansion), /iagca (if getting carried away) |
| **Anxiety** | Worried about failure | → /evaluate with risk focus | → /fla, /prm, /obo, /saf, /dys (specific risk tools) |
| **Burnout** | Need to reassess scope and priorities | → /want (what do they actually want?) | → /ecal (effort calibration), /awtlytrn (find limits) |
| **Confusion** | Need clarity on the situation | → /sid (identify the situation) | → /ezy (easy mode), /obv (check the obvious) |

### 4. Is the Emotion About the Problem, Themselves, or the Process?

- **About the problem** ("This is broken", "It's not working"): diagnostic need.
  → INVOKE: /diagnose $ARGUMENTS
- **About themselves** ("I'm not good enough", "I can't do this"): this is a claim about their capability — test it.
  → INVOKE: /claim [the self-doubt as a testable proposition]
  Also consider: → INVOKE: /want $ARGUMENTS — what do they actually want underneath the doubt?
- **About the process** ("This is taking too long", "This approach isn't working"): evaluation need.
  → INVOKE: /evaluate [the process/approach]
  Also consider: → INVOKE: /iaw [reframe the approach]
- **About the scope** ("There's too much", "I'm getting carried away"): scope control need.
  → INVOKE: /iagca $ARGUMENTS — compress scope back to essentials.
- **About the future** ("What if this fails?", "I'm worried about the outcome"): risk need.
  → INVOKE: /fla or /obo $ARGUMENTS — map the specific risks.
  → INVOKE: /gop $ARGUMENTS — also map what good outcomes are possible.

### 5. Deeper Emotional Routing

Some emotional states benefit from specific newer skills:

| Situation | Invoke |
|-----------|--------|
| User feels wrong mental model is the problem | → /rmm (recover from wrong mental model) |
| User has knowledge but can't act on it | → /kta (knowledge to action) |
| User needs to see the worst case to stop worrying | → /dys (dystopia analysis) |
| User needs to see the best case to get motivated | → /utp (utopia analysis) |
| User wants to trace why they feel this way | → /sycs (so you can see — trace implications) |
| User's emotion is based on vague wisdom | → /platitude (operationalize the belief) |
| User says "I think..." about their situation | → /it (formalize the belief) |
| User says "X, but Y" about their situation | → /but (resolve the tension) |
| User says "I'm not sure about..." | → /nsa (classify the uncertainty) |
| User is overwhelmed by options | → /dom (eliminate dominated options) + /ro (reorder remainder) |
| User needs a story/narrative to make sense of it | → /story |

---

## Execute

1. Acknowledge the emotion (1-2 sentences).
2. State the implicit request you've identified.
3. Invoke the appropriate skill:

**Frustration:**
→ INVOKE: /diagnose $ARGUMENTS

**Overwhelm:**
→ INVOKE: /how $ARGUMENTS — with a focus on decomposition (/dcm)
→ If scope is the issue: INVOKE: /iagca $ARGUMENTS
→ If complexity is the issue: INVOKE: /ezy $ARGUMENTS

**Stuck:**
→ INVOKE: /how $ARGUMENTS — with a focus on finding new approaches (/foht)
→ If the framing might be wrong: INVOKE: /iaw $ARGUMENTS
→ If the mental model might be wrong: INVOKE: /rmm $ARGUMENTS

**Doubt:**
→ INVOKE: /claim [the doubt stated as a testable proposition]
→ If self-deception is possible: INVOKE: /sdc $ARGUMENTS

**Excitement:**
→ INVOKE: /viability $ARGUMENTS
→ If scope is expanding wildly: INVOKE: /ycshikfmif or /iagca

**Anxiety:**
→ INVOKE: /evaluate $ARGUMENTS — with risk focus
→ INVOKE: /obo $ARGUMENTS — check for obvious bad outcomes
→ Also consider: /gop to balance with good outcomes

**Burnout:**
→ INVOKE: /want $ARGUMENTS — reconnect with the actual want
→ INVOKE: /ecal $ARGUMENTS — calibrate effort to match stakes
→ INVOKE: /awtlytrn $ARGUMENTS — estimate actual limits

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Skipping acknowledgment** | Jumped straight to analysis | Always acknowledge first — even one sentence |
| **Emotional bypass** | "Let's focus on the facts" when the emotion IS the signal | The emotion carries information — use it as a routing signal |
| **Toxic positivity** | "It'll be fine!" without addressing the cause | Don't fix the feeling — address the cause |
| **Wrong routing** | User is anxious but got diagnostic instead of risk assessment | Re-read — anxiety means map risks, not find causes |
| **Self-doubt as fact** | Accepted "I can't do this" instead of testing it | Self-doubt is a claim — test it with /claim |

---

## After Completion

Report:
- The emotion acknowledged
- The implicit need identified
- Results from the routed skill
- Suggested next step

### Follow-Up Routing

After the emotion is processed and the routed skill completes:
- **"What should I do?"** → INVOKE: /action or /how
- **"What's the next step?"** → INVOKE: /next
- **"I'm still stuck"** → Try a different approach: /iaw, /rmm, or /kta
- **"What skills should I run?"** → INVOKE: /fonss or /wsib
- **"I'm getting carried away"** → INVOKE: /iagca

---

## Integration

- **Use from**: Any router (when the user's input has emotional content alongside their request)
- **Routes to**: /diagnose (frustration), /how (overwhelm/stuck), /claim (doubt), /viability (excitement), /evaluate (anxiety), /want (burnout), /iagca (scope overwhelm), /kta (knowledge-action gap)
- **Differs from**: /want (emotion processes feeling to find the need, want starts from a stated goal), /diagnose (emotion processes the person's state, diagnose processes the problem's state)
- **Complementary**: /sdc (self-deception check for doubt), /rmm (wrong mental model for stuck), /iaw (reframing for stuck), /obo (concrete risk mapping for anxiety)
