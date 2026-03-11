# /sp Improve this prompt: "Use AI to think better"
**Date:** 2026-03-09
**Skill:** /sp (Steelman Prompt)

---

## Pass 1: Classify

**ORIGINAL PROMPT:** "Use AI to think better"

**TYPE: GOAL**

This is a goal-type prompt. The user wants to achieve something ("think better") using a tool ("AI"), but hasn't specified what "think better" means, what kind of thinking, in what context, or what success looks like.

---

## Pass 2: Unbundle

```
ORIGINAL: "Use AI to think better"

QUESTIONS FOUND:
1. What kinds of thinking does the user want to improve? (analytical, creative, decision-making, problem-solving, writing, strategic?)
2. What does "better" mean here? (faster, more rigorous, fewer blind spots, more creative, more structured?)
3. What role should AI play? (partner, checker, generator, challenger, organizer?)
4. What's the context? (professional work, personal decisions, learning, writing, research?)
```

This is a compound prompt disguised as a simple one. "Think better" bundles at least four distinct sub-questions.

---

## Pass 3: Criteria

```
MISSING CRITERIA:
- What domain of thinking? (decisions, analysis, creativity, problem-solving, writing, planning)
- What does "better" mean specifically? (fewer errors, broader perspective, more structured, faster, deeper)
- What's the current problem? (what thinking failures or limitations is the user actually experiencing?)
- What's the context of use? (daily work, specific project, ongoing practice, one-off situation)
- What level of AI involvement? (AI as tool, AI as thinking partner, AI as checker/critic)
- What does success look like? (a specific outcome, a repeatable process, a new habit)
```

---

## Pass 4: Failure-check

```
FAILURE MODES:
- A response could list generic AI tips ("use ChatGPT to brainstorm!") without addressing any specific thinking weakness — fix: specify what kind of thinking failure the user wants to address
- A response could treat this as a tool recommendation question and just list AI products — fix: frame the prompt around thinking improvement, not tool selection
- A response could deliver platitudes about "AI-augmented cognition" without giving concrete, actionable methods — fix: require specific techniques with examples of when to use each
```

---

## Pass 5: Skill Routing

```
RECOMMENDED SKILLS:
- Primary: /want — this is a goal prompt; /want will clarify what the user actually wants beneath the surface framing
- Also consider: /how — once the goal is clarified, "how do I use AI to improve X thinking" becomes a method question
- Supplementary: /se — if the user wants to explore the full space of AI-assisted thinking techniques
```

---

## Pass 6: Reconstruct

```
IMPROVED PROMPT:

I want to use AI (like Claude or similar LLMs) as a thinking partner to improve
the quality of my reasoning. Specifically:

1. What are the 5-7 most common thinking failures that AI can help catch or
   correct? (e.g., confirmation bias, scope neglect, weak analogies) For each
   one, give me a concrete technique — what I type, what I ask for, what the
   AI does.

2. What's a practical daily workflow for using AI to pressure-test my thinking
   before I act on decisions or share conclusions? I want a repeatable process,
   not one-off tricks.

3. What should I NOT use AI for when it comes to thinking — where does
   AI-assisted reasoning reliably make things worse?

Context: I'm a professional who makes analytical and strategic decisions regularly.
I'm not looking for "AI can help you brainstorm" — I want specific, structured
methods that improve reasoning rigor.

SUGGESTED SKILL: /want I want to use AI as a thinking partner to improve the
quality of my reasoning — what are the concrete techniques, a daily workflow,
and the known failure modes?
```

---

## Summary

| | |
|---|---|
| **Original prompt** | "Use AI to think better" |
| **Classification** | GOAL — vague aspiration with no criteria, scope, or success definition |
| **Improved prompt** | See reconstructed prompt above (copy-paste ready) |
| **Suggested skill** | `/want` (goal clarification), then `/how` (method), optionally `/se` (exploration) |

**What the improvement adds:**
- **Specifies the kind of thinking**: reasoning quality, not creativity or speed
- **Defines "better"**: catching thinking failures, pressure-testing conclusions, improving rigor
- **Adds structure**: three distinct, answerable sub-questions instead of one vague blob
- **Prevents platitudes**: explicitly asks for concrete techniques with examples, rejects generic advice
- **Includes failure awareness**: asks where AI makes thinking worse, not just better
- **Sets audience level**: professional context, not beginner tips
- **Makes it actionable**: requests a repeatable workflow, not a one-time list
