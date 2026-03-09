---
name: "wre - Writing Requirements Engineering"
description: "Derive writing requirements before drafting. Builds a multi-stage requirements object: artifact definition, thesis and claim set, technical requirements, philosophical requirements, expansion requirements, outline requirements, exclusions, traceability, and draft readiness."
context: fork
---

# Writing Requirements Engineering

**Input**: $ARGUMENTS

---

## Purpose

Do not draft first.
Do not polish first.
Do not free-associate first.
Do requirements first.

This skill treats writing as a requirements engineering problem.
It derives what the artifact must do.
It derives what the artifact must not do.
It derives what the artifact must prove.
Only after that does it permit an outline.
Only after that does it permit a draft.

Use it for essays, posts, arguments, explainers, and other writing where:
- the writer keeps splicing together too many ideas
- the target venue has real standards
- the core question is unclear
- the draft keeps overclaiming
- the writing needs philosophical precision
- the artifact needs to carry a proof path rather than a topic pile

---

## Core Principles

1. Requirements precede outline.
2. Outline precedes draft.
3. Technical requirements and philosophical requirements are different.
4. Every requirement must be atomic.
5. Every requirement must be testable.
6. Exclusions are requirements.
7. Traceability is mandatory.
8. Every section in the final artifact must earn its place.
9. A writing artifact needs a thesis object before it needs structure.
10. A philosophical essay needs anti-equivocation requirements before stylistic polish.

---

## Stage 0: Artifact Definition

Define the writing target.

```
ARTIFACT:
- Type: [essay / post / memo / explainer / sequence post / comment]
- Venue: [where it will appear]
- Reader: [who reads it]
- Reader baseline: [what they already know]
- Writer goal: [what the artifact must achieve]
- Reader after-state: [what the reader should now see / believe / distinguish / be able to do]
- Core unresolved question: [single question]
- Scope boundary: [what this artifact is NOT trying to do]
- Stakes: [why getting this right matters]
```

Do not proceed until the artifact has:
- one reader
- one main question
- one bounded scope
- one clear after-state

---

## Stage 1: Thesis and Claim Set

Define the central claim object before deriving requirements.

This stage answers:
- What is the main thesis?
- What weaker version is defensible?
- What stronger version must be refused?
- What supporting claims are required?
- What claims are tempting but out of scope?

Format:

```
THESIS OBJECT
- Core thesis: [single sentence]
- Claim type: [heuristic / epistemic / explanatory / normative / metaphysical / mixed]
- Stronger claim refused: [single sentence]
- Supporting claims:
  [C1] ...
  [C2] ...
  [C3] ...
- Out-of-scope claims:
  [O1] ...
  [O2] ...
```

Do not continue until:
- the thesis fits the scope boundary
- the stronger claim refused is explicit
- the supporting claims are distinct

---

## Stage 2: Technical Requirements

Derive the operational requirements of the writing artifact.

Technical requirements include:
- target length range
- evidence requirements
- citation or prior-work requirements
- structure constraints
- tone constraints
- banned words or moves
- examples needed
- claims that require support
- claims that must be weakened or scoped
- venue-specific constraints
- opening constraints
- ending constraints

Format:

```
TECHNICAL REQUIREMENTS
[T1] Requirement: ...
     Verification: ...
[T2] Requirement: ...
     Verification: ...
```

Each technical requirement must answer:
- what must be true
- how we will know it is satisfied

---

## Stage 3: Philosophical Requirements

Derive what the piece must cover at the level of thought, not format.

Philosophical requirements include:
- what distinction the essay must make
- what equivocations it must avoid
- what it must define
- what it must not define
- what burden of proof it is taking on
- what kind of claim it is making
- what stronger claim it must explicitly refuse
- what prior frameworks it must relate to
- what the reader must understand by the end
- what the essay must preserve without collapsing
- what level of abstraction it must stay at
- what bridge claims are needed between sections

Format:

```
PHILOSOPHICAL REQUIREMENTS
[P1] Requirement: ...
     Verification: ...
[P2] Requirement: ...
     Verification: ...
```

Useful categories:
- ontology requirements
- epistemology requirements
- explanatory requirements
- scope requirements
- novelty-positioning requirements
- anti-equivocation requirements
- anti-overclaim requirements
- bridge requirements
- burden-of-proof requirements

