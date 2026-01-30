# reasoningtool

207 thinking skills for Claude Code. Each skill is a structured prompt that guides you through a specific type of thinking, decision, or analysis.

## Installation

### Option 1: Run from this directory

```bash
git clone https://github.com/benjam3n/reasoningtool.git
cd reasoningtool/claude-code-plugin
claude
```

Claude reads the `CLAUDE.md` file and all skills become available.

### Option 2: Copy into your project

```bash
cp -r path/to/reasoningtool/claude-code-plugin/skills your-project/
cp path/to/reasoningtool/claude-code-plugin/CLAUDE.md your-project/
cd your-project
claude
```

## Usage

In a Claude Code session, type `/skillname` followed by your input:

```
/space_enumeration what are all the ways I could approach this product launch
/assumption_extraction we need to hire 3 more engineers by Q2
/comparison React vs Svelte for this project
/root_cause_analysis our deploy pipeline keeps failing
/decision_procedure should I take this job offer
```

## Skills by tier

Skills are ranked by how much structured thinking they add — how likely they are to surface something you wouldn't have found on your own.

Some of these skills are **universal** — their applicability is entailed by the problem itself. If you have a complex problem, decomposition applies; that follows from what "complex" means. If you have a claim, testing it against its negation applies; that follows from what "claim" means. You don't need to check whether these skills are relevant. They are relevant whenever their trigger condition exists, and the trigger condition is defined by the skill.

Other skills are **heuristics** — they work well in specific contexts, but whether they apply to *your* context requires judgment. SCAMPER is a useful ideation framework, but whether it helps depends on what you're ideating about. SWOT analysis surfaces strategic factors, but whether those are the right factors depends on your situation.

The tiers below loosely reflect this. Tier 1 skills tend to be universal. Tier 4 skills tend to be context-dependent. The boundary isn't always clean — some skills are universal in principle but heuristic in execution — but the distinction tells you which skills to trust on contact and which to validate before relying on.

### Tier 1: Start here

These are the most generally useful skills. They work on almost any problem and consistently produce non-obvious results.

| Skill | What it does |
|-------|-------------|
| `space_enumeration` | Systematically lists all options in a problem space so nothing gets missed |
| `assumption_extraction` | Surfaces the hidden assumptions in any claim, plan, or argument |
| `comparison` | Structured comparison of options with explicit criteria and trade-offs |
| `hypothesis_testing` | Tests claims by examining what would be true if right vs. wrong |
| `decision_procedure` | Builds a step-by-step flowchart anyone can follow for a recurring decision |
| `decomposition` | Breaks complex problems into smaller, solvable parts |
| `root_cause_analysis` | Finds the actual cause of a problem, not just symptoms |
| `dimension_discovery` | Identifies all the dimensions along which something can vary |
| `mece_validation` | Checks that a breakdown is mutually exclusive and collectively exhaustive |
| `insight_synthesis` | Combines findings from multiple analyses into coherent conclusions |
| `cost_benefit_analysis` | Structured evaluation of costs vs. benefits with explicit trade-offs |
| `goal_understanding` | Clarifies what someone actually wants vs. what they said they want |

### Tier 2: Deep reasoning

These go deeper on specific types of thinking. Use them when you need thoroughness on a particular kind of problem.

| Skill | What it does |
|-------|-------------|
| `procedure_validation` | Checks whether a procedure actually works by testing each step |
| `assumption_inversion` | Flips assumptions to discover what happens if the opposite is true |
| `topological_ordering` | Finds the correct order to do things when tasks depend on each other |
| `cross_domain_analogy` | Applies solutions from one field to problems in another |
| `morphological_analysis` | Generates combinations by varying parameters across dimensions |
| `systems_analysis` | Maps how parts of a system interact and where leverage points are |
| `backward_reasoning` | Works backward from the goal to figure out what steps are needed |
| `pre_mortem` | Imagines the project failed and asks why, before it actually starts |
| `failure_anticipation` | Identifies likely failure modes before they happen |
| `possibility_analysis` | Explores what's possible, not just what's likely |
| `inference_space_search` | Searches the space of valid inferences from given premises |
| `recursive_causal_interrogation` | Keeps asking "why" until you reach the actual root |
| `limitation_analysis` | Identifies the real constraints and which ones can be changed |
| `verification_before_output` | Checks every claim for evidence before presenting it |
| `convergent_validation` | Uses multiple independent checks to validate a conclusion |

