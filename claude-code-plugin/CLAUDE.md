# Reasoning Toolkit

This project contains 207 thinking skills. Each skill is a structured procedure in `skills/[name]/SKILL.md`.

## How Skills Work

When the user types `/skillname [input]`, read the corresponding `skills/[skillname]/SKILL.md` file and follow its instructions, applying them to the user's input.

## Invoking Skills

When you see `→ INVOKE: /procedure_name [args]` in a skill, read and execute that skill next. Skills can chain into other skills — follow the chain until completion.

## Skill Discovery

If the user asks what skills are available, point them to the `skills/` directory or suggest relevant skills based on what they're trying to do.

## Common Starting Points

| User wants to... | Suggest |
|---|---|
| Make a decision | `/decision_procedure`, `/comparison`, `/cost_benefit_analysis` |
| Solve a problem | `/root_cause_analysis`, `/debugging`, `/decomposition` |
| Explore options | `/space_enumeration`, `/possibility_analysis`, `/dimension_discovery` |
| Check assumptions | `/assumption_extraction`, `/assumption_verification`, `/hypothesis_testing` |
| Write something | `/high_quality_writing`, `/persuasive_writing`, `/storytelling` |
| Plan a project | `/project_scoping`, `/dependency_extraction`, `/topological_ordering` |
| Understand a goal | `/goal_understanding`, `/goal_decomposition`, `/goal_refinement` |
| Research a topic | `/literature_review`, `/source_research`, `/field_analysis` |
| Validate work | `/procedure_validation`, `/mece_validation`, `/verification_before_output` |
| Generate ideas | `/morphological_analysis`, `/cross_domain_analogy`, `/innovation_engine` |
