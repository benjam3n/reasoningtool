# Reasoning Toolkit

This repository contains 367 reusable skills in `claude-code-plugin/skills/*/SKILL.md`.

## Skill Discovery

- Treat every directory matching `claude-code-plugin/skills/<skill-id>/SKILL.md` as an available skill.
- Use `claude-code-plugin/skills.json` for skill descriptions, titles, categories, and invocation metadata.
- If the user invokes a skill as `/skill-id ...`, open the matching `SKILL.md` and follow it.
- If a skill contains `-> INVOKE: /other-skill ...` or `→ INVOKE: /other-skill ...`, open that skill and continue the chain.
- If the user asks what skills exist, prefer suggesting router skills first, then inspect `claude-code-plugin/skills.json` for more specific matches.

## Router Skills

- `/claim`: test a claim
- `/decide`: compare options
- `/viability`: test whether an idea survives scrutiny
- `/evaluate`: assess work for correctness and risk
- `/diagnose`: investigate what is broken
- `/search`: explore a space broadly
- `/want`: clarify a goal
- `/how`: derive methods and next steps
- `/emotion`: handle emotionally framed requests
- `/action`: execute or operationalize work
- `/create`: produce content
- `/technical`: route domain-specific technical questions
- `/analyze`: route analysis-heavy requests
- `/certainty`: push depth until resolved
- `/iterate`: improve an existing output
- `/meta`: orient the user to the toolkit
- `/sp`: improve a prompt

## Notes

- The skill files already include Codex-compatible frontmatter.
- For global Codex installation outside this repository, use `scripts/install_codex_skills.sh`.
