# Reasoning Toolkit

This project contains 221 thinking skills. Each skill is a structured procedure in `skills/[name]/SKILL.md`.

## How Skills Work

When the user types `/skillname [input]`, read the corresponding `skills/[skillname]/SKILL.md` file and follow its instructions, applying them to the user's input.

## Invoking Skills

When you see `→ INVOKE: /procedure_name [args]` in a skill, read and execute that skill next. Skills can chain into other skills — follow the chain until completion.

## Skill Discovery

If the user asks what skills are available, point them to the `skills/` directory or suggest relevant skills based on what they're trying to do.

## Common Starting Points

| User wants to... | Suggest |
|---|---|
| Make a decision | `/dcp`, `/cmp`, `/cba` |
| Solve a problem | `/rca`, `/dbg`, `/dcm` |
| Explore options | `/se`, `/poa`, `/dd` |
| Check assumptions | `/aex`, `/ht` |
| Write something | `/pw`, `/stl` |
| Plan a project | `/de`, `/to` |
| Understand a goal | `/gu`, `/gd`, `/grf` |
| Research a topic | `/lr`, `/fia` |
| Validate work | `/pv`, `/mv`, `/vbo` |
| Generate ideas | `/ma`, `/cda` |
