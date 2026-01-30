---
name: p
description: Convert analysis findings into steelmanned, actionable plans with conditional recommendations. Every recommendation includes a derivation chain explaining WHY. Requires a source analysis from /ar, /aw, /u, /araw, or /uaua.
---

# PROPOSE - Evidence-Derived Plan Synthesis

**Input**: $ARGUMENTS

---

## Core Principles

1. **Plans derive from evidence only.** Every plan must trace back to specific numbered items (F-numbers, R-numbers, W-numbers, U-numbers) from a source analysis. If you cannot cite a source item, you don't have a plan -- you have a guess. This skill REFUSES to operate without a source analysis.

2. **Steelman before evaluating.** Every plan is presented in its strongest possible form BEFORE being evaluated. A plan that was never steelmanned was never fairly considered.

3. **Conditional recommendations as default.** "Use this if X / don't use this if Y" is the standard format. Binary RECOMMEND / NOT RECOMMEND is a failure mode -- reality has conditions.

4. **Every recommendation has a derivation chain.** Source items -> what they show -> why that leads to this verdict. No recommendation without the chain.

5. **NOT RECOMMENDED plans get full treatment.** Rejected plans include: steelman, why the steelman still fails, and what would change the verdict. Anything less is strawman rejection.

6. **What you give up is part of the plan.** Every plan forecloses alternatives. If you can't state what a plan makes impossible, you haven't analyzed it.

7. **Three phases, strict separation.** Phase 1 extracts (no evaluation). Phase 2 compiles (no new plans). Phase 3 recommends (only from the registry). Never mix phases.

---

## Prerequisite: Source Analysis

This skill REQUIRES a prior analysis from one of:
- `/ar` (Assume Right) -- source items are R-numbered
- `/aw` (Assume Wrong) -- source items are W-numbered
- `/u` (Universalize) -- source items are U-numbered
- `/araw` (Assume Right / Assume Wrong) -- source items are C-numbered (claims) and F-numbered (findings)
- `/uaua` (Universalize-ARAW-Universalize-ARAW) -- source items are U-numbered and F-numbered

**If no source analysis exists in the conversation or is provided as input:**

```
PROPOSE REFUSED
===============
No source analysis found.

/p converts analysis findings into plans. It does not generate plans from scratch.

To use /p:
1. Run /ar, /aw, /u, /araw, or /uaua on your topic first
2. Then run /p to convert the findings into actionable plans

For generating plans without prior analysis, use /pss instead.
```

**Stop here. Do not proceed.**

---

## Phase 1: PLAN EXTRACTION

### Step 1: Identify the Source

```
SOURCE ANALYSIS: [which skill produced it -- ar/aw/u/araw/uaua]
SOURCE TOPIC: [what was analyzed]
SOURCE DEPTH: [depth level if specified]
ITEM PREFIX: [R/W/U/C+F -- the numbering used in the source]
TOTAL SOURCE ITEMS: [count]
```

### Step 2: Extract Plan Seeds

Scan the source registry for "plan seeds" -- items that point toward action. Every seed must cite a source item number.

**Seed types to extract:**

| Seed Type | Where to Find | Example |
|-----------|--------------|---------|
| **DO_FIRST actions** | Synthesis section of ARAW/UAUA | "Test assumption X" from F23 |
| **Derived alternatives** | AW findings, multi-valued AW | Alternative Y from W8 or F15 |
| **Foreclosures** | AR findings, foreclosure nodes | "Can no longer do Z" from R6 or F6 |
| **CRUX points** | CRUX registry in ARAW | "If X is true, then plan A; if false, plan B" from CRUX-3 |
| **Tensions** | Tension registry | "X contradicts Y" -- resolve via plan |
| **Convergent implications** | AR/ARAW where multiple branches require same thing | Multiple branches point to same action |
| **Validated claims** | Claims that SURVIVED/VALIDATED in registry | Build on what held up |
| **Rejected claims** | Claims that were REJECTED | Avoid plans that depend on these |
| **Load-bearing assumptions** | U findings marked LOAD-BEARING | Plans that test or hedge these |
| **Uncomfortable findings** | Findings explicitly marked uncomfortable | Plans others would avoid |

Format each seed:

```
[SEED-1] [action/direction implied] -- SOURCE: [item number(s)] -- SEED TYPE: [type]
[SEED-2] [action/direction implied] -- SOURCE: [item number(s)] -- SEED TYPE: [type]
...
```

### Step 3: Cluster Seeds into Plans

Group related seeds into 3-7 concrete plans. Each plan must:
- Have a clear action statement (what you DO)
- Cite at least 2 source items
- Be distinct from other plans (not a variant of the same thing)

