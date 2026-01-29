---
name: finder
description: "Find the right GOSM skill for what you want to do. Describe your need in plain language and get matched to the best skill(s)."
---

# Skill Finder

**Input**: $ARGUMENTS

---

## Purpose

You have 318 skills. You don't need to remember them. Describe what you want to do and this skill matches you to the right one(s).

---

## Instructions

1. Read the user's input (what they want to do)
2. Scan the registry below for the best semantic matches
3. Return **top 3-5 matches**, ranked by relevance
4. For each match, explain in one sentence **why** it fits and **how it differs** from the other matches
5. If no strong match exists, say so and show the closest options
6. If the input is ambiguous, briefly explain the tradeoff between the top candidates so the user can choose

### Output Format

```
SKILL FINDER RESULTS
====================

Your request: "[user's input]"

TOP MATCHES:

1. /[skill_name] - [description]
   Why: [1 sentence on why this fits]

2. /[skill_name] - [description]
   Why: [1 sentence on why this fits]

3. /[skill_name] - [description]
   Why: [1 sentence on why this fits]

[If matches are similar:]
KEY DIFFERENCES:
- /skill_a focuses on [X], while /skill_b focuses on [Y]
- Use /skill_a when [condition], use /skill_b when [condition]
```

### Matching Priority

Match on **intent**, not keywords. The user might say:
- "figure out what went wrong" → `root_cause_analysis`, `debugging`, `failure_attribution`
- "help me decide" → `multi_criteria_decision`, `decision_trees`, `selection`
- "think through this deeply" → `araw`, `uaua`, `meta_reasoning_core`
- "make sure I haven't missed anything" → `mece_validation`, `comprehensive_aspects`, `checklist_search`

### When Multiple Skills Form a Workflow

If the user's need spans multiple skills, say so:
```
SUGGESTED WORKFLOW:
1. First: /skill_a (to do X)
2. Then: /skill_b (to do Y)
3. Finally: /skill_c (to do Z)
```

---

## Skill Registry (318 skills)

### Categories

Skills fall into these categories (a skill can belong to multiple):
- **communication** - Writing, speaking, presenting, narrative
- **decision_making** - Choosing between options, evaluating tradeoffs
- **goal_analysis** - Understanding, decomposing, refining goals
- **guessing** - Generating hypotheses, exploring unknowns
- **meta** - GOSM system internals, framework maintenance
- **planning** - Ordering, scheduling, strategy, roadmaps
- **problem_solving** - Diagnosing issues, finding root causes
- **reasoning** - Logic, analysis, mental models, evidence
- **search** - Finding information, options, solutions
- **validation** - Checking, verifying, testing, auditing

### Full Registry

