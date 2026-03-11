# /boc Am I settling on "Claude Code plugin" as the distribution method when something better exists?
**Date:** 2026-03-09
**Skill:** /boc (Better Option Check)

---

## BETTER OPTION CHECK

**Interpretation selected: Option expansion** — You have a working distribution method and want to discover options you haven't considered before committing further.

---

### Step 1: Current Choice

```
USER'S CURRENT CHOICE: Claude Code plugin (slash-command skills via SKILL.md files)

Evidence of commitment:
├── Stated directly: "reasoningtool is currently distributed as a Claude Code plugin"
├── Implied by behavior: 592 skills built in this format, website built, marketplace.json exists
├── Assumed by default: Deep investment in the SKILL.md → slash-command architecture
└── Commitment level: DECIDED (heavy investment, but questioning — healthy sign)

Why this choice:
├── Native integration with Claude Code CLI
├── Skills as markdown files = easy to author and version
├── Slash-command UX is low-friction for users already in Claude Code
└── Unknown: whether alternatives were evaluated before committing
```

---

### Step 2: Extract Preferences from Choice

| Inferred Preference | How Inferred | Strength |
|--------------------|--------------|----------|
| **Claude ecosystem alignment** | Built specifically for Claude Code | STRONG |
| **Low-friction authoring** | Skills are markdown files, not code | STRONG |
| **Solo-maintainable** | One developer, 592 skills — needs to scale without a team | STRONG |
| **Structured reasoning over chat** | Skills are procedures, not prompts | STRONG |
| **User triggers explicitly** | Slash-command pattern = user-initiated | WEAK |
| **No infrastructure dependency** | Files on disk, no server needed for core | STRONG |
| **Composability** | Skills chain via INVOKE | STRONG |

---

### Step 3: Full Option Space

```
OPTION SPACE FOR: Distribution methods for a library of 592 structured reasoning skills

Commonly Known Options:
├── 1. Claude Code plugin (current) — slash commands via SKILL.md
├── 2. ChatGPT Custom GPT — each skill or skill-group as a GPT
├── 3. OpenAI GPT Actions / Assistants API — skills as tool definitions
├── 4. System prompt injection — paste skills into system prompts
├── 5. VS Code extension — skills as code actions or commands
├── 6. Web app (standalone) — interactive skill runner in the browser

Less Known Options:
├── 7. MCP Server (Model Context Protocol) — skills as MCP tools/resources, works across Claude, Cursor, Windsurf, etc.
├── 8. Cursor Rules / .cursorrules — similar to Claude Code but for Cursor users
├── 9. Windsurf Rules — same pattern for Windsurf IDE
├── 10. GitHub Copilot Extensions — skills as Copilot chat participants
├── 11. CLAUDE.md-only (no plugin) — just ship the CLAUDE.md with skill routing, users clone the repo
├── 12. npm package / CLI tool — `npx reasoningtool decide "should I..."`

Hybrid Options:
├── 13. MCP Server + Claude Code plugin — MCP for cross-platform, plugin for native UX
├── 14. Multi-IDE rules files — ship .cursorrules, CLAUDE.md, .windsurfrules from same source
├── 15. Web app + API — browser UI for non-developers, API for integrations
├── 16. Browser extension — inject skills into any LLM web interface (Claude.ai, ChatGPT, etc.)

Non-Obvious Options:
├── 17. LLM-agnostic prompt library (YAML/JSON) — structured format any tool can consume
├── 18. Obsidian plugin — reasoning skills inside a knowledge management tool
├── 19. Raycast / Alfred extension — OS-level skill invocation
├── 20. Discord/Slack bot — team-oriented skill access
├── 21. Prompt marketplace listings — list on PromptBase, FlowGPT, etc.
├── 22. Documentation site with copy-paste — website IS the distribution (you partially have this)

Options User Likely Doesn't Know About:
├── 23. OpenRouter / LiteLLM middleware — skills as middleware that works with any model
├── 24. Langchain / LangGraph tool definitions — skills as agent tools
├── 25. Custom LSP (Language Server Protocol) — skills as IDE-agnostic completions
├── 26. Bookmarklet / userscript — inject skill UI into any web chat interface

TOTAL: 26 options generated
```

