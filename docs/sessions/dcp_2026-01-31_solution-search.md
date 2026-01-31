# Decision Procedure — Solution Search

**Date**: 2026-01-31
**Input**: solution search

---

# SOLUTION SEARCH PROCEDURE
### How to find the right solution to any problem, from emergency fixes to pioneer territory

---

## Step 1: Decision Dimensions

**D1: Problem Clarity** — Do you know exactly what the problem is, or is the problem itself unclear? A precise problem ("the server returns 500 errors on POST requests") searches differently than a vague one ("something feels wrong with user growth"). This determines whether you start by defining the problem or searching for solutions.

**D2: Solution Space Familiarity** — How much do you already know about possible solutions? Range: you've solved this exact type before → you've solved adjacent problems → you know the domain but not this specific issue → you don't even know what domain this belongs to. This determines where you start looking.

**D3: Time Constraint** — How much time do you have before you need a working solution? Range: minutes (production outage) → hours → days → weeks → open-ended. This determines depth vs. speed tradeoff and whether you can afford to search broadly or must satisfice.

**D4: Reversibility** — Can you try a solution and switch if it's wrong? Range: fully reversible (try, undo, try again) → costly to reverse (migration, public commitment) → irreversible (surgery, deleted data, published work). This determines how much verification the solution needs before implementation.

**D5: Solution Uniqueness Requirement** — Do you need THE right answer, A good-enough answer, or a novel answer nobody has tried? Standard problems need known solutions. Creative problems need novel ones. Optimization problems need the best one. This determines search strategy shape.

**D6: Resource Budget** — What can you spend on the search itself? Money (hire an expert, buy a tool), social capital (ask for favors, use network), effort (personal time and energy), attention (cognitive bandwidth). Search costs are real and can exceed the problem's cost.

**D7: Knowledge Distribution** — Where does the knowledge needed to solve this problem live? In your own head, in documentation, in other people, in experimentation only, or nowhere yet (no one has solved this). This determines which search channels to use.

**D8: Failure Cost** — What happens if the solution you find is wrong? Range: minor inconvenience → wasted time/money → damaged relationships/reputation → catastrophic/irreversible harm. High failure cost demands more thorough search and verification.

**D9: Problem Recurrence** — Is this a one-time problem or does it recur? One-time problems justify quick fixes. Recurring problems justify investing in robust, reusable solutions. This determines how much infrastructure to build around the solution.

**D10: Constraint Profile** — What constraints must the solution satisfy? Technical constraints (compatibility, performance), resource constraints (budget, timeline), social constraints (stakeholder buy-in, user willingness), regulatory constraints (legal, compliance). Missing a hard constraint invalidates the entire solution.

**D11: Decomposability** — Can the problem be broken into independent sub-problems? Decomposable problems can be searched in parallel. Monolithic problems must be solved holistically. This determines search architecture.

**D12: Signal-to-Noise Ratio** — How much irrelevant information will you encounter while searching? Some domains (medical symptoms, software errors) have enormous noise. Others (math problems, legal precedent) have cleaner search spaces. This determines how much filtering you need.

---

## Step 2: Options per Dimension

**D1 Problem Clarity:**
- **Crystal clear**: You can state the problem in one sentence with specific observables
- **Mostly clear**: You know the category but not the specifics
- **Symptomatic**: You observe symptoms but don't know the underlying problem
- **Vague unease**: Something is wrong but you can't articulate what

**D2 Solution Space Familiarity:**
- **Expert**: You've solved this type before. Search = recall + adapt.
- **Adjacent**: You've solved related problems. Search = analogy + transfer.
- **Literate**: You know the domain vocabulary. Search = research + filter.
- **Novice**: You don't know what you don't know. Search = orient + learn + then search.
- **Pioneer**: Nobody has solved this. Search = invent + experiment.

