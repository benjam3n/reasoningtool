---
name: "vdp - Visual Design Principles"
description: Eight principles of visual design derived from first principles (cognitive load, gestalt perception, reading research). Use as a gate before any visual design work -- every design decision should trace back to one of these principles. If a design element can't be justified by a principle, remove it.
---

# Visual Design Principles

**Input**: $ARGUMENTS

---

## Purpose

These principles were derived from first principles during a UAUA 16x session on website design. They answer the question: what makes a design look good, and can we derive that from something more fundamental than taste?

The answer: yes, partially. Good design reduces cognitive load, matches visual hierarchy to information hierarchy, and makes the content -- not the design -- the thing the reader notices.

**What this produces**: A set of gates that any design decision must pass. If a decision can't be justified by at least one principle, it's decoration, and decoration competes with content.

**Source**: uaua_2026-01-29_website-design.md

---

## The Eight Principles

### Principle 1: Visual hierarchy must match information hierarchy

**Derivation**: The eye scans before it reads. If the most important information isn't the most visually prominent, the reader processes information in the wrong order. This wastes time and damages comprehension.

**Rule**: importance -> visual weight. If title > subtitle > body > caption, then visual weight must follow: largest/boldest -> large/medium -> regular -> small/light.

**Gate**: For any page, can a stranger identify the information hierarchy from a 2-second glance? If not, the visual hierarchy is broken.

**Test**: Squint test -- blur the page. The most important elements should still be the most visible.

---

### Principle 2: Consistency signals intentionality

**Derivation**: When elements that serve the same function look the same, the reader builds a mental model. When they look different, the reader must re-learn. Inconsistency reads as accident, which reads as incompetence.

**Rule**: same function -> same form. Every card should look like every other card. Every heading at the same level should have the same size/weight/color.

**Gate**: Pick any two instances of the same element type (e.g., two cards, two H2s, two buttons). Do they look identical? If not, which one is wrong?

**Test**: Catalog all instances of each element type. Any visual difference between instances of the same type is a bug unless justified by different function.

---

### Principle 3: Whitespace is structural, not empty

**Derivation**: The space between elements groups related things and separates unrelated things. Insufficient spacing makes everything feel cramped and related. Excessive spacing makes elements feel disconnected. The eye uses proximity to infer grouping (Gestalt law of proximity).

**Rule**: spatial proximity -> perceived relationship. Related elements need less space between them than unrelated elements.

**Gate**: For any group of elements, does the spacing communicate the correct relationships? Are related items closer together than unrelated items?

**Test**: If you remove all borders, lines, and boxes, can you still tell which elements are grouped? If the answer depends on spacing alone, the spacing is doing its job.

---

### Principle 4: Fewer typefaces, sizes, and colors = more clarity

**Derivation**: Each distinct visual style creates a category the reader must process. Minimizing categories reduces cognitive load. Two fonts, four sizes, three colors can express everything needed.

**Rule**: Minimize the number of distinct visual categories. Each new font, size, weight, or color must justify its existence by serving a function not already served.

**Gate**: List every distinct font/size/weight/color combination on the page. For each, what function does it serve? If two styles serve the same function, merge them. If a style serves no function, remove it.

**Specific maximums**:
- Typefaces: 2 design fonts (e.g., sans for headings, serif for body) + 1 functional (monospace for code)
- Sizes: 5-6 steps on a consistent scale (e.g., Major Third 1.25x ratio)
- Colors: 1 accent color + neutrals (text, background, borders)

---

### Principle 5: Alignment creates order

**Derivation**: Elements on a shared grid or baseline create invisible lines that the eye follows. Misaligned elements break these lines and create visual noise. The brain perceives aligned elements as intentional and misaligned elements as accidental.

**Rule**: geometric regularity -> perceived order -> trust. All elements should sit on a shared grid.

**Gate**: Draw vertical and horizontal lines through the page. Do elements align to these lines, or are there arbitrary offsets?

**Specific implementation**: Use an 8px grid for all spacing. Multiples of 8 (8/16/24/32/48/64/96/128) cover every spacing need. Use 4px only for fine adjustments inside small components.

---

### Principle 6: Contrast controls attention

**Derivation**: The eye is drawn to what's different. High contrast (dark on light, large on small, colored on neutral) attracts attention. Low contrast recedes. This is Gestalt figure-ground.

**Rule**: difference -> attention. Use high contrast for what matters (headings, calls to action, key content), low contrast for what's secondary (captions, metadata, supporting text).

**Gate**: What does the reader look at first? Is that the most important thing on the page? If the reader's eye goes to a secondary element first, contrast is misallocated.

