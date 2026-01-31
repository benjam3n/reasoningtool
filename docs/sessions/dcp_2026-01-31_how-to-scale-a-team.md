# DCP — How to Scale a Team

**Date**: 2026-01-31
**Input**: How to scale a team — when and how to split, add layers, or restructure as a group grows (from /analyze 8x optimal group organization → /dcp)

---

# HOW TO SCALE A TEAM — DECISION PROCEDURE

## STEP 0: CLASSIFY YOUR CURRENT SITUATION

**Q1. Current team size?** (A) 1-5, (B) 6-9, (C) 10-15, (D) 16-30, (E) 31-60, (F) 61+
**Q2. Growth rate?** (S) Stable, (G) Gradual 1-2/quarter, (R) Rapid 3+/quarter or doubling in 12 months
**Q3. Work type?** (X) Exploration, (Y) Execution, (Z) Mixed
**Q4. Colocated?** (L) Same location/TZ band, (D) Distributed 4+ hours apart
**Q5. Single context holder?** (1) Yes — one bottleneck, (0) No — shared

---

## SECTION A: DO YOU ACTUALLY NEED TO SCALE?

### A1: List top 3 bottlenecks (be specific)

### A2: Would adding a person fix this within 90 days?
- YES for 2+ of 3 → Proceed to Section B
- NO for 2+ → STOP. Problem is not headcount. Fix coordination, tooling, or priorities.

### A3: Brooks's Law check
Mid-project with hard deadline <3 months away? → Do NOT add people. Reduce scope or extend deadline.

---

## SECTION B: ROUTING BY SIZE

| Current size | Go to |
|---|---|
| 1-5 | Section C: Simple Growth |
| 6-9 | Section D: First Split Decision |
| 10-15 | Section E: Mandatory Restructure |
| 16-30 | Section F: Multi-Team Architecture |
| 31-60 | Section G: Federation and Hierarchy |
| 61+ | Section H: Organization Design |

---

## SECTION C: SIMPLE GROWTH (1-5)

- Identify missing capability: (a) need more hours → generalist, (b) need new skill → specialist, (c) leader overloaded → ops/PM hire
- Hire one person at a time. Wait for full ramp before next hire.
- At 6 people, read Section D.

---

## SECTION D: THE FIRST SPLIT DECISION (6-9)

### Warning Signs (check all that apply):
- [ ] Meetings run over or need follow-ups
- [ ] People duplicate work unknowingly
- [ ] Team lead spends >50% time coordinating
- [ ] Decisions stall — "we need to check with everyone"
- [ ] Natural subgroups have formed

**0-1 checked:** Stay unified. Re-evaluate quarterly.
**2-3 checked:** Prepare for split.
**4-5 checked:** Split immediately.

### Split Pattern:
- Can work divide into 80%+ independent areas? → **Pod Split** (two teams of 3-5)
- Cannot? → **Rotating Pair Model** (defer split, re-evaluate monthly)

### Pod Split Execution:
1. Define ownership boundaries (one sentence per pod)
2. Assign people (each pod needs: 1 senior decision-maker, 1 full-lifecycle person, 3-5 total)
3. Define interface (shared resources, conflict resolution, meeting cadence)
4. Designate pod leads (50%+ time on direct work)

### Health check at 2, 6, and 12 weeks:
- Can you complete 80%+ of work without the other pod?
- Do you know what the other pod is doing?
- Is the pod lead spending <30% on coordination?

---

## SECTION E: MANDATORY RESTRUCTURE (10-15)

- If not already split into pods, do so now (Section D process)
- Add dedicated coordinator if 3+ pods or 2 pods sharing >30% work
- Standardize pod interfaces: written charter, visible work board, escalation path

---

## SECTION F: MULTI-TEAM ARCHITECTURE (16-30)

### Structure:
```
        [Overall Lead]
       /       |       \
   [Group A]  [Group B]  [Group C]
    /   \      /   \
  Pod1  Pod2  Pod3  Pod4
```

- Groups = 2-3 pods sharing a domain. Group lead manages pod leads, owns roadmap.
- Overall lead manages group leads, owns strategy and hiring.
- Define decision rights at each level explicitly.
- Choose coordination model based on work type (Execution/Exploration/Mixed).
- For distributed teams: align pods to timezone bands (4+ hours overlap minimum).

