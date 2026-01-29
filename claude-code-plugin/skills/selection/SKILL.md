---
name: selection
description: "Make the final selection from ranked options after all analysis is complete. Includes LLM-compatible feasibility assessment."
context: fork
---

# Selection

**Input**: $ARGUMENTS

---

## Overview

Make the final selection from ranked options after all analysis is complete. This procedure transforms human-context filters into LLM-verifiable assessments.

---

## Step 0: Context Assessment

| Factor | Value | Notes |
|--------|-------|-------|
| Selection mode | SINGLE / MULTIPLE / CONDITIONAL | |
| Decision reversibility | EASY / HARD / IMPOSSIBLE | |
| Time pressure | URGENT / NORMAL / FLEXIBLE | |

**If URGENT**: Steps 1, 4, 5 only (skip extensive feasibility)
**If IMPOSSIBLE reversibility**: Include Step 6 (extended rationale)

---

## Step 1: Review Rankings and Context

Examine the input from comparison/optimization.

**What to examine**:
1. Top-ranked option and why
2. How close are top options in score?
3. Key differentiating factors
4. Any red flags in the analysis?

**LLM Execution**:
```
From input/prior analysis, extract:
- Top 3 options with scores
- Score gaps between them
- Primary differentiators
- Any noted uncertainties
```

**Output format**:
```
RANKINGS REVIEW
===============
#1: [option] (score: [X])
#2: [option] (score: [Y]) - gap: [X-Y]
#3: [option] (score: [Z]) - gap: [X-Z]

Close race: [YES if gap < 10% / NO]
Key differentiators: [list]
Red flags: [list or "none"]
```

---

## Step 2: Feasibility Assessment

Check top options against practical considerations.

**LLM Feasibility Assessment Protocol**:

For each top candidate (usually top 3), assess using available information:

### 2.1: Resource Requirements
| Question | LLM Assessment Method | Result |
|----------|----------------------|--------|
| Does this require skills/capabilities? | Search input for skill keywords (expertise, experience, training, certification) | List required skills OR "None explicitly mentioned" |
| Does this require specific resources? | Search for resource mentions (money, tools, equipment, people, time) | List resources with amounts if stated |
| Does this have time requirements? | Search for temporal indicators (deadline, by, within, before, urgent) | Note timeline OR "No deadline specified" |

**LLM Execution**:
```
For resource assessment:
1. Scan option description for: cost, price, budget, hours, days, team, equipment
2. Scan context for: available budget, current skills, timeline mentioned
3. Compare: requirements vs. stated availability
4. Flag gaps: What's required but not confirmed available?
```

### 2.2: Risk Profile
| Question | LLM Assessment Method | Result |
|----------|----------------------|--------|
| What could go wrong? | Generate 3-5 failure modes based on option type | List with likelihood (HIGH/MED/LOW) |
| Is failure recoverable? | Check for: one-way decisions, sunk costs, reputation effects | REVERSIBLE / HARD TO REVERSE / IRREVERSIBLE |
| What's the downside magnitude? | Assess: financial loss, time lost, opportunity cost, relationship damage | LOW / MEDIUM / HIGH / CATASTROPHIC |

**LLM Execution**:
```
Risk assessment pattern:
1. Identify option category (financial, career, relationship, technical)
2. Apply domain-typical failure modes:
   - Financial: loss, fraud, market change
   - Career: mismatch, burnout, opportunity cost
   - Relationship: conflict, loss, misunderstanding
   - Technical: failure, delay, scope creep
3. Rate each failure mode: P(occurs) × Impact
```

### 2.3: Stakeholder Considerations
| Question | LLM Assessment Method | Result |
|----------|----------------------|--------|
| Who else is affected? | Extract named parties + infer standard stakeholders for option type | List with roles |
| What concerns might they have? | Map stakeholder interests to option impacts | List concerns per stakeholder |
| Are there approval requirements? | Check for: manager, partner, board, regulatory mentions | List approvers OR "None apparent" |

**LLM Execution**:
```
Stakeholder assessment:
1. Explicit stakeholders: names mentioned in input
2. Implicit stakeholders (by option type):
   - Career: employer, family, colleagues
   - Financial: partners, dependents, creditors
   - Technical: users, team, downstream systems
3. For each: What do they want? How does this option affect that?
```

### 2.4: Timing Considerations
| Question | LLM Assessment Method | Result |
|----------|----------------------|--------|
| Are there prerequisites? | Check for dependencies, sequences, requirements | List with status (met/unmet/unknown) |
| Are there timing constraints? | Search for: deadline, window, expire, before, by | List with dates/timeframes |
| Is this the right time? | Compare urgency signals vs readiness signals | NOW / SOON / LATER / FLEXIBLE |

**Timing Assessment Logic**:
```
NOW indicators: urgent, critical, deadline imminent, opportunity expiring
SOON indicators: approaching deadline, dependencies resolving, building pressure
LATER indicators: not ready, prerequisites unmet, other priorities higher
FLEXIBLE indicators: no deadline, reversible, low stakes
```

