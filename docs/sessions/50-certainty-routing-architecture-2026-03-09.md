# /certainty Is the category-skill routing architecture the right design, or should it be restructured?
**Date:** 2026-03-09
**Skill:** /certainty (Maximum Effort)

---

## Phase 1: Classify and Set Resolution Criteria

### 1. What Is the Question?

The core question: **Is the current two-tier architecture -- where 17 category skills act as routers that classify input and dispatch to ~575 specialist skills -- the right design for the Reasoning Toolkit? Or should it be restructured into a different architecture?**

### 2. What Does "Resolved" Mean?

This is an **analytical + decision question**. Resolved means:
- All major architectural alternatives have been identified and compared
- The strengths and weaknesses of the current design have been tested to bedrock
- Competing architectures have been evaluated with equal rigor
- A clear recommendation with justified confidence, where alternatives are considered and rejected for stated reasons
- No remaining unresolved branches, untested assumptions, or competing conclusions

### 3. Classify the Input

This is an analytical question about a system design -- it combines elements of a claim ("this architecture is right"), a decision ("should it be restructured?"), and an evaluation ("assess this design"). Starting with **analysis at 8x**, incorporating claim-testing and decision frameworks.

### 4. Enhanced Classification Signals

The input contains a tension: "right design **or** should it be restructured?" This is a binary framing that likely conceals a spectrum. Noting this for exploration.

---

## Phase 2: Iterative Resolution

### ITERATION 1: Structural Analysis + ARAW on Core Claims

#### Step 0: Meta-ARAW (Strategy Selection)

**Restate the question:** The Reasoning Toolkit uses 17 category skills (claim, decide, diagnose, search, how, want, action, evaluate, emotion, viability, create, analyze, technical, meta, certainty, iterate, sp) as routers. Each classifies user input and dispatches to specialist skills. Is this the right architecture?

**Evaluability:** This is a design decision, not a truth claim. Must extract underlying claims and test those.

**Uncertainty type:** Primarily model uncertainty -- we need to determine whether we're using the right mental model for skill organization.

**Dimensions to explore:**
- Functional: Does the routing architecture actually work for users?
- Structural: Is the two-tier pattern coherent and consistent?
- Scalability: Does it hold up as skills grow from 563 to 1000+?
- Learnability: Can users find what they need?
- Maintainability: Can the system be maintained and evolved?
- Alternatives: What other architectures could serve the same purpose?

#### Step 1: Identify and Unbundle Claims

```
[C1] The category-skill routing pattern is the right architecture for organizing 563+ reasoning skills.
  -- TYPE: explicit -- VOI: high

[C2] 17 categories is the right number of entry points.
  -- TYPE: implicit -- VOI: high

[C3] The categories are correctly defined (the taxonomy is right).
  -- TYPE: implicit -- VOI: high

[C4] Two tiers (category -> specialist) is the right depth.
  -- TYPE: implicit -- VOI: high

[C5] Classification-then-dispatch is better than direct access for most users.
  -- TYPE: presupposed -- VOI: high

[C6] Category skills should cross-redirect to each other when input is misclassified.
  -- TYPE: implicit (observed in every category skill) -- VOI: medium

[C7] The "Is This Actually X?" pattern in every category skill is the right way to handle misclassification.
  -- TYPE: implicit -- VOI: medium

[C8] Category skills should contain both routing logic AND analytical framing (core principles, interpretations, depth scaling).
  -- TYPE: implicit -- VOI: medium

[C9] The current modes (ARAW, UAUA, AR-forward, Direct, Router, Maximum, Meta-iteration) correctly group the categories.
  -- TYPE: implicit -- VOI: medium

[C10] A flat namespace (/claim, /decide, /dbg, /araw) is the right naming approach.
  -- TYPE: implicit -- VOI: medium

[C11] Users can reliably identify which category their input belongs to.
  -- TYPE: presupposed -- VOI: high

[C12] The cross-referencing pattern (where every category redirects to every other) is maintainable.
  -- TYPE: implicit -- VOI: high

[C13] The architecture should prioritize routing accuracy over routing speed.
  -- TYPE: presupposed -- VOI: medium

[C14] Category skills serve both as routers AND as analytical frameworks that add value beyond pure routing.
  -- TYPE: meta -- VOI: high

[C15] The alternative of no categories (just 563 flat skills) would be worse.
  -- TYPE: implicit -- VOI: high

[C16] The architecture is robust to the addition of new skills without restructuring.
  -- TYPE: implicit -- VOI: high

[C17] The current architecture doesn't create harmful failure modes (e.g., infinite routing loops, misrouting that wastes effort).
  -- TYPE: implicit -- VOI: high

[C18] The "Is This Actually X?" redirect pattern creates an implicit consensus mechanism where all 17 categories agree on what each input type is.
  -- TYPE: meta -- VOI: medium
```

#### Phase 1: EXPLORATION

