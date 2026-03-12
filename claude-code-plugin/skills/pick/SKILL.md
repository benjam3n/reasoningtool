---
name: "pick - Skill Picker"
description: "Pick N skills using a specified algorithm. Supports random, goal-directed, intent-matching, category filtering, useful ranking, question-driven elimination, and freeform semantic search."
tier: "category"
categories: ["Meta & Navigation"]
tags: ["discovery", "selection", "navigation", "meta"]
output:
  format: "prose"
---

# Skill Picker

**Input**: $ARGUMENTS

---

## Purpose

Select exactly N skills from the library using one of several algorithms. Every invocation must specify a count and a selection method. The output is always a concrete, actionable list — not a menu to browse.

---

## Syntax

```
/pick [N] [algorithm] [optional arguments]
```

**Examples:**
- `/pick 10 random`
- `/pick 10 goal achieve AGI`
- `/pick 5 want figure out what I actually want`
- `/pick 10 useful`
- `/pick 7 category Research & Analysis`
- `/pick 5 question me`
- `/pick 3 chain starting from /rca`
- `/pick 10 for I need to launch a product and validate the market`
- `/pick 8 tier core`
- `/pick 10 diverse`
- `/pick 5 deep`
- `/pick 10 complement /araw`

---

## Step 0: Parse Input

Extract from the input:

```
N = [number of skills to return — default 10 if not specified]
ALGORITHM = [one of the algorithms below — infer from phrasing if not explicit]
ARGS = [everything after the algorithm keyword]
```

**Algorithm detection rules:**
- Starts with a number → that's N
- Contains "random" → RANDOM
- Contains "goal" or describes a desired outcome → GOAL
- Contains "want" or "I want" or "figure out" → WANT
- Contains "useful" or "best" or "top" → USEFUL
- Contains "category" or a known category name → CATEGORY
- Contains "tier" or "core" or "experimental" → TIER
- Contains "question" or "ask me" or "interview" → QUESTION
- Contains "chain" or "starting from" or "workflow" → CHAIN
- Contains "for" followed by a situation description → SITUATION
- Contains "diverse" or "coverage" or "spread" → DIVERSE
- Contains "deep" or "thorough" or "exhaustive" → DEEP
- Contains "complement" or "pair with" or "goes with" → COMPLEMENT
- Contains "like" or "similar to" → SIMILAR
- Anything else → SEMANTIC (treat the whole thing as a search query)

---

## Algorithms

### RANDOM
Pick N skills uniformly at random from the full library.

**Procedure:**
1. Load all skill IDs from skills.json
2. Shuffle randomly
3. Take first N
4. For each, show: `id — title — tier — 1-line description`

**Variant:** `random [tier/category]` — constrain the pool first, then pick randomly within it.

---

### GOAL
Pick N skills most likely to help achieve a specific goal.

**Procedure:**
1. Read the goal from ARGS
2. Decompose the goal into 3-5 sub-capabilities needed:
   - What must be UNDERSTOOD? (analysis skills)
   - What must be DECIDED? (decision skills)
   - What must be PLANNED? (planning skills)
   - What must be VALIDATED? (validation skills)
   - What must be CREATED? (creation skills)
   - What could go WRONG? (risk/diagnostic skills)
   - What is UNKNOWN? (exploration skills)
3. For each sub-capability, search skills.json for skills whose description, categories, tags, or title match
4. Score each candidate:
   - **Relevance**: How directly does this skill address a sub-capability? (0-3)
   - **Tier weight**: tier1=3, tier2=2.5, category=2, tier3=2, experimental=1.5, tier4=1
   - **Chain bonus**: +1 if this skill invokes other relevant skills (compound value)
5. Rank by score, take top N
6. Verify coverage: do the N skills cover at least 3 different sub-capabilities? If not, swap lowest-scoring duplicate-capability skills for highest-scoring uncovered capabilities.

**Output:**
```
GOAL: [stated goal]
SUB-CAPABILITIES IDENTIFIED:
  [C1] [capability] — addressed by: [skill IDs]
  [C2] [capability] — addressed by: [skill IDs]
  ...

PICKED [N] SKILLS:
  1. /[id] — [title] — [1-line why this helps with the goal]
     Addresses: [C-numbers] | Tier: [tier] | Invokes: [list or none]
  2. ...

COVERAGE: [X of Y sub-capabilities addressed]
SUGGESTED WORKFLOW: [recommended order to use these skills]
```

---

### WANT
Pick N skills to help someone clarify, explore, or achieve what they want.

**Procedure:**
1. Read the want/desire from ARGS
2. Classify the want:
   - **Vague want** ("figure out what I want") → prioritize: `/gu`, `/ve`, `/pre`, `/grf`, `/wt`, `/dd`, `/pbi`, exploration skills
   - **Directional want** ("I want to be healthier") → prioritize: goal analysis + domain skills
   - **Specific want** ("I want to negotiate a raise") → prioritize: domain + execution skills
