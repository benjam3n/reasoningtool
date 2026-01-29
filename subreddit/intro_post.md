# Welcome to r/reasoningtool

**TL;DR**: This subreddit is about structured reasoning — methods for checking whether you're thinking in the right direction, not just thinking faster. [reasoningtool](https://github.com/benjam3n/reasoningtool) is an open-source implementation of these ideas. The sub is for sharing sessions, skills, improvements, discussion, and challenges to the approach.

---

## The problem

Every AI tool helps you think faster. Agents execute tasks. Chain-of-thought produces better single-shot answers. Prompt libraries give you templates. All of them make you faster at whatever you're already doing.

None of them tell you whether what you're doing is the right thing to be doing.

This is a structural problem, not a prompting problem. If you ask an AI to evaluate your plan, it evaluates your plan. It doesn't ask whether your plan is solving the right problem. If you ask it to brainstorm alternatives, it generates alternatives. It doesn't test whether those alternatives actually survive scrutiny. If you ask it to test your idea, it tests your idea. It doesn't tell you what ideas you never considered.

These aren't failures of intelligence. They're failures of *direction*. The tool does exactly what you asked — but what you asked might be wrong, and the tool has no mechanism to notice.

## What's missing

There are two fundamentally different operations in reasoning:

1. **Exploration**: What options exist? What haven't I considered? What's the full space of possibilities? This is divergent — it expands your view.

2. **Testing**: Is this actually true? What happens if it's wrong? What survives scrutiny? This is convergent — it narrows your view.

Most tools do one or the other. Brainstorming tools explore but don't test. Debate tools test but don't explore. Chain-of-thought does a bit of both but neither systematically. And none of them *alternate* — exploring, then testing what you found, then exploring the edge cases of what survived, then testing again.

The alternation matters because the two operations have structural blind spots that don't overlap. Exploration alone finds options but can't tell you which ones work. Testing alone validates what you're looking at but can't tell you what you're not looking at. Alternating covers both.

This isn't a new philosophical observation. It's related to divergent/convergent thinking in design, generate-and-test in AI search, and Popperian falsification. What's less common is an implementation — actual tools that force the alternation rather than just describing it.

## What reasoningtool does

[reasoningtool](https://github.com/benjam3n/reasoningtool) is an open-source project that implements structured reasoning as 207 skills for Claude Code, plus Python tools for running deeper explorations programmatically.

**The core methods:**

- **ARAW** (Assume Right / Assume Wrong) takes any claim and branches it: what follows if true? what follows if false? Then it recurses — every conclusion is another claim. The result is a tree of tested claims stored in SQLite.

- **UAUA** (Universalize, ARAW, Universalize, ARAW) alternates between mapping the full possibility space and testing what it finds. First pass explores, second pass tests, third pass finds edge cases of survivors, fourth pass validates. Each pass uses a different logic — type enumeration vs. binary elimination — so their blind spots don't overlap.

- **207 structured skills** covering reasoning, analysis, writing, planning, research, decision-making, and more. Skills are classified by universality: Tier 1 skills apply whenever their trigger condition exists (if you have a complex problem, decomposition applies — that follows from what "complex" means). Tier 4 skills depend on context.

**The Python tools** (in `src/`):
- Seed any claim and auto-expand it into a branching ARAW tree using an LLM
- Visualize the tree in an interactive browser viewer — filter by branch type, depth, domain; click any node for details
- Synthesize findings across multiple explorations
- Ground abstract claims in evidence with epistemic quality tracking
- Export to JSON, GEXF, or GOSM-compatible YAML

## How it compares

| | reasoningtool | AI agents (AutoGPT, CrewAI) | Prompt libraries | Chain-of-thought (o1, etc.) |
|---|---|---|---|---|
| Structured exploration | Yes (universalization) | No | No | Implicit |
| Systematic testing | Yes (ARAW) | No | No | Implicit |
| Alternation between both | Yes (UAUA) | No | No | No |
| Persistence across sessions | Yes (SQLite) | Varies | No | No |
| Interactive visualization | Yes (Sigma.js) | No | No | No |
| Cross-run synthesis | Yes | No | No | No |
| Classifies skills by universality | Yes (tiered) | No | Some | No |
| Philosophy of *why* it works | Yes (essays) | No | No | No |

The difference isn't features — someone could add any of these to an existing framework. The difference is *design intent*. Agents are designed to execute tasks. Prompt libraries are designed to produce better outputs. This toolkit is designed to check whether you're solving the right problem before you solve it.

## What's proven and what's claimed

Honest accounting:

**Proven (by the structure itself):**
- If you test both "assume right" and "assume wrong," you will consider alternatives you wouldn't have otherwise. This is logically necessary — the operation forces it.
- If you alternate between exploration and testing, you cover failure modes that either operation alone misses. This follows from the fact that their blind spots are complementary.

**Claimed (based on principles, not yet empirically validated):**
- The alternation produces better decisions than non-alternating methods.
- The universal/heuristic skill classification helps users pick the right tools faster.
- The full UAUA cycle (4 passes) is meaningfully better than a 2-pass version.

This is experimental. The philosophy is grounded in epistemology and information theory. The implementation is v1. We think it works — we want to find out whether it does, and where it breaks.

## What this subreddit is for

This is a place for:

- **Sessions**: Share ARAW or UAUA sessions you've run. What did you explore? What did you find? What surprised you?
- **Skills**: New reasoning skills, improvements to existing ones, proposals for different classifications.
- **Tools**: Python scripts, visualization improvements, export formats, integrations with other platforms.
- **Philosophy**: Discussion of the principles behind structured reasoning. Challenges welcome — if a premise is wrong, we want to know.
- **Comparisons**: How does this compare to other reasoning methods? Where does it do better? Where does it do worse?
- **Applications**: Using the toolkit on real problems — career decisions, technical analysis, research questions, anything where structured reasoning helps.
- **Meta**: How should the toolkit itself be improved? What's missing? What's over-engineered?

## Background reading

Three essays explore the philosophy in depth:

- [Two Kinds of Search, and Why You Need Both](https://github.com/benjam3n/reasoningtool/blob/main/Two%20Kinds%20of%20Search%2C%20and%20Why%20You%20Need%20Both.md) — why alternation between exploration and testing covers blind spots that either alone misses.
- [Universal Principles of Mathematical Problem Solving](https://github.com/benjam3n/reasoningtool/blob/main/Universal%20Principles%20of%20Mathematical%20Problem%20Solving.md) — the distinction between universal principles (entailed by definitions) and heuristics (contingent on context).
- [The Structure of Careful Thought](https://github.com/benjam3n/reasoningtool/blob/main/The%20Structure%20of%20Careful%20Thought.txt) — an earlier essay on asymmetric testing of claims.

## Getting started

```bash
git clone https://github.com/benjam3n/reasoningtool.git
cd reasoningtool/claude-code-plugin
claude
```

Then type `/araw should I change careers` or `/uaua 4x what's the best approach to learning math` or any other question.

For programmatic use (auto-expansion, visualization, synthesis), see `src/README.md`.

## How to contribute

Post here. That's the main thing. Share a session, propose a skill, challenge a premise, show where the toolkit fails. The toolkit gets better when people use it on problems the creator didn't anticipate.

If you want to contribute code, the repo is [here](https://github.com/benjam3n/reasoningtool). Apache 2.0 licensed.

---

Questions, feedback, introductions — put them in the comments.
