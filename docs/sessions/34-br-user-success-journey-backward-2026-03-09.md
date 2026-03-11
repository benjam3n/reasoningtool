# /br From "a user successfully solved their problem using reasoningtool," work backward through every step they took
**Date:** 2026-03-09
**Skill:** /br (Backward Reasoning)

---

## Interpretation Selected

**Interpretation 1 — Reverse-engineer an outcome.** Something happened (a user successfully solved their problem) and we want to reconstruct the full chain of decisions, actions, and conditions that led to it.

## Depth

**2x** (default): minimum 5 backward steps, 2 premise chains, 2 alternative paths, 2 validation checks.

---

## Step 1: Endpoint Statement

**Endpoint**: A user successfully solved their problem using reasoningtool.

This means: the user had a real problem, applied one or more skills from the toolkit, followed the structured procedure, and arrived at a result they found genuinely useful — not just interesting, but *actionable*. They walked away with clarity, a decision, a plan, or a reframe they didn't have before.

---

## Step 2: What Goal Does This Serve?

**Immediate purpose**: The user wanted to resolve a specific cognitive challenge — a decision, diagnosis, analysis, or creative task — that they couldn't adequately handle with unstructured thinking alone.

They weren't looking for "a cool AI tool." They were looking for *better thinking about a specific thing*. The toolkit was instrumental, not the point.

---

## Step 3: What Problem Generated That Goal?

**Generating problem**: The user hit a wall. Their normal thinking process — intuition, pros/cons lists, asking friends, googling — wasn't giving them confidence in their answer. They needed structured analytical support but didn't have access to a consultant, coach, or analyst.

Possible problem variants:
- "I keep going in circles on this decision"
- "I know something's wrong but I can't pinpoint it"
- "I need to write something but I can't find the angle"
- "I have too many options and no way to compare them"

---

## Step 4: What Context Created That Problem?

**Generating context**: The user was already working in a terminal/IDE environment using Claude Code. They had a workflow that included AI assistance for coding or reasoning tasks. The problem they hit wasn't a coding problem — it was a *thinking* problem that their normal tools didn't address.

---

## Step 5: Full Backward Trace

Working backward from the endpoint through every step:

### Backward Step 7 (earliest): User discovers Claude Code exists
The user learned about Claude Code — Anthropic's CLI tool. They installed it, got comfortable using it for development work. This established the *platform* on which the toolkit would later run.

### Backward Step 6: User encounters reasoningtool
This is the critical discovery moment. How did they find it?

**Premise Chain A (organic discovery):**
- User saw a GitHub repo, a tweet, a blog post, or a recommendation
- The framing caught them: "592 thinking skills as a Claude Code plugin"
- They were curious enough to click through

**Premise Chain B (problem-driven search):**
- User was already frustrated with a specific problem
- They searched for "Claude Code plugins," "structured thinking tools," or "decision frameworks"
- reasoningtool appeared in results and looked relevant

### Backward Step 5: User installs the plugin
The user ran the installation process. This required:
- Reading enough of the README or docs to understand what it was
- Trusting it enough to install (open source, clear structure, no weird dependencies)
- Successfully getting it into their Claude Code setup (adding to `~/.claude/commands/` or equivalent)
- Seeing the skills show up and feeling "okay, this actually works"

**Key requirement**: The installation had to be frictionless enough that they didn't abandon it. Any error, ambiguity, or extra step would have been a drop-off point.

### Backward Step 4: User figures out which skill to use
This is the hardest step in the journey. 592 skills is overwhelming. The user needed to bridge the gap between "I have a problem" and "I should type `/skillname`."

**Premise Chain A (guided entry):**
- User typed `/meta` or read CLAUDE.md
- They saw the category table: "A decision to make → `/decide`"
- The category matched their problem, so they tried it
- The category skill (e.g., `/decide`) routed them to the right analytical skill (e.g., `/dcp` or `/cba`)

**Premise Chain B (direct entry):**
- User already knew what kind of analysis they wanted (e.g., "root cause analysis")
- They typed `/rca` directly, or scanned the direct skills table and found a match
- They skipped the routing layer entirely

In either case, the user had to accomplish *skill selection* — mapping their felt problem to a skill name. This required either good documentation, good routing, or prior familiarity.

### Backward Step 3: User runs the skill with their actual input
The user typed something like `/dcp Should I take the new job or stay at my current one` or `/rca Our deploy pipeline keeps failing on Tuesdays`. They committed their real problem to the tool.

**What had to be true:**
- They trusted the tool enough to give it a real problem (not just a test)
- The skill's input format was intuitive enough that they didn't have to study it
- They framed their problem in a way the skill could work with

