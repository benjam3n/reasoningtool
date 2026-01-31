---
name: "how - Find the Method"
description: Sub-orchestrator for method-seeking. Routes to FOHT method discovery, step generation, or goal clarification based on what's defined.
---

# How

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Extract the Goal

What does the user want to achieve? State it clearly. "How do I X" → the goal is X.

### 2. Is This Actually Method-Seeking?

- **"Should I X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"Why is X happening?"** → This is diagnostic. → INVOKE: /diagnose $ARGUMENTS
- **"What are the options?"** → This is exploration. → INVOKE: /search $ARGUMENTS
- **"I want X"** → This is goal-stating (wants are deeper). → INVOKE: /want $ARGUMENTS
- **"Do X"** → This is a command (they know the how). → INVOKE: /action $ARGUMENTS
- **If it IS method-seeking** → continue.

### 3. Is the Goal Well-Defined?

- **Well-defined** ("How do I deploy to AWS", "How do I prepare for a job interview"): proceed to method discovery.
- **Vague** ("How do I get better", "How do I improve things"): goal needs clarification first.
  → INVOKE: /want $ARGUMENTS — clarify what they actually want, then return.

### 4. Are Constraints Known?

- **Yes** (budget, time, skills, tools specified): search for methods within constraints.
- **No**: either ask the user, or explore unconstrained first and filter later.

### 5. Single Method or Full Plan?

- **Single method** ("How do I center a div"): answer directly. No skill invocation needed for trivial how-tos.
- **Multi-step method** ("How do I launch a product"): method discovery needed.
  → INVOKE: /foht $ARGUMENTS
- **Full plan** ("How do I build a startup from scratch"): method discovery → step generation → ordering.
  → INVOKE: /foht $ARGUMENTS — then → /stg → /to for the chosen method.

### 6. Is the How Actually Known?

- **Method unknown** ("How do I?"): discover methods.
  → INVOKE: /foht $ARGUMENTS
- **Method known, steps unknown** ("I'll use X, but what are the steps?"): generate steps.
  → INVOKE: /stg [method] or /op [procedure]
- **Both known** ("I know what to do, just do it"): this is a command.
  → INVOKE: /action $ARGUMENTS

---

## Execute

**Default path (goal defined, method unknown):**
→ INVOKE: /foht $ARGUMENTS

The /foht skill uses AR-forward mode: assume the goal is right, search for methods that achieve it, test each method with compressed AR/AW, recommend the best surviving method.

---

## After Completion

Report:
- The goal as understood
- Methods discovered and tested
- Recommended method with rationale
- Prerequisites for the recommended method
- First concrete steps
