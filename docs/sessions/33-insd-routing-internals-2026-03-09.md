# /insd What's actually happening inside the routing when someone types /claim vs /decide vs /analyze?
**Date:** 2026-03-09
**Skill:** /insd (Inside)

---

## Interpretation Selected

**Interpretation 2 — Explore for discovery.** The question is about understanding the internal mechanics of three routing systems. This is domain exploration — the user knows these skills exist but wants to understand what's actually happening beneath the surface when each one fires.

**Depth:** 2x (5 inversions, 2 representations, 2 cycles, 2 crystal tests)

**Phase:** Section B (Exploration) flowing into Section C (Crystallization)

---

## SECTION B: EXPLORATION

### B1: Domain Boundary

**The routing logic of /claim, /decide, and /analyze** — specifically, how each sub-orchestrator receives the same raw user input and transforms it into a different analytical pathway. Not the skills they route to, but the routing decisions themselves.

---

### B2: Five Surprising or Contradictory Facts

After reading all three SKILL.md files, here are the facts that don't fit a simple "each skill does its own thing" model:

1. **All three route to each other.** /claim routes to /decide if the input is really a decision. /decide routes to /claim if the input is really an assertion. /analyze routes to both /claim and /decide if it detects a claim or a decision. They form a triangle of mutual re-routing, not three independent pipelines.

2. **All three share nearly identical "Is This Actually a [X]?" gates.** Each skill has a section that checks whether the input is misclassified — and all three check for the same set of alternatives (/want, /emotion, /it, /but, /nsa, /handle). The overlap is almost complete. The routing guard logic is largely copy-pasted across all three.

3. **/analyze has no primary engine of its own.** /claim routes to /araw (its engine). /decide routes to /cmp and /araw (its engines). /analyze routes to /dcm + /ins by default, but also to /diagnose, /cmp, /fla, /prm, /swa, /cma, /pbi, /sya, /eth, /fut, /dom, /difr — 14+ different skills. It is almost entirely a dispatcher with no proprietary analytical operation.

4. **/claim and /decide share the same core engine (/araw) but configure it differently.** /claim adjusts the AR/AW balance based on the user's confidence level. /decide uses /araw to stress-test individual options after comparison. Same engine, different parameterization strategy.

5. **The depth-scaling tables measure completely different things.** /claim scales by "claims" and "findings." /decide scales by which skills get invoked (light = /cmp only, deep = /araw + /prm + /fla). /analyze scales by "dimensions" and "passes." There is no shared depth metric across the three, even though a user might reasonably expect "4x" to mean the same thing everywhere.

---

### B3: Why Each Fact Is Surprising

1. **Mutual re-routing:** I expected three parallel pipelines. Instead, they form an interconnected graph where the first job of each skill is to check whether it should hand off to one of the others. The routing layer is not a tree — it's a mesh.

2. **Shared guard logic:** I expected each skill's "is this really my job?" check to be specialized. Instead, they share ~8 identical re-routing checks. This suggests the real entry-point logic lives upstream (at the category-skill level in CLAUDE.md), and these guards are a safety net for misrouting, not the primary classification layer.

3. **/analyze as pure dispatcher:** I expected /analyze to have its own analytical method the way /claim has /araw. Instead, /analyze is a meta-router — a second-level orchestrator that classifies the *type* of analysis and delegates entirely. It's structurally different from /claim and /decide.

4. **Shared engine, different config:** I expected /claim and /decide to use fundamentally different tools. Instead, /araw is the workhorse for both — the difference is what gets fed into it and how its output gets used. /claim feeds it a proposition and reads back a verdict. /decide feeds it competing options and reads back a comparative stress test.

5. **Incommensurable depth scales:** I expected "4x" to be a universal concept. Instead, each skill defines depth in terms of its own native operations. This means depth is not a system-wide parameter — it's a local configuration that each skill interprets independently.

---