**D3 Time Constraint × D4 Reversibility Interaction:**
| | Reversible | Costly to reverse | Irreversible |
|---|---|---|---|
| **Minutes** | Try first promising | Try + monitor closely | Stabilize, don't solve yet |
| **Hours** | Try top 3, pick best | Research then try best | Research heavily, try once |
| **Days** | Broad search, optimize | Systematic comparison | Expert consultation |
| **Weeks+** | Exhaustive search | Pilot/prototype first | Multiple expert opinions |

**D5 Solution Uniqueness:**
- **Known solution exists**: Search is FINDING, not inventing. Use databases, documentation, experts.
- **Good-enough needed**: Satisficing search — stop at first acceptable answer.
- **Optimal needed**: Exhaustive search — enumerate options, compare systematically.
- **Novel needed**: Creative search — analogies from other domains, constraint removal, inversion.

**D7 Knowledge Distribution:**
- **In your head**: Recall, journal review, sleep on it
- **In documentation**: Google, manuals, Stack Overflow, academic papers
- **In other people**: Network, experts, communities, mentors
- **In experimentation**: A/B tests, prototypes, trial-and-error
- **Nowhere yet**: First principles reasoning, novel synthesis, invention

**D9 Recurrence × D6 Budget Interaction:**
- One-time + low budget → Quick fix, move on
- One-time + high budget → Thorough search, implement well
- Recurring + low budget → Find a cheap systematic approach
- Recurring + high budget → Build infrastructure (tool, process, automation)

**D11 Decomposability:**
- **Fully decomposable**: Break into parts, solve each independently, combine
- **Partially decomposable**: Some parts interact, solve clusters
- **Monolithic**: All parts interdependent, must solve as whole
- **Layered**: Must solve in sequence (each layer depends on previous)

---

## Step 3: Hidden Assumptions

People searching for solutions typically assume:

1. **"The problem as stated IS the problem."** Often the stated problem is a symptom, a downstream effect, or a misframing. Solving the stated problem can leave the real problem untouched. Experts ask "is this the right problem?" before searching for solutions. Novices jump straight to solution search.

2. **"The solution exists in my domain."** If you're a programmer, you search for code solutions. If you're a manager, you search for process solutions. The actual solution may require crossing domain boundaries — a technical problem may need a people solution, or vice versa.

3. **"Google/asking someone is always the first step."** For problems you've seen before, the first step is RECALL — checking your own memory and notes. For truly novel problems, the first step is FRAMING — making sure you're asking the right question. External search is step 2 or 3, not step 1.

4. **"More search = better solution."** Search has diminishing returns. After a certain point, you're finding variations of the same answers. The skill is knowing WHEN to stop searching, not how to search more.

5. **"I'll recognize the right solution when I see it."** Recognition requires evaluation criteria. Without explicit criteria defined BEFORE searching, you'll gravitate toward solutions that feel right (confirmation bias) rather than solutions that ARE right.

6. **"The first working solution is the solution."** First solutions tend to address the most obvious aspect of the problem. They frequently miss edge cases, side effects, and long-term costs. The first solution should be treated as a HYPOTHESIS, not an answer.

7. **"If I can't find a solution, the problem is too hard."** Often the issue is search strategy, not problem difficulty. Switching search channels (people instead of documents, experiments instead of theory, adjacent domains instead of your domain) frequently unlocks stuck searches.

8. **"Solutions are things you find."** Sometimes the best solution is removing a constraint, redefining the problem, or deciding the problem doesn't need solving. These aren't "solutions" in the traditional sense but they resolve the situation.

9. **"I need to search alone."** Most people either search entirely alone (missing collective knowledge) or immediately ask others (never developing their own understanding). The optimal pattern is: form your own hypothesis first, THEN consult others to test and expand it.

10. **"All search channels are equally good."** Different channels have radically different signal-to-noise ratios for different problem types. Technical documentation is great for "how do I use X" and terrible for "should I use X." People are great for "what should I do" and unreliable for "what's the exact syntax."

---

## Step 4: The Procedure

