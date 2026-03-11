# /analyze The pattern of how skills reference and invoke each other
**Date:** 2026-03-09
**Skill:** /analyze (Analyze a Situation)

---

## Interpretation

This is **structural analysis** -- understanding how a system (the skill dependency graph) is organized, what patterns emerge from the connections between parts, and what those patterns mean for the system's behavior.

Analysis type: **Structural + Pattern**

---

## Decomposition

### The Numbers

- **592 total skills** in the toolkit
- **117 skills** (20%) contain at least one `INVOKE` directive
- **475 skills** (80%) contain zero `INVOKE` directives
- **~584 total INVOKE directives** across the codebase
- **185 unique skills** are invoked as targets by at least one other skill
- **407 skills** (~69%) are never invoked by any other skill

### Dimension 1: The Invocation Hierarchy (Who Calls Whom)

The system has a clear **layered architecture** with four tiers:

**Tier 1 -- Heavy Routers (25-34 INVOKE directives each)**

| Skill | INVOKE Count | Role |
|-------|-------------|------|
| /evaluate | 34 | Artifact assessment router |
| /analyze | 33 | Situation analysis router |
| /how | 32 | Method-finding router |
| /action | 30 | Execution router |
| /decide | 30 | Decision router |
| /search | 29 | Exploration router |
| /viability | 28 | Idea-testing router |
| /want | 26 | Goal-pursuit router |
| /diagnose | 26 | Causal analysis router |
| /create | 25 | Content production router |
| /emotion | 22 | Emotional processing router |

These are the **category skills** from the CLAUDE.md table. Each contains extensive routing logic: "Is this actually a decision? Route to /decide. Is this actually a claim? Route to /claim." They form the **intake layer** of the system.

**So what:** The top ~11 skills account for roughly 311 of 584 INVOKE directives (53%). The system's routing logic is concentrated in a small number of orchestrators. If any of these skills has a routing error, it affects a large percentage of user interactions.

**Tier 2 -- Medium Routers (5-18 INVOKE directives each)**

| Skill | INVOKE Count | Role |
|-------|-------------|------|
| /claim | 18 | Claim-testing router |
| /iterate | 9 | Meta-iteration |
| /next | 9 | Follow-up routing |
| /technical | 8 | Domain routing |
| /certainty | 5 | Maximum rigor mode |
| /uga | 5 | Understanding gap analysis |

These are **secondary orchestrators** -- they receive traffic from Tier 1 and either do work themselves or route further.

**Tier 3 -- Light Routers (1-4 INVOKE directives each)**

About 100 skills that invoke 1-4 other skills, typically for follow-up routing ("after this, you might want /decide" or "if this reveals X, try /fla"). These are **worker skills with exit ramps**.

**Tier 4 -- Leaf Nodes (0 INVOKE directives)**

475 skills that never invoke another skill. They receive input, do their work, and return output. These are the **pure analytical tools** -- /araw, /se, /fla, /dcm, /prm, etc.

**So what:** The architecture is a **funnel**: broad intake (11 routers) narrowing through secondary routing (6 skills) into a large pool of specialized workers (475+). This is a classic dispatch pattern, similar to how operating systems handle syscalls or how web frameworks handle HTTP routing.

### Dimension 2: The Most-Invoked Targets (Who Gets Called)

The top 30 most-invoked skills (by how many INVOKE directives point to them):

| Rank | Skill | Times Invoked | Category |
|------|-------|--------------|----------|
| 1 | /decide | 19 | Category router |
| 2 | /how | 17 | Category router |
| 3 | /fla | 15 | Worker (failure anticipation) |
| 4 | /want | 14 | Category router |
| 4 | /next | 14 | Follow-up router |
| 6 | /tbd | 13 | Worker (to be determined) |
| 6 | /araw | 13 | Worker (argue/rebut/argue/weigh) |
| 8 | /handle | 12 | Catch-all router |
| 8 | /evaluate | 12 | Category router |
| 10 | /sycs | 11 | Worker (so you can see) |
| 10 | /it | 11 | Worker (I think) |
| 12 | /nsa | 10 | Worker (not sure about) |
| 12 | /claim | 10 | Category router |
| 14 | /se | 9 | Worker (systematic enumeration) |
| 14 | /but | 9 | Worker (tension resolution) |
| 16 | /foht | 7 | Worker (figure out how to) |
| 16 | /diagnose | 7 | Category router |
| 16 | /ata | 7 | Worker (assign to action) |
| 16 | /action | 7 | Category router |
| 20 | /to | 6 | Worker (task ordering) |
| 20 | /search | 6 | Category router |
| 20 | /obo | 6 | Worker (obvious bad outcomes) |
| 20 | /dcm | 6 | Worker (decomposition) |
| 20 | /cmp | 6 | Worker (comparison) |
| 25 | /viability | 5 | Category router |
| 25 | /sya | 5 | Worker (systems analysis) |
| 25 | /pv | 5 | Worker (procedure validation) |
| 25 | /prm | 5 | Worker (pre-mortem) |
| 25 | /iterate | 5 | Worker (iteration) |
| 25 | /iagca | 5 | Worker (scope compression) |

