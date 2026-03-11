# /evaluate Assess the quality of the /araw skill as a thinking procedure
**Date:** 2026-03-09
**Skill:** /evaluate (Assess Something)

---

## Routing

**What's being evaluated:** The `/araw` skill (Assume Right / Assume Wrong Search), a structured thinking procedure defined in `SKILL.md`.

**Evaluation type:** Quality check — "Is this good as a thinking procedure?"

**Is this actually evaluation?** Yes. Not a claim to test, not a decision, not a diagnosis. The user wants an assessment of the quality of a procedure.

**Routed to:** Procedure Validation (`/pv`) adapted for quality assessment, with criteria established below.

**Standard:** No external standard stated. Deriving criteria from the domain: what makes a thinking procedure good?

**Scope:** Whole procedure — assessing the full ARAW skill file.

**Self-evaluation?** No — evaluating the user's work. Balanced assessment, but the evaluate skill's principle 3 applies: "Evaluation is not confirmation. The purpose is to find weaknesses, gaps, and errors."

---

## Criteria Established

A thinking procedure is good to the extent that it:

1. **Achieves its stated goal** — Does it actually produce what it claims to produce?
2. **Is executable** — Can a practitioner (in this case, an LLM) reliably follow it?
3. **Has clear structure** — Are steps, phases, and dependencies well-ordered?
4. **Handles failure modes** — Does it anticipate and mitigate common ways it could go wrong?
5. **Scales appropriately** — Does it work for simple inputs and complex inputs?
6. **Is internally consistent** — Do its parts align with each other?
7. **Produces non-obvious output** — Does it generate results the user wouldn't get without it?
8. **Constrains bad behavior** — Does it prevent the executor from taking shortcuts or producing garbage?
9. **Has appropriate scope** — Is it neither too narrow nor too broad for its purpose?
10. **Is learnable** — Can someone understand what it does and why from reading it?

---

## Procedure Validation

### PROCEDURE TO VALIDATE: /araw (Assume Right / Assume Wrong Search)

**GOAL:** For any claim, decision, or position, systematically explore what follows if it's true (AR) and what breaks if it's false (AW), recurse to bedrock, compile all findings, and derive synthesis only from the compiled registry.

**STEPS (as defined in the skill):**

0. Meta-ARAW (Strategy Selection) — optional at 1-2x, required at 4x+
1. Identify and Unbundle Claims — parse input into numbered claims
2. Phase 1: Exploration — ARAW each claim, build numbered finding trees
3. Phase 2: Finding Registry — compile all findings into categorized registry
4. Phase 3: Synthesis — derive conclusions only from the registry

**Plus cross-cutting concerns:**
- Corruption Pre-Inoculation
- Core Principles (10)
- Anti-Failure Checks (9)
- Pre-Completion Checklist (18 items)
- Quick Mode (ARAW-Lite)
- Depth Floors table

---

### Completeness Check

**To achieve the goal (rigorous bidirectional claim analysis), we need:**

| Sub-goal | Covered by | Status |
|----------|-----------|--------|
| Parse input into testable claims | Step 1 | Covered |
| Handle non-claim inputs (decisions, requests) | Step 0 + Claim Evaluability section | Covered |
| Explore implications if true | Phase 1 AR | Covered |
| Explore reasons if false | Phase 1 AW | Covered |
| Find alternatives when wrong | Multi-Valued AW, AW by Claim Type | Covered |
| Recurse to solid ground | Bedrock labels (4 types) | Covered |
| Track all findings systematically | F-numbering, Registry | Covered |
| Prevent confirmation bias | Corruption Pre-Inoculation, Principles 3-4, Anti-Failure Checks | Covered (heavily) |
| Produce actionable output | Synthesis: DO_FIRST ACTIONS, CRUX points | Covered |
| Scale to different complexity levels | Depth Floors table (1x-32x) | Covered |
| Handle edge cases and failures | Anti-Failure Checks, "When ARAW Fails" | Covered |
| Quick mode for simple cases | ARAW-Lite section | Covered |
| Save/persist output | Saving Output section | Covered (delegates to /sf) |

