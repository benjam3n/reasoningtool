---
name: space_discovery
description: Discover what space exists BEFORE generating guesses. Maps dimensions, stakeholders, time horizons, and adjacent spaces. Run this before guess_generation to ensure comprehensive coverage.
---

# Space Discovery

**Input**: $ARGUMENTS

---

## Core Principle: DISCOVER BEFORE COVERING

Don't assume the space is known. Discover it first.
Guesses CREATE the space - they don't map to a pre-existing space.

This procedure runs BEFORE `/guess_generation` to define what needs to be covered.

---

## Step 1: What COULD This Be About?

List all possible framings of the input:

| Frame | How It Changes the Space |
|-------|-------------------------|
| Literal interpretation | [what space does this create?] |
| Metaphorical interpretation | [what space does this create?] |
| Surface-level reading | [what space does this create?] |
| Deep reading | [what space does this create?] |
| Best-case framing | [what space does this create?] |
| Worst-case framing | [what space does this create?] |
| User's likely intent | [what space does this create?] |
| Alternative intents | [what space does this create?] |

**Frames discovered**: [list all, aim for 5-10]

---

## Step 2: Who COULD Care About This?

List all stakeholders who might be affected or have perspectives:

| Stakeholder | Their Perspective | Why It Matters |
|-------------|-------------------|----------------|
| The speaker/user | [their view] | [impact on space] |
| Direct beneficiaries | [their view] | [impact on space] |
| Direct losers | [their view] | [impact on space] |
| Implementers | [their view] | [impact on space] |
| Future selves | [their view] | [impact on space] |
| Society/public | [their view] | [impact on space] |
| Adversaries | [their view] | [impact on space] |
| Neutral observers | [their view] | [impact on space] |

**Stakeholders discovered**: [list all, aim for 5-10]

---

## Step 3: What Time Frames COULD Matter?

List all relevant time horizons:

| Time Horizon | What Changes | Relevance |
|--------------|--------------|-----------|
| Immediate (now) | [what's true now?] | [why it matters] |
| Short-term (days/weeks) | [what changes?] | [why it matters] |
| Medium-term (months) | [what changes?] | [why it matters] |
| Long-term (years) | [what changes?] | [why it matters] |
| Historical context | [what led here?] | [why it matters] |
| Cyclical patterns | [what repeats?] | [why it matters] |
| Irreversible changes | [point of no return?] | [why it matters] |

**Time horizons discovered**: [list all relevant ones]

---

## Step 4: What Dimensions COULD Vary?

For the input, identify ALL axes of variation:

### Standard Dimensions (check each)

| Dimension | Applicable? | Possible Values |
|-----------|-------------|-----------------|
| AGENT (who) | YES/NO | [enumerate if yes] |
| ACTION (what doing) | YES/NO | [enumerate if yes] |
| OBJECT (what affected) | YES/NO | [enumerate if yes] |
| REASON (why) | YES/NO | [enumerate if yes] |
| METHOD (how) | YES/NO | [enumerate if yes] |
| TIME (when) | YES/NO | [enumerate if yes] |
| LOCATION (where) | YES/NO | [enumerate if yes] |
| DEGREE (how much) | YES/NO | [enumerate if yes] |
| CERTAINTY (how sure) | YES/NO | [enumerate if yes] |
| SCOPE (how broadly) | YES/NO | [enumerate if yes] |

### Domain-Specific Dimensions

For this specific input, what OTHER dimensions exist?

| Custom Dimension | Possible Values |
|------------------|-----------------|
| [dimension 1] | [values] |
| [dimension 2] | [values] |
| [dimension 3] | [values] |

**Dimensions discovered**: [count of applicable standard + custom]

---

## Step 5: What Adjacent Spaces COULD Connect?

What related problems/topics connect to this one?

| Adjacent Space | Connection | Why It Matters |
|----------------|------------|----------------|
| [related topic 1] | [how it connects] | [might need to explore] |
| [related topic 2] | [how it connects] | [might need to explore] |
| [related topic 3] | [how it connects] | [might need to explore] |
| [prerequisite] | [must be true for this to matter] | [check first] |
| [consequence] | [follows from this] | [downstream effect] |

**Adjacent spaces discovered**: [list]

---

## Step 6: What Types of Claims COULD Exist?

Check which claim types are relevant:

| Claim Type | Applicable? | Example in This Context |
|------------|-------------|------------------------|
| Factual | YES/NO | [example if yes] |
| Causal | YES/NO | [example if yes] |
| Predictive | YES/NO | [example if yes] |
| Normative | YES/NO | [example if yes] |
| Modal | YES/NO | [example if yes] |
| Relational | YES/NO | [example if yes] |
| Intentional | YES/NO | [example if yes] |
| Meta | YES/NO | [example if yes] |

**Claim types applicable**: [list]

---

## Step 7: Synthesize the Space Map

Combine all discoveries into a space map:

```
SPACE MAP FOR: "[input]"

FRAMES: [count] possible interpretations
├── [frame 1]
├── [frame 2]
└── ...

STAKEHOLDERS: [count] perspectives to consider
├── [stakeholder 1]
├── [stakeholder 2]
└── ...

TIME HORIZONS: [count] relevant
├── [horizon 1]
├── [horizon 2]
└── ...

DIMENSIONS: [count] axes of variation
├── Standard: [which apply]
├── Custom: [domain-specific]
└── Total cells: [product of values]

ADJACENT SPACES: [count] connections
├── [adjacent 1]
├── [adjacent 2]
└── ...

CLAIM TYPES: [count] / 8 applicable
└── [list applicable]

TOTAL SPACE SIZE ESTIMATE:
[frames] × [stakeholders] × [time horizons] × [dimension combinations] = [rough size]
```

---

## Step 8: Recommend Coverage Strategy

Based on space size, recommend coverage mode for `/guess_generation`:

| Space Size | Recommended Mode | Rationale |
|------------|------------------|-----------|
| Small (<100 regions) | EXHAUSTIVE | Can cover everything |
| Medium (100-1000) | ADAPTIVE | Start broad, go deep on signal |
| Large (1000-10000) | TARGETED | Focus on high-impact regions |
| Huge (>10000) | BOUNDARY | Map edges, sample interior |

**Recommended mode**: [MODE]
**Reason**: [why this mode]

---

## Output Format

```
## SPACE DISCOVERED FOR: "[input]"

### Frames: [N]
[list]

### Stakeholders: [N]
[list]

### Time Horizons: [N]
[list]

### Dimensions: [N standard + M custom]
Standard applicable: [list]
Custom discovered: [list]

### Adjacent Spaces: [N]
[list]

### Claim Types: [N/8]
[list applicable]

### Space Size Estimate
[calculation]

### Coverage Recommendation
Mode: [EXHAUSTIVE/ADAPTIVE/TARGETED/BOUNDARY]
Reason: [why]

### Priority Regions
High-impact regions to cover first:
1. [region]
2. [region]
3. [region]

### Skip Candidates
Regions that might be skipped:
1. [region] - [reason to skip]
2. [region] - [reason to skip]
```

---

## Next Procedure

→ INVOKE: /guess_generation [input] --coverage-mode=[MODE] --space-map=[this output]

---

**Execute now**: Discover the space before guessing.
