---
name: "insd - Insight and Discovery"
description: "Generate genuine insights by identifying stuck-points, inverting assumptions, changing representations, using incubation, and crystallizing through stability tests."
---

# Insight and Discovery

**Input**: $ARGUMENTS

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/insd 4x [input]").

| Depth | Min Inversions | Min Representations | Min Cycles | Min Crystal Tests |
|-------|---------------|--------------------|-----------|--------------------|
| 1x    | 3             | 1                  | 1         | 1                  |
| 2x    | 5             | 2                  | 2         | 2                  |
| 4x    | 8             | 3                  | 3         | 3                  |
| 8x    | 12            | 4                  | 4         | 5                  |
| 16x   | 18            | 5                  | 6         | 7                  |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## STEP 0: What phase are you in?

Read all three. Pick the one that fits best.

(A) I have a specific problem and I'm stuck on it.
    -> Go to SECTION A: UNSTICKING

(B) I'm exploring a domain and want to find something interesting.
    -> Go to SECTION B: EXPLORATION

(C) I had a partial insight and want to develop it fully.
    -> Go to SECTION C: CRYSTALLIZATION

---

### SECTION A: UNSTICKING

You have a problem. You've been working on it. You're not making progress. The goal is to break the impasse.

**Step A1**: Write down your current approach in one sentence.
- Example: "I'm trying to reduce server costs by optimizing database queries."
- What you should see: A clear statement of WHAT you're doing and HOW you're doing it.

**Step A2**: Write down what would count as "solved."
- Example: "Server costs drop below $500/month without degrading response times."
- What you should see: A concrete, testable outcome.

**Step A3**: List every assumption in your A1 sentence.
- Go word by word. Each noun and verb hides an assumption.
- "reduce" assumes the number should go down (not be restructured). "server costs" assumes the cost unit is the server (not the query, not the feature, not the user). "optimizing" assumes the current approach is right and needs tuning (not replacement). "database queries" assumes the database is the bottleneck (not the architecture).
- Target: At least 5 assumptions. If you found fewer, you're not looking hard enough -- reread your sentence.

**Step A4**: For each assumption, write the opposite.
- "Reduce costs" -> "What if costs should increase in some areas to decrease elsewhere?"
- "Database queries are the problem" -> "What if the database is fine and the problem is elsewhere?"
- What you should see: Statements that feel slightly wrong or uncomfortable. That discomfort is signal.

**Step A5**: Which inverted assumption feels most uncomfortable?
- Pick ONE. The one that makes you think "no, that can't be right" the strongest.
- WARNING: If none feel uncomfortable, you haven't inverted deeply enough. Return to A4.

**Step A6**: Spend exactly 10 minutes exploring the uncomfortable inversion AS IF it were true. Don't evaluate it. Just follow its implications.
- Write continuously. Don't stop to judge.
- What you should see: After 5-7 minutes, a moment where you think "wait, actually..." or "huh, that's interesting."

**Step A7**: Did a new angle emerge?
- YES -> Go to SECTION C: CRYSTALLIZATION with the new angle.
- NO -> Go to Step A8.

**Step A8**: Change your representation.
- If you've been thinking in words -> draw a picture.
- If you've been using diagrams -> write a story where the components are characters.
- If you've been formal/mathematical -> explain it to an imaginary 10-year-old using only physical analogies.
- If you've been building -> step back and describe what you see as if you're a journalist visiting for the first time.
- Spend 15 minutes in the new representation.

**Step A9**: Did a new angle emerge?
- YES -> Go to SECTION C: CRYSTALLIZATION.
- NO -> Go to Step A10.

**Step A10**: STOP WORKING. Do something physically active and completely unrelated for at least 30 minutes. Walking, exercise, cooking, cleaning. NOT reading, NOT scrolling, NOT "relaxing while thinking about it."
- Your only task during this break: if any thought about the problem surfaces, notice it and let it pass. Don't grab it.

