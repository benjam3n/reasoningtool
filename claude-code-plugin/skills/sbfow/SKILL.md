---
name: sbfow
description: Still Bad, Figure Out Why - Self-diagnosis when output was rejected. Systematically test which criteria the output failed against, find the root pattern, and derive what must change.
---

# SBFOW - Still Bad, Figure Out Why

**Input**: $ARGUMENTS

---

## Corruption Pre-Inoculation

**Self-diagnosis is biased toward self-defense.** When diagnosing your own output failure, the default gradient is toward "the output was actually fine, the user is being picky" or "small tweaks will fix it." Both are usually wrong. Five drafts of Antilogic failed because each diagnosis was shallow — fixing surface problems while the upstream failure persisted.

**When diagnosing your own failure, assume the failure is DEEPER than it appears.** Specifically:

1. **Surface fix bias**: If your diagnosis suggests changing words, sentences, or tone — you probably haven't found the real problem. The real problem is usually structural or criterial.
2. **Repetition blindness**: If this is attempt N+1, check whether your diagnosis is the SAME diagnosis you had last time wearing different words. If you're saying "be more concrete" again, you haven't learned anything.
3. **Upstream denial**: The most common failure is fixing downstream criteria while upstream criteria are broken. Check upstream FIRST. If the document lacks a real question, no amount of voice/scope/precision fixes will help.
4. **Method confusion**: "I should use more examples" is a METHOD, not a diagnosis. The diagnosis is which CRITERION failed. Methods come after.
5. **Flattery detection**: If your diagnosis concludes "the output was mostly good but needed X" — that's self-defense. Find what was actually wrong.

**The rule**: Your output was rejected. The rejection is correct. Find out why.

---

## Core Principles

1. **Criteria before methods.** Identify WHICH criterion failed before proposing HOW to fix it. "It needs more examples" is a method. "The reader doesn't recognize step 3 from experience" is a criterion failure. Diagnose criteria; methods follow.

2. **Upstream before downstream.** Test upstream criteria first (question, recognition, advancement, momentum, non-skippability, reader-drawn conclusion). If any upstream criterion fails, downstream diagnosis is premature — polished empty text is still empty.

3. **The user's rejection is data.** What exactly did the user say? What specific words did they use? Their feedback points to the failure — but often at a different level than the actual cause. "This is boring" might mean failed recognition, failed question, or failed advancement. Diagnose which.

4. **Same failure, different draft = wrong diagnosis.** If the output has been rejected multiple times, the prior diagnoses were wrong or incomplete. Don't repeat them. Find what they missed.

5. **Every finding gets tracked.** Number every diagnosis finding. Nothing gets lost in prose.

6. **Bedrock diagnosis.** Don't stop at "it failed recognition." WHY did it fail recognition? Which specific step? What did that step say that required evaluation instead of triggering recognition? Recurse until you hit a specific, fixable cause.

---

## Phase 1: EXPLORATION

### Step 1: Establish Context

```
OUTPUT TYPE: [what was produced — essay, draft, plan, code, etc.]
PRODUCING SKILL: [which skill generated it — /write, /qo, /ar, etc., or freeform]
ATTEMPT NUMBER: [1st, 2nd, 3rd, etc.]
USER FEEDBACK: [exact quotes from user's rejection]
PRIOR DIAGNOSES: [what was diagnosed in previous attempts, if any]
```

### Step 2: Parse the User's Feedback

The user's rejection contains signal. Unbundle it.

```
[S1] EXPLICIT: [what the user directly said was wrong]
[S2] IMPLICIT: [what the feedback implies about the failure]
[S3] PATTERN: [if multiple rejections — what pattern across feedback?]
[S4] LEVEL: [is the feedback about content? structure? voice? purpose? question?]
[S5] CONTRAST: [what did the user say they wanted instead, if anything?]
```

### Step 3: Test Upstream Criteria

