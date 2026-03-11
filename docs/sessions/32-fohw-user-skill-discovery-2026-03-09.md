# /fohw How does a new user actually figure out which skill to use?
**Date:** 2026-03-09
**Skill:** /fohw (Figure Out How it Works)

---

## Interpretation Selected

**Interpretation 1 — Understand a specific system.** The user has a concrete system (the skill-discovery pathways in reasoningtool) and wants to understand how a new user actually navigates from "I have a problem" to "I'm running the right skill."

---

## STEP 0: What are you trying to understand?

**THE THING**: How a new user of reasoningtool — someone who knows nothing about its 592 skills, 17 category routers, tier system, or website — figures out which skill to invoke for their actual need.

Specifically: What are the discovery pathways, what information do they have at each step, and where do they get stuck or succeed?

---

## STEP 1: How deep do you need to go?

**Choice: C — "I need to know WHY IT WORKS"**

We need to understand the mechanism: what causes a user to land on the right skill (or fail to)? Understanding the structure alone (listing the pathways) isn't enough — we need to know which pathways actually work for new users and why.

This means: Section B (map the structure) then Section C (understand the mechanism).

---

## SECTION B: Map the Structure

**Access level: DIRECT ACCESS** — we can read every source file, every skill, the website, and the CLAUDE.md routing tables.

### Step B2: Direct Inspection — Parts Found

**Part 1: CLAUDE.md Category Table (the "Start Here" router)**
- 17 rows mapping user situations to category skills
- Entry format: "User has... [situation] -> Use [/command]"
- Requires the user to classify their own situation into one of 17 types

**Part 2: Category Skills (sub-orchestrators)**
- 17 skills that receive natural-language input and route to specific analytical skills
- Examples: `/claim`, `/decide`, `/diagnose`, `/how`, `/want`, `/meta`
- Each one internally classifies the input further and dispatches to lower-level skills

**Part 3: CLAUDE.md Direct Skills Table (power user shortcut)**
- Maps "User wants to..." descriptions to specific skill commands
- 25+ rows covering decision-making, problem-solving, writing, planning, etc.
- Requires the user to already know what category their need falls into

**Part 4: Meta-skills for skill discovery**
- `/meta` — orientation and routing ("Get Oriented")
- `/wsib` — "What Skill Is Best" — takes a prompt and recommends the single best skill
- `/fonss` — "Figure Out Next Skills" — sequences multiple skills for a goal
- `/dtse` — "Does This Skill Exist" — looks up skills by name or function
- `/handle` — "Handle This" — converts maximally ambiguous requests into classified tasks
- `/extract` — extracts what's implicit in a prompt

**Part 5: Website (browse/search/filter)**
- Homepage with tiered skill display: Tier 1 (12 core), Tier 2 (16 analytical), Category Skills (17), Experimental (4)
- Tier 3: ~100+ skills organized into named categories (Research & Analysis, Writing & Communication, Planning & Projects, Business, Software & Engineering, etc.)
- Tier 4: ~200+ skills in fine-grained categories (Core Exploration, Search Methods, Goal Processing, Assumptions & Critique, etc.)
- Tier 5: remaining skills
- Tag/category filtering with emoji-based meta-categories
- Search functionality
- Session-persisted filter/sort state

**Part 6: The tier system itself**
- Tier 1: 12 essential skills everyone should know
- Tier 2: 16 analytical skills for deeper work
- Tier 3: Domain-specific professional skills
- Tier 4: Atomic/compositional skills (building blocks)
- Tier 5: Specialized/niche skills
- Tiers serve as progressive disclosure — don't show everything at once

**Part 7: Skill chaining / invocation**
- Skills can call other skills via `INVOKE: /procedure_name`
- Category skills route to analytical skills
- A user who enters any category skill gets routed automatically

### Structural Diagram