```
[PLAN-1] [clear action statement]
  Seeds: [SEED-numbers]
  Source items: [item numbers from original analysis]

[PLAN-2] [clear action statement]
  Seeds: [SEED-numbers]
  Source items: [item numbers from original analysis]
...
```

**Cluster check:** If you have fewer than 3 plans, the source analysis may be too narrow -- note this. If you have more than 7, look for plans that can merge.

### Step 4: Steelman Each Plan

For EVERY plan (including ones you suspect will be rejected), present the strongest possible case:

```
[PLAN-1] STEELMAN:
  STRONGEST CASE: [2-4 sentences -- the best argument for this plan]
  BEST CONDITIONS: [when/where this plan would work best]
  IDEAL OUTCOME: [what success looks like if everything goes right]
  SOURCE SUPPORT: [which source items support this plan, with brief explanation]
```

**Steelman quality check:** If your steelman is 1 sentence or dismissive, you failed. A steelman should make someone genuinely consider the plan.

### Step 5: Evaluate Against Source Evidence

For EVERY plan, evaluate honestly using source evidence:

```
[PLAN-1] EVALUATION:
  SUPPORTING EVIDENCE: [source items that support -- item numbers + what they show]
  OPPOSING EVIDENCE: [source items that oppose -- item numbers + what they show]
  EVIDENCE BALANCE: [which side has stronger/more bedrock evidence]
  CRITICAL DEPENDENCY: [what must be true for this plan to work -- cite items]
  FAILURE MODE: [how this plan most likely fails -- cite items]
```

---

## Phase 2: PLAN REGISTRY

After ALL extraction and evaluation is complete, compile into a structured registry. No new plans introduced here.

```
PLAN REGISTRY
=============

SOURCE: [skill] on [topic] at [depth]
PLANS EXTRACTED: [N]

[PLAN-1] [action statement]
  STEELMAN: [strongest case -- 1-2 sentences]
  STRENGTHS: [from source items -- cite numbers]
  WEAKNESSES: [from source items -- cite numbers]
  RISKS: [what could go wrong -- cite items]
  DEPENDENCIES: [what must be true -- cite items]
  REVERSIBILITY: [easy to undo / hard to undo / one-way door]
  COST: [what this requires -- time, money, effort, opportunity]
  GIVES UP: [what this plan forecloses -- what you can no longer do]
  FIRST ACTIONS: [concrete next steps if this plan is chosen]

[PLAN-2] ...
...

COMPARISON TABLE:
| Plan | Strengths | Weaknesses | Reversible? | Cost | Gives Up |
|------|-----------|------------|-------------|------|----------|
| PLAN-1 | [brief] | [brief] | [Y/N/Partial] | [brief] | [brief] |
| PLAN-2 | [brief] | [brief] | [Y/N/Partial] | [brief] | [brief] |
...

PLAN INTERACTIONS:
- [PLAN-X] and [PLAN-Y]: [compatible / incompatible / sequential]
- [PLAN-X] enables [PLAN-Z]: [how]
- [PLAN-X] blocks [PLAN-Z]: [how]
```

---

## Phase 3: RECOMMENDATION SYNTHESIS

Derived entirely from the plan registry. No new plans or evidence introduced here.

### Categorize Each Plan

Every plan gets ONE of four categories:

**RECOMMENDED** -- Evidence strongly supports. Use this.
```
[PLAN-N] RECOMMENDED
  DERIVATION CHAIN:
    Source items [numbers] show [what they show]
    -> This means [intermediate conclusion]
    -> Therefore [why this plan follows]
  USE IF: [conditions where this is the right choice]
  DON'T USE IF: [conditions where this is wrong]
  FIRST ACTIONS:
    1. [specific action] -- resolves [what]
    2. [specific action] -- resolves [what]
```

**CONDITIONALLY RECOMMENDED** -- Evidence supports under specific conditions.
```
[PLAN-N] CONDITIONALLY RECOMMENDED
  DERIVATION CHAIN:
    Source items [numbers] show [what they show]
    -> This means [intermediate conclusion]
    -> Therefore [why this plan follows WHEN conditions hold]
  CONDITION: [precise condition that must be true]
  HOW TO CHECK: [how to verify the condition]
  USE IF: [when the condition holds + what else must be true]
  DON'T USE IF: [when the condition fails + what to do instead]
  IF CONDITION UNKNOWN: [what to do to find out]
  FIRST ACTIONS:
    1. [specific action] -- resolves [what]
```