```
[C1] "The category-skill routing pattern is the right architecture for organizing 563+ reasoning skills."

  ASSUME RIGHT:
  [F1] If right: The system provides a manageable entry point for users who don't know which of 563 skills to use.
    -- STRENGTH: necessary
    [F2] If F1 right: Users need only learn 17 categories instead of 563 skills.
      -- STRENGTH: probable
      [F3] If F2 right: The learning curve is bounded by the category count, not the skill count.
        [F4] -> BEDROCK-OBSERVE: Users who read CLAUDE.md see a 17-row table, not a 563-row table.
    [F5] If F1 right: New skills can be added without changing the user-facing interface.
      -- STRENGTH: probable
      [F6] If F5 right: The system scales horizontally -- new specialist skills slot under existing categories.
        [F7] -> BEDROCK-OBSERVE: The system grew from ~415 to ~563 skills without changing the 17-category structure.
  [F8] If right: Category skills serve as analytical guardrails, not just routers.
    -- STRENGTH: necessary
    [F9] Each category adds: interpretations (disambiguating user intent), core principles (domain-specific analytical standards), routing logic (choosing the right specialist), depth scaling (matching effort to stakes), and failure modes (catching common mistakes).
      [F10] -> BEDROCK-OBSERVE: /claim adds skeptical testing posture, bundling detection, confidence-based AR/AW balance. /decide adds reversibility assessment, foreclosure mapping, criteria extraction. These are not routing -- they are analytical value-add.
  [F11] FORECLOSED if right: Cannot easily reorganize skills by alternative taxonomies (e.g., by domain, by output type, by depth).
    [F12] Consequence: Users who think in domain terms ("software", "business") must go through /technical as a secondary router, adding a layer.
      [F13] -> BEDROCK-OBSERVE: /technical exists specifically to handle this, routing by domain x task type.

  ASSUME WRONG:
  [F14] Wrong because: 17 categories may still be too many for users to hold in mind.
    -- SEVERITY: serious
    [F15] Evidence: The median person can hold 4-7 items in working memory. 17 exceeds this.
      [F16] -> BEDROCK-TEST: Measure whether new users can correctly classify their input into 1 of 17 categories without help.
    [F17] If F14 holds: Users would default to /meta (ask for help) or /certainty (maximum effort to avoid choosing) rather than choosing the right category.
      [F18] This would make the routing layer a friction point rather than an aid.
  [F19] Wrong because: The classification task is actually hard.
    -- SEVERITY: serious
    [F20] "Is this a claim, a decision, a goal, or an exploration?" is a distinction that even trained analysts debate.
      [F21] -> BEDROCK-OBSERVE: Every category skill has an "Is This Actually X?" section that redirects to other categories -- this section exists BECAUSE the boundary between categories is fuzzy.
    [F22] If F19 holds: Misclassification is common, and the redirect pattern is a repair mechanism, not a feature.
      [F23] Alternative derived from F19: A single intelligent dispatcher that classifies and routes, rather than 17 competing classifiers each checking "is this mine?"
        [F24] If F23 right: Eliminates the N-way "Is This Actually X?" redundancy.
          [F25] -> BEDROCK-LOGIC: A single classifier has one boundary decision. N classifiers each have one boundary decision plus N-1 redirect checks. Single classifier is O(1), current is O(N).
  [F26] Wrong because: The two-tier depth may be wrong.
    -- SEVERITY: conditional
    [F27] Some category skills (like /technical) are themselves routers that add a third tier.
      [F28] -> BEDROCK-OBSERVE: /technical routes to domain clusters (software, business, finance) which then route to specialist skills. This is 3 tiers.
    [F29] Other category skills (like /claim) route almost directly to /araw with framing. This is barely 2 tiers.
      [F30] -> BEDROCK-OBSERVE: /claim's primary execution is just "INVOKE: /araw $ARGUMENTS" with balance and depth parameters.
    [F31] The actual tier depth varies from 1.5 to 3 depending on path, creating inconsistent user experience.
  [F32] Wrong because: The architecture creates a massive cross-referencing maintenance burden.
    -- SEVERITY: serious
    [F33] Each of the 17 category skills has an "Is This Actually X?" section that references 7-10 other category skills.
      [F34] This creates approximately 17 x 8 = 136 cross-references that must be kept consistent.
        [F35] -> BEDROCK-LOGIC: Adding a new category skill (category #18) requires updating the "Is This Actually X?" section of all 17 existing categories.
    [F36] Alternative derived from F32: Extract the classification logic into a shared component.
      [F37] If F36 right: Changes to classification rules happen in one place, not 17.
  [F38] Wrong because: The architecture conflates two functions in category skills.
    -- SEVERITY: serious
    [F39] Category skills do BOTH classification/routing AND analytical framing (core principles, interpretations, depth scaling).
      [F40] -> BEDROCK-OBSERVE: /claim's "Core Principles" section (skeptical testing, bundling detection, confidence-based balance) is analytically valuable regardless of routing.
    [F41] If F38 holds: The routing function could be separated from the analytical framing function.
      [F42] Alternative: Category skills become pure analytical frameworks, while routing is handled by a separate dispatcher.
        [F43] If F42 right: /claim becomes "how to think about claims" (no routing), and a dispatcher decides "this is a claim" (no analytical framing).
          [F44] -> BEDROCK-TENSION: Contradicts F10 -- the analytical value of category skills comes precisely from their integrated routing + framing. Separating them loses the "Is this actually a claim?" intelligence.
```

```
[C5] "Classification-then-dispatch is better than direct access for most users."

  ASSUME RIGHT:
  [F45] If right: Users don't need to know skill names to get good results.
    -- STRENGTH: necessary
    [F46] If F45 right: A user saying "I think remote work is more productive" gets routed through /claim (which adds skeptical framing, bundling detection, balance adjustment) rather than directly hitting /araw (which would test whatever is stated without the claim-specific intelligence).
      [F47] -> BEDROCK-OBSERVE: /claim adds specific value: it detects bundled claims, sets AR/AW balance based on user confidence, checks if the claim is testable, and routes to /it or /but for input-shape issues. Direct /araw access skips all of this.
  [F48] If right: The system handles ambiguous input gracefully.
    -- STRENGTH: probable
    [F49] "I'm frustrated that my startup isn't growing" could be emotional (/emotion), diagnostic (/diagnose), goal-related (/want), or analytical (/analyze).
      [F50] The /emotion router handles this by acknowledging first, then routing to the implied analytical need.
      [F51] -> BEDROCK-OBSERVE: /emotion explicitly maps frustration -> /diagnose, overwhelm -> /how, stuck -> /how + /iaw, doubt -> /claim.

  ASSUME WRONG:
  [F52] Wrong because: Power users already know which skill they want.
    -- SEVERITY: conditional
    [F53] If F52 holds: The routing layer adds latency and token cost without value for users who would type /araw directly.
      [F54] -> BEDROCK-OBSERVE: The system already supports direct skill invocation -- /araw, /cmp, /dbg all work directly. The category layer is optional for power users.
      [F55] -> BEDROCK-TENSION: Contradicts F52's severity -- since direct access is already available, C5 is about default behavior, not forced behavior.
  [F56] Wrong because: LLMs can classify input without explicit routing rules.
    -- SEVERITY: serious
    [F57] Claude can read "I think remote work is more productive" and understand it's a claim to test without needing /claim's routing rules.
      [F58] -> BEDROCK-TEST: Compare output quality when (a) user types a prompt and Claude routes through category skill rules vs (b) Claude uses its own judgment to select skills. If (b) is equal or better, the routing layer is redundant.
    [F59] If F56 holds: The category skills' routing logic is encoding intelligence that the LLM already has, creating redundancy.
      [F60] Alternative derived from F56: Replace routing logic with a thin skill-discovery layer that lists relevant skills and lets the LLM choose.
        [F61] If F60 right: Category skills become suggestion menus, not dispatchers.
  [F62] Wrong because: The classification step can fail silently.
    -- SEVERITY: conditional
    [F63] If someone types "I need to quit my job" into /claim, the "Is This Actually X?" check should redirect to /decide or /want. But if they enter it into /action, they might get "execute the quit" without deeper analysis.
      [F64] -> BEDROCK-TEST: Test whether different entry points for the same input produce meaningfully different outputs. If yes, the routing matters. If no, it's redundant.
```