```
SOLUTION SEARCH PROCEDURE
===========================

STEP 0: What kind of search is this?

Answer these THREE questions:

Q1: Can I state the problem in one specific sentence?
    → YES: Go to Q2.
    → NO: Go to SECTION P (Problem Clarification).

Q2: Have I solved this exact type of problem before?
    → YES: Go to SECTION R (Recall & Adapt).
    → SIMILAR BUT NOT EXACT: Go to Q3.
    → NO, THIS IS NEW TO ME: Go to Q3.

Q3: Is this a time-sensitive emergency (need answer in minutes/hours)?
    → YES: Go to SECTION E (Emergency Search).
    → NO: Go to SECTION S (Systematic Search).

After any section completes → Go to SECTION V (Verify Before Implementing).


================================================================
SECTION P: PROBLEM CLARIFICATION
(Use when you can't clearly state the problem)
================================================================

Step P1: SYMPTOM LIST
  Write down every observable symptom — things you can see,
  measure, or point to. Not interpretations. Not causes.
  Just what's happening.
  → Target: at least 5 symptoms. If fewer, ask someone else
    what they've noticed.
  → What you should see: A list of specific, observable facts.
    "Revenue is down 15%" not "the business is struggling."

Step P2: CONTRAST
  For each symptom, complete:
  "This is happening, but I expected __________ instead."
  → What you should see: The GAP between reality and
    expectation for each symptom.

Step P3: CLUSTER
  Do any symptoms seem related? Group them.
  - Same timeframe?
  - Same component/area/person?
  - One could cause another?
  → If you find clusters: The CLUSTER is your problem,
    not the individual symptoms.
  → If no clusters: You may have multiple independent
    problems. Pick the one with highest impact first.

Step P4: SINGLE SENTENCE
  Write ONE sentence: "The problem is that [specific thing]
  is [specific behavior] when it should be [specific
  expected behavior], and this matters because [specific
  consequence]."
  → Can you write this sentence?
    → YES: Go back to STEP 0, Q2 (you now have a clear
      problem).
    → NO: Your problem may be a GOAL, not a problem.
      Reframe as: "I want [X] but currently have [Y]."
      Then go to STEP 0, Q2.

================================================================
SECTION R: RECALL & ADAPT
(Use when you've solved this type before)
================================================================

Step R1: REMEMBER
  Write down: What did I do last time this happened?
  Be specific — not "I fixed it" but the actual steps.
  → What you should see: A concrete sequence of actions.

Step R2: MATCH CHECK
  Compare the current problem to the remembered one:
  (a) Same symptoms? (YES/NO)
  (b) Same context/environment? (YES/NO)
  (c) Same constraints? (YES/NO)
  → All YES: Apply the same solution. Go to SECTION V.
  → Any NO: List what's different. These differences are
    where the old solution might fail.

Step R3: ADAPT
  For each difference identified in R2:
  "Because [difference], I need to change [specific part]
   of the old solution to [specific modification]."
  → Can you make all needed modifications?
    → YES: Apply modified solution. Go to SECTION V.
    → NO: The differences are too large. The old solution
      is a starting REFERENCE, not the answer. Go to
      SECTION S, but bring your old solution as a baseline.

================================================================
SECTION E: EMERGENCY SEARCH
(Use when you need an answer in minutes to hours)
================================================================

Step E1: TRIAGE — Is this actually an emergency?
  (a) What happens if I do NOTHING for 24 hours?
  → THINGS GET MUCH WORSE: Confirmed emergency. Continue.
  → THINGS STAY THE SAME: Not an emergency. You have time.
     Go to SECTION S.
  → I DON'T KNOW: Assume emergency. Continue, but set a
     timer for 1 hour to reassess.

Step E2: STABILIZE BEFORE SOLVING
  Can you stop the bleeding without solving the problem?
  (Revert a change, turn something off, switch to a backup,
   put up a temporary fix, buy time)
  → YES: Do it NOW. Then proceed with more time.
  → NO: Continue to E3.

Step E3: FASTEST PATH TO AN ANSWER
  In this order, try each for no more than 10 minutes:
  (a) Do I already know a possible solution? (Even a guess.)
      → Write it down. Don't implement yet. Move to (b).
  (b) Is there ONE specific person who would know?
      → Contact them NOW. While waiting, move to (c).
  (c) Is the exact error/symptom searchable?
      → Search the exact message/symptom verbatim.
      → Found a match? → Apply it. Go to SECTION V.
  (d) None of the above worked in 10 minutes each?
      → Use your guess from (a). It's better than nothing.
      → Go to SECTION V.

Step E4: POST-EMERGENCY
  After the emergency is resolved:
  Write down what happened, what you did, and whether it
  worked. Then schedule time to do a proper SECTION S search
  for a robust solution. Emergency fixes are temporary.

================================================================
SECTION S: SYSTEMATIC SEARCH
(Use for non-emergency problems you haven't solved before)
================================================================

Step S1: DEFINE CRITERIA BEFORE SEARCHING
  Before looking at ANY solutions, write down:
  (a) MUST-HAVE: What must the solution do? (Hard
      requirements — any solution missing these is
      disqualified.)
  (b) NICE-TO-HAVE: What would be ideal but not required?
  (c) MUST-NOT: What must the solution NOT do? (Deal-
      breakers — side effects, costs, dependencies you
      can't accept.)
  → What you should see: A concrete checklist you can
    hold any candidate solution against.

Step S2: CLASSIFY THE PROBLEM
  Which of these best describes your situation?

  ┌─────────────────────────────────────┬──────────────┐
  │ Situation                           │ Go to        │
  ├─────────────────────────────────────┼──────────────┤
  │ "How do I do [specific thing]?"     │ Step S3-HOW  │
  │ "Why is [thing] happening?"         │ Step S3-WHY  │
  │ "Which [option] should I choose?"   │ Step S3-WHICH│
  │ "What should I do about [situation]"│ Step S3-WHAT │
  │ "Is there a better way to [thing]?" │ Step S3-BETTER│
  └─────────────────────────────────────┴──────────────┘

Step S3-HOW: PROCEDURAL SEARCH
  The answer is a set of steps someone has documented.
  Search order (try each before moving to next):
  (a) Official documentation for the specific tool/system
  (b) Search: "[exact thing] tutorial" or "[exact thing]
      how to"
  (c) Community forums specific to the domain (Stack
      Overflow for code, specific subreddits, industry
      forums)
  (d) Ask a person with direct experience
  → Found an answer?
    → YES: Go to Step S5.
    → NO after all four: Reframe. Are you asking the right
      HOW question? Maybe you're trying to do X when you
      should do Y. Go to Step S3-WHAT.

Step S3-WHY: DIAGNOSTIC SEARCH
  The answer is a root cause.
  (a) What changed? List everything different between
      "working" and "not working." (Time, environment,
      configuration, inputs, people, dependencies.)
  (b) For each change: "Could this change cause the
      symptom?"
      → YES for any: Test by reverting that change (if
        possible). Did the symptom disappear?
        → YES: You found the cause. Go to Step S5.
        → NO: Keep looking.
  (c) No changes found, or reverting didn't help:
      Search the exact symptom/error (verbatim, in quotes).
  (d) Still stuck: The cause may be a COMBINATION of
      factors. List your top 3 suspects. Test them in
      pairs. Go to Step S5 when found.

Step S3-WHICH: COMPARISON SEARCH
  The answer is a ranked selection from known options.
  (a) List ALL options you're aware of (minimum 3).
      → Fewer than 3? Search: "[problem type] options" or
        "[problem type] alternatives" to find more.
  (b) Score each option against your MUST-HAVE list (S1a).
      Disqualify any that fail a must-have.
  (c) Score survivors against MUST-NOT list (S1c).
      Disqualify any that violate a deal-breaker.
  (d) Score remaining against NICE-TO-HAVE list (S1b).
  (e) Pick the top scorer. Go to Step S5.
  → If all options were disqualified: Your requirements
    may be contradictory. Go to Step S4-REFRAME.

Step S3-WHAT: STRATEGIC SEARCH
  The answer requires framing before searching.
  (a) List all approaches you can think of (at least 3).
      Techniques to generate more:
      - What would an expert in this area do?
      - What would someone from a DIFFERENT field do?
      - What if I removed the biggest constraint?
      - What if I did nothing — what happens naturally?
      - What's the opposite of my first instinct?
  (b) For each approach: "What's the best realistic
      outcome?" and "What's the worst realistic outcome?"
  (c) Eliminate any where worst-case is unacceptable.
  (d) For survivors: search for evidence that this approach
      has worked for similar problems.
  (e) Pick the approach with best evidence. Go to Step S5.

Step S3-BETTER: OPTIMIZATION SEARCH
  You have a working solution but suspect a better one exists.
  (a) What specifically is unsatisfying about the current
      solution? (Speed, cost, quality, complexity,
      maintenance burden, user experience?)
  (b) Search for how others solve the specific PAIN POINT,
      not the original problem.
  (c) Found alternatives?
      → YES: Compare against current solution on the
        specific dimension you're optimizing.
        → Better? Go to Step S5.
        → Not clearly better? Keep current. The search
          cost of continuing likely exceeds the gain.
      → NO: Your current solution may be near-optimal
        for your constraints. Accept it.

Step S4-REFRAME: YOUR QUESTION MAY BE WRONG
  If you're stuck after exhausting the search paths above:
  (a) Write down the problem again from scratch. Don't
      look at your earlier framing.
  (b) Compare old framing vs. new framing. Different?
      → YES: Search using the new framing. Go back to S2.
      → NO: Continue to (c).
  (c) Ask: "What ASSUMPTION am I making that might be
      false?" Write down 3 assumptions.
      For each: "If this assumption were false, what
      would the solution look like?"
      → Did this produce a new direction?
        → YES: Search in that direction. Go back to S2.
        → NO: Go to (d).
  (d) Ask: "Does this problem actually need to be solved?"
      What happens if you live with it?
      → Consequences are acceptable: STOP. The solution is
        "don't solve this." This is a valid outcome.
      → Consequences are not acceptable: Escalate. Find
        an expert (Step S6).

Step S5: EVALUATE THE CANDIDATE SOLUTION
  You have a candidate. Before implementing, check:
  (a) Does it meet ALL must-haves from S1a? (YES/NO)
      → NO: Reject. Go back to where you were.
  (b) Does it violate any must-nots from S1c? (YES/NO)
      → YES: Reject. Go back.
  (c) Do you understand WHY it works? (YES/NO)
      → NO: Search for an explanation. Implementing a
        solution you don't understand invites future
        problems. (Exception: emergency — implement now,
        understand later.)
  (d) Has someone else used this successfully for a
      similar problem? (YES/NO/CAN'T TELL)
      → YES: Strong candidate. Go to SECTION V.
      → NO: Weak candidate. Look for alternatives unless
        you're in emergency mode.
      → CAN'T TELL: Treat as weak. Look briefly for
        alternatives (15 min max), then proceed.

Step S6: ESCALATE — HUMAN EXPERT SEARCH
  You need a person, not a document.
  (a) Who has DIRECT experience with this type of problem?
      (Not "smart person" — specifically this problem type.)
  (b) Search order for finding the right person:
      - Your immediate network (colleagues, friends)
      - Professional communities (forums, Slack groups,
        professional associations)
      - Paid experts (consultants, coaches, specialists)
  (c) When you contact them, provide:
      - The specific problem (your P4 sentence)
      - What you've already tried
      - What your constraints are (S1)
      Ask: "Have you seen this before? What would you do?"
  (d) Got advice?
      → YES: Treat it as a candidate. Go to Step S5.
      → NO/unavailable: You may be in pioneer territory.
        Go to Step S7.

Step S7: PIONEER MODE — NO KNOWN SOLUTION EXISTS
  You've exhausted known solutions. Time to invent.
  (a) Break the problem into the smallest possible
      sub-problems.
  (b) For each sub-problem: does a known solution exist
      for THAT? (Run SECTION S for each sub-problem.)
  (c) Can you combine known sub-solutions into a novel
      overall solution?
      → YES: You've assembled a novel solution from
        known parts. Go to SECTION V.
  (d) For sub-problems with no known solution:
      Design the smallest possible experiment to learn
      ONE thing. Run it. Use the result to inform
      the next experiment.
  (e) Repeat (d) until you have a working approach.
      This may take multiple cycles. Each cycle should
      be timeboxed (decide the timebox before starting).

→ Any solution found → Go to SECTION V.


================================================================
SECTION V: VERIFY BEFORE IMPLEMENTING
(Use after finding any candidate solution)
================================================================

Step V1: REVERSIBILITY CHECK
  If this solution is wrong, can I undo it?
  → EASILY (< 1 hour, no side effects): Implement it.
     Monitor for 24 hours. Done.
  → WITH EFFORT (hours to days, some side effects):
     Continue to V2.
  → NOT AT ALL (permanent change): Continue to V2
     AND V3.

Step V2: SECOND OPINION
  Describe the problem AND your proposed solution to
  one other person. Ask:
  "What am I missing? What could go wrong?"
  → They raised concerns?
    → YES: Address each concern. Can you address them all?
      → YES: Implement.
      → NO: The unaddressed concern is a new problem.
        Can you live with it? If yes, implement.
        If no, search for a solution that doesn't
        have this problem (go back to your search section).
  → NO concerns raised: Implement.

Step V3: SMALL TEST (for irreversible solutions only)
  Can you test the solution on a SMALL scale first?
  (A subset of data, one user, one department, a pilot
  project, a prototype, a simulation?)
  → YES: Run the small test. Did it work?
    → YES: Scale up. Implement fully.
    → NO: What went wrong? Fix it and retest, or
      go back to your search section.
  → NO, IT'S ALL-OR-NOTHING:
    → Is there a way to make it reversible?
      (Backup, snapshot, rollback plan, parallel run?)
      → YES: Create the rollback plan first.
        Then implement.
      → NO: Accept the risk explicitly: "I am implementing
        an irreversible solution. If it fails, [specific
        consequence] will happen and I accept that."
        Then implement.
```

