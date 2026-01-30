---
date: 2026-01-27
topic: Best practices for writing AI constitution document family
depth: 4x
claims: 12
crux_points: 5
status: LIKELY (refined standards with major paradigm corrections)
tensions: 5
---

# ARAW 4x: Writing Standards for AI Constitution Document Family

## Context

Following plan for improved constitution (document family, not single doc), user requested 4x ARAW to:
1. Identify best practices for rigorous writing
2. Question whether those practices are actually good
3. Ensure logical cohesion and high standards

Key prior decision: **Document family**, not single document.

---

## META-ARAW STRATEGY SELECTION

```
META-ARAW STRATEGY SELECTION
============================
RESTATED QUESTION: What are the best practices for writing a rigorous, logically
cohesive AI constitution document family? Then question whether these practices
are actually good.

Problem type: Decomposable (identify practices → question each)
Uncertainty type: Model uncertainty (what IS "rigorous" for this document type?)
Pitfall risk: Paradigm import (may import wrong domain's standards)
Selected frame: Writing craft frame, with paradigm questioning
Novelty target: Find where "rigor" actually hurts rather than helps
Strategy: Generate practices → ARAW each → find counterexamples
Depth: 4x
```

---

## Initial Practices (Before Questioning)

| # | Practice | Domain Source |
|---|----------|---------------|
| 1 | Justify every claim | Academic |
| 2 | Define terms precisely | Legal/technical |
| 3 | Follow logical structure | Philosophy |
| 4 | Be internally consistent | Logic |
| 5 | Write clearly | Technical writing |
| 6 | Structure systematically | Engineering |
| 7 | Use precise language | Legal |
| 8 | Illustrate with examples | Pedagogy |
| 9 | Bound scope explicitly | Academic |
| 10 | Acknowledge uncertainty | Science |
| 11 | Address counterarguments | Philosophy |
| 12 | Be self-contained | Publication |

---

## CRUX Points

### CRUX 1: Is academic rigor the right paradigm?

**Finding**: Constitution is NORMATIVE (commits to values), not DESCRIPTIVE (reports facts). Academic rigor fits descriptive writing.

**Resolution**: Rigor of commitment, not rigor of argument.

### CRUX 2: What kind of logic applies?

**Finding**: Values are foundational, not derived. Logic connects values to applications.

**Resolution**: Logical cohesion = consistent application of stated values, NOT derivation of values.

### CRUX 3: Is precision a feature or gaming target?

**Finding**: Both. Semantic precision (meaning clear) is good. Boundary precision (exact thresholds) enables gaming.

**Resolution**: Semantically precise, boundary-flexible.

### CRUX 4: Should examples be included?

**Finding**: Examples help training but constrain interpretation and reveal attack surface.

**Resolution**: Minimize in public docs; frame as illustrations; OK in internal training docs.

### CRUX 5: How does document family change standards?

**Finding**: Some standards (self-containment, systematic structure) apply to family, not individual docs.

**Resolution**: Meta-document defines family structure; individual docs optimized for purpose.

---

## Novel Findings

1. **[NOVEL] Constitution is normative, not descriptive** - Academic writing standards assume descriptive purpose. Normative documents commit rather than prove.

2. **[NOVEL] Semantic precision vs Boundary precision** - Meaning should be clear; exact thresholds should be flexible.

3. **[NOVEL] Examples are attack surfaces** - Each example teaches adversaries what to game around.

4. **[NOVEL] Counterarguments shouldn't be in final document** - Constitution commits, doesn't argue.

5. **[NOVEL] Vagueness can be feature** - Some concepts (wellbeing, dignity) are irreducibly vague. Forcing precision distorts them.

6. **[NOVEL] Scoped consistency > Global consistency** - Context-dependent rules aren't contradictory if scopes are clear.

7. **[NOVEL] Document family changes everything** - Self-containment, systematic structure, example usage work differently in family.

---

## Refined Practice Assessments

| # | Practice | Assessment | Revised Practice |
|---|----------|------------|------------------|
| 1 | Justify every claim | LIKELY | Justify applications; for values, explain don't derive |
| 2 | Define precisely | UNCERTAIN | Semantic precision yes, boundary precision no |
| 3 | Logical structure | LIKELY | For consistency, not for deriving values |
| 4 | Internal consistency | FOUNDATIONAL | Yes, but acknowledge irreducible tensions |
| 5 | Clear writing | LIKELY | Clear principles, precise applications, layered |
| 6 | Systematic structure | LIKELY | At family level, purpose-organized at doc level |
| 7 | Precise language | LIKELY | Semantic yes, boundary flexible |
| 8 | Use examples | UNCERTAIN | Sparingly, as illustrations, minimize in public |
| 9 | Bound scope | LIKELY | Yes with revision triggers; some principles unbounded |
| 10 | Acknowledge uncertainty | LIKELY | About means not values; layered by audience |
| 11 | Address counterarguments | LIKELY | In development, not in final document |
| 12 | Self-contained | UNLIKELY | Family self-contained; docs reference each other |

