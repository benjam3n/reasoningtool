---
name: ai
description: Invert assumptions to discover blind spots and alternative possibilities. What if the opposite were true?
---

# Assumption Inversion

**Input**: $ARGUMENTS

---

## Purpose

Take extracted assumptions and **invert** them to discover:
- Blind spots in current thinking
- Alternative possibilities not considered
- Potential failure modes
- Novel approaches

**Why inversion works**:
- Assumptions constrain the solution space
- Inverting opens new regions of possibility
- Many innovations come from questioning "obvious" assumptions

**Prerequisites**: Assumptions extracted (use `/assumption_extraction` first, or provide assumptions directly)

---

## The Inversion Process

### Step 1: List Assumptions to Invert

```
ASSUMPTIONS FOR INVERSION:

Source: [where these came from]

1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]
...
N. [Assumption N]

TOTAL: [N] assumptions
```

---

### Step 2: Apply Inversion Techniques

For each assumption, apply multiple inversion types:

| Technique | Method | Example |
|-----------|--------|---------|
| **Negation** | "What if NOT X?" | "Customers want low prices" -> "What if customers don't want low prices?" |
| **Reversal** | "What if the opposite?" | "We sell to customers" -> "What if customers sell to us?" |
| **Elimination** | "What if X didn't exist?" | "We need a website" -> "What if we had no website?" |
| **Maximization** | "What if X were infinite?" | "Limited budget" -> "What if budget were unlimited?" |
| **Minimization** | "What if X were zero?" | "We have a team" -> "What if team size were zero?" |
| **Time shift** | "What if X were different timing?" | "Launch next quarter" -> "What if we launched yesterday/in 10 years?" |
| **Actor swap** | "What if different actor?" | "We build this" -> "What if competitors/customers built this?" |

---

### Step 3: Structured Inversion

For each assumption:

```
INVERTING: [Assumption]
===================================================

ORIGINAL: [assumption as stated]

INVERSIONS:

1. NEGATION: What if NOT [assumption]?
   -> [inverted statement]
   Implication: [what this would mean]
   Plausibility: [0-100%]

2. REVERSAL: What if the opposite?
   -> [reversed statement]
   Implication: [what this would mean]
   Plausibility: [0-100%]

3. ELIMINATION: What if this didn't exist/matter?
   -> [eliminated version]
   Implication: [what this would mean]
   Plausibility: [0-100%]

4. EXTREME: What if this were 10x or 0.1x?
   -> [extreme version]
   Implication: [what this would mean]
   Plausibility: [0-100%]

MOST INTERESTING INVERSION: [which one]
WHY: [what makes it interesting]

===================================================
```

---

### Step 4: Filter by Plausibility and Interest

```
INVERSION TRIAGE:

HIGH PLAUSIBILITY + HIGH INTEREST (explore deeply):
- [Inversion 1]: [brief description]
- [Inversion 2]: [brief description]

HIGH PLAUSIBILITY + LOW INTEREST (note but don't pursue):
- [Inversion 3]: [brief description]

LOW PLAUSIBILITY + HIGH INTEREST (creative exploration):
- [Inversion 4]: [brief description]

LOW PLAUSIBILITY + LOW INTEREST (discard):
- [Inversion 5]: [brief description]
```

---

### Step 5: Explore Promising Inversions

For each promising inversion, ask:

```
EXPLORING: [Inverted assumption]
===================================================

IF THIS INVERSION WERE TRUE:

1. What would be different?
   - [Consequence 1]
   - [Consequence 2]
   - [Consequence 3]

2. Who would benefit?
   - [Beneficiary 1]
   - [Beneficiary 2]

3. Who would lose?
   - [Loser 1]
   - [Loser 2]

4. What would we do differently?
   - [Action 1]
   - [Action 2]

5. Is there evidence this is already partially true?
   - [Evidence/counter-evidence]

6. What would make this become true?
   - [Trigger 1]
   - [Trigger 2]

INSIGHT FROM THIS INVERSION:
[Key insight or blind spot revealed]

===================================================
```

---

### Step 6: Synthesize Blind Spots and Alternatives

