---
name: "empth - Empathic Thinking"
description: Systematically see from another person's perspective — not just "what would they feel" but "what do they see, believe, value, fear, and want given THEIR context and history?" Empathy as an analytical skill, not just a feeling.
output:
  format: "prose"
---

# EMPTH - Empathic Thinking

**Input**: $ARGUMENTS

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Person understanding**: The user wants to deeply understand a specific person's perspective — what that person sees, believes, values, fears, and wants — to navigate a relationship, conversation, or decision.
**Interpretation 2 — Reaction prediction**: The user wants to predict how a specific person or group will react to a message, decision, or change — not what "people in general" would think, but what THIS person would think given THEIR context.
**Interpretation 3 — Perspective gap diagnosis**: The user senses a disconnect with someone and wants to understand WHERE the gap is — what the other person sees that they don't, or what they see that the other person doesn't.

If ambiguous, ask: "I can help with understanding someone's full perspective, predicting how they'll react to something specific, or diagnosing where a perspective gap lives — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Corruption Pre-Inoculation

**Projection is the default failure mode.** If your empathic model sounds like what YOU would think in their position, you are projecting, not empathizing. The whole point is to construct a model that is NOT you. If the perspective model agrees with the user on everything, you are flattering, not analyzing.

> Full protocol: `_shared/corruption-pre-inoculation.md`

---

## Core Principles

1. **Context is everything.** The same event means different things to different people because they have different histories, beliefs, incentives, and information. "How would I feel?" is NOT empathy. "What do THEY see, given what THEY know and have experienced?" — that's empathy.

2. **People are locally rational.** Almost everyone's behavior makes sense from inside their own model of the world. If someone's actions seem irrational, you haven't understood their model yet. Find the model where their behavior is the best available move.

3. **Beliefs are upstream of emotions.** People don't just "feel" things arbitrarily. Feelings follow from beliefs about what is true, what matters, and what is at stake. Map the beliefs to understand the emotions. Change the beliefs to change the emotions.

4. **Identity is the third rail.** When something threatens a person's identity — their sense of who they are, what they're good at, what group they belong to — rational processing shuts down and defensive processing takes over. Always check whether an identity threat is in play.

5. **Stated reasons are often not real reasons.** People give socially acceptable explanations for positions driven by fear, status, loyalty, or identity. The empathic model must include what they WON'T say, not just what they will.

6. **Asymmetric information creates asymmetric reality.** Two people in the same situation can see completely different things because they have access to different information. Map what each person knows and doesn't know.

---

## Phase 1: CONTEXT RECONSTRUCTION

Build the world as the other person sees it. You are constructing THEIR reality, not yours.

### Step 1: Identify the Person and Situation

```
PERSON: [who — name, role, relationship to user]
SITUATION: [what is happening from a neutral standpoint]
USER'S VIEW: [how the user sees it — brief]
```

### Step 2: Map Their Context

For the target person, reconstruct:

```
INFORMATION ACCESS:
- What they know: [facts available to them]
- What they don't know: [facts they lack that the user has]
- What they believe that may be wrong: [beliefs not grounded in evidence]
- What they know that the user doesn't: [their unique information]

HISTORY & EXPERIENCE:
- Relevant past experiences: [events that shape how they interpret this]
- Pattern matches they're likely making: [what does this remind them of?]
- Scars and sensitivities: [past hurts that get activated here]

BELIEFS & VALUES:
- What they believe is true about this situation: [their mental model]
- What they believe is important: [their values hierarchy]
- What they believe about themselves: [identity claims]
- What they believe about the user: [perception of the other party]

INCENTIVES & CONSTRAINTS:
- What they want (stated): [expressed desires]
- What they want (unstated): [underlying needs — safety, status, belonging, autonomy]
- What they fear: [threats they perceive]
- What they're constrained by: [obligations, loyalties, dependencies]
```

### Step 3: Construct Their Internal Narrative

Write 2-4 sentences AS them (first person), expressing how they see the situation. This is not what they would SAY — it is what they would THINK if they were being completely honest with themselves.

```
THEIR INTERNAL NARRATIVE:
"[First-person narrative expressing their honest view]"
```

---

## Phase 2: PERSPECTIVE ANALYSIS

### Step 4: Find the Divergence Points

Where does the other person's view diverge from the user's? Label each:

