# Decision Procedure — How to Ask the Wrong Question

**Date**: 2026-01-31
**Skill**: /dcp (Decision Procedure)
**Input**: how to ask the wrong question

---

## Step 1: Discover Decision Dimensions (`/dd`)

**Input**: "How to ask the wrong question" — this is about recognizing when you're framing a problem incorrectly, and building a procedure to detect and correct wrong questions before investing effort in answering them.

The recurring decision: **"Is the question I'm about to invest effort in actually the right question?"**

### Dimensions that determine whether a question is wrong:

1. **Premise Validity** — Does the question contain false assumptions? ("How do I make my employees stop being lazy?" assumes laziness is the problem.)

2. **Level of Abstraction** — Is the question too specific (missing the forest) or too vague (no actionable answer possible)? "What color should the button be?" vs. "How do I make the product better?"

3. **Addressee Fit** — Is this question being asked of the right person/source/method? Asking your lawyer for medical advice.

4. **Causal Direction** — Does the question assume the right causal relationship? "Why does my marketing not work?" when the product is the problem.

5. **Solution Presupposition** — Does the question smuggle in the answer? "Should we use React or Vue?" when the real question is "Do we need a SPA at all?"

6. **Scope Boundary** — Does the question include/exclude the right elements? "How do I fix this function?" when the architecture is wrong.

7. **Temporal Frame** — Is the question about the right time horizon? "How do I hit Q2 targets?" when the annual strategy is broken.

8. **Stakeholder Alignment** — Does the question reflect what actually matters, or what the asker *thinks* matters? "How do I get a promotion?" when the real question is "Am I in the right career?"

9. **Measurability** — Can you tell when you've answered it? "How do I be more creative?" has no finish line.

10. **Constraint Awareness** — Does the question acknowledge real constraints, or does it operate in fantasy-land? "How do I launch in 2 weeks?" when regulatory approval takes 6 months.

11. **Problem vs. Symptom** — Is the question about a root cause or a surface manifestation? "Why is the server slow?" when it's a database design issue.

12. **Binary Trap** — Does the question force an either/or when more options exist? "Should I stay or leave?"

---

## Step 2: Enumerate Options per Dimension (`/se`)

| Dimension | Possible States |
|---|---|
| **Premise Validity** | Valid premises / One+ false premise / Unexamined premises / Contradictory premises |
| **Level of Abstraction** | Too concrete (micro) / Right level / Too abstract (macro) / Mixed levels simultaneously |
| **Addressee Fit** | Right source / Wrong expertise / Right expertise wrong context / No one can answer this |
| **Causal Direction** | Correct causal model / Reversed cause-effect / Confounding variable / No causal relationship exists |
| **Solution Presupposition** | Open question / Mildly presupposes / Strongly presupposes / Question IS the answer |
| **Scope Boundary** | Too narrow / Right scope / Too broad / Misframed boundary |
| **Temporal Frame** | Too short-term / Right horizon / Too long-term / Wrong phase of lifecycle |
| **Stakeholder Alignment** | Reflects real needs / Reflects stated needs (not real) / Reflects asker's needs (not stakeholders') / Reflects no one's actual needs |
| **Measurability** | Clear success criteria / Fuzzy but approximable / Unmeasurable / Measuring wrong thing |
| **Constraint Awareness** | All constraints visible / Missing hard constraint / Imaginary constraint / Conflicting constraints |
| **Problem vs. Symptom** | Root cause / Intermediate cause / Symptom / Unrelated to actual problem |
| **Binary Trap** | Open option space / Unnecessarily narrowed / False binary / Exhaustive but missing best option |

**Key interactions**:
- If Premise Validity = false, almost every other dimension is compromised
- If Problem vs. Symptom = symptom, Causal Direction is almost certainly wrong too
- Solution Presupposition + Binary Trap compound: a presupposed binary is the most dangerous question form

---

## Step 3: Surface Hidden Assumptions (`/aex`)

The standard approach to evaluating questions assumes:

1. **"I know what I don't know"** — People assume they can tell when they're asking the wrong question. In reality, wrong questions feel exactly like right questions from the inside.

2. **"The question is obvious from the situation"** — People assume the problem hands you the question. Actually, the same situation supports dozens of framings.

3. **"Experts ask better questions"** — Experts often ask *narrower* questions due to the Einstellung effect (fixation on familiar problem frames).

