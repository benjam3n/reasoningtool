# /se Enumerate all the types of thinking tasks a person might bring to an AI
**Date:** 2026-03-09
**Skill:** /se (Space Enumeration)

---

## Interpretation

**Interpretation 1 — Generate a comprehensive list**: The user wants to systematically enumerate all types of thinking tasks a person might bring to an AI, with the explicit goal of testing whether the current 17 category skills cover the full space.

---

## Step 1: Confirm Dimensions

```
DIMENSIONS FOR: Types of thinking tasks a person brings to an AI

1. Cognitive Operation: What the person needs their mind (or the AI's mind) to DO
   - Evaluate, Generate, Analyze, Decide, Transform, Diagnose,
     Plan, Explain, Validate, Explore, Synthesize, Remember,
     Predict, Monitor, Regulate

2. Object Type: What kind of thing they're working ON
   - Claim/belief, Decision/choice, Idea/concept, Work product,
     System/process, Goal/outcome, Emotion/experience, Content/text,
     Problem/failure, Domain knowledge, Relationship/interaction,
     Data/evidence, Skill/capability, Identity/self, Norm/rule

3. Stance: What posture the person is in when they arrive
   - Stuck (blocked, confused), Uncertain (exploring, unsure),
     Confident-but-checking (verifying), Active (executing),
     Reactive (something happened), Curious (learning),
     Overwhelmed (too much), Bored/understimulated (too little)

4. Directional Orientation: Which way in time/abstraction are they facing
   - Backward (what happened, why), Present (what is, what's true now),
     Forward (what to do next, what will happen), Meta (how am I thinking)

5. Desired Output Form: What shape the answer should take
   - A verdict/judgment, A list/enumeration, A plan/sequence,
     A reframe/new perspective, A draft/artifact, An explanation/model,
     A recommendation, A question (better than the one they asked),
     A feeling of being heard, A structured framework

TOTAL SPACE: 15 × 15 × 8 × 4 × 10 = 72,000 combinations
GRANULARITY: REPRESENTATIVE (with hierarchical grouping)
```

---

## Step 2: Enumeration Strategy

Space size > 5,000 → **Hierarchical**: enumerate by primary dimension (Cognitive Operation), then cross-reference against Stance and Object Type to find meaningful clusters.

---

## Step 3: Hierarchical Enumeration

### Level 1: Primary Dimension — Cognitive Operation

I organize all thinking tasks into **20 top-level task types**, grouped into 6 meta-categories.

---

### META-CATEGORY A: ASSESSMENT (Is this true/good/right?)

#### 1. Claim Testing
*"Is this true?"*
The person has a proposition, assertion, or belief and wants to know if it holds up.
- Fact-checking a specific claim
- Stress-testing an argument's logic
- Detecting bias or motivated reasoning in a source
- Checking whether evidence actually supports a conclusion
- Evaluating competing claims against each other

**Current coverage:** `/claim` — well-covered.

#### 2. Evaluation / Judgment
*"Is this good?"*
The person has a work product, output, performance, or state of affairs and wants a quality assessment.
- Grading writing, code, design, strategy
- Assessing whether something meets a standard
- Comparing actual vs. expected outcomes
- Reviewing someone else's work (or your own)
- Gauging readiness (is this ready to ship/submit/present?)

**Current coverage:** `/evaluate` — well-covered.

#### 3. Validation / Verification
*"Did I get this right?"*
The person has completed something and wants confirmation or error-detection, not open-ended evaluation.
- Proofreading and error-checking
- Verifying a calculation or derivation
- Checking that a plan covers all requirements
- Sanity-checking a decision before committing
- Testing whether an answer is consistent with constraints

**Current coverage:** Partially under `/evaluate`. Also served by direct skills (`/pv`, `/mv`, `/fwa`). No dedicated category entry point for "check my work" as distinct from "evaluate this thing." **Minor gap.**