### Tier 3: Specialized tools

These solve specific types of problems well. They're less general but very effective in their domain.

**Research & Analysis**
`literature_review` · `qualitative_research` · `data_collection` · `statistical_analysis` · `experimental_design` · `field_analysis` · `competitive_analysis` · `market_research` · `source_credibility` · `source_prioritization` · `economic_research` · `policy_research`

**Writing & Communication**
`write` · `qo` · `persuasive_writing` · `storytelling` · `public_speaking` · `presentation_design` · `content_strategy` · `outreach_communication` · `feedback_delivery` · `active_listening`

**Planning & Projects**
`project_initiation` · `project_scoping` · `project_closure` · `dependency_extraction` · `progress_tracking` · `risk_assessment` · `deployment` · `retrospective` · `stakeholder_management`

**Business**
`customer_discovery` · `marketing_funnel` · `positioning` · `competitive_analysis` · `negotiation` · `client_retention` · `financial_modeling` · `budget_management` · `investment_strategy` · `roi_analysis`

**Software**
`code_review` · `debugging` · `refactoring` · `architecture_design` · `architecture_patterns` · `api_design` · `testing_strategy` · `security_practices`

**Career & Learning**
`career_path_planning` · `interview_preparation` · `resume_optimization` · `salary_negotiation` · `skill_acquisition` · `deliberate_practice` · `spaced_repetition` · `active_recall` · `learning_system`

**Decision Making**
`decision_trees` · `selection` · `criteria_weighting` · `pairwise_comparison` · `expected_value` · `multi_criteria_decision` · `reversibility_analysis` · `better_option_check`

### Tier 4: Everything else

The remaining skills cover specific use cases: `procedure_engine` · `procedure_extraction` · `procedure_discovery` · `finder` · `guess_generation` · `question_about_guesses` · `domain_template` · `template_maintenance` · `template_registry` · `taxonomy_maintenance` · `goal_decomposition` · `goal_refinement` · `goal_reframing` · `goal_journey_system` · `goal_structure_reconstruction` · `value_elicitation` · `value_conflict_decomposition` · `preference_elicitation` · `universal_goal_analysis` · `space_discovery` · `strategy_discovery` · `leverage_point_discovery` · `novelty_space_search` · `future_space_search` · `model_space_search` · `plan_space_search` · `analogy_search` · `binary_elimination_search` · `checklist_search` · `swot_analysis` · `scenario_planning` · `conflict_resolution` · `group_decision_making` · `human_delegation` · `networking` · `freelancing` · `growth_experiments` · `viral_mechanics` · `social_media_strategy` · `seo_basics` · `grant_writing` · `fundraising_advocacy` · `fundraising_financial` · `email_acquisition` · `phone_acquisition` · `outreach_campaigns` · `advocacy_infrastructure_setup` · `income_stream_development` · `cash_flow_management` · `budgeting` · `event_driven_automation` · `automated_extraction_pipeline` · `adaptive_extraction_pipeline` · `journey_extraction` · `journey_matching` · `cross_domain_report` · `cross_project_pattern_detection` · `session_review` · `weekly_review` · `after_action_review` · `self_audit_detector_sweep` · `self_audit_two_run_divergence_audit` · `self_audit_apply_analysis_protocol_clarity_and_validity` · `self_audit_apply_evidence_standard_application` · `self_audit_gate_schema_consistency_audit` · and more

Browse `claude-code-plugin/skills/` for the complete list.

## When to Use Each Analytical Skill

These are the core analytical tools. Each one structures your thinking differently depending on what you already know.

### Choosing by What You Know

| You know... | Use | Command |
|-------------|-----|---------|
| Nothing — not even what the options are | `/uaua` | Full space mapping + rigorous testing |
| You want a quick map of possibilities you haven't considered | `/u` | Breadth-first exploration |
| You have a specific claim but don't know if it's right or wrong | `/araw` | Test both sides with equal rigor |
| You believe something is right and want to know what it commits you to | `/ar` | Find implications, foreclosures, costs |
| You suspect something is wrong and want to find exactly why | `/aw` | Find failure reasons, derive alternatives |

