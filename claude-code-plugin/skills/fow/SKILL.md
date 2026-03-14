---
name: "fow - Figure Out Why"
description: "Systematic diagnosis of WHY something is happening (or not happening). Forces generation of multiple candidate explanations before evaluation, separates symptoms from causes, and distinguishes proximate from root cause. Works across domains: code, systems, design, behavior, outcomes."
context: fork
output:
  format: "prose"
---

# Figure Out Why

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Why is this happening?**: Something observable is occurring and the user wants to understand its cause (e.g., "why is the build slow?", "why do users abandon the onboarding flow?").
**Interpretation 2 — Why is this NOT happening?**: Something expected is failing to occur and the user wants to understand what's blocking it (e.g., "why isn't the cache invalidating?", "why won't this person respond to feedback?").
**Interpretation 3 — Why did this happen?**: A past event occurred and the user wants to understand the causal chain that produced it (e.g., "why did we lose that client?", "why did the migration corrupt data?").

If ambiguous, ask: "I can help diagnose why something IS happening, why something ISN'T happening, or why something already happened — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Core Principle: The Five-Before-One Rule

**Most people stop at the first plausible explanation.** The first explanation that "makes sense" captures attention and forecloses further search. This is premature closure, and it is the single most common diagnostic failure.

/fow exists to prevent this. The rule:

**Generate AT LEAST 5 candidate explanations before evaluating ANY of them.**

Not 5 versions of the same idea. Five genuinely different causal hypotheses. If your candidates are all variations on one theme, you haven't generated enough. Push into different categories, different levels of analysis, different domains.

Why 5? Because:
- Candidate 1 is what everyone already thinks. It's the obvious answer.
- Candidate 2 is the second-most-obvious. Still within the same frame.
- Candidate 3 starts requiring effort. You're leaving the default frame.
- Candidate 4 forces you into uncomfortable territory. Different level of analysis.
- Candidate 5 is where genuine insight often hides. It's the one nobody considered.

**Do not skip this. Do not evaluate early. Generate first, judge second.**

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/fow 4x [input]").

| Depth | Min Candidates | Min Levels Deep | Min Tests Proposed | Min Distinguishing Predictions |
|-------|---------------|-----------------|--------------------|---------------------------------|
| 1x    | 5             | 3               | 3                  | 2                               |
| 2x    | 7             | 5               | 5                  | 4                               |
| 4x    | 10            | 7               | 8                  | 6                               |
| 8x    | 15            | 9               | 12                 | 10                              |
| 16x   | 20            | 12              | 18                 | 15                              |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## Step 1: Stabilize the Observation

Before asking "why," make sure you know WHAT is actually happening.

1. **State the observation precisely.** Not "the system is broken" but "API latency exceeds 2s on POST requests to /submit after 3pm daily."
2. **Separate observation from interpretation.** "The button doesn't work" is observation. "The click handler is broken" is interpretation. Start with observation.
3. **Quantify where possible.** How often? How much? Since when? Under what conditions?
4. **Identify the delta.** What changed? What's different between when it worked and when it didn't? Between where it works and where it doesn't?
5. **Check: is this actually a problem?** Sometimes the "problem" is expected behavior that the observer doesn't understand. Rule this out explicitly.

```
OBSERVATION: [precise, interpretation-free statement of what's happening]
SINCE: [when it started, or when it was first noticed]
FREQUENCY: [how often, under what conditions]
DELTA: [what changed, or what's different between working/not-working]
CONFIRMED PROBLEM: [yes/no — is this actually unexpected behavior?]
```

---

## Step 2: Separate Symptoms from the Phenomenon

Most "why" questions are about symptoms, not the core phenomenon. Treating a symptom as the thing to explain leads to shallow answers.

1. **List everything observable.** All the symptoms, effects, and associated observations.
2. **Identify which are downstream effects of others.** If A causes B, and B causes C, then C is a symptom of B, and B is a symptom of A. Don't explain C directly — explain A.
3. **Find the earliest/deepest phenomenon.** This is what you're actually trying to explain.

```
SYMPTOMS (downstream effects):
- [S1] [symptom] — downstream of: [which other symptom or the core phenomenon]
- [S2] [symptom] — downstream of: [which other symptom or the core phenomenon]
- ...

CORE PHENOMENON (what actually needs explaining):
[The earliest/deepest thing in the causal chain that you can observe]
```