---

### META-CATEGORY B: DECISION & CHOICE (What should I do?)

#### 4. Decision-Making
*"Which option should I pick?"*
The person faces a choice between discrete alternatives and needs to select.
- Choosing between job offers, tools, approaches
- Prioritizing a backlog or to-do list
- Allocating scarce resources (time, money, attention)
- Go/no-go decisions
- Tiebreaking when options seem equivalent

**Current coverage:** `/decide` — well-covered.

#### 5. Preference Clarification
*"What do I actually want?"*
The person doesn't yet know their own criteria. They need to discover what matters to them before they can choose.
- Clarifying values when they conflict
- Figuring out why a "good on paper" option feels wrong
- Distinguishing between what they want, what they think they should want, and what others want for them
- Identifying non-negotiables vs. nice-to-haves

**Current coverage:** Partially under `/want` and `/emotion`. But `/want` is goal-forward ("I want X, how do I get it") and `/emotion` is feeling-forward. The case of "I don't know what I want" sits between them. **Minor gap** — probably best handled by `/want` absorbing it.

---

### META-CATEGORY C: GENERATION & CREATION (Make something)

#### 6. Content Creation
*"Write/build/design this for me."*
The person needs an artifact produced: text, code, image prompt, outline, email, presentation, etc.
- Drafting from scratch
- Adapting existing content for a new audience or format
- Generating variations or alternatives
- Filling in a template or structure
- Translating between formats (bullet points → prose, spec → code)

**Current coverage:** `/create` — well-covered.

#### 7. Ideation / Brainstorming
*"Give me ideas."*
The person needs quantity and novelty. They want a wide spread of possibilities, not a single answer.
- Generating options for a project, name, approach
- Creative stimulus (what if...?)
- Recombining existing elements in new ways
- Finding analogies from other domains
- Breaking out of a rut

**Current coverage:** Partially under `/search` (UAUA mode explores), and direct skills `/ma`, `/cda`. But there's no category-level entry point that says "I need ideas." A person saying "give me ideas for..." would likely be routed to `/create` or `/search`, neither of which is exactly right. **Moderate gap.**

#### 8. Problem Construction / Question Formulation
*"What's the right question to ask?"*
The person doesn't need answers yet — they need to frame the problem correctly.
- Turning a vague feeling of "something's wrong" into a crisp problem statement
- Generating hypotheses to test
- Identifying what would need to be true for something to work
- Formulating research questions
- Scoping: what's in and out of the problem

**Current coverage:** Partially under `/analyze` and `/diagnose`. The `/sp` skill improves prompts. But the general case of "help me figure out what the actual question is" lacks a direct category entry. **Moderate gap.**

---

### META-CATEGORY D: ANALYSIS & UNDERSTANDING (Help me understand)

#### 9. Explanation / Teaching
*"Explain this to me."*
The person doesn't understand something and wants it made clear.
- Explain a concept, term, or mechanism
- Explain it at a specific level (ELI5, expert, etc.)
- Explain why something is the way it is (not just what)
- Walk through a worked example
- Compare two things to highlight differences

**Current coverage:** `/technical` routes domain-specific questions. `/how` answers procedural questions. But pure "explain this concept to me" doesn't have an obvious category entry point. A person saying "What is X?" or "Why does Y happen?" might not think they have a "domain-specific question" or a "how do I" question. **Moderate gap.**

#### 10. Analysis / Decomposition
*"Break this down for me."*
The person has something complex and wants it separated into understandable parts.
- Breaking a problem into sub-problems
- Identifying root causes
- Mapping stakeholders, forces, or variables
- Finding patterns in data or observations
- Separating signal from noise

**Current coverage:** `/analyze` — well-covered.

#### 11. Synthesis / Integration
*"Pull this together for me."*
The person has multiple inputs, sources, or perspectives and needs them unified.
- Summarizing across multiple documents
- Finding the common thread across disparate observations
- Reconciling conflicting information
- Building a coherent narrative from scattered facts
- Integrating feedback from multiple reviewers

