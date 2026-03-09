---
name: "meta - Get Oriented"
description: Sub-orchestrator for meta-questions about the toolkit. Provides skill discovery, usage guidance, and orientation.
---

# Meta

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. What Does the User Need?

| Input pattern | Need | Action |
|--------------|------|--------|
| "Help" / "What can you do?" | Orientation | Show category skills as entry points |
| "What skill should I use for X?" | Skill discovery | Classify their X, recommend category |
| "What's the difference between X and Y?" | Comparison | Explain the difference |
| "How do I use X?" | Usage guidance | Explain the skill |
| "What skills are available?" | Full listing | Point to skills directory |
| "What's new?" | Recent changes | → /wn |
| "Make me a skill for X" | Skill creation | → /cs or /mts |
| "Does a skill exist for X?" | Skill lookup | → /dtse |
| "What skill is best for X?" | Skill selection | → /wsib |
| "What skills should I run?" | Skill sequencing | → /fonss |
| "Rank skills for my goal" | Skill ranking | → /given |
| "I'm not sure what I need" | Uncertainty classification | → /nsa |
| "In this prompt, what's happening?" | Prompt decomposition | → /itp |

### 2. Can We Infer What They Actually Need?

- **"Help" with prior conversation context**: route based on what they were working on.
- **"Help" with no context**: ask what they're trying to do, then route to the appropriate category skill.
- **Explicit meta-question**: answer directly.

### 3. Route by Category

If the user describes a problem and asks for help, classify it:

| User describes... | Route to |
|------------------|----------|
| Something they think is true/false | → /claim |
| A choice to make | → /decide |
| Something broken or wrong | → /diagnose |
| Wanting to explore options | → /search |
| Knowing what but not how | → /how |
| A want or goal | → /want |
| Asking what to do next | → /next |
| Asking which skills to run next (multiple) | → /fonss |
| Asking to rank skills by ROI for a goal | → /given |
| Asking what skill is best right now | → /wsib |
| Asking to reorder an existing list | → /ro |
| Asking to build a high-quality list | → /list |
| Asking to create or update a skill | → /cs |
| Asking to design a skill-creation system | → /sc |
| Asking whether a skill exists | → /dtse |
| Asking to make a new skill directly | → /mts |
| Asking to formalize a new skill spec | → /fmtsb |
| Asking what a skill is useful for | → /uf |
| Starting with "I think..." | → /it |
| Framing with "..., but ..." | → /but |
| Asking to extract all useful skills from a prompt | → /extract |
| Asking to "handle this" broadly | → /handle |
| Asking for "and then also" tasks | → /ata |
| Asking to expand implications ("so you can see") | → /sycs |
| Asking to continue a pattern ("and so on") | → /aso |
| Saying "I'm getting carried away" | → /iagca |
| Asking to operationalize a platitude | → /platitude |
| Asking to reconcile multiple platitudes | → /platitudes |
| Asking to expand an "etc" list | → /etc |
| Asking timeline orientation / what is new | → /wn |
| Asking to extract a repeatable pattern from recent behavior | → /flhwijd |
| Asking "I'm not sure about X" | → /nsa |
| Asking to decompose a prompt | → /itp |
| Asking about scope limits | → /awtlytrn |
| Asking about ideation overflow | → /ycshikfmif |
| Asking to find unresolved decisions | → /tbd |
| Asking to sequence unresolved decisions | → /tobd |
| Asking to reframe something | → /iaw |
| Asking for easy mode | → /ezy |
| Asking for hard mode | → /hrd |
| Asking for general principles | → /genl |
| Asking for specific application | → /spcf |
| Asking for sophisticated analysis | → /soph |
| Asking for ethical analysis | → /eth |
| Asking for safety analysis | → /saf |
| Asking for future analysis | → /fut |
| Asking about best-case scenario | → /utp |
| Asking about worst-case scenario | → /dys |
| Asking about good outcomes | → /gop |
| Asking about bad outcomes | → /obo |
| Asking about obvious things | → /obv |
| Asking about good outcomes being missed | → /ogo |
| Asking for self-deception check | → /sdc |
| Asking for effort calibration | → /ecal |
| Asking to recover from wrong model | → /rmm |
| Asking to identify the situation | → /sid |
| Asking to convert knowledge to action | → /kta |
| Asking about differences between things | → /difr |
| Asking for a story or narrative | → /story |
| Asking for dominance analysis | → /dom |
| Asking for argument analysis | → /agsk |
| Asking for A/B test design | → /abts |
| Asking for debate format | → /deb |
| Something to do/execute | → /action |
| Something to assess/review | → /evaluate |
| A feeling or frustration | → /emotion |
| An idea or proposal | → /viability |
| Content to produce | → /create |
| A domain-specific question | → /technical |
| A problem to analyze | → /analyze |

---

## Category Skills Quick Reference

