# /draft Write a first Reddit post introducing reasoningtool to r/ChatGPT
**Date:** 2026-03-09
**Skill:** /draft (Draft)

---

## PIECE METADATA

```
PURPOSE: Introduce reasoningtool to r/ChatGPT — get genuine interest from people who use AI for thinking
AUDIENCE: r/ChatGPT subscribers. They prompt daily, know chain-of-thought, have tried custom instructions and prompt libraries. Skeptical of self-promo. Interested in things that actually change how they work.
FORMAT: Reddit post (title + body)
LENGTH TARGET: 500-700 words
SINGLE SENTENCE: I built 592 structured thinking procedures as a free Claude Code plugin because AI helps you think faster but doesn't help you think in the right direction.
DRAFTS COMPLETED: 3
```

---

## Phase 1: DRAFT 1 — Structure Draft

### Skeleton

```
SECTION 1: Hook — the problem everyone recognizes
  JOB: Make the reader nod in recognition
  KEY CLAIM: AI helps you think faster but not necessarily better
  SUPPORT: Everyone has had the experience of getting a confident, well-written answer that misses the actual point
  EXIT: Reader feels "yeah, I've noticed that too"

SECTION 2: Why this happens — structural diagnosis
  JOB: Give the reader a framework for the problem
  KEY CLAIM: AI does what you ask, but has no mechanism to check whether what you asked is the right question
  SUPPORT: Examples — ask it to evaluate your plan, it evaluates. It doesn't ask if you're solving the right problem.
  EXIT: Reader understands this is a direction problem, not an intelligence problem

SECTION 3: What I built — concrete description
  JOB: Show the reader what exists
  KEY CLAIM: 592 structured thinking skills as a Claude Code plugin, free and open-source
  SUPPORT: Category skills that route your input, core methods (ARAW, UAUA), examples of use
  EXIT: Reader has a mental model of what this actually is

SECTION 4: What it looks like in practice — example
  JOB: Make it tangible
  KEY CLAIM: You type a slash command and get structured analysis, not just prose
  SUPPORT: Concrete example of using a skill
  EXIT: Reader can picture themselves using it

SECTION 5: Honest accounting — what's proven vs. claimed
  JOB: Build credibility through honesty
  KEY CLAIM: The structural guarantees are real; the empirical claims are untested
  SUPPORT: Assume-right/assume-wrong logically forces consideration of alternatives. Whether that produces better decisions is unproven.
  EXIT: Reader trusts me because I'm not overselling

SECTION 6: Call to action — try it, break it
  JOB: Give the reader a next step
  KEY CLAIM: It's free, it's on GitHub, and I want people to find where it fails
  SUPPORT: Link to repo, link to website
  EXIT: Reader knows exactly how to try it
```

**Finding A — Skeleton completeness**: KEY CLAIM lines read top-to-bottom form a coherent arc: problem → why → what → example → honesty → action. Flows well.

### Draft 1 (raw)

Title: I built 592 structured thinking skills for Claude Code because AI helps you think faster — but not necessarily in the right direction

Body:

Here's something I keep running into. I ask an AI to evaluate my plan. It evaluates my plan. Thoroughly, confidently, with bullet points. But it never asks whether my plan is solving the right problem. I ask it to brainstorm alternatives. It gives me 10. But it doesn't test whether any of them survive scrutiny. I ask it to check my reasoning. It checks. But it doesn't notice what I never considered.

This isn't an intelligence failure. The model is doing exactly what I asked. The issue is that what I asked might be wrong, and nothing in the interaction catches that.

So over the past year I've been building something to address this. reasoningtool is 592 structured thinking procedures — a Claude Code plugin where each skill is a specific, repeatable reasoning method. It's free, open-source, MIT licensed.

The core idea: instead of just prompting for answers, you run your thinking through structured procedures that force you to check direction, not just speed.

Some examples of what that means in practice:

- `/claim should I change careers` — runs ARAW (Assume Right / Assume Wrong), which branches your claim into two trees: what follows if true, what follows if false. Then recurses — each conclusion becomes another claim to test. You end up with a map of your assumption's consequences in both directions.

- `/diagnose why does my team keep missing deadlines` — runs UAUA, which alternates between exploring the full space of possible causes and testing each one. Four passes: explore, test, find edge cases of survivors, validate. The alternation matters because exploration and testing have complementary blind spots.

- `/decide` routes your decision to the right analytical method — comparison, cost-benefit, goal clarification — based on what kind of decision it actually is.

There are 17 category skills that classify your input and route it, plus hundreds of direct skills for specific operations: decomposition, assumption extraction, pre-mortems, hypothesis testing, root cause analysis, and more. Each skill is a structured procedure, not a prompt template. The instructions specify what to do at each step, what to check, and what to do when you get stuck. [FIX: too much detail, cut in draft 2]