**Current coverage:** No dedicated category skill. `/analyze` decomposes; nothing explicitly recomposes. `/create` could produce a synthesis, but the thinking task is analytical, not generative. **Moderate gap.**

#### 12. Systems Understanding
*"How does this work?"*
The person wants to understand a system, mechanism, or process as a whole.
- Understanding how parts interact
- Tracing cause-and-effect chains
- Identifying feedback loops, bottlenecks, leverage points
- Mapping a process end-to-end
- Understanding why a system behaves unexpectedly

**Current coverage:** Partially under `/technical` and direct skills `/fohw`, `/insd`. The category router `/technical` should catch these, though "how does my organization work" isn't a "domain-specific" question in the way a person might frame it. **Minor gap.**

---

### META-CATEGORY E: PROBLEM-SOLVING & EXECUTION (Fix/do this)

#### 13. Diagnosis / Troubleshooting
*"Something's wrong — what is it and how do I fix it?"*
The person has a failure, bug, symptom, or undesired state and needs to find the cause and remedy.
- Technical debugging
- Interpersonal conflict diagnosis
- Health symptom analysis
- Process failure investigation
- "Why isn't this working?"

**Current coverage:** `/diagnose` — well-covered.

#### 14. Planning / Strategy
*"Help me figure out the steps."*
The person has a goal and needs a path from here to there.
- Project planning and sequencing
- Strategy formulation
- Contingency planning (what if X goes wrong?)
- Resource planning
- Roadmap creation

**Current coverage:** Partially under `/action` (execution) and `/want` (goals). But planning as a thinking task — "I'm not ready to execute yet, I need a plan" — sits between them. `/action` assumes readiness; `/want` clarifies goals but doesn't necessarily produce a plan. **Moderate gap.**

#### 15. Execution Support
*"Walk me through doing this."*
The person knows what to do conceptually but needs help with the actual doing — step-by-step guidance, templates, checklists, real-time coaching.
- Step-by-step walkthroughs
- Templates and fill-in structures
- Checklists for complex procedures
- "Watch me do this and tell me if I'm going off track"
- Adapting general advice to specific circumstances

**Current coverage:** `/action` and `/how` — reasonably well-covered between them.

#### 16. Optimization / Improvement
*"Make this better."*
The person has something that works but wants it improved — faster, cheaper, clearer, more elegant, more effective.
- Refactoring code, prose, or processes
- Removing waste or redundancy
- Finding the 80/20 (what small change gives the biggest improvement?)
- Benchmarking against best practices
- Iterative refinement

**Current coverage:** `/iterate` — well-covered for iterative improvement. `/evaluate` can identify what's wrong. Together they handle this, though a person saying "make this better" might not think to use either. Reasonable coverage.

---

### META-CATEGORY F: SELF-REGULATION & META-COGNITION (Help me think)

#### 17. Emotional Processing
*"I'm feeling [X] and need help with it."*
The person leads with an emotion — frustration, anxiety, excitement, grief — and needs the emotional dimension addressed before (or instead of) the analytical one.
- Venting / feeling heard
- Reframing a situation
- Normalizing an experience
- Separating emotional reaction from rational assessment
- Processing a setback or loss

**Current coverage:** `/emotion` — well-covered.

#### 18. Self-Awareness / Reflection
*"Help me see my own blind spots."*
The person suspects they're biased, stuck in a pattern, or not seeing something about themselves.
- Identifying cognitive biases in their reasoning
- Recognizing recurring patterns in their behavior
- Getting an outside perspective on their thinking
- Distinguishing between what they know and what they assume
- Calibrating confidence (am I overconfident or underconfident?)

