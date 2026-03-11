# /persua What's the most persuasive framing for why someone should try reasoningtool?
**Date:** 2026-03-09
**Skill:** /persua (Persuasion Analysis)

---

**Interpretation selected: Audience persuasion** — persuading a group (AI power users who already use Claude/AI) to try a free product from a solo developer.

## Corruption Pre-Inoculation

Persuasion analysis for your own product risks self-serving framing disguised as audience understanding. I'll flag any place where the analysis drifts toward "what sounds good" rather than "what's actually true for this audience." The transparency test applies doubly here: if the target audience saw this strategy document, they should think "yeah, that's fair" not "I'm being played."

---

## Phase 1: AUDIENCE MODEL

### Step 1: Define the Persuasion Target

```
TARGET: AI power users — people who already use Claude, ChatGPT, or similar tools regularly
        and want better outputs. Skews technical, self-directed, skeptical of hype.
GOAL: Get them to install reasoningtool and use it at least once on a real problem.
CONTEXT: Discovery via Reddit, HN, Twitter, GitHub — text-based, low-trust, high-noise environments.
         They'll see a post or comment, spend 5-30 seconds deciding whether to click.
RELATIONSHIP: Stranger. Solo developer with no established authority. They have zero reason to trust you.
```

### Step 2: Map Their Current Belief State

```
BELIEF MAP
==========

CURRENT POSITION: "I already know how to prompt AI well. I don't need a plugin
to think for me — I just need to ask better questions."

SUPPORTING BELIEFS (what holds their current position in place):
- [B1] "I've gotten good at prompting through experience. My workflow already works."
- [B2] "Most AI tools/plugins are either trivial wrappers or overhyped vaporware."
- [B3] "592 skills sounds like quantity over quality — probably auto-generated slop."
- [B4] "If structured thinking prompts were that useful, they'd already be built into the model."
- [B5] "Free products from solo devs are usually abandoned or half-baked."

VALUES AT STAKE (what they care about that connects to this topic):
- [V1] Craft pride — they take pride in being good at using AI. Something that implies
        they need help can feel like an insult to their competence.
- [V2] Time efficiency — they won't invest time in something that doesn't immediately
        pay off. Exploration budget is near zero.
- [V3] Intellectual honesty — they respect evidence and genuine quality. They'll change
        their mind if shown something real, but NOT from hype.
- [V4] Autonomy — they want tools that extend their capability, not tools that constrain
        or prescribe their workflow.
- [V5] Distaste for marketing — this audience pattern-matches on "selling" and discounts it
        immediately. Authenticity reads as signal; polish reads as noise.

IDENTITY CONNECTION: YES — moderate-to-high difficulty.
- Identity claim: "I'm the kind of person who figures things out myself."
- Group membership: "Power users don't need training wheels."
- This means: Framing that implies they're doing it wrong will FAIL. Framing that
  extends what they can already do will SUCCEED.

INFORMATION STATE:
- What they know: AI can be prompted well. Chain-of-thought helps. Some prompt patterns
  work better than others.
- What they don't know: The specific difference between ad-hoc prompting and a structured
  analytical procedure. That skills can chain. That the skill format includes corruption
  pre-inoculation, failure modes, and depth scaling — things most people never build into
  their prompts.
- What they believe that's wrong: That their best ad-hoc prompt is close to the ceiling
  of what structured guidance can produce. (It isn't — there's a large gap between "think
  step by step" and a 200-line analytical procedure with named failure modes.)

EMOTIONAL STATE:
- How they feel about this topic: Mildly interested but deeply skeptical. Inundated with
  AI tools. "Tool fatigue" is high.
- What threatens them about your position: The implication that their current approach
  leaves significant quality on the table. That's a competence threat.
```

### Step 3: Map Resistance Points

