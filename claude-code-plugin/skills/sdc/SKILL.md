---
name: "sdc - Self-Deception Check"
description: "Detect when reasoning is actually rationalization. Mechanical checks for motivated reasoning, emotional override, and evidence asymmetry."
---

# Self-Deception Check

**Input**: $ARGUMENTS

---

## Purpose

A mechanical procedure for recognizing when you are rationalizing rather than reasoning -- when your "analysis" is actually a post-hoc justification for a decision you have already emotionally made. Written so that someone with zero background in psychology or critical thinking can follow every step and arrive at an honest assessment.

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/sdc 4x [input]").

| Depth | Min Sections | Min Tests/Section | Min Lookbacks | Min Verifiers |
|-------|-------------|------------------|--------------|--------------|
| 1x    | 1           | 3                | 1            | 1            |
| 2x    | 1           | 5                | 2            | 2            |
| 4x    | 2           | 7                | 3            | 3            |
| 8x    | 3           | 10               | 5            | 4            |
| 16x   | 4           | 12               | 8            | 5            |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## Step 0: What type of self-deception situation is this?

Read each row. Pick the one that best matches your situation.

| # | You are... | Go to |
|---|-----------|-------|
| A | About to make a decision and want to check yourself before committing | SECTION A: Pre-Decision Check |
| B | Defending a decision you already made and someone challenged it | SECTION B: Post-Decision Audit |
| C | Noticing a recurring pattern -- you keep ending up in the same bad situation | SECTION C: Pattern Interrupt |
| D | Feeling strong emotion (anger, excitement, fear, desire) about a choice | SECTION D: Emotional Override Detection |
| E | Reviewing someone else's reasoning (or your past reasoning) for self-deception | SECTION E: Third-Party Audit |

If none of these fit, start with SECTION A. It is the most general.

---

## SECTION A: Pre-Decision Check

*Use when: You are about to make a decision and want to check yourself before committing.*

### Step A1: Write Down Your Current Leaning

Before doing anything else, complete this sentence in writing (paper or digital):

> "Right now, I am leaning toward: _______________"
> "On a scale of 1-10, how certain do I feel? ___"
> "I first started leaning this way on [date/occasion]: ___"

Why this matters: This creates a record. You cannot retroactively claim "I was always open-minded" if you wrote down a strong leaning.

What you should see: A sentence describing what you want to do and a certainty number. If your certainty is 9 or 10, proceed with heightened suspicion -- near-total certainty on complex decisions is a red flag.

### Step A2: The Body Check (30 seconds)

Close your eyes. Think about choosing the OPPOSITE of your current leaning. Notice what happens in your body for 10 seconds.

Check the sensations you notice:
- [ ] Tightness in chest or stomach
- [ ] Jaw clenching
- [ ] Urge to stop doing this exercise
- [ ] Feeling of "that's ridiculous, I don't need to consider that"
- [ ] Heat or flush
- [ ] A sudden rush of counter-arguments flooding your mind

**Scoring:**
- 0 sensations: Low emotional involvement. Proceed to Step A3.
- 1-2 sensations: Moderate emotional involvement. Proceed to Step A3 with awareness.
- 3+ sensations: HIGH emotional involvement. This decision has strong emotional drivers. Proceed to Step A3, but every subsequent test carries more weight. Also do SECTION D after completing Section A.

### Step A3: The Evidence Audit

Draw a line down the middle of a page. Label the left column "SUPPORTS my leaning" and the right column "CONTRADICTS my leaning."

List every piece of evidence, reason, or data point you can think of. Spend at least 3 minutes on each column.

**Now count:**
- Number of items in SUPPORTS column: ___
- Number of items in CONTRADICTS column: ___

**Scoring:**
- Ratio is roughly balanced (within 2:1): Your evidence gathering may be fair. Proceed to Step A4.
- SUPPORTS outnumbers CONTRADICTS by more than 3:1: **RED FLAG.** Either your position is overwhelmingly correct (possible) or you are cherry-picking (more likely for complex decisions). Proceed to Step A4 with heightened suspicion.
- CONTRADICTS column is nearly empty: **STRONG RED FLAG.** You almost certainly have not seriously engaged with the opposing view. STOP. Spend 10 minutes actively searching for the strongest case against your leaning before proceeding.

### Step A4: The Writing Test

Write two paragraphs (minimum 4 sentences each):

**Paragraph 1**: The strongest possible argument FOR your current leaning, written as if you are trying to convince a skeptic.