**GAPS FOUND:**
- **No explicit "how to prioritize which claims to ARAW first" guidance beyond VOI.** Step 1 says "ARAW high-VOI claims first" but doesn't say what to do when you have 12 high-VOI claims and only depth for 5. Minor — a practitioner can figure this out, but a novice executor might try to ARAW everything equally and run out of depth budget.
- **No explicit termination criterion for Phase 1.** The skill says "After ALL exploration is complete" but doesn't define when exploration is complete beyond "reach bedrock." In practice, tree depth can expand indefinitely. The depth floors provide a minimum but not a maximum.
- **No guidance on time/token budgeting.** The depth floors specify minimums for claims, findings, and tree levels, but don't address the practical constraint that an LLM has a finite context window. At 32x depth (35 claims, 130 findings), this is a very large output.

**GAP CHECK: Mostly covered, 3 minor gaps found.**

---

### Dependency Validation

| Step | Dependencies | Earlier Steps | Valid? |
|------|-------------|---------------|--------|
| Step 0 (Meta-ARAW) | Input | N/A | Valid |
| Step 1 (Unbundle Claims) | Input, optionally Step 0 output | Step 0 | Valid |
| Phase 1 (Exploration) | Claims from Step 1 | Step 1 | Valid |
| Phase 2 (Registry) | All findings from Phase 1 | Phase 1 | Valid |
| Phase 3 (Synthesis) | Registry from Phase 2 | Phase 2 | Valid |

**Strict phase separation is explicitly enforced:** "Phase 1 explores (no conclusions). Phase 2 compiles (no new findings). Phase 3 synthesizes (only from the registry)."

**DEPENDENCY CHECK: Valid. Clean linear dependency chain with explicit phase gates.**

---

### Feasibility Check

| Component | Feasible? | Notes |
|-----------|-----------|-------|
| Step 0: Meta-ARAW | Yes | Standard analytical reasoning |
| Step 1: Claim unbundling | Yes | Well-specified with examples |
| Phase 1: ARAW trees | Yes, with caveats | Tree format is clear; reaching BEDROCK in every branch is aspirational — many real-world claims don't reduce to testable/observable/logical bedrock without domain-specific knowledge |
| Phase 2: Registry | Yes | Mechanical compilation task |
| Phase 3: Synthesis | Yes | Template-driven |
| Depth floors at 16x-32x | Marginal | 85-130 findings with full tree structures may exceed practical output limits for a single LLM response |
| Pre-Completion Checklist (18 items) | Marginal | Self-verification of 18 items after producing a large output is cognitively expensive; an LLM may shortcut this |
| Corruption Pre-Inoculation | Partially | Detection of >80% validation or depth asymmetry requires the executor to audit its own output mid-stream, which is harder than stated |

**FEASIBILITY ISSUES:**
1. **Bedrock requirement may be unreachable for some claims.** The skill defines 4 bedrock types and says "probably true is NOT bedrock." For many real-world claims (strategic, belief-based, values-based), all branches may terminate at "conditional" or "probable" without ever reaching something empirically testable or logically necessary. The skill acknowledges this implicitly with the UNCERTAIN verdict but the language ("every branch reaches bedrock" in the pre-completion checklist) creates an impossible standard for many inputs.
2. **Self-auditing during execution is unreliable.** The Corruption Pre-Inoculation section assumes the executor can detect its own biases (>80% agreement, depth asymmetry, flattery) and correct in real-time. This is a known weakness of LLMs — they are better at following procedures than at self-monitoring.

**FEASIBILITY CHECK: Feasible with caveats. 2 issues at the margins.**

---

### Output Verification

**Goal:** Rigorous bidirectional analysis that produces: understanding of what's true, what's false, what's uncertain, and what to do next.

**Trace outputs:**
- Step 1 produces: Numbered claim list with types and VOI ratings
- Phase 1 produces: Numbered finding trees with AR/AW branches, bedrock labels, classification
- Phase 2 produces: Complete registry with verdicts (VALIDATED/REJECTED/DAMAGED/CONDITIONAL/UNCERTAIN), CRUX points, tensions, totals
- Phase 3 produces: Pattern identification, key tensions, weakest links, derived alternatives, testable predictions, DO_FIRST actions, unresolved items

**Does final output = goal?** Yes. The synthesis section directly addresses what's true (validated claims), what's false (rejected claims), what's uncertain, and what to do next (DO_FIRST actions, CRUX points).

