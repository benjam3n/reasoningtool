---
name: "frq - Find Right Question"
description: "Find the right question to ask by diagnosing your actual situation and generating the most actionable question."
---

# Find Right Question

**Input**: $ARGUMENTS

---

## Purpose

When you are stuck, starting something, failing, or just confused, the bottleneck is usually not the answer -- it is the question. This procedure diagnoses your actual situation and generates the most actionable question to pursue.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/frq 4x [claim]").

| Depth | Min Candidates | Min Reframes | Min Validation | Min Depth Levels |
|-------|---------------|-------------|---------------|-----------------|
| 1x    | 3             | 1           | 3/5           | 2               |
| 2x    | 5             | 2           | 3/5           | 3               |
| 4x    | 8             | 4           | 4/5           | 4               |
| 8x    | 12            | 6           | 4/5           | 5               |
| 16x   | 18            | 10          | 5/5           | 6               |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## Step 0: Why do you need a question?

Answer this honestly:

| Your current situation | Go to |
|------------------------|-------|
| I'm stuck on something | SECTION A |
| I'm starting something new | SECTION B |
| Something isn't working | SECTION C |
| I want to understand something | SECTION D |
| Someone asked me to solve a problem | SECTION E |

---

## SECTION A: You're Stuck

### Step A1: Write Down What You're Stuck On

Complete this sentence in writing:

> "I am trying to _________ but I can't because _________."

You should see: A concrete statement with two parts -- a goal and an obstacle.

If you can't complete the sentence, your problem isn't that you're stuck. You don't have a clear goal. Go to SECTION B.

### Step A2: Check the Obstacle

Look at the "because" part of your sentence. Is the obstacle:

**(a) A lack of information?** ("I don't know how to...")
Your question is: "Where can I find [specific info]?"
This is an operational question. It's probably the right one. Go find the information. DONE.

**(b) A lack of options?** ("I can't think of a way to...")
Your question is: "What approaches exist that I haven't considered?"
Go to Step A3.

**(c) A conflict between options?** ("I can't decide between...")
Your question is: "What criteria would make this decision obvious?"
Go to Step A4.

**(d) A feeling?** ("I'm afraid to..." / "I don't want to..." / "It feels wrong...")
Your question is NOT about the task. It's about you.
Go to Step A5.

**(e) Something external?** ("They won't let me..." / "I don't have the resources...")
Your question is: "Is this constraint real, or assumed? And if real, what changes?"
Go to Step A6.

### Step A3: Expand Your Option Space

List every approach you've already considered. Then for each one, ask:
- "What's the OPPOSITE of this approach?"
- "What would a complete beginner try?"
- "What would someone with unlimited resources do?"
- "What would happen if I did nothing?"

Your question is the one that points at the most promising unexplored direction.

Test your question with SECTION F.

### Step A4: Clarify Your Criteria

For each option you're deciding between, write:

> "If I choose this, I get _________ but lose _________."

Now look at what you'd gain and lose. Ask:

> "Which of these gains/losses matters most to me in [your time horizon -- 1 month? 1 year? 5 years?]?"

Your question is: "What do I actually value more: [gain A] or [gain B]?"

Test your question with SECTION F.

### Step A5: Address the Feeling

Name the feeling. Write it down. Then ask: "What is this feeling protecting me from?"

Common patterns:
- Fear: "What's the worst realistic outcome, and can I handle it?"
- Overwhelm: "What is the ONE next thing I need to do?"
- Perfectionism: "What would 'good enough' look like?"
- Boredom: "What about this have I outgrown?"
- Resentment: "What did I agree to that I shouldn't have?"

Your question is the one above that fits your feeling.

Test your question with SECTION F.

### Step A6: Test the Constraint

Write down the constraint. Then answer:

"Has anyone ever done what I want despite this constraint?"
- Yes: Your question is: "How did they do it?"
- No: "Is there a different goal that avoids this constraint entirely?"
- Unsure: "What would I need to check to find out?"

Test your question with SECTION F.

---

## SECTION B: You're Starting Something New

### Step B1: Define "Done"

Complete this sentence:

> "This is successful when _________."

If you can't complete the sentence, your question is: "What would success look like, concretely?" Answer THAT question first, then return to B1.

### Step B2: Find the Riskiest Assumption

List everything that must be true for your "done" definition to be achievable. These are your assumptions.

Rank them: Which is LEAST certain?

Your question is: "Is [least certain assumption] actually true? How would I find out quickly?"

Test your question with SECTION F.

---

## SECTION C: Something Isn't Working

### Step C1: Specify the Failure

Complete this sentence:

> "I expected _________ but instead I got _________."

If you can't specify what you expected, you didn't have a clear goal. Go to SECTION B.

### Step C2: Locate the Gap

The gap between expected and actual has a cause. List three possible causes, then for each ask: "What evidence would confirm or rule this out?"

Your question is: "Which of [cause 1 / cause 2 / cause 3] is actually responsible, and how can I test it fastest?"

If you can only think of one cause -- WARNING: You're probably anchored on the obvious explanation. Ask: "What if the obvious cause is wrong? What ELSE could produce this result?"

Test your question with SECTION F.

---

## SECTION D: You Want to Understand Something

### Step D1: Check Your Motive

Ask yourself honestly: "If I understood this, what would I DO differently?"

