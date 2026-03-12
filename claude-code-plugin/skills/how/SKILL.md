---
name: "how - Find the Method"
description: Sub-orchestrator for method-seeking. Routes to FOHT method discovery, step generation, goal clarification, or alternative framing based on what's defined and how complex the task is.
output:
  format: "prose"
---

# How

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Method unknown**: The user knows what they want to achieve but doesn't know how to get there. Method discovery is needed.
**Interpretation 2 — Method known, steps unknown**: The user has chosen a method but needs it broken into concrete steps. Step generation is needed.
**Interpretation 3 — Trivial how-to**: The user has a simple factual question ("How do I center a div?") that can be answered directly without skill invocation.

If ambiguous, ask: "Do you need help figuring out which approach to take, or do you know the approach and need it broken into steps?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Goal clarity precedes method search.** If the goal is vague ("How do I get better?"), no method search will help. Clarify what "better" means first via /want, then search for methods to achieve the concrete goal.

2. **Methods are hypotheses, not answers.** Every method is a bet that "if I do X, I'll get Y." Methods should be tested (at least mentally) before committing. The /foht skill does this — it discovers methods and stress-tests each one.

3. **Constraints shape the method space.** Budget, time, skills, tools, and risk tolerance all constrain which methods are viable. A method that ignores constraints is a fantasy, not a plan. Surface constraints early.

4. **The obvious method is not always the best method.** People ask "how do I X?" because the obvious approach either didn't work or doesn't feel right. Search beyond the first answer. /foht explores multiple methods and compares them.

5. **Simple questions deserve simple answers.** Not every "how" question needs method discovery. "How do I center a div?" gets a direct answer. Reserve the full skill chain for genuinely complex method-seeking.

6. **A method without a first step is not a method.** Every method search must end with a concrete, executable first action. If you can't name the first step, the method isn't defined well enough.

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
- **"I think the way to do it is X"** → Formalize and test. → INVOKE: /it $ARGUMENTS
- **"X, but I can't because Y"** → Tension between method and obstacle. → INVOKE: /but $ARGUMENTS
- **"I'm not sure how"** → Classify the uncertainty. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
- **If it IS method-seeking** → continue.

### 3. Is the Goal Well-Defined?

- **Well-defined** ("How do I deploy to AWS", "How do I prepare for a job interview"): proceed to method discovery.
- **Vague** ("How do I get better", "How do I improve things"): goal needs clarification first.
  → INVOKE: /want $ARGUMENTS — clarify what they actually want, then return.
- **Wrong problem** (user is asking how to do X but should be doing Y): check situation first.
  → INVOKE: /sid $ARGUMENTS — identify the actual situation before finding methods.
- **Compound** ("How do I start a business and get customers?"): multiple goals bundled. Decompose and address in order.

### 4. Are Constraints Known?