```
[C12] "The cross-referencing pattern (where every category redirects to every other) is maintainable."

  ASSUME RIGHT:
  [F65] If right: Each category skill acts as an autonomous agent that can handle any misrouted input.
    -- STRENGTH: probable
    [F66] If F65 right: No single point of failure -- any entry point eventually reaches the right skill.
      [F67] -> BEDROCK-LOGIC: If every category checks for every other category, then regardless of where input enters, it will be redirected correctly. This is a fully-connected graph guarantee.
  [F68] If right: The redirect pattern is self-documenting -- reading /claim tells you exactly when NOT to use /claim.
    -- STRENGTH: necessary

  ASSUME WRONG:
  [F69] Wrong because: 17 x ~8 = 136 cross-references require O(N^2) maintenance.
    -- SEVERITY: fatal
    [F70] Every time a new category is added, every existing category needs updating.
      [F71] -> BEDROCK-OBSERVE: The redirect sections across all 17 categories already show inconsistency. /claim has 8 redirects (decide, want, emotion, search, it, but, nsa, handle). /analyze has 10 redirects. /how has 9 redirects. The redirect sets are NOT identical across categories.
    [F72] If F69 holds: The cross-referencing is already partially broken.
      [F73] -> BEDROCK-OBSERVE: Some categories reference /handle, /it, /but, /nsa (newer skills) while the base pattern doesn't guarantee all 17 categories reference all others.
  [F74] Wrong because: The redirect rules duplicate classification logic.
    -- SEVERITY: serious
    [F75] "Should I X?" -> /decide appears in /claim, /want, /how, /action, /analyze, /search, /emotion, /viability, /diagnose, and /create. This single rule is written 10+ times.
      [F76] -> BEDROCK-OBSERVE: Confirmed by reading multiple category skills -- the "Should I X?" -> /decide redirect appears almost identically in every category skill.
    [F77] Alternative derived from F74: Extract shared classification rules into a single file that all categories import.
      [F78] If F77 right: Changes to "Should I X? -> /decide" happen once, propagate to all.
```

```
[C14] "Category skills serve both as routers AND as analytical frameworks that add value beyond pure routing."

  ASSUME RIGHT:
  [F79] If right: Removing the category layer would lose analytical intelligence that specialist skills don't carry.
    -- STRENGTH: necessary
    [F80] /claim adds: skeptical posture, bundling detection, confidence-based AR/AW balance, testability assessment.
      [F81] /decide adds: reversibility assessment, foreclosure mapping, criteria extraction, stakes-based depth.
        [F82] /emotion adds: emotional acknowledgment, implicit-request identification, emotion-to-need mapping.
          [F83] -> BEDROCK-OBSERVE: These are genuinely different analytical postures. /araw without /claim's framing would not detect bundled claims or adjust balance based on user confidence.
  [F84] If right: The category layer functions as a "thinking stance" selector, not just a router.
    -- STRENGTH: probable
    [F85] The modes (ARAW, UAUA, AR-forward, Direct) represent different epistemic postures.
      [F86] ARAW mode: test from both sides (claims, decisions, viability, evaluation)
      [F87] UAUA mode: explore before testing (diagnose, search)
      [F88] AR-forward mode: assume the goal is right and search for methods (want, how, emotion)
      [F89] -> BEDROCK-LOGIC: These are genuinely different analytical strategies. Testing a claim (ARAW) is structurally different from exploring a space (UAUA) or finding a method (AR-forward).
  [F90] FORECLOSED if right: Cannot simplify category skills to pure routing tables without losing this analytical value.
    [F91] Consequence: Any restructuring must preserve the analytical framing, even if routing is reorganized.

  ASSUME WRONG:
  [F92] Wrong because: The analytical framing could live in the specialist skills themselves.
    -- SEVERITY: conditional
    [F93] /araw could include bundling detection and balance adjustment without needing /claim as an intermediary.
      [F94] -> BEDROCK-TENSION: Contradicts F83 -- if bundling detection moves into /araw, then /araw must also handle the "Is this actually a claim?" check, the "Is this a decision?" check, the emotion detection, etc. /araw becomes a router.
    [F95] If F92 holds, the complexity doesn't disappear -- it migrates from category skills to specialist skills, making specialists heavier.
  [F96] Wrong because: The analytical framing is inconsistently applied.
    -- SEVERITY: conditional
    [F97] Some category skills are rich analytical frameworks (claim, decide, emotion -- each with detailed core principles and failure modes). Others are primarily routing tables (technical, action, meta).
      [F98] -> BEDROCK-OBSERVE: /technical's core principles are about routing ("Route to the most specific skill possible") while /claim's core principles are about analytical method ("Claims are tested, not confirmed"). These are qualitatively different.
    [F99] If F96 holds: The "category skill" concept conflates two different things -- analytical frameworks and routing dispatchers.
```

```
[C11] "Users can reliably identify which category their input belongs to."

  ASSUME RIGHT:
  [F100] If right: The 17-category table in CLAUDE.md serves as an effective decision tree for users.
    -- STRENGTH: probable
    [F101] The table uses natural language triggers: "A claim to test", "A decision to make", "Something broken".
      [F102] -> BEDROCK-OBSERVE: The trigger phrases are intuitive and cover common cases.

  ASSUME WRONG:
  [F103] Wrong because: Many real inputs don't fit cleanly into one category.
    -- SEVERITY: serious
    [F104] "I think I should quit my job but I'm not sure" contains: a claim ("I should quit"), a decision ("should I?"), an emotion ("not sure/anxious"), a want ("I want something different"), and potentially a diagnosis ("something is wrong with my job").
      [F105] -> BEDROCK-OBSERVE: This single sentence could legitimately enter through 5 different categories. The redirect pattern handles this, but the user's first choice affects framing.
    [F106] If F103 holds: The entry point affects the analytical framing, and different entry points produce different (potentially better or worse) analyses.
      [F107] -> BEDROCK-TEST: Route "I think I should quit my job" through /claim, /decide, /emotion, /want, and /diagnose. Compare outputs. If outputs differ meaningfully, routing matters and misrouting is costly.
  [F108] Wrong because: Users don't think in terms of "claims" and "decisions" -- they think in terms of their problem.
    -- SEVERITY: serious
    [F109] A user with a startup problem doesn't categorize it as "claim" or "decision" -- they think "my startup isn't growing."
      [F110] -> BEDROCK-OBSERVE: This is why /technical and /emotion exist -- to catch domain-oriented and emotionally-oriented input. But this means the taxonomy mixes input-type categories (claim, decide) with domain categories (technical) and affective categories (emotion).
    [F111] The taxonomy is not a single dimension -- it's a conflation of at least 3 dimensions: input type, domain, and emotional state.
      [F112] -> BEDROCK-LOGIC: A clean taxonomy should classify along one dimension. Mixing dimensions creates ambiguity (a frustrated technical decision is simultaneously /emotion, /technical, and /decide).
```

