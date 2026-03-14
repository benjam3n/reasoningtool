---
name: "qr - Question Route"
description: "Map any question to the nearest node in the 438-question graph, show connected questions by route type, and suggest reasoning skills that match."
output:
  format: "prose"
---

# Question Route

**Input**: $ARGUMENTS

---

## Core Principles

1. **Questions have structure.** Every question has a semantic type (identity, causation, obligation, method, etc.), an abstraction level (L0 concrete to L4 philosophical), and connections to other questions through typed routes. This skill makes that structure visible.

2. **The question graph is a thinking map, not a quiz.** The 438 question nodes are not trivia — they are the fundamental forms that all questions take. "Should I quit my job?" is an instance of "Should?" (obligation, L4) made concrete. Mapping to the graph reveals the deeper structure of what the user is really asking.

3. **Routes are thinking directions.** Each route type (prerequisite, implication, clarification, expansion, opposition, composition, analogy, causal, negation, concretization, contradiction, domain-crossing) represents a way to move through a question space. Offering these routes is offering the user ways to think more deeply, not just related trivia.

4. **Match abstraction level to the user.** If the user asks a concrete question (L0-L1), show concrete follow-up directions. If the user asks an abstract question (L3-L4), show abstract follow-ups. Do not offer L4 philosophical routes to someone debugging an error.

5. **Skills and questions are two lenses on the same problem.** The question graph shows WHAT to think about. The skill system shows HOW to think about it. This skill bridges the two.

---

## Phase 1: Parse the Question

```
[Q1] USER_QUESTION: [the question as stated]
[Q2] QUESTION_CORE: [the essential question, stripped of context and specifics]
[Q3] SEMANTIC_TYPE: [identity | causation | obligation | method | possibility | existence | value | epistemic | temporal | spatial | relational | modal | quantitative | comparative]
[Q4] ABSTRACTION_LEVEL: [L0 concrete | L1 category | L2 pattern | L3 principle | L4 philosophical]
```

### Semantic Type Guide

| Type | Signal words | Example |
|------|-------------|---------|
| identity | what, which, who | "What is this?" |
| causation | why, because, cause | "Why does this happen?" |
| obligation | should, must, ought | "Should I do this?" |
| method | how, by what means | "How do I fix this?" |
| possibility | can, could, able | "Can this work?" |
| existence | is, real, true | "Is this real?" |
| value | good, bad, worth, better | "Is this worth it?" |
| epistemic | know, sure, certain, true | "How do I know this is true?" |
| temporal | when, before, after, still | "When is the right time?" |
| spatial | where, here, there | "Where does this belong?" |
| relational | between, with, together | "What's the relationship?" |
| modal | might, would, if | "What if this happened?" |
| quantitative | how much, enough, many | "How much is enough?" |
| comparative | better, worse, same, different | "Is this better?" |

---

## Phase 2: Find Nearest Question Node

Read the question data files from: `/home/ben/Documents/projects/questionroute/data/questions/`

Each file is a JSON object with: `id`, `text`, `definition`, `semanticType`, `abstractionLevel`, `tags`.

### Matching procedure:

1. **Keyword extraction**: Extract the core keyword(s) from the user's question. Many question nodes are named by their core word (e.g., `should.json`, `why.json`, `enough.json`, `better.json`, `fair.json`). Check if any node ID directly matches a keyword in the question.

2. **Semantic type match**: Find all question nodes whose `semanticType` matches [Q3].

3. **Tag overlap**: Among matches, rank by how many of the node's `tags` relate to the user's question.

4. **Abstraction proximity**: Prefer nodes whose `abstractionLevel` is close to [Q4]. A concrete question (L0) should map to a concrete node if possible; an abstract question (L4) should map to an abstract node.

5. **Definition fit**: Read the `definition` field of top candidates. Select the node whose definition most closely captures what the user is asking.

```
[Q5] NEAREST_NODE: [node id]
[Q6] NODE_TEXT: [the question text from the node, e.g., "Should?"]
[Q7] NODE_DEFINITION: [the node's definition]
[Q8] NODE_SEMANTIC_TYPE: [the node's semanticType]
[Q9] NODE_ABSTRACTION: L[0-4]
[Q10] MATCH_QUALITY: [strong | moderate | weak]
[Q11] MATCH_REASONING: [why this node was selected]
```

If MATCH_QUALITY is weak, also identify a second candidate:
```
[Q12] SECONDARY_NODE: [node id]
[Q13] SECONDARY_REASONING: [why this might also fit]
```

---

## Phase 3: Retrieve Connected Questions

Read the route file from: `/home/ben/Documents/projects/questionroute/data/routes/[nearest_node_id].json`

Each route file contains a `sourceId` and an array of `routes`, each with: `targetId`, `type`, `reason`, `weight`.

