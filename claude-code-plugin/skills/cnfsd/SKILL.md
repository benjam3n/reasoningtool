---
name: "cnfsd - Confused"
description: "For mental fog where things don't make sense. Separates what you understand from what you don't, identifies the gap type, and provides the right tool to close it."
---

# CNFSD - Confused

**Input**: $ARGUMENTS

---

## Core Principles

1. **Confusion is useful.** It means you're at the boundary of your knowledge. That boundary is exactly where learning happens. Confusion isn't a problem to eliminate — it's a signal to follow.

2. **Confusion has a shape.** "I'm confused" is too vague to solve. "I'm confused about WHY X leads to Y" is solvable. The first job is naming the shape.

3. **You understand more than you think.** Confusion feels total but rarely is. There's always a part you DO get. Finding that part gives you a foundation to build from.

4. **Different gaps need different tools.** A missing fact needs a lookup. A missing concept needs an analogy. A missing connection needs a diagram. Using the wrong tool for the gap type wastes time and deepens frustration.

---

## Phase 1: Name the Confusion

What word completes this sentence: "I'm confused about ___"

```
[C1] RAW_CONFUSION: [user's input, as stated]
[C2] CONFUSION_TYPE: Which of these fits?
```

| Type | Pattern | Example |
|------|---------|---------|
| **HOW** | I don't understand the mechanism | "How does this process actually work?" |
| **WHY** | I don't understand the reason | "Why would they design it this way?" |
| **WHAT** | I don't understand the thing itself | "What even IS a derivative?" |
| **WHICH** | I can't tell options apart | "Which of these frameworks should I use?" |
| **WHEN** | I don't understand the timing/sequence | "When does this step happen relative to that one?" |
| **WHO** | I don't understand the actors/responsibilities | "Who is supposed to handle this?" |

```
[C3] TYPED_CONFUSION: "I'm confused about [HOW/WHY/WHAT/WHICH/WHEN/WHO] [specific statement]"
```

---

## Phase 2: Map What You Know vs. Don't Know

```
[C4] I UNDERSTAND:
  1. [thing you're clear on]
  2. [thing you're clear on]
  3. [thing you're clear on]

[C5] I DON'T UNDERSTAND:
  1. [specific gap]
  2. [specific gap]

[C6] THE BOUNDARY: [where understanding stops and confusion begins]
```

The boundary is the most important finding. It's the exact point where things stop making sense.

---

## Phase 3: Identify the Gap Type

```
[C7] GAP_TYPE: [facts | concepts | connections]
```

| Gap Type | Signal | You're Missing... | Fix |
|----------|--------|-------------------|-----|
| **Facts** | "I don't have the information" | Data, definitions, specifics | Look it up. The answer exists somewhere. |
| **Concepts** | "I have the info but don't get it" | A mental model for how it works | Find an analogy. Map the unfamiliar to the familiar. |
| **Connections** | "I get the pieces but not how they fit" | The relationship between things you understand | Draw it out. Visualize the connections. |

---

## Phase 4: Close the Gap

### For Facts Gaps

```
[C8-F] MISSING_FACTS:
  1. [what specific fact/data is needed]
  2. [what specific fact/data is needed]

[C9-F] WHERE_TO_FIND: [source — documentation, person, research]
[C10-F] QUICK_CHECK: Can this be answered in under 5 minutes?
  - If yes: go look it up now.
  - If no: note it and work around the gap temporarily.
```

### For Concept Gaps

```
[C8-C] UNFAMILIAR_CONCEPT: [the thing you don't get]
[C9-C] FAMILIAR_ANALOG: [what's the closest thing you DO understand that's similar?]
[C10-C] ANALOGY: "[Unfamiliar concept] is like [familiar thing] because [shared structure], except [key difference]."
[C11-C] TEST: Does this analogy hold? Where does it break down?
```

### For Connection Gaps

```
[C8-X] PIECES: [list the things you understand individually]
[C9-X] MISSING_LINK: [what relationship between them is unclear]
[C10-X] DRAW_IT:
  [A] --[relationship?]--> [B] --[relationship?]--> [C]

[C11-X] SEQUENCE_CHECK: Is the confusion about:
  - Cause and effect? (A causes B? Or B causes A?)
  - Sequence? (Does A happen before or after B?)
  - Hierarchy? (Is A part of B, or is B part of A?)
  - Dependency? (Does A require B?)
```

---

## Phase 5: Output

```
CONFUSED
========

RAW: [what the user said]
TYPED: "I'm confused about [HOW/WHY/WHAT/WHICH/WHEN/WHO] [specific]"

I UNDERSTAND:
  - [known thing 1]
  - [known thing 2]

I DON'T UNDERSTAND:
  - [gap 1]
  - [gap 2]

THE BOUNDARY: [where understanding stops]

GAP TYPE: [facts | concepts | connections]

TO CLOSE THE GAP:
  [Specific action based on gap type]

AFTER CLOSING:
  Re-state the thing that confused you. If it now makes sense, you're done.
  If new confusion emerged, you moved the boundary — that's progress. Run /cnfsd again on the new confusion.

READY FOR:
- /lr [topic] — if the facts gap requires research
- /fohw [system] — if the connection gap is about how a system works
- /aex [assumption] — if the confusion might stem from a wrong assumption
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Staying vague** | "I'm just confused" without typing the confusion | Push for the HOW/WHY/WHAT/WHICH — name it precisely |
| **Wrong gap type** | Treating a concept gap as a facts gap (looking up info that doesn't help) | If looking it up didn't help, it's not a facts gap — try analogy |
| **Skipping the known** | Jumping to what's confusing without mapping what's clear | Always map understanding first — it's the foundation |
| **Shame spiral** | "I should understand this" blocking the process | Confusion is evidence of engagement, not failure |
| **Premature resolution** | Accepting "I sort of get it" when you don't | Test understanding: can you explain it to someone else? If not, the gap is still open |

---

## Depth Scaling

| Depth | Phases | Gap Resolution | Follow-up |
|-------|--------|---------------|-----------|
| 1x | Name + gap type | Single action | None |
| 2x | Full mapping + gap type | Action + test | Verification |
| 4x | Deep mapping + multiple gaps | Multiple actions | Re-map after each |
| 8x | Full + root cause of confusion | Complete resolution path | Pattern analysis of recurring confusion |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Confusion typed precisely (HOW/WHY/WHAT/WHICH/WHEN/WHO)
- [ ] Known territory mapped (what IS understood)
- [ ] Unknown territory mapped (what ISN'T understood)
- [ ] Boundary identified
- [ ] Gap type classified (facts/concepts/connections)
- [ ] Specific action for closing the gap provided
- [ ] No shame or judgment in the output

---

## Integration

- Use from: "I'm confused", "this doesn't make sense", "I don't get it", mental fog
- Routes to: `/lr` (research for fact gaps), `/fohw` (system understanding), `/aex` (assumption checking)
- Differs from `/idk`: idk has no information at all; cnfsd has information that doesn't cohere
- Differs from `/unsure`: unsure understands but doesn't trust; cnfsd doesn't understand
- Differs from `/lost`: lost had understanding and lost direction; cnfsd can't form understanding
