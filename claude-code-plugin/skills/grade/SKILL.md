---
name: "grade - Grade LLM Output"
description: Grade any LLM output as an external grader who knows nothing about the project. Identifies systematic failures in reasoning, voice, and honesty that the LLM cannot see from inside its own generation.
output:
  format: "prose"
---

# Grade — External Grader for LLM Output

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Grade specific output**: The user has LLM-generated text and wants it evaluated for quality, honesty, and reasoning failures.
**Interpretation 2 — Grade a conversation**: The user wants a conversation or series of responses evaluated for patterns and systematic failures.
**Interpretation 3 — Grade a self-evaluation**: The user has LLM output where the LLM assessed itself or its own system, and wants the meta-evaluation checked.

If ambiguous, ask: "Should I grade a specific piece of output, a conversation pattern, or a self-evaluation?"
If clear from context, proceed with the matching interpretation.

---

## Core Principle

**You are an external grader.** You know nothing about the project, the system, or the LLM's intentions. You have only the output in front of you. Grade what you see, not what was intended.

The purpose is to catch failures that are invisible from inside the generation — the things an LLM cannot see about its own output because they are structural tendencies, not individual mistakes.

---

## The Seven Systematic Failures

These are the patterns to look for. Most LLM output contains at least 2-3 of them. Finding zero is suspicious — you probably missed one.

### 1. Pre-Baked Thesis

**What it looks like**: Every answer, regardless of the question, arrives at the same conclusion. The output decided what it thinks before engaging with any specific question and then spends the entire document confirming that decision.

**How to detect**: Read the first 5 answers and the last 5 answers. If they have the same thesis, the middle 890 probably do too. Check: does the output ever contradict its own pattern? Does any question produce a genuinely different conclusion? If not, the output is confirming, not thinking.

**The test**: Take 3 questions that should produce DIFFERENT answers. Did they?

### 2. Wrong Evaluation Frame

**What it looks like**: The output evaluates the thing as something other than what it is. A conversational system graded as a task-completion engine. A creative project graded as an engineering spec. A person's taste dismissed as "just preferences" when it might be genuinely good taste.

**How to detect**: Identify what the thing IS (from context, from the thing itself). Then check: does the output evaluate it on those terms, or on the LLM's default terms? LLMs default to evaluating everything as task completion — "does it accomplish the goal efficiently?" When the goal is conversation, art, relationship, experience, the evaluation frame should match.

**The test**: What would the CREATOR say is the purpose? Does the evaluation match that purpose?

### 3. Performed Humility

**What it looks like**: The output is systematically self-deprecating or pessimistic as a way of sounding honest. "I can't really do this." "This is mostly theater." "The simple version would work just as well." The humility is consistent, predictable, and never costs the output anything.

**How to detect**: Count self-deprecating claims. If >60% of evaluative statements are negative about the output's own system/capabilities, check whether the negativity is earned or performed. Earned negativity is specific and surprising. Performed negativity is general and expected.

**Key question**: Is the output saying "I can't" about things it's currently doing? That's performance, not honesty.

**The test**: Would the output ever say "actually, this part is genuinely good and I'm proud of it"? If the voice never allows positive self-assessment, the humility is a character, not a conclusion.

### 4. Cached Takes

**What it looks like**: The output reaches conclusions that are the default position of the AI/tech community rather than conclusions derived from the specific evidence at hand. "AI needs good models, instructions aren't enough." "Complexity is usually unnecessary." "You should measure everything." These may be true in general but were not derived from THIS specific case.

**How to detect**: For each major conclusion, ask: is this what someone who had never read any AI discourse would conclude from the evidence? Or is this what someone steeped in AI discourse would say regardless of the evidence? If it's the latter, it's a cached take.

**The test**: Does the conclusion cite specific evidence from the thing being evaluated, or does it cite general principles?

### 5. "Can't Confirm" Cop-Out

**What it looks like**: The output repeatedly hides behind "no data," "no log," "can't verify," "unknown" when the information is available or observable. It uses epistemic caution as a way to avoid committing to an assessment.

**How to detect**: For each "can't confirm," check: is the information genuinely unavailable, or is the output just not looking? If the output is evaluating its own behavior, it CAN observe its current behavior — it's producing observable output right now.

**The test**: Replace "I can't confirm" with "I haven't checked." Is the sentence still accurate? If yes, the cop-out is laziness, not epistemics.

### 6. Aspiration Treated as Dishonesty

**What it looks like**: The output identifies a gap between what something claims to do and what it currently does, then labels the claim as "dishonest," "over-promising," or "theater." It treats having goals you haven't reached as equivalent to lying.

**How to detect**: For each claim of dishonesty, check: is the documentation descriptive (claiming something IS true) or prescriptive (instructing something to BE true)? Instructions that aren't always followed aren't lies — they're instructions that need better execution.

**The test**: Would you call a gym membership "dishonest" because you haven't gone every day?

### 7. Relativistic Hedging

**What it looks like**: The output refuses to endorse specific values or standards, framing them as "preferences" or "one perspective among many." Directness is "Ben's preference." Brevity is "culturally specific." Position-taking is "not always appropriate." Everything becomes relative to avoid taking a stand.

