# Decision Procedure — How to Act on a Guess

**Date**: 2026-01-31
**Input**: continue with what is logically next (sequel to "what it means to guess")

---

# HOW TO ACT ON A GUESS — DECISION PROCEDURE

## Step 1: Decision Dimensions

You have a guess. Now what? These dimensions determine the right next move.

| # | Dimension | Description | Why It Matters |
|---|-----------|-------------|----------------|
| 1 | **Guess quality** | How much evidence and reasoning supports the guess? | A decomposed Fermi estimate deserves different treatment than a coin-flip hunch |
| 2 | **Action required** | Does acting on this guess commit resources, change state, or affect others? | Some guesses are just beliefs you hold; others trigger irreversible actions |
| 3 | **Testability** | Can you design a cheap test that would confirm or refute the guess? | If yes, test before acting. If no, you're stuck with the guess as-is |
| 4 | **Cost of being wrong** | What do you lose if the guess is wrong and you acted on it? | Asymmetric costs change everything — some wrong guesses cost nothing, others are catastrophic |
| 5 | **Cost of delay** | What do you lose by waiting to gather more information instead of acting now? | Sometimes the cost of not deciding exceeds the cost of deciding wrong |
| 6 | **Updatability** | If you act now, can you change course later when new information arrives? | Updatable actions tolerate worse guesses |
| 7 | **Competing guesses** | Do you have alternative guesses that point in different directions? | A single guess feels like knowledge. Two competing guesses remind you it's uncertain |
| 8 | **Confidence-action mismatch** | Is the size of the action proportional to the quality of the guess? | Betting your life savings on a hunch is a mismatch; buying a $5 lottery ticket on a hunch isn't |
| 9 | **Information decay** | Does the guess become less valid over time? | A guess about today's weather is worthless tomorrow; a guess about human nature holds for decades |
| 10 | **Dependency chain** | Do other decisions depend on this guess being right? | One bad guess that feeds ten downstream decisions is more dangerous than one bad guess in isolation |

---

## Step 2: Options Within Each Dimension

**Guess quality**: Pure hunch / Anchored estimate / Reasoned inference / Evidence-backed estimate / Near-certain

**Action required**: No action (just a belief) / Small reversible action / Medium commitment / Large irreversible commitment

**Testability**: Easily testable (minutes/free) / Testable with effort (hours/some cost) / Testable with significant investment / Untestable

**Cost of being wrong**: Zero / Minor inconvenience / Moderate loss / Major loss / Catastrophic

**Cost of delay**: None / Opportunity fades slowly / Opportunity fades fast / Window closes permanently

**Updatability**: Fully updatable (can pivot anytime) / Partially updatable (some sunk cost) / Locked in once committed

**Competing guesses**: No alternatives / One alternative / Multiple alternatives / Contradictory evidence both ways

**Confidence-action mismatch**: Proportional / Slightly mismatched / Severely mismatched

**Information decay**: Stable (guess stays valid indefinitely) / Moderate (valid for weeks/months) / Perishable (valid for hours/days)

**Dependency chain**: Standalone guess / Feeds 1-2 other decisions / Foundation for many decisions

---

## Step 3: Hidden Assumptions About Acting on Guesses

1. **"I should wait until I'm sure."** Certainty is expensive and sometimes impossible. Every moment spent pursuing certainty has a cost. The question isn't "am I sure?" but "is acting now better than waiting?"

2. **"If my guess is probably right, I should go all-in."** Probable doesn't mean certain. A 70% guess means it's wrong 30% of the time. Size your action to survive being wrong.

3. **"I should treat my guess the same as someone else's fact."** Your guess hasn't been tested. Treat it as a hypothesis, not a conclusion — act on it provisionally, with checkpoints.

4. **"Testing a guess is always worth it."** Testing has costs. If the stakes are low enough, acting on the untested guess and seeing what happens IS the most efficient test.

5. **"Once I act, I'm committed."** Many actions are more reversible than they feel in the moment. Check whether you're actually locked in or just telling yourself you are.

6. **"A wrong guess means I failed."** Wrong guesses that were well-constructed and proportionally acted on are not failures — they're information. The failure is acting disproportionately on a bad guess, or never updating.

7. **"I need to decide right now."** Urgency is often manufactured — by others, by anxiety, or by framing. Check: what actually happens if you decide tomorrow?

---

## Step 4: The Procedure

