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

---

## Execute

Answer the meta-question directly, or route to the appropriate category skill.

For orientation ("help" / "what can you do?"), present the category skills table above.
