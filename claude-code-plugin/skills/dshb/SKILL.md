---
name: "dshb - Dashboard Design"
description: Design an information dashboard by identifying the audience, the decisions it supports, the right metrics, and the layout for quick scanning.
output:
  format: "prose"
---

# Dashboard Design

**Input**: $ARGUMENTS

---

## Step 1: Identify the Audience

Different people need different views. Design for a specific user.

```
PRIMARY AUDIENCE: [who will look at this dashboard most often]
ROLE: [their job function]
FREQUENCY OF USE: [real-time / daily / weekly / monthly]
CONTEXT OF USE: [morning standup / executive review / operations monitoring / self-service]

SECONDARY AUDIENCES:
- [audience] — Different needs: [what they need that the primary doesn't]

SKILL LEVEL: [expert with data / comfortable / needs hand-holding]
```

---

## Step 2: Identify Decisions the Dashboard Supports

A dashboard that doesn't drive action is decoration.

```
DECISIONS THIS DASHBOARD MUST SUPPORT:
1. [decision] — Triggered when: [condition]
   Action taken: [what the viewer does in response]
2. [decision] — Triggered when: [condition]
   Action taken: [what the viewer does in response]
3. [decision] — Triggered when: [condition]
   Action taken: [what the viewer does in response]

QUESTIONS THE VIEWER ASKS:
- [question 1 — e.g., "Are we on track?"]
- [question 2 — e.g., "Where should I focus?"]
- [question 3 — e.g., "What changed?"]

ANTI-GOAL: This dashboard should NOT try to answer: [out-of-scope questions]
```

---

## Step 3: Select Metrics

Choose a balanced set of leading and lagging indicators.

```
METRICS:

LAGGING INDICATORS (outcomes — what already happened):
1. [metric] — Definition: [exactly how it's calculated]
   Why it matters: [what it tells you]
2. [metric] — Definition: [exactly how it's calculated]
   Why it matters: [what it tells you]

LEADING INDICATORS (predictors — what's about to happen):
1. [metric] — Definition: [exactly how it's calculated]
   Predicts: [which lagging indicator it leads]
2. [metric] — Definition: [exactly how it's calculated]
   Predicts: [which lagging indicator it leads]

HEALTH METRICS (guardrails — things that shouldn't break):
1. [metric] — Acceptable range: [min-max]

EXCLUDED METRICS (considered but rejected):
- [metric] — Reason: [vanity metric / not actionable / too noisy / etc.]

TOTAL METRICS ON DASHBOARD: [number — flag if > 10]
```

---

## Step 4: Design Layout for Quick Scanning

Optimize for the "5-second test" — can someone understand status in 5 seconds?

```
LAYOUT:

TOP ROW (glanceable status):
[2-4 big numbers or status indicators — the most critical KPIs]

MIDDLE (trends and context):
[Time-series charts showing trajectory — are things getting better or worse?]

BOTTOM (detail and drill-down):
[Tables or breakdowns for investigation when something looks off]

VISUAL HIERARCHY:
1. [most important element] — Position: [top-left / center]
2. [second most important] — Position: [position]
3. [supporting detail] — Position: [position]

CHART TYPES:
- [metric]: [line / bar / gauge / sparkline / table / heatmap] — Reason: [why this type]

COMPARISON CONTEXT:
- Show vs. [previous period / target / benchmark / peer group]
```

---

## Step 5: Define Thresholds and Alerts

Make the dashboard self-interpreting. Color and alerts should carry meaning.

```
THRESHOLDS:

| Metric | Green (good) | Yellow (watch) | Red (act now) |
|--------|-------------|---------------|--------------|
| [metric 1] | [range] | [range] | [range] |
| [metric 2] | [range] | [range] | [range] |

ALERTS (push notifications, not just color):
- When [condition]: notify [who] via [channel]
- When [condition]: notify [who] via [channel]

ANOMALY DETECTION:
- Flag when [metric] deviates more than [X standard deviations / X%] from [baseline]
```

---

## Step 6: Plan Data Sources and Refresh Cadence

The best-designed dashboard fails if the data is stale or broken.

```
DATA SOURCES:
| Metric | Source System | Update Frequency | Owner |
|--------|-------------|-----------------|-------|
| [metric 1] | [system/database] | [real-time/hourly/daily] | [who maintains] |
| [metric 2] | [system/database] | [real-time/hourly/daily] | [who maintains] |

REFRESH CADENCE: [how often the dashboard updates]
DATA LATENCY: [how old is the data when it appears — be honest]

DATA QUALITY RISKS:
- [risk — e.g., manual data entry, incomplete records]
  Mitigation: [how to handle]

MAINTENANCE PLAN:
- Review dashboard relevance: [quarterly / when strategy changes]
- Data source health check: [monthly]
```

---

## Integration

Use with:
- `/mets` -> Choose the right metrics before designing the dashboard
- `/abts` -> Design experiment dashboards with proper statistical context
- `/rgc` -> Build compliance monitoring dashboards