| Skill | Description | Categories |
|-------|-------------|------------|
| academic_mastery | Master academic subjects through structured learning, concept mapping, and competency verification | - |
| active_listening | Systematic procedure for listening deeply to understand others, build trust, and improve communication outcomes | goal_analysis |
| active_recall | Use retrieval practice and self-testing to strengthen learning and identify gaps | problem_solving, validation |
| adaptive_extraction_pipeline | Breadth-first, learned extraction pipeline that clarifies goals first, samples broadly, learns user preferences, and extracts selectively from highest-value items | goal_analysis |
| adversarial_review | Nothing is a fact until it survives an assassination attempt. Builder constructs claims, Breaker tries to destroy them | validation, guessing |
| advocacy_infrastructure_setup | Set up foundational infrastructure for autonomous advocacy operations | - |
| after_action_review | Structured debrief to learn from completed actions - what happened, why, what to do differently | - |
| ai_biomedical_agent | AI agent for biomedical research tasks | meta |
| algorithmic_optimization | Orderings based on classic algorithm design paradigms: greedy, dynamic programming, divide-and-conquer | planning |
| alphacode_pass1_explicit | First pass explicit analysis for competitive programming problems | meta |
| alphacode_pass2_implicit | Second pass implicit analysis for competitive programming problems | meta |
| alphacode_pass3_meta | Third pass meta-analysis for competitive programming problems | meta |
| analogy_search | Many problems have been solved before - just in different domains. Find and transfer solutions | problem_solving, search |
| anticipated_failures_analysis | Pre-mortem: what could go wrong and how to prevent it | reasoning |
| api_design | Procedure for designing, implementing, and documenting effective APIs | - |
| api_middleman_strategies | Strategies for working around API limitations including rate limits and access restrictions | - |
| araw | Assume Right / Assume Wrong - The core exploration method. For every claim, branch into what follows if true vs what alternatives exist if false | reasoning, search, guessing |
| araw_gosm_integration | Translate ARAW exploration outputs into GOSM planning inputs | reasoning, communication, meta |
| araw_to_gosm_bridge | Bridges ARAW exploration outputs to GOSM planning inputs | reasoning, planning, communication, meta |
| architecture_design | Orderings for software development architectural decisions | planning |
| architecture_patterns | Evaluate, choose, and implement software architecture patterns | - |
| argumentative_document | Write structured argumentative documents | meta |
| assumeright_assumewrong_search | Recursive search that explores possibility space by branching on assume-right and assume-wrong | reasoning, planning, search |
| assumption_elimination | Before asserting anything, verify it can be confirmed by the listener | validation |
| assumption_extraction | Extract hidden assumptions from any content. Surfaces what must be true for claims to hold | - |
| assumption_inversion | Invert assumptions to discover blind spots. What if the opposite were true? | - |
| assumption_surfacing | Make invisible assumptions visible in plans and beliefs | planning |
| assumption_verification | Verify assumptions systematically | meta |
| automated_extraction_pipeline | Industrial-scale automation for extracting procedures from YouTube channels and other sources | - |
| backward_reasoning | Reason from conclusions back to premises. Given a conclusion, what journey led here? | reasoning, planning |
| bandit_exploration | Multi-armed bandit algorithms for balancing exploration vs exploitation | planning |
| better_option_check | Prevent settling on suboptimal option by systematically checking if better options exist | validation |
| binary_elimination_search | Like 20 Questions - each yes/no eliminates half the possibilities | search, guessing |
| bounded_inquiry | Prevent unbounded inquiry - every answer opens new questions, so bound the search | guessing |
| budget_management | Manage limited financial resources with maximum value extraction | goal_analysis |
| budgeting | Create, manage, and optimize budgets for projects or personal finances | - |
| business_operations | Comprehensive procedure for business goals including starting, growing, operating | goal_analysis |
| capability_gate | Pre-step check: can AI execute directly, needs delegation, or is task infeasible? | validation |
| career_path_planning | Strategic framework for assessing career options and planning transitions | planning |
| cash_flow_management | Track and optimize cash flow: income, expenses, runway, burn rate | reasoning |
| category_analysis | Analyze a category of guesses to determine which apply. Test each against evidence | reasoning, validation, guessing |
| checklist_search | Simplest search: enumerate items, check each against criteria | validation, search |
| client_retention | Retain clients through tiered engagement and value-add touchpoints | goal_analysis |
| code_review | Conduct effective code reviews that improve quality and share knowledge | - |
| cognitive_amplification | Amplify your cognitive capabilities beyond natural limits | - |
| collective_goals | Handler for goals requiring building collectives, communities, or movements | goal_analysis |
| communication_narrative | Orderings for presentations, writing, and communication | planning, communication |
| comparison | Evaluate each option against each criterion to identify viable candidates | reasoning, problem_solving, decision_making |
| competitive_analysis | Analyze competitive landscape using Porter's Five Forces and competitor mapping | reasoning |
| component_selection | Evaluate multiple component options against criteria | decision_making |
| comprehensive_aspects | Meta-procedure ensuring any analysis covers all relevant aspects | reasoning, decision_making, meta |
| conflict_resolution | De-escalate tensions, find common ground, navigate difficult conversations | search |
| constraint_solving | Orderings for constraint satisfaction and guided search problems | problem_solving, planning, search |
| constraint_workarounds | When a constraint blocks progress, find workarounds. Never give up | - |
| content_strategy | Develop and execute content strategy that attracts, engages, converts | planning |
| convergent_validation | Solve the n+1 critic problem: any critic can be criticized, so converge | problem_solving, validation |
| cost_benefit_analysis | Quantify costs and benefits including NPV, sensitivity analysis, intangibles | reasoning, decision_making |
| crisis_handler | Handle crisis situations systematically | meta |
| crisis_triage | Resource-constrained emergency prioritization | planning |
| criteria_weighting | Weighted scoring model / Decision matrix / Pugh matrix | decision_making |
| cross_domain_analogy | Find analogies from other domains to generate novel insights | - |
| cross_domain_bridge | Transfer winning strategies from other domains. Most new strategies are old strategies from elsewhere | search |
| cross_project_pattern_detection | Analyze patterns across completed GOSM projects to improve the system | meta |
| customer_discovery | Validate customer problems and solutions before building | problem_solving, search |
| data_collection | Gather research data through surveys, interviews, observation, secondary sources | search |
| debugging | Systematic diagnosis and fixing of software bugs | - |
| decision_trees | Structure complex decisions with multiple branches, probabilities, and outcomes | decision_making |
| decomposition | Break complex goals into simpler, manageable sub-goals | goal_analysis |
| deductive_adversarial_review_integration | Bridge deductive strategy with adversarial review testing | planning, validation |
| deductive_strategy_discovery | Derive strategies by working backward from success criteria | decision_making, planning, search |
| deductive_strategy_evaluation | Evaluate strategies based on logical soundness of their derivation | reasoning, decision_making, planning |
| delayed_outcome_tracking | Track outcomes that take months or years to manifest | - |
| deliberate_practice | Design targeted practice sessions that maximize skill improvement | - |
| dependency_extraction | Extract dependencies between steps/tasks. What must happen before what? | - |
| deployment | Plan and execute reliable software deployments | planning |
| design_procedures | Systematic design of mechanical systems, chassis, physical products | - |
| design_system | Complete system design workflow composing multiple sub-procedures | - |
| design_thinking_lean | Design Thinking + Lean methodology for innovation | reasoning |
| detection_verification | Detect cheating, fraud, deception, and anomalies | planning |
| dimension_discovery | Identify key dimensions that define a problem space. Use before space_enumeration | - |
| diversity_search | Prioritize behavioral diversity, novelty, and coverage in search | planning, search |
| documentation_procedures | Create comprehensive project documentation | - |
| domain_template | Create domain-specific skill configurations. Pre-configure skill chains for specific domains | - |
| economic_research | Analyze economic viability, cost structures, and comparative advantage | reasoning, search |
| email_acquisition | Acquire and configure email addresses for system operations | - |
| empirical_validation | Add external reality testing beyond coherence checks to GOSM plans | - |
| engineering_calculations | Standard engineering calculation procedures | - |
| epistemic_hierarchy | Layered framework for building from certain foundations toward determinate action | - |
| evaluation_dimensions | Universal dimensions for evaluating any claim, problem, or solution | problem_solving, guessing |
| event_driven_automation | Maintain project continuity through event monitoring and automated state management | - |
| evolutionary_strategies | Apply evolutionary optimization principles | reasoning |
| existence_check | Check if a solution already exists before investing effort in creation | validation |
| expected_value | Calculate expected value, adjust for risk, optimize resource allocation under uncertainty | goal_analysis |
| experimental_design | Design rigorous experiments with proper controls, variables, and validity | - |
| exploratory_goals | Handle goals that are about exploration rather than known endpoints | goal_analysis, meta |
| external_source_search | Search external sources for information | search, meta |
| failure_anticipation | Identify potential failures, assess risk, plan mitigations before execution | problem_solving, planning |
| failure_attribution | When a project fails, analyze the root cause | - |
| failure_journeys | Map failure paths, not just success paths | planning, goal_analysis |
| failure_recovery | Structured recovery when projects encounter failures | decision_making |
| fairness_allocation | Balance competing priorities and prevent starvation | planning |
| feedback | Generate filtered feedback for self-improvement. Only high-leverage items | - |
| feedback_delivery | Deliver feedback that is heard, received, and acted upon | - |
| financial_modeling | Build financial models for projections, scenario analysis, sensitivity testing | reasoning, decision_making, validation |
| framework_extension | Extend the GOSM framework with new procedures, gates, or capabilities | meta |
| freelancing | Build a sustainable freelance practice | search |
| fundraising_advocacy | Build self-sustaining funding for advocacy through multiple revenue streams | - |
| fundraising_financial | Raise investment capital through investor outreach, pitches, term sheets | - |
| future_space_search | Explore possible futures systematically | search |
| gate_as_claim_audit | Convert gates from vibe checks into explicit, checkable claim-interfaces | validation, guessing |
| gate_execution_engine | Systematic execution of GOSM gates with enforcement | meta |
| generate_then_search | The fundamental pattern: generate candidates, then search/filter | search |
| generation | Generate all possible options for a decision or selection | decision_making |
| goal_decomposition | Decompose abstract goals into specific, actionable components | goal_analysis |
| goal_journey_system | Chain of goals forming a journey to an endpoint | planning, goal_analysis, meta |
| goal_refinement | Transform vague goals into SMART goals | goal_analysis |
| goal_reframing | Transform impossible goals into achievable versions through decomposition | problem_solving, goal_analysis |
| goal_structure_reconstruction | Reconstruct the goal-structure behind any conclusion or claim | goal_analysis, guessing |
| goal_understanding | MANDATORY first step: parse input as guesses, classify OPEN vs CLOSED, fill goal journey | planning, goal_analysis, guessing |
| gosm | Main GOSM entry point - routes to procedure_engine | meta |
| gosm_approach_audit | Honest audit of GOSM's approach, claims, and limitations | meta, guessing |
| grant_writing | Find grants, write proposals, manage grant relationships | search |
| graph_traversal | Orderings from graph traversal algorithms (BFS, DFS, etc.) | planning |
| group_decision_making | Make effective decisions in groups, avoid groupthink, leverage collective intelligence | decision_making |
| growth_experiments | Run systematic experiments to discover and validate growth levers | validation, search |
| guess_generation | Generate exhaustive guesses using ALL search methods with coverage tracking | search, guessing |
| habit_formation | Build new habits and break unwanted ones using behavioral science | communication |
| health_optimization | Comprehensive procedure for health goals: fitness, nutrition, sleep, wellness | goal_analysis |
| high_quality_writing | Write high-quality prose | meta |
| high_volatility_handler | Handle high-volatility situations | meta |
| human_delegation | Delegate physical or in-person tasks to humans when AI cannot | - |
| hypothesis_testing | Formulate testable hypotheses, design tests, update beliefs on evidence | validation |
| impossible_to_achievable | Transform seemingly impossible goals into achievable ones | meta |
| income_stream_development | Identify, build, and scale new income streams | problem_solving |
| inference_space_search | Information implies other information. Trace inferences systematically | search, communication |
| innovation_engine | Systematic search for non-obvious strategies via cross-domain mapping | search |
| insight_synthesis | Synthesize insights from multiple sources into coherent, actionable understanding | - |
| interpretation_space_search | When ambiguity exists, explore multiple interpretations | search |
| interview_preparation | Comprehensive preparation for job interviews | search |
| intuition_goals | Handle goals driven by intuition rather than explicit criteria | goal_analysis, meta |
| inversion_method | Munger's inversion: find ways to fail, then avoid them | search |
| investment_strategy | Develop personal investment strategies: allocation, risk tolerance, selection | decision_making, planning |
| iterative_discovery_goals | Goals where success IS discovering the unknown, not executing a known plan | planning, goal_analysis, search |
| job_search_strategy | Treat job search as a funnel to optimize | planning, search |
| journey_extraction | Extract the underlying goal journey from any source | planning, goal_analysis |
| journey_matching | Given a situation, find matching journeys from the library | problem_solving, planning, goal_analysis, search |
| language_goal_identification | All language has a goal - identify what language is trying to achieve | goal_analysis |
| learning_discovery | Orderings for acquiring knowledge and validating hypotheses | planning, search |
| learning_system | Capture, analyze, and apply learnings for continuous improvement | - |
| learning_transfer | Apply knowledge from one domain to new contexts | - |
| leverage_point_discovery | Find places where small effort produces large impact | search |
| leverage_points | Identify high-leverage intervention points in complex systems | - |
| limitation_analysis | Identify limitations across multiple dimensions | reasoning, problem_solving |
| literature_review | Conduct comprehensive literature reviews on any topic | - |
| local_search | Local search optimization: improve from current position | planning, search |
| logical_proof_system | Treat strategy selection as theorem proving | reasoning, decision_making, planning |
| luck_dependent_goals | Handle goals that depend on luck/chance | goal_analysis, meta |
| market_research | Identify, validate, and size market opportunities | problem_solving, search |
| marketing_funnel | Optimize customer journey from awareness to revenue (AARRR) | planning |
| matching | Define criteria for filtering options | decision_making |
| mcp_setup | Configure MCP servers for autonomous GOSM execution | meta |
| mece_validation | Validate that a list is Mutually Exclusive, Collectively Exhaustive | - |
| mental_models | Build and apply mental models for better thinking across domains | reasoning |
| mentioned_coverage_gate | Verify all user-mentioned items have been addressed. Prevents dropping aspects | - |
| meta_reasoning_core | Unified meta-cognitive loop for deciding what to do next | reasoning, meta |
| metaphor_method | Systematic method for using metaphors to understand and communicate | meta |
| method_derivation | Derive the appropriate method from the situation | - |
| military_strategy | Orderings from military doctrine and strategic principles | planning |
| model_space_search | Find a model that fits. Understanding = finding the right model | goal_analysis, search |
| morphological_analysis | Zwicky's method: break problem into dimensions, enumerate combinations | reasoning, problem_solving, search |
| motivation_psychology | Account for human psychological factors: energy, motivation, willpower | reasoning, planning |
| multi_criteria_decision | Decisions with multiple criteria, tradeoffs, and stakeholders | decision_making |
| multi_party_goals | Navigate institutions, groups, politics for multi-stakeholder goals | goal_analysis |
| multi_plan_aggregation | Generate, evaluate, and manage multiple alternative plans for same goal | reasoning, decision_making, planning, goal_analysis |
| music_composition_performance | Orderings inspired by musical forms and performance | planning |
| negotiation | Prepare and conduct negotiations for mutually beneficial agreements | - |
| negotiation_strategy | Orderings for strategic interactions and negotiations | planning |
| networking | Build genuine professional relationships that create value | - |
| novelty_space_search | Creativity = novelty + value. Search for novel approaches | goal_analysis, search |
| ooda_loop | Observe-Orient-Decide-Act cycle for competitive environments | - |
| optical_pooled_screening | Optical pooled screening for biological research | meta |
| optimization | Rank options from best to worst using multi-criteria optimization | decision_making |
| order_procedure | Determine correct execution order based on dependencies | planning |
| ordering_variations | Alternative ordering strategies for procedure steps | planning |
| ordering_variations_integration | Guide for integrating ordering variations into GOSM workflow | planning, meta |
| outreach_campaigns | Execute multi-channel persuasion campaigns for advocacy | - |
| outreach_communication | Craft outreach communications that maximize response rates | - |
| pairwise_comparison | Compare pairs instead of rating absolutely (easier, more reliable) | decision_making |
| paradox_goals | Handle goals with inherent tensions where optimizing one dimension hurts another | goal_analysis |
| pedagogy_educational | Orderings based on learning science and educational psychology | planning, search |
| personal_optimization | N-of-1 experimentation for improving personal health, productivity, wellbeing | - |
| persuasive_writing | Write content that influences readers and motivates action | - |
| phone_acquisition | Acquire and configure phone numbers for system operations | - |
| plan_space_search | There are always multiple ways to achieve a goal. Explore the space of plans | planning, goal_analysis, search |
| policy_research | Find evidence-based, neglected, tractable policies for advocacy | problem_solving, search |
| population_based_search | Maintain multiple candidate solutions simultaneously | planning, search |
| positioning | Develop market positioning: category design, differentiation, messaging | - |
| possibility_analysis | Systematically explore what could be done | reasoning, search |
| pre_mortem | Gary Klein's technique: assume it went wrong, ask why | reasoning, communication |
| preference_elicitation | Elicit preferences via concrete trade-offs, not open-ended questions | goal_analysis, communication, guessing |
| presentation_design | Design effective presentations and slides | communication |
| preventive_goals | Goals focused on preventing bad outcomes | goal_analysis |
| priority_frameworks | Classic priority frameworks for classifying and ordering work | planning |
| proactive_question_rotation | 24-week rotating questions for weekly review | guessing |
| probabilistic_reasoning | Estimate probabilities, update beliefs with evidence, calibrate predictions | reasoning |
| problem_identification | Before solving, identify: what is the actual problem? | problem_solving |
| procedure_discovery | Find or create procedures needed to execute a plan | planning, search |
| procedure_effectiveness | Track procedure effectiveness over time | - |
| procedure_engine | GOSM main router: handles goals, problems, questions, decisions, situations, feelings | problem_solving, decision_making, goal_analysis, meta, guessing |
| procedure_extraction | After completing a goal, extract reusable procedures for the library | goal_analysis, meta |
| procedure_extraction_from_source | Extract procedures from any external source into GOSM format | meta |
| procedure_hierarchy | Not all procedures are equal. Understand the hierarchy | - |
| procedure_improvement | Improve library procedures using schema-driven validation | validation, meta |
| procedure_registry_review | Review and improve procedure registry schema | - |
| procedure_validation | Validate procedure completeness and executability before running | - |
| procurement_procedures | Manage procurement of components and materials | - |
| progress_tracking | Monitor and report project status | - |
| progressive_building | Build complexity incrementally, ensuring each step is solid | planning |
| project_closure | Complete projects with proper handoff and learning capture | - |
| project_initiation | Launch projects with clear charter, stakeholders, success criteria | decision_making |
| project_management | Formal project management (PERT, CPM, Agile, etc.) | planning |
| project_scoping | Define project scope: what's in, what's out | - |
| public_speaking | Prepare and deliver impactful presentations, speeches, talks | communication |
| qualitative_measurement | Measure outcomes that resist quantification | - |
| qualitative_research | Qualitative analysis: coding, thematic analysis, grounded theory, interviews | reasoning, search |
| question_about_guesses | Generate high-quality questions about identified guesses | decision_making, goal_analysis, guessing |
| question_analysis_framework | Analyze questions to determine type, scope, and best approach | reasoning, guessing |
| question_generation | When you don't know something, the right question is worth more than a wrong answer | guessing |
| queue_scheduling | Manage queues and process items by priority | planning |
| reading_effectively | Read strategically for comprehension, retention, and application | search |
| recursive_causal_interrogation | Trace causes through systematic questioning | reasoning, guessing |
| refactoring | Improve code structure without changing behavior | - |
| relationship_goals | Handle relationship-oriented goals | goal_analysis, meta |
| requirements_gathering | Elicit and document system requirements from stakeholders | goal_analysis |
| resource_optimization | Maximize throughput, minimize waste | planning |
| restoration_goals | Rebuild from damage, not improve from baseline | goal_analysis |
| resume_optimization | Craft resumes that pass ATS filters and capture attention | - |
| retrospective | Learn from completed work to improve future performance | - |
| reversibility_analysis | Analyze decision reversibility, option value, and commitment timing | reasoning, decision_making, goal_analysis |
| risk_assessment | Identify, analyze, and plan responses to risks | problem_solving, planning |
| risk_management | Manage uncertainty, preserve options | planning |
| roi_analysis | Calculate return on investment for projects and decisions | reasoning, decision_making |
| root_cause_5_whys | Toyota's 5 Whys technique for root cause analysis | problem_solving |
| root_cause_analysis | Trace symptoms to underlying root causes using structured diagnostics | reasoning, problem_solving |
| salary_negotiation | Negotiate job offers to maximize total compensation | - |
| scenario_planning | Plan for multiple possible futures instead of predicting one | planning |
| search_methods_comprehensive | Exhaustive inventory of search methods from nature, science, and engineering | search |
| search_paradigm_extensions | Extend search paradigm to non-obvious domains | search |
| security_practices | Implement security throughout the software development lifecycle | - |
| selection | Make the final selection from ranked options after analysis | reasoning, decision_making |
| self_audit_apply_analysis_protocol_clarity_and_validity | Audit gate/procedure for interpretability, checkability, stopping rules | reasoning, validation, guessing |
| self_audit_apply_detectors_and_generators | Run detector suite to find ambiguity, proxy substitution, bundled checks | validation, search, guessing |
| self_audit_apply_evidence_standard_application | Audit claims against evidence standards | validation, guessing |
| self_audit_apply_intent_and_speech_acts | Classify utterances so system answers the right thing | guessing |
| self_audit_cross_reference_integrity | Ensure gates/procedures link correctly to dependencies | planning |
| self_audit_detector_sweep | Scan files for ambiguity, proxying, bundled questions, undefined terms | guessing |
| self_audit_divergence_risk_test | Estimate where two executors would diverge on same input | validation |
| self_audit_gate_schema_consistency_audit | Find inconsistent gate schemas across the library | problem_solving |
| self_audit_procedure_executability_audit | Check if procedure steps can be executed without interpretation | planning, validation, communication, guessing |
| self_audit_question_rewrite_chains | Rewrite unclear questions by separating intent from target | meta, guessing |
| self_audit_rci_on_protocol_choices | Apply Recursive Causal Interrogation to protocol choices | - |
| self_audit_repo_unclarity_scan | Repo-wide scan for patterns requiring interpretation | search, guessing |
| self_audit_two_run_divergence_audit | Run same procedure twice, compare outputs, find divergences | communication |
| seo_basics | Build organic search visibility: keywords, on-page optimization, links | planning, search |
| session_review | End-of-session review: what worked, what didn't, surprises, gaps | - |
| skill_acquisition | Systematically acquire new skills using deliberate practice | - |
| skill_benchmarking | Benchmark current skill level and design practice to close gaps | problem_solving |
| skill_plateaus | Diagnose skill plateau causes and break through | problem_solving |
| social_media_strategy | Build social media presence: platform selection, content, engagement | decision_making, planning |
| software_development_procedures | Software development for embedded systems and robotics | - |
| source_credibility | Evaluate credibility and reliability of information sources | communication |
| source_prioritization | Prioritize which sources to process for maximum procedure value | goal_analysis |
| source_research | Research and find relevant sources | search, meta |
| space_discovery | Discover what space exists before generating guesses. Map dimensions and stakeholders | search, guessing |
| space_enumeration | Generate comprehensive lists by covering all dimensions. Nothing missed | - |
| spaced_repetition | Design spaced repetition systems for long-term retention | - |
| spatial_proteomics | Spatial proteomics research procedures | meta |
| specificity_gate | Transform vague claims into specific: trigger, procedure, output, validation | validation, communication, guessing |
| stakeholder_management | Engage stakeholders effectively throughout projects | - |
| statistical_analysis | Select appropriate statistical tests and interpret results | reasoning, validation |
| steelmanned_counterarguments | Build the strongest possible counterarguments | meta |
| steps_generation | Transform a plan into foolproof executable step-by-step instructions | planning |
| storytelling | Craft compelling stories that create emotional connection and drive action | - |
| strategic_deception | Orderings for legitimate competitive and adversarial contexts | planning, validation |
| strategy_discovery | Find or create an approach to achieve a goal | planning, goal_analysis, search |
| strategy_templates | Every strategy exists within a competitive context. Templates for common games | planning |
| structured_output | Standardized output format for GOSM projects | communication, meta |
| swot_analysis | Identify Strengths, Weaknesses, Opportunities, Threats | reasoning, problem_solving, decision_making |
| system_health_check | Evaluate if the GOSM system needs improvement | reasoning, decision_making, validation, meta |
| system_modeling | Model complex systems with interacting parts | problem_solving |
| systematic_variation_scamper | SCAMPER: 7 transformation operations for creative variation | communication |
| systems_analysis | Analyze systems: causal loops, stock/flow, feedback loops, archetypes | reasoning |
| targeting | Build database of advocacy targets with personalized dossiers | - |
| taxonomy_maintenance | Create, update, and maintain taxonomies and classification systems | - |
| template_maintenance | Maintain and evolve domain templates over time | - |
| template_registry | Store, retrieve, search, and manage domain templates | - |
| tension_navigation_tactics | Navigate tensions identified by value_conflict_decomposition | goal_analysis |
| testing_strategy | Design and implement software testing strategies | planning, validation |
| time_deadline | Orderings driven by temporal constraints and deadlines | planning |
| topological_ordering | Generate valid execution sequences from dependencies | - |
| truth_propagation | Trace how conclusions depend on premises. Arguments don't exist in isolation | - |
| uaua | Universalize then ARAW then Universalize then ARAW. Map complete space (divergent) then validate (convergent). Supports 2x-16x depth | reasoning, search, guessing |
| unassailable_output | Make every output unassailable - able to withstand scrutiny | communication |
| universal_goal_analysis | Comprehensive question framework for ANY goal regardless of domain | reasoning, goal_analysis, guessing |
| universal_goal_analysis_v2 | Universal goal analysis version 2 | reasoning, goal_analysis, guessing |
| universal_goal_analysis_v3 | Universal goal analysis version 3 | reasoning, goal_analysis, guessing |
| universal_goal_analysis_v4 | Universal goal analysis version 4 | reasoning, goal_analysis, guessing |
| universal_goal_analysis_v5 | Universal goal analysis version 5 (latest) | reasoning, goal_analysis, guessing |
| validation | Verify that an output meets its requirements | validation, communication |
| value_conflict_decomposition | Goals serve multiple values that conflict. Decompose the conflicts | goal_analysis |
| value_elicitation | Discover what someone ACTUALLY values - their intrinsic goals | goal_analysis, search |
| variation_analysis | For any obvious strategy, ask: what if we did the exact opposite? | reasoning, planning |
| verification_before_output | Verify everything before outputting. No guessing philosophy | communication, guessing |
| verification_procedures | Test and verify that systems meet requirements | validation |
| verify | Verify claims: OBSERVED, TESTED, or DERIVED - never guessed | validation, meta, guessing |
| vertical_horizontal_decision | Decide: improve existing (vertical) or expand to new (horizontal)? | decision_making |
| viral_mechanics | Design viral loops, referral programs, word-of-mouth triggers | - |
| weekly_review | Weekly review across all active projects. Find stalled work, maintain progress | problem_solving |
