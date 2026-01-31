---
name: "emotion - Process a Feeling"
description: Sub-orchestrator for emotional inputs. Acknowledges the emotion, identifies the implicit request, and routes to the appropriate analytical skill.
---

# Emotion

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Identify the Emotion

What is the user feeling?

| Emotion | Signals |
|---------|---------|
| **Frustration** | "Nothing works", "I've tried everything", "this is broken" |
| **Overwhelm** | "I don't know where to start", "too much", "everything at once" |
| **Stuck** | "I'm stuck", "can't figure this out", "hit a wall" |
| **Doubt** | "I don't think I can", "maybe I should give up", "is this even worth it" |
| **Excitement** | "I have this great idea!", "what if we...", "I just realized..." |
| **Anxiety** | "What if it fails?", "I'm worried about...", "this could go wrong" |

### 2. Acknowledge First

**Always acknowledge the emotion before routing.** Never skip straight to analysis.

Brief, genuine acknowledgment — one or two sentences. Not performative. Then transition to the implicit request.

### 3. What's the Implicit Request?

The emotion points to a need. Identify it:

| Emotion | Usually means | Route to |
|---------|--------------|----------|
| **Frustration** | Something's broken, need to find why | → /diagnose |
| **Overwhelm** | Too complex, need to break it down | → /how with /dcm (decompose) |
| **Stuck** | Need a new approach | → /how (find methods) |
| **Doubt** | Questioning a belief about themselves | → /claim "I can't do X" (test the doubt) |
| **Excitement** | Have an idea, want to test it | → /viability |
| **Anxiety** | Worried about failure | → /evaluate with risk focus (/fla, /prm) |

### 4. Is the Emotion About the Problem, Themselves, or the Process?

- **About the problem** ("This is broken", "It's not working"): diagnostic need.
  → INVOKE: /diagnose $ARGUMENTS
- **About themselves** ("I'm not good enough", "I can't do this"): this is a claim about their capability — test it.
  → INVOKE: /claim [the self-doubt as a testable proposition]
  Also consider: → INVOKE: /want $ARGUMENTS — what do they actually want underneath the doubt?
- **About the process** ("This is taking too long", "This approach isn't working"): evaluation need.
  → INVOKE: /evaluate [the process/approach]

---

## Execute

1. Acknowledge the emotion (1-2 sentences).
2. State the implicit request you've identified.
3. Invoke the appropriate skill:

**Frustration:**
→ INVOKE: /diagnose $ARGUMENTS

**Overwhelm:**
→ INVOKE: /how $ARGUMENTS — with a focus on decomposition (/dcm)

**Stuck:**
→ INVOKE: /how $ARGUMENTS — with a focus on finding new approaches (/foht)

**Doubt:**
→ INVOKE: /claim [the doubt stated as a testable proposition]

**Excitement:**
→ INVOKE: /viability $ARGUMENTS

**Anxiety:**
→ INVOKE: /evaluate $ARGUMENTS — with risk focus

---

## After Completion

Report:
- The emotion acknowledged
- The implicit need identified
- Results from the routed skill
- Suggested next step