3. Build a journey: Discovery → Analysis → Planning → Execution → Validation
4. Pick N skills that cover this journey, weighted toward the phase matching the want's clarity level
5. Score using GOAL algorithm but add a **journey-phase bonus** (+1 for skills matching the appropriate phase)

**Output:** Same format as GOAL but with journey phases instead of sub-capabilities.

---

### USEFUL
Pick the N most generally useful skills.

**Procedure:**
1. Score every skill:
   - **Tier score**: tier1=10, tier2=8, category=7, experimental=6, tier3=4, tier4=2
   - **Connectivity**: count of (invokes + invoked_by) — more connected = more useful
   - **Breadth**: number of non-empty categories/tags — broader = more general
   - **Size**: line_count > 200 = +2, > 100 = +1 (proxy for depth/quality)
2. Rank by composite score
3. Take top N
4. Verify diversity: no more than 3 skills from the same category. Swap duplicates for next-highest from underrepresented categories.

**Output:**
```
TOP [N] MOST USEFUL SKILLS:
  1. /[id] — [title] — Score: [X] (tier=[T], connections=[C], breadth=[B])
     [1-line description]
  2. ...
```

---

### CATEGORY
Pick N skills from a specific category (or matching a category pattern).

**Procedure:**
1. Match ARGS against known categories in skills.json (fuzzy match — "research" matches "Research & Analysis")
2. Filter skills to those in the matched category
3. If more than N, rank by tier score + line_count
4. If fewer than N, include skills from adjacent categories (share tags/invocations with matched category)
5. Take N

---

### TIER
Pick N skills from a specific tier.

**Procedure:**
1. Map ARGS to tier: "core"=tier1, "important"=tier2, "domain"=tier3, "specialized"=tier4, "category"=category, "experimental"=experimental
2. Filter and return N (random if pool > N, all if pool <= N + pad from adjacent tier)

---

### QUESTION
Interactive elimination — ask the user questions to narrow down to N skills.

**Procedure:**
1. Start with the full skill pool
2. Ask 3-5 binary or multiple-choice questions that maximally discriminate:
   - "Are you trying to (a) understand something, (b) decide something, (c) create something, (d) fix something?" → eliminates ~75%
   - "Is this about (a) a specific project, (b) a general capability, (c) a feeling/situation?" → eliminates ~66%
   - "Do you need (a) deep analysis of one thing, or (b) broad coverage of many things?" → eliminates ~50%
   - "What domain? (a) technical, (b) business, (c) personal, (d) any" → eliminates ~75%
   - "How much time do you have? (a) quick answer, (b) thorough analysis, (c) deep dive" → selects tier
3. After each answer, filter the pool
4. From the remaining pool, pick N using USEFUL algorithm
5. Present with explanation of why each survived the elimination

**Output:**
```
QUESTIONS ASKED:
  Q1: [question] → Answer: [answer] → Pool: [X] → [Y] skills
  Q2: ...

PICKED [N] SKILLS (from [final pool size] candidates):
  1. /[id] — [title] — [why this survived all filters]
  ...
```

**Note:** If the user provided arguments after "question me", use those as implicit answers to skip some questions. E.g., `/pick 5 question me about launching a startup` → skip Q1 (create/decide), skip Q4 (business).

---

### CHAIN
Pick N skills that form a workflow chain starting from a given skill.

**Procedure:**
1. Start with the seed skill from ARGS
2. Build outward: add skills this one invokes, then skills THOSE invoke, breadth-first
3. If the chain is shorter than N, add skills that invoke the seed (upstream)
4. If still short, add skills in the same category with complementary functions
5. Order the N skills in execution sequence (dependency-aware)

**Output:**
```
CHAIN STARTING FROM: /[seed]

  Step 1: /[id] — [title] — [what it does in this chain]
    ↓ feeds into
  Step 2: /[id] — [title] — [what it does in this chain]
    ↓ feeds into
  ...

CHAIN LOGIC: [1-sentence explanation of why this sequence]
```

---

### SITUATION
Pick N skills for a described situation (triggered by "for [situation]").

