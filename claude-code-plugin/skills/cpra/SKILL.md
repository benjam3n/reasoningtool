---
name: cpra
description: "Meta-procedure for ensuring any analysis, procedure, or decision covers all relevant aspects."
---

# Comprehensive Aspects

**Input**: $ARGUMENTS

---

## Overview

Meta-procedure for ensuring any analysis, procedure, or decision covers all relevant aspects without blind spots.

Apply this AFTER creating any procedure/analysis to verify completeness. Apply this DURING analysis to ensure you're not missing angles.

Core principle: Incomplete analysis leads to incomplete solutions. The aspects you don't consider are the ones that bite you. But: not every aspect is relevant to every situation. Comprehensive doesn't mean exhaustive — it means "no blind spots."

## Steps

### Step 1: Identify What's Being Checked
1. What analysis, procedure, or decision is being evaluated for completeness?
2. What is its purpose?
3. Who are the stakeholders?
4. What are the consequences of missing something?

### Step 2: Apply Universal Aspect Checklist
Check the subject against each category. For each, ask: "Has this been considered?"

**Temporal aspects:**
- [ ] Short-term effects (days-weeks)
- [ ] Medium-term effects (months)
- [ ] Long-term effects (years)
- [ ] Timing and sequencing
- [ ] Deadlines and time pressure
- [ ] Historical context (what happened before)

**Stakeholder aspects:**
- [ ] Direct users/beneficiaries
- [ ] Indirect affected parties
- [ ] Opponents/competitors
- [ ] Regulators/authorities
- [ ] Future stakeholders (who doesn't exist yet but will be affected)

**Resource aspects:**
- [ ] Financial cost
- [ ] Time cost
- [ ] Attention/cognitive cost
- [ ] Opportunity cost (what you CAN'T do if you do this)
- [ ] Maintenance/ongoing cost
- [ ] Hidden costs

**Risk aspects:**
- [ ] What could go wrong?
- [ ] How likely is each failure mode?
- [ ] How severe is each failure mode?
- [ ] What's the worst case?
- [ ] What's the recovery path from failure?
- [ ] What's the cost of inaction?

**Systemic aspects:**
- [ ] First-order effects (direct)
- [ ] Second-order effects (effects of effects)
- [ ] Feedback loops (does the output affect the input?)
- [ ] Unintended consequences
- [ ] Interaction with existing systems
- [ ] Precedent effects (what does this enable/prevent in the future?)

**Epistemological aspects:**
- [ ] What do we know for certain?
- [ ] What are we assuming?
- [ ] What don't we know?
- [ ] What can't we know? (genuine uncertainty)
- [ ] How confident should we be?
- [ ] What would change our mind?

**Ethical/value aspects:**
- [ ] Is this fair to all parties?
- [ ] Are there equity implications?
- [ ] Does this align with stated values?
- [ ] Is there a conflict of interest?
- [ ] Would this survive public scrutiny?

### Step 3: Identify Gaps
From the checklist:

| Category | Aspect Missing | Severity | How to Address |
|----------|---------------|----------|---------------|
| [category] | [what was overlooked] | Critical/Major/Minor | [what to do] |

**Severity guide:**
- Critical: Missing this could cause failure or serious harm
- Major: Missing this significantly weakens the analysis
- Minor: Would be nice to include but not essential

### Step 4: Domain-Specific Aspects
Beyond the universal checklist, every domain has specific aspects. Ask:
1. What would a domain expert check that a generalist would miss?
2. What are the "known unknowns" in this domain?
3. What aspects are specific to this context?

### Step 5: Diminishing Returns Check
Comprehensiveness has costs:
1. Is additional analysis likely to change the conclusion?
2. Is the cost of more analysis justified by the decision stakes?
3. Are we pursuing completeness for its own sake vs for decision quality?

**Rule:** Stop adding aspects when the marginal insight is less than the marginal cost of analysis.

### Step 6: Report
```
COMPREHENSIVE ASPECTS CHECK:
Subject: [what was evaluated]
Purpose: [what the subject is trying to accomplish]

Coverage summary:
| Category | Covered | Gaps | Severity |
|----------|---------|------|----------|
| Temporal | [Y/Partial/N] | [gaps] | [severity] |
| Stakeholder | [Y/Partial/N] | [gaps] | [severity] |
| Resource | [Y/Partial/N] | [gaps] | [severity] |
| Risk | [Y/Partial/N] | [gaps] | [severity] |
| Systemic | [Y/Partial/N] | [gaps] | [severity] |
| Epistemological | [Y/Partial/N] | [gaps] | [severity] |
| Ethical | [Y/Partial/N] | [gaps] | [severity] |
| Domain-specific | [Y/Partial/N] | [gaps] | [severity] |

Critical gaps: [list]
Recommended additions: [what to add to address gaps]
Completeness assessment: [comprehensive / mostly complete / significant gaps]
```

## When to Use
- After creating any analysis or procedure
- During analysis when you want to check coverage
- When stakes are high and missing something is costly
- → INVOKE: /pv (procedure validation) for procedure-specific completeness
- → INVOKE: /mv (MECE validation) for structural completeness

## Verification
- [ ] All 7 universal aspect categories checked
- [ ] Domain-specific aspects identified
- [ ] Gaps cataloged with severity
- [ ] Diminishing returns assessed (not over-analyzing)
- [ ] Critical gaps addressed before proceeding
