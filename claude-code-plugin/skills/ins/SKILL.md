---
name: "ins - Insight Synthesis"
description: Synthesize insights from multiple sources into coherent, actionable understanding. Combines extraction, inversion, and analogy into unified insights.
---

# Insight Synthesis

**Input**: $ARGUMENTS

---

## Purpose

Combine insights from multiple sources and methods into **coherent, actionable understanding**:
- Integrate findings from assumption extraction, inversion, and analogy
- Resolve contradictions between sources
- Identify patterns across methods
- Generate novel insights from combinations
- Produce clear, prioritized recommendations

**This skill is the culmination** of the insight generation pipeline.

---

## Input Sources

Insight synthesis can draw from:

| Source | What It Provides | How to Invoke |
|--------|-----------------|---------------|
| **Assumption Extraction** | Hidden assumptions, risk ratings | `/aex` |
| **Assumption Inversion** | Blind spots, alternatives, failure modes | `/ai` |
| **Cross-Domain Analogy** | Imported solutions, fresh perspectives | `/cda` |
| **ARAW Analysis** | Validated/invalidated claims | `/araw` |
| **UAUA Analysis** | Comprehensive option exploration | `/uaua` |
| **Direct Observation** | Empirical data, user statements | [O: source] markers |
| **Domain Knowledge** | Expert input, research findings | External sources |

---

## The Synthesis Process

### Step 1: Collect Insights

Gather insights from all sources:

```
INSIGHT COLLECTION: [topic]

FROM ASSUMPTION EXTRACTION:
1. [Insight 1]
2. [Insight 2]
...

FROM ASSUMPTION INVERSION:
1. [Insight 1]
2. [Insight 2]
...

FROM CROSS-DOMAIN ANALOGY:
1. [Insight 1]
2. [Insight 2]
...

FROM ARAW/UAUA:
1. [Insight 1]
2. [Insight 2]
...

FROM DIRECT OBSERVATION:
1. [Insight 1]
2. [Insight 2]
...

TOTAL INSIGHTS: [N]
```

---

### Step 2: Categorize Insights

Group insights by type:

```
INSIGHT CATEGORIZATION:

ABOUT THE PROBLEM (what's really going on):
- [Insight]
- [Insight]

ABOUT ASSUMPTIONS (what we're taking for granted):
- [Insight]
- [Insight]

ABOUT BLIND SPOTS (what we're missing):
- [Insight]
- [Insight]

ABOUT SOLUTIONS (what we could do):
- [Insight]
- [Insight]

ABOUT RISKS (what could go wrong):
- [Insight]
- [Insight]

ABOUT OPPORTUNITIES (what we could gain):
- [Insight]
- [Insight]

ABOUT PROCESS (how to proceed):
- [Insight]
- [Insight]
```

---

### Step 3: Identify Patterns

Look for patterns across insights:

```
PATTERN DETECTION:

CONVERGENCE (multiple sources agree):
- [Pattern 1]: Supported by [source A], [source B], [source C]
  Confidence: HIGH
- [Pattern 2]: Supported by [source A], [source B]
  Confidence: MEDIUM

DIVERGENCE (sources contradict):
- [Topic 1]: [Source A] says X, [Source B] says Y
  Resolution: [how to resolve]
- [Topic 2]: [Source A] says X, [Source B] says Y
  Resolution: [how to resolve]

UNIQUE (only one source):
- [Insight]: Only from [source]
  Reliability: [assessment]

EMERGENT (appears only in combination):
- [Insight]: [Source A] + [Source B] together suggest [new insight]
  This is a NOVEL insight not present in any single source
```

---

### Step 4: Resolve Contradictions

For each divergence:

```
CONTRADICTION RESOLUTION: [Topic]

Source A says: [claim A]
Source B says: [claim B]

ANALYSIS:
- Are they actually contradicting? [Yes/No/Partial]
- Could both be true in different contexts? [Yes/No]
- Which has stronger evidence? [A/B/Equal]
- What would resolve this? [evidence needed]

RESOLUTION:
- [Resolved position]
- Confidence: [level]
- Remaining uncertainty: [what's still unknown]
```

---

### Step 5: Generate Novel Insights

Combine insights to create new understanding:

```
NOVEL INSIGHT GENERATION:

COMBINATION 1:
- Insight A: [insight from source 1]
- Insight B: [insight from source 2]
- Combined insight: [what emerges when you consider both]
- Why this matters: [significance]

COMBINATION 2:
- Insight A: [insight from source 1]
- Insight B: [insight from source 2]
- Insight C: [insight from source 3]
- Combined insight: [what emerges]
- Why this matters: [significance]

META-INSIGHT:
Looking across all insights, the deeper pattern is:
[Higher-level understanding that explains multiple insights]
```

---

### Step 6: Prioritize Insights

Rank insights by impact and actionability:

```
INSIGHT PRIORITIZATION:

| Insight | Impact | Actionability | Confidence | Priority |
|---------|--------|---------------|------------|----------|
| [Insight 1] | High | High | High | 1 |
| [Insight 2] | High | Medium | High | 2 |
| [Insight 3] | High | High | Medium | 3 |
| [Insight 4] | Medium | High | High | 4 |
...

IMPACT: How much does this change understanding or action?
ACTIONABILITY: Can we do something with this?
CONFIDENCE: How certain are we this is correct?
PRIORITY: Overall ranking considering all factors
```

