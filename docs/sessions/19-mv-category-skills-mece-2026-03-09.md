# /mv Check whether the category skills are mutually exclusive and collectively exhaustive
**Date:** 2026-03-09
**Skill:** /mv (MECE Validation)

---

## Step 1: Confirm Structure

```
VALIDATING: The 17 category skills as the router layer of reasoningtool

STRUCTURE:
- Total items: 17
- Categories:
  1. /claim — "A claim to test" (ARAW)
  2. /decide — "A decision to make" (ARAW)
  3. /viability — "An idea to test" (ARAW)
  4. /evaluate — "Work to assess" (ARAW)
  5. /diagnose — "Something broken" (UAUA)
  6. /search — "A space to explore" (UAUA)
  7. /want — "A goal or want" (AR-forward)
  8. /how — "A 'how do I' question" (AR-forward)
  9. /emotion — "A feeling or frustration" (AR-forward)
  10. /action — "Something to execute" (Direct)
  11. /create — "Content to produce" (Direct)
  12. /technical — "A domain-specific question" (Router)
  13. /analyze — "A problem to analyze" (Router)
  14. /certainty — "Need for maximum effort" (Maximum)
  15. /iterate — "Something to iterate on" (Meta-iteration)
  16. /meta — "Need orientation" (Informational)
  17. /sp — "A prompt to improve" (-)
- Dimensions covered: User input type / user need type
- Target MECE level: Soft MECE (this is a practical routing layer, not a formal specification)
```

---

## Step 2: Check Mutual Exclusivity (ME)

For each category skill, I check: does its scope overlap with any other category skill's scope?

### 2A: Cross-reference of "Is this actually X?" redirects

Every category skill contains an "Is this actually X?" section that reroutes misclassified inputs to other category skills. This is the primary mechanism for maintaining mutual exclusivity. The fact that every skill explicitly lists what it is NOT is strong evidence that the system is designed for ME. However, overlaps can still exist where the boundary is genuinely ambiguous.

### 2B: Overlap Analysis

| Item | Primary Category | Also Fits? | Overlap? |
|------|------------------|------------|----------|
| /claim | Test a proposition for truth | No | [x] ME |
| /decide | Choose between options | No | [x] ME |
| /viability | Test an idea for workability | /claim (truth vs workability) | [!] OVERLAP — see O1 |
| /evaluate | Assess existing work | /analyze (situations vs artifacts) | [!] OVERLAP — see O2 |
| /diagnose | Find cause of something broken | /analyze (causal analysis) | [!] OVERLAP — see O3 |
| /search | Explore an unknown space | No | [x] ME |
| /want | Clarify a goal or desire | No | [x] ME |
| /how | Find a method to achieve a goal | No | [x] ME |
| /emotion | Process a feeling | No (routes to others after acknowledging) | [x] ME |
| /action | Execute a command | /how (both deal with "do X") | [!] OVERLAP — see O4 |
| /create | Produce content | /action ("write X" could be either) | [!] OVERLAP — see O5 |
| /technical | Domain-specific routing | /analyze, /how, /evaluate, etc. | [!] OVERLAP — see O6 |
| /analyze | Analyze a situation | /diagnose, /evaluate | [!] OVERLAP — see O7 |
| /certainty | Maximum effort mode | All other categories | [!] OVERLAP — see O8 |
| /iterate | Improve existing work | /evaluate (both assess) | [!] OVERLAP — see O9 |
| /meta | Orientation / help | No (informational only) | [x] ME |
| /sp | Improve a prompt | No (distinct operation) | [x] ME |

### 2C: Detailed Overlap Analysis

**O1: /viability vs /claim**
- /viability tests "would this work?" (workability)
- /claim tests "is this true?" (truth)
- Boundary case: "We should pivot to B2B" — is this a claim or an idea?
- Resolution: Both skills explicitly distinguish themselves. /viability says "Ideas are tested for viability, not truth." /claim says it tests truth. The distinction is clear in theory but ambiguous in practice for prescriptive claims ("X is the best approach"). Both skills reroute to each other at their boundaries.
- **Severity: Low.** The distinction is well-documented and the rerouting logic handles edge cases.

**O2: /evaluate vs /analyze**
- /evaluate assesses artifacts (documents, plans, code, arguments)
- /analyze handles situations (markets, dynamics, systems, patterns)
- Boundary case: "Is my marketing strategy good?" — is the strategy an artifact or a situation?
- Resolution: /analyze explicitly states "Situations are analyzed; artifacts are evaluated." This is a clean conceptual split, though "strategy" sits on the boundary.
- **Severity: Low.** The artifact/situation distinction is well-articulated.

