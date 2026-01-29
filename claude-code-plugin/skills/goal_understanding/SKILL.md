---
name: goal_understanding
description: "MANDATORY first step before attempting any goal. Parses input as guesses, classifies OPEN vs CLOSED, fills goal journey structure. Includes clarification vs substitution check."
context: fork
---

# Goal Understanding Pre-Processor

**Input**: $ARGUMENTS

---

## Step 0: Context Detection and Variant Selection

Before deep analysis, assess context:

| Factor | Value | Notes |
|--------|-------|-------|
| Time Pressure | URGENT / NEAR / NORMAL | |
| Stakes | HIGH / MED / LOW | |
| Domain Expertise | EXPERT / INTERMEDIATE / NOVICE | |
| Action Cost | CHEAP / EXPENSIVE | |
| Complexity | SIMPLE / COMPOUND / AMBIGUOUS | See Step 0.3 |

**Variant Selection**:
- URGENT → Skip to Step 4 (minimal understanding, act fast)
- LOW stakes + CHEAP → Steps 1, 4, 7 only (quick parse)
- EXPERT → Steps 2-4, 7 (focus on gaps, not basics)
- AMBIGUOUS → Extra iteration on Step 0.5 and Step 1
- Standard → All steps

### Variant Examples

**URGENT variant** (skip to Step 4):
```
Input: "Production is down, fix it NOW"
→ Skip Steps 1-3
→ Fill minimal Goal Journey (current: down, desired: up)
→ Proceed to action immediately
```

**LOW stakes + CHEAP variant** (Steps 1, 4, 7):
```
Input: "Should I have tea or coffee?"
→ Quick claim parse (1 claim: preference exists)
→ Fill minimal structure
→ Route to simple comparison
```

**EXPERT variant** (Steps 2-4, 7):
```
Input: "I need to optimize my database queries" (from DBA)
→ Skip basic parsing, assume domain competence
→ Focus on OPEN claims about approach
→ Fill structure, note technical context
```

---

## Step 0.3: Complexity Assessment

Assess goal complexity before deep analysis:

| Complexity | Indicators | Treatment |
|------------|------------|-----------|
| **SIMPLE** | Single verb, single object, clear scope | Standard procedure, quick resolution |
| **COMPOUND** | Multiple goals bundled, "and", "while also" | Decompose into sub-goals, process each |
| **AMBIGUOUS** | Unclear what is wanted, vague language, feelings | Extra clarification before proceeding |

### Complexity Examples

**SIMPLE goal**:
```
Input: "I want to learn Python"
Complexity: SIMPLE
- Single action (learn)
- Single object (Python)
- Clear scope
→ Proceed with standard Steps 1-7
```

**COMPOUND goal**:
```
Input: "I want to switch careers, improve my health, and spend more time with family"
Complexity: COMPOUND
- Three distinct goals bundled
→ Decompose into three separate goal analyses:
   1. Career switch goal
   2. Health improvement goal
   3. Family time goal
→ Check for conflicts between goals
→ Prioritize or sequence
```

**AMBIGUOUS goal**:
```
Input: "I feel like something needs to change"
Complexity: AMBIGUOUS
- No clear action
- No specific object
- Emotional rather than directional
→ Before Step 1, clarify:
   - "What aspect of your life feels like it needs change?"
   - "What would 'better' look like?"
→ Convert feeling to tentative goal, then proceed
```

### Compound Goal Handling

When COMPOUND detected:
1. List all sub-goals explicitly
2. Check for dependencies: Does A enable B? Does C conflict with A?
3. Identify the LEAD goal (most important or most blocking)
4. Process LEAD goal first with full procedure
5. Note other goals for follow-up

```
COMPOUND DECOMPOSITION
======================
Sub-goals identified:
1. [goal A] - LEAD (most urgent)
2. [goal B] - dependent on A
3. [goal C] - independent

Dependencies:
- A → B (B needs A first)
- C independent

Proceeding with goal A...
```

### Ambiguous Goal Handling

When AMBIGUOUS detected:
1. Acknowledge the uncertainty: "I notice this is expressed as a feeling rather than a specific goal"
2. Generate candidate interpretations:
   - "This could mean you want [interpretation 1]"
   - "Or it could mean [interpretation 2]"
3. Ask clarifying question targeting the ambiguity
4. Convert answer to tentative SIMPLE or COMPOUND goal
5. Proceed with appropriate complexity handling

---

## Step 0.5: Clarification vs Substitution Check

**CRITICAL**: Before any analysis, capture the original goal exactly.

```
ORIGINAL GOAL (verbatim): "[user's exact words]"
```

Any refinement or interpretation must be checked:
→ GATE: clarification_vs_substitution [original] [interpretation]

**Substitution Red Flags** (check each):
- [ ] Am I changing what "success" means?
- [ ] Am I reducing the scope/ambition?
- [ ] Am I replacing with what I think they "really" want?
- [ ] Would achieving my version NOT achieve their version?

