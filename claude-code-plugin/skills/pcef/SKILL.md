---
name: pcef
description: "Unified framework for procedure effectiveness tracking — operational and empirical."
---

# Procedure Effectiveness

**Input**: $ARGUMENTS

---

## Overview

Unified framework for procedure effectiveness tracking. Combines two approaches:
- **OPERATIONAL**: Usage logging, value ratings, tier assignments, action items
- **EMPIRICAL**: Correlation analysis, outcome tracking, statistical thresholds

Use operational tracking after each significant procedure use. Use empirical analysis when you have 5+ projects with structured data.

## Steps

### Step 1: Operational Tracking — Log Usage
After each significant procedure use (>15 minutes):

```
PROCEDURE USE LOG:
Procedure: [name/abbreviation]
Date: [when]
Context: [what problem/goal]
Duration: [how long]
Output quality: [1-5, where 5 = highly valuable output]
Insight generated: [Y/N — did it reveal something you didn't know?]
Action items produced: [N items]
Would use again for similar problem: [Y/N]
Notes: [anything unusual about this use]
```

### Step 2: Operational Tracking — Rate Value
After logging, assign a value rating:

| Rating | Criteria | Description |
|--------|---------|------------|
| 5 — Essential | Changed the outcome | Without this procedure, result would be significantly worse |
| 4 — Valuable | Improved efficiency or quality | Could have gotten there without it, but slower/messier |
| 3 — Useful | Provided structure | Helped organize thinking, but didn't change direction |
| 2 — Marginal | Added little beyond what you'd do naturally | Procedure was overhead, not value |
| 1 — Wasteful | Consumed time without benefit | Would actively avoid next time |

### Step 3: Operational Tracking — Assign Tier
Based on accumulated usage data:

| Tier | Criteria | Action |
|------|---------|--------|
| **A — Core** | Average rating ≥ 4, used 5+ times | Maintain, refine, promote |
| **B — Useful** | Average rating ≥ 3, used 3+ times | Keep, improve weak areas |
| **C — Situational** | Average rating ≥ 3, used 1-2 times | Keep, monitor for more use |
| **D — Underperforming** | Average rating < 3 | Revise or archive |
| **U — Untested** | Never used | Test in next relevant situation |

### Step 4: Empirical Analysis — Correlate with Outcomes
When you have 5+ completed projects:

1. **Gather project data:**
   - Project success score (1-5)
   - Which procedures were used
   - How many procedures used
   - Time from start to completion

2. **Calculate correlations:**
   - Does using procedure X correlate with higher project success?
   - Does using MORE procedures correlate with success (or is there diminishing returns)?
   - Do certain COMBINATIONS of procedures predict success?

3. **Statistical thresholds:**
   - Correlation ≥ 0.3: Weak positive relationship (investigate)
   - Correlation ≥ 0.5: Moderate positive relationship (likely useful)
   - Correlation ≥ 0.7: Strong positive relationship (definitely useful)
   - Note: With small samples, these should be interpreted cautiously

### Step 5: Empirical Analysis — Identify Patterns
Look for:

| Pattern | What It Means | Action |
|---------|-------------|--------|
| Procedure X always precedes success | X is likely valuable | Ensure X is used |
| Procedure X sometimes helps, sometimes doesn't | Context-dependent | Identify which contexts |
| Procedure X correlates with FAILURE | X may be misapplied or flawed | Investigate |
| Procedures X+Y together predict success | Synergy | Use them together |
| More procedures ≠ more success | Quality over quantity | Focus on high-value procedures |
| Certain procedures are never used | May be unnecessary | Archive or promote |

### Step 6: Generate Action Items
From the analysis:

```
PROCEDURE EFFECTIVENESS REVIEW:
Period: [date range]
Projects analyzed: [N]
Procedures tracked: [N]

Tier assignments:
A (Core): [list]
B (Useful): [list]
C (Situational): [list]
D (Underperforming): [list]
U (Untested): [list]

Key findings:
1. [finding] — action: [what to do]

Revisions needed:
1. [procedure] — issue: [what's wrong] — fix: [how to improve]

Archive candidates:
1. [procedure] — reason: [why it's not working]

Promotion candidates:
1. [procedure] — reason: [why it deserves more use]
```

## When to Use
- **Operational**: After completing any significant procedure (>15 minutes)
- **Empirical**: After completing 5+ projects with structured data
- Quarterly procedure review
- When deciding to keep/archive procedures
- When procedure effectiveness is disputed
- → INVOKE: /cppd (cross-project pattern detection) for system-level patterns
- → INVOKE: /prr (procedure review) for individual procedure improvement

## Verification
- [ ] Usage logged with consistent format
- [ ] Value ratings assigned honestly (not inflated)
- [ ] Tier assignments based on data (not assumptions)
- [ ] Correlations calculated with appropriate caution about sample size
- [ ] Action items are specific (not just "improve procedure X")
- [ ] Archive/promotion decisions justified