---

## Step 5: Failure Modes & Warnings

**FAILURE MODE 1: "I jumped straight to SECTION S without doing SECTION P"**
- **How to recognize**: You're searching for solutions but getting irrelevant results. Nothing quite fits. You keep refining your search terms.
- **What's happening**: Your problem isn't well-defined. You're searching for a solution to the wrong problem.
- **Fix**: Stop searching. Go to SECTION P. Spend 15 minutes clarifying the problem before spending hours searching for solutions.

**FAILURE MODE 2: "I found a solution in the first 5 minutes and stopped"**
- **How to recognize**: You Googled it, found a Stack Overflow answer or blog post, and started implementing immediately.
- **What's happening**: First solutions are hypotheses, not answers. The first result is optimized for search ranking, not for your specific context.
- **Fix**: Check V1. If easily reversible, fine — try it. If not easily reversible, spend at least 15 more minutes looking for alternatives before committing.

**FAILURE MODE 3: "I've been searching for hours and have 20 tabs open"**
- **How to recognize**: You're reading more and more but getting less and less clarity. Each new source partially contradicts the last.
- **What's happening**: You've passed the point of diminishing returns. More search is making you MORE confused, not less.
- **Fix**: Close all tabs. From memory alone, write down the top 2-3 candidates. If you can't remember them, they weren't good. Evaluate only those 2-3 against your criteria (S1). Pick one. Implement.

