# /dys Imagine the user experience of reasoningtool 2 years from now — what's dystopian about it?
**Date:** 2026-03-09
**Skill:** /dys (Dystopian Futures)

---

## Step 1: DEFINE THE DOMAIN

```
DOMAIN: User experience of the reasoningtool skill library
SCOPE: Individual (the person trying to use the tool) + Organizational (the project itself)
```

---

## Step 2: CONSTRUCT THE WORST CASE

### A. What does it look like?

**1. What is the daily experience of people in this failed state?**

The user types a question and is met with a wall. There are 1,400+ skills. The CLAUDE.md routing table is three pages long. The user doesn't remember whether they want `/cmp`, `/cba`, `/dcp`, `/decide`, or `/wdecide`. They try `/meta` and get a response that lists 40 category-level skills, each of which routes to 10-30 sub-skills. They spend more time navigating the skill system than thinking about their actual problem.

The website has a search bar, filters by tier, filters by tag, filters by meta-category, and a mobile pager — but the fundamental problem is that the user is scanning 1,400 names trying to pattern-match their messy real-world problem to one of dozens of overlapping three-letter abbreviations.

**2. What problems have gotten worse?**

- **Overlap explosion**: Skills that do nearly the same thing with slightly different framings. `/cmp` vs `/cba` vs `/decide` vs `/dcp` was already confusing at 592 skills. At 1,400 it's unbearable. Many skills differ only in which substep they emphasize.
- **Naming collapse**: The namespace of pronounceable 2-4 letter abbreviations is exhausted. New skills get names like `/ycshikfmif` (already real) or `/awtlytrn` (already real). Nobody can remember these.
- **Routing depth**: Category skills route to sub-categories that route to skills that invoke other skills. A single query can trigger a 4-deep chain. The user loses track of what's happening and why.
- **Maintenance burden**: Bug fixes, improvements, and consistency updates across 1,400 SKILL.md files is effectively impossible for one person. Skills drift apart in format, quality, and assumptions.

**3. What capabilities have been lost?**

- **Approachability**: A new user cannot get started without a tutorial. The "just type `/claim` and go" simplicity is buried under layers of routing and specialization.
- **Coherence**: The skill library no longer feels like one tool. It feels like 1,400 tools stapled together. Different skills assume different contexts, use different output formats, and chain into incompatible sub-skills.
- **Trust**: Users cannot tell whether a given skill is well-tested and robust or was added in a batch of 28 one afternoon and never revisited.

**4. What relationships and structures have broken down?**

- The mental model of "category skill routes to analytical skill" breaks when there are 5 layers of routing.
- The tier system (Tier 1 = essential, Tier 2 = advanced) becomes meaningless when there are 200 skills per tier.
- The website, which was a discovery tool, becomes a graveyard of cards nobody scrolls through.

**5. What do people spend their time on?**

- Searching for the right skill instead of doing the thinking.
- Reading skill descriptions to figure out if this one is different from the last one they tried.
- Running a skill, getting a mediocre output, wondering if a different skill would have been better, and re-running with a different one.
- Giving up and just asking Claude a plain question without any skill invocation.

### B. What went wrong?

**1. What single failure was the tipping point?**

The decision to measure progress by skill count rather than by user outcomes. Every batch commit that "adds 28 new skills" felt productive but diluted the library's signal-to-noise ratio.

**2. What cascade of failures followed?**

1. More skills required more routing logic, which required more meta-skills (`/wsib`, `/dtse`, `/fonss`, `/handle`, `/extract`) to help users find skills.
2. Meta-skills themselves became numerous enough to need their own router.
3. The CLAUDE.md file grew to the point where it consumed a significant portion of the context window just being loaded, reducing the quality of actual analysis.
4. Skill quality dropped because attention was spread across maintaining 1,400 files instead of perfecting 50.
5. Users who tried the tool once couldn't find what they needed, bounced, and never came back.

**3. What warnings were ignored?**

