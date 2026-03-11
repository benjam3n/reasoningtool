# /sya Map the system of how ideas go from "vague intuition" to "clear actionable plan"
**Date:** 2026-03-09
**Skill:** /sya (Systems Analysis)

---

## Interpretation

**Interpretation 3 — Map an unfamiliar system.** The user wants to understand the structural dynamics of how humans move from vague intuitions to clear actionable plans — the key variables, feedback loops, and archetypes — in order to identify where reasoning tools add the most value.

---

## Step 1: Define System Boundary

### Behavior We're Trying to Understand

The process by which a fuzzy, felt-sense intuition transforms into a concrete, executable plan. This is not a clean linear pipeline — it exhibits:

- **S-curve progression**: Long flat periods of confusion, then sudden clarity bursts, then diminishing returns on refinement
- **Oscillation**: Cycling between expanding (divergent) and narrowing (convergent) phases
- **Frequent regression**: Apparent clarity collapses back into confusion when tested

### System Boundary

**Inside the boundary:**
- The thinker's mental state (clarity, confidence, motivation)
- The idea itself (specificity, testability, coherence)
- External feedback (from people, reality, tools)
- The thinker's processes (articulation, testing, structuring)
- Time and attention as finite resources

**Outside the boundary (treated as given):**
- The initial trigger of the intuition
- Domain expertise already possessed
- External circumstances that constrain implementation

**Time horizon:** Minutes to weeks. A single thinking session (30-90 min) is the dominant unit, but the full journey can span days or weeks with multiple sessions.

### Key Variables

**Stocks (things that accumulate):**

| Stock | Description | Typical Level |
|-------|-------------|---------------|
| **Idea Clarity** | How well-defined the idea is — from vague feeling to precise specification | Starts near zero |
| **Articulated Structure** | Explicit language, diagrams, frameworks attached to the idea | Starts at zero |
| **Confidence** | The thinker's belief that the idea is worth pursuing and that they understand it | Volatile |
| **Commitment** | Psychological investment in a particular framing or direction | Grows gradually, sometimes too fast |
| **Evidence Base** | Facts, data, examples, and tested assumptions supporting the idea | Starts thin |
| **Unresolved Questions** | Open questions, contradictions, and unknowns the thinker is aware of | Starts high, should decrease but often grows first |
| **Motivation/Energy** | Willingness to keep working on the idea | Depletes over time |

**Flows (rates of change):**

| Flow | Affects Stock | Direction |
|------|--------------|-----------|
| Articulation attempts | +Articulated Structure, +Idea Clarity | Inflow |
| External feedback | +/- Confidence, +Evidence Base, +Unresolved Questions | Mixed |
| Assumption testing | -Unresolved Questions, +Evidence Base, +/-Confidence | Mixed |
| Premature commitment | +Commitment, -Unresolved Questions (suppressed, not resolved) | Dangerous inflow |
| Cognitive fatigue | -Motivation/Energy | Outflow |
| Clarity breakthroughs | +Idea Clarity, +Confidence, +Motivation | Burst inflow |
| Scope expansion | +Unresolved Questions, -Idea Clarity | Outflow/inflow |
| Structuring/framing | +Articulated Structure, +Idea Clarity | Inflow |
| Reality contact | +/-Evidence Base, +/-Confidence | Mixed |

### Time Scale

The dominant time constant is **the thinking session** (30-90 minutes). Within a session, feedback loops operate on the scale of minutes. Across sessions, there are delays of hours to days where subconscious processing occurs.

---

## Step 2: Causal Relationships

### Core Causal Map

```
ARTICULATION ATTEMPTS
        |
        | (+)
        v
ARTICULATED STRUCTURE ──(+)──> IDEA CLARITY
        |                           |
        | (+)                       | (+)
        v                           v
TESTABLE CLAIMS              CONFIDENCE
        |                      |       |
        | (+)                  | (+)   | (+)
        v                      v       v
ASSUMPTION TESTING      MOTIVATION   COMMITMENT
        |                  |              |
        | (+/-)            | (+)          | (-)
        v                  v              v
EVIDENCE BASE      ARTICULATION    WILLINGNESS TO
        |           ATTEMPTS        QUESTION
        | (+)                           |
        v                               | (-)
IDEA CLARITY                            v
                                  UNRESOLVED
                                  QUESTIONS
                                  (acknowledged)
                                        |
                                        | (-)
                                        v
                                  IDEA CLARITY
                                  (undermined)

COGNITIVE FATIGUE ──(-)──> MOTIVATION ──(+)──> ARTICULATION ATTEMPTS

EXTERNAL FEEDBACK ──(+)──> UNRESOLVED QUESTIONS
                  ──(+)──> EVIDENCE BASE
                  ──(+/-)──> CONFIDENCE
```

