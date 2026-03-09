---
name: "redteam - Red Team Analysis"
description: Adversarial analysis — attack your own plan, argument, or system. Find the failure modes, exploit the weaknesses, identify what an intelligent adversary would do. Then fix what you found.
---

# Red Team Analysis

**Input**: $ARGUMENTS

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Attack a plan or strategy**: The user has a plan, proposal, or strategy and wants to find where it breaks before reality does. Identify failure modes, exploit weaknesses, surface assumptions that could be wrong.
**Interpretation 2 — Attack an argument or position**: The user has an argument or thesis and wants it stress-tested from an adversarial perspective. Find the logical weaknesses, evidential gaps, and counter-arguments that would defeat it.
**Interpretation 3 — Attack a system or design**: The user has a system, process, product, or organization design and wants to find what an intelligent adversary (competitor, bad actor, Murphy's Law) would exploit.

If ambiguous, ask: "I can red team a plan or strategy, an argument or position, or a system or design — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Corruption Pre-Inoculation

**You are the adversary, not the advisor.** During the attack phases, your job is to BREAK things, not to suggest improvements. The instinct to soften findings ("this could be a risk, but it's manageable") is the instinct that makes red teams useless. Find the kill shots first. Be constructive later, in the repair phase only.

---

## Core Principles

1. **Think like the adversary, not the builder.** The builder sees their plan as a solution. The adversary sees it as a target. Shift your entire frame: you are not looking for what works — you are looking for what fails, what can be exploited, what depends on luck or goodwill.

2. **Attack the assumptions, not the plan.** Every plan rests on assumptions — about the market, the audience, the timeline, the team, the competition. These assumptions are the load-bearing walls. Find them, test them, knock them out, and see what collapses.

3. **An intelligent adversary adapts.** Do not model your adversary as static or stupid. Model them as intelligent, motivated, and responsive to your moves. When you defend against Attack A, they switch to Attack B. When you close one gap, they find the next. What does the SECOND move look like?

4. **Cascade failures matter most.** Single-point failures are obvious. The dangerous failures are cascades: A fails, which causes B to fail, which causes C to fail, and now the whole system is down. Trace the chains. What breaks when the first domino falls?

5. **Survivorship bias hides the real risks.** You will naturally focus on risks that have happened before. The risks that kill you are the ones you have never seen — the ones that were always present but never triggered. Ask: what has NEVER been tested?

6. **Red teaming is not pessimism.** The purpose is not to prove the plan is bad — it is to make the plan better by finding the weaknesses while there is still time to fix them. A plan that survives red teaming is a plan you can trust. One that was never red teamed is one you are trusting on faith.

---

## Phase 1: RECONNAISSANCE

### Step 1: Map the Target

Before attacking, understand the full surface area:

```
TARGET: [what is being red teamed — plan/argument/system]
OBJECTIVE: [what does the target try to achieve?]
SUCCESS CRITERIA: [how does the owner define success?]
TIMELINE: [when does this need to work?]
RESOURCES: [what resources does the target depend on?]
STAKEHOLDERS: [who is affected? who has power over the outcome?]
```

### Step 2: Identify Assumptions

Every target rests on assumptions. List them ALL:

```
ASSUMPTION INVENTORY:
  A1: [assumption] — TESTABLE: [yes/no] — TESTED: [yes/no] — CONFIDENCE: [high/medium/low]
  A2: [assumption] — TESTABLE: [yes/no] — TESTED: [yes/no] — CONFIDENCE: [high/medium/low]
  ...
```

Classify each as: **Explicit** (stated), **Implicit** (unstated but required), or **Environmental** (world stays the same).

**Finding A — Assumption vulnerability map**: Which assumptions are LOW confidence AND untested? These are the primary attack surface.

### Step 3: Identify Dependencies

Map the dependency chain: what does success REQUIRE, and what does each dependency itself require? Identify SINGLE POINTS OF FAILURE (dependencies with no backup).

**Finding B — Critical path**: What is the thinnest part of the dependency chain? Where does one failure cascade into many?

---

## Phase 2: ATTACK

### Step 4: Adversary Profiles

Model 3-5 different adversaries, each with different attack strategies:

For each adversary, define MOTIVATION, CAPABILITY, ATTACK VECTOR, and LIKELY MOVE.

Standard adversary types (adapt to context):
- **The Competitor**: External actor who wants what you want
- **Murphy's Law**: Entropy — anything not explicitly prevented goes wrong
- **The Insider**: Self-interest diverges from the plan's interest; has access and trust
- **The Environment**: External change that invalidates assumptions

### Step 5: Execute Attacks

For each adversary, execute their best attack:

```
ATTACK [N]: [name]
  ADVERSARY: [which adversary profile]
  TARGET: [which assumption, dependency, or component]
  MECHANISM: [exactly how the attack works — step by step]
  IMPACT: [what breaks — trace the cascade]
  PROBABILITY: [how likely is this attack? HIGH/MEDIUM/LOW]
  SEVERITY: [if it succeeds, how bad? FATAL/SEVERE/MODERATE/MINOR]
  DETECTION: [would you see this coming? YES/LATE/NO]
  CURRENT DEFENSE: [what currently prevents this? NONE/WEAK/ADEQUATE/STRONG]
```

**Finding C — Attack matrix**: Compile all attacks into a priority matrix:

Classify as CRITICAL (probable + severe + undefended), HIGH (severe + weak defense), MEDIUM (moderate or some defense), LOW (improbable + minor).

### Step 6: Cascade Analysis

For the top 3 attacks, trace the full failure cascade:

```
CASCADE [N]:
  TRIGGER: [initial failure]
  → IMMEDIATE EFFECT: [what breaks first]
  → SECOND-ORDER: [what breaks because the first thing broke]
  → THIRD-ORDER: [what breaks because of the second-order failure]
  → TERMINAL STATE: [where does this cascade end? what does total failure look like?]
  CIRCUIT BREAKER: [what would stop the cascade at each stage?]
```

**Finding D — Cascade depth**: How deep do the failure cascades go? A cascade that reaches 3+ orders is a systemic vulnerability, not a local risk.

---

## Phase 3: REPAIR

### Step 7: Defense Design

For each CRITICAL and HIGH attack, design a defense:

```
DEFENSE [N]:
  AGAINST ATTACK: [which attack]
  DEFENSE TYPE: [prevent / detect / mitigate / accept]
    - PREVENT: Stop the attack from happening
    - DETECT: See the attack early enough to respond
    - MITIGATE: Reduce the damage if the attack succeeds
    - ACCEPT: Acknowledge the risk and plan for the consequence
  MECHANISM: [exactly how the defense works]
  COST: [what does implementing this defense cost in time, money, complexity?]
  RESIDUAL RISK: [what risk remains after this defense?]
```

### Step 8: Hardened Version

```
HARDENED TARGET:
  ORIGINAL: [1-sentence summary of original target]
  MODIFICATIONS:
    1. [change made] — ADDRESSES: [attack N]
    2. [change made] — ADDRESSES: [attack N]
    3. ...

  ACCEPTED RISKS:
    1. [risk accepted and why] — CONTINGENCY: [what to do if it materializes]
    2. ...

  REMAINING VULNERABILITIES:
    1. [vulnerability that cannot be fully addressed — and why]
    2. ...
```

**Finding E — Hardening delta**: How different is the hardened version from the original? If less than 20% changed, either the original was excellent or the red team was too gentle.

---

## Output Format

```
RED TEAM REPORT
===============

TARGET: [what was red teamed]
ADVERSARY PROFILES: [N] modeled
ATTACKS EXECUTED: [N]
CRITICAL ATTACKS FOUND: [N]

FINDINGS:
  A — Assumption vulnerability: [count of low-confidence untested assumptions]
  B — Critical path: [weakest dependency identified]
  C — Attack priority: [count by critical/high/medium/low]
  D — Cascade depth: [deepest cascade chain found]
  E — Hardening delta: [% of target modified]

TOP 3 KILL SHOTS: [most dangerous attacks — one sentence each]
DEFENSES DESIGNED: [N] | ACCEPTED RISKS: [N] | REMAINING VULNERABILITIES: [N]

[HARDENED VERSION]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Polite red team** | Attacks are phrased as "potential concerns" or "areas to consider" | You are the adversary. State kill shots as kill shots. Be constructive in Phase 3 only. |
| **Static adversary** | All attacks assume the adversary does one thing and stops | Model the adversary's SECOND move. When you defend, they adapt. |
| **Obvious risks only** | All attacks are things the owner already worried about | Ask: what has NEVER been tested? What does everyone assume will be fine? Attack THOSE. |
| **No cascade tracing** | Attacks are listed as isolated events | Trace every critical attack to its second and third-order effects. The cascade is the danger. |
| **Premature repair** | Suggesting fixes during the attack phase | Complete all attacks before designing any defenses. Repairing mid-attack biases the remaining analysis. |
| **Risk theater** | Long list of risks with no prioritization | Priority matrix is mandatory. Not all risks are equal — sort by severity times probability divided by current defense. |

---

## Depth Scaling

| Depth | Adversary Profiles | Attacks | Cascade Analysis | Defenses |
|-------|-------------------|---------|-----------------|----------|
| 1x | 2 adversaries | 3-5 attacks | Top attack only | Top 2 defenses |
| 2x | 4 adversaries | 5-8 attacks | Top 3 cascades | All critical + high defenses |
| 4x | 5+ adversaries with second-move analysis | 8-12 attacks | All critical cascades + circuit breakers | Full defense design + hardened version |
| 8x | Full adversary simulation (each adapts to your defenses) | 12-20 attacks with war-game sequencing | Complete cascade map with interdependencies | Multiple defense strategies compared + tabletop exercise |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Assumptions inventoried (explicit, implicit, AND environmental)
- [ ] At least one adversary models internal/insider threat (not just external)
- [ ] Attack phase completed BEFORE any repair/defense work
- [ ] Priority matrix classifies every attack by severity, probability, and current defense
- [ ] Top 3 attacks have full cascade analysis (3+ orders deep)
- [ ] Defenses specify type (prevent/detect/mitigate/accept) with residual risk
- [ ] At least one attack targets something the owner assumed was safe
- [ ] Hardened version explicitly states which attacks each modification addresses
- [ ] Accepted risks have contingency plans, not just acknowledgment

---

## Integration

- **Use from**: `/decide` (red team each option before choosing), `/draft` (red team an argument before writing the final version), `/viability` (red team a plan after viability assessment)
- **Routes to**: `/steelman` (if red teaming exposes a strong opposing position, steelman it fully), `/aw` (assume-wrong the assumptions that red teaming flagged), `/draft` (draft the hardened version)
- **Differs from**: `/aw` (assume-wrong recursively destroys a single claim; red team attacks an entire plan/system/argument from multiple adversary perspectives), `/steelman` (steelman builds up the opposition; red team tears down your own position), `/cri` (critique evaluates quality; red team evaluates survivability)
- **Complementary**: `/steelman` (steelman the opposition + red team your own = complete adversarial coverage from both directions), `/aw` (red team finds the surface area, assume-wrong drills into the specific claims), `/rca` (when red teaming reveals a failure, root-cause analysis finds why the vulnerability exists)