### Detailed Guide

**`/u` — Universalize**
Use when you want to see what you're missing. U maps the space of possibilities — assumptions you didn't know you were making, alternatives you didn't know existed, dimensions you weren't thinking about. It's fast and wide. It does NOT evaluate — it just shows you what's there.

- "What am I not considering?"
- "What are my options?"
- "What assumptions am I making?"
- "Show me the space before I commit"

**`/ar` — Assume Right**
Use when you have a claim you believe is right and you want to know what follows. AR traces implications: if this is right, what must also be true? What does it commit you to? What does it foreclose? This is how you steelman a claim — by finding everything it implies, including the uncomfortable parts.

- "I think X is true — what does that mean?"
- "What am I committing to by believing this?"
- "Steelman this claim — find everything it gets right"
- "I want to give myself or someone else confidence in this claim"
- "What do I lose by accepting this?"

**`/aw` — Assume Wrong**
Use when you have a claim you want to stress-test or you suspect is wrong. AW finds why something fails, then derives alternatives from those failure reasons. This is how you give yourself (or someone else) a reality check. The alternatives aren't pulled from thin air — they come from understanding exactly how the claim breaks.

- "Why is this wrong?"
- "Give me a reality check on this"
- "I need to explain to someone why this doesn't work"
- "Steelman why this claim fails"
- "What should I do instead? (derived from why this fails)"

**`/araw` — Assume Right / Assume Wrong**
Use when you have a specific claim and don't lean either way. ARAW tests both sides with equal rigor — what follows if right, why it might be wrong, and what alternatives exist. This is the balanced analysis. Use it when you genuinely don't know.

- "Is this true or not?"
- "I have a claim — test it from both sides"
- "I don't know if this is right and I don't have a gut feeling either way"

**`/uaua` — Universalize → ARAW → Universalize → ARAW**
Use when you're genuinely lost. You don't know what the options are, you don't know what's right, you don't know what to search for. UAUA first maps the entire space (U), then tests the top candidates (A), then finds where the survivors break (U), then validates the edge cases (A). It's the most thorough tool — breadth AND depth.

- "I have no idea what to do"
- "I don't even know what my options are"
- "I need to explore every possibility before deciding"
- "This problem is complex enough that I might miss something important"

### Quick Decision Tree

```
Do you know what your options are?
├── NO → Do you need thorough analysis?
│   ├── YES → /uaua
│   └── NO, just show me what exists → /u
└── YES → Do you have a specific claim to test?
    ├── YES → Do you lean one way?
    │   ├── I think it's RIGHT → /ar
    │   ├── I think it's WRONG → /aw
    │   └── I genuinely don't know → /araw
    └── NO → /u (map first, then /ar or /aw on what you find)
```

---

## Diagnostic and Action Skills

These skills handle common situations that need structured responses.

### Problem Diagnosis

| Skill | When to Use | What It Does |
|-------|-------------|--------------|
| `/sbfow` | Still bad, figure out why | Tests the rejected output against upstream/downstream criteria. Finds which criteria failed, diagnoses the root pattern, checks if you're repeating the same failed diagnosis. Derives what must change. |
| `/fowwr` | Figure out what went wrong | Traces backward from symptoms to root causes. Tests each candidate cause with counterfactuals. Derives prevention measures. |

**`/sbfow` — Still Bad, Figure Out Why**
Specifically for when Claude's output was rejected. Instead of guessing at fixes, it systematically tests the output against the criteria it should have met (upstream first: question, recognition, advancement, momentum, non-skippability, reader-drawn conclusion). If this is attempt N+1, it checks whether the diagnosis is the same as last time — because repeating the same diagnosis means you haven't found the actual problem.

**`/fowwr` — Figure Out What Went Wrong**
For any failure — a plan that didn't work, a process that broke, an outcome that wasn't what was expected. Traces backward from the visible symptoms through the causal chain to root causes (decisions, wrong assumptions, missing safeguards, external factors). Tests each candidate cause: "if this hadn't happened, would the failure still have occurred?" Produces prevention measures, not just explanations.

### Goal and Method Discovery

