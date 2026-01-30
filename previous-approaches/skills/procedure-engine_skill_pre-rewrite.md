---
name: procedure_engine
description: GOSM Procedure Engine - Automatic routing and chaining based on QUICKSTART flow. Handles goals, problems, questions, decisions, situations, and feelings.
context: fork
---

# GOSM Procedure Engine

**Input**: $ARGUMENTS

---

## Step 1: What Do You Have?

Classify the input type:

| Type | Indicators | Example |
|------|------------|---------|
| **GOAL** | "I want", "achieve", imperative, future state | "I want to start a business" |
| **PROBLEM** | "issue", "broken", "stuck", negative state | "My team is dysfunctional" |
| **QUESTION** | "should I", "?", seeking answer | "Should I take this job?" |
| **DECISION** | "or", "vs", explicit options | "Option A or Option B?" |
| **SITUATION** | Describing current state, implicit goal | "I'm stuck in my career" |
| **FEELING** | Emotional state, intuition | "Something feels off" |

**Classify now**: [TYPE]

---

## Step 2: Parse as Guesses (GUESS FIRST)

**Core Principle**: Everything the user says contains guesses. Parse them FIRST, ask questions about them SECOND.

A guess is a claim that could be wrong about something external to the claim itself.

### What's NOT a Guess (Don't Parse These)

| Type | Example | Why Not a Guess |
|------|---------|-----------------|
| Definitions | "A bachelor is unmarried" | About words, not world |
| Techniques | "Sort by dividing array" | Method, no truth claim |
| Categories | "Red is a color" | Classification system |
| Questions | "What should I do?" | Requesting, not claiming |
| Commands | "Help me with X" | Directing, not claiming |

### Parse Surface Claims

List each factual/causal/predictive claim:
1. [surface claim 1]
2. [surface claim 2]
...

### Unbundle Hidden Guesses

Each surface claim contains BUNDLED GUESSES. Unbundle them:

**Example**: "Evidence shows X" bundles:
- Guess: I correctly perceived the evidence
- Guess: I correctly remember the evidence
- Guess: I correctly interpret the evidence
- Guess: The evidence is reliable/not fabricated

**Example**: "I need to quit my job" bundles:
- Guess: Quitting will solve the underlying problem
- Guess: The job is the source of the problem
- Guess: No alternative to quitting exists
- Guess: I know what I want after quitting

For each surface claim, unbundle:
```
Surface: "[claim]"
Bundled guesses:
- [hidden guess 1]
- [hidden guess 2]
- [hidden guess 3]
...
```

### Generate Multiple Guess Types

For key claims, generate multiple guess types:

| Type | Description | Example |
|------|-------------|---------|
| **WELL-SUPPORTED** | Evidence exists, likely true | "Job is stressful [O: user reported]" |
| **UNLIKELY** | Counter-evidence or low prior | "Boss will change behavior" |
| **CONTRARIAN** | Challenges the frame | "Quitting won't help - the real issue is internal" |
| **OUT-OF-BOX** | Creative reframe | "The 'problem' is actually the solution to something else" |
| **UNCOMFORTABLE** | True but unwanted | "You're staying because you're afraid" |

**Generate now** for key claims.

### Classify Each Guess: OPEN vs CLOSED

| Guess | Type | Why |
|-------|------|-----|
| [guess] | OPEN/CLOSED | [alternatives exist / no alternatives] |

- **CLOSED**: No alternatives exist. Accept as foundation.
- **OPEN**: Alternatives exist. Needs exploration.

---

## Step 3: ARAW Search (Assume Right / Assume Wrong)

For each OPEN claim, branch:

```
Claim: "[claim]"
├── ASSUME RIGHT → Claim is true
│   └── What follows? What actions are justified?
└── ASSUME WRONG → Claim might be false
    └── What alternatives exist? What else could be true?
```

→ INVOKE: /assumeright_assumewrong_search $ARGUMENTS

---

## Step 4: Fill Goal Journey Structure

Make guesses to fill the structure:

```
CURRENT STATE:    [Where they are now]
DESIRED STATE:    [Where they want to be]
IMMEDIATE GOAL:   [What they're trying to do]
SERVES:           [What that goal serves - UNCERTAIN?]
INTRINSIC GOAL:   [What they ultimately value - NEEDS ELICITATION?]
WHY NOW:          [What triggered this - UNKNOWN?]
SUCCESS CRITERIA: [How they'll know it worked - UNKNOWN?]
CONSTRAINTS:      [What limits exist - UNKNOWN?]
```

Mark uncertain items. These become questions.

---

## Step 5: Dual Analysis (from ARAW)

### Contrarian Analysis (ASSUME WRONG branches)
- Is [stated approach] actually necessary?
- What alternatives exist?
- Is [X] the real problem/goal, or something else?

### Non-Contrarian Analysis (ASSUME RIGHT branches)
- What options exist for achieving [goal]?
- What are the next steps?
- What resources/skills are available?

**Both analyses are always done.**

---

## Step 6: Filter by User Context

What can this user act on?

| User Role | Show Contrarian? | Show Non-Contrarian? |
|-----------|------------------|----------------------|
| Decision maker | Yes | Yes |
| Implementer | Some | Yes (focus on execution) |
| Affected party | Minimal | Yes (focus on their options) |

---

## Step 7: Generate Questions (About the Guesses)

**Remember**: Guesses FIRST (Step 2), questions SECOND (this step).

### Question Quality Criteria

Before generating each question, check:

