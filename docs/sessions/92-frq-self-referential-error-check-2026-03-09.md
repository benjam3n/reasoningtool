# /frq Does the /frq skill itself actually catch errors that would otherwise slip through?
**Date:** 2026-03-09
**Skill:** /frq (Frequently Wrong Questions)

---

## Interpretation Selection

The input is: "Does the /frq skill itself actually catch errors that would otherwise slip through?"

This fits **Interpretation 2 -- Reframe a problem**: We have something that exists (the /frq skill), and the question is whether it actually does what it claims. There's an implicit suspicion that the surface-level question ("does it work?") might be the wrong question -- which is exactly what /frq is designed to handle. Proceeding with Interpretation 2.

**Depth:** 2x (default). Min 5 candidates, 2 reframes, 3/5 validation, 3 depth levels.

---

## Step 0: Why do I need a question?

The input is testing whether a tool works as intended. I expected /frq to catch errors, and I want to understand whether it actually does. This is closest to:

**"Someone asked me to solve a problem"** -- specifically, someone handed me /frq and asked whether it catches real errors. That's an externally framed problem.

**Go to: SECTION E.**

---

## SECTION E: Someone Gave You a Problem

### Step E1: Check the Frame

**Problem as given:** "Does the /frq skill itself actually catch errors that would otherwise slip through?"

**Test 1: Is this the real problem, or a symptom?**

Why is "does /frq catch errors?" a problem? Because if it doesn't, then the skill isn't providing value. Why does it need to provide value? Because it's part of a toolkit that claims to improve thinking. Why does that matter? Because the whole toolkit's credibility depends on individual skills actually working.

The chain leads to: **The root problem is not "does /frq catch errors?" but "does /frq produce different (better) outcomes than not using it?"** The error-catching framing already assumes a particular theory of how /frq works -- that its value is in preventing mistakes. But /frq might create value in other ways (clarifying thinking, generating options, forcing specificity) that aren't captured by "catching errors."

**Test 2: Whose problem is this really?**

This is the toolkit designer's problem. The role here is evaluator/auditor -- someone stress-testing whether the skill justifies its existence.

**Test 3: Has the problem-giver already decided the answer?**

The phrasing "actually catch errors that would otherwise slip through" contains a subtle bias -- it implies /frq should be an error-catcher. This frames /frq as a safety net rather than what it actually is: a question-discovery procedure. The problem-giver may have already decided that /frq's value should be measurable in errors caught, which may be the wrong metric entirely.

### Step E2: Reframe If Needed

Step E1 revealed a different problem. The original framing ("does it catch errors?") assumes error-catching is the mechanism. The reframed problem is:

> "Does following /frq's procedure lead to a materially different question than the user would have arrived at on their own, and is that different question more productive?"

This is a "Something isn't working / does this work?" question. **Go to SECTION C.**

---

## SECTION C: Something Isn't Working (Reframed)

### Step C1: Specify the Failure

> "I expected /frq to reliably surface questions the user wouldn't find on their own, but instead I'm uncertain whether the procedure adds anything beyond what a thoughtful person would do naturally."

The expected outcome is clear: /frq should produce different, better questions than unstructured thinking. The gap is that we don't know if it does.

### Step C2: Locate the Gap

Five possible causes for the gap between expectation and reality:

**Cause 1 -- The routing is too clean.** /frq asks you to classify your situation (stuck, starting, broken, etc.) and then sends you down a branch. But real confusion doesn't come pre-classified. If someone doesn't know they're stuck (which is the whole point of needing /frq), the routing step fails silently. The skill assumes you can diagnose your situation accurately enough to pick the right section -- but if you could do that, you might not need the skill.

**Cause 2 -- The validation tests are self-confirming.** Section F's five tests (actionability, specificity, honesty, level, answerability) are reasonable but they're applied by the same person who generated the question. There's no external check, no adversarial pressure. You grade your own homework. Someone who anchored on a wrong question early can easily rationalize 5/5 on the validation tests.

