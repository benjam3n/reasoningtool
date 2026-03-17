---
name: "fowtd - Figure Out What To Do"
description: "When you have a pile of data, information, options, or material and don't know what to do with it — extract what matters, identify what it's for, and produce a concrete action plan."
output:
  format: "prose"
---

# FOWTD - Figure Out What To Do

**Input**: $ARGUMENTS

---

## Core Principles

1. **Data without direction is noise.** Having lots of information feels like having lots of knowledge. It isn't. The skill's job is to turn a pile into a plan — not to reorganize the pile.

2. **The data usually implies its own purpose.** Most collections of information have a latent shape — they're evidence for a decision, inputs to a plan, background for a creation, or symptoms of a problem. Find the shape before deciding what to do.

3. **Triage before analysis.** Not everything in the pile matters. Some of it is redundant, some is irrelevant, some is critical. Sort by relevance FIRST, then figure out what to do with what survives.

4. **"What to do" means ONE clear direction, not many.** The user already has too much. Don't add more options. Converge to a single recommended course of action with a concrete first step.

5. **The action should use the data, not just acknowledge it.** "Review the data more carefully" is not a valid output. The action must transform, apply, decide on, or respond to the material.

---

## Phase 1: Material Inventory

What do you actually have?

```
[D1] RAW_MATERIAL: [brief description of the data/information/material the user has]
[D2] VOLUME: [small (fits in a paragraph) | medium (a page or two) | large (extensive)]
[D3] MATERIAL_TYPES: [data | notes | options | research | feedback | observations | mixed]
[D4] STRUCTURE: [structured (tables, lists) | semi-structured (notes with some organization) | unstructured (raw dump)]
[D5] SOURCE_COUNT: [single source | few sources | many sources]
```

---

## Phase 2: Shape Detection

What is this data shaped like? What does it want to become?

```
[D6] LATENT_SHAPE: [see table below]
[D7] EVIDENCE: [what signals this shape]
[D8] CONFIDENCE: [high | medium | low]
```

### Shape Classification Table

| Shape | Signals | The data wants to become... | Route |
|-------|---------|---------------------------|-------|
| **Decision inputs** | Options, pros/cons, tradeoffs, comparisons | A choice | → `/decide` or `/cba` |
| **Problem symptoms** | Error reports, complaints, failures, anomalies | A diagnosis | → `/diagnose` |
| **Research findings** | Studies, references, evidence, arguments | A conclusion or synthesis | → `/claim` or `/lr` |
| **Project material** | Tasks, requirements, specs, stakeholder input | A plan | → `/de` or `/to` |
| **Creative raw material** | Ideas, fragments, inspirations, references | A creation | → `/create` |
| **Feedback/evaluation** | Reviews, scores, critiques, test results | An improvement action | → `/iterate` or `/evaluate` |
| **Observations** | Patterns, trends, measurements, logs | An insight or model | → `/analyze` |
| **Options/possibilities** | Brainstorm output, alternatives, candidates | A selection | → `/decide` or `/ro` |
| **Scattered thoughts** | Random notes, half-formed ideas, tangents | Coherence | → `/iagca` or `/cls` |
| **Unknown** | No clear pattern | Clarification | → Ask user |

If CONFIDENCE is low:
```
[D9] ALTERNATIVE_SHAPE: [what else it could be]
[D10] DISAMBIGUATING_QUESTION: [what would resolve the ambiguity]
```

---

## Phase 3: Triage

Not everything matters equally. Sort the material.

```
[D11] CRITICAL: [items that directly determine the outcome — must be used]
[D12] USEFUL: [items that support or inform — use if time allows]
[D13] NOISE: [items that are redundant, irrelevant, or distracting — set aside]
[D14] MISSING: [information you'd expect to see but don't have — gaps]
```

### Triage Rules

- If >50% is NOISE → the user may be collecting instead of acting. Flag this.
- If MISSING items are critical → the next action is to GET the missing data, not to act on what exists.
- If CRITICAL items contradict each other → the next action is to resolve the contradiction.