If any flag triggered → Explicit consent required before proceeding.

### Clarification vs Substitution Examples

**Good Clarification** (same goal, more specific):
```
Original: "I want to be healthier"
Clarified: "I want to improve my health through diet and exercise"
Check: Success still means "healthier" ✓
       Scope not reduced ✓
       Still their goal ✓
→ CLARIFICATION - proceed
```

**Bad Substitution** (different goal):
```
Original: "I want to be healthier"
Substituted: "You should lose 10 pounds"
Check: Success changed from "healthier" to "weight" ✗
       Scope reduced (health → weight) ✗
       Replaced with what I think they need ✗
→ SUBSTITUTION - ask for consent
```

**Borderline Case**:
```
Original: "I need to make more money"
Interpretation: "You need income above expenses"
Check: Might be reducing "more" to "enough"
→ ASK: "Are you looking to increase income, or ensure you meet expenses?"
```

---

## Step 1: Parse Input as Guesses

The user's input contains GUESSES (claims that may or may not be true).

List each claim:
1. [claim from input]
2. [claim from input]
...

### Parsing Examples

**Simple input**:
```
Input: "I want to start a business"
Claims:
1. User wants to start a business (stated)
2. Starting a business is the right approach (implicit)
3. User is ready to start (implicit)
4. "Business" means a specific thing (ambiguous)
```

**Complex input**:
```
Input: "I need $50k for my mom's surgery next month"
Claims:
1. Mom needs surgery (stated)
2. Surgery costs $50k (stated - but is this accurate?)
3. Surgery must happen next month (stated - but why?)
4. $50k is the solution (implicit - are there alternatives?)
5. User can obtain $50k (implicit assumption)
6. This surgery is the only option (bundled assumption)
```

---

## Step 2: Classify OPEN vs CLOSED

| Claim | Type | Reasoning |
|-------|------|-----------|
| [claim] | OPEN/CLOSED | [has alternatives / foundational] |

- **CLOSED**: No alternatives exist. Accept as foundation.
- **OPEN**: Alternatives exist. Must be questioned/decomposed.

### OPEN vs CLOSED Examples

| Claim | Type | Why |
|-------|------|-----|
| "Doctor diagnosed cancer" | CLOSED | Medical fact, documented |
| "User said they want to change careers" | CLOSED | Their stated preference |
| "Surgery is the only option" | OPEN | Other treatments may exist |
| "I need $50k" | OPEN | Amount might be flexible, alternatives exist |
| "It must happen next month" | OPEN | Timeline might be negotiable |
| "I want to be happy" | CLOSED | Intrinsic goal, definitional |
| "This job will make me happy" | OPEN | Causal claim, testable |

**Key insight**: Specific-sounding claims can be OPEN.
- "$50,000" sounds specific → but the AMOUNT is negotiable (OPEN)
- "Next month" sounds specific → but the TIMING might flex (OPEN)

---

## Step 3: ARAW Each OPEN Claim

For each OPEN claim:

```
Claim: "[claim]"
├── ASSUME RIGHT → What follows if true?
└── ASSUME WRONG → What alternatives exist?
```

→ INVOKE: /assumeright_assumewrong_search [OPEN claims]

### ARAW Example

```
Claim: "Surgery is the only treatment option"
├── ASSUME RIGHT → Mom needs surgery
│   ├── What kind of surgery?
│   ├── What's the recovery?
│   └── Proceed to funding options
└── ASSUME WRONG → Other treatments exist
    ├── Medication alternatives?
    ├── Less invasive procedures?
    ├── Clinical trials?
    └── Second opinion needed?
```

---

## Step 4: Fill Goal Journey Structure

```
CURRENT STATE:    [Where they are now]
DESIRED STATE:    [Where they want to be]
IMMEDIATE GOAL:   [What they're trying to do]
SERVES:           [What that serves] - UNCERTAIN? NEEDS QUESTIONING?
INTRINSIC GOAL:   [Ultimate value] - NEEDS ELICITATION?
WHY NOW:          [Trigger] - UNKNOWN?
SUCCESS CRITERIA: [How to know it worked] - UNKNOWN?
CONSTRAINTS:      [What limits exist] - UNKNOWN?
```

Mark uncertain/unknown items.

### Goal Journey Examples

**Example 1: Career change**
```
CURRENT STATE:    Employed at corporate job, feeling unfulfilled
DESIRED STATE:    Working in a role that feels meaningful
IMMEDIATE GOAL:   Start a business
SERVES:           Autonomy? Impact? Income? [NEEDS QUESTIONING]
INTRINSIC GOAL:   Fulfillment? [NEEDS ELICITATION]
WHY NOW:          Recent event? Accumulated frustration? [UNKNOWN]
SUCCESS CRITERIA: Business running? Profitable? [UNKNOWN]
CONSTRAINTS:      Savings runway? Family obligations? [UNKNOWN]
```