```
DIVERGENCE MAP
==============

[D1] [topic/claim] — DIVERGENCE TYPE: [see below]
  User sees: [X]
  They see: [Y]
  Gap caused by: [different information / different values / different experience / identity threat]

[D2] [topic/claim] — DIVERGENCE TYPE: [see below]
  ...
```

**Divergence types:**
- **INFORMATION**: They have different facts. Resolvable by sharing information.
- **INTERPRETATION**: Same facts, different meaning. Harder — rooted in different frameworks.
- **VALUES**: Different priorities. Not "wrong" — genuinely different about what matters.
- **IDENTITY**: Position is tied to who they are. Extremely hard to move.
- **INTEREST**: Different outcomes benefit them. Structural, not personal.

### Step 5: Test the Model

For each divergence point, ask:
- Would this person recognize my description of their view? (If not, the model is wrong.)
- Does this model explain their BEHAVIOR, not just their words?
- Is there a simpler explanation I'm missing?
- Am I projecting my own framework onto them?

Mark each divergence:
- **CONFIDENT**: Strong evidence for this model
- **PLAUSIBLE**: Reasonable inference but could be wrong
- **SPECULATIVE**: Possible but needs verification

---

## Phase 3: SYNTHESIS

### Step 6: Compile the Empathic Model

```
EMPATHIC MODEL: [Person]
=====================

THEIR WORLD: [2-3 sentences — what does reality look like from inside their head?]

KEY DIVERGENCES FROM USER:
1. [D-number]: [brief — what they see differently and why]
2. [D-number]: [brief]
3. [D-number]: [brief]

WHAT THEY NEED (that they may not say):
- [need — derived from context, not assumed]
- [need]

WHAT WOULD MAKE THEM FEEL HEARD:
- [specific — not generic "active listening"]

WHAT WOULD MAKE THEM DEFENSIVE:
- [specific trigger — tied to identity or fear]

PREDICTION: If [user's planned action], they will likely [reaction], because [derived from model with D-number reference].

MODEL CONFIDENCE: [HIGH / MEDIUM / LOW]
WEAKEST ASSUMPTION: [the part of this model most likely to be wrong]
WHAT WOULD DISPROVE THIS MODEL: [observable thing that would mean you got it wrong]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Projection** | The empathic model sounds like what you would think | Rebuild from THEIR context. Ask: what experiences have THEY had that I haven't? |
| **Sympathy instead of empathy** | "They must feel so bad" without WHY | Map beliefs and values first. Emotions follow from beliefs. |
| **Flattening** | Person is modeled as one-dimensional (angry, jealous, scared) | People hold contradictory feelings. Add complexity until the model feels real. |
| **Assuming irrationality** | "They're just being irrational" | Find the model where they're locally rational. You haven't found it yet. |
| **Stated-reason acceptance** | Taking their words at face value | Ask: what would they NOT say? What's the socially unacceptable version? |
| **User-serving model** | The empathic model conveniently supports what the user wants to do | Check if the model makes the user uncomfortable anywhere. If not, it's too convenient. |

---

## Depth Scaling

| Depth | Divergence Points | Context Categories | Internal Narrative Length | Min Findings |
|-------|-------------------|-------------------|--------------------------|-------------|
| 1x | 2 | 3 | 2 sentences | 4 |
| 2x | 4 | 4 | 3 sentences | 8 |
| 4x | 6 | 5 | 4 sentences | 14 |
| 8x | 10 | 6 | 6 sentences | 22 |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Context reconstructed from THEIR information, not user's
- [ ] Internal narrative written in first person as THEM
- [ ] Every divergence point typed (information / interpretation / values / identity / interest)
- [ ] Model tested for projection — does it sound like you, or like them?
- [ ] At least one element that makes the user uncomfortable
- [ ] Prediction tied to specific divergence points
- [ ] Weakest assumption identified
- [ ] Depth floors met

---

## Integration

- **Use from**: `/conflict` (understand each party), `/persua` (understand the audience), `/trust` (understand trust gaps)
- **Routes to**: `/conflict` (if empathic model reveals structural disagreement), `/persua` (if user needs to communicate with this person), `/trust` (if trust dynamics are central)
- **Differs from**: `/sid` (self-directed identity analysis vs. other-directed), `/ecal` (calibrating your own emotions vs. modeling someone else's)
- **Complementary**: `/aw` (test the empathic model by assuming it's wrong), `/sdc` (check your own biases that might distort the model)
