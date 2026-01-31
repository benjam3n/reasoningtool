# Decision Procedure — What It Means to Guess

**Date**: 2026-01-31
**Input**: what it means to guess

---

# WHAT IT MEANS TO GUESS — DECISION PROCEDURE

## Step 1: Decision Dimensions

What factors determine whether a guess is warranted, what kind of guess it is, and whether it's a good one?

| # | Dimension | Description | Why It Matters |
|---|-----------|-------------|----------------|
| 1 | **Information available** | How much do you actually know about the thing you're guessing about? | A guess with 80% of the information is fundamentally different from a guess with 5% |
| 2 | **Stakes** | What happens if the guess is wrong? | Guessing what to eat for lunch vs. guessing whether a bridge is safe |
| 3 | **Reversibility** | Can you undo the consequences of a wrong guess? | Irreversible guesses demand more caution |
| 4 | **Time pressure** | How long can you delay before you must act? | Sometimes guessing now beats knowing later |
| 5 | **Cost of acquiring more information** | How hard is it to stop guessing and start knowing? | If you can just look it up, a guess is laziness. If you can't, a guess is necessary |
| 6 | **Type of unknown** | Is the unknown a fact, a prediction, a preference, or a category? | Each type of guess has different validity criteria |
| 7 | **Base rate awareness** | Do you know how common the thing you're guessing about is? | Most bad guesses ignore base rates |
| 8 | **Confidence calibration** | Do you know how good you are at guessing in this domain? | People who think they're guessing are sometimes knowing; people who think they're knowing are sometimes guessing |
| 9 | **Number of options** | Are you choosing between 2 things or 2,000? | Guess quality degrades with option count unless you have filtering criteria |
| 10 | **Feedback availability** | Will you find out if your guess was right? | Guesses without feedback can't improve |
| 11 | **Social context** | Are you guessing alone or in front of others? Does someone expect an answer? | Social pressure produces premature guesses |
| 12 | **Anchoring exposure** | Have you been exposed to a number, example, or suggestion before guessing? | Most people don't realize when their "guess" is just an anchor echo |

---

## Step 2: Options Within Each Dimension

**Information available**: None / Fragments / Partial pattern / Most pieces / Nearly complete

**Stakes**: Trivial / Moderate / Significant / Catastrophic

**Reversibility**: Freely reversible / Costly to reverse / Irreversible

**Time pressure**: No deadline / Soft deadline / Hard deadline / Immediate

**Cost of more info**: Free (just look) / Cheap (ask someone) / Moderate (research) / Expensive (experiment) / Impossible (unknowable)

**Type of unknown**:
- **Fact-guess**: "What year was this built?" — there is a right answer you don't have
- **Prediction-guess**: "Will it rain tomorrow?" — the answer doesn't exist yet
- **Preference-guess**: "Will they like this?" — the answer depends on someone else's internals
- **Category-guess**: "Is this a scam or legitimate?" — you're classifying something ambiguous
- **Estimation-guess**: "How many are there?" — you're approximating a quantity

**Base rate awareness**: Unknown / Vaguely known / Well-known

**Confidence calibration**: Uncalibrated / Somewhat calibrated / Well-calibrated

**Number of options**: Binary / Small set (3-7) / Large set (8+) / Continuous range

**Feedback availability**: Immediate / Delayed / Never

**Social context**: Private / Low-stakes social / High-stakes social (job interview, courtroom)

**Anchoring exposure**: None noticed / Anchor present / Multiple competing anchors

---

## Step 3: Hidden Assumptions People Make About Guessing

1. **"A guess is the opposite of knowing."** Wrong. Guessing and knowing are on a continuum. Every "known" thing was once a guess that survived testing. Every guess contains some knowledge — even a "random" guess uses implicit categories.

2. **"My gut feeling is either reliable or unreliable."** It depends on the domain. Gut feelings in domains with fast feedback and repeated practice (chess, driving) are often better than analysis. Gut feelings in domains with slow/no feedback (stock picking, hiring) are often worse than chance.

3. **"I should avoid guessing."** Sometimes guessing IS the right move. When information is expensive and stakes are low, guessing is rational. When time pressure is high, the best available guess beats no action.

4. **"A confident guess is better than an uncertain one."** Confidence is about you, not about the guess. Uncertain people with good base rates outperform confident people with bad models.

5. **"If I think hard enough, I'll stop guessing and start knowing."** Thinking without new information just refines the guess — it doesn't convert it into knowledge. At some point you're just rearranging the same uncertainty.

