---
name: "av - Assumption Verification"
description: "Systematically verify assumptions by classifying type, determining verification method, executing, and updating confidence."
---

# Assumption Verification

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Verify assumptions in a plan**: The user has a plan, strategy, or proposal and wants to check whether its underlying assumptions hold.
**Interpretation 2 — Verify assumptions in a claim**: The user has tested a claim (via /araw or /claim) and wants the assumptions behind it verified.
**Interpretation 3 — Verify specific assumptions**: The user already has a list of assumptions (possibly from /aex) and wants them checked.

If ambiguous, ask: "Do you want me to extract and verify assumptions from something, or do you already have specific assumptions to check?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Extraction is not verification.** /aex surfaces assumptions; /av verifies them. These are separate operations. Extracting an assumption and saying "this seems reasonable" is not verification — it's just restating the assumption with more words.

2. **Verification method must match assumption type.** Empirical assumptions need evidence. Logical assumptions need proof. Normative assumptions need stakeholder consensus. Using the wrong method produces false confidence.

3. **Priority by criticality x uncertainty x verifiability.** Don't verify assumptions in order of appearance. Verify the ones that matter most (high criticality), are least certain (low confidence), and can actually be checked (high verifiability). This combination maximizes information gain per effort.

4. **Background assumptions are the most dangerous.** Explicit assumptions are visible. Implicit assumptions are findable. Background assumptions — things so "obvious" nobody states them — are invisible and often wrong. Actively probe for them.

5. **Refuted high-criticality assumptions change everything.** When a critical assumption is refuted, don't just note it — trace the consequences. What part of the plan/claim/argument collapses? What needs to change?

6. **CONDITIONAL is the most common and most useful status.** Most assumptions aren't simply true or false — they hold under specific conditions. Identifying those conditions is often more valuable than a binary verdict.

---

## Procedure

### Phase 1: Extract Assumptions

1. Identify the claim, plan, or argument to examine
2. Ask: "What must be true for this to work?"
3. List every assumption across three layers:
   - **Explicit** (stated): assumptions the author acknowledged
   - **Implicit** (unstated but required): assumptions necessary for the argument to hold, but never mentioned
   - **Background** (invisible): assumptions so fundamental they feel like facts ("customers will pay for value", "the market exists", "we can hire people")
4. Number each: A1, A2, A3...

### Phase 2: Classify Each Assumption

| Type | Description | Verification Method |
|------|-------------|-------------------|
| **Empirical** | Facts, data, measurements | Evidence lookup, measurement, observation |
| **Logical** | If-then relationships, definitions | Logical analysis, proof, counterexample search |
| **Normative** | Should/ought statements, values | Value elicitation, stakeholder consensus, precedent |
| **Causal** | X causes Y, X leads to Y | Experiment, counterfactual analysis, mechanism tracing |
| **Statistical** | Distributions, rates, probabilities | Data analysis, sampling, base rate check |
| **Practical** | We can do X, they will do Y, X is feasible | Testing, prototyping, expert consultation, reference class |

### Phase 3: Prioritize

Rate each assumption on three dimensions:

```
PRIORITIZATION MATRIX:

| # | Assumption | Criticality | Confidence | Verifiability | Priority |
|---|-----------|-------------|------------|---------------|----------|
| A1 | [text] | H/M/L | H/M/L | easy/hard/impossible | [score] |

Priority = HIGH criticality + LOW confidence + EASY verifiability → verify first
```

**Priority categories:**
- **P1 (verify immediately)**: High criticality + Low confidence + Easy/moderate verifiability
- **P2 (verify if time permits)**: High criticality + High confidence (might be overconfident), OR Medium criticality + Low confidence
- **P3 (note but skip)**: Low criticality, OR impossible to verify
- **P0 (critical warning)**: High criticality + Low confidence + Impossible to verify — this is a risk that cannot be mitigated through verification

### Phase 4: Execute Verification

For each P1 and P2 assumption, apply the method matched to its type:

**Empirical**: What evidence exists? Is it reliable? Does it directly address this assumption or is it adjacent?

**Logical**: Does the if-then actually hold? Are there counterexamples? Hidden conditions?

**Normative**: Who would disagree? What alternative values lead to different conclusions?