**Paragraph 2**: The strongest possible argument AGAINST your current leaning, written as if you are trying to convince yourself to change your mind.

**Now compare:**

| Check | Yes | No |
|-------|-----|-----|
| Is Paragraph 2 shorter than Paragraph 1? | RED FLAG | OK |
| Does Paragraph 2 contain words like "but," "however," "although" that soften the argument? | RED FLAG | OK |
| Did you find Paragraph 2 physically harder to write? | RED FLAG | OK |
| Does Paragraph 2 use weaker language ("might," "could," "some people think") compared to Paragraph 1's stronger language ("clearly," "obviously," "the evidence shows")? | RED FLAG | OK |
| Did you feel an urge to rebut Paragraph 2 as you were writing it? | RED FLAG | OK |

**Scoring:**
- 0 red flags: Low self-deception risk. Proceed to Step A5.
- 1-2 red flags: Moderate self-deception risk. Proceed to Step A5.
- 3+ red flags: HIGH self-deception risk. Your ability to argue against your position is compromised. Proceed to Step A5, then strongly consider SECTION D.

### Step A5: The Inversion Test

Answer each of these questions honestly and in writing:

**Question 1 -- The Outsider Test**: "If my best friend told me they were making this exact decision for these exact reasons, would I think their reasoning was solid?"
- [ ] Yes, I would fully support their reasoning
- [ ] I would have some concerns
- [ ] I would think they were fooling themselves

**Question 2 -- The Opposite Outcome Test**: "If all the same evidence existed but it supported the OPPOSITE conclusion, would I find that evidence equally convincing?"
- [ ] Yes, I would update my view
- [ ] I am not sure
- [ ] No, I would find reasons to doubt it

**Question 3 -- The Pre-Commitment Test**: "Did I have this opinion BEFORE I encountered the evidence, or did I form it AFTER carefully reviewing the evidence?"
- [ ] I formed the opinion after reviewing evidence
- [ ] I am not sure / I had a vague leaning before
- [ ] I had this opinion first and then looked for evidence

**Question 4 -- The Stakes Test**: "If I turned out to be wrong, what would I lose?"
- [ ] Nothing significant (low ego investment)
- [ ] Some time or money
- [ ] I would look foolish, or lose status, or have to admit a mistake
- [ ] It would challenge something I believe about myself

**Scoring:**
- All first options: Low self-deception risk.
- Any second options: Moderate. Worth investigating further.
- Any third or fourth options: You are very likely engaged in motivated reasoning on this specific question. Proceed to Step A6.

### Step A6: The Verdict

Tally your red flags from Steps A2 through A5:

| Source | Red Flags |
|--------|-----------|
| A2 Body Check | ___ (0 if low, 1 if moderate, 2 if high) |
| A3 Evidence Audit | ___ (0 if balanced, 1 if 3:1, 2 if near-empty) |
| A4 Writing Test | ___ (count from table) |
| A5 Inversion Test | ___ (count of non-first answers) |
| **TOTAL** | ___ |

**Interpretation:**

| Total Score | Verdict | Action |
|-------------|---------|--------|
| 0-2 | **LOW RISK**: Your reasoning appears to be genuine analysis, not rationalization. | Proceed with your decision. Keep your written record in case you want to audit later. |
| 3-5 | **MODERATE RISK**: There are signs of emotional influence on your reasoning. | Sleep on it for 24 hours. Then re-read your Paragraph 2 from Step A4. If it now seems stronger, your initial assessment was clouded. Consult one person who would disagree with you. |
| 6-8 | **HIGH RISK**: You are very likely rationalizing. | Do not commit to this decision today. Complete SECTION D. Seek out the strongest opposing voice you can find and listen without rebutting for 10 minutes. Redo this checklist in 72 hours. |
| 9+ | **VERY HIGH RISK**: You are almost certainly deceiving yourself. | Acknowledge (in writing): "I appear to have made this decision emotionally and am constructing reasons after the fact." This is not a criticism -- it is information. The question is: knowing this, do you still want to proceed? If yes, name the real reason. |

---

## SECTION B: Post-Decision Audit

*Use when: You have already made a decision and someone is challenging it, or you are having second thoughts.*

### Step B1: Reconstruct the Timeline

Write answers to these questions:
1. When did I first start leaning toward this decision? (Date or occasion)
2. When did I first articulate reasons for it? (Date or occasion)
3. Which came first -- the leaning or the reasons?

