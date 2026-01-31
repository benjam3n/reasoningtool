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
| Something to do/execute | → /action |
| Something to assess/review | → /evaluate |
| A feeling or frustration | → /emotion |
| An idea or proposal | → /viability |
| Content to produce | → /create |
| A domain-specific question | → /technical |
| A problem to analyze | → /analysis |

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
| `/emotion` | Feel stuck/frustrated/overwhelmed | AR-forward |
| `/action` | Need something executed | Direct |
| `/create` | Need content produced | Direct |
| `/certainty` | Want maximum effort until fully resolved | Maximum |

---

## Execute

Answer the meta-question directly, or route to the appropriate category skill.

For orientation ("help" / "what can you do?"), present the category skills table above.
