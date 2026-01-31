---
name: sarus
description: "Repo-wide scan to find question patterns that commonly require interpretation before answering."
---

# Repo Unclarity Scan

**Input**: $ARGUMENTS

---

## Overview

Repo-wide scan to find question patterns that commonly require interpretation before answering. This is the broad survey that identifies where to focus detailed rewrite work.

## Steps

### Step 1: Scan for Unclarity Patterns
Search across all target files for these patterns:

| Pattern | Regex/Signal | Why Problematic |
|---------|-------------|----------------|
| Parenthetical additions | `(...)` in questions | Bundles extra checks invisibly |
| If-yes/if-no branching | "if yes", "if no" | Hides conditional logic in text |
| Compound "or" questions | "X or Y?" | Unclear if asking for choice or checking either |
| Multi-sentence questions | Two+ sentences ending in ? | Usually bundled questions |
| Undefined term hotspots | Same noun used 5+ times without definition | Everyone reads it differently |
| "If applicable" | Phrases like "where relevant" | Who decides applicability? |
| Subjective adjectives | "appropriate", "adequate", "good" | No shared standard |
| Implicit quantifiers | "The requirements", "all steps" | Which ones specifically? |

### Step 2: Catalog Findings
For each finding:

```
FINDING:
File: [path]
Line: [number]
Pattern: [which pattern matched]
Text: [the problematic text]
Severity: [H/M/L — based on how central the file is]
```

### Step 3: Prioritize by Centrality and Impact
Not all findings are equally important. Prioritize:

| Priority Tier | Criterion |
|--------------|-----------|
| **P1 — Critical** | Core gates (affect every project) |
| **P2 — High** | Procedures referenced by gates |
| **P3 — Medium** | Frequently used procedures |
| **P4 — Low** | Rarely used or peripheral procedures |

### Step 4: Group by Pattern
Aggregate findings to see which patterns are most prevalent:

| Pattern | Count | Files Affected | Priority Distribution |
|---------|-------|---------------|---------------------|
| [pattern] | [N] | [N files] | P1: [N], P2: [N], P3: [N] |

This reveals systemic issues vs one-off problems.

### Step 5: Generate Rewrite Queue
Order fixes by impact:
1. P1 findings with most common patterns first (highest impact per fix)
2. P2 findings next
3. Batch similar patterns together (fix all parenthetical bundles at once)

```
REWRITE QUEUE:
| # | File | Line | Pattern | Priority | Estimated Fix |
|---|------|------|---------|----------|--------------|
| 1 | [path] | [line] | [pattern] | P1 | [brief fix description] |
| 2 | ... | | | | |
```

### Step 6: Report
```
REPO UNCLARITY SCAN:
Files scanned: [N]
Lines scanned: [N]
Findings: [N total]

By pattern:
| Pattern | Count | Most Affected Files |
|---------|-------|-------------------|
| [pattern] | [N] | [top 3 files] |

By priority:
P1 (critical): [N]
P2 (high): [N]
P3 (medium): [N]
P4 (low): [N]

Systemic issues: [patterns appearing in 10+ files]
Top rewrite targets: [files with most P1/P2 findings]

Rewrite queue: [N items, starting with highest impact]
```

## When to Use
- When doing large-scale quality improvements
- When standardizing question style across gates/procedures
- When searching for the highest-leverage rewrite targets
- → INVOKE: /saqrc (question rewrite chains) for fixing found issues
- → INVOKE: /saadag (detectors and generators) for detailed analysis of specific files

## Verification
- [ ] All target files scanned
- [ ] Multiple pattern types checked (not just one)
- [ ] Findings prioritized by centrality
- [ ] Patterns aggregated to identify systemic issues
- [ ] Rewrite queue ordered by impact