**Current coverage:** Partially under category skills — no single entry point. Direct skills `/sdc`, `/sid`, `/ecal` serve this. But a person saying "Am I being dumb about this?" has no obvious category to enter. **Moderate gap.**

#### 19. Motivation / Accountability
*"Help me actually do the thing."*
The person knows what to do and how to do it. The problem is willpower, procrastination, follow-through, or commitment.
- Breaking through procrastination
- Building accountability structures
- Finding intrinsic motivation
- Overcoming perfectionism
- Sustaining effort over time

**Current coverage:** Partially under `/emotion` (if it presents as a feeling) or `/action` (if it presents as execution). But the core task — managing oneself — is distinct from both. **Minor gap**, likely absorbed by `/emotion` or `/want`.

#### 20. Orientation / Meta-navigation
*"I don't even know what kind of help I need."*
The person is lost — they don't know what question to ask, what tool to use, or how to start.
- "I'm overwhelmed and don't know where to begin"
- "I have a vague sense something is off"
- Choosing between different types of analysis
- Understanding what kind of problem this is
- "What should I be thinking about?"

**Current coverage:** `/meta` — well-covered. This is exactly its purpose.

---

## Step 4: Cross-Dimensional Check

```
CROSS-DIMENSIONAL ITEMS:

- "Help me learn this skill" spans Explanation (#9) AND Execution Support (#15)
  → Classify under a Learning/Skill-Acquisition type. Currently handled by
     /how (procedural) or /technical (conceptual), but the sustained learning
     journey is not a single task type either covers well.

- "Persuade me" / "Argue the other side" spans Claim Testing (#1) AND
  Self-Awareness (#18) → Currently served by /claim and direct skills /advr,
  /stc. Reasonable coverage.

- "Help me communicate this" spans Content Creation (#6) AND
  Explanation (#9) → /create covers the artifact; the thinking about *what*
  to communicate is analytical. Reasonable coverage.

- "Predict what will happen" spans Analysis (#10) AND Planning (#14)
  → Direct skills /fut, /dys cover this. No category entry point for
     pure prediction/forecasting. Minor gap.

- "Help me negotiate/persuade" spans Planning (#14) AND interpersonal
  → Direct skills /per, /col cover some of this. Specialized enough
     that it doesn't need its own category.

- "Translate between representations" (e.g., "turn this data into a story")
  spans Content Creation (#6) AND Synthesis (#11) → /create is the
  closest entry. Reasonable coverage.
```

---

## Step 5: Gap Check

```
COVERAGE CHECK:

| Task Type                  | Category Skill(s)  | Coverage   | Gap?                          |
|----------------------------|---------------------|------------|-------------------------------|
| 1. Claim Testing           | /claim              | Strong     | No                            |
| 2. Evaluation              | /evaluate           | Strong     | No                            |
| 3. Validation              | /evaluate (partial) | Moderate   | Yes — "check my work" ≠ eval  |
| 4. Decision-Making         | /decide             | Strong     | No                            |
| 5. Preference Clarification| /want, /emotion     | Moderate   | Minor — /want could absorb    |
| 6. Content Creation        | /create             | Strong     | No                            |
| 7. Ideation                | /search (partial)   | Weak       | YES — no "give me ideas" entry|
| 8. Problem Construction    | /analyze (partial)  | Weak       | YES — no "frame the problem"  |
| 9. Explanation             | /technical, /how    | Moderate   | Yes — "explain X" ≠ /how      |
| 10. Analysis               | /analyze            | Strong     | No                            |
| 11. Synthesis              | (none)              | Weak       | YES — no "pull it together"   |
| 12. Systems Understanding  | /technical          | Moderate   | Minor                         |
| 13. Diagnosis              | /diagnose           | Strong     | No                            |
| 14. Planning               | /action, /want      | Moderate   | Yes — planning ≠ executing    |
| 15. Execution Support      | /action, /how       | Strong     | No                            |
| 16. Optimization           | /iterate, /evaluate | Moderate   | No                            |
| 17. Emotional Processing   | /emotion            | Strong     | No                            |
| 18. Self-Awareness         | (direct skills only)| Weak       | YES — no "check my thinking"  |
| 19. Motivation             | /emotion (partial)  | Moderate   | Minor                         |
| 20. Orientation            | /meta               | Strong     | No                            |
```

