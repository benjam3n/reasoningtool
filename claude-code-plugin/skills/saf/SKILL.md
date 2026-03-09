---
name: "saf - Safety Analysis"
description: Systematically identify safety risks, failure modes, and protective measures for any plan, system, or action.
---

# Safety Analysis

**Input**: $ARGUMENTS

---

## Step 1: IDENTIFY WHAT NEEDS TO BE SAFE

Classify the domain:

| Domain | Focus |
|--------|-------|
| **Physical** | Bodily harm, environmental damage |
| **Financial** | Loss of money, assets, livelihood |
| **Psychological** | Mental health, emotional harm, manipulation |
| **Informational** | Data loss, privacy breach, misinformation |
| **Systemic** | Institutional failure, cascading collapse |
| **Reputational** | Trust, credibility, social standing |

State what is at risk and who is at risk.

---

## Step 2: THREAT IDENTIFICATION

For each risk domain identified:

1. **What could go wrong?** (List every failure mode)
2. **How likely is it?** (Rare / Unlikely / Possible / Likely / Near-certain)
3. **How severe if it happens?** (Negligible / Minor / Moderate / Major / Catastrophic)
4. **How detectable is it?** (Obvious / Noticeable / Hidden / Invisible)

```
THREAT MAP:
| Threat | Likelihood | Severity | Detectability | Risk Level |
|--------|-----------|----------|---------------|------------|
|        |           |          |               |            |
```

Risk Level = Likelihood x Severity (adjusted down if highly detectable, up if hidden).

---

## Step 3: EXISTING SAFEGUARDS

What protections already exist?

For each safeguard:
1. What threat does it address?
2. Does it PREVENT, DETECT, or MITIGATE?
3. Has it been tested? When did it last work?
4. What is its failure mode? (How does the safeguard itself fail?)

```
SAFEGUARD AUDIT:
| Safeguard | Addresses | Type | Tested? | Safeguard failure mode |
|-----------|-----------|------|---------|----------------------|
|           |           |      |         |                      |
```

---

## Step 4: GAP ANALYSIS

For each high-risk threat:
- Is there a safeguard? (Y/N)
- Is the safeguard sufficient? (Y/N)
- What is the residual risk after safeguards?

```
SAFETY GAPS:
1. [Threat X] — No safeguard exists. Residual risk: HIGH
2. [Threat Y] — Safeguard exists but untested. Residual risk: MEDIUM
3. [Threat Z] — Safeguard insufficient. Residual risk: MEDIUM
```

---

## Step 5: THE CATASTROPHE CHECK

Separate from probability-weighted analysis, check:

1. **What is the worst thing that could happen?** (Not likely — worst)
2. **Is it survivable?** Can the person/system recover?
3. **Is it reversible?** Can the damage be undone?
4. **Are there single points of failure?** One thing breaks and everything fails?
5. **Is there a kill switch?** Can the process be stopped mid-execution?

If any catastrophic outcome is non-survivable AND non-reversible, this requires extraordinary safeguards regardless of probability.

---

## Step 6: RECOMMENDED SAFEGUARDS

For each gap, recommend:

```
RECOMMENDATIONS:
1. [Gap] -> [Safeguard]
   Type: [PREVENT / DETECT / MITIGATE]
   Cost: [low / medium / high]
   Priority: [must-have / should-have / nice-to-have]

IMPLEMENTATION ORDER:
1. [Highest priority first — catastrophic + no safeguard]
2. [Second priority — high risk + weak safeguard]
3. [Third priority — medium risk improvements]
```

---

## Step 7: SAFETY SUMMARY

```
SAFETY ASSESSMENT:

Subject: [what was analyzed]
Overall safety level: [SAFE / CONDITIONALLY SAFE / UNSAFE / UNKNOWN]

Critical risks: [list any catastrophic risks]
Key gaps: [list unaddressed threats]
Required actions before proceeding: [must-have safeguards]

Safe to proceed if: [conditions]
NOT safe to proceed if: [conditions]
```

---

## Integration

Use with:
- `/fla` -> Detailed failure mode analysis
- `/prm` -> Pre-mortem for plans
- `/eth` -> When safety has ethical dimensions
- `/obv` -> Add obvious safety checks
- `/obo` -> Check for obvious bad outcomes
