---
name: "imprt - Improve Reasoning Tool"
description: "Auto-diagnose the reasoning toolkit as a whole — identify quality gaps, missing skills, structural inconsistencies, integration failures, and improvement priorities across the entire skill library."
---

# Improve Reasoning Tool

**Input**: $ARGUMENTS

---

## Core Principles

1. **The toolkit is a system, not a collection.** Individual skill quality matters, but the system-level properties matter more: coverage (are all thinking modes represented?), routing (can users find the right skill?), integration (do skills chain properly?), consistency (do skills follow the same standard?). Improving one skill while the routing is broken helps no one.

2. **Improvement has layers.** From most impactful to least: (a) missing capabilities that users need, (b) broken routing that sends users to wrong skills, (c) quality gaps in high-use skills, (d) quality gaps in low-use skills, (e) formatting inconsistencies. Attack in this order.

3. **The toolkit should self-diagnose.** This skill is the toolkit examining itself. The diagnostic must be honest — identifying real weaknesses, not performing a flattering self-assessment. The hardest improvements to identify are the ones the toolkit is systematically blind to.

4. **User friction is the primary signal.** If users can't find the right skill, that's worse than a skill being slightly under-polished. If the routing skills (wsib, fonss, extract, handle) don't know about newer skills, the newer skills effectively don't exist.

5. **The exemplar skills define quality, not the average.** Don't measure the toolkit against its average skill quality. Measure against the best skills (foht, sbfow, iterate, araw, w). Every skill should be within striking distance of the exemplars.

---

## Phase 1: System-Level Diagnostic

Evaluate the toolkit as a whole before looking at individual skills.

### Coverage Audit

```
[R1] THINKING_MODES_REPRESENTED:
     Decision making: [skills] — COVERAGE: [strong | adequate | weak | missing]
     Problem solving: [skills] — COVERAGE: [level]
     Exploration: [skills] — COVERAGE: [level]
     Validation: [skills] — COVERAGE: [level]
     Planning: [skills] — COVERAGE: [level]
     Writing: [skills] — COVERAGE: [level]
     Self-correction: [skills] — COVERAGE: [level]
     Meta-cognition: [skills] — COVERAGE: [level]
     Skill management: [skills] — COVERAGE: [level]
     [other modes discovered]: [skills] — COVERAGE: [level]

[R2] COVERAGE_GAPS: [thinking modes with weak or missing representation]
```

### Routing Audit

```
[R3] ROUTING_SKILLS: [list all skills that route to other skills]
[R4] ROUTING_COVERAGE: [what % of skills are reachable via routing?]
[R5] ORPHAN_SKILLS: [skills not referenced by any routing skill or integration section]
[R6] ROUTING_STALENESS: [routing skills that don't know about newer skills]
```

### Integration Audit

```
[R7] INTEGRATION_MAP: [sample of skill chains — do they work?]
[R8] BROKEN_CHAINS: [skills that invoke non-existent skills]
[R9] MISSING_INTEGRATION: [skills with no integration section]
```

### Quality Distribution

```
[R10] QUALITY_DISTRIBUTION:
      Exemplar (300+ lines, all elements, dense content): [N skills]
      Good (150-300 lines, all elements): [N skills]
      Adequate (100-150 lines, most elements): [N skills]
      Partial (50-100 lines, missing elements): [N skills]
      Stub (< 50 lines): [N skills]
```

---

## Phase 2: Individual Skill Scan

Sample skills from each quality tier and diagnose:

```
[R-N] SKILL: /[name]
     TIER: [exemplar | good | adequate | partial | stub]
     ISSUES: [specific problems found]
     USAGE: [how many other skills reference it]
     IMPROVEMENT_PRIORITY: [critical | high | medium | low | skip]
```

### Scan Strategy