**NOT RECOMMENDED** -- Evidence opposes. Don't use this.
```
[PLAN-N] NOT RECOMMENDED
  STEELMAN REMINDER: [restate the strongest case -- 1-2 sentences]
  DERIVATION CHAIN:
    Source items [numbers] show [what they show]
    -> This means [intermediate conclusion]
    -> Despite the steelman, this fails because [why]
  WHY IT FAILS: [specific source items that defeat the steelman]
  WHAT WOULD CHANGE THIS VERDICT: [what new evidence would flip to RECOMMENDED]
  USE INSTEAD: [which other plan addresses the same need]
```

**UNRESOLVED** -- Evidence insufficient to recommend or reject.
```
[PLAN-N] UNRESOLVED
  DERIVATION CHAIN:
    Source items [numbers] show [what they show]
    -> But [what's missing or contradictory]
    -> Cannot determine recommendation because [why]
  WHAT'S MISSING: [specific information needed]
  HOW TO RESOLVE: [specific actions to get that information]
  LEANS TOWARD: [which direction evidence slightly favors, if any]
```

### Final Summary

```
RECOMMENDATION SUMMARY
======================

SOURCE: [skill] on [topic]

RECOMMENDED:
- [PLAN-N]: [one-line summary] -- USE IF: [brief condition]

CONDITIONALLY RECOMMENDED:
- [PLAN-N]: [one-line summary] -- CONDITION: [brief]

NOT RECOMMENDED:
- [PLAN-N]: [one-line summary] -- BECAUSE: [brief]
  WOULD CHANGE IF: [brief]

UNRESOLVED:
- [PLAN-N]: [one-line summary] -- NEEDS: [brief]

SUGGESTED SEQUENCE:
[If multiple plans are compatible, suggest an order]
1. [First action from highest-priority RECOMMENDED plan]
2. [Check condition for CONDITIONALLY RECOMMENDED plan]
3. [Resolve UNRESOLVED plans by gathering missing info]

WHAT THIS ANALYSIS DOES NOT COVER:
[Explicitly state limitations -- what /p can't tell you]
```

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Plan from thin air** | Plan doesn't cite source item numbers | Delete it. Every plan traces to source items. |
| **Soft steelman** | 1-sentence dismissive steelman | Rewrite. Steelman should make someone genuinely consider the plan. |
| **Recommendation without derivation** | "RECOMMENDED" with no chain | Add the chain: source items -> what they show -> why this verdict. |
| **Binary-only recommendations** | All RECOMMENDED or NOT RECOMMENDED, no conditions | Add USE IF / DON'T USE IF to every recommendation. Reality has conditions. |
| **Missing "gives up"** | Plan entry has no GIVES UP field | Every plan forecloses something. Find what. |
| **Strawman rejection** | NOT RECOMMENDED without steelman reminder | Always restate the steelman before explaining why it fails. |
| **Cherry-picked evidence** | Derivation chain cites 2 items but source has 30 | Check ALL relevant source items, not just the ones that support your verdict. |
| **Missing failure mode** | Plan has no failure mode identified | Every plan can fail. How does this one fail? Cite source items. |
| **No interactions** | Plans listed independently with no interaction analysis | Check: are plans compatible? Sequential? Does one block another? |

---

## Pre-Completion Check

- [ ] Source analysis identified and referenced (skill, topic, item prefix)
- [ ] All plan seeds cite source item numbers
- [ ] 3-7 plans extracted (if fewer, noted why)
- [ ] EVERY plan steelmanned (including rejected ones)
- [ ] Steelmans are genuine (not dismissive 1-liners)
- [ ] EVERY plan evaluated against source evidence (both supporting and opposing)
- [ ] EVERY plan has: strengths, weaknesses, risks, dependencies, reversibility, cost, gives up
- [ ] Comparison table complete
- [ ] Plan interactions analyzed
- [ ] EVERY recommendation has a derivation chain (source items -> intermediate conclusion -> verdict)
- [ ] EVERY recommendation has USE IF / DON'T USE IF conditions
- [ ] NOT RECOMMENDED plans include steelman reminder + what would change verdict
- [ ] UNRESOLVED plans include what's missing + how to resolve
- [ ] No plans introduced without source item citations
- [ ] **Cherry-pick check**: Are there source items you ignored? If yes, check if they affect any plan.
- [ ] **Strawman check**: Re-read each NOT RECOMMENDED. Would a proponent feel their plan was fairly considered?
- [ ] **Condition check**: Are there RECOMMENDED plans that should be CONDITIONALLY RECOMMENDED? Binary confidence is suspicious.
