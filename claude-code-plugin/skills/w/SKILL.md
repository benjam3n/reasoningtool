---
name: w
description: Generative writing tool. Criteria-based specification for satisfying prose. Organized hierarchically — upstream criteria determine whether writing works; downstream criteria determine how well.
---

# High Quality Writing

**Input**: $ARGUMENTS

---

## How This Skill Works

This skill defines writing quality as **objective criteria** — properties the text either has or doesn't. Criteria are not methods. Methods are ways to achieve criteria. Methods are Goodhartable (you can follow "show don't tell" and still write badly). Criteria are the check (does the reader recognize this from experience? Binary.).

Criteria are **hierarchical**. Upstream criteria determine whether writing works at all. Downstream criteria determine how well it works. Fixing downstream while upstream is broken produces polished, empty text.

---

## Step 0: Define the Reader

Criteria are objective relative to a specified reader. Before writing, define:

```
WHO: [Who is reading this? What do they know already?]
NEED: [What do they need after reading? Knowledge? Capability? Decision?]
UNRESOLVED: [What question does the reader genuinely find unresolved?]
STATE AFTER: [What should the reader believe/know/feel after reading?]
```

The reader definition determines how every criterion is evaluated. "Does the reader recognize this?" depends on who the reader is.

---

## Upstream Criteria

These determine whether writing works at all. If any upstream criterion fails, no amount of downstream polish will save the document.

### Criterion 1: Unresolved Question

The document resolves a question the reader genuinely finds unresolved.

| Property | Test |
|----------|------|
| **Unresolved** | "Does the reader already know the answer?" → must be NO |
| **Cares** | "Would the answer change something the reader thinks, does, or feels?" → must be YES |
| **Resolvable** | "Does the question feel answerable within this document's scope?" → must be YES |

**Failure modes:**
- Already resolved for the reader → boring ("I already know this")
- Reader doesn't care → irrelevant ("who cares?")
- Too abstract/unbounded → frustrating ("that's unanswerable")
- Too concrete → trivial ("obviously yes/no")

The question can be established implicitly (reader discovers they have it) or explicitly (stated). Implicit is stronger — the reader owns a question they discovered.

### Criterion 2: Recognition

Each step (sentence/paragraph) is immediately recognized by the reader from their own experience — no evaluation required.

| Property | Test |
|----------|------|
| **Recognized** | "Has the reader experienced this?" → must be YES |
| **Immediate** | "Does the reader accept this without analysis?" → must be YES |

The distinction: **recognition vs evaluation.** "You say things to a close friend you'd never say at work" → instant recognition. "Judgment is a constraint" → requires evaluation (the reader must check this against experience). Recognition and evaluation are different cognitive processes. A sentence that requires evaluation is not satisfying even if the reader ultimately agrees.

Recognition does NOT mean obvious or dumbed down. The best recognized sentences articulate something the reader has experienced but never put into words — "I always knew that but never said it." This produces strong engagement, distinct from both "I already knew that" (boring) and "I'm not sure that's true" (resistance).

### Criterion 3: Advancement

Each step connects the reader's recognized experience to the unresolved question in a way they hadn't noticed before.

| Property | Test |
|----------|------|
| **Connects** | "Had the reader connected this experience to the question before?" → must be NO |
| **Advances** | "Does this step move the reader closer to resolving the question?" → must be YES |

**Recognition alone = obvious** ("yes, and?"). **Advancement alone = analytical** ("I'd need to check that"). **Both together = satisfying** ("oh, of course — and that means...").

### Criterion 4: Momentum

Each step creates the question that the next step answers. The reader always knows why they're reading the current sentence.

| Property | Test |
|----------|------|
| **Creates pull** | "Does this step make the reader want the next one?" → must be YES |
| **Continuous** | "Could the reader stop reading here and feel resolved?" → must be NO (until the end) |

A document with momentum: can't stop reading. A document without momentum: could stop after any paragraph. If a reader can stop at any point without feeling something is unresolved, the document lacks momentum.

### Criterion 5: Non-Skippability

No step can be removed without breaking the reader's path to the conclusion.

| Property | Test |
|----------|------|
| **Necessary** | "Remove this step — does the reader still arrive at the conclusion?" → must be NO |

This is proof structure. Each step is a lemma verified against the reader's experience. The conclusion is a theorem. If you can remove a paragraph and the conclusion still arrives, that paragraph was decoration.

### Criterion 6: Reader-Drawn Conclusion

The reader arrives at the conclusion before it is stated. The conclusion forms in the reader's mind from the accumulation of recognized, advancing steps.

| Property | Test |
|----------|------|
| **Pre-arrived** | "Did the reader reach this conclusion before reading it?" → must be YES |
| **Confirmation** | "Does stating the conclusion feel like confirmation, not revelation?" → must be YES |

A conclusion the reader reached themselves produces ownership ("yes, exactly"). A conclusion stated by the writer produces evaluation ("prove it"). The writer's job is to select and order steps. The conclusion is the reader's.

---

## Downstream Criteria

These determine how well the writing works, given that upstream criteria are met. Fix these ONLY after upstream criteria pass.

### Criterion 7: Precise Scope