- The existence of skills like `/wsib` ("What Skill Is Best") is already a warning sign: if users need a skill to find the right skill, the system is too complex.
- Names like `/ycshikfmif` and `/awtlytrn` are already unmemorizable. This was visible at 592 skills.
- The website already needs a pager, filters, and search. This is the tool trying to compensate for volume with UI.
- The fact that category skills exist at all — the system already can't be navigated without intermediaries.

**4. What safeguards failed?**

- No mechanism to retire, merge, or deprecate skills.
- No usage data to show which skills actually get used vs. which sit untouched.
- No quality gate — any skill in the right markdown format gets added.
- No cap or target for library size.

**5. What was the "we should have seen this coming" moment?**

When the project needed skills to help you find skills (`/wsib`, `/dtse`, `/fonss`), and then needed skills to improve skills (`/imps`, `/impss`, `/imprt`), and then needed skills to identify gaps in skills (`/skgap`). The meta-layer growing faster than the functional layer is the classic sign of a system collapsing under its own weight.

### C. How did we get here?

**1. What was the first step on this path?**

The reasonable and initially correct instinct that "more skills = more coverage = better tool." This is true from 10 to 100 skills. It's questionable from 100 to 500. It's actively harmful from 500 to 1,400.

**2. What was the point of no return?**

When the number of skills exceeded what a single person could hold in working memory (~50-80 well-known skills). Past this point, every new skill makes the existing ones harder to find, and the system relies on routing rather than user knowledge.

**3. What seemed reasonable at each step but was catastrophic in aggregate?**

- "Let's add a skill for this edge case" — reasonable individually, catastrophic x500.
- "Let's add a category skill to help route" — reasonable, but it adds a layer of indirection.
- "Let's add meta-skills to help discover skills" — reasonable, but it's treating the symptom.
- "Let's add improvement skills to improve skill quality" — reasonable, but it multiplies the maintenance burden.

**4. What feedback loops accelerated the decline?**

- **More skills -> more confusion -> more routing skills -> more skills**: The discovery problem creates demand for more meta-skills, which increases total skill count.
- **More skills -> thinner attention -> lower quality -> less trust -> less usage -> less feedback -> even lower quality**: Without usage data, bad skills persist and good skills don't get refined.
- **More skills -> longer CLAUDE.md -> more context consumed -> worse outputs -> the tool seems less useful**: The routing table literally competes with the user's problem for context window space.

---

## Step 3: EARLY WARNING SIGNALS

```
EARLY WARNINGS:

Stage 1 (still easy to fix): Users ask "which skill should I use for X?"
  more than they ask substantive questions.
  — Current status: PRESENT (the /wsib, /dtse, /fonss skills exist for this reason)

Stage 2 (harder to fix): New users bounce after trying 1-2 skills because
  they can't figure out the system. No onramp works.
  — Current status: PARTIALLY PRESENT (unclear without usage data)

Stage 3 (very difficult): The maintainer spends more time on skill
  infrastructure (routing, meta-skills, website UI) than on skill quality.
  — Current status: PRESENT (recent commits are about filtering, paging,
    navigation, batch skill additions)

Stage 4 (too late): Users bypass the skill system entirely and just talk to
  Claude directly because the overhead isn't worth it.
  — Current status: UNKNOWN (no usage telemetry)
```

---

## Step 4: WHO SUFFERS

**1. Who is harmed first?**
New users. They have no accumulated knowledge of skill names and must navigate the full complexity from day one. They are the canary.

**2. Who is harmed most?**
The maintainer. They carry the full cognitive load of 1,400+ skills, feel the pressure to add more, and bear the maintenance burden alone.

**3. Who doesn't realize they're being harmed until it's too late?**
Power users who memorized 30-40 skill names early on. They don't feel the bloat because they use the same subset. But the skills they rely on quietly degrade as attention shifts to new additions, and one day they notice the outputs aren't as good as they used to be.

**4. Who benefits from the dystopia?**
- The instinct that says "shipping is progress." Adding 28 skills in a commit feels productive.
- Competitors or alternatives that are simpler. The complexity becomes their marketing: "Unlike reasoningtool, we have 5 skills that actually work."

**5. Who has the power to prevent it but doesn't?**
The maintainer. This is a solo project. The same person who adds skills is the only person who can choose to stop adding them, merge overlapping ones, or set a cap.