---

## SECTION G: FEDERATION AND HIERARCHY (31-60)

- Verify: 3-5 group leads, 8-15 pods, 1 overall lead (or 2-3 directors if >5 groups)
- Federated decision-making: published decision rights matrix, group autonomy within interfaces
- Alignment: quarterly planning, monthly metrics, weekly leadership sync
- Enabling functions: recruiting coordinator (if 5+ hires/quarter), structured onboarding, internal comms

---

## SECTION H: ORGANIZATION DESIGN (61+)

### Three models:
| Model | Organize by | Best when | Con |
|---|---|---|---|
| Functional | Skill type | Deep specialization needed | Slow cross-functional delivery |
| Divisional | Product/segment | Products largely independent | Duplication of skills |
| Matrix | Both | Need both depth and speed | Two bosses, requires mature management |

If unsure, start Divisional — simplest to operate and course-correct.

Apply Sections E-G recursively within each division/function.

---

## QUICK REFERENCE CARDS

### Card 1: Team Size Cheat Sheet

| Size | Structure | Key Action |
|------|-----------|------------|
| 1-5 | Flat | Hire one at a time |
| 6-9 | 1 team or 2 pods | Watch for split signals |
| 10-15 | 2-3 pods + coordinator | Formalize charters |
| 16-30 | 4-6 pods in 2-3 groups | Add group leads, decision rights |
| 31-60 | Federated groups | Autonomy + alignment |
| 61+ | Topology choice | Functional/Divisional/Matrix |

### Card 2: When to Split
Split when 2+ true: size >5, meetings overflow, work 80%+ separable, lead >50% coordinating, subgroups formed.

### Card 3: When to Add a Management Layer
- Lead has >7 direct reports
- Cross-pod coordination >10 hours/week total
- Decisions stall waiting for one person
- 3+ pods need alignment

### Card 4: Ideal Pod Composition
3-5 people, 1 independent decision-maker, 1 full-lifecycle person, pod lead, written charter.

---

## COMMON MISTAKES

1. **Hiring into the pain** — new hires slow team 2-4 months before helping. Hire one at a time.
2. **Splitting by function too early** — split by mission/product, not frontend/backend.
3. **Adding hierarchy before needed** — use pod leads (70%+ IC time) before full-time managers.
4. **Not splitting when signals scream** — the team is already siloed informally.
5. **Reorganizing too frequently** — commit to structure for 6+ months.
6. **Ignoring single point of failure** — ensure 2+ people can make any critical decision.

---

## WHEN TO OVERRIDE

1. Crisis mode → collapse to tiger team, re-establish after
2. Acquisition/merger → run independently 2-3 months, then design combined structure
3. Regulated environment → layer compliance requirements on top
4. Pure research/creative → studio model instead of pods
5. Contracting → reverse the steps (merge pods, flatten, consolidate)

---

## WORKED EXAMPLES

### Example 1: Startup, 7 Engineers, Growing Fast
B-R-Y-L-1. CTO bottleneck. Split into API pod (4) and Frontend pod (3). CTO transfers context over 4 weeks. Hire into smaller pod first.

### Example 2: Cross-Functional, 22 People, Distributed
D-G-Z-D-1. Create 4 cross-functional pods, 2 groups. Director manages 2 group leads instead of 22 individuals. Align pods to timezone bands.

### Example 3: Rapidly Scaling, 40→80 in 12 Months
E-R-Y-L-0. Staged growth: hire 10 → split pods → hire 10 → create new group → repeat. Never let new hires outnumber veterans in a pod. Split before overcrowded.

---

## FINAL CHECKLIST

- [ ] Problem is headcount, not coordination
- [ ] Not adding mid-crisis with near deadline
- [ ] Pod sizes 3-5
- [ ] Each pod delivers end-to-end (80%+)
- [ ] Written charters and visible work boards
- [ ] Decision rights findable in <60 seconds
- [ ] No single bottleneck person
- [ ] Committed to structure for 6+ months
- [ ] Hiring one at a time per pod
- [ ] 2+ people for every critical decision