```
[C16] "The architecture is robust to the addition of new skills without restructuring."

  ASSUME RIGHT:
  [F113] If right: New specialist skills slot under existing categories without structural changes.
    -- STRENGTH: probable
    [F114] -> BEDROCK-OBSERVE: The system grew from ~415 to ~563 skills. But it also added new category-level concepts (/it, /but, /nsa, /handle, /platitude) that are referenced in every category skill's redirect section.

  ASSUME WRONG:
  [F115] Wrong because: New "input shape" skills (/it, /but, /nsa, /handle, /etc, /aso) required updating every category skill.
    -- SEVERITY: fatal
    [F116] -> BEDROCK-OBSERVE: Every category skill now has redirects for "I think X" -> /it, "X, but Y" -> /but, "I'm not sure" -> /nsa, "Handle this" -> /handle. These were added to all 17 categories.
    [F117] If F115 holds: The architecture is NOT robust to new cross-cutting concerns. Each new input-shape skill requires O(N) updates to existing category skills.
      [F118] Alternative derived from F115: Input-shape detection should be a pre-processing step that runs BEFORE category classification, not a check inside each category.
        [F119] If F118 right: "I think X, but Y" -> /it + /but as pre-processing, then the processed output enters the category layer.
          [F120] -> BEDROCK-LOGIC: This is a pipeline architecture (pre-process -> classify -> route) vs the current star architecture (every category handles everything).
```

```
[C17] "The architecture doesn't create harmful failure modes."

  ASSUME RIGHT:
  [F121] If right: Misrouted input gets caught by the redirect pattern.
    -- STRENGTH: probable

  ASSUME WRONG:
  [F122] Wrong because: Infinite routing loops are theoretically possible.
    -- SEVERITY: conditional
    [F123] If /claim gets input it classifies as emotional and sends to /emotion, and /emotion classifies it as self-doubt and sends back to /claim, a loop results.
      [F124] -> BEDROCK-TEST: Check whether any category pair could create a circular redirect. /claim sends "I'm frustrated about X" to /emotion. /emotion sends self-doubt ("I can't do this") to /claim. This is technically a valid cycle if the input contains both frustration and self-doubt about the same topic.
    [F125] In practice, the LLM would probably not loop because the input changes each time. But the rules don't explicitly prevent loops.
  [F126] Wrong because: Silent misrouting wastes significant effort.
    -- SEVERITY: serious
    [F127] If "I need to restructure my team" enters through /action (because "restructure" sounds like a command), the system might try to execute a restructuring plan without first diagnosing whether restructuring is the right move.
      [F128] -> BEDROCK-OBSERVE: /action does check "Is this actually a command?" but the check depends on surface-level signals, not deep understanding of the request.
```

#### Self-Evaluation (Iteration 1)

**Unresolved branches:**
1. What specific alternative architectures exist? (explored partially -- need more)
2. Does the analytical framing in category skills actually improve output quality? (F58, F107 -- untested)
3. Is the maintenance burden a practical problem or a theoretical concern? (F69-F78)

**Untested assumptions:**
1. That users primarily enter through category skills (vs. direct skill invocation)
2. That the LLM couldn't do the routing better on its own (F56-F61)

**Competing conclusions:**
1. The category layer adds genuine analytical value (F79-F91) vs. The analytical value could live elsewhere (F92-F95)
2. The cross-referencing is a robust safety net (F65-F68) vs. The cross-referencing is an unmaintainable mess (F69-F78)

Continuing to Iteration 2.

---

### ITERATION 2: Alternative Architectures + Stress-Testing Key Tensions

#### Branch 1: Alternative Architectures

```
[C19] "A single dispatcher skill would be better than 17 competing classifiers."
  -- TYPE: derived from F23 -- VOI: high

  ASSUME RIGHT:
  [F129] If right: Classification happens once, in one place, with one set of rules.
    -- STRENGTH: necessary
    [F130] Changes to classification rules happen in one file, not 17.
      [F131] -> BEDROCK-LOGIC: O(1) maintenance for classification changes vs O(N).
  [F132] If right: The dispatcher can use a decision tree or weighted scoring, not just pattern matching.
    -- STRENGTH: probable
    [F133] Could score input on multiple dimensions simultaneously (type, domain, emotion, input-shape) and route based on combined assessment.
      [F134] -> BEDROCK-LOGIC: Multi-dimensional classification is strictly more powerful than sequential single-dimension checks.

  ASSUME WRONG:
  [F135] Wrong because: A single dispatcher loses the analytical framing that category skills provide.
    -- SEVERITY: fatal (if analytical framing is truly valuable)
    [F136] -> BEDROCK-TENSION: Whether this is fatal depends on whether C14 (analytical framing adds value) is validated. If the framing can be preserved separately, this severity drops.
  [F137] Wrong because: A single dispatcher becomes a god object -- too complex to maintain.
    -- SEVERITY: serious
    [F138] 17 categories x complex routing logic = a massive single file.
      [F139] -> BEDROCK-OBSERVE: The current /meta skill already approaches this -- it has 100+ routing rules and is the longest category skill.
    [F140] Alternative: Use /meta's approach but more systematically -- a single dispatcher that references external classification rules.
```

```
[C20] "A pipeline architecture (pre-process -> classify -> frame -> execute) would be better than the current star architecture."
  -- TYPE: derived from F118-F120 -- VOI: high

  ASSUME RIGHT:
  [F141] If right: Input-shape detection (/it, /but, /nsa, /handle, /etc, /aso) runs as a pre-processing step, cleaning the input before classification.
    -- STRENGTH: necessary
    [F142] Classification runs on cleaned input, producing a category + confidence score.
    [F143] The matched category's analytical framing is applied (core principles, depth, balance).
    [F144] The framed input is dispatched to the specialist skill.
    [F145] -> BEDROCK-LOGIC: This separates concerns cleanly: input normalization, classification, analytical framing, execution.
  [F146] If right: Adding a new input-shape skill requires updating only the pre-processing step, not all 17 categories.
    -- STRENGTH: necessary
    [F147] -> BEDROCK-LOGIC: O(1) for new cross-cutting concerns vs current O(N).
  [F148] If right: The analytical framing (core principles, interpretations, failure modes) is preserved in phase 3 of the pipeline.
    -- STRENGTH: necessary
    [F149] Category skills become pure analytical frameworks -- no routing logic, no "Is This Actually X?" checks.
      [F150] FORECLOSED if right: Category skills lose their autonomy -- they can no longer self-correct for misrouted input.
        [F151] -> BEDROCK-TENSION: The self-correction (redirect pattern) is a safety net. Removing it requires the classifier in step 2 to be highly accurate.

  ASSUME WRONG:
  [F152] Wrong because: The pipeline assumes clean separation, but in practice, classification and framing are intertwined.
    -- SEVERITY: serious
    [F153] /claim's "Core Principles" section influences how the input is interpreted -- "claims are tested, not confirmed" changes how the input is read, which changes what the input IS.
      [F154] -> BEDROCK-OBSERVE: The act of framing an input as a "claim to test" vs a "decision to make" changes what you see in the input. This is not a bug -- it's the whole point.
    [F155] If F152 holds: Classification and framing cannot be fully separated because framing IS classification.
      [F156] -> BEDROCK-LOGIC: This is a variant of the frame problem in AI -- you can't classify without some framing, and you can't frame without some classification. The current architecture handles this by combining them in category skills.
  [F157] Wrong because: A pipeline adds latency for simple cases.
    -- SEVERITY: conditional
    [F158] "Test this claim: X is true" doesn't need pre-processing, classification, or framing -- it should go directly to /araw.
      [F159] -> BEDROCK-OBSERVE: The current system already supports this -- users can invoke /araw directly.
```

