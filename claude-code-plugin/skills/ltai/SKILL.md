---
name: "ltai - Long-Term AI Orchestration"
description: Plan for AI-agent coordination and autonomous operation. Design handoff protocols, error recovery, and human oversight.
output:
  format: "prose"
---

# Long-Term AI Orchestration

**Input**: $ARGUMENTS

---

## Step 1: Identify Tasks Suitable for Agents

Audit the work described in the input and classify tasks by automation suitability.

```
AGENT SUITABILITY MAP:
FULLY AUTOMATABLE (agent can do end-to-end):
- [Task]: [Why it's suitable — deterministic, well-defined, low-stakes]

AGENT-ASSISTED (agent does most, human reviews):
- [Task]: [What the agent does vs. what the human checks]

HUMAN-LED, AGENT-SUPPORTED (human drives, agent helps):
- [Task]: [What support the agent provides]

HUMAN-ONLY (do not automate):
- [Task]: [Why — judgment, stakes, ambiguity, relationships]
```

Rules:
- Tasks with clear inputs, clear outputs, and verifiable results are most suitable
- Tasks requiring taste, political judgment, or novel reasoning stay human-led
- "Fully automatable" does not mean "no oversight" — it means the agent can execute without mid-task human input
- Be conservative — overestimating AI capability is the most common error

---

## Step 2: Design Agent Handoff Protocols

For each automatable or agent-assisted task, define how work flows between agents and humans.

```
HANDOFF PROTOCOLS:
1. [Task/workflow name]:
   - Trigger: [What initiates the agent]
   - Input format: [What the agent receives]
   - Processing: [What the agent does, step by step]
   - Output format: [What the agent produces]
   - Handoff point: [When/how it returns to human or next agent]
   - Quality gate: [How to verify the output before accepting]

2. [Task/workflow name]:
   ...
```

Rules:
- Every agent task needs a defined trigger and a defined endpoint
- Output format must be specified — agents that produce unstructured output create downstream chaos
- Quality gates are mandatory, not optional
- If two agents hand off to each other, specify the interface contract between them

---

## Step 3: Plan for Error Recovery

Define what happens when agents fail, produce bad output, or encounter edge cases.

```
ERROR RECOVERY PLAN:
1. [Failure mode]: [What goes wrong]
   - Detection: [How you know it failed]
   - Automatic recovery: [What the agent tries first]
   - Escalation trigger: [When it stops trying and alerts a human]
   - Rollback procedure: [How to undo damage if any]
   - Prevention: [How to reduce this failure's frequency]

2. [Failure mode]:
   ...
```

Rules:
- Assume agents WILL fail — the question is how gracefully
- Silent failures are worse than loud failures — detection is the first priority
- Automatic recovery should have a retry limit — infinite loops are a real risk
- Every escalation must have a clear human recipient, not just "someone"

---

## Step 4: Design Human Oversight

Define the oversight structure that keeps humans informed and in control.

```
OVERSIGHT STRUCTURE:
- Monitoring dashboard: [What metrics/status to display]
- Review cadence: [How often humans review agent output — daily/weekly/per-batch]
- Kill switches: [How to stop agents immediately if needed]
- Audit trail: [What gets logged and where]
- Authority levels: [Who can start, stop, modify, or override agents]
```

Rules:
- Oversight must be proportional to stakes — high-stakes tasks need more frequent review
- Kill switches must work immediately, not "after the current batch"
- Audit trails are non-negotiable — you must be able to reconstruct what happened and why
- Avoid "oversight theater" — dashboards nobody looks at don't count

---

## Step 5: Project Capability Evolution

Forecast how agent capabilities will change and plan accordingly.

```
CAPABILITY EVOLUTION:
SHORT-TERM (next 6 months):
- Agents can likely handle: [tasks moving from human-led to agent-assisted]
- Key enabler: [what makes this possible]

MEDIUM-TERM (6-18 months):
- Agents can likely handle: [tasks moving from agent-assisted to fully automated]
- Key enabler: [what makes this possible]

LONG-TERM (18+ months):
- Speculative capabilities: [what might become possible]
- Preparation needed now: [what to build/design now to be ready]

ASSUMPTIONS TO MONITOR:
- [Assumption about AI progress]: [How to tell if it's wrong]
```

Rules:
- Short-term forecasts should be conservative and based on current trajectory
- Long-term forecasts should acknowledge high uncertainty
- "Preparation needed now" is the actionable output — what architectures, data, or processes to build today
- Monitor assumptions actively — revise the plan when assumptions break

---

## Integration

Use with:
- `/hpat` -> Use historical patterns to calibrate AI capability forecasts
- `/de` -> Turn the orchestration plan into a structured delivery
- `/mtnw` -> Identify new domains where AI agents create the most leverage
- `/immg` -> Find immediate gaps in current agent infrastructure
