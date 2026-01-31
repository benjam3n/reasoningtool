# Reasoning Toolkit

This project contains 355 thinking skills. Each skill is a structured procedure in `skills/[name]/SKILL.md`.

## How Skills Work

When the user types `/skillname [input]`, read the corresponding `skills/[skillname]/SKILL.md` file and follow its instructions, applying them to the user's input.

## Invoking Skills

When you see `→ INVOKE: /procedure_name [args]` in a skill, read and execute that skill next. Skills can chain into other skills — follow the chain until completion.

## Skill Discovery

If the user asks what skills are available, point them to the `skills/` directory or suggest relevant skills based on what they're trying to do.

## Category Skills (Start Here)

These are sub-orchestrators — they classify your input and route to the right analytical skills.

| User has... | Use | Mode |
|---|---|---|
| A claim to test | `/claim` | ARAW |
| A decision to make | `/decide` | ARAW |
| An idea to test | `/viability` | ARAW |
| Work to assess | `/evaluate` | ARAW |
| Something broken | `/diagnose` | UAUA |
| A space to explore | `/search` | UAUA |
| A goal or want | `/want` | AR-forward |
| A "how do I" question | `/how` | AR-forward |
| A feeling or frustration | `/emotion` | AR-forward |
| Something to execute | `/action` | Direct |
| Content to produce | `/create` | Direct |
| A domain-specific question | `/technical` | Router |
| A problem to analyze | `/analyze` | Router |
| Need for maximum effort | `/certainty` | Maximum |
| Something to iterate on | `/iterate` | Meta-iteration |
| Need orientation | `/meta` | Informational |
| A prompt to improve | `/sp` | — |

## Direct Skills (Power Users)

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