- Read ALL stubs and partials (they're short)
- Sample 20% of adequate skills
- Spot-check 10% of good skills
- Read all routing and category skills fully (they're system-critical)

---

## Phase 3: Systemic Issue Detection

```
[R-N] SYSTEMIC_ISSUE: [pattern across multiple skills]
     AFFECTED_COUNT: [how many skills]
     SEVERITY: [how much this degrades the toolkit]
     ROOT_CAUSE: [why this pattern exists — era effect, generation method, etc.]
     FIX: [systemic fix, not per-skill]
```

### Common Systemic Issues

| Issue | Signal | Systemic Fix |
|-------|--------|-------------|
| **Era quality gaps** | Skills from one date are systematically worse | Batch improvement via /impss |
| **Routing staleness** | New skills not in routing tables | Update all routing skills' integration sections |
| **Inconsistent structure** | Different skills use different section names/formats | Establish template, normalize |
| **Missing cross-references** | Skills that should reference each other don't | Map skill relationships, update integration sections |
| **Category imbalance** | 50 decision skills but 3 writing skills | Create new skills in underrepresented areas via /skgap |
| **Naming inconsistency** | Some skills use abbreviations, others full words | Establish naming convention |
| **Depth inconsistency** | Some skills have 8x depth, others have no scaling | Add depth scaling to all |

---

## Phase 4: Improvement Roadmap

```
IMPROVEMENT ROADMAP
===================

CRITICAL (do now):
  1. [specific action] — IMPACT: [what this fixes]
  2. [specific action] — IMPACT: [what this fixes]

HIGH (do soon):
  1. [specific action] — IMPACT: [what this fixes]

MEDIUM (do when able):
  1. [specific action]

LOW (backlog):
  1. [specific action]

RECOMMENDED SKILL CREATION:
  1. /[name] — [what it would do] — WHY: [gap it fills]
  2. /[name] — [what it would do] — WHY: [gap it fills]

RECOMMENDED SKILL IMPROVEMENTS:
  → INVOKE: /impss [list of skills needing improvement]

RECOMMENDED GAP ANALYSIS:
  → INVOKE: /skgap [areas identified as underrepresented]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Flattering self-assessment** | "The toolkit is comprehensive and well-structured" without identifying real issues | Be adversarial. What would a frustrated user complain about? |
| **Individual focus only** | Looked at skills one by one but missed system-level issues | Start with system diagnostics (coverage, routing, integration) before individual skills |
| **Quantity metrics only** | "We have 400+ skills!" without quality assessment | Count skills by quality tier, not just total |
| **Improvement without priority** | List of 50 improvements with no ordering | Everything gets a priority level. Critical/high get done. Low goes to backlog |
| **Missing the user perspective** | All improvements are structural/internal, none address usability | Ask: "Can a new user find the right skill for their problem in < 30 seconds?" |
| **Scope blindness** | Only evaluates what exists, not what's missing | Coverage audit must identify ABSENT thinking modes, not just assess present ones |

---

## Depth Scaling

| Depth | System Audit | Skill Scan | Pattern Detection | Roadmap |
|-------|-------------|-----------|-------------------|---------|
| 1x | Coverage + routing only | Stubs only | Top 3 patterns | Critical actions only |
| 2x | Full system audit | All stubs + partials + routing skills | All patterns | Full roadmap |
| 4x | Full + user journey simulation | 50% of all skills | Full + root cause | Full + timeline |
| 8x | Full + competitive analysis | All skills | Full + prediction | Full + implementation plan |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Coverage audit completed — all thinking modes assessed
- [ ] Routing audit completed — orphan and stale routing identified
- [ ] Integration audit completed — broken chains found
- [ ] Quality distribution mapped across all tiers
- [ ] Systemic issues identified with root causes
- [ ] Improvement roadmap has clear priority ordering
- [ ] Missing skills identified (not just improvements to existing)
- [ ] User-facing issues prioritized over internal quality issues

---

## Integration

- Use from: toolkit maintenance, periodic quality reviews, after large skill additions
- Routes to: `/impss` (batch skill improvement), `/skgap` (skill gap analysis), `/imps` (single skill improvement)
- Complementary: `/skgap` (imprt finds all issues; skgap specifically finds missing capabilities)
- Differs from `/imps`: imps improves one skill; imprt diagnoses the whole toolkit
- Differs from `/impss`: impss executes batch improvements; imprt identifies what needs improving
- Differs from `/skgap`: skgap finds missing skills; imprt assesses the toolkit holistically