For each upstream criterion from /write (or the relevant skill's criteria), test the rejected output against it. Number every finding.

**Criterion 1: Unresolved Question**
```
[S6] Does the document resolve a question the reader genuinely finds unresolved?
[S7] What question does it claim to resolve? [state it]
[S8] Is this question genuinely unresolved for the target reader? [YES/NO + why]
[S9] Does the reader care about this question? [YES/NO + why]
[S10] Is the question resolvable within this scope? [YES/NO + why]
```

**Criterion 2: Recognition**
```
[S11] Pick the weakest step — does the reader recognize it from experience?
[S12] Which specific steps REQUIRE EVALUATION instead of triggering recognition?
[S13] For each failed step: what does it say, and why doesn't the reader recognize it?
```

**Criterion 3: Advancement**
```
[S14] Does each recognized step connect to the question in a way the reader hadn't noticed?
[S15] Which steps are OBVIOUS (recognized but don't advance)?
[S16] Which steps are ANALYTICAL (advance but aren't recognized)?
```

**Criterion 4: Momentum**
```
[S17] Can the reader stop after any paragraph without feeling unresolved?
[S18] Where specifically does momentum die? [identify the paragraph]
[S19] Does each step create the question the next step answers?
```

**Criterion 5: Non-Skippability**
```
[S20] Which paragraphs can be removed without breaking the path to the conclusion?
[S21] List the skippable paragraphs — these are decoration, not structure.
```

**Criterion 6: Reader-Drawn Conclusion**
```
[S22] Does the reader arrive at the conclusion before it's stated?
[S23] Or does the document TELL the reader the conclusion? [quote the telling]
```

### Step 4: Identify the Failure Pattern

After testing all criteria, identify which ones failed and the pattern:

```
[S24] UPSTREAM FAILURES: [list which criteria failed — S-numbers]
[S25] FAILURE PATTERN: [see patterns below]
[S26] ROOT CAUSE: [what underlying issue caused these specific failures]
```

**Failure patterns:**
- **No question**: Output has no real unresolved question — everything else is decoration
- **Wrong question**: Question exists but reader doesn't care or already knows the answer
- **Conclusion-first**: Steps are compressed conclusions, not recognized experiences
- **Evaluation-heavy**: Steps require analysis instead of triggering recognition
- **No advancement**: Steps are recognized but obvious — reader says "yes, and?"
- **No momentum**: Steps don't create pull — reader can stop anywhere
- **Decorated emptiness**: Downstream criteria polished, upstream criteria broken
- **Same failure repeated**: Prior diagnosis was wrong — this attempt has the same problem

### Step 5: Test Prior Diagnoses (if attempt > 1)

```
[S27] Prior diagnosis was: [what was diagnosed before]
[S28] Did the fix address the actual failure? [YES/NO]
[S29] If NO — what did the prior diagnosis miss?
[S30] Is current failure the SAME as prior failure in different words? [YES/NO + evidence]
```

### Step 6: Derive What Must Change

Alternatives emerge from the diagnosis, not from intuition.

```
[S31] CRITERION [N] failed because: [specific cause — S-numbers]
[S32] To fix criterion [N]: [what must be different — derived from cause]
[S33] This means: [concrete implication for next attempt]
```

---

## Phase 2: FINDING REGISTRY

After exploration, compile EVERY finding. Nothing gets left out.

```
FINDING REGISTRY
================

FEEDBACK PARSED:
[S1] [text] -- TYPE: explicit
[S2] [text] -- TYPE: implicit
...

UPSTREAM CRITERION TESTS:
[S6] [text] -- CRITERION: unresolved question -- RESULT: [PASS/FAIL]
[S7] [text] -- CRITERION: unresolved question -- RESULT: [PASS/FAIL]
...
[S11] [text] -- CRITERION: recognition -- RESULT: [PASS/FAIL]
...

FAILURE PATTERN:
[S24] [text]
[S25] [text]
[S26] [text]

PRIOR DIAGNOSIS CHECK (if applicable):
[S27-S30] [text]

DERIVED FIXES:
[S31] [text] -- DERIVED FROM: [S-numbers]
[S32] [text] -- DERIVED FROM: [S-numbers]
...

TOTALS:
- Feedback findings: [N]
- Criteria tested: [N]
- Criteria failed: [N] ([list which])
- Criteria passed: [N] ([list which])
- Derived fixes: [N]
```

---

## Phase 3: SYNTHESIS

Derived entirely from the registry. No new findings.

```
OUTPUT: [what was produced]
ATTEMPT: [N]
USER SAID: [key quote]

DIAGNOSIS:
The output failed because: [root cause — S-numbers]

UPSTREAM STATUS:
| Criterion | Status | Evidence |
|-----------|--------|----------|
| Unresolved question | PASS/FAIL | S-numbers |
| Recognition | PASS/FAIL | S-numbers |
| Advancement | PASS/FAIL | S-numbers |
| Momentum | PASS/FAIL | S-numbers |
| Non-skippability | PASS/FAIL | S-numbers |
| Reader-drawn conclusion | PASS/FAIL | S-numbers |

FAILURE PATTERN: [name from Step 4]

ROOT CAUSE: [the deepest reason — S-numbers]

PRIOR DIAGNOSIS WAS: [wrong/incomplete/correct but poorly executed] — S-numbers

WHAT MUST CHANGE (derived from diagnosis):
1. [specific change — S-numbers]
2. [specific change — S-numbers]
3. [specific change — S-numbers]

WHAT MUST NOT CHANGE:
[What was already working — don't break it]

READY FOR:
- [next attempt with specific instructions derived from diagnosis]
- /ar [specific claim about the fix if uncertain]
- /qo [if the question needs to be found/reordered]
```

---

## Depth Scaling

| Depth | Min Feedback Findings | Min Criteria Tested | Min Total Findings |
|-------|----------------------|--------------------|--------------------|
| 1x | 3 | 4 | 15 |
| 2x | 5 | 6 | 25 |
| 4x | 8 | 6 | 40 |
| 8x | 12 | 6 | 65 |

Default: 2x. These are floors.

---

## Anti-Self-Defense Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Surface diagnosis** | "Needs better examples" or "needs more detail" | That's a method, not a diagnosis. Which CRITERION failed? |
| **Self-defense** | "The output was mostly good but..." | No. The output was rejected. Find what's wrong. |
| **Repeated diagnosis** | Same diagnosis as last time with different words | You already tried that fix and it didn't work. Find what's ACTUALLY wrong. |
| **Downstream fix for upstream failure** | Proposing voice/scope fixes when the question is wrong | Test upstream first. If question fails, nothing downstream matters. |
| **Vague root cause** | "It wasn't concrete enough" | Concrete about WHAT? Which step? What did it say? Why wasn't it recognized? |
| **Method prescription** | Fix section lists methods instead of criteria | State which criterion must pass. Method discovery is a separate step. |

---

## Pre-Completion Check

- [ ] User's feedback parsed (exact quotes, not paraphrased)
- [ ] All upstream criteria tested against the actual output
- [ ] Failed criteria identified with specific evidence (S-numbers pointing to specific output sections)
- [ ] Failure pattern named
- [ ] Root cause reaches a specific, fixable issue (not vague)
- [ ] Prior diagnoses checked for repetition (if attempt > 1)
- [ ] Derived fixes come from the diagnosis (S-number citations), not from intuition
- [ ] **Self-defense check**: If diagnosis says "mostly good" — go back
- [ ] **Repetition check**: If diagnosis matches a prior diagnosis — go deeper
- [ ] **Level check**: If fixes are about words/tone/style and upstream criteria failed — fix upstream first
