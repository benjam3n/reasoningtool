---
name: gg
description: Generate exhaustive guesses about user input using ALL search methods with coverage tracking. Guessing is SEARCH through possibility space. Tracks space created vs space covered to ensure comprehensive exploration.
---

# Guess Generation (Exhaustive Search with Coverage Tracking)

**Input**: $ARGUMENTS

---

## Core Principles

1. **GUESSING IS SEARCH** - Apply ALL search methods systematically
2. **GUESSES CREATE THE SPACE** - Don't assume pre-existing space; guessing reveals it
3. **COVERAGE > COUNT** - 50 guesses covering 10 dimensions > 500 covering 3 dimensions
4. **TRACK WHAT'S COVERED** - Measure dimensions, perspectives, time horizons, not raw count
5. **ADAPTIVE DEPTH** - Go deep where impact is high and confidence is low
6. **MINIMUM DEPTH** - Generate enough guesses that no reviewer can find gaps
7. **ONE QUESTION PER GUESS** - Never bundle multiple questions into one guess
8. **CRUX IDENTIFICATION** - Mark guesses where ASSUME RIGHT vs ASSUME WRONG produce maximally divergent paths
9. **QUESTION HIERARCHY** - Some questions only asked after others (e.g., exact date after precision level)
10. **SHOW THE QUESTION** - Every guess explicitly states what question it answers

---

## Unbundling Rules

**NEVER bundle these into single guesses:**
- When + How long (separate: Q1=precision level, Q2=exact date, Q3=duration hours)
- Who + For whom (separate: Q1=who does work, Q2=who benefits)
- Method + Time (separate: Q1=what method, Q2=when applied)
- What + Why (separate: Q1=what is it, Q2=why do it)

**Correct structure:**
```
Q1: When do you plan to start? (precision level)
   - Within the next hour [CRUX:HIGH]
   - Within the next day [CRUX:MED]
   - Within the next week [CRUX:MED]
   ...

Q2: What is the exact start date?
   (Only asked after Q1 determines precision)
   - [User provides specific date]
   - Not yet determined
   ...

Q3: How long will it take? (duration in hours)
   - Less than 1 hour [CRUX:HIGH]
   - 1-4 hours [CRUX:MED]
   ...
```

---

## CRUX Identification (ARAW Integration)

A entry is CRUX when ASSUME RIGHT leads to completely different actions than ASSUME WRONG.

### CRUX Rating Framework

**The Test**: "If I flip my assumption on this entry, does my ENTIRE approach change?"

| Rating | % of Total | Definition | Test |
|--------|------------|------------|------|
| **HIGH** | 10-25% | Wrong = solving wrong problem entirely | Strategy completely changes |
| **MED** | 40-50% | Wrong = significant adjustment needed | Approach changes meaningfully |
| **LOW** | 30-40% | Wrong = minor adjustment | Details change, core stays same |

### HIGH-CRUX Examples (strategy changes)
- "Is this reversible?" - One-way door changes everything
- "Who is the actual decision maker?" - Wrong person = wasted effort
- "Is the stated want the actual want?" - Wrong target entirely
- "Are they in crisis?" - Crisis response vs normal pace
- "Is this the real goal or proxy?" - Solving for wrong level

### MED-CRUX Examples (approach changes)
- "How complex is this?" - Changes effort level, not goal
- "What resources are available?" - Constrains options, doesn't change goal
- "What's the timeline precision?" - Shapes approach, doesn't redirect it

### LOW-CRUX Examples (details change)
- "Exact number of stakeholders (3 vs 5)" - Scale detail
- "Specific tool choice" - Implementation detail
- "Documentation format" - Output detail

### Common Mistakes
- Marking everything HIGH because "it matters"
- Marking HIGH because information is unknown
- Confusing "would be good to know" with "changes everything"

### Table Format (with "Why This Rating")
```
| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Immediate (now) | HIGH | Crisis mode vs planned = different | Drop everything | Can plan first |
| This week | MED | Near-term changes priority | High priority | Lower priority |
| This month | LOW | Flexible, details change | Standard planning | Adjust timeline |
```

**Ask HIGH-CRUX questions first** - they eliminate most uncertainty fastest.

**Reference**: See `/data/guess_libraries/TEMPLATE_unbundled_v2.md` for framework.
See `/data/guess_libraries/universal/06_why_reason.md` for example with correct distribution.

---

## Minimum Depth Requirements

**For each method, generate AT LEAST:**