```
HOW TO ACT ON A GUESS — DECISION PROCEDURE
===========================================

PURPOSE: You have a guess (from the "What It Means to Guess" procedure
or from anywhere else). This procedure tells you what to do with it:
act, test, refine, wait, or abandon.


STEP 0: State the guess and the action.

  Write down TWO things:
  1. THE GUESS: "I believe ___"
  2. THE ACTION: "And therefore I would ___"

  If you can't state the action → you don't have a decision.
  You just have a belief. Hold the belief loosely and stop here.

  If you can state both → Go to Step 1.


STEP 1: Can you test this guess cheaply?

  "Cheaply" means: less than 10% of the cost/time/effort of
  the full action.

  YES → Go to SECTION A (Test First).
  NO  → Go to Step 2.


STEP 2: What happens if you're WRONG?

  Pick one:

  A) "Nothing bad. I lose a little time or money."
     → Go to SECTION B (Just Act).

  B) "Something moderately bad. I waste real resources or
      miss a better option."
     → Go to SECTION C (Act Cautiously).

  C) "Something seriously bad. Real harm, major loss,
      or irreversible damage."
     → Go to SECTION D (Protect First).


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION A: Test First
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  You can test the guess before committing. Do it.

  Step A1: Design the SMALLEST test.
    Ask: "What's the cheapest thing I could do or observe
    that would make me MORE or LESS confident in this guess?"

    Examples:
    - Guess: "This restaurant is good" → Test: Check 3 reviews
    - Guess: "This approach will work" → Test: Try it on one
      small case first
    - Guess: "They'll say yes" → Test: Ask a related,
      lower-stakes question first

  Step A2: Define what you expect to see.
    BEFORE running the test, write down:
    - "If my guess is RIGHT, I expect to see ___"
    - "If my guess is WRONG, I expect to see ___"

    ⚠ WARNING: If you can't define what "wrong" looks like,
    the test is useless. Redesign it or skip to Step 2.

  Step A3: Run the test.

  Step A4: Interpret the result.
    Did you see what you expected for RIGHT or WRONG?
    → RIGHT: Your guess is now an informed guess. Return to
      Step 2 and act on it with increased confidence.
    → WRONG: Your guess was wrong. Update it or abandon it.
      Go to SECTION E (Update or Abandon).
    → AMBIGUOUS: The test didn't help. You're back where
      you started. Go to Step 2 and act on what you have.

  → DONE (after completing the next section)


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION B: Just Act (Low Stakes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  The cost of being wrong is low. Act on the guess.

  Step B1: Act.
    Do the thing. Don't overthink it.

  Step B2: Note what happens.
    Did the guess turn out right or wrong?
    → RIGHT: File this away. Your guessing in this domain
      may be decent.
    → WRONG: File this away too. No harm done, but track it.
      If you're consistently wrong in this domain, your
      guessing model needs updating.

  → DONE


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION C: Act Cautiously (Moderate Stakes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  The cost of being wrong is real but survivable.

  Step C1: Size the action to the guess quality.

    GUESS QUALITY          → ACTION SIZE
    ─────────────────────────────────────────
    Pure hunch             → Smallest possible version
    Reasoned inference     → Moderate commitment
    Evidence-backed        → Full commitment (but with C2)

  Step C2: Set a CHECKPOINT.
    Before acting, decide: "I will check whether this guess
    was right after ___ [time/event/milestone]."
    Write down the checkpoint. Be specific.

    Example: "I'll try this approach for one week. On Friday,
    I'll check whether it's working. If not, I'll switch."

  Step C3: Define your EXIT CRITERIA.
    "I will STOP and change course if I see ___."
    Write this down BEFORE you start, while you're still
    objective. Once you're invested, you'll resist quitting.

  Step C4: Act.
    Execute the sized-down action from C1.

  Step C5: At the checkpoint, evaluate honestly.
    Did you see your exit criteria? If yes → SECTION E.
    Are things on track? If yes → continue or expand.
    Ambiguous? → Run another checkpoint. Don't expand yet.

  → DONE


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION D: Protect First (High Stakes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  The cost of being wrong is severe.

  Step D1: Can you WAIT?
    → YES (no deadline, or deadline is far): Go to D2.
    → NO (must act now): Go to D3.

  Step D2 (Can wait): Gather more information.
    What is the single most valuable piece of information
    you're missing? Go get it. Repeat until one of:
    - Your guess becomes evidence-backed → Go to Section C
    - You run out of accessible information → Go to D3
    - A deadline arrives → Go to D3

  Step D3 (Must act now): Apply the MINIMAX rule.
    Don't act on the MOST LIKELY outcome.
    Act on the outcome you can MOST SURVIVE if wrong.

    Ask: "If my guess is wrong, which action leaves me in
    the best position?"

    Choose that action, even if it's not optimal for the
    case where you're right.

  Step D4: Can you HEDGE?
    Is there an action that partially succeeds whether the
    guess is right OR wrong?
    → YES: Take the hedge. Examples:
      - Diversify instead of concentrating
      - Buy insurance / options / reversibility
      - Do the reversible part now, delay the irreversible part
    → NO: Proceed with D3's answer.

  Step D5: Get a SECOND OPINION.
    Before acting, find ONE person who:
    - Has no stake in the outcome
    - Has experience in this domain
    - Doesn't know your guess yet
    Ask them what THEY would guess. Compare.
    If they agree → more confidence. Act via Section C.
    If they disagree → you have competing guesses.
    Go to SECTION F.

  → DONE


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION E: Update or Abandon the Guess
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Your test failed or your checkpoint showed problems.

  Step E1: What specifically was wrong?
    Not "it didn't work" — WHAT didn't match expectations?
    Write it down in one sentence.

  Step E2: Does the new information NARROW or DESTROY
    your guess?

    NARROW (the guess was partly right):
    → Revise the guess. "My original guess was [X]. The
      evidence now suggests [Y]. I'm updating to [Z]."
    → Return to Step 0 with the updated guess.

    DESTROY (the guess was fundamentally wrong):
    → Abandon it. Generate a NEW guess that accounts for
      what you learned. Return to Step 0.

    ⚠ WARNING: If you've updated the same guess more than
    3 times and it keeps failing → your model of this
    domain is broken. Stop guessing. Seek someone who
    actually knows.

  → DONE


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION F: Competing Guesses
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  You have two or more guesses pointing in different
  directions.

  Step F1: Can you test WHICH guess is right?
    → YES: Design a test that would distinguish between
      them. Go to Section A.
    → NO: Continue to F2.

  Step F2: Do the guesses lead to DIFFERENT actions?
    → NO: If both guesses lead to the same action, it
      doesn't matter which is right. Act. You're done.
    → YES: Continue to F3.

  Step F3: Is there an action that works REASONABLY WELL
    under both guesses?
    → YES: Take it. This is the robust choice.
    → NO: Continue to F4.

  Step F4: Which guess has BETTER evidence?
    List the evidence for each. Whichever has more
    specific, concrete, recent, and relevant evidence wins.
    If truly equal → flip a coin. Seriously. When evidence
    is equal, deliberation adds no value. Decide and track
    the result so you learn for next time.

  → DONE
```