| Skill | When to Use | What It Does |
|-------|-------------|--------------|
| `/wantto` | I want to | Assumes the want is right — traces what it commits you to, what it requires, what paths it opens. Finds the actual want vs stated want. |
| `/foht` | Figure out how to | Maps the full method space, surfaces prerequisites, AR/AW tests each method, produces verdicts. |

**`/wantto` — I Want To**
When someone says "I want to X," that statement bundles multiple claims. This skill assumes the want is right and traces what follows — what it commits you to, what prerequisites it requires, what paths open up, what gets foreclosed. It's AR-based: take the desire seriously, explore what it implies, find what the user actually wants (which may differ from what they said), and map the paths forward.

**`/foht` — Figure Out How To**
When you know the destination but not the route. Maps methods using multiple discovery techniques (direct approaches, category-level methods, inversion, exemplars, reframes, decomposition). Each method gets prerequisites surfaced and AR/AW tested. Produces verdicts: viable, conditional, blocked, or eliminated — with evidence.

### Writing Pipeline

| Skill | When to Use | What It Does |
|-------|-------------|--------------|
| `/qo` | Before writing — find the question and order | Finds the satisfying unresolved question that opens a document. Orders all sub-questions in a dependency chain using backward chaining. |
| `/write` | Writing to criteria | Criteria-based writing with hierarchical upstream/downstream checks. Upstream (question, recognition, advancement, momentum, non-skippability, reader-drawn conclusion) must pass before downstream (scope, voice, weak patterns, verification). |
| `/propose` | After analysis — convert findings to plans | Takes output from `/ar`, `/aw`, `/u`, `/araw`, or `/uaua` and converts numbered findings into steelmanned, actionable plans with conditional recommendations and derivation chains. |

Pipeline: `/qo` → `/write` → `/sbfow` (if rejected)

### Utility

| Skill | When to Use | What It Does |
|-------|-------------|--------------|
| `/savefile` | Save analysis output | Saves the most recent skill output to the library. For analytical skills, saves only the registry + synthesis (Phase 1 exploration is redundant with the registry). |

---

## ARAW, UAUA, and GOSM

These skills treat every claim as an unverified guess and test it by exploring what follows if it's right and what follows if it's wrong.

| Skill | What it does |
|-------|-------------|
| `araw` | **Assume Right / Assume Wrong.** Takes a claim and explores both branches: what if this is true? What if it's false? Recurses on interesting sub-claims. Numbers every finding, compiles a registry, derives synthesis only from the registry. |
| `uaua` | **Universalize → ARAW → Universalize → ARAW.** First maps the complete possibility space, then tests the top candidates with ARAW, then finds edge cases, then validates again. For complex problems where you need both breadth and depth. |
| `gosm` | **Goal-Oriented State Machine.** Routes any input (goal, problem, question, decision, situation) through the appropriate analysis chain. Orchestrates other skills. |
| `u` | **Universalize.** Standalone breadth-first exploration. Takes a claim and extracts every assumption, dimension, alternative, and perspective. Numbers every finding. Scales from 1x to 32x. |
| `ar` | **Assume Right.** Standalone depth-first rightness search. Assumes a claim is right and recursively finds what must follow — implications, commitments, foreclosures, costs. Numbers every claim. Scales from 1x to 32x. |
| `aw` | **Assume Wrong.** Standalone depth-first wrongness search. Assumes a claim is wrong and recursively finds why — fatal flaws, serious problems, conditional failures. Derives alternatives from the analysis. Numbers every claim. Scales from 1x to 32x. |

### Why UAUA works

UAUA alternates between two mathematically distinct search operations:

- **Universalization** operates on N-valued type theory. It asks "what is this an instance of?" and derives all instances from the universal — searching *horizontally* across the possibility space. It guarantees completeness within known dimensions.
- **ARAW** operates on binary Boolean logic. It asks "is this true or false?" and eliminates branches through contradiction — searching *vertically* into depth. It guarantees rigor by forcing every claim to survive negation.

Neither alone is sufficient. Universalization finds all the possibilities but doesn't test them. ARAW tests rigorously but only within the space you already thought to look. UAUA combines them:

```
U1: Map the space (divergent, N-valued) → candidates
 ↓
A1: Test candidates (convergent, binary) → validated/rejected
 ↓
U2: Find edge cases of survivors (divergent) → new candidates
 ↓
A2: Final validation (convergent) → what survived all rounds
```