---

### Step 4: Score All Options Against Preferences

Preferences:
- P1: Claude ecosystem alignment
- P2: Low-friction authoring (markdown-based)
- P3: Solo-maintainable at 592+ skills
- P4: Structured reasoning (not just prompts)
- P5: No heavy infrastructure
- P6: Composability (skill chaining)
- P7: Broad reach / addressable market

| Option | P1 | P2 | P3 | P4 | P5 | P6 | P7 | Total | Rank |
|--------|----|----|----|----|----|----|-----|-------|------|
| 1. Claude Code plugin (current) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | 6/7 | 2 |
| 7. MCP Server | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | 6.5/7 | 1 |
| 11. CLAUDE.md-only (no plugin) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | 6/7 | 2 |
| 13. MCP + Claude Code hybrid | ✓ | ~ | ~ | ✓ | ✓ | ✓ | ✓ | 5.5/7 | 4 |
| 14. Multi-IDE rules files | ~ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | 5.5/7 | 4 |
| 6. Web app (standalone) | ✗ | ✗ | ~ | ✓ | ✗ | ~ | ✓ | 2.5/7 | 10 |
| 17. LLM-agnostic prompt library | ✗ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | 5.5/7 | 4 |
| 2. ChatGPT Custom GPT | ✗ | ✗ | ✗ | ~ | ✓ | ✗ | ✓ | 2/7 | 11 |
| 8. Cursor Rules | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | 5/7 | 7 |
| 12. npm CLI | ✗ | ~ | ✓ | ✓ | ✓ | ✓ | ~ | 4.5/7 | 8 |
| 16. Browser extension | ✗ | ✗ | ✗ | ✓ | ~ | ~ | ✓ | 2.5/7 | 10 |
| 18. Obsidian plugin | ✗ | ✓ | ~ | ✓ | ✓ | ~ | ~ | 3.5/7 | 9 |
| 22. Docs site (copy-paste) | ✗ | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | 4/7 | 8 |

---

### Step 5: Options That Rank Higher

```
OPTIONS THAT RANK HIGHER THAN CURRENT CHOICE:

1. MCP Server (Model Context Protocol)
   Score: 6.5/7 vs current 6/7
   Better because: MCP is THE emerging standard for tool integration across AI IDEs.
   A single MCP server makes your 592 skills available in Claude Code, Claude Desktop,
   Cursor, Windsurf, Cline, Continue, and any future MCP-compatible client — without
   maintaining separate integrations for each. Your skills become tools/resources that
   any client can discover and invoke. Skill chaining works via tool-call sequencing.
   Markdown authoring is preserved (MCP server reads the same SKILL.md files).
   Why user might not have considered: MCP ecosystem matured significantly in late 2025
   and early 2026. The plugin format predates widespread MCP adoption. The current
   architecture is VERY close to what an MCP server would need — the gap is small.
```

Only one option scored strictly higher. The current choice is strong.

---

### Step 6: Why User May Be Settling

| Reason for Suboptimal Choice | Evidence | Addressable? |
|------------------------------|----------|--------------|
| **Status quo bias** | Heavy investment in current format (592 skills) | YES — migration cost is low because SKILL.md files don't change |
| **Satisficing (first viable)** | Claude Code plugin was the natural starting point | YES — show that MCP expands reach without losing anything |
| **Assumed constraint: "Claude-only is fine"** | Built for Claude ecosystem | YES — MCP IS the Claude ecosystem AND other ecosystems |
| **Didn't realize MCP matured** | Plugin format may predate MCP's practical readiness | YES — inform |
| **Actually near-optimal** | The format IS good; the question is reach, not quality | PARTIALLY — current choice is 6/7, not fundamentally wrong |

---

### Step 7: Before You Commit

