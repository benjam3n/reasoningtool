# /val Use 3 independent methods to validate whether the skill tier system reflects actual quality differences
**Date:** 2026-03-09
**Skill:** /val (Validation)

---

## Validation Setup

```
TARGET: The tier system (tier 1/2/3/4) used to classify ~570 skills
REQUIREMENTS SOURCE: Derived from the tier system's implied purpose
TOTAL REQUIREMENTS: 9 (3 per validation method)
CRITICALITY LEVELS: See below per requirement
```

The tier system claims to represent quality/importance levels, with tier 1 being the best (12 skills), tier 2 next (27 skills), tier 3 domain-specific (92 skills), and tier 4 the remainder (439 skills). Three independent methods are used to test this claim:

1. **Structural Quality Analysis** -- Do higher-tier skills have objectively better structure?
2. **Network Centrality Analysis** -- Are higher-tier skills more interconnected and referenced?
3. **Curation Signal Analysis** -- Are higher-tier skills more likely to be recommended and discoverable?

---

## Method 1: Structural Quality Analysis

### R1: Higher-tier skills should have more content (line count)
**CRITICALITY:** Important
**EVIDENCE:**

| Tier | Avg Lines | Median Lines | Min | Max |
|------|-----------|-------------|-----|-----|
| Tier 1 | 324 | 351 | 115 | 542 |
| Tier 2 | 322 | 315 | 110 | 710 |
| Tier 3 | 199 | 146 | 56 | 759 |
| Tier 4 | 163 | 149 | 50 | 556 |

**STATUS: Partially met.**
Tier 1 and tier 2 have ~60-100% more content on average than tier 3/4. But tier 1 and tier 2 are essentially identical in length (324 vs 322 avg). The claim holds for the top-vs-bottom divide but fails to differentiate the top two tiers from each other. Also, 3% of tier-4 skills and 14% of tier-3 skills exceed the tier-1 average of 324 lines.

### R2: Higher-tier skills should have more sections (structural sophistication)
**CRITICALITY:** Important
**EVIDENCE:**

| Tier | Avg Sections | Min | Max |
|------|-------------|-----|-----|
| Tier 1 | 8.8 | 5 | 19 |
| Tier 2 | 8.5 | 5 | 15 |
| Tier 3 | 5.5 | 4 | 16 |
| Tier 4 | 6.7 | 3 | 35 |

**STATUS: Partially met.**
Tier 1/2 have more sections than tier 3 on average (8.5-8.8 vs 5.5). But tier 4 averages 6.7 sections -- *more* than tier 3 -- which contradicts the tier ordering. Tier 1 and tier 2 are again nearly identical.

### R3: Higher-tier skills should have better structural features (interpretations, depth scaling, failure modes, etc.)
**CRITICALITY:** Critical
**EVIDENCE:**

| Feature | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---------|--------|--------|--------|--------|
| Interpretations section | 100% | 100% | 43% | 8% |
| Core Principles section | 8% | 4% | 4% | 23% |
| Depth Scaling section | 42% | 52% | 7% | 23% |
| Failure Modes section | 0% | 4% | 3% | 22% |
| Pre-Completion Checklist | 0% | 4% | 3% | 18% |
| Integration section | 25% | 15% | 8% | 51% |

Skills with ALL 5 advanced sections (Core Principles, Depth Scaling, Failure Modes, Pre-Completion Checklist, Integration):
- Tier 1: **0 out of 12** (0%)
- Tier 2: **1 out of 27** (4%)
- Tier 3: **3 out of 92** (3%)
- Tier 4: **80 out of 439** (18%)

**STATUS: Not met.**
This is the most damaging finding. There are two distinct skill "formats" in the codebase:
- **Format A** (Tier 1/2): Characterized by an Interpretations section (100% of tier 1/2 have it). Lacks Core Principles, Failure Modes, Pre-Completion Checklists.
- **Format B** (Tier 4): Characterized by Core Principles + Failure Modes + Integration sections. 80 tier-4 skills have ALL five advanced structural features; zero tier-1 skills do.

The tiers do not reflect structural quality. They reflect *which batch the skill was created in*. Tier 1/2 skills have one format; tier 4 skills have a newer, arguably more sophisticated format with more guardrails (failure modes, checklists, integration). The tier system labels the older format as higher quality even though the newer format has more quality-assurance features.

---

## Method 2: Network Centrality Analysis

### R4: Higher-tier skills should be invoked by more other skills (they are foundational)
**CRITICALITY:** Critical
**EVIDENCE:**

| Tier | Total invoked_by | Avg invoked_by | Skills never invoked |
|------|-----------------|----------------|---------------------|
| Tier 1 | 38 | 3.2 | 1/12 (8%) |
| Tier 2 | 55 | 2.0 | 14/27 (52%) |
| Tier 3 | 36 | 0.4 | 67/92 (73%) |
| Tier 4 | 264 | 0.6 | 318/439 (72%) |

**STATUS: Partially met.**
Tier 1 skills are the most invoked per-skill (avg 3.2), confirming they serve as foundational building blocks. The ordering tier1 > tier2 > tier3 holds for per-skill averages. However, tier 4 has a higher per-skill invocation average (0.6) than tier 3 (0.4), and tier 4 has a *much* higher total (264 vs 36), meaning the bulk of the system's interconnection lives in tier 4.

