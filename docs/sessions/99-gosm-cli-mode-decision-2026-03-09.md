# /gosm Route this through the full analysis chain: "Should reasoningtool have a CLI mode separate from the Claude Code plugin?"
**Date:** 2026-03-09
**Skill:** /gosm (Goal-Oriented State Machine)

---

## Context Assessment

| Factor | Assessment | Rationale |
|--------|-----------|-----------|
| **Urgency** | NORMAL (days+) | No deadline forcing this decision |
| **Stakes** | MEDIUM | Affects distribution reach but doesn't threaten the core project |
| **Expertise** | EXPERT | Solo developer who built the system, understands the architecture |
| **Action Cost** | EXPENSIVE | Significant development effort; once a CLI exists, it creates a maintenance surface that's hard to abandon |
| **Information** | MODERATE | Clear picture of current state; uncertain about actual demand for a CLI |

## Variant Selected: Standard

MEDIUM stakes + NORMAL time + EXPENSIVE action cost warrants balanced analysis. Not urgent enough for Lite, not high-stakes enough for Full. The EXPENSIVE cost pushes toward thoroughness but EXPERT knowledge means we don't need the full procedure engine.

---

## Standard Analysis

### 1. Classify

**DECISION** — Whether to invest development effort in a new distribution channel.

### 2. Key Claims (Surface + Hidden)

1. **Surface claim**: A CLI mode would make reasoningtool accessible to people who don't use Claude Code.
2. **Surface claim**: Building and maintaining a CLI is significant work for a solo developer.
3. **Hidden assumption**: There is a meaningful audience that wants structured thinking skills but doesn't use Claude Code.
4. **Hidden assumption**: The skills would work equally well outside the Claude Code plugin context (where Claude is the executor).

### 3. ARAW the Most Important Claim

The most important claim is #4: **The skills would work equally well outside the Claude Code plugin context.**

**Assume Right (skills work well outside Claude Code):**
- A CLI could pipe skill templates into any LLM (Claude API, local models, GPT, etc.)
- The skills become model-agnostic, which massively expands the audience
- You could also target other integrations: VS Code extensions, web apps, API services
- The SKILL.md files are already plain text procedures — they're inherently portable

**Assume Wrong (skills need Claude Code's execution context):**
- The skills rely on Claude reading the SKILL.md and *executing* it — they're prompts for an AI, not standalone tools
- A CLI that just prints the SKILL.md content is a glorified `cat` command
- To actually be useful, a CLI would need to either: (a) call an LLM API itself, or (b) format the skill as a prompt the user pastes elsewhere
- Option (a) means building an LLM client (API keys, streaming, cost management) — dramatically more scope
- Option (b) is low-value — users could just read the files
- The chaining mechanism (`INVOKE: /procedure_name`) requires an executor that can recursively load and run skills — a CLI would need to replicate this

**Verdict on this claim**: The skills are *prompts for an AI executor*, not standalone procedures. A CLI without an LLM backend would be nearly useless. A CLI with an LLM backend is a fundamentally different product — it's building your own Claude Code competitor.

### 4. Goal Journey

**Current state**: 563 skills distributed as a Claude Code plugin. Users invoke via slash commands. Claude reads and executes the SKILL.md files. Works well within that context.

**Desired state**: Broader accessibility — more people can use the thinking skills.

**What actually serves this goal?**

The goal is broader accessibility. A CLI is one path, but consider what "accessible without Claude Code" actually requires:

- If target users have another LLM tool (Cursor, Aider, etc.) → they need the skill files in a format those tools can consume, not a CLI
- If target users have no LLM tool → they need a full LLM-powered application, which is a massive undertaking
- If target users just want to read the procedures → a website or documentation serves this (and you already have a website)

A CLI is a means, not the end. The end is distribution.

### 5. Contrarian View

**Strongest challenge**: "You're overthinking this. A simple CLI that formats a skill as a prompt and copies it to clipboard — or pipes it to `claude` or `llm` CLI tools — would take a weekend to build and opens up every terminal user. You don't need to build an LLM client. Just be a skill-selector and prompt-formatter. Let the user choose their own executor."

This is actually compelling. A thin CLI that does:
```
rt /gosm "my question" | claude
rt /gosm "my question" | llm
rt /gosm "my question" | pbcopy
```
...would be modest in scope. But it still can't handle skill chaining (INVOKE), which is core to how the deeper skills work.

### 6. Actionable Filter

What can the solo developer actually do?

| Option | Effort | Value | Verdict |
|--------|--------|-------|---------|
| **Full CLI with LLM backend** | Months | High if it works | Too much scope for solo dev |
| **Thin CLI (prompt formatter)** | 1-2 weekends | Moderate — but breaks on chaining | Possible but limited |
| **Publish skills as downloadable prompt library** | Days | Moderate — serves Cursor/Aider users | Low effort, decent reach |
| **Improve existing website** | Days | Serves browsers/learners | Already in progress |
| **Do nothing — focus on skills** | Zero | The skills themselves are the product | Often the right call |

### 7. Crux Question

**"Is there demonstrated demand from people who want to use these skills but can't because they don't have Claude Code?"**

If yes (people are asking for it) → build the thin CLI or prompt library.
If no (speculative) → don't build it. You'd be building distribution for an audience you haven't confirmed exists.

### 8. Recommended Action

**Don't build a CLI right now.** Instead:

1. **Validate demand first.** Add a "Use without Claude Code" section to the website explaining how to use the SKILL.md files manually with any LLM. See if anyone engages with it.
2. **If demand emerges**, build the thinnest possible thing: a prompt-formatter CLI (`rt /skillname "input"` that outputs formatted prompt text). Skip the LLM backend entirely — let users pipe to their own tools.
3. **Protect your time.** The highest-leverage work for a solo developer is writing better skills, not building distribution infrastructure for an unvalidated audience. The 563 skills *are* the moat. A CLI is commodity work anyone could build once the skills exist.

**Verification**: Track whether anyone uses the "Use without Claude Code" documentation. If usage is near-zero after a month, the demand signal is clear: the current audience is Claude Code users, and that's fine.

---

## Pre-Completion Check

- [x] Context assessed (urgency, stakes, expertise, cost, information)
- [x] Variant matches context (Standard for MEDIUM stakes + NORMAL time + EXPENSIVE cost)
- [x] Output depth matches variant (balanced analysis, not exhaustive)
- [x] Specific action recommended (validate demand before building; protect solo dev time)