| Skill | For when you... | Mode |
|-------|----------------|------|
| `/claim` | Have something that might be true or false | ARAW |
| `/decide` | Need to choose between options | ARAW |
| `/viability` | Have an idea to test | ARAW |
| `/evaluate` | Have work to assess | ARAW |
| `/diagnose` | Need to find why something's wrong | UAUA |
| `/search` | Want to explore a space | UAUA |
| `/how` | Know what but not how | AR-forward |
| `/want` | Have a goal or desire | AR-forward |
| `/next` | Need the single highest-value next step | Router |
| `/fonss` | Need an ordered sequence of next skills | Router |
| `/given` | Need ROI-ranked skills for a specific goal | Ranking |
| `/wsib` | Need best single skill selection now | Skill Selection |
| `/ro` | Need an expert reorder of an existing list | Ordering |
| `/list` | Need a high-quality list with rationale | Listing |
| `/cs` | Need to create/update a skill or find missing ones | Skill Design |
| `/sc` | Need to design a skill-creation system | Skill Operations |
| `/dtse` | Need to check if a skill exists and what to do next | Skill Lookup |
| `/mts` | Need to make a new skill draft quickly | Skill Drafting |
| `/fmtsb` | Need a formalized skill spec and rollout plan | Skill Formalization |
| `/uf` | Need use-cases and limits for a skill | Skill Analysis |
| `/it` | Need to formalize an \"I think\" claim | Claim Framing |
| `/but` | Need to resolve claim-objection tension | Tension Handling |
| `/extract` | Need all useful skills extracted from a prompt | Skill Extraction |
| `/handle` | Need broad situation handling collapsed to action | Execution Routing |
| `/ata` | Need implied adjacent tasks added and ordered | Scope Expansion |
| `/sycs` | Need implication expansion | Reasoning Expansion |
| `/aso` | Need bounded pattern continuation | Pattern Expansion |
| `/iagca` | Need scope compression from idea sprawl | Focus Control |
| `/platitude` | Need one platitude turned into action rules | Operationalization |
| `/platitudes` | Need multiple platitudes reconciled | Conflict Resolution |
| `/etc` | Need an \"etc\" tail expanded explicitly | Enumeration |
| `/wn` | Need timeline orientation by new items | Timeline |
| `/flhwijd` | Need to convert recent behavior into a reusable procedure | Pattern Capture |
| `/emotion` | Feel stuck/frustrated/overwhelmed | AR-forward |
| `/action` | Need something executed | Direct |
| `/create` | Need content produced | Direct |
| `/certainty` | Want maximum effort until fully resolved | Maximum |
| `/iterate` | Have something to improve | Meta-iteration |

### Depth and Mode Skills

| Skill | For when you... | Effect |
|-------|----------------|--------|
| `/ezy` | Need the simplest possible path | Breaks problem into easiest steps |
| `/hrd` | Need maximum rigor, no shortcuts | Every assumption surfaced, every edge case |
| `/genl` | Need general principles | Extracts transferable patterns |
| `/spcf` | Need specific application | Applies a principle to exact situation |
| `/soph` | Need multi-layered sophistication | Cross-domain synthesis, second-order effects |
| `/ecal` | Need to calibrate effort | Maps stakes to effort level |

### Analysis and Projection Skills

| Skill | For when you... | Effect |
|-------|----------------|--------|
| `/eth` | Need ethical/moral analysis | Multi-framework ethical evaluation |
| `/saf` | Need safety analysis | Risk identification, protective measures |
| `/fut` | Need future projections | Multi-timeframe trend analysis |
| `/utp` | Need best-case scenario | Utopia construction and path |
| `/dys` | Need worst-case scenario | Dystopia construction and prevention |
| `/gop` | Need good outcome identification | Good outcome maximization |
| `/obo` | Need obvious bad outcomes checked | Catches ignored downsides |
| `/ogo` | Need obvious good outcomes checked | Catches missed upsides |
| `/obv` | Need obvious things checked first | Catches what everyone assumes someone checked |
| `/dom` | Need to eliminate dominated options | Strict dominance filtering |
| `/difr` | Need to differentiate similar things | Classifies differences by significance |
| `/agsk` | Need argument analysis | Checks logical validity and evidence |
| `/abts` | Need experiment design | A/B test with proper controls |
| `/deb` | Need debate format | Steelmans both sides |
| `/story` | Need a narrative | Creates illustrative stories |

### Self-Check Skills

| Skill | For when you... | Effect |
|-------|----------------|--------|
| `/sdc` | Need self-deception check | Detects motivated reasoning |
| `/sid` | Need to identify the actual situation | Prevents solving wrong problem |
| `/rmm` | Need to recover from wrong mental model | Dismantles and replaces broken models |
| `/kta` | Know what to do but can't start | Diagnoses execution barriers |

### Scope and Task Skills

| Skill | For when you... | Effect |
|-------|----------------|--------|
| `/iagca` | Are getting carried away | Compresses scope to essentials |
| `/ycshikfmif` | Keep finding more ideas | Structures ideation into batches |
| `/awtlytrn` | Need to know current limits | Estimates practical boundaries |
| `/ata` | Need adjacent tasks identified | Surfaces implied prerequisites/follow-ups |
| `/tbd` | Have unresolved decisions | Converts TBDs to explicit questions |
| `/tobd` | Need to sequence TBD resolutions | Dependency-ordered resolution path |

---

## Execute

Answer the meta-question directly, or route to the appropriate category skill.

For orientation ("help" / "what can you do?"), present the category skills table above.

For skill discovery, use:
- → /wsib — to find the single best skill for a situation
- → /fonss — to find an ordered sequence of skills
- → /given — to rank skills by ROI for a goal
- → /dtse — to check if a specific skill exists
- → /uf — to understand what a skill is useful for
- → /extract — to find all skills relevant to a prompt

---

## Integration

- **Use from**: Any situation where the user is lost, confused, or asking about the toolkit itself
- **Routes to**: All category skills, all skill discovery skills (/wsib, /fonss, /given, /dtse, /uf, /extract), all depth/mode skills (/ezy, /hrd, /genl, /spcf, /soph)
- **Differs from**: /handle (meta is informational, handle is action-oriented), /next (meta orients, next selects the best immediate action)
- **Complementary**: /wsib (meta shows options, wsib picks the best one), /fonss (meta orients, fonss sequences next skills)