**So what:** Two distinct patterns emerge in the most-invoked list:

1. **Cross-routing targets** -- Category routers that other category routers redirect to. /decide (19), /how (17), /want (14), /evaluate (12). These are invoked because category routers detect "this isn't actually my type of input" and re-route. This means the system has a **disambiguation mesh** at the top level: any entry point can redirect to any other entry point.

2. **Universal worker skills** -- Skills that many different routers call as part of their actual work: /fla (15), /araw (13), /tbd (13), /sycs (11), /se (9). These are the **most trusted tools** in the system -- the ones that routers reach for regardless of domain.

### Dimension 3: The Cross-Routing Mesh

The category routers form a **dense mutual reference network**. Every single Tier 1 router contains a section like:

```
"Should I X?" -> /decide
"Is X true?" -> /claim
"How do I X?" -> /how
"I want X" -> /want
"Review my X" -> /evaluate
"Write about X" -> /create
"Handle this" -> /handle
```

This creates a **disambiguation layer** where the system can self-correct. If a user enters through /analyze but their input is actually a decision, the system redirects to /decide. This mesh means:

- **Any entry point works.** Users don't need to pick the "right" skill -- any category skill will eventually route to the correct one.
- **The mesh is not bidirectional equally.** /decide is the most-invoked router (19 times), while /create is invoked only twice. Users bring more ambiguously-decisional inputs than ambiguously-creative ones.
- **The cost is redundancy.** The same routing table appears in 10+ skills. A change to the routing logic (e.g., adding a new category skill) requires updating all of them.

**So what:** This is a **fault-tolerant intake system**. The redundancy is deliberate -- it ensures the user reaches the right analytical process regardless of which entry point they choose. But it also means the routing logic is the most maintenance-intensive part of the codebase.

### Dimension 4: Integration Metadata

Beyond `INVOKE` directives, skills also declare relationships through their Integration sections:

- **87 skills** have a "Use from" field (declaring who sends them traffic)
- **101 skills** have a "Routes to" field (declaring where they send traffic)
- **113 skills** have a "Differs from" field (declaring disambiguation boundaries)
- **68 skills** have a "Complementary" field (declaring optional pairings)

This is a **secondary dependency graph** -- softer than INVOKE, more like documentation of the intended architecture. It represents the designed relationships, while INVOKE represents the executable ones.

**So what:** Only about 15-19% of skills have this integration metadata. The remaining 80%+ are structurally isolated -- they do their work but don't declare how they relate to the rest of the system. This creates a **discoverability gap**: the system knows how its top ~100 skills relate, but the other ~490 are findable only by name or description.

### Dimension 5: Invocation Flow Patterns

Several distinct invocation patterns emerge:

**Pattern 1: Disambiguate-then-dispatch** (most common)
```
User -> /analyze -> "this is actually a decision" -> /decide -> /araw -> done
```
Category skill recognizes input type, redirects to correct category, which dispatches to workers.

**Pattern 2: Decompose-then-synthesize**
```
User -> /analyze -> /dcm (break apart) -> /ins (synthesize) -> done
```
Sequential pipeline where output of one skill feeds into the next.

**Pattern 3: Fan-out**
```
User -> /decide -> /araw + /prm + /fla (all three on the same input)
```
Single input processed by multiple skills in parallel for triangulation.

**Pattern 4: Recursive cycles**
```
/gg -> /qag -> /gg (guess-and-question loop)
/araw -> [may produce claims] -> /claim -> /araw
```
A small number of skills form intentional loops where output feeds back as input. These are rare but structurally significant -- they're the only skills that can run indefinitely.

**Pattern 5: Follow-up routing**
```
Worker skill -> "After completion, user may want:" -> /decide, /action, /fla
```
Soft invocations in the "After Completion" section -- not automatic, but suggested next steps. These create the **long-tail of the graph** where almost any skill can lead to any other.

**So what:** The system uses a mix of hard routing (INVOKE in execution paths), soft routing (INVOKE in follow-up sections), and metadata routing (Integration sections). The hard routing is a DAG with a few intentional cycles. The soft routing turns the whole system into a nearly fully-connected graph.