4. **"More information fixes wrong questions"** — Gathering more data to answer the wrong question makes you more confidently wrong, not less wrong.

5. **"Questions are neutral"** — Every question frames reality. "Why did the project fail?" vs. "What did the project reveal?" create different answer spaces.

6. **"You can evaluate a question in isolation"** — A question is only right or wrong relative to a goal. Without knowing the goal, you can't evaluate the question.

7. **"Wrong questions are obviously bad"** — The most dangerous wrong questions are *almost* right — they feel productive and generate plausible answers that happen to be irrelevant.

8. **"Asking 'is this the right question?' is sufficient"** — This is itself often the wrong meta-question. Better: "What would change if this question turned out to be unanswerable?"

---

## Step 4: Generate the Procedure (`/stg`)

---

```
WRONG QUESTION DETECTION PROCEDURE
====================================

WHO THIS IS FOR: Anyone about to invest significant time, money,
or effort answering a question. Use this BEFORE you start working
on the answer.

TIME TO COMPLETE: 15-30 minutes per question evaluated.

YOU WILL NEED: The question you're evaluating, written down.
```

### STEP 0: What type of question are you checking?

| Your question looks like... | Go to... |
|---|---|
| "How do I [specific action]?" | SECTION A |
| "Why is [thing] happening?" | SECTION B |
| "Should I [option A] or [option B]?" | SECTION C |
| "What is the best [thing]?" | SECTION D |
| None of these / I'm not sure | SECTION E |

---

### SECTION A: "How do I..." Questions

**Step A1**: Write down what you'd do with the answer once you had it. Literally: "If someone told me how, I would then ___."

**Step A2**: Look at what you wrote. Is that action *definitely* the right next move?
- If YES and you're confident → **Step A3**
- If you hesitated or said "probably" → **STOP. Your question is likely wrong.** Go to SECTION E, Step E1.

**Step A3**: Remove the "how" — state only the outcome you want. Example: "How do I increase conversion?" becomes "I want higher conversion."
- Now ask: Is there a way to get that outcome that doesn't involve the method your question assumes?
- If YES → Your question is **too narrow**. Reframe as: "What are all the ways to achieve [outcome]?"
- If NO → Your question may be fine. Proceed to CHECKPOINT 1.

---

### SECTION B: "Why is..." Questions

**Step B1**: Write down the thing you'd *do differently* once you knew why. "If I knew why, I would ___."

**Step B2**: Is there a way to do that thing without knowing why?
- If YES → You don't need "why." Your real question is "How do I [the thing from B1]?" Go to SECTION A.
- If NO → Proceed to Step B3.

**Step B3**: List 3 possible answers to your "why" question. If each answer would lead you to the *same* action, you don't need the "why" — you already know what to do. **Your question is a procrastination mechanism.**

**Step B4**: If different answers lead to different actions, your question is probably right. Proceed to CHECKPOINT 1.

---

### SECTION C: "Should I A or B?" Questions

**Step C1**: Write down who told you the options are A and B. Was it:
- You assumed these were the only options → **HIGH RISK of wrong question.** Go to Step C2.
- Someone else framed it this way → Go to Step C3.
- These are genuinely the only options (e.g., "Should I accept or decline this offer?") → Go to CHECKPOINT 1.

**Step C2**: Spend 2 minutes listing other options. Write them down. If you find even one plausible option C, your question was wrong. **Reframe**: "What are all my options for [the underlying goal]?"

**Step C3**: Ask: Does the person who framed it this way benefit from limiting your options?
- If YES (e.g., a salesperson, a recruiter) → Treat as Step C2.
- If NO → Go to CHECKPOINT 1.

---

### SECTION D: "What is the best..." Questions

**Step D1**: Best *for what purpose*? Write down the specific purpose.
- If you can't write a specific purpose → **Your question is wrong.** You need to figure out what you're optimizing for first. Reframe: "What am I actually trying to achieve?"
- If you wrote a purpose → Step D2.

**Step D2**: Best *given what constraints*? List your constraints (budget, time, skill level, etc.).
- If you listed fewer than 2 constraints → You're probably in fantasy-land. Add real constraints and re-ask.
- If you have constraints → Step D3.

**Step D3**: Your refined question is: "What is the best [thing] for [purpose] given [constraints]?" Does this still feel like the question you started with?
- If YES → Proceed to CHECKPOINT 1.
- If NO → Your original question was wrong. Use the refined version.

