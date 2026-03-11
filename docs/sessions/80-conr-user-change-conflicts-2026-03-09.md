# /conr What's the most likely conflict that will arise when users start requesting changes to skills?
**Date:** 2026-03-09
**Skill:** /conr (Conflict Resolution)

---

## Step 1: Identify the Parties and Positions

```
PARTIES:
- PARTY A: Users — POSITION: "Skills should be adapted to how I actually use them — simpler,
  shorter, domain-specific, differently structured."
- PARTY B: Solo Maintainer — POSITION: "Skills need to maintain structural consistency, design
  philosophy coherence, and quality standards across all 592 skills."

APPARENT CONFLICT: Users want skills customized to individual preferences; the maintainer
needs a coherent, maintainable system that doesn't fragment into 592 competing visions.
```

---

## Step 2: Uncover Underlying Interests

Positions are what people say they want. Interests are why they want it. The resolution lives in the interests, not the positions.

**PARTY A (Users):**
- Position: "Change skills to match how I think/work"
- Interest 1: **Effectiveness** — They want the skill to actually produce good output for their specific use case, not a generic one
- Interest 2: **Efficiency** — They don't want to wade through steps that are irrelevant to their context
- Interest 3: **Ownership** — If they're investing time using and contributing to the tool, they want their experience to matter
- Fear: That the tool stays abstract and academic rather than becoming practically useful for their real work; that their feedback disappears into a void

**PARTY B (Solo Maintainer):**
- Position: "Skills need to follow the design philosophy and structural patterns"
- Interest 1: **Coherence** — 592 skills only work as a system if they share consistent structure, invocation patterns, and composability
- Interest 2: **Maintainability** — One person cannot maintain 592 skills if each one is a special snowflake with unique structure
- Interest 3: **Vision integrity** — The project has a specific thesis about proceduralized thinking; diluting that into "whatever users want" destroys the core value proposition
- Fear: Death by a thousand cuts — each individual change seems reasonable, but collectively they fragment the system into incoherence and the maintainer burns out trying to support divergent forks

---

## Step 3: Find Shared Interests

```
SHARED INTERESTS:
1. Skills should actually work well when invoked — neither party wants skills that
   produce poor output
2. The project should grow in adoption — both parties benefit from a thriving ecosystem
3. Skills should improve over time — stagnation serves no one

COMPATIBLE INTERESTS:
1. Users' desire for domain-specific skills doesn't conflict with structural consistency —
   you can have a domain-specific skill that follows the standard format
2. Maintainer's need for composability doesn't conflict with users wanting shorter skills —
   a skill can be both brief and composable
3. Users' desire for ownership can be satisfied through contribution pathways that don't
   require the maintainer to accept every change into core

GENUINELY INCOMPATIBLE:
1. Users who want to fundamentally restructure how skills work (e.g., "just make it a
   one-line prompt") vs. the procedural-step design philosophy — these are different
   products
2. Users who want the maintainer to personally implement every requested change vs.
   the maintainer's finite capacity — this is a resource constraint, not a values conflict
```

---

## Step 4: Generate Options

```
OPTIONS:
1. CONTRIBUTION GUIDELINES WITH GUARDRAILS — Publish clear skill design principles
   (structure template, composability rules, naming conventions). Accept PRs that follow
   them, reject those that don't.
   — Serves users' interest in ownership and the maintainer's interest in coherence.

2. COMMUNITY SKILLS DIRECTORY (SEPARATE FROM CORE) — Create a "community/" directory
   where user-contributed skills live with looser standards. Core skills remain maintainer-
   controlled. Community skills can graduate to core if proven.
   — Serves users' interest in customization and the maintainer's interest in quality control.

3. SKILL PARAMETERS/VARIANTS — Add a mechanism where skills accept a mode flag
   (e.g., `/rca --brief` or `/rca --domain=engineering`). Same core procedure, different
   depth or framing.
   — Serves users' efficiency interest and the maintainer's structural consistency interest.

4. "IMPROVE" PIPELINE (EXPAND THE PIE) — Users submit improvement suggestions via
   issues tagged by skill. Maintainer batches improvements quarterly. Users get influence
   without direct merge access. The /imps and /impss skills already exist to process these.
   — Serves users' interest in being heard and the maintainer's interest in controlled change.

5. FORK-FRIENDLY ARCHITECTURE (TRADE) — Explicitly design for easy forking: users
   maintain their own skill overrides in a personal directory that layers on top of core.
   User gets full customization; maintainer's core stays clean.
   — Users get total freedom; maintainer gives up "one true version" but keeps core intact.
```