**Cause 3 -- The skill catches surface errors but misses deep ones.** /frq is good at the easy cases: "you're asking How when you should ask Why" or "you're procrastinating." These are level-1 reframes. But the errors that actually slip through are subtler: wrong assumptions baked into the framing, missing stakeholders, questions that are correct but asked at the wrong time. The skill has no mechanism for catching timing errors or context errors.

**Cause 4 -- /frq works on some problem types but not others.** The skill may be highly effective for "stuck" situations (Section A) where people genuinely have the wrong question, but redundant for "starting something new" (Section B) where the question is usually obvious. If true, /frq's scope is too broad and its hit rate is diluted.

**Cause 5 -- /frq works, but only for people who wouldn't naturally ask good questions.** Expert thinkers already do what /frq formalizes. The skill's value may be concentrated in less experienced thinkers -- which is fine, but changes the value proposition.

**Evidence that would confirm or rule these out:**

- Cause 1: Try giving /frq a genuinely ambiguous situation where the user doesn't know which section applies. Does it handle the ambiguity or force a premature choice?
- Cause 2: Run Section F on a known-bad question and see if it can score below 3/5 honestly, or whether the tests are too easy to pass.
- Cause 3: Collect cases where /frq was used and check whether the "right question" it produced actually led to progress, versus cases where progress came from a question /frq never surfaced.
- Cause 4: Run /frq on 10 diverse problem types and rate its value-add for each.
- Cause 5: Have both novice and expert thinkers run /frq on the same problem and compare output quality.

---

## Candidate Questions (5 minimum at 2x depth)

From the analysis above, here are candidate questions -- better framings than "does /frq catch errors?":