Also problematic: 52% of tier-2 skills are never invoked by any other skill. If tier 2 represents "important" skills, more than half are isolated from the skill network.

### R5: Higher-tier skills should invoke other skills (they are orchestrators)
**CRITICALITY:** Important
**EVIDENCE:**

| Tier | Total invokes | Avg invokes |
|------|--------------|-------------|
| Tier 1 | 11 | 0.9 |
| Tier 2 | 1 | 0.0 |
| Tier 3 | 28 | 0.3 |
| Tier 4 | 181 | 0.4 |

**STATUS: Not met.**
Tier 2 invokes almost nothing (total of 1 across 27 skills). Tier 4 is the most active invoker both in total and per-skill average (excluding tier 1). If orchestration capability is a quality signal, tier 4 outperforms tier 2 and tier 3.

### R6: Higher-tier skills should have richer metadata (categories, tags, input_types)
**CRITICALITY:** Nice-to-have
**EVIDENCE:**

| Tier | Avg categories | Avg tags | Avg input_types | Incomplete metadata % |
|------|---------------|----------|-----------------|----------------------|
| Tier 1 | 1.2 | 1.5 | 0.7 | 42% |
| Tier 2 | 0.8 | 0.9 | 0.4 | 59% |
| Tier 3 | 0.6 | 1.4 | 0.6 | 30% |
| Tier 4 | 0.5 | 0.9 | 0.3 | 69% |

**STATUS: Not met.**
Metadata completeness does not follow tier order. Tier 3 has the lowest rate of incomplete metadata (30%), while tier 2 (59%) and tier 1 (42%) have more gaps. If anything, this suggests tier 3 was batch-processed with metadata while tier 1/2 were not systematically tagged.

---

## Method 3: Curation Signal Analysis

### R7: Higher-tier skills should be the ones recommended in CLAUDE.md routing tables
**CRITICALITY:** Critical
**EVIDENCE:**

From the CLAUDE.md "Direct Skills" recommendation table, 48 skills are recommended. Their tier distribution:

| Tier | # Recommended | % of Tier |
|------|--------------|-----------|
| Tier 1 | 11 | 92% of tier 1 |
| Tier 2 | 18 | 67% of tier 2 |
| Tier 3 | 8 | 9% of tier 3 |
| Tier 4 | 11 | 3% of tier 4 |

**STATUS: Met.**
This is the strongest validation signal. 92% of tier-1 skills and 67% of tier-2 skills appear in the curation table. The tiers do strongly predict whether a skill is recommended. However, 11 tier-4 skills are also recommended (e.g., /advr, /but, /pbr, /gd, /grf, /col, /conr, /per, /aso, /ata), raising the question of whether those should be promoted.

### R8: Higher-tier skills should be category-skill targets (routed to by orchestrators)
**CRITICALITY:** Important
**EVIDENCE:**
Category skills (17 orchestrators like /claim, /decide, /diagnose) route users to specific analytical skills. Per the invoked_by data, tier-1 skills average 3.2 incoming references while tier-4 skills average 0.6. This means tier-1 skills are 5x more likely to be a routing destination.

**STATUS: Met.**
Tier 1 skills are disproportionately the targets of category-level routing, confirming they occupy a central role in the system's architecture.

### R9: The tier boundaries should be clean -- no tier-4 skill should outperform a tier-1 skill on quality metrics
**CRITICALITY:** Important
**EVIDENCE:**
- 15 tier-4 skills exceed the tier-1 average line count (324 lines)
- 80 tier-4 skills have all 5 advanced structural sections; 0 tier-1 skills do
- 11 tier-4 skills are recommended in CLAUDE.md routing tables
- Tier-4 skill /but has 9 incoming invocations (more than 8 of the 12 tier-1 skills)

**STATUS: Not met.**
The tier boundaries are porous. Numerous tier-4 skills outperform tier-1 skills on structural quality, network centrality, or curation signals.

---

## Coverage Calculation

| Status | Count | Weight | Score |
|--------|-------|--------|-------|
| Met | 2 | 1.0 | 2.0 |
| Partially met | 3 | 0.5 | 1.5 |
| Not met | 4 | 0.0 | 0.0 |

**Raw coverage: 3.5 / 9 = 39%**

### Criticality-Weighted Coverage

| Level | Met | Partially | Not Met | Score |
|-------|-----|-----------|---------|-------|
| Critical (R3, R4, R7) | 1 | 1 | 1 | 1.5/3 = 50% |
| Important (R1, R2, R5, R8, R9) | 1 | 2 | 2 | 2.0/5 = 40% |
| Nice-to-have (R6) | 0 | 0 | 1 | 0/1 = 0% |

---

## Verdict

```
VERDICT: PARTIAL
RATIONALE: One critical requirement is not met (R3: structural quality does not follow tier order),
one critical requirement is only partially met (R4: network centrality partially follows tiers),
and overall coverage is 39%, well below the 50% threshold for even a partial pass in the
strictest sense. The tier system captures a real signal (curation and routing centrality) but
conflates it with a format-generation artifact, and the boundaries are porous.
```