**FAILURE MODE 4: "I keep searching in the same channel"**
- **How to recognize**: You've been Googling for an hour. Or you've asked 5 people. Or you've read 3 books. All from the same type of source.
- **What's happening**: Different channels find different solutions. If one channel isn't working, it's not because you haven't searched hard enough — it's because the answer isn't in that channel.
- **Fix**: Switch channels completely. If you've been searching documentation, ask a person. If you've been asking people, try experimenting. If you've been theorizing, try the most basic thing and observe what happens.

**FAILURE MODE 5: "The solution works but I don't know why"**
- **How to recognize**: You followed instructions and the problem went away, but you couldn't explain what the solution does.
- **What's happening**: You've applied a black-box fix. It might work now and break later, or it might have side effects you can't see.
- **Fix**: For LOW-stakes problems: accept it, move on. For HIGH-stakes: spend time understanding the mechanism BEFORE relying on it.

**FAILURE MODE 6: "I solved it but the problem came back"**
- **How to recognize**: The same or similar problem reappears within days or weeks.
- **What's happening**: You addressed a symptom, not the root cause.
- **Fix**: Go to S3-WHY. Specifically: what changed between "fixed" and "broken again"? If nothing changed, your solution was never actually solving the root cause. Go deeper.

**FAILURE MODE 7: "I'm stuck on SECTION P — I can't clarify the problem"**
- **How to recognize**: You've been trying to write the P4 sentence for 30 minutes and keep failing.
- **What's happening**: You may have a GOAL, not a problem. Or you may have multiple problems tangled together.
- **Fix**: Skip P4. Instead, list the 3 most concrete symptoms from P1 and treat EACH as a separate problem. Solve the easiest one first. Often, solving one reveals or resolves the others.

