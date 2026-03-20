---
name: "onar - Narrative Generation"
description: Generates structured narratives that tell a clear story. Takes a topic or set of facts and arranges them into a coherent narrative with a through-line, transitions, and purpose-driven structure.
output:
  format: "prose"
---

# Narrative Generation

**Input**: $ARGUMENTS

---

## Step 1: Identify the Story

Determine what kind of narrative this is and what story is being told.

| Structure | When to use | Example |
|-----------|-------------|---------|
| **CHRONOLOGICAL** | Events over time | Project history, incident timeline |
| **CAUSAL** | Cause-and-effect chain | Root cause explanation, impact analysis |
| **THEMATIC** | Organized by themes | Strategy overview, state-of-the-world |
| **PROBLEM-SOLUTION** | Setup then resolution | Proposal, case study |
| **COMPARATIVE** | Two paths contrasted | Before/after, option A vs B |

```
NARRATIVE TYPE: [CHRONOLOGICAL / CAUSAL / THEMATIC / PROBLEM-SOLUTION / COMPARATIVE]
STORY IN ONE SENTENCE: [the core story being told]
```

---

## Step 2: Establish the Through-Line

The through-line is the single thread that connects every part of the narrative. Without it, the narrative is just a list of facts.

```
THROUGH-LINE: [the connecting idea that ties everything together]
AUDIENCE: [who is reading this]
PURPOSE: [inform / persuade / explain / motivate / document]
```

Rules:
- Every section must connect back to the through-line
- If a fact doesn't serve the through-line, cut it or rethink the through-line
- The through-line should be statable in one sentence

---

## Step 3: Select Key Points

Gather the raw material and select what belongs in the narrative.

```
KEY POINTS:
1. [point] — [why it matters to the story]
2. [point] — [why it matters to the story]
3. [point] — [why it matters to the story]
...

EXCLUDED:
- [point cut] — [why it doesn't serve the narrative]
```

Rules:
- Include only what advances the through-line
- Aim for 4-8 key points; fewer is usually better
- Each point should earn its place

---

## Step 4: Arrange for Clarity

Order the key points using the chosen structure. Design the narrative arc.

```
NARRATIVE ARC:
1. OPENING: [hook or context-setting — why should the reader care?]
2. BODY:
   a. [first major point or section]
   b. [second major point or section]
   c. [third major point or section]
   ...
3. CLOSING: [conclusion, call to action, or forward look]
```

Rules:
- Open with the most compelling or orienting point
- Build momentum — each section should raise stakes or deepen understanding
- Close with what matters most: the implication, the ask, or the next step

---

## Step 5: Write Transitions

Connect each section to the next. Transitions do the heavy lifting of making a narrative feel coherent rather than choppy.

For each section boundary, draft a transition that:
- Closes the previous idea
- Opens the next idea
- Makes the logical connection explicit

---

## Step 6: Validate Against Purpose

Check that the narrative serves its intended purpose:

- **Inform**: Does the reader understand the situation after reading?
- **Persuade**: Is the argument logical and the evidence compelling?
- **Explain**: Could someone unfamiliar with the topic follow this?
- **Motivate**: Does it create urgency or desire to act?
- **Document**: Is it complete enough to stand on its own?

```
PURPOSE CHECK: [does the narrative achieve its goal? what's missing?]

GENERATION FAILURE CHECK:
- Voice collapse: Read the narrative aloud. Does it sound like a specific person telling a specific story, or does it sound like "professional writing"? Could any AI assistant have produced this? If yes, the voice has collapsed. Rewrite with concrete sensory details, unusual word choices, or rhythms that belong to THIS story.
- Cached narrative: Is the story following a stock arc (hero's journey, underdog triumph, lesson-learned) because it's the default, or because it's actually the right structure? Test: has this exact narrative shape been used in 10,000 other pieces? If the structure is predictable, the narrative isn't doing work — it's performing "story."
- False structure: Remove all headers and formatting. Does the narrative still flow and make sense? If it falls apart without structural scaffolding, the structure was doing the thinking. The prose should carry the story on its own.
- Aspiration as conclusion: Does the narrative end with "and so we look forward to..." or "the future holds promise"? Delete the last paragraph. If the piece is better, the ending was filler. End on something concrete and specific.
```

---

## Step 7: Deliver

Present the complete narrative, formatted for its audience and purpose.

---

## Integration

Use with:
- `/pw` -> Apply professional writing standards to the narrative
- `/stl` -> Match a specific style or tone
- `/olst` -> Generate supporting lists within the narrative
- `/odec` -> Embed a decision recommendation in narrative form
