---
name: "sum - Summarize"
description: "Summarize anything — text, conversations, situations, projects, decisions, or experiences — using the interpretation that best matches what the user actually needs."
output:
  format: "prose"
---

# Summarize

**Input**: $ARGUMENTS

---

## Step 0: Detect Interpretation

Before summarizing, identify what the user actually needs. The interpretations below were derived from three independent sources — the purposes people summarize for, the input types people bring, and the cognitive operations summaries perform — and validated by convergence across all three.

| Interpretation | User's Purpose | What to Produce |
|---|---|---|
| **Compress** | Make something shorter while preserving content | Multi-level compression (1 sentence → 1 paragraph → 1 page) |
| **Distill** | Find the core insight in something complex | Irreducible core + supporting structure + what to ignore |
| **Recap** | Capture what happened in a temporal sequence | Decisions, actions, insights, open questions, emotional temperature |
| **Status** | Know where a project or effort currently stands | Current state, trajectory, blockers, next steps |
| **Synthesize** | Find patterns across multiple sources | Convergent themes, divergences, and the combined picture |
| **Explain** | Communicate something to a specific audience | Audience-adapted summary using their vocabulary and concerns |
| **Retrospect** | Wrap up a completed effort with lessons learned | What worked, what didn't, what to carry forward, what to stop |
| **Extract** | Pull specific categories of content from a body | Structured, ranked extraction of claims, actions, decisions, etc. |

### Detection Rules

- Long text, single source, "make it shorter" → **Compress**
- Complex argument, "what's the point?" → **Distill**
- Conversation, meeting, session log → **Recap**
- Ongoing project, "where are we?" → **Status**
- Multiple sources, "what's the picture?" → **Synthesize**
- "Explain this to [person/audience]" → **Explain**
- Completed effort, "what did we learn?" → **Retrospect**
- "Pull out the [X]" or "list all the [Y]" → **Extract**

### Disambiguation

If ambiguous, ask using plain language (not internal terminology):

> I can summarize this in different ways:
> (a) Make it shorter — keep the same content, just less of it
> (b) Find the main point — what's this really about?
> (c) List what happened — decisions, actions, open questions
> (d) Show where things stand — progress, blockers, next steps
> (e) Find patterns across sources — what themes recur?
> (f) Explain it for someone specific — adapted to their context
> (g) Wrap it up — what worked, what didn't, lessons learned
> (h) Pull out specific things — claims, actions, data, etc.
> Which fits?

### Boundary Clarification

- **Compress vs Distill**: Compress makes the SAME content shorter. Distill finds the ONE core idea and structures everything around it. Test: if you expanded the summary back out, would you get the original (Compress) or a thesis paper (Distill)?
- **Recap vs Status**: Recap is BACKWARD-looking (what happened). Status is FORWARD-looking (where are we going). Recap answers "what did we discuss?" Status answers "are we on track?"
- **Recap vs Extract**: Recap always follows a temporal sequence (conversation, meeting, session) with preset categories. Extract works on any source and the user specifies what to pull out.
- **Synthesize vs Compress**: Compress works on ONE source. Synthesize works on MULTIPLE sources to find what they share and where they diverge.
- **Retrospect vs Recap**: Recap captures what happened. Retrospect evaluates what happened — what worked, what failed, what to change.

```
INTERPRETATION: [which one]
REASON: [why this matches]
```

---

## Interpretation 1: COMPRESS