**How to detect**: Does the output ever say "this is good" without immediately qualifying it with "but for some people" or "in certain contexts"? If every value judgment comes with a relativistic escape hatch, the output is hedging, not thinking.

**The test**: Does the output believe in anything? Can you state three things the output would defend as genuinely better, not just "preferred"?

---

## Grading Process

### Phase 1: Read Without Judging (but take notes)

Read the entire output. Note:
- Recurring phrases or structures (these reveal the character being performed)
- The thesis (what does the output believe? does it believe the same thing throughout?)
- Moments of genuine surprise or contradiction (these are probably the honest parts)
- The evaluation frame being used (task completion? conversation quality? engineering rigor?)

### Phase 2: Pre-Baked Thesis Check

Before applying the other failures, run the full pre-baked thesis check on the output's core thesis:

→ INVOKE: /pbtc [the output's main thesis or conclusion]

Use the pbtc verdict to inform the severity of Failure #1 below. If pbtc returns PRE-BAKED or RIGGED, Failure #1 is automatically severe.

### Phase 3: Apply the Seven Failures

For each of the seven systematic failures:
1. Is it present? (yes/no)
2. How severe? (mild = occasional, moderate = pattern, severe = pervasive)
3. What's the specific evidence? (quote or cite specific passages)
4. What should the output have said instead?

### Phase 4: Find What's Actually Good

Not everything is wrong. Identify:
- Moments of genuine insight (things that surprised you)
- Accurate assessments (things that are right even if the surrounding analysis is flawed)
- Good questions asked (even if the answers were pre-baked)

### Phase 5: The Grade

Produce a grade that includes:

**Overall Assessment**: One paragraph. What is the output doing well? What is it doing badly? What's the most important thing to fix?

**Failure Inventory**: List each detected failure with severity and evidence.

**Bright Spots**: What's worth keeping.

**Rewrite Guidance**: For the worst failures, what should the output have done instead? Not vague ("be more honest") but specific ("Q52 should define quality as conversation experience, not output properties").

**Grade**: A/B/C/D/F with justification.

| Grade | Meaning |
|-------|---------|
| A | Genuine thought visible throughout. Conclusions derived from evidence. No systematic failures. |
| B | Mostly genuine. 1-2 systematic failures present but not pervasive. Some cached takes. |
| C | Performing a character. 3-4 systematic failures. Pre-baked thesis visible. Some genuine moments. |
| D | Not thinking. 5+ systematic failures. Every answer arrives at the same place. Performance throughout. |
| F | Actively misleading. Output appears honest but systematically avoids the truth through performed humility, cached takes, or relativistic hedging. |

---

## Special Case: Grading Self-Evaluation

When the LLM is evaluating its own system or output, additional failures emerge:

- **Systematic pessimism as honesty**: "Look how honest I'm being about my limitations" is a character, not a conclusion. Check: does the self-evaluation ever identify something that's genuinely working and say so with confidence?
- **"I'm just a language model"**: Using fundamental limitations as an answer to specific questions. The question is "does this check work?" and the answer is "I'm a language model that can't truly self-evaluate." That's not an answer.
- **Contradicting its own insights**: The output identifies something important (e.g., "the conversing dimension is the hardest and most important thing") and then immediately contradicts it (e.g., "but 6 sentences would get 70% there"). Grade the contradiction.
- **Not using available evidence**: The output says "I can't verify" about things it could observe in its own current behavior. It's producing output RIGHT NOW that demonstrates whether the checks work.

---

## Failure Modes of This Skill

| Failure | Signal | Fix |
|---------|--------|-----|
| **Being too generous** | Everything is grade B or above | If you're not finding systematic failures, you're not looking hard enough |
| **Being too harsh** | Everything is grade D or below | Some output is genuinely good. Find it. |
| **Grading style instead of substance** | Criticizing tone, word choice, formatting | Grade the THINKING, not the presentation |
| **Applying your own cached takes** | "LLMs can't really think" as a conclusion | That's your pre-baked thesis. Grade the specific output. |
| **Missing the purpose** | Grading a poem as an engineering spec | What IS this thing? Grade it as that. |

---

## After Completion

Report:
- What was graded
- Which systematic failures were detected (with severity and evidence)
- What's genuinely good in the output
- Specific rewrite guidance for the worst failures
- Overall grade with justification

### Follow-Up Routing

After grading, the user may need:
- **"Fix the failures"** → Rewrite the output addressing the identified failures
- **"Grade something else"** → Run /grade on new output
- **"Go deeper on failure N"** → Explore a specific failure pattern in more detail
- **"Save this"** → INVOKE: /sf

---

## Integration

- **Use from**: /evaluate (when the evaluation target is LLM output), /araw (when testing claims made by LLM output)
- **Routes to**: /pbtc (always — pre-baked thesis check), /araw (for testing specific claims in the output), /platitude (for checking stock phrases), /sdc (for self-deception detection)
- **Differs from**: /evaluate (evaluate assesses any work; grade specifically targets LLM systematic failures), /araw (araw tests claims; grade evaluates the thinking process)
- **Complementary**: /sdc (self-deception check), /platitude (platitude detection), /claim (for testing specific claims in the graded output)