| Method | Minimum Per Applicable Category |
|--------|--------------------------------|
| Morphological (AGENT) | 8+ variations |
| Morphological (ACTION) | 12+ variations |
| Morphological (OBJECT) | 10+ variations |
| Morphological (REASON) | 15+ variations |
| Morphological (METHOD) | 15+ variations |
| Morphological (TIME) | 8+ variations |
| Morphological (DEGREE) | 10+ variations |
| Morphological (CERTAINTY) | 8+ variations |
| Morphological (SCOPE) | 6+ variations |
| Morphological (CONSTRAINTS) | 15+ variations |
| SCAMPER (each operation) | 4+ variations |
| Stakeholder Perspectives | 12+ perspectives |
| Time Horizons | 12+ variations |
| Claim Types (each) | 4+ variations |
| Analogy Domains (each) | 4+ variations |
| Pre-Mortem (each error type) | 2+ variations |

**Total minimum**: 200+ guesses for any meaningful input

**Reference**: See `/docs/example_comprehensive_guess_generation.md` for a complete example with 238 guesses.

---

## Derivation Requirement

Every guess must show derivation:
- `[D: from morphological AGENT dimension]`
- `[D: from SCAMPER Substitute operation]`
- `[D: from analogy to biology domain]`
- `[D: from pre-mortem perception error check]`

Do NOT list guesses without showing which method generated them.

---

## Step 0: Check Guess Library First

Before generating guesses from scratch, check if a pre-generated library exists:

```bash
python scripts/guess_library.py lookup "$INPUT"
```

**If library found**:
1. Retrieve with: `python scripts/guess_library.py get [library_id]`
2. Review the 200+ pre-generated guesses
3. Customize for this specific user if needed
4. Skip to Step 13 (Coverage Analysis)

**If no library found**:
1. Continue with full generation below
2. After completing, save to library with: `python scripts/guess_library.py add`

**Related goals**: Check for related goal chains that share guesses:
```bash
python scripts/guess_library.py related [library_id]
```

---

## Step 0.5: Select Coverage Mode

Choose based on space size (from `/space_discovery` or estimated):

| Mode | When to Use | What It Does |
|------|-------------|--------------|
| **EXHAUSTIVE** | Stakes high, space small | All methods, all dimensions |
| **TARGETED** | Time-constrained, space large | High-impact regions only |
| **ADAPTIVE** | Uncertain stakes | Start broad, go deep on signal |
| **BOUNDARY** | New/unknown problem | Map edges before interior |

**Selected mode**: [MODE]
**Reason**: [why this mode fits]

---

## Step 1: Filter Non-Guesses

| Type | Test | Action |
|------|------|--------|
| Definition | About words | Accept |
| Technique | Method | Accept |
| Category | Classification | Accept |
| Question | Requesting | Answer |
| Command | Directing | Execute |

**Non-guesses**: [list]

---

## Step 2: Parse Surface Claims

Extract ALL claims (aim for 10-20 per sentence):

1. Explicit claims (stated directly)
2. Implicit claims (assumed but not stated)
3. Presupposition claims (must be true for statement to make sense)
4. Implicature claims (conversationally implied)

**Surface claims extracted**: [list]

---

## Step 3: Depth Decision (Per Claim)

For each claim, decide depth before exploring:

| Claim | Impact if Wrong | Confidence | Depth Decision |
|-------|-----------------|------------|----------------|
| [claim 1] | HIGH/MED/LOW | HIGH/MED/LOW | DEEP/SHALLOW |
| [claim 2] | HIGH/MED/LOW | HIGH/MED/LOW | DEEP/SHALLOW |

**Depth rules**:
- HIGH impact + LOW confidence → DEEP (full unbundling, all inversions, analogy search)
- HIGH impact + HIGH confidence → MEDIUM (verify assumptions)
- LOW impact + any confidence → SHALLOW (note and move on, 1-2 unbundlings max)

---

## Step 4: Morphological Analysis

### Dimension Enumeration (Track Coverage)

| Dimension | Applicable? | Values Enumerated | Covered? |
|-----------|-------------|-------------------|----------|
| AGENT (who) | YES/NO | [values] | ✓/✗ |
| ACTION (what) | YES/NO | [values] | ✓/✗ |
| OBJECT (affected) | YES/NO | [values] | ✓/✗ |
| REASON (why) | YES/NO | [values] | ✓/✗ |
| METHOD (how) | YES/NO | [values] | ✓/✗ |
| TIME (when) | YES/NO | [values] | ✓/✗ |
| LOCATION (where) | YES/NO | [values] | ✓/✗ |
| DEGREE (how much) | YES/NO | [values] | ✓/✗ |
| CERTAINTY (how sure) | YES/NO | [values] | ✓/✗ |
| SCOPE (how broadly) | YES/NO | [values] | ✓/✗ |

