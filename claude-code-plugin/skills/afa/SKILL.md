---
name: afa
description: "A premortem imagines failure has already occurred, then works backward to identify what went wrong."
---

# Anticipated Failures Analysis (Premortem)

**Input**: $ARGUMENTS

---

## Overview

A postmortem examines why something failed after the fact. An anticipated failures analysis (premortem) imagines that failure has already occurred, then works backward to identify what went wrong.

Research shows that prospective hindsight — imagining an event has already occurred — increases ability to identify reasons for outcomes by 30% (Mitchell, Russo, Pennington, 1989).

Key insight: It's psychologically easier to explain a past failure than to predict a future one. The premortem exploits this by treating the future as if it were the past.

## Steps

### Step 1: Set Up the Premortem
1. What is the project, plan, or decision being analyzed?
2. What does success look like? (Define so failure is clear)
3. Set the time frame: "It is [date]. This project has FAILED."

**Critical framing:** Don't say "might fail." Say "HAS failed." The certainty is what unlocks the reasoning.

### Step 2: Imagine Total Failure
"The project has failed spectacularly. It's not just a little off — it's a disaster."

Each participant (or each analytical pass) independently generates:
1. What went wrong? (Be specific — not "things went badly" but "the API couldn't handle load")
2. What was the first sign of trouble? (When should we have noticed?)
3. What did we ignore or underestimate?
4. What surprised us?

Generate at least 10 failure reasons before evaluating any.

### Step 3: Categorize Failure Modes

| Category | Failure | Likelihood | Severity | Detectable? |
|----------|---------|-----------|----------|------------|
| **Planning** | Goals were wrong/unclear | | | |
| **Planning** | Timeline was unrealistic | | | |
| **Planning** | Resources were insufficient | | | |
| **Execution** | Key person left/unavailable | | | |
| **Execution** | Quality was worse than expected | | | |
| **Execution** | Integration between parts failed | | | |
| **External** | Market/conditions changed | | | |
| **External** | Competitor moved first | | | |
| **External** | Dependency failed | | | |
| **Human** | Team conflict/misalignment | | | |
| **Human** | Decision-maker changed mind | | | |
| **Human** | Burnout/motivation collapse | | | |
| **Technical** | Approach didn't work as expected | | | |
| **Technical** | Scaling problems emerged | | | |
| [Custom] | [specific to this project] | | | |

### Step 4: Prioritize by Risk
For each failure mode, score:
- **Likelihood**: 1 (unlikely) to 5 (almost certain)
- **Severity**: 1 (minor setback) to 5 (project-killing)
- **Detectability**: 1 (obvious early) to 5 (hidden until too late)

Risk score = Likelihood × Severity × Detectability

Focus on the top 5 risks.

### Step 5: Design Preventions and Mitigations
For each top risk:

```
RISK: [failure mode]
Score: [L × S × D = total]

Prevention (reduce likelihood):
- [action to prevent this from happening]

Early detection (reduce detectability):
- [signal that would warn us early]
- [check/gate that would catch this]

Mitigation (reduce severity):
- [action to limit damage if it happens]
- [backup plan / fallback]

Owner: [who is responsible for watching this]
Review: [when to check if prevention is working]
```

### Step 6: Integrate into Plan
1. Add preventions as tasks in the project plan
2. Add early detection signals to monitoring
3. Add mitigation plans as contingencies
4. Assign owners to each risk
5. Schedule risk reviews

### Step 7: Report
```
PREMORTEM ANALYSIS:
Project: [name]
Imagined failure date: [when]

Top failure modes:
| # | Failure | L | S | D | Risk Score |
|---|---------|---|---|---|-----------|
| 1 | [failure] | [1-5] | [1-5] | [1-5] | [score] |

Preventions:
1. [action] — prevents: [which risk] — owner: [who]

Early warning signals:
1. [signal] — indicates: [which risk] — check: [when]

Mitigations:
1. [backup plan] — for: [which risk]

Biggest blind spot discovered: [what the premortem revealed that wasn't obvious before]
```

## When to Use
- Before committing to a major decision
- At project kickoff
- Before launching a new initiative
- When confidence seems too high
- When the team isn't voicing concerns
- → INVOKE: /prm (pre-mortem) for Gary Klein's original method
- → INVOKE: /fla (failure analysis) for systematic failure identification
- → INVOKE: /fat (failure attribution) for post-failure analysis

## Verification
- [ ] Failure imagined as CERTAIN (not "might fail")
- [ ] At least 10 failure modes generated before evaluation
- [ ] Failures categorized (planning, execution, external, human, technical)
- [ ] Risks scored on likelihood, severity, AND detectability
- [ ] Top risks have prevention AND mitigation plans
- [ ] Owners assigned for each risk