Key insight: If the leaning came before the reasons, the reasons may be rationalizations. This is not certain -- sometimes gut feelings are correct -- but it means the reasons need extra scrutiny.

### Step B2: The Reasons Inventory

List every reason you give (or have given) for this decision. Number them.

Now, for each reason, answer:
- Did I discover this reason through research, or did it "come to me" while defending my decision?
- If someone proved this specific reason was wrong, would I change my decision?

**Critical test**: If no single reason being disproven would change your decision, you are not reasoning from the evidence -- the evidence is decoration. Your real reason is something else. Go to Step B3.

### Step B3: Find the Real Reason

Complete this sentence three times, each time with a different ending:

> "The real reason I made this decision, the one I would be embarrassed to say out loud, might be: _______________"

Rules:
- Each answer must be something you would NOT put in a formal justification
- Each answer must involve an emotion, desire, fear, or ego-related motive
- You are not claiming these ARE the real reasons -- you are generating candidates

What you should see: At least one of the three answers should produce a physical reaction -- a wince, a flush, a desire to cross it out. That one deserves attention.

### Step B4: The Substitution Test

Imagine someone you consider foolish or biased made this exact same decision for these exact same stated reasons. Write down your reaction.

- Would you find their reasoning convincing?
- Would you suspect they were rationalizing?
- What would you think their REAL reason was?

If you would suspect them of rationalizing: You should apply the same suspicion to yourself.

### Step B5: The Update Test

Think of the single strongest piece of evidence or argument against your decision.

Now rate honestly:
- How much time did you spend thinking about this counter-evidence compared to the supporting evidence? ___
- Did you look for reasons this counter-evidence might be wrong? (Yes / No)
- Did you look for reasons the supporting evidence might be wrong with equal vigor? (Yes / No)

If you spent more effort attacking counter-evidence than attacking supporting evidence: This is asymmetric skepticism -- the hallmark of motivated reasoning.

### Step B6: The Commitment Device

If Steps B1-B5 reveal likely self-deception:

Write down and share with one trusted person:

> "I acknowledge that my decision about [X] may have been driven more by [emotion/desire from B3] than by the reasons I stated. The test I will use to check: [specific observable outcome]. If [outcome] does not occur by [date], I will reconsider."

Why sharing matters: Self-deception thrives in private. Making your test public creates accountability.

---

## SECTION C: Pattern Interrupt

*Use when: You notice you keep ending up in the same bad situation.*

### Step C1: List the Recurrences

Write down the last 3-5 times you ended up in this same type of situation. For each one, write the reason you gave at the time for why it was different or would work out.

### Step C2: Compare the Reasons

Look at the reasons from C1. Highlight similarities.

What you should see: The reasons will sound different on the surface but share an underlying structure. Common patterns:

| Surface Reason | Underlying Pattern |
|---------------|-------------------|
| "This time is different because of [new detail]" | Novelty bias -- every time feels different, but the structure is the same |
| "I've learned from last time" | Learning claim without evidence of changed behavior |
| "The circumstances were against me before, but now..." | External attribution -- blaming circumstances, not your pattern |
| "This person/opportunity is special" | Idealization -- different object, same pattern |

### Step C3: Name the Pattern

Complete this sentence:

> "The pattern I keep repeating is: I [behavior], telling myself [justification], and then [consequence]."

Read this sentence aloud. If you feel resistance to reading it aloud, the pattern is significant.

### Step C4: Identify the Payoff

Every repeated pattern has a hidden payoff -- something you get from it even though the outcome is bad.

Answer: "What do I get to avoid, feel, or maintain by repeating this pattern?"

Common payoffs:
- Avoiding a harder decision
- Maintaining a self-image ("I'm the kind of person who...")
- Feeling excitement/hope (the anticipation is the payoff, not the outcome)
- Avoiding grief or loss (the pattern keeps hope alive)

### Step C5: The Pattern-Break Test

Write down what you would do differently if you accepted that the pattern, not the circumstances, is the problem. What specific behavior would change?

If you cannot name a specific behavioral change, you are still inside the self-deception.

---

## SECTION D: Emotional Override Detection

*Use when: You are experiencing strong emotion about a decision.*

### Step D1: Name the Emotion

Pick the closest match from this list:

| Category | Specific Emotions |
|----------|------------------|
| **Wanting** | Desire, craving, excitement, enthusiasm, hope |
| **Protecting** | Fear, anxiety, dread, caution, suspicion |
| **Defending** | Anger, indignation, righteousness, contempt |
| **Preserving** | Attachment, loyalty, nostalgia, sentimentality |
| **Avoiding** | Shame, embarrassment, guilt, regret |

