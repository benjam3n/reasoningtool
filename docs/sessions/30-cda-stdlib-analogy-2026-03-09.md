# /cda What can reasoningtool learn from how programming languages manage their standard libraries?
**Date:** 2026-03-09
**Skill:** /cda (Cross-Domain Analogy)

---

**Interpretation selected:** Solution transfer -- reasoningtool has a specific set of problems (discoverability, quality variance, organization, deprecation, versioning across 592 skills) and wants to import proven solutions from how programming languages manage their standard libraries.

**Depth:** 2x (3 domains searched, 3 analogies, 2 deep mappings, 2 transfer tests)

---

## Step 1: Abstract the Problem

```
PROBLEM ABSTRACTION:

Original problem: reasoningtool has 592 skills that suffer from
discoverability problems, quality variance, unclear organization,
no deprecation strategy, and no versioning. Users struggle to find
the right skill and trust its quality.

Core pattern (domain-neutral):
- STRUCTURE: A large collection of modular capabilities, each doing
  one thing, organized under a single umbrella
- DYNAMIC: The collection grows over time; some items become
  outdated, overlap, or vary in quality; users must find the right
  item without knowing the full inventory
- GOAL: Users can quickly find, trust, and use the right capability
  for their situation
- CONSTRAINT: Maintainer bandwidth is finite; backward compatibility
  matters; users range from novice to expert

ABSTRACTED PROBLEM:
"A growing library of modular capabilities needs organization,
quality control, and navigation systems so users can find and
trust the right module without needing to know the full inventory."
```

---

## Step 2: Search for Analogous Domains

```
ANALOGY SEARCH:

Abstracted problem: A growing library of modular capabilities needs
organization, quality control, and navigation so users can find and
trust the right module.

| Domain              | Analogous Situation                          | Score |
|---------------------|----------------------------------------------|-------|
| Programming langs   | Standard library management (Python, Rust, Go)| 10   |
| Medicine            | Drug formulary / clinical guidelines library  | 7    |
| Law                 | Legal code organization (statutes, precedent) | 6    |
| Architecture        | Building code standards library               | 5    |
| Biology             | Enzyme/protein function cataloging            | 4    |
| Music               | Real Book / standard repertoire management    | 6    |
| Cooking             | Recipe database curation (Serious Eats, ATK)  | 7    |

TOP 3 ANALOGIES (highest similarity):
1. Programming languages: Standard library management - Score: 10
2. Cooking: Recipe database curation (America's Test Kitchen) - Score: 7
3. Medicine: Drug formulary management - Score: 7
```

---

## Step 3: Deep Dive on Top Analogies

### Analogy 1: Programming Language Standard Libraries

```
ANALOGY DEEP DIVE: Programming Languages - Standard Library Management
===================================================

THE ANALOGY:
Your problem: 592 skills with discoverability, quality, org, deprecation issues
Analogous to: How Python/Rust/Go manage hundreds of stdlib modules

STRUCTURAL MAPPING:
| reasoningtool         | -> | Programming Language          |
|-----------------------|----|-------------------------------|
| Skill (/cda, /rca)   | -> | Standard library module       |
| Skill categories      | -> | Package namespaces            |
| SKILL.md format       | -> | Module API contract           |
| User invoking /skill  | -> | Developer calling import      |
| Router skills (/claim)| -> | Package index / docs search   |
| Skill quality         | -> | Module test coverage + review |
| Growing skill count   | -> | Stdlib bloat over time        |
| Ben (maintainer)      | -> | Language core team             |

HOW THEY SOLVE IT IN PROGRAMMING LANGUAGES:

1. TIERED INCLUSION (Rust model)
   - Core: tiny, ultra-stable, always available
   - Std: broader, stable, ships with language
   - Crates.io (ecosystem): community, varied quality, opt-in
   Rust deliberately keeps std small and pushes things to crates.

2. NAMESPACE HIERARCHY (Python model)
   - Top-level packages: os, sys, math, json
   - Sub-packages: os.path, email.mime
   - Clear "if you want X, look in Y" mental model
   - "Batteries included" but organized by domain

3. DEPRECATION PROTOCOL (all mature languages)
   - Mark deprecated with warning, not removal
   - Point to replacement: "Use X instead"
   - Deprecation period before removal
   - Python: DeprecationWarning for 2+ versions

4. DOCUMENTATION AS FIRST-CLASS (Go model)
   - godoc generates docs from code comments
   - Every public function must have a doc comment
   - Searchable, consistent, auto-generated index
   - Examples are runnable tests

5. STABILITY MARKERS (Rust model)
   - #[stable], #[unstable], #[deprecated]
   - Each item has an explicit stability promise
   - Unstable = you can use it, but API may change

WHY IT WORKS THERE:
- Clear contract between module and user
- Discoverability through hierarchy + search
- Quality enforced by review process + testing
- Growth managed by tiering (not everything in core)

WHAT WE CAN IMPORT:
- Tier system: core skills vs. extended vs. experimental
- Stability markers on each skill
- Deprecation-with-redirect pattern
- Namespace hierarchy for organization
- Auto-generated searchable index

WHAT DOESN'T TRANSFER:
- Automated testing: Skills produce reasoning, not deterministic
  output. Can't unit-test a thinking procedure the way you test
  a sort function.
- Semantic versioning: Skills don't have "APIs" with breaking
  changes in the traditional sense.

ADAPTATION NEEDED:
- Replace automated tests with "quality tier" ratings based on
  manual assessment (has it been used? refined? does it produce
  good output?)
- Replace semver with maturity markers (draft / stable / proven / deprecated)

===================================================
```