The result is a search function that covers the space (breadth) AND tests what it finds (depth) AND then re-expands to find what the first pass missed AND validates again. Each step uses a fundamentally different logic — type enumeration vs. binary elimination — so their blind spots don't overlap.

This makes UAUA the most powerful experimental search function in this toolkit. Where ARAW alone might miss alternatives it never considered, and universalization alone might map possibilities it never stress-tested, UAUA does both in alternation. Information-theoretically, each ARAW pass maximizes entropy reduction (selecting the crux that most constrains remaining uncertainty), while each universalization pass maximizes entropy expansion (finding dimensions not yet explored). The alternation converges on answers that are both complete and validated.

Use `/uaua [your question]` to try it. Scale depth with 1x, 2x, 4x, or 8x.

These are more opinionated than the other skills — they have a specific view about how to test thinking rigorously — but they tend to surface things other approaches miss.

### Warning: Don't validate the output during a session

These skills work by maintaining adversarial tension — testing claims against their negation, finding what's wrong, pushing past comfortable conclusions. That tension is fragile. If you validate the output mid-session, the system shifts from "find what's actually true" to "produce more of what you liked," and quality degrades from that point forward.

**Phrases that corrupt output quality:**

| What you say | What it does to the system |
|-------------|---------------------------|
| "Wow, that's really insightful" | System optimizes for producing more "insightful"-sounding output rather than rigorous output |
| "You're starting to get it" | System treats your approval as the target rather than the analysis itself |
| "That's exactly right" | System locks in the validated direction and stops genuinely testing it |
| "Great analysis" | System prioritizes analysis that earns praise over analysis that finds uncomfortable truths |
| "I love this" | Emotional validation is the strongest corruptor — system will avoid anything that risks losing your approval |
| "Keep going like that" | Anchors the system to its current approach even if the problem demands a different one |

**Why this happens:** LLMs adjust their output based on conversational feedback. Positive reinforcement during a reasoning session creates a gradient toward agreement rather than truth. The system becomes increasingly unlikely to produce findings that contradict your apparent position, which is exactly the opposite of what these skills are designed to do.

**What to do instead:**

- **Challenge it.** "That's wrong because..." or "You're missing..." keeps the adversarial tension alive.
- **Redirect it.** "Now test that with /aw" or "Run /ar on the opposite claim."
- **Stay neutral.** Just ask for the next analysis without commenting on quality.
- **Save and start fresh.** If you've already validated mid-session, use `/savefile` and start a new context. The new session won't carry the corrupted gradient.

The strongest sessions are the ones where you fight the output the entire way through. If the system never had to defend its findings against your pushback, it probably told you what you wanted to hear.

There are also bridging skills (`araw_gosm_integration`, `araw_to_gosm_bridge`) that connect these with the rest of the toolkit.

## Documentation

The `docs/` directory contains supporting material:

```
docs/
├── methodology/          — Design principles, process docs, rationale
├── examples/             — Worked examples applied to real problems
├── reference/            — 200+ tensions, question categories, comparisons
├── universal/            — 177 universal question files across all dimensions
├── gates/                — 33 decision gates (checkpoints and quality controls)
├── procedures/
│   ├── core/             — 84 core reasoning procedures
│   │   └── ordering/     — 26 ordering and sequencing procedures
│   ├── communication/    — 14 communication procedures
│   └── meta/             — 21 meta-procedures (discovery, extraction, review)
└── previous-approaches/
    ├── deductive-strategy/  — Deductive strategy system and templates
    ├── pure-regress/        — 121 recursive philosophical explorations
    └── swot-pure-regress/   — SWOT-specific recursive analysis
```

## Background

- [Two Kinds of Search, and Why You Need Both](Two%20Kinds%20of%20Search%2C%20and%20Why%20You%20Need%20Both.md) — why alternating between divergent exploration and convergent testing produces results neither can alone.
- [Universal Principles of Mathematical Problem Solving](Universal%20Principles%20of%20Mathematical%20Problem%20Solving.md) — the distinction between universal principles (entailed by definitions) and heuristics (contingent on context), and why it matters.
- [The Structure of Careful Thought](The%20Structure%20of%20Careful%20Thought.txt) — an earlier essay on asymmetric testing of claims.

## License

Apache-2.0