---

## Step 3: Generate Candidate Explanations

**This is the critical step. Do NOT evaluate yet. Only generate.**

For each candidate, provide:
- A clear statement of the proposed cause
- The causal mechanism (HOW would this cause produce the observed phenomenon?)
- What category it falls into

### Candidate Categories

Force yourself to generate candidates across multiple categories:

| Category | Question to Ask |
|----------|----------------|
| **Mechanical/Direct** | What is the most direct, proximate cause? |
| **Systemic/Structural** | What system or structure makes this outcome likely? |
| **Historical/Temporal** | What changed? What accumulated over time? |
| **Human/Behavioral** | What incentive, habit, or cognitive pattern explains this? |
| **Environmental/Contextual** | What external condition or constraint is at play? |
| **Absence/Missing** | What's NOT present that should be? (missing safeguard, missing information, missing feedback) |
| **Interaction/Emergent** | Is this caused by the interaction of multiple factors, none sufficient alone? |
| **Mistaken Premise** | What if the observation itself is wrong, or the question is based on a false assumption? |

```
CANDIDATE EXPLANATIONS (generate before evaluating):

[E1] [explanation]
  Category: [which category]
  Mechanism: [how this would produce the observation]

[E2] [explanation]
  Category: [which category]
  Mechanism: [how this would produce the observation]

[E3] [explanation]
  Category: [which category]
  Mechanism: [how this would produce the observation]

[E4] [explanation]
  Category: [which category]
  Mechanism: [how this would produce the observation]

[E5] [explanation]
  Category: [which category]
  Mechanism: [how this would produce the observation]

[E6+] [continue until depth floor met]
  ...
```

### Generation Quality Check

Before proceeding, verify:
- [ ] At least 3 different categories are represented
- [ ] At least one candidate challenges the framing of the question itself
- [ ] At least one candidate would be uncomfortable or surprising to the questioner
- [ ] No two candidates are just variations of the same underlying idea
- [ ] At least one candidate involves absence (something missing) rather than presence (something happening)

If these checks fail, generate more candidates before proceeding.

---

## Step 4: Evaluate Each Candidate

NOW you may evaluate. For each candidate, apply assume-right / assume-wrong logic:

```
[E1] [explanation]

  ASSUME RIGHT (this IS the cause):
  - What else should be true if this is the cause? [list observable predictions]
  - What should NOT be happening if this is the cause? [list things that should be absent]
  - Does the timing match? [check against timeline]
  - Does the scope match? [check: does it explain ALL the symptoms, or only some?]
  - Proximate or root? [is this the immediate trigger, or the deeper reason?]

  ASSUME WRONG (this is NOT the cause):
  - What's the strongest evidence against this explanation?
  - What alternative would better explain the same evidence?
  - Is there a simpler explanation that covers the same ground?

  VERDICT: [LIKELY / POSSIBLE / UNLIKELY / RULED OUT]
  EVIDENCE GAP: [what information would confirm or rule this out?]
```

### Proximate vs. Root Cause

For every candidate rated LIKELY or POSSIBLE, ask: **is this the proximate cause or the root cause?**

- **Proximate cause**: The immediate trigger. "The server crashed because memory hit 100%."
- **Root cause**: The deeper reason the proximate cause existed. "Memory hit 100% because nobody configured alerts, because the monitoring setup has no review process, because the team has no operational maturity standards."

The proximate cause tells you what to fix RIGHT NOW. The root cause tells you what to fix SO IT DOESN'T HAPPEN AGAIN. You need both.

```
CAUSAL CHAIN (for each LIKELY/POSSIBLE candidate):
[proximate cause] <- [intermediate cause] <- [intermediate cause] <- [root cause]
```