### Analogy 2: America's Test Kitchen / Recipe Database Curation

```
ANALOGY DEEP DIVE: Cooking - Recipe Database Curation
===================================================

THE ANALOGY:
Your problem: 592 skills with quality variance and discoverability issues
Analogous to: How ATK/Serious Eats curates thousands of recipes

STRUCTURAL MAPPING:
| reasoningtool         | -> | Recipe Database                |
|-----------------------|----|--------------------------------|
| Skill                 | -> | Recipe                         |
| Skill quality         | -> | Recipe testing (ATK tests 30x) |
| Router skills         | -> | "What to cook tonight" guides  |
| Category organization | -> | Cuisine / technique / occasion |
| User finding a skill  | -> | Cook finding the right recipe  |
| Overlapping skills    | -> | 15 recipes for chocolate cake  |

HOW THEY SOLVE IT IN RECIPE CURATION:

1. CANONICAL RECIPES
   - ATK picks ONE "best" chocolate chip cookie recipe
   - Others exist but one is marked "THE recipe"
   - Reduces decision paralysis

2. SITUATION-BASED NAVIGATION
   - "Weeknight dinners under 30 min"
   - "Impressive but easy dinner party"
   - Navigate by USER SITUATION, not by ingredient taxonomy

3. HEADNOTES THAT EXPLAIN WHY
   - Every recipe explains: why this approach, what we tested,
     what didn't work, when to use this vs. alternatives
   - User can self-select before committing

4. TESTED BADGE
   - ATK: "Tested 47 times in our kitchen"
   - Signals quality without user needing to evaluate

WHY IT WORKS THERE:
- Opinionated curation beats comprehensive cataloging
- Users come with situations, not taxonomy queries
- Quality signals build trust

WHAT WE CAN IMPORT:
- "Canonical skill" marking for common use cases
- Situation-based navigation ("I'm stuck" -> here are your skills)
- Headnotes in SKILL.md explaining when to use vs. alternatives
- Quality badges based on usage/refinement history

WHAT DOESN'T TRANSFER:
- Recipe testing is empirical (taste it); skill testing is
  harder to objectify
- Recipes are independent; skills chain into each other

ADAPTATION NEEDED:
- "Tested" badge becomes "refined through N iterations" or
  "used in M real sessions with good results"
- Canonical marking needs clear criteria (not just opinion)

===================================================
```

### Analogy 3: Medicine - Drug Formulary Management

```
ANALOGY DEEP DIVE: Medicine - Drug Formulary
===================================================

THE ANALOGY:
Your problem: 592 skills, some overlapping, varying quality
Analogous to: Hospital formulary committees managing approved drugs

STRUCTURAL MAPPING:
| reasoningtool         | -> | Hospital Formulary             |
|-----------------------|----|--------------------------------|
| Skill                 | -> | Drug/therapy on formulary      |
| Overlapping skills    | -> | Me-too drugs (same class)      |
| Quality variance      | -> | Evidence quality variance      |
| Router skill          | -> | Clinical decision support      |
| Deprecation need      | -> | Removing drugs after recalls   |

HOW THEY SOLVE IT:
1. FORMULARY TIERS: Tier 1 (preferred, proven), Tier 2 (alternative),
   Tier 3 (specialist only, requires justification)
2. THERAPEUTIC EQUIVALENCE: "These 3 drugs do the same thing;
   this one is preferred because..."
3. REGULAR REVIEW CYCLES: Committee reviews formulary quarterly
4. INDICATION-BASED LOOKUP: Start from patient problem, not drug name

WHAT WE CAN IMPORT:
- Therapeutic equivalence -> "These 5 skills overlap; here's
  when to use each one"
- Formulary review cycles -> Periodic skill audit
- Indication-based lookup -> Problem-first navigation

===================================================
```

---

## Step 4: Cross-Pollinate Insights

