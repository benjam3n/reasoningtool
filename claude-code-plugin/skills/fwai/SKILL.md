---
name: "fwai - Future AI Agent Value"
description: Assess value for autonomous AI agents. Identifies tasks suitable for autonomous execution, assesses reliability requirements, evaluates error recovery needs, checks human-in-loop requirements, and projects automation potential.
---

# Future AI Agent Value

**Input**: $ARGUMENTS

---

## Step 1: Identify Tasks for Autonomous Execution

Determine which tasks or components are suitable for AI agent automation.

```
SYSTEM/DOMAIN: [what is being assessed]
CURRENT STATE: [how tasks are performed today]

TASK INVENTORY:
| Task | Current Performer | Repetitive? | Deterministic? | Agent-Suitable? |
|------|------------------|-------------|----------------|-----------------|
| [task 1] | [human/semi-auto/auto] | [Y/N] | [Y/N] | [YES/PARTIAL/NO] |
| [task 2] | [human/semi-auto/auto] | [Y/N] | [Y/N] | [YES/PARTIAL/NO] |
...

HIGHLY SUITABLE (clear agent wins):
1. [task] — Why: [repetitive, well-defined, verifiable output]

PARTIALLY SUITABLE (agent + human hybrid):
1. [task] — Agent does: [portion] — Human does: [portion]

NOT SUITABLE (keep human):
1. [task] — Why: [requires judgment / empathy / physical presence / accountability]
```

---

## Step 2: Assess Reliability Requirements

Evaluate how reliable agent execution needs to be for each task.

```
RELIABILITY REQUIREMENTS:
| Task | Required Accuracy | Failure Consequence | Acceptable Error Rate |
|------|-------------------|--------------------|--------------------|
| [task 1] | [exact / high / moderate] | [description] | [0% / <1% / <5% / <10%] |
| [task 2] | [exact / high / moderate] | [description] | [rate] |

CURRENT AI RELIABILITY ESTIMATE:
| Task | Estimated Accuracy | Meets Requirement? | Gap |
|------|-------------------|-------------------|-----|
| [task 1] | [estimate] | [Y/N] | [description] |
| [task 2] | [estimate] | [Y/N] | [description] |

RELIABILITY BLOCKERS:
- [task]: Can't automate until accuracy reaches [threshold] because [reason]
```

---

## Step 3: Evaluate Error Recovery Needs

Design how agents handle failures and unexpected situations.

```
ERROR SCENARIOS:
1. [error type] — Likelihood: [HIGH/MED/LOW]
   Detection method: [how the agent knows something went wrong]
   Recovery strategy: [retry / fallback / escalate to human / abort]
   Recovery time: [estimate]

2. [error type] — Likelihood: [level]
   Detection method: [method]
   Recovery strategy: [strategy]
   Recovery time: [estimate]

CASCADING FAILURE RISKS:
- [scenario where one agent error triggers larger problems]

GRACEFUL DEGRADATION:
- [how the system should behave when agent capability is exceeded]

UNDO REQUIREMENTS:
- [which agent actions must be reversible?]
```

---

## Step 4: Check Human-in-Loop Requirements

Determine where human oversight is necessary.

```
HUMAN-IN-LOOP ANALYSIS:
| Task/Decision | Human Required? | Why | Frequency |
|--------------|----------------|-----|-----------|
| [item 1] | [ALWAYS / SOMETIMES / NEVER] | [reason] | [how often] |
| [item 2] | [ALWAYS / SOMETIMES / NEVER] | [reason] | [how often] |

MANDATORY HUMAN CHECKPOINTS:
1. [checkpoint] — Before: [what happens next] — Because: [stakes/regulation/ethics]

ADVISORY HUMAN REVIEW (nice to have):
1. [review point] — For: [quality / learning / edge cases]

ESCALATION TRIGGERS (agent should hand off to human when):
1. [trigger condition] — Action: [how to escalate]
2. [trigger condition] — Action: [how to escalate]

APPROVAL WORKFLOWS:
- [which agent outputs need human approval before taking effect?]
```

---

## Step 5: Project Automation Potential

Estimate the trajectory and timeline for autonomous execution.

```
AUTOMATION POTENTIAL:

NEAR-TERM (current capabilities):
| Task | Automatable Now? | Confidence | Prerequisites |
|------|-----------------|------------|---------------|
| [task 1] | [Y/N/PARTIAL] | [level] | [what's needed] |
| [task 2] | [Y/N/PARTIAL] | [level] | [what's needed] |

MEDIUM-TERM (1-3 years):
- [task]: Likely automatable when [capability improvement]

LONG-TERM (3+ years):
- [task]: Requires [breakthrough in X]

AUTOMATION ROADMAP:
Phase 1: [what to automate first] — Value: [benefit] — Risk: [level]
Phase 2: [next wave] — Value: [benefit] — Depends on: [Phase 1 success]
Phase 3: [future wave] — Value: [benefit] — Depends on: [capability advances]
```

---

## Step 6: Value Assessment

```
AI AGENT VALUE SUMMARY:

TOTAL TASKS ASSESSED: [N]
AUTOMATABLE NOW: [N] ([%])
AUTOMATABLE WITH GUARDRAILS: [N] ([%])
REQUIRES HUMAN: [N] ([%])

HIGHEST-VALUE AUTOMATION TARGET:
[task] — Saves: [time/cost] — Risk: [level] — Recommend: [Y/N]

ROI ESTIMATE:
- Automation cost: [estimate]
- Ongoing savings: [estimate per period]
- Break-even: [timeline]

RISKS OF AUTOMATION:
1. [risk] — Mitigation: [approach]
2. [risk] — Mitigation: [approach]

RISKS OF NOT AUTOMATING:
1. [risk] — Impact: [description]

RECOMMENDATION:
[Automate / Partially automate / Wait / Don't automate]
Rationale: [summary reasoning]
Start with: [specific first step]
```

---

## Integration

Use with:
- `/llmf` -> Assess LLM feasibility for specific agent tasks
- `/roip` -> Optimize which tasks to automate for best ROI
- `/exint` -> Design agent integration with existing systems