### Backward Step 2: The skill produced useful output
The skill ran its structured procedure. The output was:
- Structured (not a wall of text)
- Specific to their input (not generic advice)
- Surprising or clarifying in at least one place (showed them something they hadn't seen)
- Actionable (ended with a next step, a decision, or a clear reframe)

**What had to be true:**
- The skill procedure was well-designed — it asked the right questions in the right order
- The depth scaling was appropriate (not too shallow, not exhaustingly deep)
- The output format was scannable and didn't bury the insight

### Backward Step 1: User recognized the result as valuable
The user read the output and thought: "Oh — that's actually helpful." They didn't just skim it. Something in the output either:
- Named a consideration they'd been feeling but hadn't articulated
- Revealed a blind spot or assumption they didn't know they were making
- Organized their messy thinking into a structure they could act on
- Gave them confidence in a direction they were already leaning toward

**This is the moment the outcome crystallized.** Everything before this was setup; this was the payoff.

---

## Step 6: Reconstructed Forward Story

### Chapter 1: Foundational Value
The user values making good decisions and thinking clearly. They are the kind of person who uses tools to augment their cognition — they already use an AI coding assistant, which means they're comfortable with AI as a collaborator, not just a search engine.

### Chapter 2: Platform Context
They're working in Claude Code. They have a terminal open. They're in a development or knowledge-work workflow where switching to a different tool (a whiteboard, a spreadsheet, a coaching session) would break their flow.

### Chapter 3: The Problem Emerges
A non-trivial thinking problem surfaces during their work. Maybe it's a technical architecture decision, a career choice, a strategy question, or a diagnostic puzzle. Their normal approach (think harder, make a list, ask ChatGPT) isn't cutting it. They need more structure than "just think about it" but less overhead than "hire a consultant."

### Chapter 4: Discovery
They find reasoningtool — through a recommendation, a search, or browsing GitHub. The pitch makes sense: structured thinking procedures, delivered as a Claude Code plugin. It's free, it's open source, and it runs right where they already work.

### Chapter 5: Installation
They install it. It works on the first try. They see the skill list and feel a mix of "this is a lot" and "okay, some of these look relevant."

### Chapter 6: Navigation
They find the right skill. Either they read the category table and follow the routing (`/decide` → `/dcp`), or they already know the kind of analysis they want and go direct (`/rca`, `/cba`, `/br`). The gap between "I have this problem" and "I should type this command" is bridged.

### Chapter 7: Engagement
They type the skill command with their real problem as input. They commit to the process.

### Chapter 8: Output
The skill runs. It produces structured, specific, actionable analysis. At least one insight surprises them or names something they hadn't articulated.

### Chapter 9: Resolution
They read the output and recognize it as valuable. They either make their decision, see their problem differently, identify their next step, or gain confidence in a direction. The problem that brought them here is resolved — or at least transformed from "stuck" to "moving."

---

## Step 7: Story Evaluation

### Does the story cohere?
**Yes.** Each step follows logically from the previous one. The chain of: comfortable with AI tools → encounters thinking problem → finds structured toolkit → navigates to right skill → gets useful output → solves problem is a coherent journey.

### Are the goals legitimate?
**Yes.** Wanting to think more clearly about a real problem is a legitimate, intrinsic goal. Using a structured tool to do it is a reasonable instrumental goal.

### Does the conclusion serve the goals?
**Yes.** Successfully solving the problem is exactly the goal the user had.

### Was the journey necessary?
**Partially.** The user *could* have solved their problem other ways — talking to a friend, journaling, hiring a consultant, using a generic AI prompt. The toolkit's value proposition is that it's faster, more structured, and available in-context. The journey was necessary *given the constraints* (working in a terminal, wanting structured analysis, not wanting to context-switch).

### Validation Check 1: Where does the chain most likely break?
**Step 4 (skill selection) is the most fragile link.** 592 skills is a discovery problem. If the user can't find the right skill quickly, the entire chain breaks — they either give up or pick the wrong skill and get irrelevant output. The category routing table (`/decide`, `/diagnose`, `/search`, etc.) is the critical bridge, but it only works if the user finds it and if their problem maps cleanly to one of the categories.

### Validation Check 2: What would invalidate the story?
The story breaks if:
- **Installation friction is too high** — plugin setup is confusing or error-prone, user never gets to try a skill
- **The skill output is generic** — the structured procedure doesn't actually produce better output than "Claude, help me think about X"
- **The user's problem doesn't match any skill well** — the taxonomy doesn't cover their case, and the routing sends them somewhere unhelpful
- **The user doesn't trust the process** — they see a "Step 1, Step 2" output and think "this is just a gimmick" rather than engaging with it

### Alternative Path 1: The Skeptic's Journey
Not all users arrive through enthusiasm. Some arrive skeptically ("592 skills? That's absurd"), try one skill on a throwaway problem, are mildly surprised by the structure of the output, then come back later with a real problem. The backward trace is the same, but with an extra loop: discovery → skeptical test → mild positive signal → return with real problem → success.

### Alternative Path 2: The Power User's Journey
Some users don't need the routing layer at all. They browse the skill list, immediately see skills that match frameworks they already know (root cause analysis, cost-benefit analysis, assumption examination), and go direct. For these users, the value isn't "help me figure out what kind of thinking to do" — it's "give me a reliable procedure for a kind of thinking I already know I need." Their backward trace skips Chapter 6 (navigation) almost entirely.

---

## Key Insight

The backward trace reveals that the user's success depends on **seven distinct things going right in sequence**: platform familiarity, discovery, installation, navigation, engagement, output quality, and recognition of value. The chain is only as strong as its weakest link.

The most under-discussed link is **navigation** (getting from "I have a problem" to the right `/skill` command). This is where 592 skills becomes a liability rather than an asset. The category routing skills (`/decide`, `/diagnose`, `/search`, etc.) are the load-bearing solution to this problem — they're the funnel that makes the library usable. If those category skills are well-designed and well-documented, the 592-skill library becomes an asset ("there's a skill for everything"). If they're not, it becomes a wall ("I don't know where to start").

The second critical link is **output quality** — specifically, whether the structured procedure produces insight the user *wouldn't have gotten* from an unstructured prompt. If `/dcp` produces better decision analysis than "Claude, help me decide between X and Y," the toolkit earns its existence. If it doesn't, the whole journey was unnecessary overhead.