---

## Step 5: Failure Modes

| # | Failure Mode | How to Recognize It | What to Do Instead |
|---|---|---|---|
| 1 | **Analysis paralysis** | You keep gathering information and never act. Your checkpoints keep getting delayed. You've been "about to decide" for days/weeks. | Set a hard deadline. "I will decide by [date] with whatever I have." Act on the best guess available at that point. |
| 2 | **Sunk cost escalation** | Your guess was wrong, but you keep investing because you already invested. "I've come this far..." | Check your exit criteria (C3). If they're met, exit. The money/time is gone regardless. |
| 3 | **Premature commitment** | You acted on a hunch with the force of a certainty. Full resources committed on minimal evidence. | Match action size to guess quality (C1). If you catch yourself having over-committed, can you partially reverse? |
| 4 | **Confirmation bias in testing** | You designed a test that can only confirm your guess, not refute it. Or you interpreted ambiguous results as confirmation. | Before testing, write down what WRONG looks like (A2). If you can't, your test is rigged. |
| 5 | **Never updating** | You acted on a guess months ago and never checked whether it was right. You're still operating on an unchecked assumption. | Set checkpoints at the time of action, not after. Review: "What am I currently doing based on an untested guess?" |
| 6 | **False dilemma** | You think you must choose between two options when a third option, hedge, or delay is available. | Always ask: "Is there a third option? Can I do a partial version? Can I wait?" before committing. |
| 7 | **Outsourcing your guess** | You asked an expert and treated their guess as fact. Experts guess too — they're just (sometimes) better at it. | Treat expert input as a higher-quality guess, not as certainty. Especially if the expert hasn't seen your specific situation. |
| 8 | **Abandoning good guesses too early** | One data point went wrong and you scrapped everything. But noise exists — single failures don't always invalidate a guess. | Distinguish signal from noise. Ask: "Would I expect this failure even if my guess were right?" If yes, don't abandon yet. |

---

## Step 6: Validation

- Step 0: Concrete (write down two things). No interpretation needed. **PASS**
- Step 1: Binary question with clear threshold ("less than 10%"). **PASS**
- Step 2: Three-way choice with concrete descriptions. **PASS**
- Sections A-F: All steps are actions (write, design, run, ask, check). No "consider" or "reflect." **PASS**
- Section C checkpoint system: Specific, pre-committed, with exit criteria. **PASS**
- Section D minimax: Concrete reframe from "most likely" to "most survivable." **PASS**
- Section F tiebreaker: Terminates even when evidence is equal (coin flip). No infinite loops. **PASS**
- All paths reach DONE. **PASS**

