---
name: fat
description: "When a project fails, systematically analyze the root cause and attribute failure correctly."
---

# Failure Attribution Framework

**Input**: $ARGUMENTS

---

## Overview

When a project fails, systematically analyze the root cause. Current gap: GOSM captures "what worked" but not "why did this fail?" This framework distinguishes controllable vs. uncontrollable factors and identifies what GOSM should improve.

## Steps

### Step 1: Define the Failure
1. What was the goal?
2. What was achieved? (specific, measurable)
3. What is the gap between goal and achievement?
4. When did the failure become apparent?
5. Was it sudden or gradual?

### Step 2: Gather Failure Evidence
Before attribution, collect:
1. Timeline of key events and decisions
2. What was known at each decision point?
3. What alternatives were available at each point?
4. What feedback was received and how was it responded to?
5. What resources were available vs used?

### Step 3: Identify Failure Causes
List ALL contributing causes, then classify:

**Controllable (within your power to change):**
- Poor goal definition (vague, unmeasurable, unrealistic)
- Poor strategy selection (wrong approach for the problem)
- Poor execution (right approach, badly implemented)
- Insufficient resources allocated
- Ignored warning signs
- Skipped procedures / cut corners
- Failed to adapt when conditions changed

**Partially controllable (could influence but not determine):**
- Team dynamics / coordination failures
- Stakeholder misalignment
- Dependency on unreliable partners
- Skill gaps that could have been addressed

**Uncontrollable (external factors):**
- Market changes
- Competitor actions
- Regulatory changes
- Natural events
- Technology shifts
- Bad luck (genuinely random)

### Step 4: Determine Root Cause vs Contributing Factors
For each cause identified:
1. If this cause were removed, would the project have succeeded?
   - YES → root cause candidate
   - NO → contributing factor
2. What caused THIS cause? (go deeper)
3. Keep asking until you reach something actionable

**Common root cause patterns:**
- "We didn't know" → Was the information available? Did we look?
- "We didn't have time" → Was scope realistic? Were priorities right?
- "It didn't work" → Was the approach tested early? Were alternatives explored?
- "They didn't deliver" → Was dependency risk managed? Were alternatives ready?
- "Things changed" → Was the plan robust to change? Were signals monitored?

### Step 5: Assess Attribution Honestly

**Attribution biases to watch for:**
- **Self-serving bias**: Attributing failure to external factors, success to internal skill
- **Fundamental attribution error**: Blaming people's character instead of situations
- **Hindsight bias**: "We should have known" (but did we have the information then?)
- **Single cause fallacy**: Looking for THE cause when failures are usually multi-causal
- **Narrative bias**: Creating a coherent story that may oversimplify

**Honest attribution test:**
- Would a neutral observer agree with your attribution?
- Are you attributing to factors you can't control (convenient) vs ones you can (uncomfortable)?
- If the same conditions repeated, would you fail the same way?

### Step 6: Extract Lessons

For each root cause:
```
LESSON:
Root cause: [what went wrong]
Attribution: [controllable / partially controllable / uncontrollable]
Confidence: [how sure are we this is correct]

If controllable:
  What to do differently: [specific change]
  Which procedure should enforce this: [name]
  Should a gate be added: [yes/no, what gate]

If partially controllable:
  What could reduce risk: [mitigation]
  What early warning would help: [signal to watch]

If uncontrollable:
  How to be more robust: [what would survive this]
  Should this risk be accepted or avoided: [strategy]
```

### Step 7: Report
```
FAILURE ATTRIBUTION:
Project: [name]
Goal: [what was attempted]
Outcome: [what happened]
Gap: [goal vs achievement]

Root causes:
1. [cause] — [controllable/partial/uncontrollable] — confidence: [H/M/L]

Attribution summary:
- Controllable factors: [% of failure]
- Partially controllable: [%]
- Uncontrollable: [%]

Key lessons:
1. [lesson] → [action to take]

System improvements:
- Procedures to update: [list]
- Gates to add: [list]
- Warnings to monitor: [list]
```

## When to Use
- Project failed (achievement < 50%)
- Project partially succeeded but with significant issues
- Retrospective analysis of historical failures
- → INVOKE: /rca (root cause analysis) for deeper causal analysis
- → INVOKE: /aar (after action review) for structured debrief
- → INVOKE: /afa (action failure analysis) for postmortem

## Verification
- [ ] Failure clearly defined (goal vs achievement gap)
- [ ] Evidence gathered before attribution (not jumping to conclusions)
- [ ] Causes classified as controllable / partial / uncontrollable
- [ ] Root causes distinguished from contributing factors
- [ ] Attribution biases checked
- [ ] Lessons are specific and actionable