6. **"All guesses are equal."** A doctor's guess about a diagnosis and a coin flip are both "guesses," but they draw on vastly different substrate. The word "guess" hides an enormous range of epistemic quality.

7. **"I know when I'm guessing."** This is the most dangerous assumption. People routinely mistake pattern-matched familiarity for knowledge. The feeling of knowing and the state of knowing are different systems.

---

## Step 4: The Procedure

```
WHAT IT MEANS TO GUESS — DECISION PROCEDURE
============================================

PURPOSE: When you notice yourself about to guess (or after someone asks
you to guess), use this to determine what kind of guess it is, whether
you should guess at all, and how to make the best guess available.


STEP 0: Are you actually guessing?

  Ask yourself: "Could I explain WHY I believe this, with evidence
  someone else could verify?"

  YES, clearly  → You're not guessing. You're asserting. Stop here
                   unless you want to CHECK your assertion (go to Step 5).
  YES, partly   → You're making an INFORMED guess. Go to Step 1.
  NO            → You're making a PURE guess. Go to Step 1.
  I'M NOT SURE  → You might be confusing familiarity with knowledge.
                   Go to Step 1 and treat it as a guess until proven
                   otherwise.


STEP 1: What TYPE of thing are you guessing?

  Pick the one that fits:

  A) "I'm guessing a FACT I don't have."
     (There is a right answer. I just don't know it.)
     → Go to SECTION A

  B) "I'm guessing what WILL HAPPEN."
     (The answer doesn't exist yet.)
     → Go to SECTION B

  C) "I'm guessing what CATEGORY something belongs to."
     (Is this X or Y? Is this good or bad?)
     → Go to SECTION C

  D) "I'm guessing a QUANTITY or AMOUNT."
     (How many? How much? How long?)
     → Go to SECTION D

  E) "I'm guessing what someone WANTS or FEELS."
     (Preferences, reactions, intentions.)
     → Go to SECTION E


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION A: Guessing a Fact You Don't Have
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Step A1: CAN you look it up?
    → YES: Look it up. You're done. A guess here is just laziness.
    → NO (too expensive, no source exists, etc.): Continue to A2.

  Step A2: Have you been EXPOSED to a possible answer?
    (Someone mentioned a number. You read something once.
     You heard it somewhere.)
    → YES: ⚠ WARNING — you may be anchored. That memory might be
      wrong, or the source unreliable. Write down that exposure,
      then ALSO generate an answer ignoring it. You now have two
      candidates. Proceed to A3 with both.
    → NO: Proceed to A3.

  Step A3: What ADJACENT facts do you know?
    Write down anything related. Example: "I don't know the
    population of Portugal, but I know it's smaller than Spain
    and larger than Ireland. Spain is ~47M, Ireland is ~5M."
    This creates bounds. Your guess should be INSIDE those bounds.

  Step A4: State your guess AND your confidence.
    Format: "I guess [X]. I'd bet [stakes] on it."
    If you wouldn't bet anything → your guess has near-zero
    information value. Acknowledge that.

  → DONE


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION B: Guessing What Will Happen (Prediction)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Step B1: Has this type of thing happened before?
    → YES, many times: Go to B2.
    → YES, a few times: Go to B3.
    → NO, this is unprecedented: Go to B4.

  Step B2 (Repeated event): What's the BASE RATE?
    "Out of the last N times, how often did [outcome] happen?"
    Your guess should START from the base rate and adjust only
    with specific new evidence. Write down:
    - Base rate: ___
    - What's different this time: ___
    - Adjusted guess: ___
    ⚠ WARNING: Most people adjust too far from the base rate.
    If your adjustment moves your guess more than 20 percentage
    points from base rate, write down WHY in one sentence.
    → DONE

  Step B3 (Few precedents): List every precedent you know.
    What happened? What were the conditions?
    Are current conditions more like precedent A or B?
    State your guess as a RANGE, not a point: "Between X and Y."
    → DONE

  Step B4 (No precedent): Acknowledge this is a REAL guess.
    You have no track record to draw on. Your guess reflects
    your model of how things work, which may be wrong.
    State it as: "If my understanding of [domain] is right,
    then [prediction]. But I have no precedent for this."
    → DONE


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION C: Guessing a Category (Classification)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Step C1: List the possible categories.
    (If you can't list them, you're not ready to guess. First
    figure out what the options ARE.)

  Step C2: For each category, write down ONE thing you'd
    expect to see if it were that category.
    Example: "If this email is a scam, I'd expect urgency
    language and a request for money."

  Step C3: Check which expectations are MET.
    Category with most met expectations = your guess.
    ⚠ WARNING: If TWO categories match equally well, your
    guess is genuinely ambiguous. Say so. Don't force a pick.

  Step C4: Check for the RARE category trap.
    Is one category much more common than the others?
    Even if the evidence points to the rare category, the
    common one might still be more likely. Example: A positive
    test for a rare disease is still probably a false positive.
    → DONE


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION D: Guessing a Quantity (Estimation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Step D1: Do NOT start with a number. Start with BOUNDS.
    "It's definitely more than ___."
    "It's definitely less than ___."
    Write both down.

  Step D2: Narrow the bounds.
    "It's probably more than ___."
    "It's probably less than ___."

  Step D3: Decompose if possible.
    Can you break the quantity into parts you know better?
    Example: "How many piano tuners in Chicago?"
    → Population × % with pianos × tunings/year ÷ tunings
       a tuner can do per year.
    Each piece is easier to guess than the whole.

  Step D4: State your estimate as a RANGE.
    "Between [low] and [high], probably around [middle]."
    ⚠ WARNING: Most people make their ranges too narrow.
    Whatever range you wrote, consider widening it by 50%.
    → DONE


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION E: Guessing What Someone Wants or Feels
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Step E1: Are you guessing based on what YOU would want?
    → YES: ⚠ WARNING — Projection. Other people aren't you.
      Continue to E2, but know your guess is contaminated.
    → NO: Continue to E2.

  Step E2: What EVIDENCE do you have about this person?
    List specific things they've said, done, or chosen.
    Not "they seem like the type who..." — actual observations.

  Step E3: What's the MOST COMMON preference in this
    situation?
    If you have no personal evidence (E2 came up empty), the
    base rate is your best guess. "Most people in this
    situation want ___."

  Step E4: Can you just ASK them?
    → YES: Ask. Guessing what people want when you can ask
      is a failure of communication, not a knowledge problem.
    → NO: State your guess and acknowledge it's projection
      unless you had strong evidence in E2.
    → DONE


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5: META — Should You Be Guessing At All?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  After completing any section, run this check:

  5a: What are the STAKES?
    → Trivial (what to eat, small talk): Guess freely.
       Your time is worth more than being right.
    → Moderate (work decision, purchase): Your guess is a
       starting point. Plan to verify before committing.
    → High (medical, legal, safety): DO NOT rely on a guess.
       Seek expert input. If you must act now, act on the
       SAFEST guess, not the most likely one.

  5b: Will you get FEEDBACK on this guess?
    → YES: Good. Track it. You'll improve over time.
    → NO: ⚠ You'll never know if you were right. This means
      your guessing in this domain will never improve.
      Consider whether there's a way to create feedback.

  5c: Are you guessing because it's NECESSARY or because
      it's COMFORTABLE?
    → Necessary (deadline, no information source): Proceed.
    → Comfortable (avoiding effort of looking up, asking,
      or thinking harder): This isn't guessing — it's
      settling. Go back and gather more information.
```