### Key Causal Links with Mechanisms

1. **Articulation Attempts → (+) Articulated Structure**: Every time you try to write down, speak, or diagram the idea, some structure gets captured. Even failed attempts leave residue.

2. **Articulated Structure → (+) Idea Clarity**: Externalized structure makes gaps visible, enables manipulation, and reduces cognitive load. This is the core engine.

3. **Idea Clarity → (+) Confidence**: Clearer ideas feel more real and achievable. Understanding what you mean increases trust in the idea.

4. **Confidence → (+) Motivation**: Believing the idea is going somewhere sustains effort.

5. **Confidence → (+) Commitment**: Higher confidence narrows focus toward the current framing. This is double-edged.

6. **Commitment → (-) Willingness to Question**: As psychological investment grows, challenging the current framing becomes threatening. Sunk cost dynamics.

7. **Willingness to Question → (+) Acknowledged Unresolved Questions**: Only noticed if you're looking. Commitment suppresses this.

8. **Unresolved Questions → (-) Idea Clarity**: Each real open question is a gap in the structure. Acknowledging them temporarily reduces felt clarity.

9. **Evidence Base → (+) Idea Clarity**: Tested assumptions replace speculation with grounded knowledge. Real clarity vs. false clarity.

10. **Cognitive Fatigue → (-) Motivation**: Thinking is tiring. The longer you work, the less energy remains, regardless of progress.

---

## Step 3: Feedback Loops

### Loop R1: The Articulation Engine (Reinforcing — Virtuous)
```
Articulation Attempts → (+) Articulated Structure → (+) Idea Clarity
    → (+) Confidence → (+) Motivation → (+) Articulation Attempts
```
**Classification:** Reinforcing (all positive links)
**Behavior:** The core virtuous cycle. Trying to express the idea creates structure, which creates clarity, which creates confidence, which creates motivation to keep articulating. This is the engine that drives ideas forward.
**Strength:** Dominant in early-to-mid stages when progress is noticeable.
**Delays:** Articulation → Structure can be slow if the thinker lacks frameworks.

### Loop R2: The Commitment Trap (Reinforcing — Vicious)
```
Confidence → (+) Commitment → (-) Willingness to Question
    → (-) Acknowledged Unresolved Questions → (-) [perceived] Idea Clarity Loss
    → effectively (+) perceived Confidence
```
**Classification:** Reinforcing (even number of negatives)
**Behavior:** As confidence grows, commitment grows, which suppresses questioning, which hides problems, which maintains false confidence. This creates the illusion of clarity — the idea feels done but isn't actually tested.
**Strength:** Grows over time, especially under deadline pressure.
**Delays:** The consequences of suppressed questions only appear when the plan meets reality — potentially weeks or months later.

### Loop B1: The Questioning Brake (Balancing)
```
Idea Clarity → (+) Confidence → (+) Motivation → (+) Assumption Testing
    → (+) Unresolved Questions → (-) Idea Clarity
```
**Classification:** Balancing (one negative link)
**Behavior:** As clarity increases, the thinker has enough confidence and energy to test assumptions, which reveals new questions, which pulls clarity back down. This is a healthy corrective loop that prevents premature convergence.
**Strength:** Only operates when the thinker actively tests assumptions rather than just building structure.
**Delays:** Assumption testing takes time and contact with reality.

### Loop B2: The Fatigue Brake (Balancing)
```
Articulation Attempts → (+) Cognitive Fatigue → (-) Motivation
    → (-) Articulation Attempts
```
**Classification:** Balancing (one negative in effective loop)
**Behavior:** Effort depletes energy. The harder you work, the more tired you get, the less you can work. This loop enforces natural stopping points.
**Strength:** Always present, increasingly dominant as session length grows.
**Delays:** Fatigue accumulates faster than people realize. Diminishing returns set in well before the thinker notices.