**Dimension coverage**: [N] / 10 dimensions covered

---

## Step 5: SCAMPER Transformations (Track Coverage)

| Operation | Applied? | Variations Generated |
|-----------|----------|---------------------|
| S - Substitute | ✓/✗ | [count] |
| C - Combine | ✓/✗ | [count] |
| A - Adapt | ✓/✗ | [count] |
| M - Modify | ✓/✗ | [count] |
| P - Put to other use | ✓/✗ | [count] |
| E - Eliminate | ✓/✗ | [count] |
| R - Reverse | ✓/✗ | [count] |

**SCAMPER coverage**: [N] / 7 operations applied

---

## Step 6: Perspective Coverage (Stakeholders)

| Stakeholder | Considered? | Guesses from This View |
|-------------|-------------|------------------------|
| Speaker/user | ✓/✗ | [count] |
| Direct beneficiaries | ✓/✗ | [count] |
| Direct losers | ✓/✗ | [count] |
| Implementers | ✓/✗ | [count] |
| Future selves | ✓/✗ | [count] |
| Adversaries | ✓/✗ | [count] |

**Perspective coverage**: [N] stakeholders considered

---

## Step 7: Time Horizon Coverage

| Horizon | Considered? | Guesses from This Frame |
|---------|-------------|------------------------|
| Immediate (now) | ✓/✗ | [count] |
| Short-term | ✓/✗ | [count] |
| Medium-term | ✓/✗ | [count] |
| Long-term | ✓/✗ | [count] |
| Historical | ✓/✗ | [count] |

**Time coverage**: [N] / 5 horizons covered

---

## Step 8: Inversion Coverage

For each surface claim:

| Claim | Assume-Right Explored? | Assume-Wrong Explored? |
|-------|------------------------|------------------------|
| [claim 1] | ✓/✗ | ✓/✗ |
| [claim 2] | ✓/✗ | ✓/✗ |

**Inversion coverage**: [N]% of claims have both branches

---

## Step 9: Claim Type Coverage

| Type | Guesses Generated? | Count |
|------|-------------------|-------|
| Factual | ✓/✗ | [N] |
| Causal | ✓/✗ | [N] |
| Predictive | ✓/✗ | [N] |
| Normative | ✓/✗ | [N] |
| Modal | ✓/✗ | [N] |
| Relational | ✓/✗ | [N] |
| Intentional | ✓/✗ | [N] |
| Meta | ✓/✗ | [N] |

**Type coverage**: [N] / 8 types represented

---

## Step 10: Analogy Search (10 Domains)

| Domain | Searched? | Analogies Found |
|--------|-----------|-----------------|
| Biology | ✓/✗ | [guesses] |
| Physics | ✓/✗ | [guesses] |
| Economics | ✓/✗ | [guesses] |
| Psychology | ✓/✗ | [guesses] |
| Engineering | ✓/✗ | [guesses] |
| Military | ✓/✗ | [guesses] |
| Nature | ✓/✗ | [guesses] |
| Games | ✓/✗ | [guesses] |
| History | ✓/✗ | [guesses] |
| Medicine | ✓/✗ | [guesses] |

**Analogy coverage**: [N] / 10 domains searched

---

## Step 11: Unbundling (Deep for DEEP claims only)

For DEEP claims, apply all unbundling patterns:

**Patterns to apply**:
- "I [verb]" → 6 hidden guesses
- "[noun] is [adjective]" → 7 hidden guesses
- "because [reason]" → 7 hidden guesses
- "want/need" → 7 hidden guesses
- "improve/better/good" → 7 hidden guesses
- "system" → 7 hidden guesses

For SHALLOW claims, apply 1-2 patterns only.

**Unbundling done**: [summary]

---

## Step 12: Pre-Mortem (15 Error Types)

For key claims, check each error type:

| Error Type | Checked? | Finding |
|------------|----------|---------|
| Perception error | ✓/✗ | [guess if applicable] |
| Memory error | ✓/✗ | [guess if applicable] |
| Interpretation error | ✓/✗ | [guess if applicable] |
| Source error | ✓/✗ | [guess if applicable] |
| Selection bias | ✓/✗ | [guess if applicable] |
| Confirmation bias | ✓/✗ | [guess if applicable] |
| Availability bias | ✓/✗ | [guess if applicable] |
| Anchoring | ✓/✗ | [guess if applicable] |
| Motivated reasoning | ✓/✗ | [guess if applicable] |
| Social pressure | ✓/✗ | [guess if applicable] |
| False dichotomy | ✓/✗ | [guess if applicable] |
| Scope error | ✓/✗ | [guess if applicable] |
| Timing error | ✓/✗ | [guess if applicable] |
| Causation error | ✓/✗ | [guess if applicable] |
| Definition error | ✓/✗ | [guess if applicable] |