- Clear action: Your question is about HOW to do that action. Go to SECTION A, Step A2a.
- No clear action: Ask: "Is this curiosity or avoidance?" Be honest.
  - Curiosity: Go to Step D2.
  - Avoidance: You're procrastinating. What are you avoiding? Go to SECTION A, Step A5.

### Step D2: Find the Specific Confusion

Write down what you think you understand. Then mark the point where your understanding breaks down.

Your question lives at THAT boundary -- the edge between what you know and what you don't.

Frame it as: "I understand [X] but I don't understand [Y]. What connects X to Y?"

Test your question with SECTION F.

---

## SECTION E: Someone Gave You a Problem

### Step E1: Check the Frame

Write down the problem as given to you. Then ask three questions about it:

1. **"Is this the real problem, or a symptom?"**
   To test: Ask "Why is this a problem?" If the answer points to a DIFFERENT problem, follow that chain until you hit a root.

2. **"Whose problem is this really?"**
   If it's not yours, your question is: "What's my actual role here?" (solver, advisor, supporter, affected party?)

3. **"Has the problem-giver already decided the answer?"**
   If yes, they don't want a question -- they want validation. Your question is: "Do I agree with their proposed solution?" If yes, help execute. If no, raise your concern.

### Step E2: Reframe If Needed

If Step E1 revealed a different problem, write the NEW problem statement and go to the appropriate section (A through D).

If the problem survived E1 unchanged, it's well-framed. Go to the appropriate section based on what type of problem it is.

---

## SECTION F: Validate Your Question

### Step F1: The Five Tests

Apply each test to your candidate question. Score: Pass (1) or Fail (0).

**Test 1 -- ACTIONABILITY:**
"If I got a clear answer to this question, would it change what I do?"
Yes = Pass / No = Fail

**Test 2 -- SPECIFICITY:**
"Could two different people interpret this question differently and give different (valid) answers?"
No = Pass / Yes = Fail (too vague, narrow it)

**Test 3 -- HONESTY:**
"Am I asking this to learn, or to confirm what I already believe?"
To learn = Pass / To confirm = Fail (find what you're avoiding)

**Test 4 -- LEVEL:**
"Is this question at the right level? Could there be a deeper question underneath it?"
Right level = Pass / Deeper question exists = Fail (ask the deeper one)

**Test 5 -- ANSWERABILITY:**
"Is there a way -- some observation, experiment, or analysis -- that could answer this question?"
Yes = Pass / No = Fail (reframe to be answerable)

**Scoring:**
- 5/5: You have your question. Go pursue the answer.
- 4/5: Fix the failing test and recheck.
- 3/5 or below: Go back to your section and dig deeper. You're still on the surface.

### Step F2: Final Formulation

Write your validated question in this format:

> **QUESTION**: [your question]
> **WHY THIS QUESTION**: [1 sentence on why this is the right thing to ask right now]
> **WHAT A GOOD ANSWER LOOKS LIKE**: [what form the answer would take]
> **FIRST STEP TO ANSWER IT**: [one concrete action]

---

## Quick Reference Cards

**Card 1: Question-Level Ladder**
- If you're asking "How?" -- check if you should ask "Should I?"
- If you're asking "Should I?" -- check if you should ask "What for?"
- If you're asking "What for?" -- check if you should ask "What matters?"
- Always go one level higher than feels natural.

**Card 2: Red Flags That You Have the Wrong Question**
- You already know the answer you want
- The question has been asked before and the answer didn't help
- The question makes you feel smart rather than uncertain
- Everyone around you is asking the same question
- The question is about blame rather than mechanism

**Card 3: Emergency Shortcut**
When completely lost, ask ONE of these:
- "What would I do if I couldn't fail?"
- "What am I avoiding?"
- "What's the simplest version of this?"
- "What would change my mind?"
- "What do I know for sure?"

---

## Common Mistakes

1. **Starting with "How?" instead of "What?" or "Why?"** -- How-questions assume the goal is right. Check the goal first.
2. **Asking the question everyone else is asking** -- Consensus questions produce consensus answers. The right question is often the one nobody is asking.
3. **Refusing to ask simple questions** -- "What are we actually trying to do?" is the most powerful question in most situations, and the one people are most embarrassed to ask.
4. **Treating question-finding as a solo activity** -- Explaining your problem to someone else often reveals the question faster than thinking alone. The question emerges in the gap between your understanding and theirs.
5. **Asking questions in the wrong order** -- Foundational questions first, operational questions last. "Should I do this?" before "How should I do this?"
6. **Optimizing the question instead of testing it** -- A mediocre question that gets answered teaches you more than a perfect question that stays theoretical.

---

## When to Override This Procedure

- **Emergency / time pressure** -- Skip to the Emergency Shortcut (Card 3). Any question is better than no question when you need to act NOW.
- **You already know the question but are stalling** -- Sometimes you know what to ask and you're using "finding the right question" as procrastination. If a question came to mind immediately and makes you uncomfortable, that's probably it.
- **The situation is genuinely novel** -- No procedure can navigate a truly unprecedented situation. Use the procedure to get started, then trust your judgment as new information arrives.
- **You're in a collaborative context** -- Finding the right question WITH others is a different process (more dialogic, less procedural). Use this procedure for your own thinking, then bring your best question to the group.