---

## Step 5: PREVENTION

**1. Interventions — What would prevent the worst case at each stage?**

- **Now**: Freeze skill count. Declare a moratorium on new skills until the existing 592 are audited, merged, and pruned. Set a target of ~150-200 well-maintained skills.
- **Soon**: Implement skill retirement. Skills that overlap significantly should be merged. `/cmp` and `/cba` might be one skill with a mode flag. `/wsib`, `/dtse`, `/fonss`, `/handle`, and `/extract` are five skills doing one job.
- **Architecture**: Replace the "1,400 flat files" model with a smaller set of composable primitives. Instead of a skill for every combination of analysis type + framing, have 20-30 core analytical operations that compose.
- **UX**: Instead of making users pick a skill, make the system pick for them. One entry point. User describes their problem in plain language. The system selects and composes the right analytical steps. The skill library becomes an implementation detail, not a user-facing menu.

**2. Monitoring — What should we be measuring?**

- Skill usage frequency (which of the 592 actually get invoked?)
- Time-to-first-useful-output for new users
- How often users try multiple skills before settling on one
- How often users bypass skills entirely

**3. Safeguards — What structural protections should exist?**

- A hard cap on total skill count (e.g., "no more than 200 user-facing skills")
- A requirement to retire one skill for every new skill added
- A quality bar: every skill must have at least 3 tested examples
- A "last used" timestamp to identify dead skills

**4. Red lines — What should trigger immediate action?**

- If CLAUDE.md exceeds 500 lines, the routing layer is too heavy
- If more than 10% of skills are meta-skills (skills about skills), the system is navel-gazing
- If a new user cannot successfully use the tool within 2 minutes, the onramp is broken

**5. Resilience — If prevention fails, what makes the bad outcome survivable?**

- The core insight of "structured thinking procedures" is sound regardless of how the library is organized. Even if the current implementation collapses under its own weight, the idea survives.
- The skill files are plain markdown. They can be forked, pruned, and reorganized by anyone.
- The worst case is "users ignore the skill system and talk to Claude directly" — which is fine. They lose the structure but not the AI.

---

## Step 6: OUTPUT

```
DYSTOPIA ANALYSIS:

Domain: User experience of the reasoningtool skill library

The worst case:
At 1,400+ skills, reasoningtool becomes a labyrinth. Users spend more time
searching for the right skill than doing actual thinking. The tool that was
supposed to structure thought instead becomes a source of decision paralysis.
New users bounce immediately; power users retreat to a memorized subset of
30 skills while the other 1,370 rot. The maintainer burns out maintaining
a sprawling library that nobody fully uses.

Path to dystopia:
1. Keep adding skills at current rate — seems productive, fills gaps
2. Discovery problem grows — users need meta-skills to find skills,
   CLAUDE.md bloats, routing gets deeper
3. Quality dilutes — 1,400 skills can't all be maintained; many decay,
   overlap compounds, trust erodes
4. Abandonment — users bypass the skill system entirely or leave for
   simpler alternatives

Early warnings to watch:
- Meta-skills (skills about finding skills) proliferating — PRESENT
- Maintenance focus shifting to infrastructure over quality — PRESENT
- Unmemorizable skill names appearing — PRESENT
- No usage telemetry to identify dead skills — PRESENT

Who suffers first: New users (no existing mental map to navigate complexity)
Who benefits: The "shipping is progress" instinct; simpler competitors

Prevention priorities:
1. Freeze and prune: audit all 592 skills, merge overlaps, target ~150-200
2. One entry point: stop making users pick skills; have the system pick
   for them based on plain-language input

Red line: If more than 10% of skills exist to help users navigate
the skill system itself, the system has become self-referentially bloated.
(Current state: /wsib, /dtse, /fonss, /handle, /extract, /imps, /impss,
/imprt, /skgap = 9 meta-skills. That's already ~1.5% and climbing.)

Most useful insight: The project's biggest risk is not "missing a skill
someone needs." It's "having so many skills that nobody can find the one
they need." Growth is the threat, not gaps. The next phase of this project
should be about subtraction, not addition.
```