**Procedure:**
1. Read the situation description from ARGS
2. → INVOKE: /gu [situation] (mentally — don't actually invoke, just apply goal understanding logic)
3. Identify: what is the user's actual need? What phase are they in? What domain?
4. Use GOAL algorithm with the inferred goal
5. Add a **situation-awareness bonus**: +2 for skills that explicitly handle the identified phase (planning vs execution vs recovery vs exploration)

---

### DIVERSE
Pick N skills maximizing coverage across different categories, tiers, and functions.

**Procedure:**
1. Group all skills by category
2. Round-robin: pick the highest-tier skill from each category until you have N
3. If fewer categories than N, pick second-best from largest categories
4. Ensure at least: 1 analysis skill, 1 decision skill, 1 planning skill, 1 validation skill, 1 exploration skill

**Output:** List with category diversity metrics.

---

### DEEP
Pick N skills that together provide the most thorough analysis of a topic.

**Procedure:**
1. Start with the deepest analytical skills: `/araw`, `/uaua`, `/certainty`
2. Add skills that feed into deep analysis: `/aex`, `/ht`, `/rca`, `/sya`
3. Add validation skills: `/vbo`, `/val`, `/mv`, `/pv`
4. Fill remaining slots with topic-relevant skills from ARGS (if provided)
5. Order from divergent (exploration) to convergent (validation)

---

### COMPLEMENT
Pick N skills that pair well with a specified skill.

**Procedure:**
1. Read the target skill from ARGS
2. Look up its categories, tags, invokes, and invoked_by
3. Find skills that:
   - Are invoked by or invoke the target (direct connections)
   - Share categories but have different functions (same domain, different angle)
   - Cover the target's gaps (if target is analysis, pick planning/execution)
4. Score by complementarity (different function + same domain > same function + same domain)
5. Take top N

---

### SIMILAR
Pick N skills similar to a specified skill.

**Procedure:**
1. Read the target skill from ARGS
2. Find skills sharing the most categories, tags, and invocation partners
3. Rank by overlap score
4. Take top N

---

### SEMANTIC
Fallback: treat the entire input as a natural language query.

**Procedure:**
1. Read the full query
2. For every skill in the library, score semantic relevance:
   - Title match: +3
   - Description keyword match: +2
   - Tag match: +2
   - Category match: +1
   - Invokes/invoked_by skills that matched: +1 (guilt by association)
3. Rank by score, take top N

---

## Output Format (All Algorithms)

Every output MUST include:

```
ALGORITHM: [which algorithm was used]
POOL: [how many skills were in the candidate pool]
PICKED: [N]

[numbered list with for each skill:]
  [rank]. /[id] — [title]
     [1-line reason this was picked]
     Tier: [tier] | Category: [category] | Lines: [N]

[if applicable:]
SUGGESTED ORDER: [recommended sequence to use them]
COVERAGE: [what aspects/phases are covered]
GAPS: [what's NOT covered by these N skills — suggest what to add]
```

---

## Depth Scaling

| Depth | Min skills scored | Algorithm detail |
|-------|-------------------|-----------------|
| 1x | Score top 3×N candidates | Basic scoring |
| 2x | Score top 5×N candidates | Score + verify each pick against the goal |
| 4x | Score all skills in matching tiers | Score + AR/AW the top 2N, keep survivors |
| 8x | Score entire library | Full AR/AW on top 3N, chain analysis on picks |

Default: 1x

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Popularity bias** | All picks are tier1/tier2 | Force at least 1 pick from tier3+ (hidden gems exist) |
| **Category clustering** | 4+ picks from same category | Swap lowest-scoring duplicates for top uncovered categories |
| **Obvious picks only** | Every skill is one the user probably already knows | Add at least 1 "surprise" pick with explanation of why it's non-obvious |
| **Goal drift** | Picks don't connect back to the stated goal/query | Verify each pick: "How does /X help with [goal]?" — if no clear answer, replace |
| **Chain blindness** | Picks are all leaves with no connections | Include at least 1 compound skill that invokes others |
| **Count mismatch** | Output has fewer/more than N skills | Count before outputting. Exactly N. |

---

## Pre-Completion Check

- [ ] Exactly N skills returned (not N-1, not N+1)
- [ ] Algorithm explicitly stated in output
- [ ] Every pick has a 1-line reason specific to the query (not generic)
- [ ] Category diversity checked (no more than 40% from one category unless category-filtered)
- [ ] At least 1 non-obvious pick included (for N >= 5)
- [ ] Gaps identified (what the picks DON'T cover)
- [ ] Suggested order provided (for goal/want/chain/situation algorithms)

---

## When to Use

- **Use /pick** when you want a curated set of skills for a specific purpose, count, or exploration mode
- **Use /fnd** when you want to find the single best skill for a task
- **Use /meta** when you need orientation on which category to start with
- **Use /wsib** when you need the single best skill for right now

---

## Integration

After running /pick, the user can:
- Run each picked skill in sequence: → INVOKE: /[first-pick] [input]
- Run /pick again with different algorithm for comparison
- Use picks as input to /to (topological ordering) to find optimal execution order
- Use picks as input to /de (dependency extraction) to find what must come first