### Actions Taken: Filled Gaps in Enumeration

After the gap check, here are items I added or expanded to ensure each of the 20 types is fully populated:

**Type 3 (Validation)** — added: checking a proof, verifying data pipeline output, confirming a translation is accurate, regression-testing after a change.

**Type 7 (Ideation)** — added: naming things, finding metaphors, generating counterexamples, exploring "what would the opposite look like?", mashup/crossover ideas.

**Type 8 (Problem Construction)** — added: pre-mortem framing ("imagine this failed — why?"), assumption surfacing, converting complaints into problem statements, identifying the decision that's actually being made.

**Type 11 (Synthesis)** — added: literature review synthesis, meeting-notes-to-action-items, reconciling conflicting advice, creating a unified mental model from disparate sources, "what's the bottom line across all of this?"

**Type 18 (Self-Awareness)** — added: "What pattern am I in?", "Am I asking the right question?", "What would someone who disagrees with me say?", "What am I optimizing for without realizing it?"

---

## Step 6: Organized Output

### COMPREHENSIVE LIST: Types of Thinking Tasks a Person Brings to an AI

**Organization:** By meta-category, with gap assessment against current 17 category skills.

---

#### A. ASSESSMENT — "Is this true / good / right?"
| # | Task Type | Description | Category Skill | Gap? |
|---|-----------|-------------|----------------|------|
| 1 | Claim Testing | Test whether a proposition holds up | `/claim` | None |
| 2 | Evaluation | Judge quality of a work product | `/evaluate` | None |
| 3 | Validation | Confirm correctness of completed work | `/evaluate` (partial) | Minor |

#### B. DECISION & CHOICE — "What should I do?"
| # | Task Type | Description | Category Skill | Gap? |
|---|-----------|-------------|----------------|------|
| 4 | Decision-Making | Choose between discrete options | `/decide` | None |
| 5 | Preference Clarification | Discover what I actually want/value | `/want` + `/emotion` | Minor |

#### C. GENERATION & CREATION — "Make something"
| # | Task Type | Description | Category Skill | Gap? |
|---|-----------|-------------|----------------|------|
| 6 | Content Creation | Produce an artifact (text, code, etc.) | `/create` | None |
| 7 | **Ideation** | Generate many possibilities | None dedicated | **Gap** |
| 8 | **Problem Construction** | Frame the right question | `/analyze` (partial) | **Gap** |

#### D. ANALYSIS & UNDERSTANDING — "Help me understand"
| # | Task Type | Description | Category Skill | Gap? |
|---|-----------|-------------|----------------|------|
| 9 | Explanation | Make something clear to me | `/technical` + `/how` | Moderate |
| 10 | Analysis / Decomposition | Break something complex into parts | `/analyze` | None |
| 11 | **Synthesis** | Pull multiple inputs into a whole | None dedicated | **Gap** |
| 12 | Systems Understanding | Understand how a system works | `/technical` (partial) | Minor |

#### E. PROBLEM-SOLVING & EXECUTION — "Fix / do this"
| # | Task Type | Description | Category Skill | Gap? |
|---|-----------|-------------|----------------|------|
| 13 | Diagnosis | Find what's wrong and how to fix it | `/diagnose` | None |
| 14 | **Planning** | Create a path from here to a goal | `/action` + `/want` (partial) | **Gap** |
| 15 | Execution Support | Walk me through doing it | `/action` + `/how` | None |
| 16 | Optimization | Make something that works work better | `/iterate` | None |

