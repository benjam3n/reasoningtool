# DCP — Discovering New Math & Unexplored Mathematical Areas

**Date**: 2026-01-31
**Input**: methods of discovering new math and unexplored math areas

---

# DISCOVERING NEW MATH & UNEXPLORED MATHEMATICAL AREAS — Decision Procedure

## Step 1: Decision Dimensions (`/dd`)

What dimensions determine where new math can be found?

| # | Dimension | Description | Why It Matters |
|---|-----------|-------------|----------------|
| 1 | **Discovery Method** | How are you looking? (generalizing, connecting, axiom-tweaking, problem-driven, tool-driven) | Different methods find different kinds of new math; using only one leaves entire regions unexplored |
| 2 | **Existing Structure Being Examined** | What known mathematical object or theorem are you starting from? | New math almost always grows from old math — the starting point determines what's reachable |
| 3 | **Abstraction Level** | Are you working at the concrete (examples, computations), mid-level (theorems, structures), or meta-level (categories, foundations)? | Each level has different discovery modes; most people stay at one level and miss opportunities at others |
| 4 | **Inter-domain Distance** | How far apart are the fields being connected? | Close connections are well-mined; distant connections yield the biggest surprises but are hardest to spot |
| 5 | **Constraint Variation** | Which axioms, conditions, or constraints are you relaxing, strengthening, or replacing? | Every axiom is a choice; changing one generates a new mathematical universe |
| 6 | **Computational Accessibility** | Can you generate examples, test conjectures, or visualize objects computationally? | Computation reveals patterns invisible to pure reasoning; inaccessible objects stay unexplored |
| 7 | **Existence of Obstructions** | Are there known impossibility results, no-go theorems, or barriers in this area? | Obstructions mark boundaries — and boundaries are where new math often begins (what happens just outside?) |
| 8 | **Problem Source** | Where does the motivating question come from? (internal to math, physics, CS, biology, engineering, philosophy) | External problems have historically generated entire new fields (calculus from physics, information theory from engineering) |
| 9 | **Formalization Gap** | Is there informal/intuitive mathematical knowledge that hasn't been formalized? | Unformalised intuitions are unexplored territory by definition |
| 10 | **Community Attention** | How many people are working in this area? | Crowded areas have diminishing returns; neglected areas may be neglected for good reason OR may be gold mines |
| 11 | **Tool Availability** | What proof assistants, CAS systems, visualization tools, or AI tools can access this area? | New tools open new areas — the telescope didn't just improve astronomy, it created new astronomy |
| 12 | **Analogical Depth** | Is there a known analogy between two areas that hasn't been fully exploited? | Partial analogies are maps with blank regions — the blanks are where new math lives |

---

## Step 2: Options per Dimension (`/se`)

| Dimension | Possible States |
|-----------|----------------|
| **Discovery Method** | Generalization (weaken hypotheses) / Specialization (add constraints, find structure) / Connection (bridge two fields) / Axiom mutation (change foundational rules) / Problem-driven (solve an open problem, see what tools are needed) / Computation-driven (find patterns, then explain) / Obstruction analysis (find what blocks a result, study the blockage) / Analogy transfer (import machinery from field A to field B) |
| **Existing Structure** | Algebraic (groups, rings, fields, modules) / Geometric (manifolds, metric spaces, schemes) / Topological (homotopy, homology, sheaves) / Combinatorial (graphs, matroids, posets) / Analytic (functions, operators, measures) / Logical (models, proofs, computability) / Number-theoretic / Probabilistic / Categorical |
| **Abstraction Level** | Concrete examples & computations / Specific theorems & proofs / General theories & structures / Meta-level (foundations, category theory, type theory) |
| **Inter-domain Distance** | Same subfield / Adjacent subfields / Different branches of math / Math + another science / Math + non-science domain |
| **Constraint Variation** | Relax a condition / Strengthen a condition / Replace a condition with a different one / Remove a condition entirely / Add a new condition / Change the base field/ring / Change finite → infinite or vice versa / Change commutative → noncommutative |
| **Computational Accessibility** | Fully computable (can enumerate, test, visualize) / Partially computable (some aspects) / Theoretically computable but intractable / Not computable |
| **Obstructions** | None known / Known impossibility with clean boundary / Known impossibility with fuzzy boundary / Conjectured impossibility / Known to be independent of standard axioms |
| **Problem Source** | Pure math internal / Physics / Computer science / Biology / Engineering / Economics / Philosophy / Data science |
| **Formalization Gap** | Fully formalized / Partially formalized / Intuitive but unformalised / No existing framework |
| **Community Attention** | Hot topic (>100 active researchers) / Active (10-100) / Niche (<10) / Abandoned / Never studied |
| **Tool Availability** | Rich toolset exists / Some tools / Tools from adjacent field could apply / No tools yet |
| **Analogical Depth** | No known analogy / Surface analogy noted / Partial dictionary exists / Deep functor-level correspondence (partially exploited) / Fully exploited analogy |

