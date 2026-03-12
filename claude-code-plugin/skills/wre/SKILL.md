---
name: "wre - Writing Requirements Engineering"
description: "Derive writing requirements before drafting. Builds a multi-stage requirements object: artifact definition, thesis object, technical requirements, philosophical requirements, expansion requirements, outline requirements, exclusions, traceability, and draft gate."
context: fork
output:
  format: "prose"
---

# Writing Requirements Engineering

**Input**: $ARGUMENTS

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Pre-draft requirements derivation**: The user has a writing topic or assignment and wants to derive rigorous requirements before any drafting begins, to prevent the common failure of writing without clear intellectual obligations.
**Interpretation 2 — Draft diagnosis**: The user has a draft that isn't working and suspects the problem is at the requirements level, not the prose level — they want to reverse-engineer what requirements are missing or conflicting.
**Interpretation 3 — Thesis stress-testing**: The user has a thesis or central claim and wants to build the full requirements scaffolding around it — defining what it commits them to, what it excludes, and what support structure it demands.

If ambiguous, ask: "I can help with deriving requirements before you write, diagnosing a broken draft's missing requirements, or stress-testing a thesis — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Writing fails at the requirements stage, not the drafting stage.** A bad draft is almost always a symptom of missing, conflicting, or untested requirements. "The draft doesn't work" usually means "the requirements were never derived." Rewriting is wasted effort if the requirements are still wrong.

2. **Technical requirements and philosophical requirements are different failure modes.** Technical requirements (length, tone, structure, evidence) are about format and craft. Philosophical requirements (what distinction must be made, what equivocation must be avoided, what burden of proof is assumed) are about thought. Conflating them produces writing that's well-formatted but intellectually incoherent.

3. **A thesis is not a topic.** "This essay is about AI alignment" is a topic. "Alignment researchers systematically underweight the difficulty of value specification because they treat it as an engineering problem rather than a philosophical one" is a thesis. The thesis object must be a claim — something that could be wrong, that has a stronger version you refuse and a weaker version that's trivially true.

4. **Every requirement must be testable.** "The essay should be clear" is not a requirement — there's no verification condition. "The reader should be able to state the core distinction in one sentence after reading" is a requirement. Untestable requirements are decorative and will not constrain the draft.

5. **Exclusions do more work than inclusions.** Knowing what the artifact must NOT do eliminates more bad drafts than knowing what it must do. "This essay does not argue that X" prevents the most common failure mode: scope creep through bundled theses. Exclusions are the highest-leverage requirements.

6. **Traceability prevents decoration.** Every section, example, and transition in the outline must trace back to a requirement. If a section exists but satisfies no requirement, it's decorative — it exists because the writer wanted to include it, not because the artifact needs it. Decoration is the primary failure mode of ambitious writing.

---

## Stage 0: Artifact Definition

Define the writing target before any requirements work.

```
ARTIFACT DEFINITION
  Type: [essay | post | memo | explainer | sequence post | comment | report | proposal]
  Venue: [where it will appear — specific publication, blog, internal doc]
  Reader: [specific audience — not "general public"]
  Reader baseline: [what they already know — what you don't need to explain]
  Writer goal: [what the artifact must achieve — be specific]
  Reader after-state: [what the reader should see / believe / distinguish / be able to do after reading]
  Core unresolved question: [single question this artifact answers]
  Scope boundary: [what this artifact is NOT trying to do]
  Stakes: [why getting this right matters — what goes wrong if it's bad]
```

**Gate**: Do not proceed until the artifact has:
- One specific reader (not multiple audiences)
- One main question (not a cluster)
- One bounded scope (with explicit exclusions)
- One clear after-state (testable)

If you cannot specify these, the artifact is not ready for requirements — it needs `/foht` or `/gu` first.

---

## Stage 1: Thesis Object

Define the central claim before deriving requirements.