#### F. SELF-REGULATION & META-COGNITION — "Help me think"
| # | Task Type | Description | Category Skill | Gap? |
|---|-----------|-------------|----------------|------|
| 17 | Emotional Processing | Help with feelings first | `/emotion` | None |
| 18 | **Self-Awareness** | Reveal my blind spots & biases | Direct skills only | **Gap** |
| 19 | Motivation / Accountability | Help me follow through | `/emotion` (partial) | Minor |
| 20 | Orientation | I don't know what help I need | `/meta` | None |

---

### Summary of Gaps

**5 meaningful gaps** (no clear category-level entry point):

| Gap | What the person says | Suggested fix |
|-----|----------------------|---------------|
| **Ideation** | "Give me ideas for..." | Add `/ideate` or expand `/search` to explicitly welcome brainstorming |
| **Problem Construction** | "Help me figure out what the actual problem is" | Add `/frame` or expand `/analyze` to include framing mode |
| **Synthesis** | "Pull all of this together for me" | Add `/synthesize` or expand `/create` to include synthesis mode |
| **Planning** | "Help me make a plan" | Add `/plan` as a category skill (distinct from `/action`'s "execute now") |
| **Self-Awareness** | "Am I thinking about this wrong?" | Add `/reflect` or expand `/meta` to include self-examination |

**4 minor gaps** (covered but the person might not find the entry point):

| Gap | What the person says | Suggested fix |
|-----|----------------------|---------------|
| Validation | "Check my work" | Add language to `/evaluate` making "verification" an explicit mode |
| Preference Clarification | "I don't know what I want" | Add language to `/want` making ambiguity an explicit starting state |
| Explanation | "Explain X to me" | Add `/explain` or ensure `/technical` welcomes non-domain-specific explanations |
| Systems Understanding | "How does this work?" | Covered if `/technical` is framed broadly enough |

---

### Current 17 Category Skills Mapped to 20 Task Types

```
STRONG COVERAGE (1:1 match):
  /claim      → Claim Testing
  /evaluate   → Evaluation
  /decide     → Decision-Making
  /create     → Content Creation
  /diagnose   → Diagnosis
  /analyze    → Analysis
  /emotion    → Emotional Processing
  /meta       → Orientation
  /iterate    → Optimization

MODERATE COVERAGE (handles it, but entry point is indirect):
  /want       → Preference Clarification (+ partial Planning)
  /how        → Execution Support (+ partial Explanation)
  /action     → Execution Support (+ partial Planning)
  /technical  → Explanation (+ partial Systems Understanding)
  /search     → partial Ideation
  /viability  → specialized Claim Testing (for ideas)
  /certainty  → meta-level (applies to any task type)
  /sp         → specialized (prompt improvement)

NO CATEGORY COVERAGE:
  Ideation (standalone brainstorming)
  Problem Construction / Framing
  Synthesis / Integration
  Planning (as distinct from execution)
  Self-Awareness / Reflection
```

---

```
METADATA:
- Total task types identified: 20
- Dimensions covered: 5 (Cognitive Operation, Object Type, Stance, Direction, Output Form)
- Granularity: REPRESENTATIVE (hierarchical)
- Gaps identified: 5 meaningful, 4 minor
- Cross-dimensional items: 6 (all resolved)
- Items in "Other": 0 (all classified)
```

---

## Quality Checklist

- [x] Dimensions confirmed or discovered
- [x] Granularity level specified
- [x] Appropriate strategy chosen for space size
- [x] All dimensions represented
- [x] Cross-dimensional items handled
- [x] Gap check completed
- [x] Output organized clearly
- [x] Metadata included

---

## Next Steps

1. Use `/mv` to verify the 20 types are MECE (mutually exclusive, collectively exhaustive)
2. Decide which of the 5 gaps warrant new category skills vs. expanding existing ones
3. Test with real user inputs: collect 50 actual user opening messages and classify each against these 20 types to validate coverage empirically