### B4: Connecting the Surprises

Facts 1 and 2 are clearly related. The mutual re-routing (fact 1) and the shared guard logic (fact 2) are both consequences of the same underlying pattern: **the three skills occupy overlapping territory in input space, and the system handles this by making each skill capable of recognizing when it's received something that belongs to a sibling.**

Facts 3 and 4 are also related. /analyze being a pure dispatcher (fact 3) while /claim and /decide share an engine (fact 4) reveals a structural asymmetry: **/claim and /decide are engine-wrappers around /araw, while /analyze is a routing table with no engine.**

**Hypothesis connecting all five:** The three skills are not parallel alternatives performing the same function differently. They occupy three structurally distinct roles in the system architecture:
- **/claim** is an engine-wrapper (configures and invokes /araw for propositions)
- **/decide** is an engine-wrapper with pre-processing (invokes /cmp first, then /araw for stress-testing)
- **/analyze** is a second-tier router (classifies the analysis type, then delegates to specialized skills)

The "routing" is not one system — it's three different kinds of system that happen to share an interface pattern.

---

### B6: Attempting to Break the Hypothesis

**Strongest counterargument:** "/analyze does have a default execution path (/dcm + /ins), so it's not purely a router — it does have its own analytical operation."

**Response:** True, /analyze has a default. But that default is itself a two-skill chain (/dcm then /ins), not a single proprietary operation. Compare: /claim's default is /araw (one skill, configured). /decide's default is /cmp then /araw (two skills, chained). /analyze's default is /dcm then /ins (two skills, chained). So the structural difference holds: /claim wraps one engine, /decide chains two engines, /analyze either chains two general-purpose skills or routes to one of 14+ specialists. The router characterization survives — /analyze just has a fallback chain for when no specialist matches.

**Boundary condition identified:** The hypothesis holds for the routing layer. Once you're inside the invoked skill (e.g., inside /araw), the three entry points no longer matter — /araw runs the same regardless of whether /claim or /decide sent it there. The structural differences are in the routing, not in the execution.

---

### B7: Refined Hypothesis

In the Reasoning Toolkit, **/claim, /decide, and /analyze are three structurally distinct sub-orchestrators that share an interface pattern but occupy different architectural roles**: /claim is an engine-configurer (parameterizes /araw based on confidence and testability), /decide is a staged pipeline (enumerate options, then stress-test the winner), and /analyze is a second-tier classifier (determines analysis type, then delegates to one of 14+ specialist skills). Their apparent symmetry as "category skills" masks a real asymmetry in how they process input.

---

## SECTION C: CRYSTALLIZATION

### C1: The Insight, Plainly

The three skills look like siblings but are architecturally parent-child-cousin. /claim and /decide are thin wrappers around the same engine (/araw), differing only in what they feed it and how they read the output. /analyze is a completely different beast — a second routing layer that classifies what kind of analysis you need and dispatches to specialist skills, most of which /claim and /decide never touch.

### C2: What I Believed Before

Before: These three skills are parallel alternatives — three flavors of "think hard about something," each applying its own methodology. The user picks which flavor they want, and each skill runs its own distinct process.

After: They are not parallel. They are structurally different kinds of components that share a naming convention. Two are engine-wrappers. One is a router. The shared naming (category skills in CLAUDE.md) obscures a real architectural distinction.

### C3: What Changes If This Is Correct

1. **You would stop treating /analyze as equivalent to /claim or /decide when explaining the system.** /analyze is more like a second copy of the top-level CLAUDE.md routing table, specialized for analytical requests. It doesn't "do analysis" — it classifies your analysis need and sends you to the right place. Telling a user "/analyze will analyze your problem" is misleading; it will *route* your problem.

2. **You would recognize that /claim and /decide are the skills where the system's core opinion-forming happens.** Both ultimately produce verdicts via /araw. The system's ability to actually assess truth or weigh options lives in /araw, and /claim and /decide are the two doorways to it. /analyze doesn't form opinions — it organizes.