**O3: /diagnose vs /analyze**
- /diagnose finds causes of problems (causal analysis)
- /analyze handles general analysis including causal analysis
- Boundary case: "What's causing our churn?" could enter either.
- Resolution: /analyze routes causal analysis to /diagnose. /analyze says "Causal: 'What's causing X?' -> /diagnose." This is handled by explicit delegation.
- **Severity: Low.** /analyze explicitly delegates causal analysis to /diagnose.

**O4: /action vs /how**
- /action executes commands ("Do X")
- /how finds methods ("How do I X?")
- Boundary case: "Deploy this to production" — does the user want execution or method-finding?
- Resolution: /action says "If the method is unclear -> /how." /how says "If the user says 'Do X' -> /action." The distinction is: does the user know HOW and just wants it done (action), or do they not know HOW (how)?
- **Severity: Low.** The distinction is clear and both skills reroute correctly.

**O5: /create vs /action**
- /create produces content (writing, presentations, etc.)
- /action executes commands, including "write X"
- Boundary case: "Write a summary of this document" — action or create?
- Resolution: /action explicitly maps "Write / Draft -> /create." So /action delegates content production to /create. The overlap is handled by /action serving as a first-pass router that catches content production and delegates.
- **Severity: Low.** Explicit delegation in /action's routing table.

**O6: /technical vs everything**
- /technical routes by domain, but every domain task also has a task type that maps to another category skill
- /technical says "Task type overrides domain" — if someone asks "should I use React or Vue?", /decide handles the structure, and software skills provide evidence
- Boundary case: nearly any domain-specific question could also be classified as a claim, decision, evaluation, etc.
- Resolution: /technical explicitly says task type overrides domain. It functions as a secondary classification dimension (domain) that supplements the primary dimension (task type). In practice, /technical is a fallback for when the domain is the salient feature and the task type isn't clear.
- **Severity: Medium.** /technical is not a peer category — it is an orthogonal dimension. Every /technical input is also a claim/decision/evaluation/etc. The system handles this through /technical's principle that "task type overrides domain," but conceptually /technical is a different kind of category than the others.

**O7: /analyze vs /diagnose vs /evaluate**
- These three form a cluster where boundaries are well-documented but real-world inputs frequently sit at the intersection.
- /analyze = understand a situation
- /evaluate = assess an artifact
- /diagnose = find the cause of a problem
- All three have explicit redirects to each other.
- **Severity: Low-Medium.** The theoretical distinctions are clear (situation/artifact/cause), but a user saying "analyze my business plan" could reasonably enter any of the three.

**O8: /certainty vs everything**
- /certainty is not a content category — it is a depth modifier. It takes any input, classifies it using the other categories, and runs that category at 8x depth with iterative resolution.
- This means /certainty overlaps with every other category by design. It is a meta-mode, not a peer category.
- **Severity: Medium.** /certainty is categorically different from the others. It is a depth/effort amplifier, not a type classifier. A user who says "I need maximum effort on this claim" could enter /claim or /certainty — the answer is the same content but different depth.

**O9: /iterate vs /evaluate**
- /iterate improves existing work
- /evaluate assesses existing work
- /iterate explicitly distinguishes itself: "iterate changes things, evaluate assesses them"
- Boundary: "Make this better" could enter either. /iterate would identify what to change and change it. /evaluate would identify what's wrong and report it.
- **Severity: Low.** The assess-vs-change distinction is clear.

### 2D: ME Summary

```
MUTUAL EXCLUSIVITY CHECK:

OVERLAPS FOUND: 9 overlap relationships identified
- 5 Low severity (well-handled by explicit rerouting)
- 2 Low-Medium severity (handled but boundary cases exist)
- 2 Medium severity (conceptual category confusion — /technical and /certainty are different kinds of things)

STRUCTURAL FINDING: The overlaps divide into two distinct types:

TYPE A — True boundary ambiguity (O1, O2, O3, O4, O5, O7, O9):
These are cases where two skills have adjacent scopes and real-world inputs can sit at
the boundary. All 7 are well-handled by explicit rerouting logic in each skill's
"Is this actually X?" section.

TYPE B — Dimensional mismatch (O6, O8):
/technical is not a task-type category; it is a domain-type category. /certainty is
not a task-type category; it is a depth-mode category. These operate on different
classification dimensions than the other 15 skills, which classify by task type.

OVERLAP RATE: 9 overlaps involving 11 of 17 items
However, TYPE A overlaps are mitigated by rerouting logic.
Effective overlap rate (unmitigated): 2 / 17 = 12%

ME SCORE: 88%
```