Write: "The emotion driving this decision is most likely: _______________"

### Step D2: The Intensity Scale

Rate the emotional intensity from 1-10.

| Rating | Description |
|--------|-------------|
| 1-3 | Mild preference. You could go either way without distress. |
| 4-6 | Moderate pull. You have a clear preference and would be disappointed if overridden. |
| 7-8 | Strong pull. You feel urgency to decide NOW. Counter-arguments make you agitated. |
| 9-10 | Overwhelming. You cannot seriously consider the alternative. It feels physically impossible or disgusting. |

Key insight: At 7+, your rational faculties are significantly impaired for THIS specific decision. Not impaired in general -- impaired for this one decision. The emotion has a thumb on the scale.

Action for 7+: Do not make this decision right now. Wait minimum 24 hours. If impossible to wait, proceed to Step D3 but know that your results will be emotion-influenced.

### Step D3: The Functional Analysis

Answer these three questions:

1. "What does this emotion want me to DO?" (The action the emotion is pushing toward)
2. "What does this emotion want me to AVOID?" (What the emotion is pulling me away from)
3. "If I removed this emotion entirely and was a cold, calculating machine, what would I choose?"

If the cold-machine answer differs from your emotional answer: You now have two data points. The emotion is not automatically wrong -- but you must acknowledge it is a factor, not just "my analysis."

### Step D4: The Emotion-Reason Disentangle

For each reason you have given for your decision, classify it:

| My Reason | This reason came from... | How I know |
|-----------|------------------------|------------|
| [Reason 1] | Emotion / Analysis / Both / Unsure | [Evidence] |
| [Reason 2] | Emotion / Analysis / Both / Unsure | [Evidence] |
| [Reason 3] | Emotion / Analysis / Both / Unsure | [Evidence] |

How to classify:
- If you had the reason BEFORE the emotion: probably Analysis
- If the reason appeared AFTER or DURING the emotion: probably Emotion
- If the reason conveniently supports what the emotion wants: probably Emotion
- If the reason would apply even with the opposite emotion: probably Analysis

What you should see: If most reasons classify as Emotion or Unsure, your "analysis" is likely rationalization.

---

## SECTION E: Third-Party Audit

*Use when: Reviewing someone else's reasoning (or your own past reasoning) for self-deception.*

### Step E1: Identify the Conclusion

Write down the conclusion the person (or past-you) reached.

### Step E2: Identify the Stated Reasons

List every reason they gave.

### Step E3: Apply the Seven Tests

For each test, mark PASS or FLAG:

| # | Test | Question | PASS / FLAG |
|---|------|----------|-------------|
| 1 | **Conclusion-First** | Did the conclusion seem to exist before the research? | |
| 2 | **Asymmetric Skepticism** | Were supporting and opposing evidence held to the same standard? | |
| 3 | **Convenient Reasoning** | Does every piece of reasoning happen to support the desired conclusion? | |
| 4 | **Missing Counter** | Is the strongest opposing argument addressed or ignored? | |
| 5 | **Emotional Language** | Does the reasoning use emotional/loaded language disguised as analysis? | |
| 6 | **Motive Check** | Does the person have a clear emotional motive for this conclusion? | |
| 7 | **Survivorship** | Are they citing examples that support them while ignoring examples that don't? | |

**Scoring:**
- 0-1 flags: Reasoning appears genuine
- 2-3 flags: Moderate self-deception risk
- 4+ flags: High probability of motivated reasoning

### Step E4: The Steel Man Test

Can you construct a version of their reasoning that reaches the OPPOSITE conclusion using equally valid logic?
- If yes: Their conclusion is not determined by the evidence alone -- preference played a role.
- If no: Their conclusion may genuinely follow from the evidence.

### Step E5: Deliver the Audit

If this is for someone else, frame it as:

> "I notice that [specific observation from tests], which sometimes indicates the conclusion came before the analysis. I could be wrong -- what would change your mind about this?"

The question "what would change your mind" is diagnostic: If they cannot name anything specific that would change their mind, the belief is not evidence-based.

---

## Quick Reference Cards

### Card 1: The Five-Second Self-Deception Check

Ask yourself: **"What would change my mind?"**

- If you can name a specific, realistic thing: You are probably reasoning.
- If you cannot, or if you immediately explain why nothing could: You are probably rationalizing.

### Card 2: The Four Red Flags of Motivated Reasoning

