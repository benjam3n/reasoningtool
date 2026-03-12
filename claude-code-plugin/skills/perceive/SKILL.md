---
name: "perceive - Perception Engine"
description: "Process a large body of work — strip noise, preserve all signal including nuance, reorganize into the optimal representation, and reason about what it means and what to do."
output:
  format: "prose"
---

# Perception Engine

**Input**: $ARGUMENTS

---

## What This Is

This is NOT summarization. Summarization is lossy — it drops content to get shorter. Perception is lossless on signal — it strips only genuine noise (boilerplate, redundancy, process artifacts, filler) and keeps EVERYTHING that matters, including nuance, tensions, edge cases, and surprises. Then it reasons about what the combined signal means.

The analogy: summarization is a thumbnail image (smaller, lower resolution). Perception is a cleaned-up photograph (same resolution, artifacts removed, properly cropped and color-corrected).

---

## Interpretations

**Interpretation 1 — Bulk output processing**: The user has many outputs (prompt results, skill outputs, agent results, documents) and needs to absorb them all without reading each one individually. The perception engine reads everything, strips noise, preserves all signal, and presents the combined picture with reasoning about what to do.

**Interpretation 2 — Single deep output processing**: The user has one large, complex output and needs to perceive what's actually in it — the real findings, not the scaffolding.

**Interpretation 3 — Ongoing perception**: The user wants to set up a perception layer for work that's being produced incrementally. "As things come in, process them through this lens."

If ambiguous, default to Interpretation 1 (bulk processing) — it's the most common need.

---

## Core Principles

1. **Noise is NOT the same as less important.** Noise is genuinely useless content: formatting artifacts, step-counting boilerplate, restated instructions, hedge phrases, generic advice, filler transitions. A nuanced insight that only matters in edge cases is NOT noise — it's low-frequency signal. Keep it.

2. **The user's context determines what's signal.** The same sentence can be noise in one context and critical signal in another. Always anchor perception in: what is the user trying to do? What decisions do they face? What would change their behavior?

3. **Preserve tensions and contradictions.** When two outputs disagree, BOTH are signal. Don't resolve the tension — surface it. The user needs to see where their information conflicts.

4. **The best representation depends on what happens next.** If the user needs to make a decision, organize by decision-relevant factors. If they need to act, organize by priority. If they need to understand, organize by theme. ASK or infer what they need to do next, and let that drive the format.

5. **Reasoning is mandatory.** Don't just present clean signal — THINK about what it means. What patterns emerge? What conclusions does the combined evidence support? What should the user do? This is the difference between a filing system and an advisor.

---

## Phase 1: INGEST

Read everything. For bulk processing, read all sources before doing any analysis.

```
INGESTED:
  Sources: [count]
  Total volume: [rough word/page count]
  Source list:
  1. [source name/file] — [1-line content description]
  2. [source name/file] — [1-line content description]
  ...
```

---

## Phase 2: PERCEIVE — Separate Signal from Noise

For each source, classify every element as signal or noise.

### What Counts as NOISE (strip it):

- Process artifacts: step numbers, phase headers, checklist formatting, "Pre-Completion Checklist" sections
- Boilerplate: skill invocation instructions, integration sections, depth scaling tables
- Hedge filler: "it's worth noting that," "it should be mentioned," "generally speaking"
- Restated instructions: when the output repeats back the input or the skill's own structure
- Generic advice: anything true of everything and therefore informative about nothing
- Redundancy across sources: the same insight stated in 4 different outputs (keep the best formulation, note the convergence)

### What Counts as SIGNAL (keep all of it):

- **Findings**: specific claims, conclusions, assessments, measurements
- **Insights**: things that shift understanding, reframe the situation, or reveal something non-obvious
- **Tensions**: where two findings conflict, or where a finding conflicts with the user's current approach
- **Nuance**: qualifications that change the meaning — "X is true EXCEPT when Y" (the exception is signal)
- **Surprises**: anything unexpected, counterintuitive, or that contradicts prior assumptions
- **Recommendations**: specific suggestions for action, with reasoning
- **Evidence**: data, examples, or reasoning that supports or undermines a finding
- **Edge cases**: scenarios where the main finding doesn't hold (these are high-value signal that summaries typically drop)
- **Questions raised**: things the work surfaced that weren't in the original question
- **Emotional/energy signals**: when the analysis reveals frustration, avoidance, excitement, or resistance — these are information

```
For each source:
  [Source N]:
  SIGNAL:
  - [S-N.1] [finding/insight/tension/etc.] — type: [finding/insight/tension/nuance/surprise/recommendation/evidence/edge-case/question/emotional]
  - [S-N.2] ...
  NOISE STRIPPED: [brief description of what was removed and why]
```

---

## Phase 3: CROSS-REFERENCE — Find the Combined Picture

Now work across all sources:

### Convergence
Where do multiple sources point to the same conclusion?

```
CONVERGENCES (appear in 3+ sources):
- [finding] — confirmed by: [source list] — STRENGTH: [strong/moderate]
```

Strong convergence = high-confidence signal. The more independent paths that arrive at the same conclusion, the more you should trust it.

### Divergence
Where do sources disagree?

```
DIVERGENCES (sources conflict):
- [topic]: [Source A says X] vs [Source B says Y]
  → Why they might differ: [different assumptions, different scope, different framing]
  → Which is more supported: [assessment, or "genuinely unresolved"]
```

Do NOT resolve divergences by picking a side unless the evidence clearly favors one. Present both.

### Unique Signals
What appears in only one source but is potentially important?