```
RESISTANCE ANALYSIS
===================

[R1] "592 skills sounds like quantity-farming, not quality"
  Type: EVIDENTIAL — they infer low quality from high quantity
  Strength: HIGH
  Addressable: YES — by showing ONE skill in detail and letting quality speak

[R2] "I already prompt well — I don't need this"
  Type: IDENTITY — admitting they need it means admitting a gap
  Strength: HIGH
  Addressable: PARTIALLY — can reframe as "extending range" not "fixing a deficit,"
  but some identity resistance will remain

[R3] "Solo dev, free product — will it be maintained? Is it serious?"
  Type: PRACTICAL — legitimate concern about longevity and quality
  Strength: MEDIUM
  Addressable: YES — open source, they can see the repo, read the code, fork it

[R4] "I don't want to learn a new system with 592 commands"
  Type: PRACTICAL — perceived learning cost is too high
  Strength: HIGH
  Addressable: YES — you don't need to learn 592 skills. You type /decide and it
  routes for you. Entry point is ONE command, not 592.

[R5] "This is probably just prompt templates dressed up"
  Type: EVIDENTIAL — they'll assume the simplest explanation
  Strength: MEDIUM
  Addressable: YES — showing the actual structure (phases, failure modes, corruption
  pre-inoculation, depth scaling, skill chaining) proves it's not a template

PRIMARY RESISTANCE: [R2] — the identity-connected belief that they don't need help
thinking. If you trigger this, no amount of evidence about quality will land.
Everything else is downstream of whether you can avoid threatening their competence.
```

---

## Phase 2: STRATEGY CONSTRUCTION

### Step 4: Find the Persuasion Path

```
PERSUASION PATH
===============

STARTING POINT: "I already know that structured prompting produces better outputs than
vague prompting." [They already believe this — it's why they're power users.]
  ↓ connects to
BRIDGE BELIEF: "But there's a difference between the structure I improvise in the moment
and a structure that was designed, tested, and refined over hundreds of iterations.
Same as the difference between writing code from scratch vs. using a well-designed library."
  ↓ connects to
TARGET BELIEF: "reasoningtool is a library of structured thinking procedures I can call
when I need them — it doesn't replace my judgment, it gives me better scaffolding."

WHY THIS PATH WORKS: It validates their existing skill (you're already good at this),
acknowledges the principle they already accept (structure helps), and extends it to
a natural conclusion (curated structure > improvised structure) using an analogy they
already live by (libraries > writing from scratch).

ALTERNATIVE PATH (if primary fails):

STARTING POINT: "I've noticed that AI gives qualitatively different outputs when I give
it detailed analytical frameworks vs. general instructions."
  ↓ connects to
BRIDGE BELIEF: "Building those frameworks from scratch every time is possible but
inefficient — and I probably miss failure modes I'm not thinking about."
  ↓ connects to
TARGET BELIEF: "Having pre-built, refined analytical procedures available on demand
makes me faster AND more thorough."
```

### Step 5: Design the Message