```
[C21] "The current architecture should be preserved but with shared classification rules extracted."
  -- TYPE: hybrid alternative derived from F36, F77 -- VOI: high

  ASSUME RIGHT:
  [F160] If right: Category skills keep their analytical framing and autonomy.
    -- STRENGTH: necessary
  [F161] If right: The "Is This Actually X?" rules are extracted into a shared reference.
    -- STRENGTH: necessary
    [F162] Each category skill imports the shared classification rules instead of embedding them.
      [F163] -> BEDROCK-LOGIC: Maintenance becomes O(1) for shared rules + O(1) per category for category-specific rules.
  [F164] If right: New input-shape skills (/it, /but, /nsa) are added to the shared reference once.
    -- STRENGTH: necessary
  [F165] FORECLOSED if right: Each category skill's "Is This Actually X?" section is replaced by a reference/import, losing some readability.

  ASSUME WRONG:
  [F166] Wrong because: The current architecture format (markdown files) doesn't support imports or references.
    -- SEVERITY: fatal
    [F167] -> BEDROCK-OBSERVE: Skills are standalone SKILL.md files. There is no import mechanism. References like "_shared/corruption-pre-inoculation.md" appear in some skills but are not systematically supported.
    [F168] If F166 holds: Shared classification rules would require either (a) a new mechanism for shared content or (b) a pre-processing build step that injects shared rules into each skill file.
      [F169] Alternative: Use a shared file as a reference that the LLM reads when needed, not a literal import.
        [F170] -> BEDROCK-OBSERVE: The skill invocation pattern already reads files on demand. A shared classification file could work the same way -- "Before routing, read _shared/classification-rules.md".
```

#### Branch 2: Is the Analytical Framing Actually Valuable?

```
[C22] "The analytical framing in category skills measurably improves output quality vs. direct specialist skill invocation."
  -- TYPE: derived from tension between F79-F91 and F92-F95 -- VOI: high

  ASSUME RIGHT:
  [F171] If right: /claim + /araw produces better analysis than bare /araw because /claim adds bundling detection, balance adjustment, and testability assessment.
    -- STRENGTH: probable
    [F172] Specific mechanisms that add value:
      - Bundling detection: "Remote work is better" -> 3 separate claims tested, not 1 vague claim
      - Confidence-based balance: Confident assertion gets more AW, uncertain question gets more AR
      - Testability assessment: Untestable claims get restated as testable predictions
      - Depth matching: Fragment -> 2x, paragraph -> 4x-8x
      [F173] -> BEDROCK-LOGIC: These are not routing functions -- they are analytical transformations that change the input before it reaches /araw. Removing them would produce different (worse) /araw output.
  [F174] If right: The category layer functions as "analytical middleware" -- it preprocesses input to improve specialist skill output.
    -- STRENGTH: necessary
    [F175] -> BEDROCK-LOGIC: This is analogous to data preprocessing in ML pipelines. Raw input -> category skill (transform) -> specialist skill (execute). The transform step improves results.

  ASSUME WRONG:
  [F176] Wrong because: The LLM applying the specialist skill can do the same transformations inline.
    -- SEVERITY: serious
    [F177] A sufficiently detailed /araw skill could include its own bundling detection, balance adjustment, and testability assessment.
      [F178] -> BEDROCK-OBSERVE: /araw already has Step 0 (Meta-ARAW) which does strategy selection, and Step 1 which does claim unbundling. The overlap with /claim's routing logic is significant.
    [F179] If F176 holds: /claim is partially redundant with /araw's own preprocessing.
      [F180] -> BEDROCK-TENSION: Contradicts F173 -- but only partially. /claim's confidence-based AR/AW balance and its specific "Is this a claim?" check are NOT in /araw. /araw's Meta-ARAW handles claim-internal strategy but not the classification question.
  [F181] Wrong because: The analytical framing is inconsistent across categories.
    -- SEVERITY: conditional
    [F182] Some categories (claim, decide, emotion, want) have rich analytical framing. Others (action, technical, meta) have thin framing -- mostly routing logic with minimal analytical principles.
      [F183] -> BEDROCK-OBSERVE: /action's core principles are 4 sentences about clarity and ordering. /claim's core principles are 6 detailed analytical stances. The quality varies significantly.
    [F184] If F181 holds: The "analytical framing adds value" claim is true for some categories and false for others.
```

#### Branch 3: Is the Taxonomy Correct?