```
NEW USER
  |
  |--- [Path A: CLAUDE.md] ---> Category Table (17 entries)
  |         |                        |
  |         |                   Match situation? ---> /category_skill ---> auto-routes to specific skill
  |         |                        |
  |         |                   No match? ---> Direct Skills Table ---> pick by "wants to..."
  |         |
  |--- [Path B: Website] ---> Browse tiers ---> Find skill by name/category
  |         |                        |
  |         |                   Search ---> keyword match ---> skill page
  |         |                        |
  |         |                   Filter by tag ---> narrow results
  |         |
  |--- [Path C: Meta-skills] ---> /meta "help"
  |         |                        |
  |         |                   /wsib "my prompt" ---> single best skill
  |         |                        |
  |         |                   /handle "this mess" ---> classified + routed
  |         |
  |--- [Path D: Just try something] ---> /claim, /decide, /how (guess a category)
  |         |                                    |
  |         |                               Skill chains to the right place
  |
  |--- [Path E: Ask Claude directly] ---> Claude reads CLAUDE.md ---> recommends
```

### Connections and Flows

| Connection | What flows | Direction |
|---|---|---|
| User -> CLAUDE.md | User reads table, self-classifies | User-initiated |
| User -> Website | User browses/searches | User-initiated |
| User -> /meta | Natural language need | User to system |
| /meta -> /wsib, /fonss, /dtse | Routing based on meta-question type | System internal |
| /wsib -> specific skill | Single recommendation | System to user |
| Category skill -> analytical skill | Classified input | System internal |
| Analytical skill -> next skill | INVOKE chain | System internal |

### Step B5: Validate the Map

**Removal test for each part:**

| Part | If removed | Role in one sentence |
|---|---|---|
| CLAUDE.md Category Table | No starting point for CLI users | First-contact routing for users who read docs |
| Category Skills | Users must pick specific skills themselves | Convert vague needs into specific skill chains |
| Direct Skills Table | Power users lose their shortcut | Bypasses category routing for users who know what they want |
| Meta-skills (wsib/dtse/handle) | No way to ask the system itself for help | Let the system do the classification instead of the user |
| Website | No visual browsing/discovery | Enables exploration, search, and progressive disclosure |
| Tier system | 592 skills shown flat — overwhelming | Controls information density, shows important things first |
| Skill chaining | Users must manually sequence skills | Automates multi-step analysis |

All parts accounted for. Structural map is complete.

---

## SECTION C: Understand the Mechanism

### Step C1: The most important causal question

**"Why does a new user succeed or fail at finding the right skill?"**

What causes the match (or mismatch) between a user's actual need and the skill they end up running?

### Step C2: Three Hypotheses

**Hypothesis 1 — The Vocabulary Gap.** New users fail because the system's language doesn't match their language. The category table says "A claim to test" but the user thinks "I want to check if something is true." The skill names are terse abbreviations (`/aex`, `/pbr`, `/rca`) that mean nothing to someone who hasn't memorized them. Success depends on whether the user's natural phrasing happens to match the system's vocabulary.

**Hypothesis 2 — The Classification Burden.** New users fail because the system requires them to classify their own need before it can help — but classification IS the hard part. A user who doesn't know if they have "a claim to test" vs. "a decision to make" vs. "an idea to test" can't use the routing table. The 17 categories are too many to scan and too similar to distinguish. Success depends on whether the user can accurately self-diagnose their problem type.

**Hypothesis 3 — Progressive Disclosure Works.** New users actually succeed most of the time because the tier system and category routers absorb the complexity. A user who types `/meta help` or just picks any roughly-correct category skill gets routed to the right place automatically. The 592 skills are invisible to new users — they only see 12 (Tier 1) or 17 (categories). The system is not as overwhelming as it looks because most of the complexity is hidden behind orchestration layers.

### Step C3: Discriminating Tests

| Test / Observation | H1 (Vocab Gap) predicts | H2 (Classification Burden) predicts | H3 (Progressive Disclosure Works) predicts |
|---|---|---|---|
| A: User describes need in own words to /meta or /wsib — does the system find the right skill? | Often fails — system can't map natural language to skill names | Succeeds — because the SYSTEM does the classification, not the user | Succeeds — this is the designed pathway |
| B: User reads CLAUDE.md category table — can they pick the right row? | Sometimes fails — vocabulary mismatch | Often fails — too many similar categories | Usually succeeds — categories are distinct enough |
| C: User picks a "close enough" category skill (e.g., /how when they need /decide) — do they still reach a useful outcome? | Irrelevant to vocab | Fails — wrong classification produces wrong chain | Succeeds — category skills re-classify internally |
| D: User browses website tier 1 — can they find a relevant starting skill among 12? | Depends on whether descriptions match their mental model | Partially succeeds — 12 is scannable | Succeeds — 12 is manageable |