| Criterion | Description | Pass? |
|-----------|-------------|-------|
| **Generativity** | Opens new lines of inquiry | HIGH/MEDIUM/LOW |
| **Specificity** | Clear what counts as answer | HIGH/MEDIUM/LOW |
| **Depth** | Goes UPSTREAM (toward causes), not sideways | UPSTREAM/SIDEWAYS |
| **Answerability** | Can be grounded in evidence | YES/PARTIAL/NO |

### "Why Continue?" Gate

Before each question, ask:
1. Is this UPSTREAM? (toward causes, not sideways)
2. Is it DIFFERENT? (not a rephrasing)
3. Is it ANSWERABLE? (can be grounded)
4. Would the answer MATTER? (changes understanding)

**STOP generating questions when they become**:
- REPETITIVE: Same question rephrased
- SIDEWAYS: Related topic, not causal
- UNANSWERABLE: No way to ground it
- LOW-VALUE: Answer wouldn't change anything

### Questions to Ask (Filtered)

For each question, document:
```
Question: [question]
About guess: [which guess this questions]
Gate check: [UPSTREAM/DIFFERENT/ANSWERABLE/MATTERS]
Priority: [HIGH/MEDIUM/LOW]
```

**Remember**: After-questioning results are ALSO guesses, not conclusions. Mark as "current working guess" not "answer".

---

## Step 8: Value Elicitation (if intrinsic goal unknown)

→ INVOKE: /value_elicitation $ARGUMENTS

Keep asking until circularity:
- "What's important to you about [X]?"
- "When you have [X], what does that give you?"

---

## Step 9: Check for Failure Patterns

### First: Legitimate Iteration Check
- [ ] Measurable improvement each cycle?
- [ ] Backward reasoning identified gaps?
- [ ] Foundational work that must precede testing?

If all checked → NOT failure, continue.

### If not legitimate iteration:

→ INVOKE: /failure_journeys (check for sustainable failure)

- Same pattern repeating?
- Would success threaten something?
- Is struggle part of identity?

---

## Step 10: Trace Goal Journey

→ INVOKE: /goal_journey_system

```
ACTION: [verb phrase]
    ↓ serves
GOAL: [what that achieves]
    ↓ serves
GOAL: [what that enables]
    ↓ serves
INTRINSIC: [from value elicitation]
```

Each step must serve the next. No gaps.

---

## Step 11: Generate Steps

→ INVOKE: /steps_generation

For execution:
1. Verb phrases ("Do X" not "X happens")
2. Specific and verifiable
3. Each serves the goal chain

---

## Step 12: Verify Before Output

→ INVOKE: /verification_before_output

Every claim needs a marker:
- `[O: source]` - Observed directly
- `[T: N=X, result]` - Tested with results
- `[D: A + B → C]` - Derived from verified premises

If unverifiable → state as guess or exclude.

---

## Step 13: Empirical Validation (NEW)

→ INVOKE: /empirical_validation

**Before final commitment**, check if any part can be tested:

1. Extract testable predictions from the plan
2. Design minimum viable test
3. Decide: test first vs act then test vs set checkpoints
4. Log predictions for future calibration

**Why this matters**: Story coherence is insufficient. Coherent narratives can mask poor plans (Hollywood problem). External reality testing catches what internal consistency misses.

**Skip conditions**:
- Action is trivially reversible → Just act
- Extreme time pressure → GOSM-Lite already used
- No test possible → Commit with uncertainty noted
- Test cost > action cost → Just act

Even when skipping, LOG predictions for calibration.

---

## Output Format

```
## Input Classification
Type: [GOAL/PROBLEM/QUESTION/DECISION/SITUATION/FEELING]

## Surface Claims Parsed
[List of explicit claims from input]

## Bundled Guesses Unbundled
[For each surface claim, the hidden guesses within it]

## Guess Variety (Multiple Types)
| Claim | WELL-SUPPORTED | UNLIKELY | CONTRARIAN | OUT-OF-BOX | UNCOMFORTABLE |
|-------|----------------|----------|------------|------------|---------------|
| ... | ... | ... | ... | ... | ... |

## OPEN vs CLOSED Classification
| Guess | Type | Reason |
|-------|------|--------|
| ... | OPEN/CLOSED | ... |

## ARAW Analysis
[Key branches from Assume Right / Assume Wrong]

## Goal Journey Structure
[Filled structure with uncertainties marked]
[All items marked as GUESS not FACT]

## Dual Analysis Summary
CONTRARIAN: [Key alternatives/reframes]
NON-CONTRARIAN: [Key options/next steps]

## Questions About Guesses
[Questions that passed the "why continue?" gate]
[Each linked to which guess it questions]

## Current Working Guesses (Not Conclusions)
[After-questioning results, still marked as guesses]

## Recommended Procedure Chain
(Example for GOAL: → CHAIN: [/goal_understanding, /value_elicitation, /goal_journey_system])
```

---

## Procedure Chains by Type

| Input Type | Procedure Chain |
|------------|-----------------|
| GOAL | /goal_understanding → /value_elicitation → /goal_journey_system → /steps_generation |
| PROBLEM | /problem_identification → /root_cause_5_whys → /araw → /leverage_point_discovery |
| QUESTION | /question_analysis_framework → /bounded_inquiry → /verification_before_output |
| DECISION | /comparison → /evaluation_dimensions → /criteria_weighting → /selection |
| SITUATION | /goal_understanding → /araw → /goal_reframing → /steps_generation |
| FEELING | /araw → /value_elicitation → /goal_understanding |

---

**Execute now**: Begin with Step 1 classification.