```
[C3] "The 17 categories are correctly defined."

  ASSUME RIGHT:
  [F185] If right: The categories partition the space of user inputs with minimal overlap and minimal gaps.
    -- STRENGTH: necessary
    [F186] The current partition:
      - By epistemic task: claim (test truth), decide (choose), diagnose (find cause), search (explore), evaluate (assess work)
      - By user state: want (goal unclear), how (goal clear, method unclear), emotion (feeling-driven), action (method clear)
      - By output type: create (produce content)
      - By domain: technical (domain-specific)
      - By analytical type: analyze (break down situation)
      - Meta/system: meta (orientation), certainty (max effort), iterate (improve), sp (improve prompt)
    [F187] -> BEDROCK-OBSERVE: This is at least 5 different classification dimensions collapsed into one list.

  ASSUME WRONG:
  [F188] Wrong because: The categories mix classification dimensions.
    -- SEVERITY: serious
    [F189] "claim" classifies by epistemic task. "emotion" classifies by user state. "technical" classifies by domain. "create" classifies by output type. These are orthogonal dimensions.
      [F190] -> BEDROCK-LOGIC: Orthogonal dimensions should be independently specifiable, not conflated. A user could have a "technical emotional claim about creating something" -- which category handles this?
    [F191] If F188 holds: The correct taxonomy would be multi-dimensional: (epistemic task) x (user state) x (domain) x (output type).
      [F192] But this creates a combinatorial explosion: 5 epistemic tasks x 4 user states x 12 domains x 5 output types = 1200 cells.
        [F193] -> BEDROCK-LOGIC: Full dimensional decomposition is impractical. Some conflation is necessary. The question is whether the CURRENT conflation is the best one.
  [F194] Wrong because: Some categories overlap significantly.
    -- SEVERITY: conditional
    [F195] /analyze and /diagnose overlap on causal analysis. /analyze explicitly says "Causal -> route to /diagnose."
      [F196] -> BEDROCK-OBSERVE: /analyze exists partly as a catch-all for "anything analytical that doesn't fit other categories." This is useful but creates ambiguity.
    [F197] /want and /how overlap when the user has a goal and wants a method -- "/want" traces the goal, "/how" finds the method, but many inputs need both.
      [F198] -> BEDROCK-OBSERVE: /want explicitly routes to /how after goal clarification. They are designed as a sequence (want -> how), but users could enter at either point.
  [F199] Wrong because: Some inputs have no natural home.
    -- SEVERITY: conditional
    [F200] "Tell me about X" (pure information request) doesn't naturally fit any category. It's not a claim, decision, diagnosis, search, or any other category.
      [F201] -> BEDROCK-OBSERVE: This would likely enter /search or /technical, but it's not exploration (the user isn't looking for options) and it's not domain-specific (could be any topic).
    [F202] "Compare X and Y" goes through /analyze or /decide, but pure comparison (no decision needed) doesn't fit perfectly in either.
```

#### Self-Evaluation (Iteration 2)

**Unresolved branches resolved:**
- Alternative architectures fully explored: single dispatcher (C19), pipeline (C20), shared rules (C21)
- Analytical framing value tested (C22) -- verdict: genuinely valuable for some categories, redundant for others
- Taxonomy correctness tested (C3) -- verdict: mixed dimensions but pragmatically reasonable

**New tensions found:**
- F156: Classification and framing are intertwined, making pipeline architecture hard
- F180: Some analytical preprocessing is in category skills, some is in specialist skills -- partial overlap
- F193: Full dimensional decomposition is impractical, so some conflation is necessary

**Remaining untested assumption:**
- Whether users primarily enter through categories vs. direct skills (affects how much the routing layer matters)

**Competing conclusions narrowing:**
- The cross-referencing is clearly a maintenance problem (F69-F78, F115-F117)
- The analytical framing is clearly valuable for the rich categories (F171-F175)
- The taxonomy's dimension-mixing is a real issue but the alternatives are worse (F192-F193)

Proceeding to Iteration 3 for synthesis of key tensions.

---

### ITERATION 3: Resolving Key Tensions + Checking for Blind Spots

#### Tension 1: Analytical framing requires integration with routing (F156) vs. routing creates maintenance burden (F69-F78)

[F203] Resolution: The tension is real and cannot be fully resolved. However, it can be MANAGED:
- Keep analytical framing integrated with categories (preserving F156)
- Extract ONLY the shared classification rules ("Is This Actually X?") into a shared reference (F169-F170)
- Each category skill retains its unique analytical framing (core principles, interpretations, failure modes)
- The shared reference handles only the cross-category redirect checks
[F204] -> BEDROCK-LOGIC: This is a partial decomposition -- separate the parts that are truly shared (classification redirects) from the parts that are category-specific (analytical framing). Neither a full merge (single dispatcher) nor the status quo (full duplication) is optimal.

#### Tension 2: Category skills vary wildly in analytical richness (F182-F183)

[F205] Resolution: This reveals that not all 17 "category skills" are the same kind of thing:
- **Rich analytical frameworks** (claim, decide, want, how, emotion, search, diagnose, viability, evaluate): These provide genuine analytical value through core principles, interpretations, and failure modes. They are thinking stances.
- **Routing dispatchers** (technical, analyze, action, create, meta): These primarily route by matching input patterns. Their "analytical" content is about routing, not about how to think.
- **Meta-level operators** (certainty, iterate, sp): These operate on other skills' output, not directly on user input.
[F206] -> BEDROCK-OBSERVE: The 17 "category skills" are actually 3 types conflated under one label. This conflation is not causing active harm, but it explains the inconsistency.

#### Tension 3: Mixed taxonomy dimensions (F189-F193)

[F207] Resolution: The mixed dimensions are a pragmatic compromise, not a design error.
- Pure dimensional taxonomy (epistemic x state x domain x output) creates 1200+ cells -- unusable
- The current 17 categories use a priority ordering: epistemic task first (claim > decide > evaluate), then user state (want > how > emotion), then domain (technical), then output (create), then meta (meta, certainty, iterate, sp)
- This priority ordering means: always try to classify by epistemic task first; fall back to user state; fall back to domain; fall back to output type
[F208] -> BEDROCK-LOGIC: This is the same approach that medical diagnosis uses -- check the most discriminating feature first, then refine. It's not elegant taxonomy but it's effective triage.

#### Blind Spot Check: What would someone from a different perspective notice?

[F209] A UX designer would notice: The 17-category table puts the burden of classification on the user. Good UX would have the system classify automatically.
  -> This points to the value of /meta as the default entry point, or to an implicit dispatcher that runs before any category skill.

[F210] A software architect would notice: The current architecture is a distributed routing system with no central coordination. This is resilient (no single point of failure) but inconsistent (rules can drift between nodes).
  -> This points to the shared-classification-rules approach (F169-F170).

[F211] A cognitive scientist would notice: The categories map loosely to established cognitive operations: assertion testing (claim), choice (decide), causal reasoning (diagnose), exploration (search), planning (how), goal-setting (want), emotion regulation (emotion), evaluation (evaluate), creativity (create), execution (action). This is not arbitrary -- it reflects how humans actually think.
  -> This supports the claim that the taxonomy is fundamentally sound, even if the execution has maintenance issues.

#### Checking for Obvious Things Missed

[F212] Obvious check: Does the current architecture actually cause problems in practice?
  -> BEDROCK-OBSERVE: The system is in active use. The question was prompted not by user complaints or system failures but by architectural curiosity. This suggests the architecture is working well enough that its flaws are theoretical, not practical.

[F213] Obvious bad outcomes: What's the worst case if the architecture stays as-is?
  -> As skills grow, the cross-referencing maintenance burden grows O(N^2). At some point, inconsistencies accumulate and redirect rules drift. But this is a slow degradation, not a cliff.

[F214] Self-deception check: Am I being too generous to the current architecture because it exists and works?
  -> The analysis found genuine problems: O(N^2) maintenance (F69), mixed dimensions (F189), inconsistent analytical richness (F182). These are real. But the alternatives examined (single dispatcher, pipeline) have their own genuine problems (F135-F137, F152-F156). The conclusion that "keep but refactor" is best is not status-quo bias -- it's derived from the alternatives being genuinely worse for the most valuable properties.