**Step A11**: After the break, before doing anything else, write the FIRST thing that comes to mind about the problem.
- Don't filter. Don't judge. Write it raw.
- What you should see: Often something different from where you left off. The break reorganized something.

**Step A12**: Is the first-thought different from your A1 approach?
- YES -> Go to SECTION C: CRYSTALLIZATION with this new frame.
- NO -> Go to Step A13.

**Step A13**: Talk to someone who knows NOTHING about your domain.
- Explain the problem in plain language. Their job is only to ask questions, especially "why" and "what do you mean by..."
- Don't seek their solution. Seek the moment where explaining something reveals you don't understand it as well as you thought.
- What you should see: At least one point where you say "hm, good question" and don't have a ready answer.

**Step A14**: Did the conversation surface a gap in your understanding?
- YES -> The gap IS the insight. Go to SECTION C.
- NO -> Return to Step A3 with a DIFFERENT one-sentence description of your approach. You may have the wrong problem framing entirely. If you've cycled through A3 three times with different framings, go to SECTION B (you may need to explore more broadly before this specific problem can yield).

---

### SECTION B: EXPLORATION

You don't have a specific stuck-point. You want to discover something interesting in a domain.

**Step B1**: Pick a domain boundary.
- Exploration requires a container. State what you're exploring.
- TOO BROAD: "science" / "business" / "philosophy"
- TOO NARROW: "the third parameter of this function"
- RIGHT SIZE: "how cells decide to divide" / "what makes some marketplaces succeed" / "the relationship between rhythm and meaning in poetry"
- What you should see: A scope where you could spend 2 hours and not run out of material, but not so broad you don't know where to start.

**Step B2**: Collect 5 SPECIFIC FACTS about your domain that you find surprising, confusing, or contradictory.
- Not "interesting" -- specifically things that don't fit your current understanding.
- Read, search, ask, observe. Don't analyze yet. Just collect.
- WARNING: If everything you find makes sense, you're reading confirmatory material. Seek out critics, edge cases, failures, or historical wrong turns.

**Step B3**: For each fact, write: "This is surprising because I expected ___."
- The gap between expectation and reality is where discovery lives.
- What you should see: Your implicit model of the domain becoming visible.

**Step B4**: Do any two surprises seem related?
- Look for pairs where the same underlying cause could explain both.
- YES -> Write a one-sentence hypothesis connecting them. Go to Step B6.
- NO -> Go to Step B5.

**Step B5**: Pick the MOST surprising fact. Ask: "What ELSE would be true if this fact is pointing at something deeper?"
- List 3 predictions that would follow.
- Then check: are any of those predictions true?
- If YES -> You may have found a pattern. State it as a hypothesis. Go to Step B6.
- If NO or UNCLEAR -> Collect 5 more surprising facts (Step B2). After 3 cycles of B2-B5 with no emerging pattern, change your domain boundary (return to B1 with an adjacent topic).

**Step B6**: You have a hypothesis. Now try to BREAK it.
- Find the strongest counterexample or objection.
- Not a straw-man -- the real best argument against your idea.
- What you should see: Either the hypothesis breaks (return to B4 with a refined version) or survives with a clarification of its boundary conditions.

**Step B7**: The hypothesis survived attempted destruction.
- State it precisely: "In [context], [X] because [Y], which means [Z]."
- Go to SECTION C: CRYSTALLIZATION.

---

### SECTION C: CRYSTALLIZATION

You have something -- a new angle, a hypothesis, a felt sense that something is there. The goal is to make it solid.

**Step C1**: State the insight in one sentence, as plainly as possible.
- No jargon. No hedging. Say what you actually think is true.
- "I think [X] is happening because [Y]."
- WARNING: If you can't state it in one sentence, you don't have one insight -- you have several partial ones. List them separately and process each through C1.

**Step C2**: What did you believe BEFORE this insight?
- Write the old belief explicitly.
- What you should see: A clear contrast. If old and new aren't clearly different, the "insight" may be restatement, not reorganization. Return to wherever you came from.