### Step C4: Running the Tests

**Test A result: The meta-skills (/meta, /wsib, /handle) DO successfully map natural language to skills.** /wsib explicitly extracts intent semantically ("Intent over keywords" is principle #2). /handle converts maximally ambiguous input into classified tasks. /dtse bridges "natural-language intent to terse abbreviation" (its principle #1). These skills exist precisely to solve the vocabulary gap problem.

- This **supports H3** (the system has designed pathways that work)
- This **partially eliminates H1** — the vocabulary gap exists at the CLAUDE.md table level but NOT at the meta-skill level
- This **partially eliminates H2** — if the user reaches a meta-skill, classification is handled by the system

**Test B result: The CLAUDE.md table has 17 rows with descriptions like "A claim to test," "A decision to make," "Something broken."** These are situation-descriptions, not task-descriptions. A user who says "I want to figure out if my startup idea is good" could plausibly match "A claim to test," "An idea to test," "Work to assess," or "A decision to make." Four rows seem applicable.

- This **supports H2** — the category table creates real classification burden
- This **partially supports H1** — the descriptions are compact enough to be ambiguous

**Test C result: Category skills contain internal routing logic.** For example, /meta routes based on input patterns and can redirect to /wsib, /fonss, /dtse, or directly classify the problem. If a user picks /how when they needed /decide, the /how skill will encounter a decision-shaped input and could potentially re-route or at least apply useful analysis. However, the re-routing is not guaranteed — a wrong category skill applies its own framework, which may produce useful-but-suboptimal output.

- This **partially supports H3** — wrong entry points are survivable, not catastrophic
- This **partially supports H2** — the re-routing isn't perfect, so classification still matters

**Test D result: Tier 1 has 12 skills with clear one-sentence descriptions.** Space Enumeration, Assumption Extraction, Comparison, Hypothesis Testing, Decision Procedure, Decomposition, Root Cause Analysis, Dimension Discovery, MECE Validation, Insight Synthesis, Cost-Benefit Analysis, Goal Understanding. These are generic enough that most users can find one that relates to their need. But they're analytical primitives, not entry points — a new user wanting to "figure out if my startup idea is viable" wouldn't intuitively reach for "Hypothesis Testing."

- This **partially supports H1** — the tier 1 skills use analytical vocabulary, not user-problem vocabulary
- This **partially undermines H3** — progressive disclosure works for reducing quantity but the 12 shown aren't the right 12 for new users (they're the most important analytical tools, not the best entry points)

### Step C5: Refine

No single hypothesis is fully eliminated. The picture is becoming clear: **all three are partially true, but they operate at different layers.**

**Refined understanding:**

The discovery system has THREE layers, each with a different failure mode:

1. **Self-service layer** (CLAUDE.md table, website browsing, tier display): Here, H1 and H2 are real problems. The user must do their own vocabulary translation and self-classification. The tier system helps with overwhelm but doesn't help with matching.

2. **Assisted layer** (category skills like /meta, /how, /decide): Here, H2 is partially solved — the category skill does further classification. But the user still had to pick the right category to enter this layer.

3. **Fully-delegated layer** (/wsib, /handle, /meta "help"): Here, H1 and H2 are both solved — the user gives natural language, the system does all classification. This is the designed solution. **But the user has to know these meta-skills exist to use them.**

### Step C6: State the understanding and stress-test it

**This works because the system has three concentric discovery layers — self-service, assisted, and fully-delegated — but the critical bottleneck is that new users don't know the fully-delegated layer exists.**

The system's architecture assumes users will discover /meta, /wsib, or /handle, which then absorb all the classification complexity. But these meta-skills are buried in the same 592-skill catalog as everything else. The CLAUDE.md table lists /meta as "Need orientation" — but a new user who doesn't know what "orientation" means in this context won't reach for it. The Direct Skills table lists "Find the right skill" -> `/wsib, /dtse, /extract, /fonss, /handle` — but this row assumes the user already knows they need help finding a skill, AND that they're reading this table.

**The bootstrapping problem:** The skills that solve the discovery problem are themselves subject to the discovery problem.