---

### SECTION E: Unclear or Unusual Questions

**Step E1**: State the *goal behind the question*. Not "what am I asking?" but "what situation am I trying to change?"

**Step E2**: Is the question about a **symptom** or a **root cause**? Test: If you solved it, would the underlying situation actually improve?
- If NO → You're treating a symptom. Ask: "What is causing [the situation I want to change]?"
- If YES → Step E3.

**Step E3**: Rephrase your question 3 different ways, each starting with a different word (Why/What/How/Who/When/Where). Pick the framing that feels most *uncomfortable*. That's likely closer to the right question.

Proceed to CHECKPOINT 1.

---

### CHECKPOINT 1: The Five Lethal Tests

Run your question (original or reframed) through ALL five. Fail ANY one = wrong question.

| # | Test | How to check | If it fails... |
|---|---|---|---|
| 1 | **Premise Test** | List every fact your question treats as true. Is each one verified? | Find the false premise. Rebuild the question without it. |
| 2 | **Null Test** | "What if this question has no answer?" Would that change what you do? | If nothing changes, you don't need to answer it. |
| 3 | **Inversion Test** | Ask the opposite question. ("Why does this work?" instead of "Why does this fail?") Does the opposite question reveal more? | Use the inverted question. |
| 4 | **Stakeholder Test** | Who else cares about this answer? Would THEY ask the same question? | Investigate how others would frame it. |
| 5 | **Action Test** | What *specific action* will you take once answered? Can you name it? | If no clear action → wrong question or premature question. |

---

### STEP FINAL: Output

After running through the sections and checkpoint:

- **If your question survived unchanged** → It's probably the right question. Answer it.
- **If your question changed once** → Use the new version. It's likely better.
- **If your question changed 2+ times** → You're in a poorly-understood problem space. Before answering any question, invest time in understanding the *situation* first. Use: "What is actually going on with [situation]?" as your starting question.

---

## QUICK REFERENCE CARDS

### Card 1: The 3-Second Sniff Test
Before deep analysis, ask: **"If I got a perfect answer to this question right now, would I know what to do next?"**
- YES → Question might be fine.
- NO → Question is definitely wrong.

### Card 2: Wrong Question Red Flags
- You've been "researching" for a long time with no action taken
- Multiple smart people give you different answers
- The answer keeps changing depending on who you ask
- You feel like you need "just a little more information"
- The question came from someone else and you never examined it

### Card 3: The Reframe Formula
`Wrong: "How do I [method]?"`
`Right: "What achieves [outcome] given [constraints]?"`

`Wrong: "Why is [bad thing] happening?"`
`Right: "What would I do differently if I knew?"`

`Wrong: "Should I A or B?"`
`Right: "What are all options for [goal]?"`

---

## Step 5: Anticipate Failures (`/fla`)

### Failure Mode 1: "My question passed, but it was still wrong"
**When it happens**: The question contains a false premise you genuinely believe is true. The Premise Test only catches premises you can *see*.
**How to recognize**: You get a clear answer, act on it, and things don't improve.
**Override**: Ask someone with a *different worldview* to read your question and tell you what it assumes. People outside your domain catch premises insiders are blind to.

### Failure Mode 2: "I reframed into an even worse question"
**When it happens**: During Section E, Step E3, the "most uncomfortable" reframe is uncomfortable because it's *bad*, not because it's *revealing*.
**How to recognize**: The reframed question makes you feel confused, not exposed.
**Override**: Discomfort from a right question feels like "I don't want this to be the real issue." Discomfort from a bad question feels like "This doesn't make sense." Trust the distinction.

### Failure Mode 3: "I got stuck in infinite reframing"
**When it happens**: Every question leads to another reframe. Analysis paralysis.
**How to recognize**: You've reframed 3+ times and still aren't confident.
**Override**: Stop reframing. Your problem isn't the question — it's insufficient understanding of the situation. Do fieldwork: talk to people, observe the system, gather data. Come back when you have new information.

### Failure Mode 4: "I skipped to the section I wanted"
**When it happens**: User classifies their question into the most flattering category (Section D instead of Section B).
**How to recognize**: The section's steps don't quite fit your situation.
**Override**: If steps feel awkward, you're in the wrong section. Go back to Step 0 and pick honestly.