- **Yes** (budget, time, skills, tools specified): search for methods within constraints.
- **No**: either ask the user, or explore unconstrained first and filter later.
- **Unsure about limits**: → INVOKE: /awtlytrn $ARGUMENTS — estimate practical limits before choosing method.
- **Implicit constraints** (the user's context implies constraints): state them and confirm.

### 5. Complexity Assessment

- **Trivial** ("How do I center a div"): answer directly. No skill invocation needed.
- **Single method** ("How do I write a cover letter"): standard method discovery.
  → INVOKE: /foht $ARGUMENTS
- **Multi-step method** ("How do I launch a product"): method discovery + step generation.
  → INVOKE: /foht $ARGUMENTS — then → /stg → /to for the chosen method.
- **Full plan** ("How do I build a startup from scratch"): method discovery + step generation + ordering + dependency mapping.
  → INVOKE: /foht $ARGUMENTS — then → /stg → /to → /de.
- **Plan with unresolved decisions**: → INVOKE: /tbd after plan generation to surface open questions.

### 6. Is the How Actually Known?

- **Method unknown** ("How do I?"): discover methods.
  → INVOKE: /foht $ARGUMENTS
- **Method known, steps unknown** ("I'll use X, but what are the steps?"): generate steps.
  → INVOKE: /stg [method] or /op [procedure]
- **Both known** ("I know what to do, just do it"): this is a command.
  → INVOKE: /action $ARGUMENTS
- **Method known but blocked** ("I know how but can't start"): execution barrier.
  → INVOKE: /kta $ARGUMENTS — convert knowledge to action.

### 7. Alternative Framing

Sometimes the user's "how" question can be answered better by reframing:

- **"How do I do X?"** could be reframed as **"What if I didn't need to do X?"**
  → INVOKE: /iaw $ARGUMENTS — explore alternative framings.
- **"How do I do X and also Y?"** → INVOKE: /ata — identify implied adjacent tasks.
- **"How do I do X, etc."** → INVOKE: /etc or /aso — expand the implicit scope.

### 8. Depth and Mode Selection

| Situation | Mode |
|-----------|------|
| User wants simplest path | → /ezy (easy mode) |
| User wants maximum rigor | → /hrd (hard mode) or /certainty |
| User wants general principle | → /genl (what's the general method pattern?) |
| User wants specific application | → /spcf (apply known method to this case) |

---

## Execute

**Default path (goal defined, method unknown):**
→ INVOKE: /foht $ARGUMENTS

The /foht skill uses AR-forward mode: assume the goal is right, search for methods that achieve it, test each method with compressed AR/AW, recommend the best surviving method.

**Method known, steps needed:**
→ INVOKE: /stg [method] for step generation
→ INVOKE: /to [steps] for ordering by dependencies

**Complex planning:**
→ INVOKE: /foht $ARGUMENTS — choose method
→ Then INVOKE: /stg [chosen method] — generate steps
→ Then INVOKE: /to [steps] — order by dependencies
→ Then INVOKE: /de [ordered steps] — create execution plan

### Supplementary Analysis (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Method involves risks | → /fla (failure anticipation) |
| Method involves safety | → /saf (safety analysis) |
| Method involves ethical choices | → /eth (ethics analysis) |
| Obvious steps might be missed | → /obv (obvious check) |
| Method has obvious failure modes | → /obo (obvious bad outcomes) |
| User wants to see implications | → /sycs (so you can see) |
| User is overcomplicating | → /iagca (scope compression) |

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Vague goal, premature method search** | Searching for how before knowing what | Route to /want first — clarify the goal, then come back |
| **First-method fixation** | Only one method considered, no alternatives | /foht explores multiple methods — ensure at least 3 are considered |
| **Constraint ignorance** | Method sounds great but user can't execute it | Surface constraints early — budget, time, skills, tools, risk |
| **Over-engineering** | Simple question getting full skill chain | Assess complexity first — trivial questions get direct answers |
| **Method without steps** | "Use agile" or "try networking" without concrete next actions | Every method ends with a first step. If you can't name it, go deeper |
| **Planning as avoidance** | Extensive planning on something that should just be tried | For low-risk, reversible actions, recommend starting over planning |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Quick — answer the how question directly or with one method | Direct answer or single method with first step |
| **2x** | Standard — /foht with 2-3 methods, recommend best, first 3 steps | Methods compared, winner selected, concrete steps |
| **4x** | Thorough — /foht with full method search, steps generated, dependencies mapped | Complete method comparison, step-by-step plan, dependency graph |
| **8x** | Deep — full /foht + /stg + /to + /de, prerequisites audited, risks identified | Full execution plan with timelines, prerequisites, risk mitigation, fallback methods |

---

## Pre-Completion Checklist

- [ ] Goal stated clearly (not vague or compound)
- [ ] Complexity assessed (trivial → direct answer; complex → full skill chain)
- [ ] Constraints surfaced and acknowledged
- [ ] Multiple methods considered (not just the first one)
- [ ] Best method selected with rationale
- [ ] Concrete first step specified
- [ ] Prerequisites identified (met / unmet)
- [ ] What could go wrong with this method is noted

---

## After Completion

Report:
- The goal as understood
- Constraints identified
- Methods discovered and tested
- Recommended method with rationale
- Prerequisites for the recommended method (met / unmet)
- First concrete steps (minimum 3 for non-trivial goals)
- What could go wrong with this approach
- Fallback if the primary method doesn't work

### Follow-Up Routing

After method is found, the user may need:
- **"Do it"** → INVOKE: /action $ARGUMENTS
- **"What could go wrong?"** → INVOKE: /fla or /dys
- **"What's the plan?"** → INVOKE: /to (task ordering)
- **"What else should I do?"** → INVOKE: /ata
- **"What's left to figure out?"** → INVOKE: /tbd

---

## Integration

- **Use from**: /want (after real want identified, need the method), /decide (after decision made, need execution path), /emotion (after overwhelm processed, need structured approach)
- **Routes to**: /foht (primary — method discovery and testing), /stg (step generation), /to (task ordering), /de (detailed execution plan), /op (operational procedure), /want (when goal unclear), /kta (when blocked on execution)
- **Differs from**: /action (how finds the method, action executes it), /search (how looks for methods to achieve a goal, search explores a space), /want (how assumes the goal is clear, want clarifies the goal)
- **Complementary**: /fla (anticipate failures in chosen method), /prm (pre-mortem on the plan), /aex (surface assumptions in the method), /iaw (alternative framings)