---

## Step 6: Validation Check

| Criterion | Status |
|---|---|
| Every step is a concrete action | PASS — all steps produce written output or a routing decision |
| All decision points are binary or explicit multiple choice | PASS — YES/NO or table routing throughout |
| No jargon without definition | PASS — satisficing, channels, signal-to-noise defined in context |
| Every path leads to a concrete output | PASS — all paths terminate in SECTION V or explicit "stop" |
| No dead ends or loops | PASS — S4-REFRAME can loop but with explicit escalation exit (S4d) |
| Followable without domain expertise | PASS — domain-agnostic throughout |
| "What you should see" markers included | PASS — present at key steps |

---

## QUICK REFERENCE CARDS

**The Search Channel Priority Table:**

| Problem Type | Try First | Try Second | Try Third |
|---|---|---|---|
| "How do I..." | Documentation | Community forum | Person with experience |
| "Why is this..." | What changed? | Exact error search | Experimentation |
| "Which should I..." | Criteria list → compare | Expert opinion | Pilot/experiment |
| "What should I..." | Generate options | Evidence search | Expert strategy |
| "Is there better..." | Specific pain point search | Adjacent domain search | Accept current |

**The 5-Minute Decision Tree:**

```
Can I state the problem clearly?
├── NO → Clarify first (SECTION P)
└── YES → Have I solved this before?
    ├── YES → Recall & adapt (SECTION R)
    └── NO → Is it an emergency?
        ├── YES → Stabilize, then fast-path (SECTION E)
        └── NO → Define criteria, classify, search (SECTION S)
```