```
===================================================
INVERSION SYNTHESIS: [topic]
===================================================

BLIND SPOTS DISCOVERED:

1. [Blind spot 1]
   Hidden by assumption: [which assumption]
   Revealed by inversion: [which inversion]
   Implication: [what to do about it]

2. [Blind spot 2]
   Hidden by assumption: [which assumption]
   Revealed by inversion: [which inversion]
   Implication: [what to do about it]

===================================================

ALTERNATIVE POSSIBILITIES:

1. [Alternative 1]
   If we assumed: [inverted assumption]
   We could: [new possibility]
   Feasibility: [assessment]

2. [Alternative 2]
   If we assumed: [inverted assumption]
   We could: [new possibility]
   Feasibility: [assessment]

===================================================

FAILURE MODES (inversions that could happen to us):

1. [Failure mode 1]
   If [assumption] becomes false: [consequence]
   Early warning signs: [what to watch]
   Mitigation: [how to prepare]

2. [Failure mode 2]
   If [assumption] becomes false: [consequence]
   Early warning signs: [what to watch]
   Mitigation: [how to prepare]

===================================================

ACTIONABLE INSIGHTS:

1. [Insight 1] -> Action: [what to do]
2. [Insight 2] -> Action: [what to do]
3. [Insight 3] -> Action: [what to do]

===================================================
```

---

## Quick Inversion (Abbreviated)

For fast blind spot discovery:

```
QUICK INVERSION: [topic]

Top 3 assumptions:
1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]

Quick inversions:
1. What if NOT [A1]? -> [implication]
2. What if opposite of [A2]? -> [implication]
3. What if [A3] didn't exist? -> [implication]

Biggest blind spot: [what we're missing]
```

---

## Example: "We need to hire more engineers"

### Assumptions
1. More engineers = more output
2. We need more output
3. Hiring is the way to get engineers
4. Engineers are the bottleneck

### Inversions

**Assumption 1: "More engineers = more output"**
- NEGATION: More engineers ≠ more output
  - Implication: Brooks's Law—adding people to late project makes it later
  - Plausibility: 60% (well-documented phenomenon)

- REVERSAL: Fewer engineers = more output
  - Implication: Small teams move faster, less coordination overhead
  - Plausibility: 40% (depends on context)

**Assumption 4: "Engineers are the bottleneck"**
- NEGATION: Engineers are NOT the bottleneck
  - Implication: Hiring won't help; need to find real bottleneck
  - Plausibility: 50% (often the case)

- ELIMINATION: What if there were no bottleneck?
  - Implication: System is already optimal; expectations are wrong
  - Plausibility: 20%

### Synthesis

```
BLIND SPOTS DISCOVERED:

1. Coordination costs ignored
   Hidden by: "More engineers = more output"
   Revealed by: Negation
   Implication: Calculate coordination cost before hiring

2. Bottleneck assumption untested
   Hidden by: "Engineers are the bottleneck"
   Revealed by: Negation
   Implication: Do bottleneck analysis first

ALTERNATIVE POSSIBILITIES:

1. Improve tooling instead of hiring
   If we assumed: Current engineers are under-leveraged
   We could: Invest in automation, better tools
   Feasibility: High—often better ROI than hiring

2. Reduce scope instead of increasing capacity
   If we assumed: We don't need all planned output
   We could: Prioritize ruthlessly, do less
   Feasibility: Medium—requires stakeholder alignment

FAILURE MODES:

1. If "more = more output" is false
   Consequence: Money wasted, team slower
   Warning signs: Velocity decreasing despite hiring
   Mitigation: Track velocity per engineer
```

---

## Inversion Patterns

### For Business Assumptions
Focus on: Customer assumptions, market assumptions, competitive assumptions

### For Technical Assumptions
Focus on: Scalability assumptions, dependency assumptions, architecture assumptions

### For Process Assumptions
Focus on: Sequence assumptions, role assumptions, resource assumptions

### For Strategy Assumptions
Focus on: Competitive advantage assumptions, market timing assumptions, capability assumptions

---

## Quality Checklist

Before completing:
- [ ] All assumptions listed
- [ ] Multiple inversion techniques applied to each
- [ ] Plausibility and interest rated
- [ ] Promising inversions explored deeply
- [ ] Blind spots identified
- [ ] Alternative possibilities generated
- [ ] Failure modes mapped
- [ ] Actionable insights synthesized

---

## Integration

Use with:
- `/assumption_extraction` -> Extract assumptions first
- `/cross_domain_analogy` -> Find domains where inversions are the norm
- `/insight_synthesis` -> Combine insights from multiple inversions
- `/araw` -> Test inversions with Assume Right / Assume Wrong