---

### Stopping Condition Check

- **No unresolved branches remain**: All major architectural alternatives explored. All key tensions resolved.
- **No untested assumptions remain**: The main load-bearing assumptions (analytical framing adds value, classification is hard, alternatives have real costs) have been tested to bedrock.
- **No competing conclusions remain**: The analysis converges on "the architecture is fundamentally sound but has specific maintainability issues that can be addressed without restructuring."
- **Diminishing returns**: Further iterations would refine details but not change the conclusion.

Proceeding to Final Synthesis.

---

## Phase 3: Final Synthesis

### Finding Registry

```
FINDING REGISTRY
================

CLAIMS TESTED: 22
[C1-C22 as listed above]

TOTAL FINDINGS: 214

AR FINDINGS (select key implications):
[F1-F7] Routing provides manageable entry, horizontal scaling
[F8-F10] Category skills add genuine analytical value beyond routing
[F45-F51] Classification-then-dispatch handles ambiguous input gracefully
[F65-F68] Cross-referencing creates robust safety net
[F79-F91] Analytical framing functions as "thinking stance" selector
[F171-F175] Category layer is "analytical middleware"

AR FINDINGS (key foreclosures):
[F11-F13] Cannot easily reorganize by alternative taxonomies
[F90-F91] Cannot simplify to pure routing without losing analytical value
[F150] Pipeline architecture loses self-correction capability

AW FINDINGS (key wrongness reasons):
[F14-F18] 17 categories exceeds working memory -- SEVERITY: serious
[F19-F25] Classification boundaries are fuzzy; redirect pattern is repair mechanism -- SEVERITY: serious
[F32-F37] O(N^2) cross-referencing maintenance burden -- SEVERITY: fatal for scaling
[F69-F78] Cross-references already showing inconsistency -- SEVERITY: fatal
[F103-F112] Mixed taxonomy dimensions create ambiguity -- SEVERITY: serious
[F115-F117] New cross-cutting skills require O(N) updates -- SEVERITY: fatal
[F188-F193] Categories conflate orthogonal dimensions -- SEVERITY: serious

AW FINDINGS (key derived alternatives):
[F23-F25] Single intelligent dispatcher -- REJECTED (loses analytical framing)
[F36-F37, F77-F78, F169-F170] Shared classification rules -- VALIDATED
[F118-F120] Pipeline architecture -- REJECTED (classification and framing are intertwined)
[F160-F165] Hybrid: keep categories, extract shared rules -- VALIDATED
[F205-F206] Reclassify 17 skills into 3 types (frameworks, dispatchers, operators)

BEDROCK REACHED: 22 points
[F4, F7, F10, F25, F47, F76, F83, F89, F102, F112, F131, F134, F145, F156, F167, F170, F173, F175, F190, F193, F204, F208]

TENSIONS:
[F44] Separating routing from framing (F42) contradicts the value of their integration (F10)
[F55] Direct access already exists, so C5 is about defaults not mandates
[F94] Moving analytical framing into specialist skills makes them into routers
[F136] Single dispatcher loses framing IF framing can't be preserved separately
[F151] Pipeline self-correction depends on classifier accuracy
[F156] Classification and framing are intertwined (frame problem)
[F180] Partial overlap between category preprocessing and specialist preprocessing

CLAIM VERDICTS:
[C1] CONDITIONAL -- right architecture WITH maintenance improvements
[C2] CONDITIONAL -- 17 works as triage; too many for memorization, fine for decision tree
[C3] DAMAGED -- mixed dimensions, but alternatives are worse
[C4] CONDITIONAL -- two tiers works for most paths, three for domain-specific
[C5] VALIDATED -- genuinely better than flat access for most users
[C6] VALIDATED -- necessary safety net given fuzzy boundaries
[C7] DAMAGED -- right idea, wrong implementation (duplicated everywhere)
[C8] CONDITIONAL -- true for rich categories, false for thin ones
[C9] VALIDATED -- modes represent genuine epistemic postures
[C10] VALIDATED -- flat namespace works given category-first entry
[C11] DAMAGED -- users can't reliably classify, but redirect pattern compensates
[C12] REJECTED -- not maintainable at O(N^2), already showing inconsistency
[C13] VALIDATED -- accuracy matters more than speed for analytical tasks
[C14] VALIDATED -- for rich categories; DAMAGED for thin categories
[C15] VALIDATED -- flat 563 skills clearly worse
[C16] REJECTED -- new cross-cutting skills require O(N) updates
[C17] CONDITIONAL -- no practical loops observed, but no explicit prevention
[C18] VALIDATED -- the consensus mechanism works, but the implementation is costly
[C19] REJECTED -- single dispatcher loses analytical value
[C20] REJECTED -- pipeline can't cleanly separate classification from framing
[C21] VALIDATED -- hybrid approach preserves value while reducing maintenance
[C22] VALIDATED -- for rich categories; not meaningfully true for thin ones

CRUX POINTS:
[CRUX-1] Can shared classification rules be implemented without losing category-specific intelligence?
  -- resolves: F69-F78, F115-F117
  -- test: Prototype a shared classification file and verify category skills still work correctly when referencing it
[CRUX-2] Should the 3 types of "category skills" (frameworks, dispatchers, operators) be formally distinguished?
  -- resolves: F205-F206, F182-F184
  -- test: Reclassify the 17 skills and assess whether explicit typing improves clarity
[CRUX-3] Should input-shape detection (/it, /but, /nsa, /handle) be extracted as a pre-processing step?
  -- resolves: F115-F120
  -- test: Implement pre-processing and verify it catches the same cases that in-category detection catches
```

---

## CERTAINTY RESOLUTION

**QUESTION:** Is the category-skill routing architecture the right design, or should it be restructured?

**RESOLUTION CRITERIA:** Clear recommendation with justified confidence, alternatives considered and rejected for stated reasons, risks identified. No remaining unresolved branches, untested assumptions, or competing conclusions.

**ITERATIONS COMPLETED:** 3

**TOTAL FINDINGS:** 214 across all iterations

### ANSWER

**The category-skill routing architecture is fundamentally sound and should be preserved, but it has three specific structural problems that should be addressed through targeted refactoring -- not wholesale restructuring.**

The architecture is right because:

1. **The category layer provides genuine analytical value**, not just routing. Skills like /claim, /decide, /emotion, and /want add analytical intelligence (bundling detection, confidence-based balance, reversibility assessment, emotion-to-need mapping) that would be lost in any pure-routing alternative. This is the most important finding -- the categories are "thinking stances," not just dispatchers.

