---
name: "sp - Steelman Prompt"
description: Improves a prompt before it gets answered. Adds precision, scope, criteria, skill routing, and failure-proofing without answering the question.
output:
  format: "prose"
---

# Steelman Prompt

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Vague prompt**: The user has a prompt that's too vague to get a good answer. Needs precision, scope, and criteria added.
**Interpretation 2 — Compound prompt**: The user has a prompt that bundles multiple questions. Needs unbundling into distinct, answerable sub-questions.
**Interpretation 3 — Failure-prone prompt**: The user has a prompt that could technically be answered in useless ways. Needs failure-proofing.

If ambiguous, run all passes.
If clear from context, skip passes that don't apply.

---

## Core Principles

1. **Improve the question, don't answer it.** The output of /sp is a better prompt, not a response to the prompt.

2. **Preserve intent exactly.** The improved prompt must ask the same question as the original, just more precisely.

3. **Add what's missing, don't add what's not needed.** If the prompt is already tight, say so and return it unchanged.

4. **The best prompts have built-in failure prevention.** A good prompt makes it hard for the responder to give a bad answer.

---

## Pass 1: Classify

Identify the prompt type:

| Type | Signal | Example |
|------|--------|---------|
| **CLAIM** | "X is true", "X is better" | "Remote work is more productive" |
| **DECISION** | "Should I X?", "X or Y?" | "Should I switch to Rust?" |
| **DIAGNOSTIC** | "Why is X?", "What's causing X?" | "Why are users churning?" |
| **EXPLORATORY** | "What are the options?", "How could I?" | "What are all the ways to grow revenue?" |
| **GOAL** | "I want X", "I need to X" | "I want to be a better leader" |
| **METHOD** | "How do I X?" | "How do I deploy to production?" |
| **EMOTIONAL** | "I'm frustrated", "I'm stuck" | "Nothing is working and I don't know what to do" |
| **CREATIVE** | "Write X", "Create X" | "Write a blog post about AI safety" |
| **META** | "What skill should I use?", "Help me" | "I don't know where to start" |

```
TYPE: [CLAIM / DECISION / DIAGNOSTIC / EXPLORATORY / GOAL / METHOD / EMOTIONAL / CREATIVE / META]
```

SKIP: If the type is obvious, state it in one line and move on.

---

## Pass 2: Unbundle

Split compound prompts into distinct questions.

```
ORIGINAL: [original prompt]

QUESTIONS FOUND:
1. [question 1]
2. [question 2]
...
```

Also check for:
- **"I think X"** — contains an implicit claim that should be made explicit
- **"X, but Y"** — contains a tension that should be separated
- **"I'm not sure about X"** — contains uncertainty that should be classified
- **"X, etc."** — contains an implied list that should be expanded
- **"Handle this"** — too vague, needs decomposition into sub-tasks

SKIP: If the prompt contains a single clear question, skip this pass entirely.

---

## Pass 3: Criteria

Add what the prompt is missing based on its type:

- **CLAIM**: What would falsify this? What's the scope? What counts as evidence?
- **DECISION**: What are the criteria? What alternatives exist? What are the constraints? What's reversible vs irreversible?
- **DIAGNOSTIC**: What are the symptoms? What's the timeline? What changed? What's been tried?
- **EXPLORATORY**: What dimensions matter? What are the constraints? When is the list complete? How exhaustive?
- **GOAL**: What does success look like? What's the timeline? What are the constraints? What's the real want vs proxy?
- **METHOD**: What's the goal? What are the constraints? What resources are available? What's been tried?
- **EMOTIONAL**: What's the underlying need? What would resolution look like?
- **CREATIVE**: Who's the audience? What's the purpose? What's the quality standard? What format?
- **META**: What are you trying to accomplish? What have you already tried?

```
MISSING CRITERIA:
- [criterion 1]
- [criterion 2]
...
```

SKIP: If the prompt already specifies its own success criteria, skip.

---

## Pass 4: Failure-check

Identify 2-3 ways a response could technically satisfy the prompt but be useless.