```
MESSAGE ARCHITECTURE
====================

OPENING: "You already know that HOW you prompt matters. You've probably noticed
that when you give Claude a detailed analytical framework — specific steps, specific
failure modes to check — you get qualitatively different output than when you say
'analyze this for me.' reasoningtool is 592 of those frameworks."
  Why this works: Validates B1 (they're already good), connects to V1 (craft pride),
  frames the tool as extending their existing insight rather than correcting a deficit.

RESISTANCE RESPONSE for [R1] ("592 = quantity over quality"):
  Acknowledge: "592 skills sounds like it could be auto-generated slop. Fair."
  Address: Show one skill. Pick /rca or /dcp — let them read the actual SKILL.md file.
  200+ lines of structured procedure with phases, failure modes, corruption pre-inoculation,
  depth scaling. Then say: "They're all like this."
  Bridge: "You can judge quality in 30 seconds by reading one skill file. It's all in
  the repo."

RESISTANCE RESPONSE for [R2] ("I don't need this"):
  Acknowledge: DO NOT ADDRESS THIS DIRECTLY. Never say "you need this."
  Address: Instead, demonstrate. Show a before/after — the same question with and without
  a skill. Let the output quality gap speak. Frame as: "Here's what /rca produces on a
  debugging problem" — not "here's what you're missing."
  Bridge: "It's not about needing it. It's about whether you'd rather improvise the
  analytical framework every time or call one that's already been refined."

RESISTANCE RESPONSE for [R4] ("I don't want to learn 592 commands"):
  Acknowledge: "You don't need to learn 592 skills."
  Address: "Type /decide when you have a decision. Type /claim when you have a claim to
  test. These category skills figure out which analytical tool to use. You learn maybe
  5-6 entry points and the system routes from there."
  Bridge: Connects to V2 (time efficiency) — low learning cost, immediate payoff.

RESISTANCE RESPONSE for [R5] ("Just prompt templates"):
  Acknowledge: "If these were prompt templates I wouldn't have built 592 of them."
  Address: Each skill has: phased execution, interpretation matching, corruption
  pre-inoculation (checking for ways the analysis could deceive itself), typed failure
  modes, depth scaling, and cross-skill invocation. It's closer to a standard library
  than a template collection.
  Bridge: "Read one SKILL.md file and you'll see the difference in about 10 seconds."

CORE ARGUMENT: "You already structure your prompts. This is 592 pre-built, refined
analytical procedures — a standard library for thinking. Type /decide with your
decision, or /claim with your claim, and get a structured analysis that would take
you 20 minutes to scaffold yourself. It's free, it's open, and you can read every
line of every skill before you use it."
  Evidence they'll find credible: The actual skill files. Source code. Before/after
  output comparisons. Their own experience running one skill on a real problem.
  Evidence they'll dismiss: Testimonials (too few users), metrics (unverifiable),
  claims about "AI-powered" anything (pattern-matches as hype), your own enthusiasm
  (you're the builder, of course you think it's good).

WHAT NOT TO SAY:
- "Most people prompt AI wrong" — competence threat, triggers R2, dead on arrival
- "Revolutionary/game-changing/breakthrough" — hype vocabulary, instant credibility loss
- "AI-powered thinking tool" — meaningless to this audience, reads as marketing
- "Save hours of time" — unverifiable claim, this audience wants to verify before believing
- Anything that implies they're not already good at this
- Anything that sounds like you're selling (they'll discount it 10x)

ASK: "Install it, run /decide on a decision you're actually facing, and see if the
output is better than what you'd get without it. Takes 2 minutes."
```

### Step 6: Check the Ethics

```
ETHICS CHECK
============

Transparency test: If the target saw this entire analysis, would they feel:
- [x] Understood and respected → ETHICAL
  (The analysis accurately represents their beliefs and respects their competence.
  The strategy is: show them something real and let them judge.)

Autonomy test: Does the strategy:
- [x] Present genuine evidence for a genuine benefit → YES
  (The core move is: "read a skill file, run it on a real problem, judge for yourself.")

Reciprocity test: Would you be comfortable if someone used this strategy on YOU?
- [x] Yes → proceed
  (This is essentially: understand what I care about, don't insult my competence,
  show me something real, and let me decide. That's how I'd want to be approached.)

FLAGS: None. The strategy relies entirely on the product being genuinely good.
If the skills aren't actually high quality, this strategy fails — and it should.
No manipulation is covering for a weak product here.
```

---

## Phase 3: SYNTHESIS

### Step 7: Compile the Persuasion Plan