---

## Step 5: Evaluate Options

| Option | Users' interests met (1-5) | Maintainer's interests met (1-5) | Fairness | Durability | Total |
|--------|---------------------------|----------------------------------|----------|------------|-------|
| 1. Contribution guidelines | 3 | 4 | 4 | 3 | 14 |
| 2. Community skills directory | 4 | 4 | 4 | 3 | 15 |
| 3. Skill parameters/variants | 4 | 3 | 4 | 4 | 15 |
| 4. Improve pipeline | 3 | 5 | 3 | 4 | 15 |
| 5. Fork-friendly architecture | 5 | 4 | 4 | 5 | 18 |

**Analysis of scores:**

- **Option 1** is standard but causes friction — users who get PRs rejected feel unheard, and the maintainer becomes a bottleneck. Durability drops as volume increases.
- **Option 2** creates a two-tier system that can breed resentment ("why won't you accept my skill into core?"). Moderate durability.
- **Option 3** is elegant but increases per-skill complexity. The maintainer has to build and maintain the variant system.
- **Option 4** is maintainer-friendly but makes users feel they're shouting into a queue. Fairness suffers at scale.
- **Option 5** scores highest because it resolves the core tension structurally: users get complete freedom without requiring maintainer effort, and the maintainer's core is never at risk.

---

## Step 6: Propose Resolution

```
RECOMMENDED RESOLUTION:

Combine Option 5 (fork-friendly architecture) with Option 1 (contribution guidelines)
as a layered strategy.

PRIMARY: Design a personal-override directory structure where users can create their own
skill variants that shadow core skills. Users run their version; core stays untouched.
This is effectively what the reasoningtoolpersonal directory already demonstrates —
formalize it as the intended customization path.

SECONDARY: For changes that genuinely improve core skills for everyone, publish
contribution guidelines with clear criteria: the change must preserve the step structure,
maintain composability, and improve output quality for the general case.

WHY THIS WORKS:
- For Users: They get total control over their experience. No gatekeeper. They can
  simplify, extend, restructure, or domain-specialize any skill without asking permission.
- For Maintainer: Core skills are never at risk. No obligation to review, merge, or
  debate subjective preferences. Contribution pipeline exists but is opt-in for both sides.
- Shared: The project grows in adoption because customization is a feature, not a threat.
  The best community innovations can still flow upstream through a clear, low-pressure path.

WHAT EACH SIDE GIVES UP:
- Users give up: Expectation that their preferred version becomes the default for everyone
- Maintainer gives up: Expectation that all users run skills exactly as designed; must
  accept that many users will run modified versions

IMPLEMENTATION:
1. Document the override/layering mechanism — how a user creates a personal skills
   directory that takes precedence over core (this pattern already exists in the project
   structure)
2. Write CONTRIBUTING.md with clear skill design principles and the criteria for changes
   that belong in core vs. personal overrides
3. Add a "Customization" section to project documentation explaining: "Core skills
   represent the maintainer's opinionated defaults. Fork freely. Override locally.
   Submit upstream only if it improves the general case."
```

---

## Step 7: Failure Planning

```
IF RESOLUTION FAILS:
- SIGNAL: Users still feel unheard despite having override capability — they want
  validation, not just freedom. This manifests as repeated issues saying "you should
  change X" even after the override path exists. Or: the override mechanism is too
  complex and nobody uses it.
- FALLBACK: Appoint 2-3 community maintainers with merge access to a "community-core"
  branch. This distributes the gatekeeping burden and gives active contributors a
  real stake. The solo maintainer retains veto on the main core.
- PREVENTION:
  1. Make the override mechanism dead simple (one directory, naming convention match, done)
  2. Explicitly name the design philosophy in the README so disagreements are about
     stated principles, not unstated preferences
  3. Celebrate community forks publicly — "here's how user X customized /rca for
     their engineering team" — so forking feels like a feature, not a rejection
```

---

## The Most Likely Conflict, Named

The single most likely conflict is **"simplify this" vs. "the complexity is the point."** Users will look at a 7-step skill and say "I only need steps 2 and 5." The maintainer will say "Steps 1, 3, 4, 6, and 7 exist to prevent the blind spots that make steps 2 and 5 unreliable." This is a genuine philosophical disagreement — the project's thesis is that *thorough procedures produce better thinking*, while many users will want *faster procedures that feel good enough*.

The fork-friendly architecture resolves this cleanly: users who want the abbreviated version can have it, and the core retains the full procedure for users who want the thoroughness the project was designed to provide. Neither side has to convince the other they're wrong.