```
UNIQUE SIGNALS (one source only, but potentially high-value):
- [finding] — from: [source] — why it might matter: [reason]
```

### Emergent Patterns
What becomes visible only when you look across all sources together?

```
EMERGENT PATTERNS (not in any single source, visible only in combination):
- [pattern] — evidence: [which sources contribute to this pattern]
```

---

## Phase 4: REPRESENT — Optimal Format

Choose the representation based on what the user needs to do next:

| User's Next Action | Optimal Representation |
|---|---|
| Make a decision | Decision-relevant factors, organized for/against, with recommendation |
| Prioritize work | Ranked list with impact/effort/urgency scores |
| Understand a situation | Thematic map with convergences and tensions |
| Take action | Ordered action list with dependencies and first steps |
| Communicate to others | Narrative with key points and evidence |
| Explore further | Questions raised, gaps found, suggested investigations |

If the next action isn't clear, ask: "What do you need to DO with this information?"

If you can infer it from context, state your inference and proceed.

```
REPRESENTATION FORMAT: [which format]
REASON: [why this format serves the user's next action]
```

Then produce the output in that format, using ONLY the signal from Phases 2-3. Every item in the representation must trace back to a specific S-number from Phase 2.

---

## Phase 5: REASON — What Does This Mean?

This is the phase that makes perception different from filtering. Think about what the combined signal means.

```
REASONING
=========

WHAT THE EVIDENCE SAYS:
[2-5 sentences synthesizing the convergent findings into a coherent picture]

WHAT'S UNCERTAIN:
[list the divergences and unresolved questions — be honest about what you don't know]

WHAT SURPRISED ME:
[findings that don't fit the expected pattern — these often contain the most value]

WHAT THIS MEANS FOR [user's goal/situation]:
[specific implications — not generic advice, but "given YOUR context, this means..."]

RECOMMENDED ACTIONS (in priority order):
1. [action] — because: [reasoning traced to specific findings]
2. [action] — because: [reasoning]
3. [action] — because: [reasoning]

WHAT I'D INVESTIGATE NEXT:
- [question or gap worth pursuing]
```

---

## Phase 6: COMPLETENESS CHECK

Before outputting, verify nothing important was lost:

```
COMPLETENESS CHECK:
- [ ] Every source was ingested (none skipped or skimmed)
- [ ] Signal classification used all 10 signal types (findings, insights, tensions, nuance, surprises, recommendations, evidence, edge cases, questions, emotional)
- [ ] Tensions and contradictions were PRESERVED, not resolved prematurely
- [ ] Nuance and edge cases were kept (the stuff summaries drop)
- [ ] Cross-referencing found both convergences AND divergences
- [ ] Representation format matches the user's next action
- [ ] Reasoning references specific findings, not generic principles
- [ ] No signal was dropped for the sake of brevity
```

---

## Depth Scaling

| Depth | Sources Processed | Cross-Referencing | Reasoning |
|---|---|---|---|
| 1x | All sources, surface signal only | Convergences only | Key findings + 1 recommendation |
| 2x | All sources, full signal extraction | Convergences + divergences | Full reasoning with actions |
| 4x | All sources, full signal + sub-signals | Full cross-reference + emergent patterns | Deep reasoning + investigation suggestions |
| 8x | All sources, exhaustive signal extraction | Full + unique signals assessed | Reasoning + scenario analysis + decision framework |

Default: 2x.

---

## Failure Modes

| Failure | Signal | Fix |
|---|---|---|
| **Treated it as summarization** | Output is shorter but lost nuance and edge cases | Go back to Phase 2 — check every signal type. Nuance and edge cases are NOT noise. |
| **Resolved tensions** | "After considering both sides, X is right" | DON'T resolve. Present both sides. The user decides. |
| **Generic reasoning** | "You should focus on what matters most" | Reasoning must reference SPECIFIC findings from Phase 2. No generic advice. |
| **Noise preserved** | Output includes step numbers, checklists, boilerplate from source documents | Strip process artifacts. They're scaffolding, not content. |
| **Signal dropped for brevity** | "In the interest of space, I'll focus on the top 5" | No. Keep ALL signal. This is not summarization. Use better organization instead of cutting. |
| **Format doesn't match need** | Beautiful thematic map when the user needs an action list | Phase 4 — ask or infer what the user needs to DO, and let that drive the format. |
| **No reasoning** | Just presented the filtered signal without thinking about what it means | Phase 5 is mandatory. The user can filter noise themselves. The value is in the REASONING. |
| **Skipped sources** | "I focused on the most relevant 10 of 100" | No. Ingest ALL sources. The ones you'd skip might contain the most surprising findings. |

---

## Practical Execution for Large Batches

When processing many sources (10+), use this approach:

1. **Batch ingest**: Read sources in groups of 5-10
2. **Per-batch perception**: Extract signal from each batch
3. **Cross-batch synthesis**: Combine signal across all batches
4. **Single reasoning pass**: Reason about the combined signal once, not per-batch

For very large batches (50+), use parallel agents:
- Each agent processes a batch and returns signal only (no noise, no reasoning)
- One final pass combines all agent signals, cross-references, and reasons

---

## Integration

Use with:
- `/sum` → When lossy compression IS what's needed (quick overview, not full perception)
- `/pri` → When perception reveals many possible actions and you need to rank them
- `/enough` → When you're not sure if you've processed enough sources
- `/phil` → When perception reveals you need to rethink requirements before acting
- `/ar` or `/aw` → When a perceived finding needs stress-testing
- `/wtdn` → When perception produces clear next steps