---

## Quick Reference Cards

**THE ACTION LADDER**
```
Guess quality:     hunch → estimate → inference → evidence-backed
                     ↓         ↓          ↓             ↓
Match action:    smallest   moderate    full      full + hedge
                 possible   version     version   removed
```

**THE THREE QUESTIONS BEFORE ACTING**
```
1. Can I test this cheaply?     → YES: Test first
2. Can I survive being wrong?   → YES: Act, with checkpoints
3. Can I wait for more info?    → YES: Wait, with deadline
   All three NO?                → Act on safest option
```

**THE UPDATE RULE**
```
Evidence confirms   → Continue, maybe expand
Evidence ambiguous  → Continue at same size, add checkpoint
Evidence contradicts → Shrink or stop. Update guess.
3+ failed updates   → Your model is broken. Get help.
```

---

## Common Mistakes

1. Treating "I don't know" as a reason not to act — inaction is also a choice, with its own consequences
2. Waiting for certainty in domains where certainty doesn't exist (predictions, preferences, novel situations)
3. Matching the size of the action to the strength of the feeling rather than the strength of the evidence
4. Skipping the checkpoint — committing and never looking back to see if the guess was right
5. Designing tests that can only confirm, never refute (asking leading questions, cherry-picking metrics)
6. Abandoning a guess because of one failure in a noisy domain, or holding a guess despite repeated failures in a clear domain

---

## When to Override This Procedure

- **Emergency/safety**: Skip to Section D, Step D3 immediately. Act on safest option. Analyze later.
- **Domain expertise**: If you genuinely have deep expertise (10,000+ hours, fast feedback, demonstrated calibration), your intuitions are more trustworthy than this flowchart. Trust them — but still set checkpoints.
- **Trivial decisions**: If the total cost of ALL outcomes is less than the cost of running this procedure, just pick one. Don't optimize what doesn't matter.
- **Ethical decisions**: This procedure optimizes for outcomes. If the action is wrong regardless of whether the guess is right (lying, cheating, harming), no amount of good guessing justifies it.

---

## Worked Examples

### Example 1: "I think this job candidate is good"

**Step 0**: Guess: "This candidate will perform well." Action: "Extend an offer."
**Step 1**: Can I test cheaply? YES — reference checks, a work sample test, a second interview. → Section A.
**A1**: Smallest test: Ask for a work sample relevant to the actual role.
**A2**: If right: work sample shows competence, clear communication, meets deadline. If wrong: misses requirements, sloppy, late.
**A3**: Run the test.
**A4**: Result matches "right" predictions → Guess upgraded. Return to Step 2.
**Step 2**: Cost of being wrong? Moderate — bad hire costs time and money but is fixable. → Section C.
**C1**: Guess is now evidence-backed → full commitment reasonable.
**C2**: Checkpoint: 90-day review.
**C3**: Exit criteria: If after 90 days they're below expectations on core responsibilities.
**C4**: Extend offer.

### Example 2: "I think the market will go up"

**Step 0**: Guess: "The stock market will rise this year." Action: "Invest heavily."
**Step 1**: Can I test cheaply? NO — markets can't be cheaply pre-tested.
**Step 2**: Cost of being wrong? Serious — could lose significant money. → Section D.
**D1**: Can I wait? No hard deadline, but delay has opportunity cost. → D2.
**D2**: Most valuable missing info: I don't actually have any edge over the market. Gathering more info won't help because I'm not a professional. → D3.
**D3**: Minimax: If wrong about the market going up, what action survives? Diversified index investment — captures upside if right, limits downside if wrong.
**D4**: Hedge? Yes — invest a portion now, dollar-cost-average the rest over months.
**D5**: Second opinion: Any honest financial advisor would say "you can't predict the market, diversify." Confirms the hedge approach.

### Example 3: "I think my partner is upset with me"

**Step 0**: Guess: "They're upset." Action: "Bring it up and address it."
**Step 1**: Can I test cheaply? YES — ask. → Section A.
**A1**: Smallest test: "Hey, is everything okay between us?"
**A2**: If right: they'll confirm or show relief at being asked. If wrong: genuine confusion at the question.
**A3**: Ask.
**A4**: They say "actually, yeah, something's been bothering me." → Guess confirmed. But now you don't need to guess anymore — you can have an actual conversation.

---

*Validation status: This procedure has not been validated by domain experts.*