For philosophical writing, require explicit treatment of:
- what is being claimed
- what is not being claimed
- what would count against the claim

---

## Stage 4: Expansion Requirements

Only after technical and philosophical requirements exist.

Expansion requirements specify what the final artifact must contain in order to satisfy the earlier requirements.

This stage still does not produce the outline.
It produces the obligations that the outline must satisfy.

Expansion requirements include:
- which sections must exist
- which concepts must be introduced
- which examples must exist
- which transitions must occur
- what order the reasoning must follow
- what must be introduced early
- what must be deferred
- what must be cut entirely
- what objection or limit must be acknowledged

Format:

```
EXPANSION REQUIREMENTS
[E1] Requirement: ...
     Satisfies: [T..., P...]
[E2] Requirement: ...
     Satisfies: [T..., P...]
```

Each expansion requirement must trace back to earlier requirements.

---

## Stage 5: Outline Requirements

Now derive the outline obligations.

This stage is not freeform outlining.
This stage converts expansion requirements into an ordered proof-bearing skeleton.

For each section, specify:
- section purpose
- question answered
- dependency
- required claims
- forbidden drift
- exit condition

Format:

```
OUTLINE REQUIREMENTS
[L1] Section: ...
     Purpose: ...
     Answers: ...
     Depends on: [...]
     Must include: [...]
     Must not do: [...]
     Exit condition: ...

[L2] Section: ...
```

Rules:
- no section without a requirement source
- no section that exists only for style
- no example section unless a prior requirement demands an example
- no conclusion that introduces a new thesis

---

## Stage 6: Exclusions

List what this artifact must not do.

```
EXCLUSIONS
[X1] ...
[X2] ...
[X3] ...
```

Examples:
- bundled theses
- literature-free reinvention
- throat-clearing openings
- overclaiming
- definitions fights
- tangents that belong in a second post
- examples that hijack the topic
- conclusions that switch subjects

---

## Stage 7: Traceability Matrix

Map all outline and expansion requirements to the earlier requirements they satisfy.

Format:

```
TRACEABILITY
[E1] satisfies [T2, P3, P7]
[L1] satisfies [E1, E3]
[L2] satisfies [E2, T4]
...
```

Any expansion or outline requirement with no traceability is likely decorative.
Any technical or philosophical requirement with no expansion path is unsatisfied.

---

## Stage 8: Draft Gate

Only draft after all of the following pass:

- [ ] Artifact has one core unresolved question
- [ ] Thesis object exists
- [ ] Stronger claim refused is explicit
- [ ] Technical requirements are atomic
- [ ] Philosophical requirements are atomic
- [ ] Expansion requirements trace back to earlier requirements
- [ ] Outline requirements trace back to expansion requirements
- [ ] Exclusions are explicit
- [ ] At least one likely equivocation has been neutralized
- [ ] At least one likely reader objection has a planned location
- [ ] The conclusion does not introduce a new subject

If the gate fails:
- do not draft
- return to requirements work

---

## Output Format

```
ARTIFACT DEFINITION
...

THESIS OBJECT
...

TECHNICAL REQUIREMENTS
[T1] ...

PHILOSOPHICAL REQUIREMENTS
[P1] ...

EXPANSION REQUIREMENTS
[E1] ...

OUTLINE REQUIREMENTS
[L1] ...

EXCLUSIONS
[X1] ...

TRACEABILITY
[E1] satisfies [...]
[L1] satisfies [...]

DRAFT READINESS
STATUS: READY | NOT READY
BLOCKERS:
- ...
```

---

## Integration

- Use before: `/w`
- Use before: `/qo`
- Use after: `/sbfow` when a draft keeps failing
- Use with: `/araw` to test candidate core claims before drafting
- Use with: `/ar` to derive what a thesis commits the essay to covering

---

## Verification

- [ ] No draft prose appeared before requirements
- [ ] Thesis object exists before requirements expansion
- [ ] Technical requirements are distinct from philosophical requirements
- [ ] Expansion requirements are derived rather than improvised
- [ ] Outline requirements exist and are not decorative
- [ ] Exclusions are explicit
- [ ] Traceability is complete
- [ ] Draft gate is meaningful rather than ceremonial