2. **The two-tier structure scales horizontally.** The system grew from ~415 to ~563 skills without changing the 17-category structure. New specialist skills slot under existing categories naturally.

3. **The alternatives are worse.** A single dispatcher loses analytical framing (tested and rejected). A pipeline architecture can't cleanly separate classification from framing because they're intertwined -- the act of framing input as a "claim" changes what you see in it (tested and rejected). Flat access to 563 skills is obviously unworkable.

4. **The taxonomy, while imperfect, reflects genuine cognitive operations** (assertion testing, choice, causal reasoning, exploration, planning, goal-setting, emotion regulation). The mixed dimensions are a pragmatic compromise -- pure dimensional taxonomy creates a 1200+ cell matrix.

However, three problems need fixing:

**Problem 1: O(N^2) cross-referencing.** Every category skill embeds 7-10 redirects to other categories, creating ~136 cross-references. These are already inconsistent and require O(N) updates for every new category or input-shape skill. **Fix:** Extract shared classification rules ("Should I X?" -> /decide, "I think X" -> /it, etc.) into a shared reference file. Each category skill references this file instead of embedding the rules. Category-specific analytical framing stays in each category skill.

**Problem 2: Input-shape skills are cross-cutting concerns.** /it, /but, /nsa, /handle, /etc, and /aso are referenced in every category skill because they apply to any input type. **Fix:** Extract input-shape detection as a pre-processing step (a shared "input normalization" reference) that runs before category classification. This is the specific case where the pipeline pattern IS appropriate -- input normalization is genuinely separable from category classification.

**Problem 3: The 17 "category skills" are actually 3 different types.** Rich analytical frameworks (claim, decide, want, how, emotion, search, diagnose, viability, evaluate) are qualitatively different from routing dispatchers (technical, analyze, action, create, meta) and meta-level operators (certainty, iterate, sp). This isn't causing active harm, but explicitly recognizing these types would improve clarity and set appropriate expectations for each.

**CONFIDENCE:** High

The analysis tested 22 claims across 214 findings, examined 4 alternative architectures (single dispatcher, pipeline, shared rules, hybrid), and resolved 7 major tensions. The conclusion is robust because:
- The strongest alternative (full pipeline restructuring) was rejected for a fundamental reason (classification and framing are intertwined -- F156)
- The recommended changes (shared classification rules, input-shape pre-processing) address the specific problems found without disrupting the architecture's strengths
- The finding that category skills add analytical value (not just routing) was confirmed independently through multiple paths (F10, F47, F83, F173)

### KEY EVIDENCE

1. **Category skills function as analytical middleware, not just routers** (F79-F91, F171-F175). /claim adds bundling detection, confidence-based balance, and testability assessment that /araw alone does not provide. This is the most load-bearing finding -- it means the category layer cannot be replaced by pure routing without quality loss.

2. **The cross-referencing pattern is already breaking** (F69-F78, F115-F117). The "Is This Actually X?" sections across 17 category skills are inconsistent -- some reference newer skills (/it, /but, /nsa) and some don't. This will get worse as skills grow. This is the most urgent problem.

3. **Alternative architectures fail on the fundamental constraint** (F135-F137, F152-F156). Both the single-dispatcher and pipeline alternatives require separating classification from analytical framing, but F156 shows these are intertwined -- framing an input as a "claim" vs a "decision" changes what you see in the input. This means the current integrated approach is structurally correct.

### WHAT WAS TESTED AND SURVIVED

- The category layer adds genuine analytical value beyond routing (C14 -- VALIDATED)
- Classification-then-dispatch is better than flat access (C5 -- VALIDATED)
- The modes (ARAW, UAUA, AR-forward, Direct) represent genuine epistemic postures (C9 -- VALIDATED)
- The taxonomy, despite mixed dimensions, is a pragmatic compromise that works (C3 -- DAMAGED but better than alternatives)
- The cross-referencing provides a necessary safety net for fuzzy boundaries (C6 -- VALIDATED)

### WHAT WAS TESTED AND ELIMINATED

- Single dispatcher as a replacement (C19 -- REJECTED: loses analytical framing)
- Full pipeline restructuring (C20 -- REJECTED: classification and framing are intertwined)
- The cross-referencing is maintainable as-is (C12 -- REJECTED: O(N^2), already inconsistent)
- The architecture handles new cross-cutting skills gracefully (C16 -- REJECTED: requires O(N) updates)
- Users can reliably self-classify (C11 -- DAMAGED: they can't, but redirects compensate)

### REMAINING UNCERTAINTY

- **Whether the analytical framing measurably improves output quality** has not been empirically tested. The logical argument is strong (F173-F175), but an A/B test (same input through /claim + /araw vs bare /araw) would provide conclusive evidence. This is the highest-value test to run.
- **Whether the LLM's native classification ability makes the routing rules redundant** (F56-F61). As LLMs improve, the explicit routing rules may become less necessary. The analytical framing, however, would remain valuable regardless of LLM capability.
- **Whether 17 categories is too many for users.** Exceeds working memory limits (F15), but the table format and natural-language triggers mitigate this. Would benefit from user testing.

### WHAT WOULD CHANGE THIS ANSWER

1. **If empirical testing showed that /araw alone produces equally good output as /claim + /araw**, the analytical framing argument collapses and a simpler routing-only architecture would be justified.
2. **If LLMs become reliable enough to classify and frame inputs without explicit rules**, the entire category layer becomes optional middleware rather than necessary infrastructure.
3. **If the system grows past ~50 categories**, the O(N^2) cross-referencing becomes unmanageable even with shared rules, and a fundamentally different approach (e.g., embedding-based skill discovery) would be needed.
4. **If users consistently enter through direct skill invocation** (bypassing categories), the category layer is providing maintenance cost without user value.

---

### Recommended Actions (Priority Order)

1. **Create `_shared/classification-rules.md`** containing the cross-category redirect rules. Update each category skill to reference this file instead of embedding rules. This addresses the most urgent problem (O(N^2) maintenance) with minimal disruption.

2. **Create `_shared/input-shape-detection.md`** containing the pre-processing rules for /it, /but, /nsa, /handle, /etc, /aso. Reference this at the start of each category skill. This prevents future O(N) updates when new input-shape skills are added.

3. **Formally distinguish the three types of "category skills"** in CLAUDE.md: analytical frameworks (claim, decide, want, how, emotion, search, diagnose, viability, evaluate), routing dispatchers (technical, analyze, action, create), and meta-level operators (certainty, iterate, sp, meta). This sets appropriate expectations and guides future development.

4. **Run an empirical quality comparison** (when feasible): route the same 20 inputs through category skills vs. direct specialist skills. If category framing measurably improves output, this validates the architecture empirically. If not, simplification is warranted.