```
## BEFORE COMMITTING TO: Claude Code Plugin as sole distribution method

### Options That Match Your Preferences Better

1. **MCP Server**
   - Matches: Claude alignment, solo-maintainable, structured reasoning, no heavy infra, composability, AND broad reach
   - Why you might not have considered it: Your plugin predates MCP's maturity. MCP servers feel like "building infrastructure" but a simple MCP server that reads your existing SKILL.md files is ~200 lines of code.
   - Compared to your current choice: Identical developer experience (markdown skills, same file structure). But users on Cursor, Windsurf, Claude Desktop, and other MCP clients can now access your skills — not just Claude Code CLI users.
   - Worth exploring if: You want reach beyond Claude Code without maintaining multiple integrations.

2. **Multi-IDE Rules (CLAUDE.md + .cursorrules + .windsurfrules)**
   - Matches: Low-friction authoring, solo-maintainable, structured reasoning, no infra
   - Why you might not have considered it: Feels like "just copying files" — but it's the lowest-effort way to reach Cursor/Windsurf users TODAY.
   - Compared to your current choice: Zero new code. Generate .cursorrules and .windsurfrules from existing CLAUDE.md. Users clone repo and get skills in their IDE.
   - Worth exploring if: You want quick wins before building an MCP server.

3. **LLM-Agnostic Prompt Library (structured YAML/JSON)**
   - Matches: Solo-maintainable, structured, no infra, composable, broad reach
   - Why you might not have considered it: Feels like "losing the Claude Code integration." But this is about having a canonical format that GENERATES Claude Code plugins, MCP servers, Cursor rules, etc.
   - Compared to your current choice: Your SKILL.md files are ALREADY almost this. A build step that reads SKILL.md and outputs multiple formats gives you every distribution channel from one source.
   - Worth exploring if: You want a "write once, distribute everywhere" architecture.

### What Your Current Choice Sacrifices

- **Reach** — Claude Code CLI is a narrow audience (developers who use Claude Code specifically)
- **Platform resilience** — if Anthropic changes the plugin format, you're locked in
- **Non-developer access** — your website partially addresses this, but skills can't be invoked from the site

### Recommendation

EXPLORE_ALTERNATIVES

Reason: Your current choice scores 6/7 — it's genuinely good. But MCP Server scores 6.5/7 by adding broad reach while preserving everything you already have. The migration cost is LOW because your SKILL.md files don't change — you'd be adding a thin MCP layer on top of the existing file structure. This isn't "start over," it's "add a front door."
```

---

### Step 8: Prioritized Alternatives

| Priority | Option | Why Prioritized |
|----------|--------|-----------------|
| 1 | **MCP Server** | Highest preference match (6.5/7), adds the one thing you're missing (reach), low migration cost, future-proof |
| 2 | **Multi-IDE rules files** | Zero-cost quick win you could do this week, expands to Cursor/Windsurf users |
| 3 | **LLM-agnostic source format** | Strategic architecture choice — "build once, distribute to all" — but higher effort, do later |

---

## Summary Verdict

**You're not settling badly — but you are leaving reach on the table.**

Your Claude Code plugin is a 6/7 match for your preferences. The SKILL.md format, slash-command UX, and composability are genuinely strong choices. The one gap is **reach**: you're locked to Claude Code CLI users.

**The move is not to abandon the plugin — it's to add MCP as a parallel distribution layer.** Your 592 SKILL.md files don't change. You build a thin MCP server (~200 lines) that exposes them as tools. Suddenly your skills work in Claude Code, Claude Desktop, Cursor, Windsurf, Cline, and every future MCP client.

The architecture would be:
```
SKILL.md files (source of truth, unchanged)
  ├── Claude Code plugin (current, keep it)
  ├── MCP Server (new, ~200 lines, reads same files)
  ├── .cursorrules / .windsurfrules (generated, free reach)
  └── Website (existing, for discovery)
```

**Recommendation: EXPLORE_ALTERNATIVES** — specifically, prototype an MCP server that reads your existing SKILL.md files. You'll know within a day whether the reach gain justifies the small effort.

---

*Execution checklist:*
- [x] Current choice identified with commitment level
- [x] Preferences extracted from choice
- [x] 26 options generated in full space
- [x] All viable options scored against preferences
- [x] Better options identified
- [x] Reasons for suboptimal choice analyzed
- [x] Top 3 alternatives prioritized
- [x] Recommendation generated