**Step C3**: What CHANGES if this insight is correct?
- List concrete implications:
  - What would you do differently?
  - What would you predict differently?
  - What would you stop doing?
  - What new questions does it raise?
- Target: At least 3 concrete changes. If you can't find 3, the insight may be trivial -- interesting but not action-relevant.

**Step C4**: What's the strongest argument AGAINST your insight?
- Write it as if you're a smart critic who disagrees.
- Not a weak objection -- the real one.
- What you should see: Either a genuine threat to the insight (which refines it) or a clarification of the conditions under which it holds.

**Step C5**: Can you RE-DERIVE the insight from scratch?
- Close your notes. Wait 5 minutes. Then try to reconstruct the insight from memory, including the reasoning that led to it.
- YES, and the re-derivation matches -> The insight is stable. Go to Step C6.
- YES, but the re-derivation is different -> You have TWO paths to related but different insights. Both are worth keeping. State each separately and process the new one from C1.
- NO, can't reconstruct -> The insight was state-dependent (mood, context). It may still be valid but needs more development. Return to the section you came from.

**Step C6**: Formalize and record.
- Write the insight in full:
  - The claim (one sentence)
  - The evidence (what led you here)
  - The boundary conditions (when this applies and doesn't)
  - The implications (what changes)
  - The open questions (what you still don't know)

-> PROCEDURE COMPLETE. You have a crystallized, tested, re-derivable insight.

---

## QUICK REFERENCE CARDS

### Card 1: The Insight Loop
Problem -> Assumptions -> Inversion -> Discomfort -> Follow the discomfort -> New angle -> Test -> Crystallize

### Card 2: When You're Stuck
1. Name your approach in one sentence
2. List its assumptions
3. Invert the most uncomfortable one
4. Explore the inversion without judging
5. If nothing: change representation
6. If nothing: take a physical break
7. If nothing: explain to a non-expert

### Card 3: Representation Switches
Words -> Pictures -> Stories -> Math -> Physical models
Always switch TO whichever you haven't tried yet.

### Card 4: Surprise as Compass
Surprise = expectation does not equal reality.
The gap between what you expected and what you found is the most information-dense location in any domain. Go toward surprise, not away from it.

---

## COMMON MISTAKES

1. **Trying harder in the same mode.** Symptom: You've been at it for hours and feel like "if I just think a bit more..." Fix: Any approach that hasn't yielded in 30 minutes of focused effort needs a mode switch, not more effort.

2. **Skipping the discomfort.** Symptom: You invert an assumption and immediately think "that's obviously wrong" and move on. Fix: The inversion that feels most wrong is the most valuable to explore. "Obviously wrong" is your current model protecting itself.

3. **Premature formalization.** Symptom: You have a vague sense of something and immediately try to write it precisely. Fix: Hold the vague sense. Sketch it. Talk about it loosely. Let it stabilize before locking it down.

4. **Confusing novelty with insight.** Symptom: "I've never thought of this before!" but it doesn't change anything you'd actually do. Fix: Apply the C3 test -- does it change predictions or actions? If not, it's a curiosity, not an insight.

5. **Explaining away anomalies.** Symptom: "Oh that's just because of [easy explanation]" without checking. Fix: Write down the easy explanation. Then ask: "What if the easy explanation is wrong?" Investigate for at least 5 minutes before accepting it.

6. **Never testing the insight.** Symptom: You have an exciting idea and immediately start building on it without checking if it's true. Fix: Always do Step C4 (strongest counterargument) and C5 (re-derivation) before investing in the idea.

7. **Solo loop.** Symptom: You've been cycling alone for hours. Fix: Another person's questions are the cheapest way to surface assumptions you can't see. Talk to someone.

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **Seek expert help when**: The domain is technical and getting the answer wrong has high consequences (medical, legal, structural engineering, etc.). Use this procedure for understanding, not for final decisions in high-stakes technical domains.

- **Abandon the procedure when**: You've been through all three sections and nothing emerged. This likely means you need more raw material -- go learn more about the domain before trying to have insights about it.

- **Skip to Section C when**: You already had the insight and just want to test and formalize it.

- **Use a different approach when**: The "insight" you need is actually a calculation, a lookup, or a known result. Not everything requires discovery -- sometimes you just need to find the answer someone else already has.

---

## WORKED EXAMPLES

### Example 1: Software engineer stuck on a performance bug

**A1**: "I'm trying to speed up the API by caching database results."
**A2**: "Response time under 200ms for 95th percentile."
**A3**: Assumptions: speed is the problem (not perceived speed); API is the bottleneck (not frontend); caching is the solution (not restructuring); database is slow (not the query pattern); results are cacheable (not dynamic).
**A4**: Inversion: "What if the database is fast and the problem is the 47 sequential queries, not any single query's speed?"
**A5**: This feels uncomfortable because "we already looked at the query count."
**A6**: [10 min exploring]: "If query count is the real issue, then caching is a band-aid -- we'd still make 47 round trips to the cache. The real fix is restructuring the data access pattern to batch..."
**A7**: YES -- new angle: batch the data access, don't cache it.
**C1**: "The performance problem is 47 sequential round trips, not slow individual queries."
**C2**: Previously believed individual query speed was the issue.
**C3**: Changes: stop optimizing individual queries, redesign the data fetching to use 2-3 batch queries instead.
**C4**: Counter: "But some queries depend on previous results." Response: "Only 3 of the 47 have true dependencies. The other 44 can be parallelized or batched."
**C5**: Re-derived successfully. The key is round-trip count, not query speed.
**C6**: Formalized. Insight is stable.

### Example 2: Researcher exploring "why some ideas spread"

**B1**: Domain boundary: "What determines whether an intellectual idea gets adopted by a field vs. ignored."
**B2**: Surprising facts:
  1. Darwin's theory was independently co-discovered by Wallace -- the time was "ripe."
  2. Mendel's genetics was ignored for 35 years then rediscovered by three people simultaneously.
  3. Continental drift was rejected for 50 years despite strong evidence.
  4. Some wrong ideas (phlogiston) persisted for decades with strong institutional support.
  5. Many breakthroughs came from outsiders to the field.
**B3**: "I expected ideas spread based on evidence quality. But facts 2-4 show that evidence quality is nearly irrelevant -- timing and fit with existing frameworks matter more."
**B4**: Facts 2 and 3 connect: both are about ideas that were "right" but the field wasn't ready. Hypothesis: "An idea spreads when it solves a problem the field is currently stuck on, regardless of the idea's independent merit."
**B6**: Counter: "Antibiotics spread immediately based on dramatic evidence." Refinement: "Ideas spread fast when they solve a FELT problem. Fields with no felt problem reject even correct ideas."
**B7**: Hypothesis survived: "Intellectual adoption is demand-driven, not supply-driven. An idea needs a pre-existing unsolved problem in the audience's mind to land."
**C1-C6**: [crystallization process completed]

### Example 3: Someone exploring personal career dissatisfaction

**A1**: "I'm trying to find a more fulfilling job by searching for roles that match my skills."
**A3**: Assumptions: fulfillment comes from skill-match; jobs are the unit of analysis (not projects or relationships); searching is the right action (not creating); "my skills" are fixed (not developable).
**A4**: "What if fulfillment has nothing to do with skill-match?"
**A5**: Deeply uncomfortable -- "I spent years developing these skills."
**A6**: [10 min]: "Every time I was most fulfilled, it wasn't because I was using my skills -- it was because I was learning something new that felt slightly beyond me. The fulfilled state is the learning state, not the competence state..."
**A7**: YES -- new angle.
**C1**: "I'm fulfilled by the learning edge, not by skill application. I need a role that keeps me at the boundary of my competence, not one that uses what I already know."
[continues through crystallization...]