---

## Step 5: Failure Modes

| # | Failure Mode | How to Recognize It | What to Do Instead |
|---|---|---|---|
| 1 | **Mistaking familiarity for knowledge** | You feel certain but can't explain why. The answer "just feels right." | Treat it as a guess regardless of the feeling. Run the procedure. |
| 2 | **Anchoring without noticing** | You heard a number or suggestion before forming your guess, and your guess is suspiciously close to it. | Explicitly generate an answer while pretending you never heard the anchor. Compare the two. |
| 3 | **Guessing when you could know** | The answer is available (searchable, askable, testable) but you defaulted to guessing. | Stop and check: "Can I just find out?" If yes, find out. |
| 4 | **Treating a range as a point** | You gave one number instead of a range. You said "it'll take 3 weeks" instead of "between 2 and 5 weeks." | Always express guesses as ranges. If you can't give a range, your understanding is too thin to guess. |
| 5 | **Ignoring base rates** | You focused entirely on the specific case and ignored how things usually go. "But THIS time is different..." | Write down the base rate first. Adjust from there. Make yourself justify any large departure. |
| 6 | **Projecting your preferences** | When guessing what others want, you unconsciously substituted your own preferences. | Ask: "Would a person with the OPPOSITE personality from me guess the same thing?" If no, your guess is projection. |
| 7 | **False precision** | Your guess has more decimal places than your knowledge warrants. "I'd say there's a 73% chance." | Round to the nearest 10%. If you can't tell the difference between 70% and 80%, you don't have 73% precision. |
| 8 | **Guessing in high-stakes situations out of social pressure** | Someone asked, everyone's waiting, silence feels awkward. So you guessed. | Say "I don't know" or "I'd need to check." This is always available and almost always better than a pressured guess. |

