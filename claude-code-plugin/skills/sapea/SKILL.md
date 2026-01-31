---
name: sapea
description: "Check whether a procedure's questions/steps can be executed without interpretation and whether outputs are checkable."
---

# Procedure Executability Audit

**Input**: $ARGUMENTS

---

## Overview

Check whether a procedure's questions/steps can be executed without interpretation and whether outputs are checkable. A procedure that requires interpretation is not a procedure — it's advice.

## Steps

### Step 1: Identify Procedure Interface
For the target procedure:
1. **Declared inputs**: What does it say it takes?
2. **Declared outputs**: What does it say it produces?
3. **Undeclared inputs**: What does an executor need to know that isn't stated?
4. **Assumed context**: What background knowledge is required?

**Flag:** Any undeclared input or assumed context means the procedure can't be executed "cold."

### Step 2: Check Step Executability
For each step in the procedure:

| Step | Action Specified? | Done Criteria? | Testable? | Guess Required? |
|------|------------------|---------------|-----------|----------------|
| [step] | Y/N | Y/N | Y/N | Y/N |

**Action specified:** Does the step say WHAT to do (not just what to think about)?
**Done criteria:** Does the step say when it's COMPLETE?
**Testable:** Can someone verify the step was done correctly?
**Guess required:** Must the executor guess something to proceed?

### Step 3: Check Output Checkability
For each output the procedure claims to produce:

1. Is the output format specified?
2. Is there a quality criterion?
3. Can someone OTHER than the executor judge if the output is good?
4. Is the output directly usable by the next step/procedure?

### Step 4: Check Stopping Rules
1. Does the procedure state when to stop? (Not "when it feels done")
2. Is the stopping rule mechanical? (Can be evaluated objectively)
3. What happens if you can't meet the stopping rule? (Fallback defined?)
4. Could someone run this forever without realizing they should stop?

### Step 5: Score Executability
| Dimension | Score (1-5) | Evidence |
|-----------|------------|---------|
| Input completeness | | [what's missing] |
| Step clarity | | [which steps are unclear] |
| Output checkability | | [which outputs can't be verified] |
| Stopping rules | | [is there a clear stop point] |
| Interpretation burden | | [how much guessing required] |

Overall executability: [score / 25]
- 20-25: Fully executable by a stranger
- 15-19: Executable with minor interpretation
- 10-14: Requires significant interpretation
- Below 10: Not really a procedure — it's advice

### Step 6: Propose Improvements
For each issue found:

```
IMPROVEMENT:
Location: [which step/section]
Issue: [what's not executable]
Current: [what it says now]
Proposed: [clearer version]
Why better: [how this reduces interpretation]
```

### Step 7: Report
```
EXECUTABILITY AUDIT:
Procedure: [name]
Overall score: [X/25]

Interface:
- Declared inputs: [list]
- Missing inputs: [what's needed but not stated]
- Output format: [specified / unspecified]

Step executability:
| Step | Executable? | Issue |
|------|------------|-------|
| [step] | Y/N | [what's wrong] |

Stopping rule: [clear / unclear / missing]

Top improvements needed:
1. [most impactful fix]
2. [second most impactful]
3. [third]
```

## When to Use
- When a procedure sounds good but is hard to apply
- When different executors produce different outputs
- Before promoting a procedure to "required" or "core"
- → INVOKE: /sadrt (divergence risk test) for testing consistency across executors
- → INVOKE: /pv (procedure validation) for overall procedure quality

## Verification
- [ ] All inputs (declared and undeclared) identified
- [ ] Each step checked for action, done criteria, testability
- [ ] Outputs checked for format and checkability
- [ ] Stopping rules assessed
- [ ] Executability scored honestly
- [ ] Improvements proposed for low-scoring areas