**Example 2: Health goal**
```
CURRENT STATE:    Mom has [condition]
DESIRED STATE:    Mom is healthy/treated
IMMEDIATE GOAL:   Get $50k for surgery
SERVES:           Mom's health
INTRINSIC GOAL:   Family wellbeing, love
WHY NOW:          Urgency of condition [NEEDS CLARIFICATION]
SUCCESS CRITERIA: Treatment complete, positive outcome
CONSTRAINTS:      Timeline (next month stated), funding
```

---

## Step 5: Identify Domain

| Domain | Indicators |
|--------|------------|
| Career/Work | job, boss, salary, promotion, colleagues |
| Relationship | partner, friend, family, communication |
| Financial | money, budget, invest, save, debt |
| Health | body, energy, sleep, diet, exercise |
| Personal Growth | learn, improve, skill, habit |
| Creative | make, build, create, art, project |
| Life Direction | meaning, purpose, stuck, path |

**Domain**: [identified domain(s)]

---

## Step 6: Generate Questions

Questions to ask user (for uncertain/unknown items):

1. [Question] - fills [field]
2. [Question] - decomposes [OPEN claim]
3. [Question] - verifies [assumption]

### Question Quality Criteria

Good questions are:
- **Specific**: Not "tell me more" but "what's the timeline?"
- **Gap-filling**: Directly addresses an unknown
- **Actionable**: Answer changes the analysis
- **Prioritized**: Most important unknowns first

**Question Priority Order**:
1. Questions that resolve OPEN claims (highest value)
2. Questions that fill INTRINSIC GOAL (guides everything)
3. Questions that fill CONSTRAINTS (bounds options)
4. Questions that fill WHY NOW (reveals urgency)

---

## Step 7: Determine Next Procedure

Based on input type and gaps:

- If intrinsic goal unknown:
  → INVOKE: /value_elicitation $ARGUMENTS

- If problem statement:
  → INVOKE: /problem_identification $ARGUMENTS

- If decision/options:
  → INVOKE: /comparison $ARGUMENTS

- If ready to trace journey:
  → INVOKE: /goal_journey_system $ARGUMENTS

---

## Common Goal Patterns

### Pattern 1: Financial Emergency
```
Indicators: "need money", "by [date]", "for [purpose]"
Structure:
- IMMEDIATE: Get [amount]
- SERVES: [purpose - medical, debt, opportunity]
- KEY QUESTIONS: Is amount fixed? Is timeline fixed? Alternatives?
→ Route to: /problem_identification (is money the real problem?)
```

### Pattern 2: Career Transition
```
Indicators: "want to [quit/change/start]", job dissatisfaction
Structure:
- IMMEDIATE: Leave current situation
- SERVES: Better fit? More money? Autonomy?
- KEY QUESTIONS: What's wrong with current? What would ideal look like?
→ Route to: /value_elicitation (find intrinsic goal)
```

### Pattern 3: Relationship Issue
```
Indicators: Partner/friend/family + conflict/communication
Structure:
- IMMEDIATE: Resolve specific conflict
- SERVES: Relationship health
- KEY QUESTIONS: Pattern or isolated? Both parties want resolution?
→ Route to: /araw (explore relationship dynamics)
```

### Pattern 4: Skill/Learning Goal
```
Indicators: "want to learn", "improve at", "become better"
Structure:
- IMMEDIATE: Acquire skill
- SERVES: Career? Personal? Specific project?
- KEY QUESTIONS: What level? By when? How measure progress?
→ Route to: /skill_acquisition
```

### Pattern 5: Vague Dissatisfaction
```
Indicators: "stuck", "unfulfilled", "something's missing"
Structure:
- IMMEDIATE: Unclear
- SERVES: Unclear
- KEY QUESTIONS: What's working? What's not? Last time you felt fulfilled?
→ Route to: /value_elicitation (find intrinsic goals)
```

---

## Output Format

```
## Parsed Claims
[OPEN/CLOSED classification]

## Goal Journey Structure
[Filled structure with uncertainties marked]

## Questions for User
[Prioritized questions]

## Next Procedure
→ INVOKE: /[next_procedure] [args]
```

---

## Verification Criteria

| Step | Verification |
|------|--------------|
| Step 0 | Context assessed, variant selected |
| Step 0.5 | Original captured, no substitution |
| Step 1 | All claims parsed including implicit |
| Step 2 | Each claim classified with reasoning |
| Step 3 | OPEN claims have ARAW branches |
| Step 4 | Goal Journey filled, uncertainties marked |
| Step 5 | Domain identified |
| Step 6 | Questions generated for unknowns |
| Step 7 | Next procedure identified |

---

## Integration Points

- **Often invoked from**: /procedure_engine (first step for goals), automatic on goal-type input
- **Routes to**: /value_elicitation, /problem_identification, /comparison, /goal_journey_system, /araw
- **Related**: /guess_generation, /question_about_guesses