---

### Step 7: Generate Synthesis Output

```
===================================================
INSIGHT SYNTHESIS: [topic]
===================================================

EXECUTIVE SUMMARY:
[2-3 sentences capturing the most important insights]

===================================================

KEY INSIGHTS (prioritized):

1. [INSIGHT 1] ** HIGHEST PRIORITY **
   Source: [where this came from]
   Confidence: [level]
   Implication: [what this means]
   Action: [what to do about it]

2. [INSIGHT 2]
   Source: [where this came from]
   Confidence: [level]
   Implication: [what this means]
   Action: [what to do about it]

3. [INSIGHT 3]
   Source: [where this came from]
   Confidence: [level]
   Implication: [what this means]
   Action: [what to do about it]

[Continue for top 5-7 insights]

===================================================

CONVERGENT FINDINGS (high confidence):

These insights are supported by multiple independent sources:

- [Finding 1]
  Evidence: [sources that support]

- [Finding 2]
  Evidence: [sources that support]

===================================================

NOVEL INSIGHTS (emerged from synthesis):

These insights were not present in any single source:

- [Novel insight 1]
  Derived from: [combination of sources]
  Significance: [why this matters]

- [Novel insight 2]
  Derived from: [combination of sources]
  Significance: [why this matters]

===================================================

REMAINING UNCERTAINTIES:

- [Uncertainty 1]: Would need [evidence] to resolve
- [Uncertainty 2]: Would need [evidence] to resolve

===================================================

RECOMMENDED ACTIONS:

IMMEDIATE (high priority, can do now):
[ ] [Action 1]
[ ] [Action 2]

SHORT-TERM (within [timeframe]):
[ ] [Action 3]
[ ] [Action 4]

TO INVESTIGATE (need more information):
[ ] [Investigation 1]
[ ] [Investigation 2]

===================================================

SYNTHESIS METADATA:
- Sources used: [list]
- Total insights collected: [N]
- Contradictions resolved: [N]
- Novel insights generated: [N]
- Confidence level: [overall assessment]

===================================================
```

---

## Quick Synthesis (Abbreviated)

For fast insight integration:

```
QUICK SYNTHESIS: [topic]

Sources: [list what was analyzed]

Top 3 insights:
1. [Highest priority insight]
2. [Second priority]
3. [Third priority]

Novel insight: [something that emerged from combination]

Main action: [single most important thing to do]
```

---

## Example: Synthesizing Analysis of "Sales Team Performance"

### Input
- Assumption extraction: Found 12 assumptions
- Assumption inversion: Found 5 blind spots
- Cross-domain analogy: Military, sports insights
- Direct observation: Metrics data

### Synthesis

```
EXECUTIVE SUMMARY:
Sales underperformance stems from misaligned incentives and unclear territories,
not skill gaps. The team has capability but is fighting the system. Quick wins
are possible through territory redesign and comp plan simplification.

KEY INSIGHTS:

1. INCENTIVES ARE MISALIGNED ** TOP **
   Source: Assumption inversion + direct observation
   Confidence: HIGH
   Implication: Comp plan rewards wrong behaviors
   Action: Audit comp plan against desired behaviors

2. TERRITORY OVERLAP CAUSES CONFLICT
   Source: Cross-domain analogy (military) + direct observation
   Confidence: HIGH
   Implication: Reps compete with each other, not competitors
   Action: Clear territory boundaries

3. SKILL GAP ASSUMPTION IS WRONG
   Source: Assumption inversion
   Confidence: MEDIUM
   Implication: Training won't help; structural fix needed
   Action: Pause training, focus on structure

NOVEL INSIGHT:
Combining military "clear command" with sports "defined positions":
The team needs clear "positions" with non-overlapping responsibilities,
not just territories. Who owns relationship vs. who closes?

MAIN ACTION: Redesign territories and roles before any other intervention.
```

---

## Synthesis Quality Markers

| Marker | Meaning |
|--------|---------|
| **[CONVERGENT]** | Multiple sources agree |
| **[NOVEL]** | Emerged from synthesis, not single source |
| **[UNCERTAIN]** | Insufficient evidence |
| **[ACTIONABLE]** | Clear next step exists |
| **[STRATEGIC]** | Changes direction, not just tactics |

---

## Quality Checklist

Before completing:
- [ ] All available sources collected
- [ ] Insights categorized by type
- [ ] Patterns identified (convergence, divergence, unique)
- [ ] Contradictions resolved or flagged
- [ ] Novel insights generated from combinations
- [ ] Insights prioritized by impact/actionability/confidence
- [ ] Synthesis output generated
- [ ] Actions recommended
- [ ] Uncertainties acknowledged

---

## Integration

This skill typically comes AFTER:
- `/aex` -> Surface hidden assumptions
- `/ai` -> Find blind spots
- `/cda` -> Import outside solutions
- `/araw` or `/uaua` -> Rigorous claim testing

Full insight generation pipeline:
```
[Input]
    ->
/aex -> Hidden assumptions
    ->
/ai -> Blind spots, alternatives
    ->
/cda -> Outside perspectives
    ->
/ins -> Combined, prioritized insights
    ->
[Actionable understanding]
```