**Stress tests:**

1. **Counter-explanation: "Claude just figures it out."** In practice, when a user talks to Claude with the plugin installed, Claude reads CLAUDE.md and can route intelligently without the user knowing any skill names. Claude itself acts as the "fully-delegated layer." This is true — but it only works when the CLAUDE.md is in context. On the website, in documentation, or when recommending the tool to others, the user IS on their own.

2. **Edge case: A user who just types /meta.** This works well. /meta asks what they need and routes. But "just type /meta" is itself information a new user doesn't have. The entire system hinges on one piece of onboarding: "Start with /meta if you don't know where to go."

3. **Related system: VS Code extension marketplace.** VS Code has thousands of extensions. Users find them by: (a) searching by keyword, (b) browsing curated "featured" lists, (c) recommendations based on file type. ReasoningTool's website has (a) and (b) via tiers. It's missing (c) — contextual, automatic recommendation based on what the user is actually doing.

**The understanding holds, with one refinement:** The system works well for users who enter through Claude (because Claude does the routing) but poorly for users who enter through the website or documentation alone (because the bootstrapping problem is unsolved there).

---

## Synthesis: The Complete Discovery Mechanism

### What actually happens for each user type

**User Type A: Claude Code user (plugin installed)**
1. User types a natural-language prompt
2. Claude reads CLAUDE.md, sees category table
3. Claude classifies the input and either (a) runs the right category skill directly, or (b) invokes /wsib internally
4. User gets routed correctly without knowing any skill names
5. **This pathway works.** Claude is the fully-delegated layer.

**User Type B: Power user who read the docs**
1. User memorized the category table or direct skills table
2. User self-classifies: "I have a claim to test -> /claim"
3. Category skill routes them further
4. **This pathway works after initial learning investment.** The 17-row table is learnable.

**User Type C: New user on the website**
1. User sees 12 Tier 1 skills, 17 category skills, and categories expanding into hundreds
2. User scans skill names and one-sentence descriptions
3. User either (a) finds one that sounds right and clicks, (b) uses search, or (c) leaves confused
4. **This pathway partially works.** Search helps if they use the right keywords. Browsing works if a skill name/description resonates. But there's no "I don't know what I need" entry point on the website.

**User Type D: New user in Claude Code, no knowledge**
1. User heard about the tool, installed it, opens Claude Code
2. User doesn't know any skill names
3. User either (a) just asks their question normally (Claude routes — works), or (b) tries to invoke a skill and doesn't know which one
4. If (b), user is stuck unless they discover /meta
5. **Path (a) works transparently. Path (b) has the bootstrapping problem.**

### Where the system breaks

| Failure point | Why it breaks | What would fix it |
|---|---|---|
| CLAUDE.md category table: too many similar rows | User can't distinguish "claim to test" from "idea to test" from "work to assess" | Reduce to 5-7 categories or add a decision tree ("Is it about truth? -> /claim. Is it about choice? -> /decide") |
| Tier 1 shows analytical primitives, not entry points | New users don't think in terms of "Decomposition" or "MECE Validation" | Show category skills (entry points) more prominently than tier 1 (analytical tools) |
| Meta-skills are not visually distinguished | /meta, /wsib, /handle are listed alongside 589 other skills | Give them a dedicated "Start Here" section, distinct from tiers |
| Website has no "I don't know what I need" path | Every path assumes some self-knowledge | Add a guided flow: "What are you trying to do?" -> 3-4 broad options -> narrowing questions -> skill recommendation |
| Skill abbreviations are opaque | `/pbr`, `/aex`, `/rca` mean nothing to new users | Already mitigated by full names on website; in CLI, Claude provides the translation |

### The key insight

**The system's discovery mechanism is actually good — but it's good at the wrong layer.** The fully-delegated layer (/meta, /wsib, Claude's own routing) elegantly solves the vocabulary and classification problems. But that layer is invisible to new users. The visible layer (CLAUDE.md tables, website tiers, skill names) still has the bootstrapping problem.

The single highest-leverage fix: **Make the entry point impossible to miss.** Whether that's a prominent "Start here: /meta" on every surface, a website onboarding flow, or defaulting Claude to explain available categories when it detects a new user — the architecture is sound, it just needs a louder front door.