**Specific requirement**: Body text contrast ratio must meet WCAG AA minimum (4.5:1). For headings (large text), 3:1 minimum. Aim for AAA (7:1) when possible.

---

### Principle 7: Typography legibility has measurable properties

**Derivation**: These are not aesthetic preferences. They're the result of reading research and optometry.

**Rules**:
| Property | Optimal Range | Why |
|----------|--------------|-----|
| Line length | 45-75 characters (~550-700px) | Beyond 75, the eye loses track returning to the next line |
| Line height | 1.5-1.7 for body text | Below 1.5, lines feel cramped. Above 1.7, the eye struggles to connect lines |
| Font size | 16-20px for body text | Below 16, reading requires effort on most screens |
| Paragraph spacing | > line spacing | Must visually separate paragraphs more than lines within paragraphs |

**Gate**: Measure these properties on every text-heavy page. Any value outside optimal range needs justification.

**Specific implementation for editorial/essay sites**:
- Body: 18px, line-height 1.65
- Max prose width: 680px (~65 characters at 18px)
- Paragraph spacing: 1.5em (larger than line-height)

---

### Principle 8: The design should be invisible

**Derivation**: If the reader notices the design, the design is competing with the content. Good design creates the conditions for content to be absorbed without drawing attention to itself. The reader should notice the IDEAS, not the layout.

**Rule**: design serves content. If design draws attention to itself, it's failing.

**Gate**: After reading a page, does the reader think about what they read or how the page looked? If the latter, the design is too loud.

**What this rules out**:
- Decorative elements (gradients, shadows, illustrations) that don't serve information hierarchy
- Animations that don't serve navigation or state change
- Background patterns or textures
- Unusual layouts that require the reader to learn how to read the page
- Colored backgrounds behind text (unless for a specific functional purpose like code blocks or callouts)

**What this does NOT rule out**:
- Beautiful typography (this IS invisible -- it makes reading effortless)
- Generous whitespace (this is structural, not decorative)
- Considered color (one accent color, applied consistently to interactive elements)
- Subtle transitions on hover/focus (these serve feedback, not decoration)

---

## Application Procedure

When making any design decision:

1. **Identify which principle(s) justify this decision.** If none do, the decision is decoration. Remove it.

2. **Check for conflicts.** Some decisions satisfy one principle but violate another (e.g., a large decorative header satisfies contrast but violates invisible design). When principles conflict, Principle 8 (invisible design) wins for content-heavy sites. Principle 6 (contrast/attention) wins for action-oriented pages.

3. **Test with gates.** Each principle has a gate test. Run them. Fail any gate = revise the design.

4. **Iterate.** Design is not one-pass. Apply principles -> test -> revise -> test again.

---

## Derived Design Decisions (from UAUA session)

These specific decisions were validated through the UAUA 16x process and trace to the principles above:

| Decision | Traces to Principle |
|----------|-------------------|
| Serif body + sans headings | P1 (hierarchy), P4 (two fonts), P7 (legibility) |
| 680px max prose width | P7 (measurable legibility) |
| 18px body, 1.65 line-height | P7 (measurable legibility) |
| Near-black on warm white (#1a1a1a on #faf9f6) | P6 (contrast), P7 (legibility) |
| One accent color (#3d5a80 deep muted blue) | P4 (fewer colors), P6 (contrast for links) |
| 8px spacing grid | P5 (alignment), P3 (structural whitespace) |
| No decorative elements | P8 (invisible design) |
| Content-specific layouts | P1 (hierarchy matches info type) |
| Major Third type scale (1.25x) | P4 (limited sizes), P1 (clear hierarchy) |

---

## When to Use This Skill

| Situation | Use |
|-----------|-----|
| Building a new website or page | Apply all 8 principles as gates before finalizing |
| Reviewing an existing design | Run each gate test, catalog violations |
| Choosing between design options | Which option satisfies more principles? |
| Debating a design decision | Trace both positions to principles. The one with stronger grounding wins. |
| "This looks wrong but I can't say why" | Walk through principles 1-8. The violated principle is the diagnosis. |

---

## What This Skill Does NOT Cover

- Brand identity (what should this look/feel like?) -- use /pos
- Color psychology specifics -- use /fia on color theory
- Interaction design (how should this behave?) -- different domain
- Information architecture (what pages, what structure?) -- use /dcm
- Content strategy (what to write?) -- use /cts

This skill covers **visual execution** -- given content and structure, how to present it so the reader absorbs the content without noticing the design.