### Failure Mode 5: "The procedure said my question was fine, but the real issue was the goal"
**When it happens**: The question is well-formed for a goal that itself is wrong.
**How to recognize**: You answer the question, achieve the goal, and still aren't satisfied.
**Override**: This procedure checks *questions*, not *goals*. If you suspect the goal is wrong, evaluate the goal first using: "What will be different in my life when this goal is achieved? Do I actually want that?"

---

## Step 6: Validate Executability (`/pv`)

**Validation checklist**:

| Check | Status |
|---|---|
| Every step is a concrete action (write, list, ask) — not "consider" or "reflect" | PASS |
| All decision points are binary or explicit multiple choice | PASS |
| No jargon without inline definition | PASS |
| Every path terminates (no dead ends or infinite loops) | PASS — infinite reframe caught by Failure Mode 3 |
| Someone with no expertise could follow this | PASS — no domain knowledge required |
| Steps reference observable outputs ("write down," "list," "count") | PASS |

**Issue found and fixed**: Step E3 ("pick the framing that feels most uncomfortable") relies on subjective judgment. Failure Mode 2 was added to catch misapplication.

---

## COMMON MISTAKES

1. **Using this procedure on trivial questions.** "What should I have for lunch?" doesn't need a procedure. Use this for questions where the answer will cost significant resources to obtain or act on.

2. **Running the procedure in your head.** Write things down. The procedure works because it forces externalization. Mental shortcuts defeat the purpose.

3. **Stopping at the first reframe.** The first reframe is often just a slightly better wrong question. Run CHECKPOINT 1 on your reframe too.

4. **Treating "the question changed" as failure.** Changing your question is the *point*. It means you caught a wrong question before wasting effort on it.

5. **Skipping the Action Test.** This is the most commonly skipped test and the most valuable. If you can't name a specific action you'll take with the answer, you are not ready to ask the question.

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **Emergency situations**: When speed matters more than precision. Ask the obvious question and correct later.
- **Emotional questions**: "Should I leave this relationship?" has dimensions this procedure doesn't cover. Seek a counselor, not a flowchart.
- **Questions that are their own answer**: Some questions (especially philosophical or creative ones) generate value through the asking, not the answering. This procedure is for *instrumental* questions.
- **When an expert is available**: If you have access to a genuine domain expert, ask them "Am I asking the right question?" directly. That's faster and more reliable.

---

## WORKED EXAMPLES

### Example 1: The Entrepreneur

**Original question**: "How do I get more website traffic?"

- Section A → Step A1: "If I knew how, I would implement the tactic and get more visitors."
- Step A2: Is more traffic the right move? Hesitation — conversion rate is 0.3%.
- **STOP** → Section E, Step E1: Goal = more revenue.
- Step E2: More traffic with 0.3% conversion is a symptom. Root cause: the site doesn't convert.
- **Reframed question**: "Why do 99.7% of visitors leave without buying?"
- CHECKPOINT 1: Passes all five tests. Action Test → "I would fix the top exit points."

**Result**: Avoided months of SEO work that would have multiplied a broken funnel.

### Example 2: The Manager

**Original question**: "Should I fire Dave or put him on a PIP?"

- Section C → Step C1: Manager assumed these were the only options.
- Step C2: Other options: reassign Dave, change his role, address the team dynamic, check if the problem is management not Dave.
- **Reframed question**: "What's causing Dave's underperformance and what's the best way to resolve it?"
- CHECKPOINT 1: Passes. Action Test → "I would address the root cause, which might be firing, PIP, reassignment, or changing my own behavior."

**Result**: Avoided a premature binary choice.

### Example 3: The Student

**Original question**: "What's the best programming language to learn?"

- Section D → Step D1: Purpose = "to get a job." Specific enough.
- Step D2: Constraints = "I have 3 months, no CS background, targeting web development." Two constraints listed.
- Step D3: Refined: "What's the best first programming language for someone with no CS background who wants a web dev job within 3 months?"
- **Question changed from original.** Use the refined version.
- CHECKPOINT 1: Passes all five tests.

**Result**: The refined question is answerable; the original was not (there is no "best language" in the abstract).

---

```
VALIDATION STATUS: This procedure has not been validated by domain experts.
It is a synthesis of epistemology, decision science, and practical reasoning patterns.
Test it on low-stakes questions before relying on it for high-stakes decisions.
```