Every claim is scoped exactly right for the reader. No sweeping generalizations a smart reader could counterexample. No condescending statements that waste the reader's time.

| Property | Test |
|----------|------|
| **Survives AW** | "Could the smartest adversarial reader destroy this with a counterexample?" → must be NO |
| **Not condescending** | "Would the reader say 'duh' or 'obviously'?" → must be NO |

Assume the reader is smarter than the writer. Precision is respect. Condescension is insult.

### Criterion 8: Voice Match

Voice matches the document's purpose and the reader's expectations.

| Context | Voice | Characteristics |
|---------|-------|-----------------|
| **Technical docs** | Precise, neutral | Short sentences. Active voice. No metaphor. |
| **Essays/arguments** | Confident, direct | State positions. Show reasoning. |
| **Tutorials** | Warm, clear | Second person. Concrete examples. |
| **Academic** | Measured, qualified | Precise hedging (when warranted). Citations. |
| **Narrative** | Vivid, concrete | Sensory detail. Specific scenes. |
| **Principles/philosophy** | Dense, impersonal | No "you." No commands. No theories. Each sentence unobjectionable. |

### Criterion 9: No Weak Patterns

After drafting, scan for these. Each is a criterion violation:

| Pattern | What It Violates | Fix |
|---------|-----------------|-----|
| **Hedging qualifiers** ("could potentially perhaps") | Precise scope | State it or cut it |
| **Defensive negation** ("It's not that X is wrong...") | Advancement (wastes a step) | Say what IS true |
| **Passive responsibility** ("Mistakes were made") | Recognition (who?) | Name the actor |
| **Weasel words** ("Some experts say...") | Recognition (which?) | Name them or cut |
| **Throat-clearing** ("It's worth noting...") | Momentum (stalls) | Start with the point |
| **Summary-like statements** ("As we've discussed...") | Advancement (doesn't advance) | Advance or cut |
| **Contestable sentence** | Precise scope | Rewrite until no counterexample exists |
| **Second-person commands** ("Think about," "Consider") | Recognition (presumes experience) | Use impersonal observation |
| **Theoretical claims** ("The brain optimizes for...") | Recognition (requires evaluation) | Replace with the observable thing |
| **Persuasive structure** (build-up → conclusion) | Reader-drawn conclusion (writer arguing) | Let steps accumulate; reader concludes |

### Criterion 10: Claim Verification

Every factual claim has a source marker:
- `[O: source]` — Observed from a specific source
- `[T: test]` — Testable prediction
- `[D: premises]` — Derived from stated premises

Unmarked claims are opinions. That's fine — but know which is which.

---

## The Writing Process

### 1. Define the reader (Step 0 above)

### 2. Identify the unresolved question

What does the reader genuinely find unresolved that this document answers? Test: unresolved? cares? resolvable? If any test fails, find a different question.

### 3. Find the steps

For each step in the resolution path, find an experience the reader has had that connects to the question in a way they haven't noticed. Each step must pass:
- Recognition: reader has experienced this
- Advancement: reader hadn't connected it to the question
- Momentum: this step creates the question the next step answers
- Non-skippability: removing this step breaks the path

### 4. Order the steps

Each step must make the next step recognizable. The order that produces the highest recognition at each point is the correct order. Test: present step B before step A — does the reader recognize A? Now reverse. The order where each step is recognizable in context is the right order.

### 5. Check upstream criteria

Before polishing: does the document have a question? Does each step pass recognition + advancement? Is there momentum? Can you remove any paragraph without breaking the path? Does the reader arrive at the conclusion before it's stated?

If ANY upstream criterion fails, fix it before touching downstream.

### 6. Check downstream criteria

After upstream passes: scope, voice, weak patterns, claim verification.

---

## Structure Patterns

| Reader Need | Structure |
|-------------|-----------|
| Understand a concept | Definition → Example → Contrast → Edge cases |
| Make a decision | Options → Criteria → Comparison → Recommendation |
| Learn to do something | Goal → Prerequisites → Steps → Verification → Troubleshooting |
| Understand what happened | Context → Events → Consequences → Lessons |
| Arrive at a principle | Recognized experience → What follows → Deeper experience → What that implies → The principle (as confirmation of what reader already sees) |

---

## Pre-Completion Check

### Upstream (must ALL pass — if any fails, do not proceed to downstream)

- [ ] Reader defined (who, what they know, what's unresolved for them)
- [ ] Unresolved question identified and tested (unresolved? cares? resolvable?)
- [ ] Every step passes recognition (reader has experienced this, accepts immediately)
- [ ] Every step passes advancement (connects experience to question in new way)
- [ ] Document has momentum (reader can't stop at any point without feeling unresolved)
- [ ] Every step is non-skippable (removing any step breaks the path)
- [ ] Reader arrives at conclusion before it is stated

### Downstream (fix after upstream passes)

- [ ] Every claim precisely scoped (survives AW from smartest reader, not condescending)
- [ ] Voice matches purpose
- [ ] Weak patterns scanned and fixed
- [ ] Claims verified with source markers where applicable
- [ ] No recognizable persuasive genre (not self-help, not sermon, not TED talk)