**Pre-mortem coverage**: [N] / 15 error types checked

---

## Step 13: Space Created vs Space Covered

### Space Created (by guessing)

```
Dimensions discovered: [list]
Regions identified: [list clusters of guesses]
Boundaries found: [edges of the space]
```

### Space Coverage Analysis

```
COVERAGE METRICS SUMMARY:
├── Dimensions: [N]/10 covered ([%])
├── SCAMPER: [N]/7 operations ([%])
├── Perspectives: [N] stakeholders
├── Time horizons: [N]/5 ([%])
├── Inversion: [N]% of claims both branches
├── Claim types: [N]/8 ([%])
├── Analogies: [N]/10 domains ([%])
├── Pre-mortem: [N]/15 errors ([%])
└── OVERALL: [weighted average]%

GAPS IDENTIFIED:
├── Uncovered dimensions: [list]
├── Missing perspectives: [list]
├── Missing time horizons: [list]
├── Claims without inversion: [list]
├── Missing claim types: [list]
└── Unsearched domains: [list]
```

---

## Step 14: Fill Gaps or Justify Skipping

For each gap identified:

| Gap | Action | Reason |
|-----|--------|--------|
| [gap 1] | FILL / SKIP | [if skip: why it's OK to skip] |
| [gap 2] | FILL / SKIP | [if skip: why it's OK to skip] |

**Strategic skips** (justified under-coverage):
- [gap]: [reason to skip]

**Gaps filled**: [list guesses added to fill gaps]

---

## Step 15: Confidence × Impact Matrix

Plot all guesses:

```
                     HIGH IMPACT IF WRONG
                            │
    ┌───────────────────────┼───────────────────────┐
    │                       │                       │
    │   INVESTIGATE         │   CRITICAL            │
    │   (worth checking)    │   (must verify)       │
    │                       │                       │
LOW ├───────────────────────┼───────────────────────┤ HIGH
CONF│                       │                       │ CONF
    │   ACKNOWLEDGE         │   TRUST               │
    │   (note uncertainty)  │   (probably true)     │
    │                       │                       │
    └───────────────────────┼───────────────────────┘
                            │
                     LOW IMPACT IF WRONG
```

**Critical guesses** (High Impact × Low Confidence): [list]

---

## Output Format

```
## INPUT PARSED
[original input]

## COVERAGE MODE
Mode: [EXHAUSTIVE/TARGETED/ADAPTIVE/BOUNDARY]
Reason: [why]

## DEPTH DECISIONS
[table of claims with DEEP/SHALLOW assignments]

## GUESSES GENERATED
[organized by method: morphological, SCAMPER, analogy, inversion, unbundling, pre-mortem]

## COVERAGE METRICS
Dimensions: [N]/10 ([%])
SCAMPER: [N]/7 ([%])
Perspectives: [N] stakeholders
Time horizons: [N]/5 ([%])
Inversion: [N]%
Claim types: [N]/8 ([%])
Analogies: [N]/10 ([%])
Pre-mortem: [N]/15 ([%])
OVERALL: [%]

## GAPS
Identified: [list]
Filled: [list]
Justified skips: [list with reasons]

## SPACE ANALYSIS
Space created: [dimensions discovered, regions identified]
Space covered: [%]
Blind spots: [any remaining]

## CRITICAL GUESSES
[High Impact × Low Confidence - must question these]

## TOTAL
Guesses: [N]
Coverage: [%]
```

---

## Execution Checklist

Before completing, verify:
- [ ] Coverage mode selected with reason
- [ ] Depth decisions made for each claim
- [ ] All 10 dimensions checked (covered or N/A)
- [ ] All 7 SCAMPER operations applied
- [ ] Multiple stakeholder perspectives considered
- [ ] Multiple time horizons considered
- [ ] Both assume-right and assume-wrong for each claim
- [ ] All 8 claim types checked
- [ ] 10 analogy domains searched
- [ ] 15 pre-mortem error types checked
- [ ] Gaps identified and either filled or justified
- [ ] Coverage metrics calculated
- [ ] Critical guesses identified

---

## Next Procedure

→ INVOKE: /question_about_guesses [CRITICAL guesses]

---

**Execute now**: Generate guesses with full coverage tracking.