**When To Stop Searching:**

You have ENOUGH when any of these is true:
1. You found a solution that meets all must-haves and no must-nots
2. You've found the same answer from 3+ independent sources
3. Two more search attempts produced nothing new
4. An expert with direct experience endorsed a candidate
5. You've exceeded your time budget and have at least one candidate

---

## COMMON MISTAKES

1. **Searching before defining the problem.** The most common and most costly mistake. A clear problem statement cuts search time by 50% or more because you stop finding irrelevant solutions.

2. **Not defining evaluation criteria before searching.** Without criteria, you evaluate solutions by gut feel, which is dominated by recency bias and fluency bias.

3. **Staying in one search channel too long.** If Google hasn't helped in 20 minutes, another 20 minutes of Googling won't help either. Switch to asking a person, running an experiment, or reframing the problem.

4. **Treating the first working solution as final.** First solutions address the obvious parts. They regularly miss edge cases, have hidden costs, or solve only the surface layer.

5. **Searching for the perfect solution when a good-enough one is available.** Perfectionism in solution search has steep costs. If the problem is reversible and the stakes are moderate, the first good-enough answer is the right answer.

6. **Never escalating to human experts.** Documentation and search engines are great for well-documented problems. For novel, complex, or high-stakes problems, a 15-minute conversation with the right expert is worth 10 hours of solo searching.