**Output format**:
```
FEASIBILITY ASSESSMENT: [Option Name]
=====================================
Resource requirements:
- Skills: [required / assumed / USER_VERIFY]
- Resources: [required / assumed / USER_VERIFY]
- Time: [required / assumed / USER_VERIFY]

Risk profile:
- Potential failures: [list]
- Reversibility: [REVERSIBLE / HARD / IRREVERSIBLE]
- Downside: [LOW / MED / HIGH / CATASTROPHIC]

Stakeholders:
- Affected: [list]
- Concerns: [list]
- Approvals: [list or USER_VERIFY]

Timing:
- Prerequisites: [list]
- Constraints: [list]
- Readiness: [NOW / SOON / LATER]

FEASIBILITY VERDICT: [PROCEED / CAUTION / BLOCKED / USER_VERIFY]
Blockers: [list if any]
```

---

## Step 3: Consider Selection Mode

Based on context, determine selection approach.

**Selection modes**:

| Mode | When to use | Output |
|------|-------------|--------|
| SINGLE | Clear winner, commitment needed | One option + backup |
| MULTIPLE | Options are complementary, resources allow | Set of options |
| CONDITIONAL | High uncertainty, staged approach | Primary + fallbacks with triggers |

**Decision logic**:
```
If top options very close (gap < 10%) AND compatible:
  → Consider MULTIPLE (portfolio approach)

If high uncertainty about key factors:
  → Consider CONDITIONAL (with clear triggers)

If clear winner AND commitment appropriate:
  → SINGLE
```

**Output format**:
```
SELECTION MODE
==============
Mode: [SINGLE / MULTIPLE / CONDITIONAL]
Rationale: [why this mode]
```

---

## Step 4: Make the Selection

Execute the selection based on mode.

### For SINGLE mode:
```
SELECTION: [option name]
========================
Primary: [option]
Backup: [second option]

Why primary over backup: [key differentiators]
```

### For MULTIPLE mode:
```
SELECTION: Portfolio Approach
=============================
Options selected: [list in priority order]
- #1: [option] - primary focus
- #2: [option] - secondary
- ...

Resource allocation: [how to divide effort]
```

### For CONDITIONAL mode:
```
SELECTION: Conditional Approach
===============================
Primary: [option]

Fallback 1: [option]
  Trigger: [what would cause switch]

Fallback 2: [option]
  Trigger: [what would cause switch]

Decision points: [when to evaluate]
```

**IMPORTANT**: If top-ranked option is NOT selected, document why:
```
NOTE: Top-ranked [option] not selected because: [reason]
- Feasibility concern: [specific issue]
- Risk concern: [specific issue]
```

---

## Step 5: Document Rationale

Create clear documentation of the decision.

**Documentation elements**:
1. What was selected and why
2. What alternatives were considered
3. Why alternatives were not chosen
4. Key assumptions underlying the choice
5. What would make us reconsider

**Output format**:
```
DECISION RATIONALE
==================
Selected: [option(s)]

Why selected:
- [reason 1]
- [reason 2]

Alternatives considered:
- [option]: Not selected because [reason]
- [option]: Not selected because [reason]

Key assumptions:
- [assumption 1]: If wrong, would [impact]
- [assumption 2]: If wrong, would [impact]

Reconsider if:
- [condition 1]
- [condition 2]
```

---

## Step 6: Define Success Criteria and Reversal Triggers

Establish what happens after selection.

### Success Criteria
How to know the selection was good:
```
SUCCESS CRITERIA
================
Short-term (by [date]):
- [ ] [measurable indicator]
- [ ] [measurable indicator]

Medium-term (by [date]):
- [ ] [measurable indicator]

Validation complete when: [condition]
```

### Reversal Triggers
What conditions would cause a switch:
```
REVERSAL TRIGGERS
=================
Switch to backup if:
- [ ] [condition] occurs
- [ ] [metric] drops below [threshold]
- [ ] [event] happens

Point of no return: [when commitment becomes irreversible]
Commitment duration: [how long before reconsidering]
```

### Implementation Notes
What implementer needs to know:
```
IMPLEMENTATION NOTES
====================
Critical first steps:
1. [step]
2. [step]

Dependencies:
- [dependency]

Risks to monitor:
- [risk]
```

---

## When to Use

- After comparison has produced ranked options
- Making final commitment to course of action
- Strategy selection after analysis complete
- Multiple stakeholders need alignment
- Before resource allocation
- Decision needs documentation

---

## Verification Criteria

| Step | Verification |
|------|--------------|
| Step 1 | Rankings reviewed with gaps noted |
| Step 2 | Feasibility assessed for top options |
| Step 3 | Selection mode justified |
| Step 4 | Selection made with backup (if SINGLE) |
| Step 5 | Rationale documented |
| Step 6 | Success criteria and reversal triggers defined |

**Overall verification**:
- [ ] Selection is from ranked options (not invented)
- [ ] Feasibility assessment completed (not just rank accepted)
- [ ] Rationale documented and understandable
- [ ] Backup identified (unless single option scenario)
- [ ] Reversal triggers defined
- [ ] USER_VERIFY items flagged for user

---

## Integration Points

- **Often invoked from**: /comparison (after ranking), /multi_criteria_decision, /procedure_engine
- **Routes to**: /steps_generation (to plan execution), /project_initiation (for larger initiatives)
- **Related**: /comparison, /risk_assessment, /criteria_weighting