---

## Step 6: Validation

Every step checked against: "Can someone with no expertise follow this?"

- Step 0: Binary self-check. Clear. **PASS**
- Step 1: Multiple choice routing. No ambiguity. **PASS**
- Sections A-E: Each step is a concrete action (write down, list, check, ask). No "consider" or "think about." **PASS**
- Decision points: All binary or explicit multiple choice. **PASS**
- Dead ends: All paths reach "DONE." **PASS**
- Step 5 meta-check: Uses concrete criteria (stakes, feedback, necessity). **PASS**

---

## Quick Reference Cards

**THE GUESS SPECTRUM**
```
Pure guess ←————————————→ Informed assertion
(coin flip)   hunch   estimate   educated guess   inference   (proof)
     ↑                                                          ↑
  No information                                     Complete information
  about this specific                                verified by evidence
  question
```

**WHEN TO GUESS vs. WHEN TO FIND OUT**
```
                    Low stakes    High stakes
Easy to find out  → Find out      Find out
Hard to find out  → Guess         Guess CAUTIOUSLY + plan to verify
```

**THE THREE HONEST GUESSES**
1. "I guess X, and here's my reasoning: ___"
2. "I guess X, but I wouldn't bet on it"
3. "I genuinely don't know — my guess is as good as random here"

---

## Common Mistakes

1. Saying "I don't know" when you actually have useful partial information (under-guessing)
2. Saying "I think X" when you mean "I'm guessing X" — hiding the guess from yourself
3. Never updating a guess even after getting new information
4. Treating all guesses as equal regardless of how much evidence supports them
5. Confusing "I haven't been wrong yet" with "I'm good at this" — survivorship bias in untracked guesses
6. Guessing once and committing fully instead of guessing, acting tentatively, and updating

---

## When to Override This Procedure

- **Safety decisions**: When the wrong guess could hurt someone, don't guess. Default to the safest option and get expert help.
- **Legal/medical/financial**: These domains have professionals for a reason. Guess only to orient yourself before consulting one.
- **When you're emotionally invested**: Strong desire for a particular answer corrupts guessing. Get a disinterested party to guess instead.
- **When the question itself is wrong**: Sometimes "what should I guess?" is the wrong question. Sometimes the right move is to reject the framing entirely — you don't have to answer every question you're asked.

---

## Worked Examples

### Example 1: "How old is this building?"

**Step 0**: Can I explain why? No. → This is a guess.
**Step 1**: I'm guessing a fact. → Section A.
**A1**: Can I look it up? Probably, but I'm walking past it right now. Not urgent. → Continue.
**A2**: Exposed to a possible answer? A sign out front said "est. 1920-something" but I didn't read it clearly. → Anchored on ~1920. Note it, also generate independent guess.
**A3**: Adjacent facts: The architecture looks Art Deco. Art Deco was popular 1925-1940. The brick looks old but not crumbling.
**A4**: "I guess 1930, give or take 10 years. I'd bet $5 on it being between 1920-1940."
**Step 5**: Stakes? Trivial. No action depends on this. Guess freely.

### Example 2: "Will this startup succeed?"

**Step 0**: Can I explain why I believe what I believe? Sort of — I have some reasons. → Informed guess.
**Step 1**: Guessing what will happen. → Section B.
**B1**: Has this type of thing happened before? Yes, many times. → B2.
**B2**: Base rate of startup success: ~10% reach meaningful scale. What's different here? Strong team, crowded market, no revenue yet. Adjusted guess: maybe 15%. That's only 5 points from base rate — reasonable.
**Step 5**: Stakes? I'm considering investing. → Moderate/High. Do NOT rely solely on this guess. Get more data, talk to customers, see financials.

### Example 3: "Does my friend want me to come to their party?"

**Step 0**: Can I explain why? Not really. → Guess.
**Step 1**: Guessing what someone wants. → Section E.
**E1**: Am I projecting? I'd want people at MY party, so... yes, probably projecting.
**E2**: Evidence: They invited me (explicit). But the invite felt generic (group text). They haven't followed up.
**E3**: Most common: If someone invites you, they generally want you there.
**E4**: Can I ask? YES. → "Hey, do you actually want me to come or is this a courtesy invite?" — Ask.

---

*Validation status: This procedure has not been validated by domain experts.*