---

## Phase 4: Action Determination

Given the shape and the triaged material, what should the user actually do?

```
[D15] RECOMMENDED_ACTION: [one specific thing to do with this data]
[D16] ACTION_TYPE: [decide | build | write | analyze | fix | plan | communicate | research-more]
[D17] WHY_THIS: [why this action over alternatives — what makes it the right use of this data]
[D18] FIRST_STEP: [the concrete, immediate thing to do — not vague]
[D19] USES_WHICH_DATA: [which CRITICAL items this action directly uses]
```

### Action Selection Criteria

| Criterion | Question |
|-----------|----------|
| **Fit** | Does this action match the data's shape? |
| **Completeness** | Can this action be taken with the data available, or are gaps blocking? |
| **Value** | Does this action produce something the user can use? |
| **Urgency** | Is there a reason to act now vs. gather more? |

---

## Phase 5: Output

```
FIGURE OUT WHAT TO DO
=====================

YOU HAVE: [one-sentence summary of the material]
IT'S SHAPED LIKE: [shape — what the data wants to become]

WHAT MATTERS:
  CRITICAL: [key items, briefly]
  GAPS: [missing items, if any]
  NOISE: [what to set aside]

→ DO THIS: [recommended action — specific and concrete]
  WHY: [one sentence]
  FIRST STEP: [immediate next action]
  SKILL: → INVOKE: /skill-id $ARGUMENTS

IF GAPS BLOCK ACTION:
  GET THIS FIRST: [what missing information to obtain]
  HOW: [where/how to get it]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Reorganizing instead of acting** | Output is a better-organized version of the pile | The output must be an ACTION, not a reorganization |
| **Analysis paralysis** | "You could do X, Y, or Z" | Pick ONE. The user already has too many options |
| **Missing the shape** | Action doesn't match what the data naturally supports | Re-check shape classification table |
| **Ignoring gaps** | Recommends action when critical data is missing | Check MISSING items — if critical, get data first |
| **Too abstract** | "Synthesize the findings" | What specific output, in what format, for what audience? |
| **Treating all data as equal** | No triage, everything is "important" | Force-rank into CRITICAL / USEFUL / NOISE |

---

## Depth Scaling

| Depth | Material Inventory | Shape Detection | Triage | Action Options Considered |
|-------|-------------------|-----------------|--------|--------------------------|
| 1x | Type + volume only | Best guess | Critical only | 1 action |
| 2x | Full inventory | Shape + evidence | Full triage | 2-3 actions, pick best |
| 4x | Full + source quality | Shape + alternative + confidence | Full + gap analysis | 4-5 actions, scored |
| 8x | Full + provenance | Multi-shape analysis | Full + contradiction check | Comprehensive action matrix |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Material inventoried (not just acknowledged)
- [ ] Shape detected with evidence (not assumed)
- [ ] If low confidence on shape: alternative offered or question asked
- [ ] Triage performed — CRITICAL, USEFUL, NOISE separated
- [ ] Gaps identified (missing data that matters)
- [ ] If gaps are critical: action is "get the data," not "act without it"
- [ ] ONE recommended action (not multiple options)
- [ ] Action is concrete and specific (not "analyze further")
- [ ] First step is immediately actionable
- [ ] Action uses the CRITICAL data, not just the easy data

---

## Integration

- Use from: user has data/information/material and doesn't know what to do with it
- Differs from `/handle`: handle classifies ambiguous requests; fowtd processes data piles
- Differs from `/next`: next picks one step given clear context; fowtd creates context from raw material
- Differs from `/iagca`: iagca compresses sprawl; fowtd finds direction in data
- Differs from `/categorize`: categorize sorts things; fowtd determines what to DO with things
- Routes to: whatever skill the determined action requires
- See also: `/fowtdn` for when you've already started and need the NEXT action
