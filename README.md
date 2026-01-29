# reasoning-toolkit

207 thinking skills for Claude Code. Each skill is a structured prompt that guides you through a specific type of thinking, decision, or analysis.

## Installation

### Option 1: Run from this directory

```bash
git clone https://github.com/benjam3n/reasoning-toolkit.git
cd reasoning-toolkit/claude-code-plugin
claude
```

Claude reads the `CLAUDE.md` file and all skills become available.

### Option 2: Copy into your project

```bash
cp -r path/to/reasoning-toolkit/claude-code-plugin/skills your-project/
cp path/to/reasoning-toolkit/claude-code-plugin/CLAUDE.md your-project/
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
`high_quality_writing` · `persuasive_writing` · `storytelling` · `public_speaking` · `presentation_design` · `content_strategy` · `outreach_communication` · `feedback_delivery` · `active_listening`

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

## Experimental: ARAW, UAUA, and GOSM

These three skills use a different approach. They treat every claim as an unverified guess and test it by exploring what follows if it's right and what follows if it's wrong.

| Skill | What it does |
|-------|-------------|
| `araw` | **Assume Right / Assume Wrong.** Takes a claim and explores both branches: what if this is true? What if it's false? Recurses on interesting sub-claims. Produces a tree of tested claims. |
| `uaua` | **Universalize → ARAW → Universalize → ARAW.** First maps the complete possibility space, then tests the top candidates with ARAW, then finds edge cases, then validates again. For complex problems where you need both breadth and depth. |
| `gosm` | **Goal-Oriented State Machine.** Routes any input (goal, problem, question, decision, situation) through the appropriate analysis chain. Orchestrates other skills. |

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

See [improvedreasoningwritingexample.txt](improvedreasoningwritingexample.txt) for an essay on the thinking behind these tools.

## License

Apache-2.0