```
CROSS-POLLINATION:

Insight from Programming Languages: Tier the library. Not
everything belongs in core. Stability markers signal trust.
Deprecate with redirects, never silent removal.

Insight from Recipe Databases: Mark canonical choices. Navigate
by user situation, not internal taxonomy. Explain WHEN to use
this vs. alternatives.

Insight from Medicine: Group equivalents explicitly. Review
periodically. Look up by indication (problem), not by name.

COMBINED INSIGHT:
The three domains converge on the same architecture:

1. TIER everything (core / extended / experimental)
2. NAVIGATE by user situation, not internal structure
3. MARK quality explicitly (don't make users guess)
4. GROUP overlapping items and declare a preferred default
5. DEPRECATE with redirect, on a schedule
6. REVIEW periodically with clear criteria

NOVEL APPROACH:
A "skill formulary" system that combines all three:
- Programming-style tiers and stability markers
- Recipe-style canonical picks and situation navigation
- Medicine-style equivalence groups and periodic review
```

---

## Step 5: Validate the Analogies

```
ANALOGY VALIDATION: reasoningtool is like a programming language stdlib
===================================================

SIMILARITIES (analogy holds):
[x] Modular capabilities invoked by name
[x] Growing collection with finite maintainer bandwidth
[x] Users range from novice to expert
[x] Some items overlap or supersede others
[x] Discoverability degrades as collection grows
[x] Quality variance is a real trust problem

DIFFERENCES (analogy breaks):
[!] Skills are procedures for thinking, not deterministic functions.
    Impact: Can't test quality automatically. Need human-assessed
    quality markers instead.
[!] Skills chain and compose differently than code modules.
    Impact: Dependency management is lighter -- skills reference
    each other but don't "break" when a dependency changes.
[!] Skills don't have versioned APIs.
    Impact: Maturity markers (draft/stable/proven) work better
    than semantic versioning (1.2.3).
[!] User intent is fuzzier than a function call.
    Impact: Navigation must handle ambiguous queries -- routers
    need to be smarter than an import statement.

ANALOGY STRENGTH: Strong

The structural mapping is tight on organization, discoverability,
quality control, and deprecation. It breaks mainly on testability
and versioning granularity -- but those differences are manageable
with adaptation.

SAFE TO IMPORT:
- Tiering (core / extended / experimental)
- Stability markers (draft / stable / proven / deprecated)
- Deprecation-with-redirect protocol
- Namespace hierarchy
- Canonical defaults for common needs
- Situation-based navigation
- Periodic review cycles
- Equivalence grouping for overlapping skills

DANGEROUS TO IMPORT:
- Semantic versioning (overkill for thinking procedures)
- Automated test suites (skills produce variable reasoning, not
  deterministic output -- false confidence if you pretend otherwise)
- Strict backward compatibility promises (skills should evolve
  freely; they're not APIs that external systems depend on)
```

```
ANALOGY VALIDATION: reasoningtool is like a recipe database
===================================================

SIMILARITIES (analogy holds):
[x] User comes with a situation, needs to find the right procedure
[x] Quality varies; some items well-tested, others not
[x] Multiple items serve similar purposes
[x] Headnotes/context help users self-select

DIFFERENCES (analogy breaks):
[!] Skills compose and chain; recipes are mostly standalone.
    Impact: Need to surface skill relationships, not just
    individual skill quality.
[!] Recipes converge on one "best" version; skills may legitimately
    need multiple approaches for different contexts.
    Impact: "Canonical" should mean "start here" not "only use this."

ANALOGY STRENGTH: Moderate-to-Strong

SAFE TO IMPORT:
- Canonical marking as "start here" default
- Situation-based navigation
- Quality signals based on testing/refinement

DANGEROUS TO IMPORT:
- Reducing to one "best" skill per category (legitimate diversity
  of approaches should be preserved)
```

---

## Step 6: Cross-Domain Insight Synthesis

