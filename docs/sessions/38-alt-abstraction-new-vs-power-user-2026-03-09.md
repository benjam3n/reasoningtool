# /alt What's the right level of abstraction for presenting skills to a new user vs a power user?
**Date:** 2026-03-09
**Skill:** /alt (Abstraction Level)

---

## Interpretation

This matches **Interpretation 3 — Audience mismatch**: You understand the skill system fine, but need to pitch it at different abstraction levels for two different audiences (new users vs. power users). The question is about matching altitude to audience.

This also has a **deciding** component: you need to decide what to show at each level. I will run both **SECTION D** (communicating/audience matching) as the primary analysis, and **SECTION B** (deciding) as a secondary check.

---

## SECTION D: Explaining / Communicating Something

### Step D1: Identify your audiences.

There are two audiences:

- **Audience A**: A new user who has never used the reasoning toolkit before.
- **Audience B**: A power user who knows the system and wants direct access to specific procedures.

### Step D2: Assess each audience's current altitude.

**Audience A (new user)** — They know nothing.
- They do not know what a "skill" is in this context.
- They do not know the difference between `/claim` and `/aex`.
- They have a PROBLEM or QUESTION but no vocabulary for the toolkit.
- **Prescription**: Start ABSTRACT. Give them the big picture first, then offer concrete examples as illustrations. Structure: "[What you're trying to do] maps to [this category]."

**Audience B (power user)** — They are experts.
- They know what `/aex` does without reading the description.
- They want to find a specific tool quickly, or discover one they haven't used.
- They already have the abstract framework in their head.
- **Prescription**: Start CONCRETE. Give them the specific tool names. They already have the map.

### Step D3: Verify altitude match against current design.

Current design: **All tiers are visible simultaneously** — category skills, tier 1, tier 2, tier 3 (by category), and experimental. This creates an altitude mismatch for BOTH audiences:

| Audience | Problem with current design |
|----------|----------------------------|
| New user | **Too detailed / lost.** They see 500+ skills and cannot orient. The category skills (which are their correct entry point) are buried among equal-weight alternatives. The signal is drowned in noise. |
| Power user | **No problem, actually.** They can scan, Ctrl+F, or browse by category. The flat display works for them. But they get no benefit from the category skills cluttering their view either. |

**Diagnosis**: The current design is at the WRONG altitude for new users and at a tolerable-but-not-ideal altitude for power users.

### Step D4: Altitude bridges — what each audience needs.

**For new users (start abstract, bridge to concrete):**

What they need to see first:

| You have... | Start here |
|---|---|
| A claim to test | `/claim` |
| A decision to make | `/decide` |
| Something broken | `/diagnose` |
| A goal or want | `/want` |
| A question about how | `/how` |

This is the abstract layer. The bridge sentence is built into the category skill itself — it routes them to the concrete tool. The new user never needs to see tier 1/2/3 directly. The system navigates for them.

**For power users (start concrete, allow abstract fallback):**

What they need to see:

- A searchable/filterable list of all skills by name
- Grouping by function (decision-making, analysis, validation, etc.) rather than by tier
- Quick-reference of the short name and one-line description
- The tier labels become useful metadata (not primary navigation)

---

## SECTION B: Deciding — What should the actual design be?

### Step B1: Name the decision.

"I need to decide how to structure the skill presentation so it works for both new and power users."

### Step B2: Identify the decision's natural level.

1. Who is affected? All users of the toolkit. --> More abstract.
2. How long will this decision matter? As long as the toolkit exists. --> Abstract.
3. What breaks if wrong? New users bounce; power users tolerate it but don't love it. --> Abstract (user retention and adoption).

Natural level: **ABSTRACT** — this is an information architecture decision.

### Step B3: Check one level UP.

"What larger goal does this serve?" --> Making the toolkit accessible and useful to people who encounter it.

"Does knowing this change which option I should pick?" --> YES. The larger goal reveals that the real bottleneck is **new user onboarding**, not power user efficiency. Power users already cope. New users leave. So the design should be optimized primarily for the new user experience, with power user access as a secondary mode.

### Step B4: Check one level DOWN.

"What specific, concrete thing will happen first?"

- **If I show everything**: A new user lands on the page, sees 500+ skills, feels overwhelmed, and either leaves or picks randomly and gets a poor result.
- **If I show only categories**: A new user sees 17 entry points organized by what they're trying to do. They pick one. The system routes them. They have a good first experience. A power user who wants `/pbr` specifically has to click through to find it.

"Does seeing these concrete consequences change my preference?" --> Yes. It confirms that a **progressive disclosure** model is correct: categories first, everything else on demand.

### Step B5: Decision at validated level.

**The right abstraction levels are:**

**Layer 0 — Entry (new users):** Show ONLY the category skills, framed as situations ("I have a claim to test", "I need to make a decision"). No skill names. No jargon. No tiers. Just: "What are you trying to do?"

**Layer 1 — Browse (intermediate users):** One click deeper, show tier 1 skills grouped by function. These are the "power tools" — the user now knows enough to pick a specific analytical approach.

**Layer 2 — Full catalog (power users):** Searchable, filterable, all 500+ skills. Grouped by function, tagged by tier. This is a reference, not a starting point.

---

## Concrete Recommendation

| Layer | Who it's for | What they see | How they get there |
|---|---|---|---|
| **Entry** | New users, first visit | 8-10 situation cards: "I have a claim", "I need to decide", "Something's broken", etc. | Default landing page |
| **Browse** | Users who've used it once or twice | Tier 1 + Tier 2 skills, grouped by function (Decision, Analysis, Validation, Ideation, etc.) | "Browse all tools" link or tab |
| **Catalog** | Power users | Full searchable list with filters by tier, category, function | "Full catalog" link or tab |

### The key altitude insight

The **category skills already solve the altitude problem at the interaction level** — they take natural-language input ("I have a claim to test") and route to the right concrete tool. The missing piece is that the **presentation layer doesn't match this architecture**. The routing logic is correct; the UI flattens it.

The fix is not to change the skills. The fix is to make the UI match the skill architecture's own abstraction hierarchy: category skills are the entry points, tier 1 skills are the toolkit, and everything else is the reference library.

### What to avoid

1. **Don't hide skills from power users.** Progressive disclosure means "show the right thing first," not "make experts click through five layers." A single "show all" toggle or search bar solves this.
2. **Don't label tiers as tiers.** "Tier 1" and "Tier 3" mean nothing to users. Group by function ("Decision tools", "Analysis tools") or by situation ("When you're stuck", "When you need to validate").
3. **Don't assume new users will read instructions.** They will scan for 3-5 seconds and either click something or leave. The entry layer must be immediately scannable: short phrases, clear situations, no jargon.

---

## Altitude Trace

The input was at the **problem level**: "what's the right abstraction?" I zoomed out once to find the larger goal (accessibility and adoption), which revealed that the new-user experience is the bottleneck. I zoomed in once to see concrete consequences (what happens when someone lands on the page), which confirmed progressive disclosure as the pattern. The answer lives at the **information architecture level** — neither as abstract as "what's our product strategy" nor as concrete as "what CSS should we use."
