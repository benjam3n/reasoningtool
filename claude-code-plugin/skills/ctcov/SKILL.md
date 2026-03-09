---
name: "ctcov - Cognitive Coverage Analysis"
description: "Assess whether a system covers all types of thinking. Identifies gaps across cognitive dimensions and recommends additions."
---

# Cognitive Coverage Analysis

**Input**: $ARGUMENTS

---

## Step 1: Define the System Under Analysis

Identify what you're assessing for cognitive coverage.

1. What is the system? (toolkit, curriculum, team, process, framework)
2. What is its stated purpose?
3. Who uses it and in what contexts?

```
SYSTEM: [name/description]
PURPOSE: [what it's for]
USERS: [who uses it and when]
```

---

## Step 2: Enumerate Cognitive Dimensions

Assess coverage across these fundamental types of thinking:

### A. Perception and Attention
- **Pattern recognition**: Noticing regularities, anomalies, trends
- **Signal detection**: Separating important information from noise
- **Perspective-taking**: Seeing from other viewpoints

### B. Reasoning and Logic
- **Deductive reasoning**: Drawing conclusions from premises
- **Inductive reasoning**: Generalizing from specific cases
- **Abductive reasoning**: Inferring the best explanation
- **Analogical reasoning**: Transferring insights between domains
- **Causal reasoning**: Understanding cause and effect

### C. Memory and Knowledge
- **Knowledge capture**: Recording what's learned
- **Knowledge retrieval**: Finding what was recorded
- **Knowledge transfer**: Applying knowledge in new contexts
- **Knowledge pruning**: Removing outdated information

### D. Creativity and Generation
- **Divergent thinking**: Generating many options
- **Convergent thinking**: Narrowing to the best option
- **Recombination**: Combining existing ideas in new ways
- **Imagination**: Envisioning what doesn't yet exist

### E. Judgment and Decision
- **Evaluation**: Assessing quality or value
- **Prioritization**: Ranking by importance
- **Risk assessment**: Estimating downside
- **Trade-off analysis**: Weighing competing goods

### F. Metacognition
- **Self-monitoring**: Checking your own reasoning
- **Bias detection**: Noticing systematic errors
- **Calibration**: Aligning confidence with accuracy
- **Strategy selection**: Choosing how to think about something

### G. Social Cognition
- **Empathy**: Understanding others' emotional states
- **Motivation modeling**: Understanding why people act
- **Communication design**: Crafting messages for audiences
- **Collaboration**: Thinking with others effectively

### H. Emotional Processing
- **Emotion recognition**: Identifying what you're feeling and why
- **Emotion regulation**: Managing emotional responses
- **Emotional intelligence**: Using emotions as information
- **Stress management**: Thinking clearly under pressure

---

## Step 3: Assess Coverage

For each sub-dimension, rate the system's coverage:

```
COVERAGE MAP:

A. Perception and Attention
   - Pattern recognition:  [STRONG / PARTIAL / ABSENT]
   - Signal detection:     [STRONG / PARTIAL / ABSENT]
   - Perspective-taking:   [STRONG / PARTIAL / ABSENT]

B. Reasoning and Logic
   - Deductive:    [STRONG / PARTIAL / ABSENT]
   - Inductive:    [STRONG / PARTIAL / ABSENT]
   - Abductive:    [STRONG / PARTIAL / ABSENT]
   - Analogical:   [STRONG / PARTIAL / ABSENT]
   - Causal:       [STRONG / PARTIAL / ABSENT]

C. Memory and Knowledge
   - Capture:    [STRONG / PARTIAL / ABSENT]
   - Retrieval:  [STRONG / PARTIAL / ABSENT]
   - Transfer:   [STRONG / PARTIAL / ABSENT]
   - Pruning:    [STRONG / PARTIAL / ABSENT]

D. Creativity and Generation
   - Divergent:      [STRONG / PARTIAL / ABSENT]
   - Convergent:     [STRONG / PARTIAL / ABSENT]
   - Recombination:  [STRONG / PARTIAL / ABSENT]
   - Imagination:    [STRONG / PARTIAL / ABSENT]

E. Judgment and Decision
   - Evaluation:     [STRONG / PARTIAL / ABSENT]
   - Prioritization: [STRONG / PARTIAL / ABSENT]
   - Risk:           [STRONG / PARTIAL / ABSENT]
   - Trade-offs:     [STRONG / PARTIAL / ABSENT]

F. Metacognition
   - Self-monitoring:    [STRONG / PARTIAL / ABSENT]
   - Bias detection:     [STRONG / PARTIAL / ABSENT]
   - Calibration:        [STRONG / PARTIAL / ABSENT]
   - Strategy selection:  [STRONG / PARTIAL / ABSENT]

G. Social Cognition
   - Empathy:          [STRONG / PARTIAL / ABSENT]
   - Motivation:       [STRONG / PARTIAL / ABSENT]
   - Communication:    [STRONG / PARTIAL / ABSENT]
   - Collaboration:    [STRONG / PARTIAL / ABSENT]

H. Emotional Processing
   - Recognition:   [STRONG / PARTIAL / ABSENT]
   - Regulation:    [STRONG / PARTIAL / ABSENT]
   - Intelligence:  [STRONG / PARTIAL / ABSENT]
   - Stress:        [STRONG / PARTIAL / ABSENT]
```

---

## Step 4: Identify and Prioritize Gaps

1. List all ABSENT dimensions
2. List all PARTIAL dimensions
3. For each gap, assess frequency of need:
   - **HIGH**: Users encounter this need regularly
   - **MEDIUM**: Users encounter this need occasionally
   - **LOW**: Users encounter this need rarely

```
PRIORITY GAPS:
1. [dimension] — Frequency: [HIGH] — Impact of gap: [description]
2. [dimension] — Frequency: [HIGH] — Impact of gap: [description]
...

SECONDARY GAPS:
1. [dimension] — Frequency: [MEDIUM]
...
```

---

## Step 5: Recommend Additions

For each priority gap, recommend a specific addition:

```
RECOMMENDATIONS:
1. Gap: [dimension]
   Add: [specific tool/skill/component]
   Why: [how this fills the gap]
   Effort: [small / medium / large]

2. Gap: [dimension]
   Add: [specific tool/skill/component]
   ...
```

Also note if any existing components could be EXTENDED to cover nearby gaps rather than creating new ones.

---

## Step 6: Summary

```
OVERALL COVERAGE: [X]% of dimensions at STRONG, [Y]% PARTIAL, [Z]% ABSENT
STRONGEST AREA: [category]
WEAKEST AREA: [category]
TOP 3 ADDITIONS TO MAKE: [list]
```

---

## Integration

Use with:
- `/tkint` -> Check structural integrity alongside cognitive coverage
- `/se` -> Explore what a complete version of the system would look like
- `/spec` -> Speculate on what novel cognitive tools might look like
- `/curd` -> Design a learning path to build missing cognitive capabilities