### Dimension 6: The Unreferenced Majority

Of 592 skills, ~407 (69%) are never invoked by any other skill. These are the **direct-access skills** -- users must know their name (or discover them via /wsib, /fonss, /meta, or the website) to use them. They include:

- Specialized analytical tools (/swa, /cba, /cma)
- Writing and style skills (/pw, /stl, /wre)
- Self-check skills (/sdc, /sid, /ecal)
- Recovery skills (/rmm, /kta)
- Domain-specific tools

**So what:** The system has a **long tail problem**. 80% of skills are only reachable by direct invocation. The routing layer covers the top ~185 skills but leaves 407 discoverable only through external means. This suggests either (a) those skills are sufficiently specialized that routing to them isn't practical, or (b) the routing layer is incomplete and many useful skills go unused because users don't know they exist.

---

## Interactions Between Components

### The Central Nexus

Five skills sit at the intersection of high-outgoing (they invoke many) and high-incoming (they are invoked by many): **/decide**, **/how**, **/evaluate**, **/want**, and **/claim**. These are the **nexus skills** -- they both route and get routed to. They form the densest cluster in the graph.

### The Bridge Skills

Skills like **/araw** (13 incoming, 0 outgoing-via-INVOKE) and **/fla** (15 incoming, 0 outgoing-via-INVOKE) serve as **terminal attractors** -- many paths lead to them, but they don't redirect elsewhere. They are the system's workhorse algorithms. When a router dispatches to /araw, the chain typically terminates there with the actual analytical output.

### The Utility Belt

/tbd (13), /sycs (11), /next (14), /handle (12) are **utility skills** that get invoked from many contexts. They aren't tied to a specific analysis type -- they're called when any skill encounters unresolved questions (/tbd), needs to trace implications (/sycs), needs to suggest follow-ups (/next), or gets input it can't classify (/handle).

### Maintenance Coupling

The cross-routing mesh means the category routers are **tightly coupled** for maintenance purposes. Adding a new category skill (e.g., a new top-level router) would require updating the disambiguation section of all ~11 existing routers. This is the system's most significant maintenance cost.

---

## Synthesis

### The Architecture in One Sentence

The skill invocation system is a **hub-and-spoke graph with a fully-connected core**: 11 category routers form a disambiguation mesh at the center, routing to ~185 reachable worker skills, while 407 skills sit outside the graph entirely, accessible only by direct invocation.

### Key Structural Properties

1. **The 80/20 is inverted**: 20% of skills contain all the routing logic; 80% are pure workers. But 69% of skills are unreachable through routing at all.

2. **The disambiguation mesh is the system's core innovation**: By having every category router redirect to every other category router, the system ensures that entry point doesn't matter. This is unusual for skill/procedure systems -- most use a single dispatcher. The distributed approach is more resilient but harder to maintain.

3. **The most-invoked skills reveal what the system considers fundamental**: /decide (19), /how (17), /fla (15), /want (14), /araw (13). These are the primitives the system believes all thinking reduces to -- making decisions, finding methods, anticipating failure, pursuing goals, and testing claims.

4. **The system has two types of relationships**: Hard (INVOKE in execution) and soft (INVOKE in follow-up suggestions, Integration metadata). The hard graph is a hierarchical dispatch system. The soft graph is a nearly complete network. Users who follow soft suggestions can traverse the entire skill space; users who only follow hard routing will stay within the designed analytical pipeline.

5. **The recursive cycles are deliberate**: The /gg-/qag loop (guess/question) and the implicit /araw-/claim loop create convergence mechanisms -- they repeat until the answer stabilizes. These are the system's only non-terminating patterns, and they serve the purpose of iterative refinement.

---

## Recommended Next Steps

1. **Audit the unreferenced 407 skills** -- are they genuinely specialized (and fine as direct-access), or are they missing from routing tables where they'd be useful? A systematic check could surface 50-100 skills that should be reachable through the routing layer but aren't.

2. **Extract the disambiguation table into a shared template** -- the "Is this actually a decision? Route to /decide" logic is duplicated across 11+ files. A single shared routing table would reduce maintenance cost and ensure consistency when new category skills are added.

3. **Map the soft invocation graph** -- the follow-up routing ("After completion, user may want...") creates an informal skill discovery mechanism. Mapping it could reveal natural skill sequences that users frequently follow, informing both documentation and the website's navigation.

4. **Consider adding invocation metadata** -- skills currently don't track how often they're actually invoked at runtime. Adding lightweight analytics would reveal whether the designed graph matches actual usage patterns, and whether the 407 unreferenced skills are actually discovered and used through other means.