7. **Conflating "I can't find a solution" with "no solution exists."** Stuck usually means wrong search strategy, not impossible problem. The fix is to change HOW you're searching, not to give up.

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **Genuine expertise**: If you've solved this exact type of problem 50+ times, your intuition is calibrated. Skip the procedure and act. But verify after (SECTION V still applies).
- **Trivially simple problems**: If the problem and solution are both obvious, no procedure needed.
- **You need creativity, not search**: If the problem requires invention, this procedure is too convergent. Use divergent methods first, then use this procedure to evaluate candidates.
- **Emotional problems**: If the "problem" is actually a feeling, the solution isn't found through search — it's found through reflection, conversation, or behavioral change.
- **The problem is political, not technical**: If the real blocker is a person, a relationship, or an organizational dynamic, no amount of solution search helps.

---

## WORKED EXAMPLES

### Example 1: Software Bug (S3-WHY path)

**Problem**: "Users report the checkout page shows a blank screen after clicking 'Pay'."

- **P4 sentence**: "The checkout page renders blank after payment button click when it should show a confirmation page, and this is blocking all purchases."
- **Step 0**: Clear problem → Haven't seen this exact bug → Not emergency (workaround exists) → **SECTION S**
- **S1 criteria**: Must-have: page renders correctly. Must-not: break other payment flows.
- **S2 classify**: "Why is this happening?" → **S3-WHY**
- **S3-WHY (a)**: What changed? Deployed new payment SDK yesterday.
- **S3-WHY (b)**: Could this cause it? Yes. Revert the SDK → page works again. **Found the cause.**
- **S5**: Solution is "revert SDK or fix compatibility." Meets criteria.
- **V1**: Easily reversible. Implement the revert, then debug the SDK at leisure.

### Example 2: Career Decision (S3-WHAT path)

**Problem**: "I've been in my role for 3 years and feel stagnant."

- **Section P**: Symptoms — same tasks, no new challenges, peers advancing, boredom.
- **P4**: "I want career growth but my current role offers no advancement path, and this matters because I'm losing motivation and marketability."
- **S1 criteria**: Must-have: more challenge, new skills. Must-not: pay cut >20%, require relocation.
- **S2**: "What should I do?" → **S3-WHAT**
- **S3-WHAT (a)**: Options — negotiate new responsibilities, switch teams, switch companies, start freelancing, go back to school.
- **S3-WHAT (c)**: Eliminate school (worst case: 2 years + debt).
- **S3-WHAT (d)**: Evidence → switching companies yields 10-20% raises.
- **V2**: Mentor confirms.

### Example 3: Pioneer Territory (S7 path)

**Problem**: "I want to build a tool that detects when house plants need water based on soil color from a phone camera."

- **S3-HOW**: No existing solutions using camera + soil color.
- **S6**: Plant science forum → no one has done this.
- **S7**: Sub-problems: capture image, detect soil region, measure color, correlate color to moisture, alert user. Known solutions for all except the correlation. Weekend experiment shows color-moisture correlation is strong. Build with lookup table. Ship it.

---

*This procedure has not been validated by domain experts. It is a structured thinking aid, not a substitute for professional expertise in domains where wrong solutions carry serious consequences.*