---

## Step 3: Check Collective Exhaustiveness (CE)

### 3A: Dimension Coverage Check

The category skills classify user input by **what the user has or needs**. Let me check coverage across relevant dimensions.

**Dimension 1: User intent type**

| Intent | Category Skill | Covered? |
|--------|---------------|----------|
| Assert/test truth | /claim | Yes |
| Choose between options | /decide | Yes |
| Test workability of idea | /viability | Yes |
| Assess quality of work | /evaluate | Yes |
| Find cause of problem | /diagnose | Yes |
| Explore unknown space | /search | Yes |
| Clarify a goal | /want | Yes |
| Find a method | /how | Yes |
| Process a feeling | /emotion | Yes |
| Execute a command | /action | Yes |
| Produce content | /create | Yes |
| Domain-specific question | /technical | Yes |
| Understand a situation | /analyze | Yes |
| Maximum depth needed | /certainty | Yes |
| Improve existing work | /iterate | Yes |
| Get oriented / toolkit help | /meta | Yes |
| Improve a prompt | /sp | Yes |

**Dimension 2: Input speech acts**

| Speech Act | Example | Covered By |
|------------|---------|------------|
| Assertion | "X is true" | /claim |
| Question (factual) | "Is X true?" | /claim |
| Question (method) | "How do I X?" | /how |
| Question (option) | "What are my options?" | /search |
| Question (diagnostic) | "Why is X?" | /diagnose |
| Question (evaluative) | "Is this good?" | /evaluate |
| Command | "Do X" | /action |
| Request (content) | "Write X" | /create |
| Statement of want | "I want X" | /want |
| Statement of feeling | "I'm frustrated" | /emotion |
| Statement of idea | "What if we X?" | /viability |
| Statement of choice | "Should I X or Y?" | /decide |
| Meta-question | "What skill should I use?" | /meta |
| Prompt to improve | "Make this prompt better" | /sp |
| Request for depth | "Go deeper on this" | /certainty |
| Request for improvement | "Make this better" | /iterate |
| **Explanation request** | "Explain X to me" | **GAP — see G1** |
| **Teaching request** | "Teach me about X" | **GAP — see G2** |
| **Comparison without decision** | "How does X compare to Y?" (not choosing, just understanding) | **Partial — see G3** |
| **Prediction request** | "What will happen if X?" | **Partial — see G4** |
| **Translation/simplification** | "Explain this in simpler terms" | **GAP — see G5** |
| **Collaboration/social** | "Help me convince my team" | **Partial — see G6** |

### 3B: Edge Case Check

```
EDGE CASE PROBES:

| Probe | Found in List? | If No, Add? |
|-------|----------------|-------------|
| Extreme cases (max/min) | /certainty (max effort) | Covered |
| Boundary cases | Rerouting logic handles boundaries | Covered |
| Negative cases (what it's NOT) | Each skill defines what it's not | Covered |
| Historical cases (past examples) | No "review what happened" category | See G7 |
| Future cases (emerging) | /fut exists as a direct skill | See G4 |
| Edge stakeholders | /emotion covers the emotional user | Covered |
| Passive input ("just thinking out loud") | Not explicitly covered | See G8 |
| Multi-type input ("I want X, should I Y, and how?") | Handled by first-match routing | Covered |
```

### 3C: "What's Missing?" Brainstorm