### Loop R3: The Scope Creep Spiral (Reinforcing — Vicious)
```
Idea Clarity → (+) Visible Adjacent Questions → (+) Scope Expansion
    → (+) Unresolved Questions → (-) Idea Clarity → (-) Confidence
    → (-) Motivation → (-) Articulation Attempts → (-) Idea Clarity
```
**Classification:** Reinforcing (when it triggers, each gain in clarity reveals more to do, and the expanding scope can outrun the thinker's capacity)
**Behavior:** The better you understand the idea, the more you see what else needs to be figured out. If scope expands faster than clarity accumulates, the thinker feels like they're falling behind — understanding more but knowing less. Can spiral into paralysis.
**Strength:** Strongest for complex, interconnected problems. Weak for simple ideas.

### Loop B3: External Feedback Correction (Balancing)
```
Articulated Structure → (+) Ability to Get Feedback → (+) External Feedback
    → (+) Evidence Base → (+) Idea Clarity (corrected)
    → also (+) Unresolved Questions → (-) premature Confidence
```
**Classification:** Balancing
**Behavior:** Sharing articulated structure with others generates feedback that corrects the idea. This is the most powerful reality-check mechanism. It both builds real clarity and deflates false confidence.
**Strength:** Only operates when the thinker shares work in progress. Many people wait until they feel "ready" — which means this loop activates too late.

---

## Step 4: Stocks and Flows Model

### Stock 1: IDEA CLARITY

```
[Articulation] ──> [IDEA CLARITY] ──> [Scope Expansion]
[Evidence]     ──>                ──> [Assumption Failure]
[Structuring]  ──>                ──> [Forgetting]
```

- **Inflows:** Successful articulation, tested assumptions, external feedback, structural framing
- **Outflows:** Scope expansion (more territory revealed), assumption failures (foundations collapse), forgetting (not captured)
- **Time to fill:** 1-5 sessions for a moderately complex idea
- **Current level for most people:** Perpetually medium — enough to act on, not enough to act well

### Stock 2: ARTICULATED STRUCTURE

```
[Writing/Diagramming] ──> [ARTICULATED STRUCTURE] ──> [Abandonment]
[Tool Use]            ──>                          ──> [Revision/Deletion]
```

- **Inflows:** Writing, diagramming, speaking aloud, using structured frameworks
- **Outflows:** Abandoning documents, revising away prior structure, losing notes
- **Time to fill:** Proportional to effort. Each session adds to it.
- **Current level for most people:** Low. Most thinking happens in the head and is never externalized.

### Stock 3: CONFIDENCE

```
[Clarity Gains]   ──> [CONFIDENCE] ──> [Assumption Failures]
[Positive Feedback] ──>            ──> [Negative Feedback]
[Early Wins]       ──>            ──> [Comparison to Others]
```

- **Inflows:** Clarity breakthroughs, positive feedback, successful tests
- **Outflows:** Failed tests, negative feedback, encountering superior alternatives
- **Time to fill/drain:** Very fast — can swing dramatically in minutes
- **Current level for most people:** Either too high (false confidence from unexplored ideas) or too low (paralyzed by awareness of complexity)

### Stock 4: MOTIVATION/ENERGY

```
[Progress Signals] ──> [MOTIVATION] ──> [Cognitive Fatigue]
[External Stakes]  ──>              ──> [Confusion]
[Curiosity]        ──>              ──> [Frustration from Regression]
```

- **Inflows:** Visible progress, external deadlines, intrinsic curiosity, clarity breakthroughs
- **Outflows:** Fatigue, confusion, feeling of going in circles, scope overwhelm
- **Time to drain:** Within a single session (60-120 min). Refills between sessions (sleep, rest).
- **Current level for most people:** Sufficient to start, insufficient to finish without external structure

### Stock 5: UNRESOLVED QUESTIONS

```
[Testing/Probing]    ──> [UNRESOLVED QUESTIONS] ──> [Answering/Testing]
[External Feedback]  ──>                         ──> [Suppression/Ignoring]
[Scope Expansion]    ──>                         ──> [Deciding "Out of Scope"]
```

- **Inflows:** Testing, feedback, deeper thinking, scope expansion
- **Outflows:** Resolving through evidence, deciding to ignore, suppressing via commitment
- **Time to drain:** Varies enormously. Some questions resolve in minutes, others never do.
- **Current level for most people:** Underestimated. Most people carry fewer acknowledged questions than actually exist, because commitment suppresses awareness.

---

## Step 5: System Archetypes

### Archetype 1: SHIFTING THE BURDEN — "Thinking vs. Doing"

**Structure:**
- **Symptom:** Idea feels unclear, uncomfortable uncertainty
- **Quick fix:** Jump to action — start building, start writing, start executing before the idea is clear
- **Fundamental solution:** Do the difficult work of articulation, testing, and structuring
- **Side effect:** Acting on an unclear idea produces poor results, which must be reworked, which consumes time that could have been spent clarifying

**Behavior:** Short-term relief ("at least I'm doing something"), long-term waste. The more you skip clarification, the weaker your clarification muscles become.

**Where this shows up:** "Just start coding." "Don't overthink it." "Ship and iterate." These are sometimes right — but they're often the quick fix masquerading as wisdom.

**Leverage:** Build habits and tools that make the fundamental solution (clarification) faster and less aversive, so the quick fix is no longer needed.

### Archetype 2: LIMITS TO GROWTH — "Clarity Plateau"

**Structure:**
- **Reinforcing loop (R1):** Articulation Engine drives increasing clarity
- **Balancing constraint:** Unstructured thinking hits diminishing returns. Without better frameworks, each additional hour of thinking yields less clarity.

**Behavior:** Rapid early progress ("I had a breakthrough in the shower!") followed by a plateau ("I've been going in circles for days").

**Where this shows up:** The thinker's natural capacity to hold and manipulate ideas in their head is the constraint. Working memory is the bottleneck. Once the idea exceeds working memory capacity, progress stalls.

**Leverage:** Externalize. The constraint is internal cognitive capacity. Tools, frameworks, and written structure bypass it.

### Archetype 3: FIXES THAT FAIL — "Premature Commitment"

**Structure:**
- **Problem:** Uncertainty feels bad
- **Fix:** Commit to a specific plan to eliminate uncertainty
- **Unintended consequence:** Commitment suppresses questioning (Loop R2), hiding real problems that surface later as plan failure

**Behavior:** Oscillation. Commit → feel good → plan fails → back to uncertainty → commit again to a different plan → repeat.

**Where this shows up:** "Let's just pick an approach and go with it." Feels decisive. But if done before sufficient testing, the plan carries hidden flaws.

**Leverage:** Separate the feeling of progress from actual commitment. Create ways to feel forward motion while keeping options open — prototyping, scenario planning, conditional plans.

### Archetype 4: GROWTH AND UNDERINVESTMENT — "Not Investing in Thinking Capacity"

**Structure:**
- **Growth:** Ideas get more complex and ambitious over time
- **Underinvestment:** The thinker never upgrades their thinking tools, frameworks, or processes
- **Performance degrades:** Complex ideas outstrip simple thinking tools
- **Self-fulfilling:** "Thinking harder doesn't work" → stop investing → thinking stays weak → complex ideas feel impossible

**Behavior:** The thinker handles simple ideas fine but chokes on complex ones. Concludes they aren't a "big thinker" rather than recognizing the capacity gap.

**Leverage:** Invest in thinking infrastructure — structured frameworks, external tools, practiced procedures — before the need is acute.

---

## Step 6: Leverage Points

Ordered from most to least powerful for this system:

### Leverage Point 1: PARADIGM — "Ideas need to be externalized to be developed" (Level 2)
**Current paradigm:** "Thinking happens in your head. Smart people figure things out by thinking harder."
**Shifted paradigm:** "Thinking happens between your head and external structure. Everyone needs scaffolding. The quality of your external tools determines the complexity of ideas you can handle."
**Leverage:** Highest. This single belief change transforms every downstream behavior. A person who believes thinking requires externalization will naturally write things down, use frameworks, seek feedback, and build structure.
**Feasibility:** Hard to shift via argument. Easier to shift through experience — have them use a framework once and feel the difference.

### Leverage Point 2: INFORMATION FLOWS — "Make the current state of the idea visible" (Level 6)
**Intervention:** Create artifacts that show the thinker where they are: what's clear, what's assumed, what's unknown, what's tested. Make the invisible thinking process visible.
**Leverage:** High. Most stalling happens because the thinker can't see their own progress or gaps. Visibility enables self-correction.
**Feasibility:** High. This is exactly what structured thinking skills do — they create visible artifacts.

### Leverage Point 3: REINFORCING LOOP STRENGTH — "Accelerate the Articulation Engine (R1)" (Level 7)
**Intervention:** Reduce the friction of articulation. Provide scaffolding (templates, prompts, structures) that make it easier to get ideas out of the head and into external form.
**Leverage:** High. Speeding up R1 means faster clarity accumulation, faster confidence, and faster motivation — the whole system runs faster.
**Feasibility:** High. Frameworks, templates, and guided procedures do this directly.

### Leverage Point 4: BALANCING LOOP STRENGTH — "Strengthen the Questioning Brake (B1)" (Level 8)
**Intervention:** Build assumption-testing into the process so it happens naturally rather than requiring separate motivation. Make questioning feel like progress rather than regression.
**Leverage:** Medium-high. Counteracts R2 (the Commitment Trap). Prevents false clarity.
**Feasibility:** Medium. People resist questioning because it feels like going backward. Needs to be framed as forward motion.

### Leverage Point 5: DELAYS — "Shorten feedback cycles" (Level 9)
**Intervention:** Reduce the time between articulation and feedback. Fast iteration loops: articulate → test → learn → articulate. Reduce the delay between "I think this is clear" and "Is this actually clear?"
**Leverage:** Medium. Faster feedback prevents long wandering in wrong directions.
**Feasibility:** High with tools, medium without them. An AI partner can provide near-instant feedback.

### Leverage Point 6: BUFFER SIZE — "Protect the Motivation stock" (Level 11)
**Intervention:** Build in progress markers, small wins, and breaks. Ensure motivation doesn't drain before clarity is achieved.
**Leverage:** Low-medium. Doesn't change the dynamics, but prevents premature termination.
**Feasibility:** High. Simple process design: break tasks into stages, celebrate intermediate outputs.

---

## Step 7: Intervention Analysis

### Intervention A: Structured Thinking Frameworks (e.g., Reasoning Toolkit skills)

| Dimension | Assessment |
|-----------|------------|
| **Targets** | Leverage Points 2, 3, 4, 5 simultaneously |
| **Mechanism** | Provides externalization scaffolding (LP3), makes thinking state visible (LP2), embeds questioning steps (LP4), enables fast iteration (LP5) |
| **Direct effects** | Immediately increases flow rate into Articulated Structure stock; reduces friction of articulation |
| **Feedback effects** | Accelerates R1 (Articulation Engine). Strengthens B1 (Questioning Brake) by building tests into the process. Partially counteracts R2 (Commitment Trap) by surfacing questions before commitment hardens |
| **Delays** | Effect visible within first use (minutes). Compounding benefits over multiple uses as the thinker internalizes patterns |
| **Unintended risks** | Could trigger "Shifting the Burden" — reliance on tools instead of developing internal thinking capacity. Mitigated if frameworks are designed to teach principles, not just execute procedures |
| **Leverage** | High |
| **Feasibility** | High |
| **Time to effect** | Immediate |
| **Confidence** | High |

### Intervention B: AI-Assisted Thinking Partner

| Dimension | Assessment |
|-----------|------------|
| **Targets** | Leverage Points 3, 5 primarily |
| **Mechanism** | The thinker articulates to the AI, receives near-instant feedback, can iterate rapidly. Dramatically shortens the articulation-feedback loop |
| **Direct effects** | Increases articulation attempts (talking to AI is lower friction than writing alone). Provides external feedback without social cost |
| **Feedback effects** | Supercharges R1 by providing a responsive audience. Can strengthen B1 if the AI asks probing questions. Risk: can weaken B1 if the AI is too agreeable |
| **Delays** | Near-instant feedback cycle. Risk of too-fast iteration without depth |
| **Unintended risks** | Could strengthen R2 (Commitment Trap) if the AI validates prematurely. Could deplete Motivation if feedback is too challenging. Could create dependency (Shifting the Burden archetype) |
| **Leverage** | High |
| **Feasibility** | High (already available) |
| **Time to effect** | Immediate |
| **Confidence** | Medium — depends heavily on AI behavior design |

### Intervention C: Paradigm Shift via Experience Design

| Dimension | Assessment |
|-----------|------------|
| **Targets** | Leverage Point 1 |
| **Mechanism** | Design experiences where the thinker directly feels the difference between unstructured and structured thinking. Not argument — demonstration |
| **Direct effects** | Changes the thinker's beliefs about how thinking works |
| **Feedback effects** | Transforms all downstream behavior. A person who believes in externalization naturally seeks tools, writes things down, and structures their thinking |
| **Delays** | Requires multiple positive experiences. Could take weeks to months for the paradigm to fully shift |
| **Unintended risks** | Over-structuring: some ideas benefit from loose, associative thinking. Risk of "framework for everything" mentality that kills intuition |
| **Leverage** | Highest |
| **Feasibility** | Low-medium. Can't force paradigm shifts. Can only create conditions |
| **Time to effect** | Weeks to months |
| **Confidence** | Medium |

### Intervention Comparison

| Intervention | Leverage | Feasibility | Time to Effect | Confidence | Unintended Risks |
|---|---|---|---|---|---|
| A. Structured frameworks | High | High | Immediate | High | Tool dependency |
| B. AI thinking partner | High | High | Immediate | Medium | Premature validation, dependency |
| C. Paradigm shift | Highest | Low-medium | Weeks-months | Medium | Over-structuring |

### Recommendation

**Sequence:**

1. **Lead with A (structured frameworks)** — immediate, high-confidence, high-leverage. This is the core offering of the Reasoning Toolkit. Each skill is an intervention at Leverage Points 2-5 simultaneously.

2. **Combine A with B (AI + frameworks)** — the AI executes the frameworks, providing both structure and instant feedback. This combination addresses the widest range of leverage points. The frameworks prevent the AI from being too agreeable (LP4), while the AI prevents the frameworks from being too rigid (LP5).

3. **Let C happen naturally** — repeated positive experiences with A+B shift the paradigm over time. Don't try to argue people into believing in structured thinking. Let them feel it.

**What to monitor:**
- Do users return after first use? (R1 is engaging)
- Do users report surprises or changed minds? (B1 is working)
- Do users attempt harder problems over time? (Paradigm is shifting)
- Do users skip steps or only use easy skills? (R2 may be dominating — commitment to comfort zone)

---

## Verification Checklist

- [x] **System boundary clearly defined:** Thinker's cognitive process, from intuition to plan, bounded by session and multi-session time scales
- [x] **Causal links have clear mechanisms:** Each link explains *why* A causes B, not just that it does
- [x] **Feedback loops correctly classified:** R1, R2, R3 are reinforcing (even negatives); B1, B2, B3 are balancing (odd negatives)
- [x] **Stocks and flows properly distinguished:** 5 stocks (accumulators) with identified inflows and outflows
- [x] **Relevant archetypes identified:** Shifting the Burden, Limits to Growth, Fixes That Fail, Growth and Underinvestment — all active in this system
- [x] **Leverage points prioritized by actual leverage:** Paradigm > Information flows > Loop strength > Delays > Buffers
- [x] **Interventions traced through feedback effects:** Each intervention mapped to loops affected, with unintended consequences identified

---

## Key Insight for Reasoning Toolkit

The system of intuition-to-plan has a single dominant engine (R1: The Articulation Engine) and a single dominant failure mode (R2: The Commitment Trap). Every skill in the toolkit is most valuable when it does two things simultaneously:

1. **Accelerates R1** — makes it easier and faster to externalize, structure, and refine ideas
2. **Activates B1** — forces the thinker to question assumptions and test claims *before* commitment hardens

Skills that only do (1) build false clarity. Skills that only do (2) drain motivation. The best skills do both — they feel like forward progress *while* challenging the thinker's current understanding.

This is why ARAW-pattern skills (Articulate → Reality-test → Articulate again → Weigh) are structurally superior to simple brainstorming or simple critique. They interleave R1 and B1 in the same procedure, preventing either loop from dominating.