Keep asking "but why?" until you reach one of:
- A deliberate decision (someone chose this — now ask why they chose it)
- A structural constraint (the system is built this way — now ask why)
- An absence of something (nobody built/defined/checked this — now ask why not)
- Bedrock (a fact of the domain that can't be further decomposed)

---

## Step 5: Synthesize and Rank

```
DIAGNOSIS SUMMARY
=================

OBSERVATION: [restated precisely]

MOST LIKELY CAUSE(S):
1. [E-number] [explanation] — Confidence: [HIGH/MEDIUM/LOW]
   Proximate cause: [what's immediately responsible]
   Root cause: [what's fundamentally responsible]
   Evidence for: [what supports this]
   Evidence against: [what challenges this]

2. [E-number] [explanation] — Confidence: [HIGH/MEDIUM/LOW]
   ...

CONTRIBUTING FACTORS (not the main cause, but making it worse):
- [factor] — contributes to: [which main cause]
- ...

RULED OUT:
- [E-number] [explanation] — ruled out because: [reason]
- ...

STILL UNCERTAIN:
- [E-number] [explanation] — uncertain because: [what's missing]
- ...

INTERACTION EFFECTS:
[Are any of the causes interacting? Would cause A alone not produce the problem,
but cause A + cause B together does? Note these explicitly.]
```

---

## Step 6: Propose Verification

For each LIKELY or POSSIBLE cause, propose specific tests:

```
VERIFICATION PLAN
=================

To confirm [E-number]:
  CHECK: [specific thing to examine, measure, or test]
  EXPECT: [what you'd find if this cause is correct]
  ANTI-EXPECT: [what you'd find if this cause is wrong]
  EFFORT: [quick check / investigation / experiment]

To confirm [E-number]:
  CHECK: [specific thing to examine, measure, or test]
  EXPECT: [what you'd find if this cause is correct]
  ANTI-EXPECT: [what you'd find if this cause is wrong]
  EFFORT: [quick check / investigation / experiment]

DISTINGUISHING TESTS (tests that differentiate between competing explanations):
  TEST: [what to check]
  If [E-number] is right: [prediction]
  If [E-number] is right instead: [different prediction]

RECOMMENDED ORDER:
1. [test] — because: [why this first — fastest, cheapest, most decisive]
2. [test] — because: [why this second]
3. ...
```

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Premature closure** | Evaluated before generating 5+ candidates | Stop evaluating. Generate more candidates first. |
| **Monocausal thinking** | All candidates are variations of one idea | Force candidates from at least 3 different categories. |
| **Symptom-as-cause** | "Why" answer is itself a symptom | Ask "but why is THAT happening?" Keep going deeper. |
| **Narrative satisfaction** | Explanation "feels right" but has no testable predictions | Add specific predictions. If you can't, the explanation is too vague. |
| **Confirmation focus** | Only looked for evidence FOR the favored explanation | Actively search for evidence AGAINST it. What would disprove it? |
| **Proximate-only** | Found the trigger but not the underlying reason | Keep asking "why" until you hit a system, structure, or decision. |
| **Complexity dodge** | "It's complicated" or "multiple factors" without specifics | Name each factor, its mechanism, and its relative contribution. |
| **Observer bias** | Explanation maps to what observer expected to find | Include at least one candidate that would surprise or discomfort the observer. |

---

## When FOW Routes to Other Skills

- If the phenomenon involves claims that need stress-testing: route to `/araw`
- If a confirmed root cause needs full post-mortem treatment: route to `/rca`
- If the "why" is about a decision that was made: consider `/araw` on the decision's assumptions
- If multiple interacting causes need mapping: consider fault tree or system mapping

---

## Saving Output

Output is NOT auto-saved. If the user wants to save, they invoke `/sf` after the session.

---

## Verification Checklist

- [ ] Observation stated precisely, separated from interpretation
- [ ] Symptoms separated from core phenomenon
- [ ] At least 5 candidate explanations generated BEFORE evaluation began
- [ ] Candidates span at least 3 different categories
- [ ] At least one candidate challenges the question's framing
- [ ] At least one uncomfortable or surprising candidate included
- [ ] Each candidate evaluated with assume-right and assume-wrong
- [ ] Proximate cause distinguished from root cause for each LIKELY candidate
- [ ] Causal chains traced to bedrock (decision, structure, absence, or domain fact)
- [ ] Specific, testable verification steps proposed for top candidates
- [ ] Distinguishing tests proposed (tests that differentiate between competing explanations)
- [ ] Depth floors met (candidates, levels deep, tests, distinguishing predictions)
- [ ] No premature closure — first plausible explanation was not accepted without competition