Produce the same content at multiple compression levels. Optimize for: fidelity (doesn't distort meaning) and compression ratio (genuinely shorter).

### Step 1: Extract Claims

Read the input and list every distinct claim, fact, or point made.

```
CLAIMS:
1. [claim]
2. [claim]
...
```

### Step 2: Rank by Importance

| Claim | Centrality (1-5) | Novelty (1-5) | Total |
|---|---|---|---|
| [claim] | [score] | [score] | [sum] |

- **Centrality**: How essential to the main point? (5 = IS the point, 1 = tangential)
- **Novelty**: Would the audience be surprised? (5 = very, 1 = obvious)

Sort descending.

### Step 3: Compress at Three Levels

**ONE SENTENCE** — Top-ranked claim only. Complete, standalone, no jargon.

**ONE PARAGRAPH** (3-5 sentences) — Top 3-5 claims. First sentence = the one sentence. Last sentence = "so what" implication.

**ONE PAGE** (~250 words) — All claims scored 5+. Organized by logical grouping (not order of appearance). Key evidence for top claims. End with implications or next steps.

### Step 4: Fidelity Check

Read each compression level back. For each, ask:

```
FIDELITY CHECK:
- Level 1: Does the sentence say what the original said, or did compression change the meaning? [FAITHFUL / DISTORTED — how]
- Level 2: Would someone who read only this paragraph draw the same conclusions as someone who read the full original? [YES / NO — what differs]
- Level 3: What was dropped? Does any dropped claim matter enough that its absence is misleading? [list dropped claims that matter]
```

If any check reveals distortion, revise that level.

### Step 5: Verify

```
VERIFICATION:
- Level 1: Captures the single most important point? [YES/NO]
- Level 2: Someone could make a decision based on this alone? [YES/NO]
- Level 3: Nothing critical (scored 5+) missing? [YES/NO]
- Fidelity: No meaning distorted at any level? [YES/NO]
```

---

## Interpretation 2: DISTILL

Find the irreducible core of something complex. Not shorter — clearer. Optimize for: insight (finds what matters) and signal-to-noise (eliminates what doesn't).

### Step 1: Find the Core

The core is the ONE idea that all other ideas in the input serve. To find it:

1. State the thesis of each section or major point in the input:
   ```
   SECTION THESES:
   1. [section/point] → thesis: [what it argues]
   2. [section/point] → thesis: [what it argues]
   ...
   ```

2. Ask: which thesis do ALL the others support or elaborate? That is the core.
   - If one thesis is clearly served by the rest → that's the core
   - If two theses seem co-equal → find what they SHARE. The shared thing is the core.
   - If no hierarchy exists → the input has multiple cores. State each separately.

```
CORE INSIGHT: [The one thing this is really about, stated plainly]
CONFIDENCE: [high — clear hierarchy / medium — judgment call / low — multiple cores]
```

### Step 2: Map the Supporting Structure

```
THE CORE IS SUPPORTED BY:
1. [supporting point] — [why it matters to the core]
2. [supporting point] — [why it matters to the core]
3. [supporting point] — [why it matters to the core]

THE CORE DEPENDS ON:
- [assumption or prerequisite the core requires]
- [assumption or prerequisite the core requires]
```

### Step 3: Identify What to Ignore

```
SAFELY IGNORE:
- [element that seems important but is tangential] — [why it's not load-bearing]
- [detail that supports a supporting point but not the core] — [why it can be dropped]
- [context that's interesting but not structural] — [why it's noise]
```

### Step 4: Distilled Output

```
DISTILLED
=========
CORE: [one sentence]
STRUCTURE: [3-5 supporting points, each one sentence]
DEPENDS ON: [1-3 assumptions]
IGNORE: [what you can skip without losing the essence]
```

---

## Interpretation 3: RECAP

Summarize a conversation, meeting, session, or interaction. Optimize for: completeness of outcomes (nothing decided gets lost) and actionability (reader knows what to do next).

### Step 1: Scan for Categories

Pull from the input:

```
DECISIONS MADE:
- [decision] — [who decided, if applicable]

ACTIONS IDENTIFIED:
- [action] — [owner, if applicable] — [deadline, if applicable]

KEY INSIGHTS:
- [something that shifted understanding]

OPEN QUESTIONS:
- [unresolved question]

WHAT CHANGED:
- [state before] → [state after]

DISAGREEMENTS / TENSIONS:
- [point of disagreement] — [current status: resolved/unresolved]

EMOTIONAL TEMPERATURE:
- [was this tense, smooth, energized, draining, etc.? one sentence]
- [why it matters: e.g., "tense — alignment on X may be fragile"]
```

Leave any category empty if nothing fits — don't force it.

### Step 2: Narrative Recap

Write a 3-5 sentence narrative that covers: what the conversation was about, what was decided or discovered, what the emotional tone was, and what's still open.

```
RECAP
=====
[narrative paragraph]

DECISIONS: [list]
ACTIONS: [list with owners]
OPEN: [list]
```

---

## Interpretation 4: STATUS

Summarize where a project, situation, or effort currently stands. Optimize for: honest assessment (not spin) and forward direction (what to do, not just what is).

### Step 1: Current State

```
STATUS
======
WHAT: [what is this project/situation]
WHERE: [current state in one sentence]
PROGRESS: [what's been accomplished since the last meaningful checkpoint]
MOMENTUM: [accelerating / steady / stalled / uncertain — with one sentence of evidence]
```

### Step 2: Blockers and Next Steps

```
BLOCKED BY:
- [blocker] — [what it prevents]

NEXT STEPS:
1. [most important next action]
2. [second most important]
3. [third]

RISKS:
- [thing that could go wrong] — [likelihood: high/medium/low]
```

### Step 3: Verdict

```
OVERALL: [one sentence — is this on track, off track, or unclear?]
HONEST ADDITION: [one sentence the stakeholder needs to hear but might not want to]
```

---

## Interpretation 5: SYNTHESIZE

Find the combined picture across multiple sources. Optimize for: pattern detection (what recurs) and divergence detection (where sources disagree).

### Step 1: Source Inventory

```
SOURCES:
1. [source 1] — [brief description, 1 sentence]
2. [source 2] — [brief description, 1 sentence]
...
```

### Step 2: Extract Key Points from Each

For each source, pull the 3-5 most important claims or findings.

```
SOURCE 1 KEY POINTS:
- [point]
- [point]
...

SOURCE 2 KEY POINTS:
- [point]
...
```

### Step 3: Find Convergences and Divergences

**Before reporting convergence, check source independence:**

```
SOURCE INDEPENDENCE CHECK:
  Did sources share inputs, context, or instructions? [yes/no/partial]
  If yes: which context was shared? [describe]
  INDEPENDENCE VERDICT: [independent / partially independent / not independent]

  If NOT INDEPENDENT: Convergence across these sources may be ECHO, not signal.
  Multiple sources reaching the same conclusion from the same (possibly wrong)
  premises is not evidence — it's amplification. Flag any convergent finding
  where the converging sources shared the same context gap or assumption.
```

```
ALL SOURCES AGREE ON:
- [point that appears in 3+ sources] — INDEPENDENCE: [genuine / echo — shared assumption]
- [point that appears in 3+ sources] — INDEPENDENCE: [genuine / echo — shared assumption]

SOME SOURCES AGREE ON:
- [point] — found in: [sources] — absent from: [sources]

SOURCES DISAGREE ON:
- [topic] — [source X says A] vs [source Y says B]
  → Resolution: [which is more supported, or genuinely unresolved]

UNIQUE TO ONE SOURCE (potentially important or potentially noise):
- [point] — from: [source] — likely: [important insight / outlier / error]
```

### Step 4: The Combined Picture

```
SYNTHESIS
=========
ACROSS [N] SOURCES:

THE COMBINED PICTURE: [2-3 sentence narrative of what the sources collectively say]

STRONGEST SIGNALS (appear in most sources):
1. [signal]
2. [signal]

OPEN CONFLICTS:
- [where sources disagree and it matters]

WHAT'S MISSING (none of the sources address):
- [gap]
```

---

## Interpretation 6: EXPLAIN

Summarize something for a specific audience who doesn't have your context. Optimize for: audience fit (uses their frame, not yours) and standalone clarity (they don't need the original).

### Step 1: Identify Audience and Gap

```
AUDIENCE: [who needs to understand this]
THEY KNOW: [what they already understand]
THEY DON'T KNOW: [what's missing]
THEY CARE ABOUT: [what matters to them — not to you]
FRAME: [how they think about this domain — their vocabulary, mental models, concerns]
```

### Step 2: Bridge the Gap

Write the summary from THEIR perspective, using THEIR vocabulary, addressing THEIR concerns. Translate frames where needed (e.g., technical → business impact, research → practical implications).

```
EXPLANATION
===========
[summary written for the identified audience]
```

### Step 3: Check

```
- Does this use their vocabulary, not mine? [YES/NO]
- Does this answer what THEY would ask, not what I'd want to tell them? [YES/NO]
- Could they act on this without asking follow-up questions? [YES/NO]
- Have I translated frames, not just simplified words? [YES/NO]
```

---

## Interpretation 7: RETROSPECT

Wrap up a completed effort with lessons learned. Optimize for: honest evaluation (not self-congratulation) and transferable lessons (applicable beyond this specific effort).

### Step 1: What Was the Effort?

```
EFFORT: [what was done]
GOAL: [what it was supposed to achieve]
OUTCOME: [what actually happened]
TIMEFRAME: [when it started → when it ended]
```

### Step 2: Evaluate

```
WHAT WORKED:
- [thing that went well] — WHY it worked: [root cause of success]

WHAT DIDN'T WORK:
- [thing that went poorly] — WHY it failed: [root cause of failure]

WHAT WAS SURPRISING:
- [unexpected outcome] — LESSON: [what this teaches]

WHAT WOULD YOU DO DIFFERENTLY:
- [change] — BECAUSE: [what you now know that you didn't then]
```

### Step 3: Carry Forward

```
RETROSPECT
==========
EFFORT: [one sentence]
OUTCOME: [one sentence]

KEEP DOING: [practices that worked and should continue]
STOP DOING: [practices that failed or weren't worth the cost]
START DOING: [new practices suggested by what was learned]
KEY LESSON: [the single most important takeaway, stated as a transferable principle]
```

---

## Interpretation 8: EXTRACT

Pull specific types of content out of a larger body. Optimize for: completeness (nothing important missed) and usability (extracted items are organized, not just listed).

### Step 1: What to Extract

Determine what the user wants pulled out. Common extraction targets:

- **Claims** — assertions, arguments, positions → rank by confidence level
- **Actions** — things to do, tasks, next steps → assign owners and deadlines
- **Decisions** — choices made or needed → note who decides and by when
- **Questions** — unresolved questions → rank by urgency
- **Data** — numbers, measurements, evidence → organize by category
- **People** — who's involved and their roles → map relationships
- **Risks** — potential problems mentioned → rank by severity × likelihood
- **Requirements** — things that must be true or done → classify as must/should/could

```
EXTRACTING: [what type]
FROM: [brief description of source]
```

### Step 2: Extract

```
EXTRACTED [TYPE]:
1. [item] — [source/context]
2. [item] — [source/context]
...
```

### Step 3: Organize

Apply the ranking method appropriate to the extraction type:

| Extraction Type | Ranking Method |
|---|---|
| Claims | Confidence: high / medium / low / contested |
| Actions | Priority: must-do / should-do / nice-to-do + owner + deadline |
| Decisions | Status: decided / pending / blocked + decision-maker |
| Questions | Urgency: blocks progress / important / can wait |
| Data | Category grouping + outlier flagging |
| Risks | Severity × likelihood matrix |
| Requirements | MoSCoW: must / should / could / won't |

```
ORGANIZED [TYPE]:

[HIGH PRIORITY / HIGH CONFIDENCE / MUST-DO]:
1. [item]
2. [item]

[MEDIUM]:
1. [item]

[LOW / CAN WAIT]:
1. [item]
```

---

## Quality Criteria by Interpretation

Different summary types optimize for different things. Use the criteria for the active interpretation:

| Interpretation | Primary Criteria | Secondary Criteria | Acceptable Trade-off |
|---|---|---|---|
| Compress | Fidelity (no distortion) | Compression ratio | May lose nuance |
| Distill | Insight (finds the core) | Signal-to-noise | May oversimplify |
| Recap | Outcome completeness | Actionability | May miss subtext |
| Status | Honest assessment | Forward direction | May feel blunt |
| Synthesize | Pattern detection | Divergence detection | May over-aggregate |
| Explain | Audience fit | Standalone clarity | May lose precision |
| Retrospect | Honest evaluation | Transferable lessons | May feel uncomfortable |
| Extract | Extraction completeness | Usability of output | May decontextualize |

---

## Output Format (All Interpretations)

Every output must include:

```
SUMMARY TYPE: [interpretation name]
INPUT: [1-line description of what was summarized]

[interpretation-specific output]
```

---

## Depth Scaling

| Depth | Compress | Distill | Recap | Status | Synthesize | Explain | Retrospect | Extract |
|---|---|---|---|---|---|---|---|---|
| 1x | 1 sentence only | Core only | Decisions + actions | State + next step | Convergences only | One paragraph | What worked / didn't | List only |
| 2x | All 3 levels + fidelity | Full distillation | All categories + narrative | Full status + risks | Convergences + divergences | Audience-adapted + check | Full evaluation + carry forward | Grouped + ranked |
| 4x | + claim table | + assumption testing | + tensions + emotional temp | + trajectory analysis | + unique points + gaps | + multiple audiences | + root cause analysis | + cross-references |

Default: 2x.

---

## Failure Modes

| Failure | Signal | Fix |
|---|---|---|
| **Wrong interpretation** | Output doesn't match what user needed | Re-read Step 0; if ambiguous, ASK using the plain-language question |
| **Compression without fidelity** | Summary distorts or changes the original meaning | Run the fidelity check — compare summary claims to original claims |
| **Can't find the core** | Distillation has 5 "core insights" | There's only one core. Find the thesis all others serve. If truly no hierarchy, state that explicitly. |
| **Recap without actions** | Meeting summary is narrative only | Force the categories: decisions, actions, open questions |
| **Status without honesty** | "Everything is fine" when it isn't | Add the "honest addition" — what the stakeholder needs to hear |
| **Synthesis without divergences** | "All sources agree" (suspiciously) | Check harder — sources rarely fully agree. Find where they differ. |
| **Echo mistaken for convergence** | Multiple sources agree but shared the same inputs/context/assumptions | Run the source independence check. If sources aren't independent, their agreement proves nothing — flag convergent claims that rest on shared assumptions. |
| **Explaining to yourself** | Summary uses your jargon, not audience's | Rewrite from their vocabulary and frame, not just simpler words |
| **Retrospect without discomfort** | "Everything worked great" | If nothing went wrong, you're not being honest. Find the failures. |
| **Extracting without ranking** | 50 items pulled out, flat list | Apply the ranking method for that extraction type. Raw lists aren't summaries. |

---

## Pre-Completion Checklist

- [ ] Interpretation correctly identified (or asked using plain language if ambiguous)
- [ ] Boundary clarification applied (Compress vs Distill, Recap vs Status, etc.)
- [ ] Output uses the format and quality criteria for that interpretation
- [ ] Summary is genuinely shorter/clearer than the input (not just reformatted)
- [ ] The single most important thing is stated first
- [ ] Nothing critical was dropped (or drops are acknowledged)
- [ ] Interpretation-specific quality criteria met (fidelity for Compress, core-finding for Distill, etc.)
- [ ] Someone who reads only the summary could act appropriately

---

## Integration

Use with:
- `/sim` → When you want to simplify (make easier) rather than summarize (make shorter/clearer)
- `/tri` → When items need urgency-based sorting, not summarizing
- `/pri` → When the summary reveals items that need prioritization
- `/teach` → When the goal is learning, not just understanding
- `/reframe` → When the summary reveals the framing is wrong
- `/cmp` → When you need a detailed head-to-head comparison (more thorough than Synthesize's divergence detection)
- `/extract` → When you need skills extracted from a prompt (different skill — extracts reasoning skills, not content)
- `/phil` → To derive requirements for what a summary should contain before summarizing
- `/enough` → To check whether the summary is thorough enough for its purpose