---

## Tensions Discovered

| # | Tension | Resolution |
|---|---------|------------|
| T1 | Derivation vs Commitment | Commit to values; derive applications |
| T2 | Precision vs Flexibility | Semantic precision, boundary flexibility |
| T3 | Examples vs Principles | Minimize examples; principles primary |
| T4 | Consistency vs Honesty | Consistent within scope; acknowledge cross-scope tensions |
| T5 | Self-contained vs Evolving | Family contained; living document protocols |

---

## Writing Standards Tiers

### Tier 1: Absolute (Always Apply)

- Internal consistency (within scope)
- Clarity (for intended audience)
- Semantic precision
- Honest uncertainty (about means)

### Tier 2: Modified (Apply With Nuance)

- Justification → For applications, not foundational values
- Logical structure → For consistency, not value derivation
- Precision → Boundary-flexible while semantically precise
- Examples → Sparingly; frame as illustration
- Scope → Bounded with revision triggers

### Tier 3: Reframed (Apply Differently)

- Self-containment → At family level, not document level
- Systematic → At family level; docs purpose-organized
- Counterarguments → In development, not in final doc
- Rigor → Of commitment, not of argument

### Tier 4: Rejected (Don't Apply)

- Derive values from first principles
- Exhaustive boundary precision
- Counterargument sections in document
- Standalone documents in family

---

## The Refined Standards

### 1. Purpose First

Each document type has specific purpose. Standards serve purpose.

| Type | Purpose | Dominant Standard |
|------|---------|-------------------|
| Core principles | Establish values | Clarity, commitment |
| Capability-specific | Apply to context | Precision (internal examples OK) |
| Developer-facing | Enable implementation | Technical precision |
| Public-facing | Build trust | Accessibility |
| Regulatory | Enable oversight | Verifiability |

### 2. Semantic Precision, Boundary Flexibility

```
WRONG: "Harm is defined as injury requiring care >$1000"
RIGHT: "Harm includes injury requiring medical attention.
        Severity assessed contextually."
```

### 3. Commit, Don't Argue

```
WRONG: "We value wellbeing because [philosophy]"
RIGHT: "We are committed to wellbeing. This means [applications]."
```

### 4. Acknowledge Tensions Explicitly

```
WRONG: [Silently contradictory sections]
RIGHT: "These principles can conflict. We resolve by [rule],
        accepting trade-off of [sacrifice]."
```

### 5. Examples as Illustrations

```
WRONG: "Harmful content includes: [list]"
RIGHT: "Harmful content is [principle]. Examples that illustrate
        (not limit) include: [list]"
```

### 6. Layered for Audience

- Surface (public): Clear commitments
- Middle (developers): Technical precision
- Deep (auditors): Full reasoning, cross-references

### 7. Living Document Protocols

```
Review triggers:
- Capability benchmarks exceeded
- Significant failures
- External oversight request
- Time elapsed
```

---

## DO_FIRST Actions

1. **Establish meta-criteria** - Which standards at family vs doc level
2. **Distinguish normative from descriptive** - What academic standards apply
3. **Design semantic precision guidelines** - Meaning clear, boundaries flexible
4. **Create document family architecture** - Docs and purposes
5. **Develop example usage policy** - When/how to use
6. **Create writing style guide** - Synthesis of refined standards

---

## Confidence Assessment

| Finding | Confidence |
|---------|------------|
| Normative/descriptive distinction | FOUNDATIONAL |
| Semantic/boundary precision | LIKELY (0.8) |
| Examples as attack surfaces | LIKELY (0.75) |
| Counterarguments out of document | LIKELY (0.7) |
| Document family changes standards | FOUNDATIONAL |
| Tensions should be acknowledged | FOUNDATIONAL |

---

## Surprise-Self Test

| Question | Answer |
|----------|--------|
| Surprising finding? | YES - Normative needs different standards |
| Learned something? | YES - Semantic vs boundary precision |
| Predictable output? | NO - Expected to validate, not reframe paradigm |
| Challenges initial view? | YES - "Rigorous" needs redefinition |

**PASSED**