**Key interactions**:
- Axiom mutation + Low community attention = high chance of virgin territory
- Deep partial analogy + Computation accessible = systematic discovery possible
- External problem source + No existing framework = potential for new field creation
- Known obstruction + Constraint variation = finding what's possible just outside the boundary

---

## Step 3: Hidden Assumptions (`/aex`)

What do people implicitly assume about mathematical discovery?

| # | Hidden Assumption | Why It's Dangerous |
|---|-------------------|--------------------|
| 1 | **"New math requires genius-level insight"** | Most new math is systematic: generalize, specialize, connect, compute. The methods are mechanical even when the results are surprising. |
| 2 | **"If an area is unexplored, it's probably uninteresting"** | Many unexplored areas are simply unfashionable, or they require tools that didn't exist until recently. Lack of exploration ≠ lack of value. |
| 3 | **"You need to understand an entire field before contributing"** | Outsiders with fresh perspectives and tools from other fields have historically made major discoveries. Deep expertise helps, but isn't always necessary. |
| 4 | **"The important open problems are well-known"** | The most important undiscovered problems are by definition unknown. The known open problems are already being attacked. |
| 5 | **"Computation is just for checking proofs"** | Computation is a *discovery* tool. Patterns found computationally (Ramanujan's notebooks, experimental mathematics) have generated entire research programs. |
| 6 | **"Generalizing always yields something interesting"** | Sometimes generalizing destroys the structure that made the original interesting. The art is knowing *which* constraints to relax. |
| 7 | **"Mathematics progresses linearly from foundations up"** | Math often develops backward — results are discovered, then foundations are built to explain them. Starting from foundations and working up misses areas that would be found by starting from phenomena. |
| 8 | **"Analogy between fields is metaphorical, not precise"** | The deepest discoveries come from making analogies *precise*. Langlands program, algebraic topology, category theory — all from taking analogies literally. |
| 9 | **"You should work on what your advisor/community works on"** | Social clustering leaves systematic gaps. The highest-value areas are often in the spaces *between* research communities. |
| 10 | **"If I can't prove a theorem about it, it's not math"** | Conjectures, computational patterns, new definitions, and framework proposals are all legitimate mathematical contributions. Demanding proofs first blocks exploration. |

---

## Step 4: The Procedure (`/stg`)

```
DISCOVERING NEW MATH — PROCEDURE
=================================

PURPOSE: Given a desire to find new mathematics or identify
unexplored mathematical areas, this procedure produces
concrete candidate areas and methods to explore them.

STEP 0: What is your starting point?
┌────────────────────────────────────┬───────────────┐
│ Starting Point                     │ Go to         │
├────────────────────────────────────┼───────────────┤
│ I have a specific theorem/object   │ SECTION A     │
│ I want to extend or modify         │               │
├────────────────────────────────────┼───────────────┤
│ I have two fields I want to        │ SECTION B     │
│ connect                            │               │
├────────────────────────────────────┼───────────────┤
│ I have a problem from outside      │ SECTION C     │
│ math that needs new tools          │               │
├────────────────────────────────────┼───────────────┤
│ I want to systematically find      │ SECTION D     │
│ unexplored regions                 │               │
├────────────────────────────────────┼───────────────┤
│ I don't have a starting point      │ SECTION E     │
└────────────────────────────────────┴───────────────┘


═══════════════════════════════════════════════════
SECTION A: Extending or Modifying Known Mathematics
═══════════════════════════════════════════════════

Step A1: Write down the theorem, definition, or
         mathematical object you're starting from.
  → What you should see: Something like "The
    fundamental theorem of algebra" or "The
    category of finite groups" or "Riemann surfaces."

Step A2: List every CONDITION, HYPOTHESIS, or AXIOM
         that this object/theorem depends on.
  → Write them ALL out. Number them.
  → Example: "Fundamental theorem of algebra"
    requires: (1) algebraically closed field,
    (2) polynomial (finite degree), (3) single
    variable, (4) coefficients in the field.
  → If you have fewer than 3, you haven't looked
    hard enough. Re-examine.

Step A3: For EACH condition from A2, ask these
         questions. Write answers for each:

  (a) What happens if I REMOVE this condition?
      → Does the theorem still hold? If not, what
        breaks? What replaces it?
      → If no one has studied this: CANDIDATE AREA.

  (b) What happens if I REPLACE this condition
      with a weaker version?
      → Example: "algebraically closed" → "real closed"
        → "ordered field" → "arbitrary field"
      → At what point does the theorem break? What
        lives at the boundary?
      → If the boundary hasn't been mapped: CANDIDATE AREA.

  (c) What happens if I STRENGTHEN this condition?
      → Adding constraints sometimes reveals hidden
        structure. Example: restricting to
        "polynomials with integer coefficients" gives
        algebraic number theory.
      → If the restricted case hasn't been studied
        systematically: CANDIDATE AREA.

  (d) What happens if I change the BASE SETTING?
      → Finite → infinite. Commutative → noncommutative.
        Discrete → continuous. Deterministic →
        probabilistic. Classical → quantum.
      → Each substitution generates a potential area.

Step A4: For each CANDIDATE AREA from A3:
  → Search: has anyone studied this?
    (a) Search MathSciNet/zbMATH for the modified
        conditions.
    (b) Search arXiv for related terms.
    (c) Ask: is this a known open area, a solved
        area, or genuinely unstudied?
  → RESULT:
    → Already well-studied → Cross off, move to next.
    → Studied but incompletely → Promising. Go to A5.
    → No results found → Either trivial or unexplored.
       Go to A5.

Step A5: Viability check for each surviving candidate.
  → Can you compute at least ONE non-trivial example
    in this modified setting?
    → YES: Write it down. Does it show interesting
           structure (patterns, symmetries, surprises)?
      → YES: This is a VIABLE discovery area. Record it.
      → NO: The modification may destroy what's
            interesting. Move to next candidate.
    → NO: Can you PROVE anything (even something small)
          in this setting?
      → YES: Record what you proved. This is a foothold.
             VIABLE area.
      → NO: The area may be too hard or too degenerate.
            Move to next candidate, but note this one
            for future revisiting with better tools.


═══════════════════════════════════════════════════
SECTION B: Connecting Two Fields
═══════════════════════════════════════════════════

Step B1: Name the two fields or areas.
  → What you should see: Two named areas like
    "knot theory and number theory" or "tropical
    geometry and phylogenetics."

Step B2: For each field, list the CENTRAL OBJECTS
         (what you study) and CENTRAL OPERATIONS
         (what you do to them).
  → Field 1 objects: _________ operations: _________
  → Field 2 objects: _________ operations: _________

Step B3: Build an analogy table.
  → For each object in Field 1, ask: is there a
    corresponding object in Field 2?
  → For each operation in Field 1, ask: is there a
    corresponding operation in Field 2?
  → Write down ALL correspondences you can find,
    even partial or speculative ones.

  ┌──────────────┬──────────────┬───────────────┐
  │ Field 1      │ Field 2      │ Correspondence│
  │              │              │ (precise/     │
  │              │              │ partial/guess)│
  ├──────────────┼──────────────┼───────────────┤
  │              │              │               │
  │              │              │               │
  └──────────────┴──────────────┴───────────────┘

Step B4: Look for GAPS in the table.
  → Objects in Field 1 with NO correspondent in
    Field 2: What SHOULD the correspondent be?
    → Each gap is a potential new definition.
  → Theorems in Field 1: does the analogous
    statement in Field 2 even make sense?
    → If it makes sense but is unproven:
      CANDIDATE CONJECTURE.
    → If it doesn't make sense yet: defining
      the right framework to make it make sense
      is CANDIDATE NEW THEORY.

Step B5: Is there a known FUNCTOR, DICTIONARY, or
         TRANSLATION between these fields?
  → YES, fully developed: The easy discoveries are
    made. Look for where the functor breaks down or
    is not fully faithful — those points are where
    new math lives.
  → YES, partially developed: Extending the
    dictionary is a VIABLE research direction.
  → NO: Building one is potentially a major
    contribution. Go to B6.

Step B6: Can you construct even ONE precise
         correspondence (not just analogy)?
  → Example: an explicit map, a shared structure,
    a common generalization.
  → YES: You have the seed of a bridge. VIABLE
         discovery area.
  → NO: The connection may be superficial. Try a
        different pair of fields (return to B1) OR
        look for an intermediate field that connects
        to both.


═══════════════════════════════════════════════════
SECTION C: External Problem Needing New Tools
═══════════════════════════════════════════════════

Step C1: Write the external problem as precisely as
         you can. What do you need to calculate,
         predict, classify, or optimize?

Step C2: What is the mathematical SHAPE of this
         problem? Classify it:
  → Optimization (finding best among options)
  → Classification (sorting objects into types)
  → Prediction (modeling dynamics over time)
  → Enumeration (counting configurations)
  → Approximation (finding near-solutions)
  → Structural (understanding why something works)
  → Multiple of the above → list all that apply.

Step C3: For each mathematical shape from C2, what
         EXISTING mathematical tools address problems
         of this shape?
  → Write them down.
  → Have they been applied to your specific problem?
    → YES, and they work: No new math needed (but
       you might find new math in the details).
    → YES, and they PARTIALLY work: What specifically
       fails? The failure mode points to missing
       mathematics. CANDIDATE AREA.
    → NO: Try applying them. If they don't fit, go
       to C4.

Step C4: WHY don't existing tools work?
  → The problem has a feature that existing theory
    doesn't handle. Name that feature.
  → Examples:
    - "The space is not smooth" → need non-smooth
      analysis
    - "The objects are too large to enumerate" →
      need asymptotic or probabilistic methods
    - "The structure is self-referential" → need
      fixed-point theory or type theory
    - "The system has no nice symmetries" → need
      tools that work without symmetry
  → The named feature IS the new math you need.
    Search: has anyone built tools for this feature
    in a different context?
    → YES: Import and adapt. This is a VIABLE
           discovery path.
    → NO: You may need to build new tools from
          scratch. CANDIDATE NEW FIELD.

Step C5: Can you state ONE precise mathematical
         question that, if answered, would solve your
         problem?
  → YES: You have a well-defined problem. Search for
         it or similar problems in the literature.
  → NO: The problem isn't yet mathematical. You need
        to FORMALIZE first. The formalization itself
        may be the discovery (as when Shannon
        formalized "information").


═══════════════════════════════════════════════════
SECTION D: Systematic Search for Unexplored Regions
═══════════════════════════════════════════════════

Step D1: Pick a MATHEMATICAL LANDSCAPE to survey.
  → This could be: a branch of math (algebra,
    topology, analysis), a specific theory (group
    theory, graph theory), or a class of objects
    (manifolds, lattices, automata).

Step D2: Map the landscape using this grid.
  → List the MAIN OBJECTS studied in this area
    (rows).
  → List the MAIN QUESTIONS asked about them
    (columns): classification, enumeration,
    structure theorems, algorithms, connections
    to other areas, computational complexity.
  → Fill in each cell: Solved / Open / Partially
    known / Never asked.

  ┌──────────┬──────────┬──────────┬──────────┐
  │          │ Classify │ Count    │ Compute  │...
  ├──────────┼──────────┼──────────┼──────────┤
  │ Object 1 │ Solved   │ Open     │ Never    │
  │ Object 2 │ Partial  │ Solved   │ Open     │
  │ Object 3 │ Never    │ Never    │ Never    │
  └──────────┴──────────┴──────────┴──────────┘

Step D3: Look at the "Never asked" cells.
  → For each one: Is there a reason no one has
    asked this? (trivial? ill-defined? requires
    non-existent tools?)
    → Trivial: Skip.
    → Ill-defined: Can you make it well-defined?
      If yes, CANDIDATE AREA.
    → Requires non-existent tools: CANDIDATE AREA
      (building the tools is the discovery).
    → No obvious reason: CANDIDATE AREA (may be
      a genuine gap in the literature).

Step D4: Look for DIMENSIONAL GAPS.
  → Most areas are studied in specific dimensions
    or parameter ranges. Example: knot theory in
    3D, but what about in 4D? 5D?
  → List the parameters of your area. For each:
    what values have been studied? What values
    haven't?
  → Unstudied parameter values = CANDIDATE AREA.

Step D5: Look for TOOL GAPS.
  → What tools are used in this area?
  → What tools exist in OTHER areas that have never
    been applied here?
  → Example: machine learning applied to knot
    invariants, topological methods applied to
    data science, probabilistic methods applied
    to number theory.
  → Each unapplied tool = CANDIDATE APPROACH.

Step D6: Prioritize your candidates.
  → For each candidate area from D3-D5, score:
    (a) Can I compute an example? (YES=2, MAYBE=1, NO=0)
    (b) Does it connect to known important problems?
        (YES=2, MAYBE=1, NO=0)
    (c) Are there fewer than 10 papers on this?
        (YES=2, SOME=1, NO=0)
  → Rank by total score. Top candidates are your
    best bets.


═══════════════════════════════════════════════════
SECTION E: No Starting Point
═══════════════════════════════════════════════════

Step E1: What kind of math do you enjoy working with?
  → Algebra (manipulating symbols, abstract structures)
  → Geometry/Topology (shapes, spaces, deformations)
  → Analysis (limits, continuity, approximation)
  → Combinatorics (counting, arrangements, algorithms)
  → Logic/Foundations (axioms, proofs, computability)
  → Applied (modeling, simulation, optimization)
  → Multiple: pick whichever you find most fun.

Step E2: Go read the SURVEY PAPERS from the last 3
         years in your chosen area.
  → Sources: Bulletin of the AMS, Notices of the AMS,
    ICM proceedings, Annual Review of Mathematics.
  → As you read, write down every mention of:
    (a) "It is not known whether..."
    (b) "This suggests that..."
    (c) "It would be interesting to..."
    (d) "No analog exists for..."
  → Each of these phrases points to unexplored
    territory.

Step E3: Pick the most interesting gap from E2.
  → Go to SECTION A (if it involves modifying known
    math), SECTION B (if it involves connecting
    fields), or SECTION C (if it involves an
    external problem).

Step E4: If survey papers don't excite you:
  → Try the EXPERIMENTAL approach.
    (a) Pick any mathematical object you understand.
    (b) Compute 50-100 examples using a computer.
    (c) Look for patterns in the data.
    (d) Try to prove or disprove the patterns.
  → If you find a pattern you can't explain,
    you've found unexplored math.
```

---

## Step 5: Failure Modes (`/fla`)

| # | Failure Mode | How to Recognize It | What to Do Instead |
|---|-------------|--------------------|--------------------|
| 1 | **"This must already be known"** — assuming someone has already explored your candidate area | You find a candidate but immediately dismiss it without searching | ALWAYS search before dismissing. Many "obvious" questions have genuinely never been asked. Search MathSciNet, arXiv, and MathOverflow. If you find nothing after 30 minutes of searching, treat it as genuinely unexplored. |
| 2 | **Generalization graveyard** — removing all constraints until nothing interesting remains | Your generalized object has no non-trivial theorems and every question about it is either trivial or impossible | You've over-generalized. Go back and ADD constraints until structure reappears. The sweet spot is the weakest conditions under which interesting structure still exists. |
| 3 | **Analogy without precision** — claiming two fields are "related" without any concrete correspondence | You can describe the analogy in English but can't write a single formal statement that makes it precise | The analogy may be real but you haven't found the right formalization. Try: can you define a map between specific objects? If not after genuine effort, the analogy may be superficial. |
| 4 | **Tool obsession** — applying your favorite tool everywhere regardless of fit | You keep trying to use [category theory / machine learning / algebraic geometry / etc.] and it keeps not quite working | The tool should fit the problem, not the other way around. If you've tried 3 times and it doesn't fit, put the tool down and ask what tool the problem WANTS. |
| 5 | **Fashion following** — working on what's trendy rather than what's open | You notice your candidate area is exactly what everyone at the last conference was talking about | Hot areas have many workers and diminishing marginal returns. Deliberately look one field over from the hot area — the adjacent neglected zone often has better opportunities. |
| 6 | **Premature formalism** — trying to build a complete theory before having enough examples | You have definitions and axioms but no examples or computations | Stop axiomatizing. Compute 20 examples first. If you can't compute examples, your definitions may be wrong or your area may be empty. |
| 7 | **Ignoring computation** — doing everything by hand when a computer could reveal patterns | You've spent weeks on hand calculations and haven't found anything | Write code. Enumerate examples. Plot data. Visualization and computation have discovered more math than most people admit. Sage, Mathematica, GAP, Macaulay2, etc. |
| 8 | **Single-method fixation** — only using Section A when Section B or D would be more productive | You've done 50 axiom variations and found nothing | Switch sections. If extending known math doesn't work, try connecting fields (B) or doing a systematic survey (D). |

---

## Step 6: Validation Check (`/pv`)

Validation sweep:

- **All steps use concrete actions** (write, list, search, compute, fill in grid) — not "contemplate" or "ponder." PASS.
- **All decision points are binary or explicit multiple choice.** PASS.
- **Jargon**: Some mathematical terms used (functor, axiom, manifold) but each appears in context where a math-literate reader would understand. Target audience is someone with undergraduate math. PASS for target audience.
- **Every path terminates** at a VIABLE/NOT VIABLE verdict or a redirect to another section. PASS.
- **No dead ends or loops.** PASS — E redirects to A/B/C; all sections end with concrete outputs.
- **Scoring rubric in D6 is mechanical and unambiguous.** PASS.

One fix applied: Step A4 originally said "check the literature" without specifying how. Replaced with specific search targets (MathSciNet, zbMATH, arXiv).

---

## QUICK REFERENCE CARDS

**The 5 Core Discovery Methods:**
1. **Mutate** — Change an axiom, weaken a condition, swap a base setting
2. **Connect** — Build a bridge between two fields via analogy made precise
3. **Import** — Bring tools from one area into another where they've never been used
4. **Compute** — Generate examples until patterns emerge, then explain the patterns
5. **Formalize** — Take an informal/intuitive idea and make it mathematically precise

**The Fast Version (10 Minutes):**
1. Pick any theorem you know well
2. List its conditions
3. Change ONE condition
4. Ask: "What happens now?"
5. If you can't find the answer in the literature, you've found unexplored math

**The One Question That Finds the Most New Math:**
> "What is the RIGHT analog of [known object X] in [different setting Y]?"
> If the answer isn't obvious, the search for it IS the new math.

---

## COMMON MISTAKES

1. **Thinking discovery requires reading everything first** — You will never finish reading. Start exploring early with incomplete knowledge. Fill gaps as you need them, not preemptively.
2. **Skipping computation** — Most working mathematicians compute far more than their papers suggest. If you're not computing, you're navigating blind.
3. **Confusing "no one has done this" with "this is worth doing"** — Not all unexplored areas are interesting. The viability check (can you compute an example? does it connect to anything?) is essential.
4. **Only looking within your own field** — The richest discoveries come from importing ideas across field boundaries. Read one paper per month from a field you don't work in.
5. **Waiting for a "big idea"** — Most new math starts with a small observation ("huh, that's weird") followed by systematic investigation. Don't wait for inspiration; run the procedure.
6. **Over-abstracting before you have enough examples** — Definitions and axiom systems should emerge from examples, not precede them. "What structure do these examples share?" beats "Let me define a new structure and see if examples exist."

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **You have genuine mathematical intuition about a specific problem** — If you have a strong hunch, follow it first. Come back to systematic methods if the hunch doesn't pan out.
- **You're working with a collaborator who has complementary expertise** — Conversation with a knowledgeable partner can short-circuit the entire procedure. The procedure is most valuable when working alone.
- **You're reading a paper and spot an error or gap** — Investigating errors and gaps in existing work is a powerful discovery method not covered by this procedure. Follow the thread.
- **An established mathematician suggests a direction** — Expert taste (knowing what's "ripe") is real and hard to formalize. If someone with decades of experience says "look here," look there.

---

## WORKED EXAMPLES

### Example 1: Starting from the Fundamental Theorem of Algebra

**Section A (Extending Known Math)**
- A1: "Every non-constant polynomial over ℂ has a root in ℂ."
- A2: Conditions: (1) algebraically closed field, (2) polynomial (finite degree), (3) single variable, (4) coefficients in the field.
- A3 applied to condition (3) — change ℂ:
  - Replace ℂ with p-adic fields → studied (p-adic analysis, Hensel's lemma). Not a gap.
  - Replace ℂ with function fields → partially studied. Some open questions about analogs. CANDIDATE.
  - Replace ℂ with tropical semiring → tropical geometry! This was a major discovery area starting ~2000s.
- A3 applied to condition (4) — multiple variables:
  - Already a huge field (algebraic geometry). Well-studied.
- A3 applied to condition (5) — approximate zeros:
  - "Approximate fundamental theorem" → connects to numerical algebraic geometry. Active area with gaps. CANDIDATE.
- A4: Tropical FTA → rich literature. Approximate FTA → some papers, still developing. Function field analogs → sparse. Best candidate: **function field analogs**.

### Example 2: Connecting Knot Theory and Machine Learning

**Section B (Connecting Fields)**
- B1: Knot theory + Machine learning.
- B2: Knot theory objects: knots, links, braids, invariants. Operations: Reidemeister moves, connected sum, satellite operations. ML objects: datasets, models, loss functions. Operations: training, evaluation, feature extraction.
- B3 Analogy table: Knot invariants ↔ learned features. Reidemeister moves ↔ data augmentation (transformations that preserve the label). Classification of knots ↔ classification task.
- B4 Gaps: ML can predict knot invariants (DeepMind 2021 result), but: Can ML discover NEW invariants? Can it find the right *representation* of a knot for a given task? What topological structure does the learned feature space have?
- B5: Partial dictionary exists (several papers). Extending it is viable.
- **Result**: VIABLE area — using ML to discover structure in knot invariant relationships, and conversely using knot-theoretic ideas to understand neural network topology.

### Example 3: Systematic Survey of Matroid Theory

**Section D (Finding Gaps)**
- D1: Matroid theory.
- D2: Grid filled. Objects: matroids, oriented matroids, valuated matroids, flag matroids. Questions: classification, enumeration, algorithms, connections.
  - "Classify valuated matroids" → NEVER ASKED (valuated matroids are recent, classification not attempted).
  - "Enumerate flag matroids" → NEVER ASKED.
  - "Algorithms for delta-matroids" → PARTIAL (few complexity results).
- D4: Dimensional gaps — most matroid theory is for finite matroids. Infinite matroids were only axiomatized in 2013. Many basic questions remain open.
- D5: Tool gaps — persistent homology (from topological data analysis) has never been applied to matroid complexes.
- D6 scoring: Infinite matroid open questions (compute=2, connects=2, sparse=2, total=6). Persistent homology on matroid complexes (2+1+2=5). Valuated matroid classification (1+1+2=4).
- **Result**: Top candidate — **infinite matroid theory**, with **topological data analysis methods on matroid complexes** as second priority.

---

*Validation status: This procedure has not been validated by domain experts. It synthesizes methods from mathematical practice, philosophy of mathematics, and research methodology.*
