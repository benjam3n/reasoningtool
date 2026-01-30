# U — Universalize: "What am I missing?"

**Date**: 2026-01-29
**Depth**: 2x
**Input**: "what am i missing"

---

## Step 1: State the Claim

```
INPUT: "what am i missing"
CLAIM: "The current GOSM skill toolkit has gaps I haven't identified yet"
CLAIM TYPE: Meta / Strategic
```

## Step 2: Unbundle

**BUNDLED CLAIMS:**
1. **Explicit**: Something is missing from the toolkit
2. **Implicit**: The things already built (rewrites, new skills, anti-bias fixes) are necessary but not sufficient
3. **Presupposed**: The toolkit should be complete or at least more complete than it is
4. **Bundled**: "Missing" could mean missing skills, missing mechanisms within existing skills, missing integration between skills, missing workflows, or missing validation that what exists actually works
5. **Meta**: This is a request to search the space of possible gaps — it's asking for the unknown unknowns

## Step 3: Techniques Applied

### Technique 1: STATE SPACE — What could "missing" mean?

```
MISSING:
├── Missing skills (entire capabilities that don't exist)
├── Missing mechanisms within existing skills (gaps in how they work)
├── Missing integration (skills exist but don't compose well)
├── Missing validation (skills exist but haven't been tested to see if they work)
├── Missing feedback loops (no way to know if outputs are good)
├── Missing user workflows (skills exist but no guidance on when/how to use which)
├── Missing infrastructure (versioning, diffing, A/B testing between old/new)
├── Missing content (the library/ sessions aren't being used to improve skills)
├── Missing nothing (maybe it's good enough and the right move is to USE it, not build more)
└── Missing the wrong thing (maybe the problem isn't what's absent but what's present — bloat, redundancy, contradiction)
```

### Technique 2: INSTANCE-TO-CATEGORY — What is this toolkit an instance of?

```
"Reasoning skill toolkit" is an instance of:
├── CATEGORY: "Cognitive augmentation system"
│   Siblings: checklists, templates, frameworks, methodologies, decision support systems, expert systems
│   Missing sibling question: Does this toolkit have what those have?
│
├── CATEGORY: "Software library"
│   Siblings: npm packages, Python libraries, API toolkits
│   Missing sibling question: Does this have tests? Documentation? Versioning? Deprecation?
│
├── CATEGORY: "Personal productivity system"
│   Siblings: GTD, Zettelkasten, bullet journal, second brain
│   Missing sibling question: Does this have capture, review, archive, retrieval?
│
└── CATEGORY: "Prompt engineering system"
    Siblings: system prompts, few-shot examples, chain-of-thought templates
    Missing sibling question: Does this have evaluation, iteration, regression testing?
```

### Technique 4: PERSPECTIVE ROTATION

```
PERSPECTIVES:
├── You (the user): "I've been building and rewriting for hours. What haven't I thought of?"
├── A new user: "There are 300+ skills. Which 5 do I actually need? Where's the onramp?"
├── The LLM executing skills: "Some skills contradict each other. Some are redundant. Some reference things that don't exist anymore after the rewrites."
├── A skeptic: "You rewrote everything to be simpler, but did you actually test if simpler works better? You have zero evidence the new versions outperform the old ones."
├── Future-you in 6 months: "I forgot what half of these do. The session files in library/ are the real gold — are those organized?"
└── A competitor/alternative: "Why use 300 skills when one good system prompt and a well-trained model does 90% of this?"
```

### Technique 5: ASSUMPTION EXTRACTION

```
ASSUMPTIONS (load-bearing):
├── A1: "More skills = better toolkit" — if false, you need fewer, better skills, not more
├── A2: "The rewrites are improvements" — UNTESTED. No before/after comparison on the same problem.
├── A3: "Skills work in isolation" — if false, you need integration testing, not more skills
├── A4: "The anti-validation-bias fixes will work" — if false, the problem is deeper than missing text
├── A5: "The two projects (GOSM vs reasoning-toolkit) should stay in sync" — if false, one is canonical and the other is dead weight
├── A6: "Skills need to be invoked explicitly (/skillname)" — if false, maybe they should be auto-selected

ASSUMPTIONS (background):
├── The LLM actually follows skill instructions faithfully
├── Skill composition (skill A invoking skill B) works reliably
├── Session files in library/ are being read/used
└── The catalog.json/skill_registry.yaml actually affect behavior
```

### Technique 6: DIMENSION DISCOVERY

```
DIMENSIONS:
├── Breadth (number of skills): Currently HIGH (330+). Possibly too high.
├── Depth (quality per skill): RECENTLY IMPROVED but untested
├── Integration (how skills compose): UNKNOWN — no testing
├── Usability (how easy to use): LOW — 330 skills, no clear entry point for most tasks
├── Validation (proof it works): ZERO — no empirical testing of old vs new
├── Maintenance (keeping in sync): BROKEN — two projects diverged, discovered by accident
├── HIDDEN DIMENSION — Redundancy: Many old procedural skills overlap with new rewritten ones
├── HIDDEN DIMENSION — Consistency: Do the 330 skills agree with each other? Old ones may contradict new principles.
└── HIDDEN DIMENSION — Signal-to-noise: Does having 330 skills help or hurt? Does the LLM get confused by volume?
```

### Technique 7: TEMPORAL VARIATION

```
TEMPORAL:
├── Right now: Skills just rewritten, not tested. Momentum is high.
├── Next session: Will you remember which skills are new vs old? Which project is canonical?
├── Next month: Without validation, you won't know if rewrites helped or hurt.
└── Eventually: Either this converges to a small core that works, or it sprawls until abandoned.
```

---

## LOAD-BEARING ASSUMPTIONS

1. **The rewrites are improvements** — zero evidence yet. The old ARAW was 756 lines and produced sessions with ~50% rejection. The new one is 285 lines and produces 99% validation. The "fix" (anti-bias text) is untested.
2. **Two-project sync** — GOSM and reasoning-toolkit diverged silently. This will happen again unless one is declared canonical.
3. **Volume helps** — 330 skills might actively hurt by diluting the LLM's attention. Nobody has tested 10 skills vs 330.

## VOI RANKING

1. **Test the rewrites** — Run the same problem through old and new ARAW/UAUA and compare. This is the highest-value action because everything else assumes the rewrites work.
2. **Declare one project canonical** — GOSM or reasoning-toolkit. Kill the other or make it a build artifact. Otherwise you'll diverge again.
3. **Prune or archive old skills** — 330 skills where most are unrewritten procedural bloat may be worse than 20 sharp ones.
4. **Test anti-validation-bias fixes** — Run a UAUA session and see if rejection rate actually changes.
5. **Create a "which skill?" entry point** — The `/finder` skill exists but a simpler default routing (like `/gosm` used to do) would reduce friction.

## DIMENSIONS DISCOVERED

- **Validation**: No empirical testing of whether skills work
- **Redundancy**: Old procedural skills may contradict new principle-based ones
- **Signal-to-noise**: 330 skills may confuse the LLM
- **Project sync**: Two copies of the toolkit with no sync mechanism

## TOTAL SPACE: 28 alternatives/possibilities found

## READY FOR:
- `/aw 4x` "The rewrites are better than the originals" — test the core assumption
- `/ar 4x` "Pruning to 20 core skills would outperform 330" — explore the implications
- `/uaua 4x` "What's the right architecture for maintaining this toolkit long-term"