```
WHAT'S MISSING BRAINSTORM:

Domain expert would add:
- G1: EXPLAIN / UNDERSTAND — "Explain X to me" or "Help me understand X"
  Currently this might enter /search ("tell me about X") or /technical,
  but neither is quite right. /search explores unknown spaces; explaining
  a known concept to someone is closer to teaching. A user who says
  "Explain quantum computing to me" doesn't have a space to explore, a
  claim to test, or a problem to solve — they have a knowledge gap to fill.
  SEVERITY: Medium. /search handles "tell me about X" and /technical
  handles domain questions, but neither is a natural fit for "explain
  this concept."

- G2: LEARN / TEACH — "Teach me X" or "I want to learn X"
  Related to G1 but more structured. /want could handle "I want to learn X"
  but would trace the want rather than teaching. /how could handle the
  method ("how do I learn X?") but wouldn't do the teaching itself.
  /technical has a Learning domain with skills like /ska, /dlp, /lrs.
  SEVERITY: Low-Medium. The learning domain exists in /technical, but the
  entry point is indirect. A user saying "teach me about X" would likely
  land in /search or /technical, both of which can handle it.

- G3: COMPARE (without deciding) — "How does X compare to Y?"
  /decide handles "X or Y?" when a choice is needed. But a user who
  just wants to understand the differences without choosing is not
  deciding. /analyze handles comparative analysis via /cmp. So
  /analyze is the entry point.
  SEVERITY: Low. Covered by /analyze routing to /cmp or /difr.

- G4: PREDICT — "What will happen if X?"
  Not a claim (not asserting truth), not a decision (not choosing),
  not exploration (space is known — they want a specific projection).
  Currently would route through /analyze -> /fut or /search -> /fut.
  SEVERITY: Low. /analyze covers this via its future analysis routing.

- G5: SIMPLIFY / TRANSLATE — "Explain this in simpler terms" or
  "Translate this jargon"
  Not evaluation, not creation, not analysis. This is a transformation
  of existing content. Could route through /create with rewrite focus
  or /action as a direct command.
  SEVERITY: Low. /action handles "rewrite this" as a direct command,
  and /create handles content production.

Contrarian would add:
- G6: PERSUADE / COLLABORATE — "Help me convince my team about X"
  This bundles claim-testing (is X right?), content creation (how to
  present it), and social dynamics. /create handles the content side,
  /claim handles the truth side. /technical has collaboration skills.
  SEVERITY: Low. Covered by chaining /claim -> /create -> /pw.

- G7: RETROSPECTIVE — "What went wrong?" or "Let's review what happened"
  Not quite diagnostic (not looking for a cause of something currently
  broken) — more like historical analysis. /evaluate could assess the
  work retrospectively. /analyze could analyze the situation.
  SEVERITY: Low. /evaluate and /analyze handle this.

- G8: THINK ALOUD — "I'm just thinking through X" or unstructured musing
  The user isn't asking for anything specific — they're using the
  system as a thinking partner. Currently would likely route to /meta
  or /emotion or /want depending on content.
  SEVERITY: Low-Medium. No natural home, but /meta can catch and
  reclassify.

Adjacent domain (other reasoning/thinking frameworks) has:
- NEGOTIATE — multi-party reasoning where different stakeholders
  have different goals. Partially covered by /decide and /col
  (collaboration skill).
- PRIORITIZE — "I have too many things, help me prioritize."
  Covered by /decide and /ro (reordering), but no dedicated
  category entry point.
- MONITOR — "How do I know if X is on track?" Not covered by
  any category. Would need /evaluate + /how.
```

### 3D: CE Summary

```
COLLECTIVE EXHAUSTIVENESS CHECK:

GAPS IDENTIFIED: 4 potential gaps

G1 (EXPLAIN/UNDERSTAND) — Medium severity
  A user who says "explain X to me" has no natural category entry point.
  /search covers "tell me about X" but frames it as exploration.
  /technical covers domain questions but frames them as domain routing.
  Neither is a natural fit for "teach me this concept."
  IMPACT: Users seeking understanding/explanation may feel misclassified.

G2 (LEARN/TEACH) — Low-Medium severity
  Covered indirectly by /technical -> Learning domain skills.
  Entry point is indirect but functional.

G5 (SIMPLIFY/TRANSLATE) — Low severity
  Covered by /action (direct command) or /create (content production).
  Not a true gap, just a non-obvious routing path.

G8 (THINK ALOUD) — Low-Medium severity
  Unstructured musing has no natural home.
  /meta can catch and reclassify, but the routing is not explicit.

COVERAGE ASSESSMENT:
- Core intent types: All covered (17/17 explicit categories)
- Edge intent types: 4 gaps identified, all Low to Medium severity
- Estimated coverage: ~90%
- Gap rate: ~10%
```

---

## Step 4: Calculate MECE Score

```
MECE SCORE:

Mutual Exclusivity:
- Overlaps: 9 overlap relationships
- Type A (boundary, mitigated by rerouting): 7
- Type B (dimensional mismatch, structural): 2
- Effective unmitigated overlaps: 2 / 17 = 12%
- ME Score: 88%

Collective Exhaustiveness:
- Gaps identified: 4
  - 1 Medium severity (EXPLAIN/UNDERSTAND)
  - 2 Low-Medium severity (LEARN/TEACH, THINK ALOUD)
  - 1 Low severity (SIMPLIFY/TRANSLATE)
- Estimated coverage: 90%
- CE Score: 90%

OVERALL MECE: (88 + 90) / 2 = 89%

ASSESSMENT:
- [ ] Perfect MECE (>95%)
- [x] Soft MECE (80-95%)
- [ ] Good Enough (60-80%)
- [ ] Needs Work (<60%)
```

