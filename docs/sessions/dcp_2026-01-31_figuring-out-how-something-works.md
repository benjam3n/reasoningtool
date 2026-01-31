# Decision Procedure — Figuring Out How Something Works

**Date**: 2026-01-31
**Skill**: /dcp (Decision Procedure)
**Input**: figuring out how something works that you dont know much about

---

# FIGURING OUT HOW SOMETHING WORKS — DECISION PROCEDURE

---

## STEP 1: DIMENSION DISCOVERY (`/dd`)

### Seed Examples

1. Figuring out how a car engine works (mechanical system)
2. Understanding how a codebase works (software system)
3. Learning how a bureaucracy processes applications (organizational system)
4. Understanding how a recipe produces a result (process)
5. Figuring out how a board game works by watching others play (rule system)
6. Understanding how a financial instrument works (abstract system)
7. Figuring out how a biological organ works (natural system)
8. Understanding how a social media algorithm works (hidden system)
9. Learning how a musical instrument produces sound (physical system)
10. Figuring out how a negotiation tactic works (behavioral system)

### Comparison for Differences

- Engine vs codebase: **Observability** (can physically see parts vs. abstract/text-based)
- Codebase vs bureaucracy: **Access** (can read all code vs. can only observe from outside)
- Recipe vs board game: **Learning method** (follow instructions vs. infer rules from behavior)
- Financial instrument vs algorithm: **Transparency** (documented vs. deliberately hidden)
- Organ vs negotiation tactic: **Nature of the thing** (physical vs. behavioral)

### Dimensions Discovered