Organize the routes by type:

```
QUESTION MAP
============

Your question: [user's question]
Nearest node: [node text] — [node definition]

CONNECTED QUESTIONS (by route type):
```

### Route Type Presentation

For each route type found, present it with its thinking direction:

| Route type | Thinking direction | Present as |
|------------|-------------------|------------|
| **prerequisite** | "Before you can answer that, you need to answer..." | PREREQUISITE |
| **implication** | "If that's true/answered, then it follows that..." | IMPLICATION |
| **clarification** | "A more precise version of your question is..." | CLARIFICATION |
| **expansion** | "A broader version of your question is..." | EXPANSION |
| **opposition** | "The strongest counterposition is..." | OPPOSITION |
| **composition** | "This question is composed of these sub-questions..." | COMPOSITION |
| **analogy** | "A structurally similar question in another domain is..." | ANALOGY |
| **causal** | "The cause/effect version of this question is..." | CAUSAL |
| **negation** | "The negation of this question is..." | NEGATION |
| **concretization** | "A more concrete version is..." | CONCRETIZATION |
| **contradiction** | "This question contradicts..." | CONTRADICTION |
| **domain-crossing** | "This question crosses into..." | DOMAIN-CROSSING |

For each route found, read the target question's JSON from `/home/ben/Documents/projects/questionroute/data/questions/[targetId].json` to get its `text` and `definition`, then present:

```
[ROUTE_TYPE]: "[target question text]" — [target definition]
  Route reason: [reason from route data]
  Weight: [high | medium | low]
```

### Prioritization