**OUTPUT CHECK: Goal achieved. Output structure maps cleanly to stated purpose.**

---

### Consistency Check

| Component A | Component B | Relationship | Issue? |
|-------------|-------------|-------------|--------|
| Core Principle 1 ("Derivation, not enumeration") | Depth Floors (minimum counts) | Tension | Minor |
| Core Principle 8 ("expect 20-40% rejected") | Pre-Completion Checklist ("if >80% validated, test harder") | Aligned | None |
| ARAW-Lite (quick mode) | Depth Floors table | Independent | None |
| "No early termination" (Principle 2) | "Compress where insight is not dense" (Depth Floors note) | Tension | Minor |
| Phase separation (Principle 10) | Corruption Pre-Inoculation (requires mid-stream auditing) | Tension | Moderate |

**TENSIONS FOUND:**
1. **Principle 1 vs. Depth Floors.** "Let structure emerge from exploration" suggests organic depth, but the floors impose minimum counts (e.g., 35 claims at 32x). This creates a pull toward enumeration to hit targets, which contradicts Principle 1. The skill partially addresses this with "these are floors, go deeper where insight is dense, compress where it's not" — but in practice, a minimum of 35 claims on a single topic will often require forced enumeration.
2. **"No early termination" vs. "Compress where not dense."** Principle 2 says meet the depth floors; the depth floors note says compress. These are reconcilable in theory (meet floors but don't pad) but create ambiguity in practice.
3. **Phase separation vs. real-time bias correction.** Strict phase separation says "no conclusions in Phase 1." But the Corruption Pre-Inoculation requires detecting whether you're confirming too much during exploration, which requires a provisional conclusion about the direction of your findings. This is a genuine procedural tension — to self-correct during exploration, you must assess your exploration, which introduces judgment into a phase that's supposed to be judgment-free.

**CONSISTENCY CHECK: Mostly consistent. 3 tensions found, 1 moderate.**

---

## Quality Assessment Against Criteria

### 1. Achieves its stated goal
**Rating: Strong**

ARAW's goal is to produce rigorous bidirectional analysis. The procedure, when followed, does produce systematic exploration of both "if right" and "if wrong" for each claim. The numbered finding system and registry create a comprehensive record. The phase separation prevents premature conclusions. The synthesis template ensures actionable output.

### 2. Is executable
**Rating: Strong with caveats**

The procedure is detailed enough to follow step-by-step. Templates are provided for every phase. Classification labels are defined. However, the 18-item pre-completion checklist is ambitious for self-verification, and the bedrock requirement may be unreachable for some claim types.

### 3. Has clear structure
**Rating: Excellent**

This is ARAW's greatest strength. The three-phase architecture (Explore -> Compile -> Synthesize) with strict separation is elegant and well-motivated. The numbering system (C-numbers for claims, F-numbers for findings) creates traceability. The registry serves as a single source of truth. The synthesis template prevents freestyle conclusions.

### 4. Handles failure modes
**Rating: Excellent**

Nine explicit anti-failure checks, five corruption pre-inoculation rules, and a "When ARAW Fails" section. The failure modes are specific and well-observed: "soft AW," "validation parade," "narrative tree," "cheerleading AR," "conventional contrarian." These read as lessons learned from actual failure patterns, not theoretical concerns.

### 5. Scales appropriately
**Rating: Strong**

Six depth levels (1x through 32x) with explicit floors. ARAW-Lite for quick decisions. Meta-ARAW (Step 0) scales with depth requirement. The scaling is more convincing at lower depths (1x-4x) and becomes increasingly aspirational at higher depths (16x-32x) where the output volume may exceed practical limits.

### 6. Is internally consistent
**Rating: Good**

Mostly consistent with 3 tensions identified above. The most significant is the conflict between strict phase separation and real-time bias detection. None of the tensions are fatal — they're the kind of tensions that arise in any sufficiently detailed procedure.

### 7. Produces non-obvious output
**Rating: Strong**

The key insight of ARAW — that every AR finding generates sub-claims needing AW, and every AW finding generates alternatives needing AR — creates a recursive exploration that goes well beyond what a user would produce by "thinking about it." The foreclosure requirement ("every yes is also a no"), the unconventional alternative requirement, and the multi-valued AW approach ("wrong has multiple values") all push toward non-obvious findings. The 20-40% rejection rate expectation directly counters the tendency to confirm.

### 8. Constrains bad behavior
**Rating: Excellent**

This is ARAW's second greatest strength. The skill is deeply paranoid about the ways analysis can fail: confirmation bias, soft adversarial testing, premature conclusions, opinion-as-bedrock, cheerleading, conventional contrarianism. The Corruption Pre-Inoculation section specifically addresses the sycophancy problem (user validation degrading output). The pre-completion checklist includes specific anti-bias checks. Multiple redundant guardrails exist for the same failure modes. This feels like a procedure written by someone who has seen analysis go wrong many times.

### 9. Has appropriate scope
**Rating: Good**

ARAW handles claims, decisions, and positions — a broad scope for a single skill. The Interpretations section at the top helps disambiguate. The scope is arguably slightly too broad: testing a factual claim ("the API is slow") and stress-testing a life decision ("should I quit my job") are different enough that they might benefit from different procedures, but ARAW's flexibility (through AW by Claim Type and the depth scaling) mostly handles this.

### 10. Is learnable
**Rating: Good with caveats**

The skill is 424 lines long. It contains 10 core principles, 9 anti-failure checks, 18 pre-completion items, 4 bedrock types, 5 classification labels, 6 depth levels, and 3 interpretations. For an LLM executor that reads the whole file before each execution, this is fine. For a human trying to learn the procedure, it's dense. The Core Principles section is well-written and could stand alone as a summary. The templates make execution concrete. But the sheer volume of guidance creates a "where do I start?" problem for newcomers.

---

## Findings Summary

### What's Strong

1. **Architecture is elegant.** The three-phase design (Explore -> Compile -> Synthesize) with strict separation is the best structural decision in the skill. It prevents the most common failure mode of analytical thinking: reaching conclusions before finishing exploration.

2. **Anti-corruption is thorough.** No other thinking procedure I'm aware of explicitly addresses the sycophancy problem (user validation degrading analysis quality). The corruption pre-inoculation section is genuinely novel and addresses a real problem with LLM-assisted thinking.

3. **Failure mode coverage is excellent.** The nine anti-failure checks are specific, actionable, and clearly derived from observed failure patterns. "Soft AW — that's AR wearing a hat" is a precise description of a real failure mode.

4. **Traceability is well-designed.** C-numbers, F-numbers, bedrock labels, and the registry create an auditable chain from input to conclusion. The requirement that synthesis only references registry items prevents freestyle conclusions.

5. **The recursive insight is powerful.** "Every AR produces sub-claims that need AW. Every AW produces alternatives that need AR" is the core engine. This is genuinely more powerful than linear pro/con analysis because it discovers second- and third-order implications.

6. **Rejection as expected outcome.** Principle 8 ("expect 20-40% rejected") directly counters confirmation bias by setting an expectation that some claims should fail. This normalization of rejection is psychologically important.

### What's Weak

1. **Bedrock is aspirational for many claim types.** The four bedrock types (TEST, LOGIC, OBSERVE, TENSION) work well for factual and technical claims. For strategic, ethical, aesthetic, or values-based claims, reaching bedrock may be impossible — these claims bottom out at "this is what I value" or "reasonable people disagree," which the skill doesn't acknowledge as valid stopping points. This means the pre-completion checklist item "every branch reaches bedrock" will routinely fail for common use cases.

2. **Self-monitoring during execution is the weakest mechanism.** The Corruption Pre-Inoculation assumes the executor can detect its own biases mid-stream (>80% agreement, depth asymmetry). This is the least reliable part of the procedure because it requires meta-cognition that LLMs are not reliably good at. A better mechanism would be structural: e.g., "always write AW before AR" or "write AW for your strongest claim first."

3. **No explicit prioritization beyond VOI.** When Step 1 produces 15 claims, the only guidance is "ARAW high-VOI claims first." There's no guidance on: how many claims to fully ARAW vs. briefly check, when to stop adding claims, or how to handle the tradeoff between breadth (more claims) and depth (deeper trees per claim).

4. **High-depth modes are underspecified.** At 16x-32x, the procedure requires 85-130 findings. There's no guidance on managing this volume: how to keep track, when to break into sub-sessions, how to handle the cognitive (or context-window) load. The depth floors feel extrapolated from lower depths rather than tested at higher depths.

5. **The phase separation, while structurally sound, creates a tension with the skill's own bias-detection requirements.** You can't simultaneously "not conclude" (Phase 1) and "check whether you're confirming too much" (Corruption Pre-Inoculation). A resolution would be to add an explicit "Phase 1.5: Bias audit" step between exploration and registry.

### What's Missing

1. **No worked example at full depth.** The skill is 424 lines of procedure with zero complete examples. ARAW-Lite has a template but no example. A single worked example at 2x depth would dramatically improve executability and learnability.

2. **No "bedrock for non-empirical claims" guidance.** A large portion of real-world ARAW inputs are strategic, relational, or values-based. The skill needs either: additional bedrock types for these domains, or explicit guidance on when "this is a values claim — bedrock is the value itself" is an acceptable stopping point.

3. **No explicit guidance on when NOT to use ARAW.** The Interpretations section says what ARAW handles, but not what it shouldn't be used for. Some inputs (purely creative tasks, simple factual lookups, emotional processing) would be poorly served by ARAW, and the user/router should know this.

---

## Verdict

**Overall quality: High. This is a well-designed thinking procedure.**

**Confidence: 0.85** — I have high confidence in the structural assessment. Lower confidence in the feasibility concerns at high depth levels (I haven't observed 16x-32x ARAW executions to verify whether they work in practice).

**Rating by criterion:**

| Criterion | Rating |
|-----------|--------|
| Achieves stated goal | Strong |
| Is executable | Strong (caveats) |
| Clear structure | Excellent |
| Handles failure modes | Excellent |
| Scales appropriately | Strong |
| Internal consistency | Good |
| Non-obvious output | Strong |
| Constrains bad behavior | Excellent |
| Appropriate scope | Good |
| Learnable | Good (caveats) |

**Overall: 8/10 as a thinking procedure.**

The three areas rated "Excellent" (structure, failure modes, constraining bad behavior) represent the skill's signature strengths and are genuinely impressive. The weaknesses identified (bedrock for non-empirical claims, self-monitoring reliability, high-depth underspecification) are real but addressable. The absence of a worked example is the single most impactful gap — adding one would improve executability significantly.

---

## Specific Improvements Recommended

1. **Add a worked example at 2x depth.** Pick a concrete claim (e.g., "remote work is better for productivity"), run the full procedure, show the output. This would add ~150 lines but dramatically clarify what good execution looks like.

2. **Add bedrock types for non-empirical claims.** Candidates: `BEDROCK-VALUE: [irreducible value judgment]`, `BEDROCK-CONVENTION: [social/cultural convention]`, `BEDROCK-PREFERENCE: [stated preference with no deeper justification]`. This would make the bedrock requirement achievable for the full range of inputs ARAW handles.

3. **Add a structural bias-correction mechanism.** Instead of relying on self-monitoring, add a structural rule: "For the first claim you ARAW, write the AW branch first." This forces adversarial thinking before confirmation sets in.

4. **Add a "Phase 1.5: Exploration Audit" step.** Between Phase 1 and Phase 2, pause to check: Are AR and AW branches at similar depth? Are >80% of preliminary directions positive? This resolves the tension between phase separation and bias detection.

5. **Add claim triage guidance.** After Step 1 produces claims, add explicit guidance: "If you have more than [depth-level] claims, select the top N by VOI and briefly note the rest as DEFERRED. Deferred claims get one-line AR/AW, not full trees."

6. **Add a "not for" section.** Explicitly state what ARAW is not good for: purely creative tasks, simple factual lookups, emotional processing, tasks where speed matters more than rigor.

7. **Cap or segment high-depth modes.** For 16x-32x, add guidance: "Break into multiple ARAW sessions by claim cluster. Each session handles 5-8 claims. Cross-reference between sessions."

---

## Follow-Up Routing

After this evaluation, the user may want:
- **"Fix these issues"** -> `/how` or `/action` to implement improvements
- **"Iterate on the ARAW skill"** -> `/iterate` with this evaluation as input
- **"Improve the skill"** -> `/imps` (improve skill) targeting the specific weaknesses identified
- **"Test one of these claims"** -> `/araw` on any specific finding from this evaluation