```
THESIS OBJECT
  Core thesis: [single sentence — must be a claim, not a topic]
  Claim type: [heuristic | epistemic | explanatory | normative | metaphysical | mixed]
  Weaker claim (trivially true): [the version no one would argue with — useless but safe]
  Stronger claim (refused): [the version that would be overclaiming — tempting but indefensible]
  ACTUAL claim (defended): [the version you're actually defending — between weak and strong]
  Supporting claims:
    [C1] [claim] — REQUIRED_BECAUSE: [why the thesis needs this]
    [C2] [claim] — REQUIRED_BECAUSE: [why the thesis needs this]
    [C3] [claim] — REQUIRED_BECAUSE: [why the thesis needs this]
  Out-of-scope claims:
    [O1] [claim] — EXCLUDED_BECAUSE: [why this doesn't belong]
    [O2] [claim] — EXCLUDED_BECAUSE: [why this doesn't belong]
```

**Gate**: Do not continue until:
- The thesis is a claim (could be wrong), not a topic (can't be wrong)
- The stronger claim refused is explicit and you can articulate WHY you refuse it
- The weaker claim is identified so you know the floor of your ambition
- Supporting claims are distinct from each other and each is necessary

### Thesis Quality Test

Ask: "Could a thoughtful, informed person disagree with this thesis?" If no → it's too weak. If the disagreement would be obviously absurd → it's too strong. The thesis should live in the zone where disagreement is reasonable but you have a case.

---

## Stage 2: Technical Requirements

Derive the operational requirements of the writing artifact.

```
TECHNICAL REQUIREMENTS
[T1] Requirement: [specific, testable constraint]
     Category: [length | evidence | citation | structure | tone | vocabulary | opening | closing | venue]
     Verification: [how to check if satisfied]
[T2] ...
```

### Required Categories

Check each and derive requirements where applicable:

| Category | Ask |
|----------|-----|
| **Length** | What range? What's the hard ceiling? |
| **Evidence** | What counts as support? Data? Examples? Citations? |
| **Prior work** | What must be referenced? What's the positioning obligation? |
| **Structure** | Sections required? Ordering constraints? |
| **Tone** | Academic? Conversational? Authoritative? What's forbidden? |
| **Vocabulary** | Banned words? Required definitions? Jargon policy? |
| **Opening** | What must the opening accomplish? What opening patterns are banned? |
| **Closing** | What must the ending do? What can it NOT do? (No new theses) |
| **Venue** | What does the publication/context demand? |
| **Examples** | How many? What type? Concrete or abstract? |
| **Claims** | Which claims require explicit support? Which must be scoped? |

Each technical requirement must be:
- **Atomic** — one requirement, one thing
- **Testable** — has a verification condition
- **Non-overlapping** — distinct from other requirements

---

## Stage 3: Philosophical Requirements

Derive what the piece must achieve at the level of thought, not format.

```
PHILOSOPHICAL REQUIREMENTS
[P1] Requirement: [specific intellectual obligation]
     Category: [ontology | epistemology | scope | novelty | anti-equivocation | anti-overclaim | bridge | burden-of-proof]
     Verification: [how to check if satisfied]
[P2] ...
```

### Required Categories

| Category | Ask |
|----------|-----|
| **Distinctions** | What distinction must the essay make that readers don't currently make? |
| **Anti-equivocation** | Where could the essay use the same word for two different things? Name each risk |
| **Definitions** | What must be defined? What must NOT be defined (reader already knows)? |
| **Burden of proof** | What kind of claim is this? What level of support does that claim type require? |
| **Prior frameworks** | What existing work must be positioned against? |
| **Abstraction level** | What level must the essay stay at? Where does it risk going too abstract or too concrete? |
| **Bridge claims** | What intermediate claims connect sections? What logical gaps need filling? |
| **Anti-overclaim** | Where will the essay be tempted to claim more than it can support? |
| **Reader understanding** | What must the reader understand by the end that they didn't before? |
| **Preservation** | What tension or complexity must the essay preserve WITHOUT collapsing into a simple answer? |

For philosophical or argumentative writing, explicitly require:
- What is being claimed
- What is NOT being claimed
- What would count as evidence against the claim

---

## Stage 4: Expansion Requirements

Derive what the final artifact must contain to satisfy earlier requirements.

This stage does NOT produce the outline. It produces the **obligations** the outline must satisfy.

```
EXPANSION REQUIREMENTS
[E1] Requirement: [what the artifact must contain]
     Satisfies: [T..., P...] — traceability to earlier requirements
     Type: [section | concept | example | transition | acknowledgment | definition]
[E2] ...
```

### Derivation Rules

- Every expansion requirement must trace to at least one T or P requirement
- If a T or P requirement has no expansion requirement, it's unsatisfied → derive one
- Expansion requirements specify WHAT must exist, not WHERE it goes (that's Stage 5)
- Include: which concepts must be introduced, which examples must appear, which transitions must occur, what order reasoning must follow, what must be introduced early, what must be deferred, what must be cut, what objection must be acknowledged

---

## Stage 5: Outline Requirements

Convert expansion requirements into an ordered proof-bearing skeleton.

```
OUTLINE REQUIREMENTS
[L1] Section: [name]
     Purpose: [what this section accomplishes]
     Answers: [what question this section resolves for the reader]
     Depends on: [which prior sections must come first]
     Satisfies: [E..., T..., P...]
     Must include: [specific content obligations]
     Must not do: [specific drift risks for this section]
     Exit condition: [what must be true for this section to be complete]

[L2] ...
```

### Outline Rules

- No section without a requirement source — if it satisfies nothing, delete it
- No section that exists only for style or convention
- No example section unless a prior requirement demands an example
- No conclusion that introduces a new thesis or claim
- No introduction that buries the core question
- Section order must follow logical dependency, not just convention

---

## Stage 6: Exclusions

Explicit list of what this artifact must NOT do.

```
EXCLUSIONS
[X1] [what is excluded] — WHY: [what failure this prevents]
[X2] ...
```

### Common Exclusions to Check

| Exclusion Type | Description |
|---------------|-------------|
| **Bundled theses** | Trying to prove two things in one artifact |
| **Literature-free reinvention** | Ignoring prior work and rediscovering from scratch |
| **Throat-clearing openings** | "Since the dawn of time..." |
| **Overclaiming** | Claiming more than the evidence supports |
| **Definition fights** | Spending the essay arguing about word meanings |
| **Tangent promotion** | Including material that belongs in a separate piece |
| **Example hijacking** | An example that's more interesting than the thesis and takes over |
| **Subject-switching conclusions** | Ending on a different topic than you started |
| **Hedge stacking** | So many qualifiers the thesis dissolves |
| **False balance** | Giving equal weight to positions with unequal evidence |

---

## Stage 7: Traceability Matrix

Map all downstream requirements to upstream sources.

```
TRACEABILITY MATRIX
[E1] satisfies [T2, P3, P7]
[E2] satisfies [T1, P5]
[L1] satisfies [E1, E3]
[L2] satisfies [E2, T4]
...

UNSATISFIED REQUIREMENTS: [any T or P with no downstream path]
DECORATIVE ELEMENTS: [any L or E with no upstream source]
```

### Traceability Rules

- Any expansion or outline requirement with no upstream trace is **decorative** → remove or justify
- Any technical or philosophical requirement with no downstream path is **unsatisfied** → derive expansion requirements
- Decorative elements are the #1 source of bloat in ambitious writing
- Unsatisfied requirements are the #1 source of "the essay doesn't quite work"

---

## Stage 8: Draft Gate

Only permit drafting after ALL pass:

- [ ] Artifact has one core unresolved question (not a cluster)
- [ ] Thesis object is a claim (not a topic)
- [ ] Stronger claim refused is explicit with stated reason
- [ ] Technical requirements are atomic and testable
- [ ] Philosophical requirements are atomic and testable
- [ ] Expansion requirements trace to T and P requirements
- [ ] Outline requirements trace to expansion requirements
- [ ] Exclusions are explicit (minimum 3)
- [ ] At least one equivocation risk has been neutralized
- [ ] At least one likely reader objection has a planned location
- [ ] The conclusion does not introduce a new subject
- [ ] Traceability matrix has zero unsatisfied requirements
- [ ] Traceability matrix has zero decorative elements

```
DRAFT READINESS
STATUS: READY | NOT READY
BLOCKERS: [list any failing checks]
NEXT ACTION: [if not ready — what specific requirement work remains]
```

If the gate fails: do not draft. Return to the specific stage where the gap exists.

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Requirements retrofitted to draft** | Requirements written AFTER a draft exists, to justify what was already written | Delete the draft. Derive requirements from the question, not the existing text |
| **Topic masquerading as thesis** | "This essay is about X" instead of "I claim X" | Apply the disagreement test: could someone disagree? If not, it's a topic |
| **Untestable requirements** | "The essay should be good/clear/insightful" | Every requirement needs a verification condition. If you can't test it, it's not a requirement |
| **Philosophical requirements missing** | Only technical requirements derived | Go back to Stage 3. Philosophical requirements prevent intellectual failure; technical requirements prevent format failure |
| **Traceability skipped** | Outline produced without checking coverage | Run the matrix. Find the unsatisfied requirements and decorative elements |
| **Exclusion-free** | No explicit exclusions | Every good artifact has things it deliberately doesn't do. Derive at least 3 |
| **Gate passed ceremonially** | Checked all boxes without actually verifying | Each gate check must reference specific requirement IDs, not just "yes" |
| **Scope creep via supporting claims** | Supporting claims expand until the essay has 3 theses | Each supporting claim must be necessary for the core thesis. If it could be its own essay, it's out of scope |
| **Requirements too numerous** | 30+ requirements that can't all be satisfied in one artifact | Prioritize ruthlessly. If you can't satisfy all requirements, narrow scope rather than producing a bloated artifact |

---

## Depth Scaling

| Depth | Stages | Requirements Count | Traceability | Draft Gate |
|-------|--------|-------------------|-------------|-----------|
| 1x | 0-1-2-5-8 (skip philosophical, expansion, exclusions) | 5-8 total | Informal | Basic checklist |
| 2x | All stages | 10-15 total | Full matrix | Full gate |
| 4x | All stages + iterative refinement | 15-25 total | Full + gap analysis | Full + peer review simulation |
| 8x | All stages + /araw on thesis + /aex on assumptions | 25+ total | Full + sensitivity analysis | Full + adversarial review |

Default: 2x for essays and posts, 1x for memos and comments. These are floors.

---

## Pre-Completion Checklist

- [ ] Artifact definition has one reader, one question, one scope, one after-state
- [ ] Thesis is a claim (not a topic) with stronger version explicitly refused
- [ ] Technical and philosophical requirements are separated and each is testable
- [ ] Expansion requirements all trace to T or P requirements
- [ ] Outline requirements all trace to expansion requirements
- [ ] Exclusions explicitly state what the artifact will NOT do (minimum 3)
- [ ] Traceability matrix has zero unsatisfied and zero decorative entries
- [ ] Draft gate passed non-ceremonially (references specific requirement IDs)

---

## Integration

- Use before: `/w` (writing), `/pw` (persuasive writing)
- Use after: `/sbfow` when a draft keeps failing — the problem is usually missing requirements
- Use with: `/araw` to stress-test the thesis object before building requirements on it
- Use with: `/ar` to derive what the thesis commits the artifact to covering
- Use with: `/aex` to test assumptions embedded in the thesis
- Differs from `/w`: w handles the actual writing; wre handles the requirements that make writing possible
- Differs from `/stl`: stl addresses style and voice; wre addresses structure and intellectual obligations
- Differs from `/pw`: pw focuses on persuasion; wre focuses on requirements regardless of rhetorical goal