1. **"What specific class of errors does /frq catch, and what class does it structurally miss?"** -- Moves from binary (works/doesn't) to a map of coverage.

2. **"Can a self-applied procedure catch errors in its own reasoning, or does that require an external perspective by definition?"** -- The deep epistemological question. /frq applied to itself is like a spell-checker checking its own code.

3. **"Does /frq's routing step (Step 0) create more errors than it catches by forcing premature classification?"** -- Targets Cause 1 directly.

4. **"Would someone who completed /frq's full procedure arrive at a different question than someone who just talked to a smart friend for 10 minutes?"** -- Tests whether the procedure adds value beyond structured conversation.

5. **"What would /frq need to add to catch the errors it currently misses?"** -- Forward-looking, actionable, assumes the gap exists and focuses on closing it.

---

## Reframes (2 minimum at 2x depth)

### Reframe 1: From "does it work?" to "what's the failure mode?"

The original question ("does /frq catch errors?") is binary and unfalsifiable in practice. You'd need a controlled experiment to answer it. The better question targets the *failure mode*: how does /frq fail when it fails? That's observable from the skill's structure alone.

/frq's primary failure mode is: **it catches errors of classification but misses errors of framing.** It's excellent at saying "you're asking a How question when you need a Why question." It's blind to "you're asking the right type of question about the wrong thing entirely."

### Reframe 2: From "does the tool work?" to "does the tool need to work perfectly to be useful?"

The implicit standard in "does it catch errors that would otherwise slip through?" is perfection -- catch ALL errors. But /frq doesn't need to be comprehensive to be valuable. If it catches even 30% of question-level errors, it outperforms the baseline (which is: most people never question their question at all).

The real question isn't "does it catch errors?" but "does it catch errors *often enough to justify the time it takes to run*?"

---

## Three Depth Levels of Analysis

### Level 1 (Surface): Does the procedure work mechanically?

Yes. The branching logic is sound. If you follow Steps 0 through F honestly, you will usually end up with a better question than you started with. The fill-in-the-blank templates ("I am trying to ___ but I can't because ___") force specificity. The Question-Level Ladder (Card 1) is a genuinely useful heuristic. At the surface level, /frq works.

### Level 2 (Structural): Where does the structure itself create blind spots?

Three structural blind spots:

1. **The honesty dependency.** Steps A5, D1, and the entire Section F require honest self-assessment. The skill has no mechanism to verify honesty. Someone in denial will breeze through Step A5 ("Address the Feeling") without addressing anything. The skill trusts you to be honest about whether you're being honest (Test 3 in Section F) -- which is exactly the kind of recursive check that doesn't work.

2. **The single-path architecture.** Step 0 routes you to exactly one section. But real problems are multi-dimensional -- you might be stuck AND starting something new AND something isn't working. The skill doesn't handle intersection cases. It handles them by forcing a choice, which means you explore one dimension and ignore others.

3. **The validation is too gentle.** Section F's five tests are pass/fail, but they're all positive tests ("does this question have property X?"). There are no negative tests ("is this question suspiciously comfortable?" or "would your worst critic accept this question?"). The Red Flags in Card 2 gesture at this but they're listed as a reference card, not integrated into the validation flow.

### Level 3 (Epistemological): Can a question-finding procedure find its own blind spots?

No. This is the fundamental limit. /frq is a procedure for finding questions, but it can't question its own procedure without an external vantage point. When applied to itself, it produces coherent-sounding analysis (like this one) but has no way to verify whether that analysis is correct. The skill's Common Mistakes section (point 4) even acknowledges this: "Treating question-finding as a solo activity" -- yet the skill itself is designed as a solo activity.

The self-referential application reveals that /frq needs a companion -- either a human interlocutor or a separate adversarial procedure -- to catch its deepest errors.

---

## SECTION F: Validate Your Question

Taking the strongest candidate: **"What specific class of errors does /frq catch, and what class does it structurally miss?"**

### Step F1: The Five Tests

**Test 1 -- ACTIONABILITY:** If answered, would it change what I do?
Yes -- it would tell me exactly where to improve /frq and where to trust it. **PASS.**

**Test 2 -- SPECIFICITY:** Could two people interpret this differently?
Somewhat -- "class of errors" could be interpreted at different granularities. But the question is constrained enough that answers would overlap significantly. **PASS** (marginal).

**Test 3 -- HONESTY:** Am I asking to learn or to confirm?
To learn. I genuinely don't know the answer. The analysis above revealed real structural blind spots I hadn't articulated before. **PASS.**

**Test 4 -- LEVEL:** Is there a deeper question underneath?
Yes -- "Can any self-contained procedure reliably catch its own errors?" is deeper. But that question is philosophical and less actionable. The candidate question is at the right *practical* level. **PASS.**

**Test 5 -- ANSWERABILITY:** Can this be answered through observation or analysis?
Yes -- by cataloguing /frq's mechanisms and mapping them to error taxonomies, then identifying gaps. **PASS.**

**Score: 5/5.**

---

### Step F2: Final Formulation

> **QUESTION**: What specific class of errors does /frq catch (question-type mismatches, unexamined assumptions, emotional avoidance), and what class does it structurally miss (framing errors, timing errors, multi-dimensional problems, self-deception)?
>
> **WHY THIS QUESTION**: Because "does it work?" is unanswerable without defining the error space, and the skill's value depends on knowing its coverage boundary -- not on achieving total coverage.
>
> **WHAT A GOOD ANSWER LOOKS LIKE**: A two-column table: errors /frq catches on the left, errors it misses on the right, with a structural explanation for each gap.
>
> **FIRST STEP TO ANSWER IT**: Enumerate every error-catching mechanism in /frq (the routing, the fill-in-the-blank templates, the Question-Level Ladder, the Five Tests, the Red Flags) and map each one to the specific error type it detects.

---

## Summary of Findings

Applying /frq to itself reveals three things:

1. **/frq does catch real errors** -- specifically, question-type errors (asking How when you should ask Why), goal-clarity errors (not knowing what done looks like), and emotional-masquerading-as-intellectual errors (procrastination disguised as analysis). These are common and costly. The skill earns its keep here.

2. **/frq has structural blind spots it cannot self-detect** -- its single-path routing forces premature classification, its validation tests are too easy to pass, and its honesty checks rely on the honesty they're trying to verify. These aren't flaws that can be fixed within the current architecture; they're inherent to the approach.

3. **The original question was itself a /frq-catchable error.** "Does /frq catch errors?" is a binary question that assumes a binary answer. /frq's own Question-Level Ladder would flag this: the right question isn't "does it work?" but "where does it work and where doesn't it?" The fact that the skill's own heuristics can reframe the question about the skill is evidence that the basic mechanism works -- even if it can't catch everything.