**Causal**: What's the mechanism? Are there confounders? What else could explain the observed effect?

**Statistical**: What's the base rate? Is the sample representative? Is the effect size meaningful?

**Practical**: Has anyone done this before? What reference class applies? What's the inside vs outside view?

Record findings for each:
```
A[N]: [assumption text]
TYPE: [type]
METHOD: [what was checked]
FINDING: [what was found]
STATUS: VERIFIED | REFUTED | WEAKENED | CONDITIONAL | UNVERIFIABLE
CONDITIONS: [if CONDITIONAL, under what conditions does it hold?]
EVIDENCE: [specific evidence supporting the status]
```

### Phase 5: Report

```
ASSUMPTION VERIFICATION REPORT
Subject: [what was examined]
Total assumptions: [N]
Verified: [N] | Refuted: [N] | Weakened: [N] | Conditional: [N] | Unverifiable: [N]

P1 RESULTS (critical, verified):
| # | Assumption | Type | Status | Key Evidence |
|---|-----------|------|--------|-------------|
| A[N] | [text] | [type] | [status] | [summary] |

CRITICAL FINDINGS:
[Refuted or weakened high-criticality assumptions — what they mean for the plan/claim]

CONDITIONAL FINDINGS:
[Assumptions that hold only under specific conditions — what those conditions are]

UNVERIFIABLE RISKS:
[P0 assumptions — high criticality, can't be checked]

IMPACT ASSESSMENT:
[What changes based on these findings? What parts of the plan/claim are affected?]

RECOMMENDED ACTIONS:
1. [Specific action to address finding]
2. [Specific action to address finding]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Shallow extraction** | Only explicit assumptions found | Probe for implicit and background layers — ask "what else must be true?" |
| **Wrong verification method** | Empirical assumption checked with logic, or vice versa | Match method to type — evidence for facts, proof for logic |
| **Flat prioritization** | All assumptions treated equally | Use the criticality x confidence x verifiability matrix |
| **Binary verdicts** | Everything is VERIFIED or REFUTED | Most assumptions are CONDITIONAL — find the conditions |
| **Verification theater** | "This seems reasonable" counted as verification | Verification requires specific evidence or proof, not agreement |
| **Impact disconnect** | Assumptions refuted but no trace of consequences | When critical assumptions fail, trace what collapses |

---

## Depth Scaling

| Depth | Scope | Floor |
|-------|-------|-------|
| **1x** | Extract explicit assumptions, verify top 3 | 5 assumptions extracted, 3 verified |
| **2x** | Extract explicit + implicit, verify all P1 | 10 assumptions, all P1 verified |
| **4x** | All three layers, verify P1 and P2, full report | 15+ assumptions, P1 and P2 verified, impact assessment |
| **8x** | Exhaustive extraction, all verified, sensitivity analysis | 20+ assumptions, all verifiable ones checked, cascading impact analysis |

---

## Pre-Completion Checklist

- [ ] All three assumption layers probed (explicit, implicit, background)
- [ ] Each assumption classified by type
- [ ] Prioritized by criticality x confidence x verifiability
- [ ] Verification method matched to assumption type
- [ ] Each verified assumption has specific evidence (not just "seems right")
- [ ] CONDITIONAL assumptions have conditions stated
- [ ] Refuted high-criticality assumptions have impact traced
- [ ] P0 risks (unverifiable + critical) flagged explicitly
- [ ] Recommended actions are specific and actionable

---

## Integration

- **Use from**: /aex (extracts assumptions, /av verifies them), /claim (after ARAW, verify underlying assumptions), /decide (verify assumptions behind each option), /evaluate (verify assumptions behind assessed work)
- **Routes to**: /araw (when an assumption needs stress-testing rather than just verification), /claim (when a refuted assumption becomes a claim to test), /fla (when unverifiable assumptions represent risks)
- **Differs from**: /aex (extracts assumptions but doesn't verify), /ver (GOSM verification is about claims, /av is specifically about assumptions), /val (validates deliverables against requirements, /av verifies underlying beliefs)
- **Complementary**: /aex (extract first, then verify), /fla (failure anticipation for unverifiable assumptions), /prm (pre-mortem uses assumptions to imagine failure)