3. **You would predict that adding a new "analysis type" to the system means editing /analyze's routing table, but adding a new "testing methodology" means editing /araw or creating a sibling engine.** The extension points are in completely different places.

4. **You would notice the redundancy in guard logic and consider whether the shared "Is This Actually a [X]?" checks should be factored out into a common pre-routing step** rather than duplicated in every sub-orchestrator.

5. **You would stop assuming "4x" means the same thing across skills.** When a user says "analyze this at 4x depth," they're getting multi-dimensional decomposition. When they say "test this claim at 4x," they're getting more claims unbundled and more findings per claim. These are qualitatively different experiences hiding behind the same number.

### C4: Strongest Argument Against

**"The structural differences don't matter to the user — they type a command and get useful output. The internal architecture is an implementation detail."**

This is legitimate. From the user's perspective, all three skills take input and produce structured thinking. Whether /analyze routes internally or runs its own engine is invisible.

**Counter-response:** The structural difference matters the moment something goes wrong or the user wants to go deeper. If a user types `/analyze "Is remote work productive?"` expecting a truth-test and instead gets a structural decomposition (because /analyze's default is /dcm + /ins, not /araw), the architectural difference has surfaced as a user-facing mismatch. The routing guards try to catch this (re-routing to /claim), but the fact that they need to exist at all is evidence that the structural asymmetry creates real confusion.

### C5: Re-Derivation Test

Starting from scratch: Three category skills handle claims, decisions, and analysis. Reading each file reveals that /claim and /decide both converge on /araw as their core engine, while /analyze has no single engine — it dispatches to 14+ skills based on analysis type classification. The mutual re-routing guards exist because inputs are ambiguous and any of the three might receive something meant for a sibling. The depth scales are incommensurable because each skill measures depth in terms of its own native operations, which are fundamentally different (/araw iterations vs. routing breadth vs. dimensional coverage).

Re-derivation matches. The insight is stable.

### C6: Formalized Record

**The Claim:** /claim, /decide, and /analyze are three structurally distinct types of component — engine-wrapper, staged pipeline, and second-tier router — that share a naming convention and interface pattern but occupy fundamentally different roles in the system architecture.

**The Evidence:**
- /claim's execution section is 6 lines centered on `/araw` with balance configuration
- /decide's execution section chains `/cmp` then `/araw` with pre-mortem add-ons for high stakes
- /analyze's execution section lists 14+ routing targets organized by analysis type
- All three share ~8 identical guard checks for misrouted input
- Depth scaling tables measure incompatible quantities

**Boundary Conditions:**
- This applies to the routing/orchestration layer only. Once inside a terminal skill like /araw or /dcm, the entry path no longer matters
- This applies to the current architecture. If /analyze gained its own engine, the asymmetry would change
- The mutual re-routing works well enough that most users never encounter the structural difference

**Implications:**
- System documentation should distinguish between engine-wrappers (/claim, /decide) and routers (/analyze)
- Shared guard logic is a candidate for factoring out into a common pre-routing layer
- "Depth" is not a universal system concept — it's locally defined per skill
- /araw is the system's core truth-testing capability, accessed via two different doorways (/claim for propositions, /decide for options)

**Open Questions:**
- Do other category skills (e.g., /evaluate, /diagnose, /search) follow the same pattern, or is the engine-vs-router split unique to these three?
- Should /analyze be reclassified in CLAUDE.md from "Router" mode to something that makes its dispatcher nature more explicit?
- Would a shared pre-routing layer that handles the common guard checks reduce duplication and improve classification accuracy?
- Is the incommensurable depth scaling a design problem or a feature (allowing each skill to define depth in terms that are natural for its operation)?

---

## Procedure Complete

Crystallized, tested, re-derivable insight about the structural asymmetry in the /claim, /decide, and /analyze routing layer.