```
===================================================
CROSS-DOMAIN INSIGHT SYNTHESIS:
What reasoningtool can learn from stdlib management
===================================================

ORIGINAL PROBLEM:
592 skills with discoverability, quality variance, organization,
deprecation, and versioning challenges.

ANALOGIES EXPLORED:
1. Programming Languages: Standard library management
2. Cooking: Recipe database curation (ATK model)
3. Medicine: Drug formulary management

===================================================

KEY INSIGHTS IMPORTED:

From Programming Languages:
- Tier the library -> Create explicit tiers: Core (30-50 essential
  skills), Standard (200 solid skills), Extended (the rest),
  Deprecated (phasing out)
- Stability markers -> Tag each skill: draft | stable | proven | deprecated
- Deprecation protocol -> Never delete; mark deprecated, point to
  replacement, remove from indexes after N months

From Recipe Databases:
- Canonical defaults -> For each common situation (decision, problem,
  writing), mark ONE skill as "start here"
- Situation navigation -> Primary nav should be "I have [situation]"
  not "browse alphabetical list"
- Headnotes -> Each SKILL.md should say "Use this when X. Use /other
  instead when Y."

From Medicine:
- Equivalence groups -> Explicitly document: "/rca, /dbg, and /dcm
  all solve problems. /rca for root causes, /dbg for debugging,
  /dcm for decomposition."
- Periodic review -> Schedule quarterly audits: which skills are
  unused? which overlap? which are stale?
- Indication-based lookup -> The router skills (/claim, /decide, etc.)
  ARE the indication-based lookup. Double down on these.

===================================================

NOVEL SOLUTIONS (analogy-informed):

1. THE SKILL FORMULARY
   Source analogy: Medicine (formulary tiers) + Programming (stdlib tiers)
   How it applies: Create a formal tier system with explicit criteria:
   - Tier 1 (Core): Used weekly+, proven quality, essential.
     30-50 skills. Always surfaced first.
   - Tier 2 (Standard): Used monthly, solid quality. 150-200 skills.
     Shown when relevant.
   - Tier 3 (Extended): Specialized or experimental. Shown only
     on direct request or deep search.
   - Tier D (Deprecated): Still works but replaced by something
     better. Shows deprecation notice + redirect.
   Adaptation needed: Tier assignment based on usage data +
   maintainer judgment, not committee vote.

2. SITUATION-FIRST NAVIGATION WITH CANONICAL DEFAULTS
   Source analogy: Cooking (ATK's "what to cook tonight") +
   Medicine (indication-based lookup)
   How it applies: The router skills (/claim, /decide, /want, etc.)
   are already situation-first. Strengthen them by:
   - Making them the ONLY entry point for new users
   - Each router declares a canonical "if you're not sure, use THIS"
   - Each skill's SKILL.md includes a "when to use me vs. alternatives"
     section (recipe headnote pattern)
   Adaptation needed: Write the headnote section into each SKILL.md.
   This is manual work but high-leverage.

3. THE EQUIVALENCE MAP + DEPRECATION PROTOCOL
   Source analogies: Medicine (therapeutic equivalence) +
   Programming (deprecation warnings)
   How it applies: Create an explicit map of overlapping skills:
   - Group: problem-solving = {/rca, /dbg, /dcm, /fohw}
   - Group: decision-making = {/dcp, /cmp, /cba}
   - Group: idea-generation = {/ma, /cda, /se}
   Within each group, declare preferred default and when each
   alternative is specifically better.
   For deprecated skills: add a header line to SKILL.md:
   `> DEPRECATED: This skill is superseded by /X. Use /X instead.`
   Keep the skill working for 3 months, then archive.
   Adaptation needed: Audit all 592 skills to build equivalence
   groups. Could be done incrementally -- start with the top 50
   most-used skills.

===================================================

REFRAMED UNDERSTANDING:

Before analogies: "We have too many skills and need to organize
them better." This frames it as a taxonomy/filing problem.

After analogies: "We have a standard library that needs the same
governance mature programming languages learned the hard way:
tiering, stability contracts, deprecation protocols, canonical
defaults, and situation-based navigation."

What changed: The problem isn't organization (putting things in
the right folder). The problem is GOVERNANCE -- having explicit
policies for what gets in, what quality bar it meets, when it
gets deprecated, and how users navigate the whole thing. Every
mature standard library learned this. reasoningtool is at the
stage where Python was before PEP 594 ("Removing dead batteries")
-- large, useful, but accumulating cruft without a policy for
managing it.

===================================================
```

---

## Quality Checklist

- [x] Problem abstracted to domain-neutral pattern
- [x] Multiple domains searched (7 scanned)
- [x] Top 3 analogies deep-dived
- [x] Structural mapping completed (for top 2)
- [x] Solutions from analogous domains documented
- [x] Cross-pollination attempted
- [x] Analogies validated for transferability (2 validations)
- [x] Novel solutions generated (3)
- [x] Differences and limitations noted

---

## Concrete Next Actions

1. **Define tier criteria and assign tiers to the top 50 skills** -- this unlocks everything else. Use: which skills do the routers point to? Which appear in CLAUDE.md tables? Those are your Tier 1 candidates.

2. **Add "when to use / when not to use" headnotes to Tier 1 skills** -- one paragraph per SKILL.md. Highest-leverage single change for discoverability.

3. **Build equivalence groups for overlapping skills** -- start with the groups visible in CLAUDE.md (decision-making, problem-solving, writing). Document which is the default and when each alternative wins.

4. **Establish a deprecation protocol** -- header line in SKILL.md, redirect to replacement, 3-month sunset, then archive to a `skills/_deprecated/` directory.

5. **Schedule a quarterly review** -- even 30 minutes scanning usage patterns and checking for stale skills will prevent stdlib bloat.
