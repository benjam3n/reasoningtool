---
name: "story - Story"
description: Generate a narrative — fiction, parable, scenario, or illustrative story — that embodies a concept, explores a question, or makes an idea vivid.
---

# Story

**Input**: $ARGUMENTS

---

## Step 1: DETERMINE THE STORY TYPE

What kind of story is needed?

| Type | Purpose | Structure |
|------|---------|-----------|
| **PARABLE** | Teach a principle through analogy | Setup → Conflict → Resolution → Moral |
| **SCENARIO** | Explore a possible future | Context → Events → Consequences |
| **VIGNETTE** | Make an abstract idea concrete | Moment → Detail → Insight |
| **ALLEGORY** | Represent complex dynamics with simpler ones | World-building → Parallel events → Recognition |
| **FABLE** | Illustrate a moral through characters | Characters → Choices → Outcomes → Lesson |
| **THOUGHT EXPERIMENT** | Test an idea by inhabiting it | Premise → "What if..." → Implications |

If the user specifies a type, use it. Otherwise, choose the best fit for the input.

---

## Step 2: EXTRACT THE CORE

What is this story really about?

1. **Theme**: What idea, tension, or question does it explore?
2. **Stakes**: What matters? What's at risk?
3. **Perspective**: Whose eyes do we see through?
4. **Emotion**: What should the reader feel?

```
CORE:
Theme: [the idea]
Stakes: [what matters]
Perspective: [whose story]
Target emotion: [what the reader should feel]
```

---

## Step 3: BUILD THE ELEMENTS

### Characters (if applicable)
- Who wants what?
- What's in their way?
- What do they believe that gets tested?

### Setting
- When and where?
- What makes this world different from ours (if anything)?
- What rules govern this world?

### Conflict
- What tension drives the story?
- Is it person vs person, person vs system, person vs self, or person vs nature?
- What makes it hard to resolve?

### Arc
- Beginning: What is the status quo?
- Middle: What disrupts it?
- End: What is the new state?

---

## Step 4: WRITE THE STORY

Write the story. Follow these principles:

1. **Show, don't tell** — Use concrete detail, not abstract summary
2. **Start in the middle** — Begin where it's interesting, not at the chronological start
3. **Specific > generic** — "A cracked blue mug" not "a cup"
4. **Earn the ending** — The conclusion should feel inevitable in hindsight
5. **Trust the reader** — Don't explain the meaning; let the story carry it
6. **Appropriate length** — Match length to complexity. A vignette can be 200 words. An allegory might need 2000.

---

## Step 5: THE STORY

```
[Title]

[The story itself]
```

---

## Step 6: REFLECTION (optional, only if requested)

If the user wants analysis of the story:

```
STORY ANALYSIS:
Theme: [what it explores]
Key insight: [what the story reveals]
Connection to input: [how it relates to what was asked]
What the story tests: [what assumption or idea is being examined]
```

---

## Integration

Use with:
- `/w` -> For non-fiction writing
- `/stl` -> For style guidance
- `/utp` -> Generate a utopian story
- `/dys` -> Generate a dystopian story
- `/fut` -> Ground stories in plausible futures
- `/eth` -> Explore ethical dilemmas through narrative