---

## Gap Analysis

### GAP 1: R3 -- Structural quality inverts at tier 4
**STATUS:** Not met
**GAP:** 80 tier-4 skills have all 5 advanced structural sections (Core Principles, Depth Scaling, Failure Modes, Pre-Completion Checklist, Integration). Zero tier-1 skills have all 5. The tier system labels older-format skills as higher tier and newer-format skills as lower tier.
**IMPACT:** The tier system is partially a label for "when the skill was created" rather than "how good the skill is." Users trusting tier labels are steered away from structurally superior skills.
**FIX:** Re-evaluate the 80 tier-4 skills with full advanced structure. Promote deserving ones. Alternatively, backport advanced sections (Failure Modes, Integration, Pre-Completion Checklist) to tier-1/2 skills.
**EFFORT:** Significant

### GAP 2: R5 -- Tier 2 has almost no orchestration capability
**STATUS:** Not met
**GAP:** Tier 2 skills invoke only 1 total skill across 27 skills. Tier 4 invokes 181 total.
**IMPACT:** If tier 2 represents "important utility skills," their lack of chaining capability limits their usefulness as building blocks. Many are standalone procedures.
**FIX:** Either add chaining to tier-2 skills where appropriate, or reconsider whether standalone-ness is acceptable for tier 2 (it may be -- they may be leaf skills that are invoked, not invokers).
**EFFORT:** Moderate

### GAP 3: R6 -- Metadata completeness is worst at tier 2
**STATUS:** Not met
**GAP:** 59% of tier-2 skills have no categories, no tags, and no input_types. Tier 3 is better at 30%.
**IMPACT:** Discoverability of tier-2 skills is lower than tier-3 skills despite their supposedly higher importance.
**FIX:** Run a metadata completion pass on all tier-1/2 skills to ensure they have categories, tags, and input_types populated.
**EFFORT:** Trivial

### GAP 4: R9 -- Porous tier boundaries
**STATUS:** Not met
**GAP:** 11 tier-4 skills appear in CLAUDE.md recommendations. /but (tier 4) has 9 invoked_by references, more than most tier-1 skills. 15 tier-4 skills are longer than the tier-1 average.
**IMPACT:** The tier system under-ranks several skills that are functionally tier-1/2 by every metric.
**FIX:** Review the 11 recommended tier-4 skills (/advr, /but, /pbr, /gd, /grf, /iaw, /col, /conr, /per, /aso, /ata) for promotion to tier 2 or tier 3. Review /but specifically for tier-1 promotion given its 9 incoming invocations.
**EFFORT:** Moderate

---

## Validation Report

```
TARGET: Skill tier system (tier 1/2/3/4)
VERDICT: PARTIAL
COVERAGE: 39% (critical: 50%, important: 40%)

WHAT THE TIERS GET RIGHT:
- Tier 1 skills ARE more central in the routing network (avg 3.2 invocations vs 0.6)
- Tier 1/2 skills ARE more likely to be curated recommendations (92% / 67%)
- Tier 1 skills ARE longer on average than tier 3/4
- The tiers correctly identify which skills are entry points to the system

WHAT THE TIERS GET WRONG:
- Structural quality is INVERTED: tier 4 has 80 skills with all advanced sections; tier 1 has 0
- Tier 2 and tier 1 are indistinguishable on most metrics (length, sections, metadata)
- Tier 3 vs tier 4 boundary is arbitrary: tier 4 beats tier 3 on sections, invocations, and structural features
- 11 tier-4 skills are curated recommendations (contradiction)
- Metadata completeness is worst at tier 2 (59% incomplete)

DIAGNOSIS:
The tier system reflects TWO overlapping but conflated signals:
1. CURATION: Which skills were hand-picked as important? (Tiers 1/2 = yes, largely correct)
2. FORMAT GENERATION: Which skills were built with the latest template? (Tier 4 = newest format with most guardrails)

These signals point in opposite directions, making the combined tier label unreliable.

GAPS:
1. R3: Structural quality inverts at tier 4 -- Fix: backport advanced sections to tier 1/2 OR promote structurally complete tier-4 skills -- Effort: significant
2. R5: Tier 2 has no orchestration -- Fix: add chaining or accept leaf-node role -- Effort: moderate
3. R6: Tier 2 metadata worst -- Fix: metadata completion pass -- Effort: trivial
4. R9: Porous boundaries -- Fix: review 11 recommended tier-4 skills for promotion -- Effort: moderate

RECOMMENDED ACTIONS (by priority):
1. [Trivial] Complete metadata for all tier-1/2 skills (categories, tags, input_types)
2. [Moderate] Review and promote the 11 tier-4 skills that appear in CLAUDE.md recommendations
3. [Moderate] Decide whether tiers represent curation (hand-picked importance) or structural quality (format completeness) -- they currently conflate both and do neither well
4. [Significant] Either backport advanced sections to tier-1/2 skills, or re-tier based on structural completeness, or separate "curation" from "quality" into two independent labels
```