---

## Step 5: Recommendations

```
MECE VALIDATION RESULTS: 17 Category Skills Router Layer

STATUS: Soft MECE (89%) — Strong for a practical routing system
```

### OVERLAPS TO RESOLVE

**1. /technical is not a peer category (dimensional mismatch)**
- /technical classifies by DOMAIN, while the other 14 content categories classify by TASK TYPE. This means every /technical input is also a /claim, /decide, /evaluate, etc. /technical acknowledges this ("Task type overrides domain") but its presence as a peer in the category table creates confusion.
- Recommendation: **Accept overlap, but reframe /technical in documentation.** /technical is a secondary classifier, not a primary one. The category table could present it as a "domain refinement layer" rather than a peer category. Alternatively, rename the table entry to make this clear: "A domain-specific question (where domain expertise matters more than task type)" vs the current "A domain-specific question."

**2. /certainty is not a peer category (depth modifier)**
- /certainty classifies by DEPTH/EFFORT, not by task type. It takes any input, classifies it using the other categories, and amplifies depth. Its presence as a peer category suggests it is an alternative to /claim, /decide, etc., when it is actually a wrapper around them.
- Recommendation: **Accept overlap, but reframe /certainty in documentation.** Present it as a depth mode, not a content category. The table entry "Need for maximum effort" already signals this, but it sits alongside content categories which creates a false impression of mutual exclusivity.

**3. /analyze vs /evaluate vs /diagnose cluster**
- These three are well-differentiated in their skill files (situation/artifact/cause), but from the category table alone, a user cannot easily distinguish them. "Work to assess" (/evaluate), "A problem to analyze" (/analyze), and "Something broken" (/diagnose) could all describe the same input.
- Recommendation: **Sharpen the category table descriptions.**
  - /evaluate: "A piece of work to assess for quality" (emphasize artifact)
  - /analyze: "A situation to understand" (emphasize situation)
  - /diagnose: "Something that's broken or failing" (emphasize malfunction)

### GAPS TO FILL

**1. EXPLAIN/UNDERSTAND — "Explain X to me" / "Help me understand X"**
- This is the most significant gap. A user seeking understanding of a concept does not naturally fit any category. /search comes closest ("A space to explore") but frames the need as exploration rather than comprehension.
- Recommendation: Either (a) add an 18th category skill /explain for knowledge-transfer requests, or (b) explicitly broaden /search's description to "A space to explore or a concept to understand." Option (b) is lower-cost and sufficient, since /search already handles "Tell me about X" inputs.

**2. THINK ALOUD — Unstructured musing**
- Users who are "just thinking" and using the system as a sounding board have no explicit entry point.
- Recommendation: /meta already catches disoriented users. Add "Just thinking something through" to /meta's routing table, which classifies and redirects. No new category needed.

### STRUCTURAL OBSERVATIONS

**The 17 categories mix three classification dimensions:**

| Dimension | Categories |
|-----------|-----------|
| **Task type** (primary) | /claim, /decide, /viability, /evaluate, /diagnose, /search, /want, /how, /emotion, /action, /create, /analyze |
| **Domain refinement** (secondary) | /technical |
| **Depth/mode modifier** | /certainty, /iterate |
| **Meta/toolkit** | /meta, /sp |

This mixing is not necessarily a problem — it makes the system pragmatically useful because users may come to it from any of these dimensions. But it means the system is not MECE in a formal sense. It is MECE *within the task-type dimension* (the 12 task-type categories are strongly ME and reasonably CE), with 5 additional categories that operate on orthogonal dimensions.

### ACTIONS

- [ ] Consider reframing the category table into a primary tier (12 task-type categories) and a secondary tier (5 modifier/meta categories) to reduce dimensional confusion
- [ ] Sharpen /evaluate, /analyze, and /diagnose descriptions in the table to emphasize their distinguishing characteristic (artifact / situation / malfunction)
- [ ] Add "A concept to understand" or "A topic to learn about" to /search's scope, or broaden its table description to "A space to explore or a topic to understand"
- [ ] Add "Just thinking something through" to /meta's routing
- [ ] Consider whether /technical should be documented as a "domain refinement overlay" rather than a peer category
- [ ] Consider whether /certainty and /iterate should be documented as "mode modifiers" rather than peer categories

---

## Quality Checklist

- [x] Structure confirmed
- [x] All items checked for overlaps
- [x] Dimension coverage verified
- [x] Edge cases probed
- [x] "What's missing" brainstormed
- [x] MECE score calculated
- [x] Specific recommendations provided