1. **Certainty on complex topics**: Feeling 9/10 or 10/10 sure about something with genuine complexity.
2. **Asymmetric evidence standards**: Accepting friendly evidence uncritically, attacking unfriendly evidence harshly.
3. **Conclusion stability**: Your conclusion never changes no matter what new information appears.
4. **Emotional reactivity to challenge**: Feeling anger, contempt, or dismissal when someone questions your reasoning.

### Card 3: The Three Questions

Before any important decision:
1. "Am I looking for the right answer, or am I looking for reasons that THIS is the right answer?"
2. "When did I first form this opinion -- before or after examining the evidence?"
3. "If I am wrong, what am I protecting by not seeing it?"

### Card 4: Legitimate vs. Rationalized Reasoning

| Legitimate Reasoning | Rationalization |
|---------------------|-----------------|
| Conclusion follows from evidence | Evidence is selected to support conclusion |
| You can state the counter-argument as strongly as your argument | Counter-arguments feel weak and easy to dismiss |
| You sought out disconfirming evidence | You mainly encountered confirming evidence |
| Your confidence matches the evidence quality | Your confidence exceeds what the evidence warrants |
| You would accept this reasoning from an opponent | You would find this reasoning suspicious from an opponent |
| You can name what would change your mind | Nothing specific would change your mind |

---

## Common Mistakes

### Mistake 1: Confusing "having reasons" with "reasoning"
Rationalizations ARE reasons. They are logical, coherent, and persuasive. The question is not whether you have reasons, but whether you gathered and evaluated evidence fairly. Having an elaborate argument is not evidence of honest reasoning -- in fact, suspiciously elaborate arguments for emotionally charged conclusions should raise a flag.

### Mistake 2: Using this procedure to justify your original position
"I ran the self-deception check and I'm fine!" If you feel relieved and vindicated after running this procedure, run it again more carefully. The feeling of relief suggests you were looking for permission, not truth.

### Mistake 3: Assuming self-deception means you are wrong
Catching yourself in motivated reasoning does not automatically mean your conclusion is wrong. It means your REASONS for that conclusion are unreliable. The conclusion might still be correct for other reasons. But you need to find those real reasons or acknowledge that you are choosing based on emotion.

### Mistake 4: Applying this only to decisions you are unsure about
Self-deception is most powerful precisely on the topics where you feel MOST certain. The decisions you feel no need to check are the ones most likely to be compromised. Certainty is not evidence of correctness -- it is often evidence of emotional investment.

### Mistake 5: Believing you are "too rational" for self-deception
Intelligence and education do not protect against motivated reasoning. In fact, research suggests that smarter people are BETTER at rationalizing, because they can construct more sophisticated justifications. The smarter you are, the better you are at fooling yourself.

### Mistake 6: Running the procedure mentally instead of in writing
If you do the steps in your head, your self-deceptive mechanisms will interfere in real time -- softening counter-arguments, emphasizing favorable evidence, minimizing red flags. The entire value of this procedure is that WRITING creates an external record that you cannot retroactively edit in your memory.

### Mistake 7: Treating a low score as proof of objectivity
A low score means the procedure did not detect strong signals. It does not mean you are unbiased. Self-deception can be subtle enough to pass these tests. Use a low score as mild reassurance, not as a certificate of objectivity.

---

## When to Override This Procedure

### Override 1: Emergency situations requiring immediate action
If someone is in danger or a time-critical opportunity will disappear, act first and audit later. This procedure requires time for writing and reflection. It is not for split-second decisions.

### Override 2: Trivial decisions
Do not use a 30-minute self-deception audit to decide where to eat lunch. Reserve this for decisions that are high-stakes, hard to reverse, or involve patterns you have noticed.

### Override 3: When the protective function of self-deception is serving you
In some cases, self-deception is adaptive. Examples:
- Maintaining motivation during an extremely difficult but necessary task
- Preserving hope while dealing with a health crisis where attitude affects outcome
- Staying functional while processing grief (denial as a temporary stage)

If honest self-assessment would be actively destructive and you have no better option, it may be appropriate to defer the audit.

### Override 4: When you need a therapist, not a checklist
If running this procedure causes significant distress, if the patterns you uncover in Section C are deeply painful, or if you recognize that your self-deception is entangled with trauma -- this procedure has done its job by surfacing the issue, but a checklist cannot resolve it. Seek a qualified therapist.

