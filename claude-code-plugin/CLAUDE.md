# Reasoning Toolkit

This project contains 654 thinking skills. Each skill is a structured procedure in `skills/[name]/SKILL.md`.

## How Skills Work

When the user types `/skillname [input]`, read the corresponding `skills/[skillname]/SKILL.md` file and follow its instructions, applying them to the user's input.

## Invoking Skills

When you see `→ INVOKE: /procedure_name [args]` in a skill, read and execute that skill next. Skills can chain into other skills — follow the chain until completion.

## Skill Execution Principles

When executing any skill, these principles apply universally:

1. **Derive, then verify.** When a skill specifies minimum counts ("at least 3 reasons") or category lists ("Technical: performance, reliability..."), derive your items from the specific input FIRST. Use minimums and categories as a completeness check AFTER, not as a starting template. If you can't point to the specific input feature that generated an item, it's retrieved, not derived.

2. **Passing is a valid result.** If your analysis finds no problems after a genuinely severe test, say so with confidence. "Nothing wrong found" after rigorous testing is a strong positive finding, not a sign you missed something. The goal is accuracy, not adversarial output.

3. **Hedging must be earned.** State conclusions at the strength the evidence supports. If evidence points 65% one direction, say it leans that direction — don't retreat to "inconclusive" because it feels safer. Hedging beyond what evidence warrants is a form of dishonesty.

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
| Something broken | `/diagnose` or `/fix` | UAUA |
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
| Something to categorize | `/categorize` | Direct |
| Something to improve | `/improve` | Direct |
| Something to fix | `/fix` | Direct |
| A large body of work | `/perceive` | Direct |

## Direct Skills (Power Users)

| User wants to... | Suggest |
|---|---|
| Make a decision | `/dcp`, `/cmp`, `/cba` |
| Solve a problem | `/rca`, `/dbg`, `/dcm` |
| Explore options | `/se`, `/poa`, `/dd` |
| Check assumptions | `/aex`, `/ht` |
| Write something | `/pw`, `/stl` |
| Plan a project | `/de`, `/to`, `/plansuite` |
| Understand a goal | `/gu`, `/gd`, `/grf` |
| Research a topic | `/lr`, `/fia` |
| Validate work | `/pv`, `/mv`, `/vbo` |
| Generate ideas | `/ma`, `/cda`, `/cuw` |
| Check an answer | `/fwa`, `/frq` |
| Check themselves | `/sdc`, `/sid`, `/ecal`, `/pbtc`, `/wawd` |
| Recover from error | `/rmm`, `/kta` |
| Choose depth/scope | `/alt`, `/ign`, `/dwt` |
| Understand a system | `/fohw`, `/insd` |
| Figure out what to do with data | `/fowtd`, `/fowtdn` |
| Organize/categorize | `/categorize`, `/cls` |
| Fix something | `/fix`, `/diagnose` |
| Improve something | `/improve`, `/iterate` |
| Resume prior work | `/statous` |