```
FAILURE MODES:
- A response could [failure mode 1] — fix: [what to add]
- A response could [failure mode 2] — fix: [what to add]
```

Common failure modes to check:
- **Platitude response**: The answer could be vague wisdom instead of concrete guidance
- **Surface response**: The answer could address the surface question and miss the real question
- **Confirmation response**: The answer could agree with the user instead of testing their assumptions
- **Scope mismatch**: The answer could be too broad or too narrow for the user's needs
- **Audience mismatch**: The answer could be at the wrong level of sophistication

SKIP: If the prompt is already tight enough that failure modes are unlikely, skip.

---

## Pass 5: Skill Routing

Identify which skills would best handle the improved prompt:

```
RECOMMENDED SKILLS:
- Primary: /[skill] — [why this is the best fit]
- Also consider: /[skill] — [what it adds]
- Supplementary: /[skill] — [optional enhancement]
```

Skill mapping by type:
| Type | Primary skill | Also consider |
|------|--------------|---------------|
| CLAIM | /claim → /araw | /agsk, /obv, /eth, /fut |
| DECISION | /decide → /cmp or /araw | /dom, /obo, /ogo, /ecal |
| DIAGNOSTIC | /diagnose → /uaua or /rca | /obv, /sid, /rmm |
| EXPLORATORY | /search → /se or /uaua | /list, /siycftr, /etc |
| GOAL | /want → /wt | /kta, /iaw, /platitude |
| METHOD | /how → /foht | /stg, /to, /awtlytrn |
| EMOTIONAL | /emotion | /sdc, /kta, /iagca |
| CREATIVE | /create → /w or /pw | /wre, /story, /stl |
| META | /meta | /wsib, /fonss, /dtse |

SKIP: If the user just wants a better prompt, not skill routing.

---

## Pass 6: Reconstruct

Combine everything into a single improved prompt. This is the only output the user needs.

Rules:
- Preserve the original intent exactly
- Incorporate criteria and failure-mode fixes directly into the prompt text
- If unbundled, either recombine into one sharper question or list as numbered sub-questions
- Output as a clean copy-paste block
- Keep it concise — the improved prompt should be usable, not an essay
- Include skill routing recommendation below the prompt

```
IMPROVED PROMPT:

[The steelmanned prompt goes here — ready to copy-paste into a new session]

SUGGESTED SKILL: /[skill] [improved prompt]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Over-engineering** | Simple prompt made complex | Only add criteria that would actually change the answer quality |
| **Intent drift** | Improved prompt asks a different question | Re-read original — does the improved version ask the same thing? |
| **Answering instead of improving** | Started responding to the prompt instead of improving it | The output is a better prompt, not an answer |
| **Skill routing without improvement** | Suggested a skill but didn't improve the prompt | The prompt improvement is the primary deliverable |

---

## After Completion

Report:
- The original prompt
- Classification and type
- The improved prompt (copy-paste ready)
- Suggested skill routing
- What the improvement adds (what was missing from the original)

### Follow-Up Routing

After the prompt is improved, the user may:
- **Use the improved prompt directly**: paste it into a new session
- **Run the suggested skill**: → INVOKE: /[suggested skill] [improved prompt]
- **"What skill is best for this?"** → INVOKE: /wsib [improved prompt]
- **"Decompose this prompt"** → INVOKE: /itp [improved prompt]
- **"Extract all skills from this prompt"** → INVOKE: /extract [improved prompt]

---

## Integration

- **Use from**: Any situation where the user's prompt could be sharper before processing
- **Routes to**: /claim, /decide, /diagnose, /search, /how, /want, /emotion, /create, /meta (based on prompt type), /wsib (skill selection), /itp (prompt decomposition), /extract (skill extraction)
- **Differs from**: /itp (sp improves the prompt, itp decomposes it), /extract (sp rewrites the prompt, extract identifies skills for it), /handle (sp improves before answering, handle routes to action)
- **Complementary**: /itp (decompose the improved prompt), /wsib (select best skill for improved prompt), /fonss (sequence skills for improved prompt)