```
PERSUASION ANALYSIS: Get AI power users to try reasoningtool
============================================================

TARGET: People who already use Claude/AI well and want better outputs
CURRENT STATE: "I prompt well already. 592 skills sounds like hype. I don't need help."
DESIRED STATE: Install, run one skill on a real problem, experience the quality gap
DIFFICULTY: MEDIUM-HIGH — identity-connected ("I'm already good at this") but
addressable because the audience values evidence and will change their mind if shown proof

PRIMARY RESISTANCE: [R2] — identity-connected belief that they don't need help.
Must never be challenged directly.

PERSUASION PATH: "You already structure your prompts" → "curated structure > improvised
structure, same as libraries > writing from scratch" → "this is a standard library for thinking"

KEY MOVES:
1. VALIDATE first — "You already know structured prompting works" (connects to V1, craft pride)
2. SHOW, don't tell — link to one actual SKILL.md file, let quality speak (addresses R1, R5)
3. REFRAME the value — "Not replacing your skill, extending your range. Like using a
   library instead of writing from scratch every time" (addresses R2 without threatening identity)
4. LOWER the bar — "Install, run /decide on something real, 2 minutes" (addresses R4, connects to V2)

WHAT WILL NOT WORK (and why):
- Hype language ("revolutionary," "game-changing") — this audience pattern-matches
  on hype and discounts instantly. V5 (distaste for marketing) kills it.
- Claiming they need it — triggers R2 (identity defense). They'll reject the
  tool to protect their self-image as competent prompters.
- Emphasizing quantity ("592 skills!") as a feature — triggers R1 (quantity = low quality).
  Quantity is a liability until quality is established.
- Testimonials or social proof — insufficient user base to be credible, and this
  audience trusts their own judgment over others' endorsements.
- Explaining the system in detail before they've experienced it — too much cognitive
  investment for an unproven tool. Show, then explain.

TIMELINE EXPECTATION: Single interaction — they either try it in the next 5 minutes
or they don't. This audience doesn't "come back later." The first impression IS the
persuasion window.

CONTINGENCY: If primary path fails (they don't click through to a skill file), shift to
alternative path: post a before/after comparison showing the SAME question with and without
a skill. Let output quality be the hook instead of the product description.

ETHICAL STATUS: CLEAN — strategy relies entirely on genuine product quality and respects
audience autonomy to judge for themselves.
CONFIDENCE: MEDIUM-HIGH
WEAKEST ASSUMPTION: That the quality gap between "good ad-hoc prompting" and "running
a reasoningtool skill" is large enough to be obvious in a single demonstration. If
power users' improvised structure is already close to what the skills provide, the
"try it and see" strategy produces a shrug instead of a conversion. The entire
strategy depends on the product actually being meaningfully better — which is the
right dependency to have.
```

---

## The Framing, Distilled

**Most persuasive single-sentence framing:**

> "You already know that giving Claude structured analytical frameworks produces better output than vague prompts — reasoningtool is 592 of those frameworks, pre-built and refined, callable with a slash command."

**Why this works against every resistance point:**
- Validates their competence (R2) — "you already know"
- Explains what it IS in concrete terms (R5) — "structured analytical frameworks"
- Sidesteps the quantity objection (R1) — frames 592 as depth of library, not hype
- Implies low learning cost (R4) — "callable with a slash command"
- No hype vocabulary — reads as description, not marketing

**The analogy that does the most work:** "Standard library for thinking." Every developer understands that you COULD write everything from scratch, and that using a well-designed library isn't an admission of incompetence — it's how professionals work. This analogy:
1. Reframes "needing help" as "using good tools" (neutralizes R2)
2. Sets the right expectation — library, not magic (neutralizes disappointment)
3. Implies quality and curation (addresses R1)
4. Maps to an existing mental model they already value (connects to V1)

---

## Pre-Completion Checklist

- [x] Audience belief map constructed from THEIR perspective, not user's
- [x] Resistance points typed (evidential / motivational / identity / social / practical)
- [x] Persuasion path builds from existing beliefs — doesn't demand belief demolition
- [x] Ethics check completed — transparency, autonomy, and reciprocity tests pass
- [x] Message framed in target's values, not user's values
- [x] "What not to say" section included
- [x] At least one finding that challenges the user's approach: **The quantity (592) that feels like a selling point is actually a liability until quality is established. Lead with one skill's quality, not the count.**
- [x] Depth floors met (2x: 5 beliefs, 5 resistance points, 2 persuasion paths, 5 message elements)