| # | Dimension | Values | Why It Matters |
|---|-----------|--------|----------------|
| 1 | **Nature of the thing** | Physical/mechanical, Software/digital, Biological/natural, Social/organizational, Abstract/conceptual, Behavioral/psychological | Determines which investigation methods work |
| 2 | **Your access level** | Full (can open it up, read source), Partial (can observe inputs/outputs), None (can only read about it) | Constrains what you can do |
| 3 | **Observability** | Transparent (all internals visible), Translucent (some internals visible), Opaque (black box — only see inputs/outputs) | Determines whether you can inspect or must infer |
| 4 | **Existing documentation** | Complete docs exist, Partial docs exist, No docs / wrong docs, Deliberately undocumented | Determines starting point |
| 5 | **Experimentation allowed** | Yes — can poke, prod, break it, Limited — can try things but carefully, No — observe only | Determines whether you can test hypotheses actively |
| 6 | **Complexity** | Simple (few parts, linear), Moderate (many parts, some interaction), Complex (many parts, emergent behavior), Chaotic (behavior seems random) | Determines how long this takes and what strategy to use |
| 7 | **Your goal depth** | Functional ("how do I use it"), Structural ("what are the parts"), Causal ("why does it work"), Generative ("could I build one") | Determines when you're done |
| 8 | **Feedback speed** | Instant (push button, see result), Fast (minutes to hours), Slow (days to weeks), Very slow (months+) | Determines experiment design |
| 9 | **Decomposability** | Modular (clear parts), Entangled (parts interact heavily), Monolithic (can't separate parts) | Determines whether divide-and-conquer works |
| 10 | **Risk of getting it wrong** | Low (hobby, curiosity), Medium (work task, some consequences), High (safety-critical, expensive mistakes) | Determines how rigorous you need to be |

**TOTAL SPACE**: 6 × 3 × 3 × 4 × 3 × 4 × 4 × 4 × 3 × 3 = **1,119,744 combinations**

**Independence check**: Access and Observability are correlated (full access usually means more observable) but can vary independently (you can have full access to an opaque system, like a compiled binary you can run but not read). All other dimensions are independent.

---

## STEP 2: SPACE ENUMERATION (`/se`)

**Granularity**: HIERARCHICAL (space > 5000)

### By Primary Dimension: Your Goal Depth

#### FUNCTIONAL ("How do I use it?")
- Shallowest goal — you need input/output behavior, not internals
- Methods: Try things, read tutorials, watch someone use it, copy patterns
- Done when: You can reliably get the outputs you want from inputs you provide
- Example: Learning to drive a car without knowing how the engine works

#### STRUCTURAL ("What are the parts?")
- Medium depth — you need to identify components and their roles
- Methods: Take it apart (physically or conceptually), label parts, trace connections
- Done when: You can draw a diagram of all major components and their relationships
- Example: Understanding the modules in a codebase

#### CAUSAL ("Why does it work?")
- Deep goal — you need to understand the mechanisms, not just the parts
- Methods: Hypothesize mechanisms, test with experiments, trace cause-effect chains
- Done when: You can predict what happens when you change something AND explain why
- Example: Understanding why a particular drug treats a disease

#### GENERATIVE ("Could I build one?")
- Deepest goal — you need complete operational understanding
- Methods: All of the above, plus attempting to replicate
- Done when: You can build a working version from scratch
- Example: Reverse-engineering a competitor's product

### Key Interactions

| If Access = | And Observability = | Then Primary Method = |
|---|---|---|
| Full | Transparent | Direct inspection (fastest) |
| Full | Opaque | Experimentation (input/output probing) |
| Partial | Translucent | Structured observation + limited experiments |
| Partial | Opaque | Black-box testing + inference |
| None | Any | Research + analogical reasoning only |

---

## STEP 3: ASSUMPTION EXTRACTION (`/aex`)

### Core Claims in "Figuring out how something works"

**Claim 1**: You can understand how things work through a systematic process.
**Claim 2**: Breaking things into parts helps understanding.
**Claim 3**: Experiments reveal mechanisms.
**Claim 4**: You'll know when you understand it.

### Assumption Map

| Assumption | Type | Hiddenness | Risk if Wrong |
|------------|------|------------|---------------|
| The thing HAS a mechanism (isn't random/magical) | Existence | Surface | Low — almost always true |
| The mechanism is stable (doesn't change while you study it) | Stability | **Deep** | **High** — studying a moving target wastes effort |
| You can observe enough to form accurate models | Access | Shallow | High — if truly opaque and no experiments allowed, you're stuck |
| Your existing mental models are close enough to build on | Knowledge | **Buried** | **Critical** — wrong mental models create wrong hypotheses |
| Decomposition into parts reflects real structure | Causal | **Deep** | High — some systems have no meaningful parts |
| You can distinguish "how it actually works" from "a story that fits the data" | Knowledge | **Buried** | **Critical** — this is the confirmation bias trap |
| Time and effort invested will be proportional to understanding gained | Resources | Deep | Medium — sometimes you hit walls |
| Understanding is transferable (once you get it, you keep it) | Stability | Surface | Low — usually true |

### Priority Assumptions

1. **Your existing mental models might be wrong** — The biggest trap. You think you're learning how it works, but you're fitting observations to a wrong model. The procedure must include model-breaking steps.
2. **You can't always tell understanding from a plausible story** — You need explicit tests that distinguish "I understand this" from "I have a narrative that feels right."
3. **The thing might change while you study it** — Living systems, social systems, and software under active development shift. The procedure needs a "is this still true?" checkpoint.

---

## STEP 4: PROCEDURE GENERATION (`/stg`)

```
================================================================
HOW TO FIGURE OUT HOW SOMETHING WORKS
(When You Don't Know Much About It)
DECISION PROCEDURE
================================================================

PURPOSE: Take you from "I don't understand this thing" to
"I understand it well enough for my goal" using a systematic
process that works for ANY type of thing.

WHO THIS IS FOR: Anyone facing something they don't understand —
a machine, a system, a process, a codebase, an organization,
a natural phenomenon, a game, a skill, anything.

================================================================

STEP 0: WHAT ARE YOU TRYING TO UNDERSTAND?
================================================================

Write down:

  THE THING: _______________
  (Name the specific thing. Not "computers" — "how my laptop
  connects to wifi." Not "politics" — "how a bill becomes law
  in my country.")

  If you can't name it specifically → you need to narrow down
  first. Ask: "What specific question do I want answered?"
  Keep narrowing until you have one concrete thing.

================================================================

STEP 1: HOW DEEP DO YOU NEED TO GO?
================================================================

Pick ONE:

A) "I just need to USE it"
   (I want to operate it, get results from it, not understand
   the internals.)
   → Go to SECTION A: Learn to Use It

B) "I need to know WHAT THE PARTS ARE"
   (I want to identify the components and how they connect.)
   → Go to SECTION B: Map the Structure

C) "I need to know WHY IT WORKS"
   (I want to understand the mechanism — what causes what.)
   → Go to SECTION C: Understand the Mechanism

D) "I need to be able to BUILD ONE"
   (I need complete operational understanding.)
   → Do Sections B, then C, then go to SECTION D: Build to Learn

================================================================

SECTION A: LEARN TO USE IT
(Goal: reliable input → output)
================================================================

Step A1: Find someone or something that already knows.

  Check in this order (stop when you find one):
  □ Is there a tutorial, manual, or "getting started" guide?
  □ Is there a person you can watch using it?
  □ Is there a video of someone using it?
  □ Is there a forum/community where users discuss it?

  If YES to any → Follow that tutorial/watch that person.
  Copy what they do EXACTLY before trying your own approach.

  If NO to all → Go to Step A2.

Step A2: Poke it.

  Try the most obvious action. Observe what happens.

  Record:
  I did: _______________
  I saw: _______________

  Repeat 5 times with different actions.

  ⚠ WARNING: Before poking, ask: "Can I break this or cause
  harm by experimenting?" If YES → use a copy, sandbox, or
  practice version. If no safe version exists → go to SECTION B
  instead (observation before action).

Step A3: Build an input/output table.

  | What I did (input)  | What happened (output) | Surprised? |
  |---------------------|------------------------|------------|
  | [action 1]          | [result 1]             | Y/N        |
  | [action 2]          | [result 2]             | Y/N        |
  | [action 3]          | [result 3]             | Y/N        |
  | ...                 | ...                    | ...        |

  Fill in at least 10 rows.

Step A4: Check your understanding.

  Can you now predict what will happen before you do something?

  Test: Pick 3 new actions you haven't tried.
  For each, WRITE DOWN your prediction BEFORE doing it.

  □ Prediction 1: ___ → Actual: ___ → Match? Y/N
  □ Prediction 2: ___ → Actual: ___ → Match? Y/N
  □ Prediction 3: ___ → Actual: ___ → Match? Y/N

  3/3 match: You understand it well enough to use it. DONE.
  2/3 match: Close. Investigate the mismatch, repeat A2-A4.
  0-1/3 match: Your model is wrong. Go to Step A5.

Step A5: Break your model and rebuild.

  ⚠ CRITICAL STEP — this is where most people fail.

  Your predictions were wrong. That means your mental picture
  of how this works is wrong. Do NOT patch your old model.
  Start fresh:

  1. Write down what you THOUGHT was happening: _______________
  2. Write down what ACTUALLY happened: _______________
  3. What's the simplest explanation that fits ALL your data
     (the table from A3 PLUS the failed predictions)?
     New model: _______________

  Return to Step A4 and test the new model.

  If you've done this 3+ times and still can't predict:
  → This thing is too complex for SECTION A. Go to SECTION B.

================================================================

SECTION B: MAP THE STRUCTURE
(Goal: identify the parts and connections)
================================================================

Step B1: Determine your access level.

  □ Can you open it up / read the source / see the internals?
    → You have DIRECT ACCESS. Go to B2.

  □ Can you observe it running and try different inputs?
    → You have EXPERIMENT ACCESS. Go to B3.

  □ Can you only read about it or observe from the outside?
    → You have OBSERVATION ONLY. Go to B4.

Step B2: Direct inspection (full access).

  1. List every distinct part/component/module you can see.
     Don't interpret — just list. Aim for exhaustive.

     Parts found:
     1. _______________
     2. _______________
     3. _______________
     ... (keep going until you can't find new parts)

  2. For each part, note:
     - What it connects to (inputs/outputs/neighbors)
     - Whether it's active (does something) or passive (stores/holds)
     - Rough size/importance relative to the whole

  3. Draw a diagram: boxes for parts, lines for connections.
     Label each line: what flows along it? (data, force,
     material, information, money, authority...)

  → Go to Step B5.

Step B3: Experiment-based mapping (can try things).

  1. Start with the simplest experiment: give it one input,
     watch what happens at every point you can observe.

  2. Change ONE thing at a time. Observe what changes downstream.

     | I changed           | What changed downstream | What didn't change |
     |---------------------|-------------------------|--------------------|
     | [variable 1]        | [effects]               | [non-effects]      |
     | [variable 2]        | [effects]               | [non-effects]      |

  3. Parts that change together are likely connected.
     Parts that don't change when others do are likely independent.

  4. Draw a diagram based on what you've inferred.
     Mark uncertain connections with "?"

  → Go to Step B5.

Step B4: Observation-only mapping (no access).

  1. Find the best available description of the thing:
     - Official documentation, textbooks, explainer articles
     - If multiple sources disagree, note the disagreements

  2. Read/watch THREE different sources that explain it.
     (One source gives you one perspective. Three gives you
     the overlapping truth.)

     Source 1 says the parts are: _______________
     Source 2 says the parts are: _______________
     Source 3 says the parts are: _______________

  3. What do all three agree on? → That's probably real.
     Where do they disagree? → That's where you're uncertain.

  4. Draw a diagram of the consensus structure.
     Mark disputed areas with "?"

  → Go to Step B5.

Step B5: Validate your map.

  Test: For each part in your diagram, answer:
  □ What would happen if this part were removed?
  □ Can I explain its role in one sentence?

  If you can't answer for a part → you don't understand it yet.
  Go back and investigate that specific part.

  Test: For each connection in your diagram, answer:
  □ What flows through this connection?
  □ What would happen if this connection were cut?

  If you can't answer for a connection → investigate it.

  When you can answer all of these:
  → Your structural map is complete.

  If your goal was structural (Step 1 choice B): DONE.
  If your goal was deeper: → Go to SECTION C.

================================================================

SECTION C: UNDERSTAND THE MECHANISM
(Goal: know WHY it works, predict changes)
================================================================

Step C1: Pick the most important causal question.

  Look at your structural map (from Section B).
  Write the ONE question you most want answered:

  "Why does _______________?"
  or "What causes _______________?"
  or "How does [part X] produce [effect Y]?"

  Your question: _______________

Step C2: Generate exactly 3 hypotheses.

  ⚠ WARNING: Do NOT settle for 1 hypothesis. 1 hypothesis
  is a trap — you'll find evidence that confirms it and stop.
  3 hypotheses force you to distinguish between them.

  Hypothesis 1: _______________
  Hypothesis 2: _______________
  Hypothesis 3: _______________

  Rules for good hypotheses:
  - Each must be specific enough to be wrong
  - At least one should feel unlikely to you (fight confirmation bias)
  - They should make DIFFERENT predictions about something observable

  ⚠ WARNING (same-idea trap): After writing your 3 hypotheses,
  check: "Would the same person believe all 3 of these?" If yes,
  they're not different enough. Make hypothesis 3 something you
  think is probably wrong. The point is to have something to
  eliminate.

Step C3: Find the discriminating test.

  Ask: "What observation would be TRUE under Hypothesis 1
  but FALSE under Hypothesis 2?"

  | Test / Observation        | H1 predicts | H2 predicts | H3 predicts |
  |---------------------------|-------------|-------------|-------------|
  | [observation A]           | [result]    | [result]    | [result]    |
  | [observation B]           | [result]    | [result]    | [result]    |

  Find a test where the hypotheses DISAGREE.
  If they all predict the same thing, that test doesn't help.
  Keep looking until you find a discriminating test.

Step C4: Run the test.

  □ If you can experiment → do the test, record results.
  □ If you can only observe → look for the predicted observation.
  □ If you can only research → find data that addresses this.

  Result: _______________
  This supports Hypothesis: ___
  This eliminates Hypothesis: ___

  ⚠ WARNING (correlation trap): After finding a result that
  supports a hypothesis, ask: "Is there a fourth explanation I
  haven't considered that also predicts this result?" If yes,
  you haven't actually discriminated. You need a sharper test.

Step C5: Refine or repeat.

  If one hypothesis remains → it's your working model.
  Test it 2 more times with different observations.
  If it keeps holding up → you probably understand the mechanism.

  If no hypothesis fits → all three were wrong.
  Generate 3 new hypotheses informed by what you've learned.
  Return to C2.

  If two hypotheses remain → you need a better discriminating test.
  Return to C3.

  If you've been through C2-C5 three times and no hypothesis
  survives → the thing may be more complex than your current
  knowledge can handle. Seek an expert or take a course in the
  domain, then return.

Step C6: State your understanding and stress-test it.

  Write: "This works because _______________"

  Now try to break your understanding:
  □ Find someone who disagrees. What's their counter-explanation?
  □ Find an edge case. Does your explanation still work?
  □ Find a related system. Does your explanation predict
    how THAT system works?

  If your explanation survives → you understand the mechanism. DONE.
  If it breaks → note WHERE it broke, return to C2 with that
  new information.

  ⚠ WARNING: "It makes sense to me" is NOT the same as
  "I understand it." The test is: can you PREDICT novel
  situations and be RIGHT? If you can't test predictions,
  you have a plausible story, not an understanding.
  Be honest about the difference.

================================================================

SECTION D: BUILD TO LEARN
(Goal: complete operational understanding)
================================================================

  Prerequisites: You've completed Sections B and C.

Step D1: Attempt to build a minimal version.

  Don't build the whole thing. Build the SMALLEST version
  that demonstrates the core mechanism.

  What I'm building: _______________
  Core mechanism I'm testing: _______________

Step D2: Record where you get stuck.

  Every place you get stuck reveals a gap in your understanding.

  | Where I got stuck       | What I didn't understand |
  |-------------------------|--------------------------|
  | [point 1]               | [gap 1]                  |
  | [point 2]               | [gap 2]                  |

Step D3: For each gap, return to the appropriate section.

  - Don't know the parts → Section B (for this specific sub-area)
  - Don't know why something works → Section C (for this question)
  - Can't make it work → Step A2 (poke the original, observe more)

Step D4: Does your build work?

  □ YES → You understand it well enough to build it. DONE.
  □ NO → Compare your build to the original.
    What's different? That difference is your remaining gap.
    Return to D3.
```

---

## STEP 5: FAILURE ANTICIPATION (`/fla`)

### Failure Modes When Following This Procedure

| # | Failure Mode | O | S | D | RPN | Tier |
|---|---|---|---|---|---|---|
| 1 | **User picks wrong depth** (goes to Section A when they need Section C) and wastes time with shallow understanding | 7 | 5 | 4 | 140 | High |
| 2 | **User generates 3 hypotheses that are all variations of the same idea** — doesn't actually diversify | 8 | 7 | 7 | 392 | Critical |
| 3 | **User declares "done" too early** because predictions seemed to match (small sample, easy tests) | 7 | 6 | 8 | 336 | Critical |
| 4 | **The thing changes while being studied** (software update, organizational restructure, evolving system) | 5 | 8 | 6 | 240 | Critical |
| 5 | **User can't find 3 sources** (Section B4) for obscure or novel things | 6 | 5 | 3 | 90 | Medium |
| 6 | **User mistakes correlation for mechanism** in Section C ("X happens before Y" → "X causes Y") | 6 | 8 | 8 | 384 | Critical |
| 7 | **User gives up at Step A5** because rebuilding mental models is uncomfortable | 7 | 6 | 5 | 210 | Critical |
| 8 | **Expert explanations use jargon** the user can't parse, blocking research paths | 6 | 4 | 3 | 72 | Medium |

### Mitigations Added as Warnings

**WARNING 1** (Failure #2 — same-idea hypotheses): After writing your 3 hypotheses, check: "Would the same person believe all 3 of these?" If yes, they're not different enough. Make hypothesis 3 something you think is probably wrong. The point is to have something to eliminate.

**WARNING 2** (Failure #3 — premature "done"): Before declaring you understand something, find ONE prediction your model makes that would surprise you if true. Test that specific prediction. If your model only predicts obvious things, it might just be restating what you observed, not explaining anything.

**WARNING 3** (Failure #4 — moving target): At the start of Section C, note today's date. If your investigation spans more than a week for a living system (software, organization, market), re-verify your Section B map before continuing. Parts may have changed.

**WARNING 4** (Failure #6 — correlation vs. causation): In Step C4, after finding a result that supports a hypothesis, ask: "Is there a fourth explanation I haven't considered that also predicts this result?" If yes, you haven't actually discriminated. You need a sharper test.

**WARNING 5** (Failure #7 — giving up at model rebuild): Step A5 is the most important step in the entire procedure. Feeling confused or frustrated at this point is CORRECT — it means you're actually learning. Comfort means you haven't challenged your assumptions. Push through.

---

## STEP 6: PROCEDURE VALIDATION (`/pv`)

### Validation Report

| Dimension | Status | Issues |
|-----------|--------|--------|
| Completeness | [x] | All four depth levels covered, all access levels addressed |
| Dependencies | [x] | Sections reference prior outputs correctly, ladder is sequential |
| Feasibility | [x] | Every step is a concrete action (write, observe, compare, draw) |
| Inputs | [x] | Only input required is "a thing you want to understand" |
| Outputs | [x] | Every path terminates in DONE, a loop back, or an explicit redirect |
| Consistency | [x] | No contradictions found |

### OVERALL STATUS: **VALID**

---

## COMMON MISTAKES

1. **Starting with research instead of observation.** Reading about how something works before looking at it installs someone else's model in your head. Look first, read second. (Exception: if you have observation-only access, reading is your only option — use Section B4.)

2. **One hypothesis.** The most common mistake in all of learning. You form one explanation, then see confirming evidence everywhere. Force yourself to hold 3 explanations. It feels unnatural. Do it anyway.

3. **Confusing "it makes sense" with "I understand it."** After reading an explanation, you feel like you understand. Test: close the book and explain it to someone (or write it down from memory). If you can't, you recognized the explanation — you didn't understand it.

4. **Not recording observations.** Memory is unreliable. If you don't write down what you tried and what happened (Steps A3, B3, C4), you'll forget details and confuse your own data.

5. **Going deeper than you need to.** If you just need to use a thing (Level 1), don't map its structure (Level 2). Match your effort to your actual goal. This is Step 1 of the procedure — don't skip it.

6. **Patching instead of rebuilding.** When a prediction fails, the temptation is to add an exception ("it works like X except when..."). After 2-3 exceptions, your model is a mess. Tear it down and build a cleaner one from all your data.

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **When you have a teacher available.** A knowledgeable person who can answer questions is faster than any procedure. Use them. This procedure is for when you're on your own.
- **When safety is critical.** If misunderstanding the thing could cause injury, financial loss, or other serious harm — do NOT rely on self-guided investigation. Get professional training or expert guidance first.
- **When time pressure is extreme.** If you need to use the thing in the next 10 minutes, skip to Section A, Step A1 (find a tutorial) and don't bother with deep understanding. You can come back later.
- **When the thing is formally defined.** Mathematical systems, programming languages, and rule-based games have complete formal specifications. Read the spec. It IS the answer. No need to hypothesize.

---

## WORKED EXAMPLES

### Example 1: Figuring Out How Git Works

**Step 0**: THE THING = "How git tracks and merges code changes"
**Step 1**: Goal = CAUSAL ("why does it work") → Section B then C.

**Section B** (Map the Structure):
- Access level: Full (can read files, run commands) → Step B2.
- Parts found: working directory, staging area, local repo, remote repo, commits, branches, HEAD pointer, .git directory.
- Diagram: working directory → `git add` → staging area → `git commit` → local repo → `git push` → remote repo.
- Connections: data flows as snapshots (not diffs).

**Section C** (Understand the Mechanism):
- Question: "How does git know what changed between two branches?"
- H1: It stores diffs between versions.
- H2: It stores full snapshots and computes diffs on demand.
- H3: It stores a mix (snapshots for some files, diffs for others).
- Discriminating test: Look at `.git/objects` — are they full files or diffs?
- Result: Full file snapshots (compressed). H2 supported.
- Stress test: Does this explain why branching is fast? Yes — branches are just pointers, not copies. Understanding holds.

### Example 2: Figuring Out How a Sourdough Starter Works

**Step 0**: THE THING = "How a sourdough starter makes bread rise"
**Step 1**: Goal = CAUSAL → Section B then C.

**Section B**: Observation-only at first (can't see microbes).
- 3 sources consulted. Consensus: it's a symbiotic colony of wild yeast and lactobacillus bacteria. Yeast produces CO2 (rising). Bacteria produce lactic acid (flavor).
- Diagram: flour + water → feeds yeast + bacteria → yeast produces CO2 + alcohol → bacteria produce acid → both reproduce.

**Section C**:
- Question: "Why does my starter need to be fed regularly?"
- H1: The organisms eat all the food and starve.
- H2: Waste products (acid, alcohol) build up and poison them.
- H3: Both — food depletion AND waste accumulation.
- Test: Feed a starving starter vs. replace the liquid (remove waste) without feeding.
- Result: Just removing waste didn't revive it. Fresh flour did. H1 primarily, H3 partially.
- Stress test: Predicts that a starter in the fridge (slower metabolism) needs less frequent feeding. Confirmed.

### Example 3: Figuring Out How a Company's Pricing Works

**Step 0**: THE THING = "How my competitor sets their prices"
**Step 1**: Goal = STRUCTURAL → Section B.

**Section B**: Observation-only (no access to their internals).
- Source 1 (their website): prices listed by tier.
- Source 2 (industry analysis): common SaaS pricing models.
- Source 3 (customer reviews): reports of discounts for annual billing.
- Map: Base price × tier multiplier, with annual discount and possible enterprise custom pricing.
- Validation: Predicted price for a specific tier + annual billing → checked against website → matched.

DONE at structural level. Did not need to understand WHY those specific prices (would require Section C + access to their internal data).

---

```
================================================================
VALIDATION STATUS: This procedure has not been validated by
domain experts in learning science or epistemology.
Apply with appropriate skepticism.
================================================================

QUICK REFERENCE CARDS
================================================================

CARD 1: The Learning Ladder
+---------------------------------------------+
| Level 1: USE IT    → Know inputs/outputs    |
| Level 2: MAP IT    → Know the parts         |
| Level 3: EXPLAIN IT → Know the mechanism    |
| Level 4: BUILD IT  → Know it completely     |
|                                             |
| Each level requires the one below it.       |
| Stop at the level you actually need.        |
+---------------------------------------------+

CARD 2: The Access-Method Table
+---------------------------------------------+
| Full access    → Open it up, read source    |
| Can experiment → Change inputs, watch output|
| Observe only   → Read 3 sources, find       |
|                  consensus                  |
| No access      → Analogical reasoning from  |
|                  similar systems you DO know |
+---------------------------------------------+

CARD 3: The Three Traps
+---------------------------------------------+
| TRAP 1: One hypothesis (confirmation bias)  |
|   Fix: Always generate 3 hypotheses         |
|                                             |
| TRAP 2: "Makes sense" ≠ "Understand"        |
|   Fix: Test predictions, not narratives     |
|                                             |
| TRAP 3: Patching a wrong model              |
|   Fix: When predictions fail, rebuild from  |
|   scratch (Step A5)                         |
+---------------------------------------------+
```