### Override 5: When domain expertise should override the procedure
If you are an expert in the domain and your expert intuition conflicts with the procedure's output, the procedure may be wrong. Expert intuition IS a valid input -- this procedure is designed for decisions where you lack expertise. If you have genuine expertise (not just experience), weigh it accordingly.

---

## Worked Examples

### Example 1: "Should I quit my job to start a business?"

**Running Section A (Pre-Decision Check):**

**Step A1**: "Right now, I am leaning toward: quitting to start the business. Certainty: 8/10. I first started leaning this way 3 months ago when I had the idea."

**Step A2 (Body Check)**: Thinking about NOT quitting produces: tightness in chest, rush of counter-arguments ("but the opportunity is NOW"), urge to skip this exercise. Score: 3+ sensations = HIGH emotional involvement.

**Step A3 (Evidence Audit)**:
- SUPPORTS: 7 items (market opportunity, my skills, savings runway, friend's success story, flexible schedule, hate current job, business plan looks solid)
- CONTRADICTS: 2 items (risky economy, no business experience)
- Ratio: 3.5:1 = RED FLAG

**Step A4 (Writing Test)**:
- Paragraph FOR: Confident, specific, 8 sentences
- Paragraph AGAINST: 4 sentences, contains "but," "although," used weaker language
- Red flags: 4 out of 5 = HIGH

**Step A5 (Inversion Test)**:
- Outsider test: "I would have some concerns" about a friend doing this
- Opposite outcome: "I would find reasons to doubt" negative evidence
- Pre-commitment: "I had this opinion first and then looked for evidence"
- Stakes: "I would look foolish and have to admit a mistake"
- Score: All non-first answers = VERY HIGH

**Step A6 (Verdict)**: Total score: 2 + 1 + 4 + 4 = 11 = VERY HIGH RISK.

**Written acknowledgment**: "I appear to have made this decision emotionally -- I hate my current job and the business idea provides an exciting escape narrative. The real question I need to answer is: do I want to start a business, or do I want to leave this job? These are separate decisions. I should explore leaving the job for another job before assuming the answer is entrepreneurship."

### Example 2: "My partner and I are fine -- every couple argues."

**Running Section C (Pattern Interrupt):**

**Step C1 (Recurrences)**:
- 6 months ago: big fight, told friend "it's normal"
- 1 year ago: partner yelled at me in public, told myself "they were stressed"
- 18 months ago: discovered a lie, told myself "everyone has secrets"
- 2 years ago: friend expressed concern, told myself "they don't know our relationship"

**Step C2 (Compare Reasons)**: Each time, the reason was "special circumstances" -- stress, a bad day, external pressure. The pattern: minimize, attribute to circumstances, resume.

**Step C3 (Name the Pattern)**: "The pattern I keep repeating is: I accept harmful behavior from my partner, telling myself it is temporary or normal, and then I am surprised when it happens again."

**Step C4 (Payoff)**: "I get to avoid the terrifying prospect of being alone and having to rebuild my life. The self-deception maintains the relationship by preventing me from seeing it accurately."

**Step C5 (Pattern Break)**: "If I accepted the pattern as the problem, I would set a specific, observable boundary with a specific, observable consequence. For example: 'If yelling happens again, I will leave the room and we will discuss it in couples therapy within one week.' If I cannot bring myself to set such a boundary, I need to ask why."

### Example 3: "I've done my research and vaccines are dangerous."

**Running Section E (Third-Party Audit):**

**Step E3 (Seven Tests)**:
1. Conclusion-First: FLAG -- Person had concerns before research
2. Asymmetric Skepticism: FLAG -- Mainstream studies dismissed as "bought by pharma," fringe studies accepted uncritically
3. Convenient Reasoning: FLAG -- Every piece of evidence cited supports the pre-existing conclusion
4. Missing Counter: FLAG -- Massive body of safety data not addressed
5. Emotional Language: FLAG -- "Pumping chemicals into children" (emotional framing of routine procedure)
6. Motive Check: FLAG -- Fear for children's safety (powerful emotional driver)
7. Survivorship: FLAG -- Citing adverse events, ignoring millions of uneventful vaccinations

Score: 7/7 flags = very high probability of motivated reasoning.

**Step E4 (Steel Man)**: Can opposite conclusion be reached with equal logic? Yes -- the same "question authority" instinct could be applied to the fringe sources being trusted instead.

**Step E5 (Delivery)**: "I notice that the sources you trust for the anti-vaccine position are held to a very different standard than the sources you dismiss. What specific evidence would change your mind?" If the answer is "nothing," the belief is not evidence-based.