- Show HIGH weight routes first within each type
- Show at most 2-3 route types (the most relevant to the user's apparent need)
- Prioritize route types based on abstraction level:
  - L0-L1 questions: prioritize prerequisite, clarification, concretization
  - L2-L3 questions: prioritize implication, composition, expansion
  - L4 questions: prioritize opposition, analogy, domain-crossing

---

## Phase 4: Check for Chains and Sequences

Check if the nearest node appears in any chain files at: `/home/ben/Documents/projects/questionroute/data/chains/`
Check if it appears in any sequence files at: `/home/ben/Documents/projects/questionroute/data/sequences/`

Search for the node's `id` in chain and sequence JSON files. Chains are named descriptively (e.g., `should-you-really.json`, `is-it-worth-it.json`) and contain ordered sequences of question nodes forming a line of inquiry.

If found:
```
CHAINS CONTAINING THIS QUESTION:
  - [chain name]: [brief description of the chain's arc]

SEQUENCES CONTAINING THIS QUESTION:
  - [sequence name]: [brief description of the sequence]
```

These provide larger narrative structures that the user's question fits into — not just adjacent questions, but entire lines of inquiry.

---

## Phase 5: Suggest Reasoning Skills

Based on the semantic type, abstraction level, and what the user appears to need, suggest 2-4 reasoning skills from the reasoningtool at `/home/ben/Documents/projects/reasoningtool/claude-code-plugin/skills/`.

### Mapping: Semantic Type to Skills

| Semantic type | Primary skills | Why |
|--------------|---------------|-----|
| identity | `/se` (enumerate), `/dcm` (decompose) | Understanding what something IS requires mapping its components |
| causation | `/rca` (root cause), `/sycs` (consequences) | Causation needs causal analysis tools |
| obligation | `/decide`, `/eth` (ethics), `/dcp` (decision criteria) | Obligation questions are decision-adjacent |
| method | `/how`, `/stg` (step generation), `/foht` (method discovery) | Method questions need procedural tools |
| possibility | `/viability`, `/fla` (failure anticipation) | Possibility needs feasibility testing |
| existence | `/araw` (assume right/wrong), `/it` (formalize belief) | Existence claims need truth-testing |
| value | `/cmp` (compare), `/cba` (cost-benefit) | Value questions need comparative tools |
| epistemic | `/nsa` (classify uncertainty), `/aex` (assumption extraction) | Epistemic questions need uncertainty tools |
| temporal | `/fut` (future analysis), `/prm` (pre-mortem) | Temporal questions need forecasting tools |
| spatial | `/sya` (systems analysis), `/insd` (inside look) | Spatial questions need structural tools |
| relational | `/col` (collaborate), `/per` (perspective) | Relational questions need multi-perspective tools |
| modal | `/gg` (guess generation), `/pbr` (probabilistic reasoning) | Modal questions need possibility-space tools |
| quantitative | `/ecal` (effort calibration), `/alt` (abstraction level) | Quantitative questions need scaling tools |
| comparative | `/cmp` (compare), `/dom` (dominance) | Comparative questions need comparison tools |

### Abstraction Level Skill Adjustment

| Abstraction | Skill bias | Rationale |
|-------------|-----------|-----------|
| L0-L1 | Procedural skills (`/stg`, `/how`, `/action`) | Concrete questions need concrete procedures |
| L2 | Analytical skills (`/araw`, `/dcm`, `/se`) | Pattern-level questions need analytical tools |
| L3 | Framework skills (`/soph`, `/dd`, `/sya`) | Principle-level questions need structural tools |
| L4 | Exploratory skills (`/uaua`, `/iaw`, `/per`) | Philosophical questions need multi-perspective tools |

```
SUGGESTED SKILLS:
  1. /[skill] — [one-line reason why this skill matches the question]
  2. /[skill] — [one-line reason]
  3. /[skill] — [one-line reason] (if applicable)

To use a skill: type /[skill] followed by your question.
```

---

## Phase 6: Output

```
QUESTION ROUTE
==============

YOUR QUESTION: [user's question]
CORE FORM: [stripped-down essential question]
SEMANTIC TYPE: [type] | ABSTRACTION: L[0-4]

NEAREST NODE: "[node text]" — [definition]
  Match quality: [strong | moderate | weak]

CONNECTED QUESTIONS:
  [ROUTE_TYPE]: "[target text]" — [reason]
  [ROUTE_TYPE]: "[target text]" — [reason]
  [ROUTE_TYPE]: "[target text]" — [reason]
  (showing top 3-6 most relevant connections)

[If chains/sequences found:]
PART OF:
  Chain: [chain name] — [arc description]
  Sequence: [sequence name] — [sequence description]

THINKING TOOLS:
  /[skill] — [why it matches]
  /[skill] — [why it matches]
  /[skill] — [why it matches]

NEXT MOVES:
  - To go deeper: /qr [pick a connected question from above]
  - To analyze: /[suggested skill] [your question]
  - To auto-route: /auto [your question]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Forced mapping** | User's question mapped to a node that doesn't genuinely relate | If match quality is weak, say so. Offer the secondary node. Don't force a bad match |
| **Abstraction mismatch** | Concrete question gets L4 philosophical routes | Filter connected questions by abstraction proximity |
| **Route overload** | All 6+ routes shown, overwhelming the user | Show 3-5 most relevant. Prioritize by weight and abstraction match |
| **Skill spam** | 6+ skills suggested with no clear recommendation | Suggest 2-4 max. Lead with the single best match |
| **Graph navel-gazing** | Spending so long mapping the question that the question itself goes unanswered | The map is a tool, not the answer. After presenting the map, suggest the user pick a direction or invoke a skill |
| **Missing route data** | Route file doesn't exist for the matched node | Say "No route data found for this node" and skip to Phase 5 (skill suggestions) |
| **Overwriting the user's question** | Presenting the abstract node form and losing the user's specific question | Always show the user's original question alongside the node mapping |

---

## Depth Scaling

| Depth | Node matching | Routes shown | Chains/Sequences | Skills suggested |
|-------|--------------|-------------|-----------------|-----------------|
| 1x | Nearest node only | Top 2-3 by weight | Skip | 1-2 skills |
| 2x | Nearest + secondary | Top 3-5 organized by type | Check chains | 2-3 skills |
| 4x | Nearest + 2 candidates | All routes organized by type | Check chains + sequences | 3-4 skills with rationale |
| 8x | Full semantic neighborhood | All routes + follow target nodes one hop further | Full chain/sequence analysis | Full skill mapping with abstraction adjustment |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] User's question parsed: core form, semantic type, abstraction level identified
- [ ] Nearest question node found with match quality assessed
- [ ] Route file read and connected questions retrieved (with target node definitions looked up)
- [ ] Routes organized by type and prioritized by weight + abstraction match
- [ ] Chains and sequences checked (at 2x+ depth)
- [ ] 2-4 reasoning skills suggested with rationale
- [ ] Output includes clear next moves for the user

---

## Integration

- **Use from**: When the user has a question and wants to see its structure, connections, and analytical options before diving in. Good starting point for abstract or philosophical questions.
- **Routes to**: Any skill suggested in Phase 5. Also chains into itself — the user can `/qr` a connected question to traverse the graph.
- **Differs from `/auto`**: `/auto` classifies and immediately invokes a skill. `/qr` maps the question space and presents options. `/auto` is "do it for me." `/qr` is "show me the landscape."
- **Differs from `/meta`**: `/meta` shows what skills exist. `/qr` shows what questions connect to the user's question and which skills match.
- **Differs from `/search`**: `/search` enumerates a problem space. `/qr` navigates the question graph.
- **Complementary**: `/auto` (after seeing the map, auto-route into the best skill), `/soph` (for L3-L4 questions that need deep structural analysis), `/uaua` (for exploratory traversal of the question space)