What I'm honest about: the structural guarantees are real. If you test "assume right" and "assume wrong," you will consider alternatives you wouldn't have otherwise — the operation forces it. If you alternate exploration and testing, you cover failure modes that either alone misses. But whether all of this produces measurably better decisions than just asking a smart question — that's unproven. This is v1 of an experimental approach. I think it works. I want to find out where it breaks.

Website: [reasoningtool.com](https://reasoningtool.com)
GitHub: [github.com/benjam3n/reasoningtool](https://github.com/benjam3n/reasoningtool)

```bash
git clone https://github.com/benjam3n/reasoningtool.git
cd reasoningtool/claude-code-plugin
claude
```

Then type `/claim` or `/decide` or `/diagnose` followed by whatever you're thinking about.

If you try it and it falls apart on something — that's genuinely useful feedback. The toolkit improves when people use it on problems I didn't anticipate. [FIX: ending is weak]

**Finding B — Coverage check**: All 6 skeleton sections have content. No gaps.

---

## Phase 2: DRAFT 2 — Logic Draft

### Paragraph Audit

```
¶1 JOB: Show the problem through concrete experience
    CLAIM: AI evaluates what you ask but doesn't check whether the question is right
    SUPPORT: Three examples (evaluate plan, brainstorm alternatives, check reasoning)
    CONNECTS TO NEXT VIA: therefore (this leads to a diagnosis)

¶2 JOB: Name the structural diagnosis
    CLAIM: This is a direction failure, not an intelligence failure
    SUPPORT: The model does what you asked; nothing catches wrong questions
    CONNECTS TO NEXT VIA: therefore (I built something to address it)

¶3 JOB: Introduce what exists
    CLAIM: 592 structured thinking procedures, free, open-source
    SUPPORT: Factual description
    CONNECTS TO NEXT VIA: specifically (here's the core idea)

¶4 JOB: State the core design principle
    CLAIM: Structured procedures that check direction, not just speed
    SUPPORT: Implied by the problem statement
    CONNECTS TO NEXT VIA: specifically (examples follow)

¶5 JOB: Show concrete examples
    CLAIM: Skills do specific, structured operations
    SUPPORT: Three examples with what actually happens
    CONNECTS TO NEXT VIA: meanwhile (broader inventory)

¶6 JOB: Describe the broader skill set
    CLAIM: 17 category skills plus hundreds of direct skills
    SUPPORT: Lists of skill types
    CONNECTS TO NEXT VIA: however (honesty caveat)

¶7 JOB: Honest accounting of claims vs. evidence
    CLAIM: Structural guarantees are real; empirical claims are untested
    SUPPORT: Logical argument for why ARAW forces alternatives; admission that decision quality is unproven
    CONNECTS TO NEXT VIA: therefore (try it)

¶8 JOB: Provide links and getting-started
    CLAIM: Here's how to try it
    SUPPORT: Website, GitHub, install instructions
    CONNECTS TO NEXT VIA: specifically (what to type)

¶9 JOB: Call to action
    CLAIM: Feedback on failures is welcome
    SUPPORT: Toolkit improves from unexpected use cases
    CONNECTS TO NEXT VIA: terminal
```

**Finding C — Paragraph failures**:
- ¶4 is thin — "check direction, not just speed" restates the problem without adding new information. Merge into ¶3.
- ¶6 has too much detail for Reddit. Cut the inventory list; the examples in ¶5 already make it tangible. Keep one sentence about scope.
- ¶9 ending is weak — "genuinely useful feedback" sounds like boilerplate. Make it more specific.

### Argument Flow Test

First sentences read in sequence:
1. "Here's something I keep running into."
2. "This isn't an intelligence failure."
3. "So over the past year I've been building something to address this."
4. "The core idea: instead of just prompting..."
5. "Some examples of what that means..."
6. "There are 17 category skills..."
7. "What I'm honest about..."
8. "Website: reasoningtool.com"
9. "If you try it and it falls apart..."

**Finding D — Buried leads**: ¶1 opener is fine for Reddit (casual hook), but ¶4's first sentence is vague. Fixed by merging into ¶3. ¶8 has no real first sentence — it's just a link. Acceptable for the format. 1 buried lead fixed.

### Cut and Restructure

- Merged ¶4 into ¶3 (one sentence about design principle added to intro paragraph)
- Cut most of ¶6 — kept one sentence about scope, moved it into the examples section
- Strengthened ¶9 ending — made it about specific curiosity rather than generic feedback request
- Resolved [FIX] markers

**Finding E — Revision delta**: 3 of 9 paragraphs changed (33%) — merged 1, cut 1, rewrote 1. Above 10% threshold.

---

## Phase 3: DRAFT 3 — Prose Draft

### Tone Audit

```
INTENDED TONE: Conversational but substantive — fellow practitioner sharing a tool, not marketer pitching a product
TONE BREAKS: "MIT licensed" is jargon that breaks conversational tone — changed to just "free and open-source"
REGISTER SHIFTS: The ARAW/UAUA explanations get slightly technical — acceptable because the audience is technical
```

**Finding F — Tone consistency**: One minor break fixed (MIT licensed → open-source). Otherwise consistent throughout.

### Sentence-Level Pass

- Replaced "This isn't an intelligence failure" with "This isn't a capability problem" (more natural for the audience)
- Cut "Thoroughly, confidently, with bullet points" — showing off, not earning its words
- Shortened UAUA explanation — kept alternation concept, cut the "four passes" detail
- Varied sentence openings in the examples section (was repetitive with "runs...")
- Cut hedge stack in honesty section ("But whether all of this produces measurably better decisions than just asking a smart question" → simpler version)

### Final Cut

Draft 1: ~620 words. Draft 2: ~540 words. Draft 3 target: ~500 words. Cut: weakest example detail, one redundant sentence in the opener, throat-clearing in the CTA.

---

## FINDINGS

```
A — Skeleton completeness: Complete. KEY CLAIM sequence forms coherent arc.
B — Coverage check: All sections covered, no gaps.
C — Paragraph failures: 2 found (thin paragraph merged, over-detailed paragraph cut). 0 remaining.
D — Buried leads: 1 found and fixed.
E — Revision delta: 33% of paragraphs changed in Draft 2.
F — Tone consistency: 1 minor break fixed. Consistent in final.
```

## REVISION METRICS

```
Draft 1 word count: ~620
Draft 2 word count: ~540
Draft 3 word count: ~490
Paragraphs cut: 2 (merged into others)
Paragraphs added: 0
Unsupported claims remaining: 0
```

---

## THE FINAL DRAFT

### Title

**I built 592 structured thinking skills for Claude Code because AI helps you think faster — but not necessarily in the right direction**

### Body

Here's something I keep running into. I ask an AI to evaluate my plan. It evaluates my plan. But it never asks whether my plan is solving the right problem. I ask it to brainstorm alternatives. It gives me ten. But it doesn't test whether any of them actually hold up. I ask it to check my reasoning. It checks — but it doesn't notice what I never considered.

This isn't a capability problem. The model does exactly what I asked. The issue is that what I asked might be wrong, and nothing in the interaction catches that.

Over the past year I've been building something to address this. [reasoningtool](https://reasoningtool.com) is 592 structured thinking procedures as a Claude Code plugin — free, open-source. Instead of prompting for answers, you run your thinking through procedures that check *direction*, not just speed.

Some examples:

- **`/claim should I change careers`** — branches your claim into two trees: what follows if this is true? what follows if it's false? Then recurses on each conclusion. You end up with a map of consequences in both directions, not just the one you were already leaning toward.

- **`/diagnose why does my team keep missing deadlines`** — alternates between exploring the full space of possible causes and testing each one. Exploration alone finds options but can't tell you which work. Testing alone validates what you're looking at but misses what you're not. The alternation covers both blind spots.

- **`/decide`** — classifies what kind of decision you're actually facing and routes it to the right method: comparison, cost-benefit, goal clarification, or something else. Because "I need to decide" doesn't tell you *how* to decide.

There are 17 category skills that route your input to the right analysis, plus ~575 direct skills covering decomposition, assumption extraction, pre-mortems, hypothesis testing, root cause analysis, and more. Each one is a structured procedure with specific steps, not a prompt template.

What I want to be honest about: the structural guarantees are real. If you test both "assume true" and "assume false," you *will* consider alternatives you wouldn't have otherwise — the operation forces it. But whether this produces measurably better decisions than just thinking carefully on your own? Unproven. This is v1 of an experimental approach. I think it works. I want to find out where it breaks.

GitHub: [github.com/benjam3n/reasoningtool](https://github.com/benjam3n/reasoningtool)
Website: [reasoningtool.com](https://reasoningtool.com)

```
git clone https://github.com/benjam3n/reasoningtool.git
cd reasoningtool/claude-code-plugin
claude
```

Then type `/claim` or `/decide` or `/diagnose` followed by whatever you're actually thinking about.

I'm especially curious what happens when people use it on problems I never anticipated — that's where structured methods either prove themselves or expose their limits. If it falls apart on something, I'd like to hear about it.

---

## Pre-Completion Checklist

- [x] Skeleton was built before any prose was written
- [x] Every paragraph has a stated job (one clause, no duplicates)
- [x] Every claim has support (no unsupported assertions remain)
- [x] Every transition states a logical relationship (no filler connectors)
- [x] Draft 3 is shorter than Draft 1 (620 → 490)
- [x] Tone is consistent throughout (conversational-substantive, no register shifts)
- [x] First sentences of paragraphs produce a coherent summary when read alone
- [x] All [FIX] markers and placeholder brackets are resolved
