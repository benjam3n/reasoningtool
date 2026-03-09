---
name: "exps - Exploration"
description: Systematically explores an unfamiliar space by mapping boundaries, identifying dimensions, sampling broadly, and flagging surprises and promising regions.
---

# Exploration

**Input**: $ARGUMENTS

---

## Step 1: Map the Boundaries

Define the edges of the space before exploring the interior.

```
SPACE DEFINITION:
- Domain: [what area are we exploring?]
- In scope: [what's included]
- Out of scope: [what's excluded and why]
- Known unknowns: [things we know we don't know]
- Adjacent spaces: [related areas we're not exploring yet]
```

Rule: If you can't define the boundaries, the space is too vague. Narrow it.

---

## Step 2: Identify Dimensions

Find the axes along which this space varies.

```
DIMENSIONS:
1. [Dimension 1]: [what it measures] — range: [low end] to [high end]
2. [Dimension 2]: [what it measures] — range: [low end] to [high end]
3. [Dimension 3]: [what it measures] — range: [low end] to [high end]
4. [Dimension 4]: [what it measures] — range: [low end] to [high end]
```

Aim for 3-6 dimensions. Fewer means you're missing structure. More means some dimensions are redundant.

---

## Step 3: Sample Broadly

Take a wide sweep before going deep anywhere.

```
BROAD SAMPLE:

| Region | Description | Initial Assessment | Promising? |
|--------|------------|-------------------|------------|
| [region 1] | [what's here] | [first impression] | [yes/maybe/no] |
| [region 2] | [what's here] | [first impression] | [yes/maybe/no] |
| [region 3] | [what's here] | [first impression] | [yes/maybe/no] |
| [region 4] | [what's here] | [first impression] | [yes/maybe/no] |
| [region 5] | [what's here] | [first impression] | [yes/maybe/no] |
| [region 6] | [what's here] | [first impression] | [yes/maybe/no] |
```

Rule: Sample at least 5 regions. Resist the pull to dive deep into the first interesting thing.

---

## Step 4: Track Coverage

Monitor what's been explored and what hasn't.

```
COVERAGE MAP:
- Explored: [list of regions/dimensions covered]
- Unexplored: [list of regions/dimensions not yet touched]
- Coverage estimate: [rough percentage of the space sampled]
- Biggest gap: [the largest unexplored area]
```

---

## Step 5: Identify Promising Regions

Flag the areas worth going deeper on.

```
PROMISING REGIONS:
1. [Region]: [why it's promising] — confidence: [high/medium/low]
2. [Region]: [why it's promising] — confidence: [high/medium/low]
3. [Region]: [why it's promising] — confidence: [high/medium/low]

RANKING CRITERIA: [what makes a region "promising" in this context]
```

---

## Step 6: Flag Surprises and Anomalies

Note anything unexpected — these are often the most valuable findings.

```
SURPRISES:
- [Surprise 1]: Expected [X], found [Y] — significance: [high/medium/low]
- [Surprise 2]: Expected [X], found [Y] — significance: [high/medium/low]

ANOMALIES:
- [Anomaly 1]: [what's unusual] — worth investigating: [yes/no]
- [Anomaly 2]: [what's unusual] — worth investigating: [yes/no]
```

SKIP: If no surprises emerged, that itself is worth noting — the space may be well-understood.

---

## Step 7: Exploration Summary

Synthesize findings into an actionable map.

```
EXPLORATION REPORT:
- Space: [one-line description]
- Key dimensions: [the 2-3 most important]
- Most promising: [top region and why]
- Biggest surprise: [most unexpected finding]
- Recommended next step: [go deep on X / explore Y / analyze Z]
```

---

## Integration

Use with:
- `/ornt` -> Orient first, then explore the identified space
- `/anst` -> Analyze the most promising regions in depth
- `/se` -> Enumerate options within a promising region
- `/dd` -> Deep-dive into a specific region after broad exploration
