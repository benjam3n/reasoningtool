# Decision Procedure — Scaling Thinking Depth

**Date**: 2026-01-31
**Input**: enabling the decision procedure skill to think for different lengths 2x 4x 8x as long as now etc or to add new skills for more dimensions and more depth

---

## Step 1: Dimension Discovery

The decision: "Should I scale existing skills to think longer (2x, 4x, 8x) or add new skills for more dimensions and depth?"

### Seed Examples

1. ARAW already scales via depth floors (1x–32x) with min claims, findings, tree levels
2. `/certainty` bypasses depth entirely — just iterates until resolved
3. `/dcp` chains 6 skills but has no depth parameter at all
4. `/iterate` has depth floors for its assessment dimensions
5. Router skills (`/claim`, `/viability`) infer depth from input complexity
6. Some skills are atomic (single-purpose) and depth doesn't apply
7. Adding a new `/dcp-deep` skill would duplicate the chain logic

### Dimensions Discovered

| # | Dimension | Values | Why It Matters |
|---|-----------|--------|----------------|
| 1 | **Scaling mechanism** | Depth floors, iteration count, skill chaining, token budget | Determines HOW the skill thinks longer |
| 2 | **What scales** | Breadth (more dimensions), depth (deeper per dimension), both | A 2x DCP could mean 2x more dimensions OR 2x deeper per dimension |
| 3 | **Where depth is applied** | Individual sub-skills, the chain itself, both | DCP chains 6 skills — do you scale each, or add more links? |
| 4 | **User interface** | Explicit depth arg, auto-inferred, always-max | How does the user request deeper thinking? |
| 5 | **Composability** | New skill vs. parameter on existing skill | Add a new `/dcp-deep` or add `depth` to `/dcp`? |
| 6 | **Which sub-skills scale** | dd, se, aex, stg, fla, pv (all 6), or a subset | Not all sub-skills benefit equally from more depth |
| 7 | **Diminishing returns point** | Where more depth stops helping | A 32x `/pv` (validation) is probably overkill |
| 8 | **Compatibility** | Works with existing depth system or creates new one | Should match the 1x/2x/4x/8x convention |

**Space size**: Large, but the dependencies collapse it significantly.

---

## Step 2: Enumerate Options per Dimension

### Dimension 1: Scaling Mechanism

| Option | How it works | Pros | Cons |
|--------|-------------|------|------|
| **A. Depth floors per sub-skill** | Each of DCP's 6 chained skills gets depth floors like ARAW | Consistent with existing system; granular control | Needs depth floors defined for dd, se, aex, stg, fla, pv |
| **B. Iteration count** | Run the chain multiple times, refining each pass | Simple; each pass catches what the last missed | Diminishing returns quickly; expensive |
| **C. Chain extension** | Add more skills to the chain at higher depths | More dimensions = more thorough | New skills need to exist and be relevant |
| **D. Hybrid** | Depth floors for sub-skills + chain extension at higher tiers | Gets both deeper AND broader | More complex to specify |

### Dimension 2: What Scales

| Option | At 2x | At 4x | At 8x |
|--------|-------|-------|-------|
| **Breadth only** | 12-18 dimensions (vs 8-15) | 18-25 dimensions | 25+ dimensions |
| **Depth only** | Same dimensions, deeper enumeration | Much deeper per dimension | Exhaustive per dimension |
| **Both** | 12+ dimensions, moderate depth | 18+ dimensions, deep | 25+ dimensions, exhaustive |

### Dimension 5: Composability

| Option | Description | Verdict |
|--------|-------------|---------|
| **New skill** (`/dcp-deep`) | Separate skill for deep decision procedures | Bad: duplicates chain logic, maintenance burden |
| **Depth parameter on `/dcp`** | `/dcp 4x choosing a college major` | Good: consistent with AR/AW/ARAW pattern |
| **Auto-inferred** | DCP detects complexity and scales itself | Risky: may under- or over-invest |

---

## Step 3: Hidden Assumptions

| # | Assumption | Status | Impact |
|---|-----------|--------|--------|
| 1 | "More thinking = better output" | **Partially true** — only if the extra thinking addresses real gaps, not padding | High — justifies the whole feature |
| 2 | "All 6 sub-skills benefit from depth" | **False** — `/pv` (validation) at 8x is mostly redundant. `/dd` and `/fla` benefit most | High — should scale selectively |
| 3 | "The depth system should be uniform" | **Questionable** — some skills scale better with breadth, others with depth | Medium — suggests per-skill tuning |
| 4 | "Users will specify depth" | **Sometimes** — power users will, but most won't | Medium — need a default |
| 5 | "Existing depth convention (1x-32x) is the right frame" | **Strong** — it's already established across 6+ skills | High — don't break convention |
| 6 | "Adding new skills is better than scaling existing ones" | **Usually false for DCP** — the chain structure is the value; adding links is only useful if the new skill addresses a real gap | High — suggests scaling > adding |

---

## Step 4: The Procedure

```
SCALING THINKING DEPTH PROCEDURE
=================================

STEP 0: What kind of depth scaling do you need?

┌─────────────────────────────────────────────────────────┐
│ I want an EXISTING skill to think longer/deeper         │
│ → Go to SECTION A                                       │
│                                                         │
│ I want to ADD NEW SKILLS for more coverage              │
│ → Go to SECTION B                                       │
│                                                         │
│ I want BOTH (deeper existing + new skills)              │
│ → Do SECTION A first, then SECTION B                    │
└─────────────────────────────────────────────────────────┘


SECTION A: SCALING AN EXISTING SKILL
=====================================

Step A1: Does the skill already have depth floors?
  - Check: Does its SKILL.md contain a depth table (1x/2x/4x/8x)?
  - YES → Go to A2 (tune the existing floors)
  - NO  → Go to A3 (add depth floors)

Step A2: Tune existing depth floors.
  For each depth tier, ask:
  a) What METRIC increases? (claims, findings, dimensions, tree levels)
  b) What's the RATIO between tiers? (should be ~1.5-2x per tier)
  c) Where are DIMINISHING RETURNS? (mark the tier where more depth
     stops producing new insight)
  → Output: Updated depth floor table. Done for this skill.

Step A3: Add depth floors to a skill that lacks them.
  a) Identify the skill's COUNTABLE OUTPUTS.
     Examples:
     - /dd: number of dimensions discovered
     - /se: number of options enumerated per dimension
     - /aex: number of assumptions surfaced
     - /stg: number of steps in procedure, number of decision points
     - /fla: number of failure modes anticipated
     - /pv: number of validation checks performed

  b) Set the 1x BASELINE.
     Run the skill once at natural depth. Count the outputs.
     That's your 1x floor.

  c) Build the depth table.
     Use this scaling formula:

     | Depth | Multiplier on countable outputs |
     |-------|---------------------------------|
     | 1x    | 1.0 (baseline)                  |
     | 2x    | 1.7                             |
     | 4x    | 2.5                             |
     | 8x    | 4.0                             |
     | 16x   | 6.0                             |
     | 32x   | 9.0                             |

     Note: NOT linear. Diminishing returns are built in.
     (8x depth ≠ 8x output. It's ~4x output at 8x thoroughness.)

  d) Define WHAT CHANGES at each tier (not just "more"):

     | Depth | What changes beyond count                    |
     |-------|----------------------------------------------|
     | 1x    | Obvious dimensions/options only               |
     | 2x    | + Non-obvious dimensions, edge cases          |
     | 4x    | + Cross-domain analogies, interaction effects |
     | 8x    | + Adversarial testing, assumption inversion   |
     | 16x   | + Second-order effects, historical parallels  |
     | 32x   | + Exhaustive enumeration, formal verification |

  e) Add to the skill's SKILL.md file.

Step A4: For COMPOUND skills (like /dcp that chain other skills):
  a) Decide which sub-skills get depth pass-through.

     For /dcp specifically:

     | Sub-skill | Scale with depth? | Rationale                          |
     |-----------|------------------|------------------------------------|
     | /dd       | YES (high value)  | More dimensions = better coverage  |
     | /se       | YES (high value)  | More options = better enumeration  |
     | /aex      | YES (medium)      | More assumptions = better safety   |
     | /stg      | PARTIAL           | More steps, but clarity > quantity  |
     | /fla      | YES (high value)  | More failure modes = more robust   |
     | /pv       | CAP AT 2x         | Validation has fast diminishing returns |

  b) Set compound depth table:

     | Depth | dd    | se    | aex   | stg   | fla   | pv    |
     |-------|-------|-------|-------|-------|-------|-------|
     | 1x    | 1x    | 1x    | 1x    | 1x    | 1x    | 1x    |
     | 2x    | 2x    | 2x    | 2x    | 1x    | 2x    | 1x    |
     | 4x    | 4x    | 4x    | 4x    | 2x    | 4x    | 2x    |
     | 8x    | 8x    | 8x    | 8x    | 4x    | 8x    | 2x    |

  c) Write the depth table into the compound skill's SKILL.md.

→ SECTION A COMPLETE. Your skill now scales with depth.


SECTION B: ADDING NEW SKILLS FOR MORE DIMENSIONS
=================================================

Step B1: Identify the GAP.
  What is the existing skill NOT covering that more depth can't fix?

  Test: "If I ran the current skill at 32x, would it cover this?"
  - YES → You don't need a new skill. Go back to Section A.
  - NO  → There's a genuine gap. Continue.

Step B2: Name the gap precisely.
  Common gaps in compound skills:

  | Gap | What's missing | Candidate new sub-skill |
  |-----|---------------|------------------------|
  | Stakeholder perspective | Procedure only considers one viewpoint | Add /pre (preference elicitation) to chain |
  | Temporal dynamics | Procedure is static, decision changes over time | Add /snp (scenario planning) to chain |
  | Second-order effects | Procedure misses downstream consequences | Add /sya (systems analysis) to chain |
  | Competitive context | Procedure ignores what others are doing | Add /cma (competitive analysis) to chain |
  | Value alignment | Procedure optimizes wrong objective | Add /ve (value elicitation) to chain |
  | Implementation risk | Procedure is correct but hard to execute | Add /fla (already in DCP) or /exc to chain |

Step B3: Determine WHERE in the chain the new skill goes.
  a) Does it need information from an earlier step? → Place after that step.
  b) Does it produce information a later step needs? → Place before that step.
  c) Is it independent? → Place in parallel (run alongside existing steps).

Step B4: Decide if this is a PERMANENT addition or DEPTH-GATED.
  - Always valuable → Add to base chain (runs at all depths)
  - Only valuable at high depth → Gate it:
    "If depth >= 4x, also run [new skill] between Step N and Step N+1"

Step B5: Update the compound skill's SKILL.md.
  Add the new link to the chain definition.
  Update the depth table if depth-gated.

→ SECTION B COMPLETE. Your skill now covers more dimensions.


QUICK REFERENCE CARDS
=====================

CARD 1: DCP Depth Floors (Proposed)

| Depth | Dimensions | Options/dim | Assumptions | Failure modes | Procedure steps |
|-------|-----------|-------------|-------------|---------------|----------------|
| 1x    | 8-10      | 3-5         | 5-8         | 5-8           | 15-25          |
| 2x    | 10-15     | 5-8         | 8-12        | 8-12          | 20-35          |
| 4x    | 15-20     | 8-12        | 12-18       | 12-20         | 30-50          |
| 8x    | 20-25     | 12-15       | 18-25       | 20-30         | 40-70          |

CARD 2: When to Scale vs. When to Add

| Signal | Action |
|--------|--------|
| Output feels thin/shallow | Scale depth (Section A) |
| Output feels thorough but MISSING something | Add skill (Section B) |
| Output is good but user wants more | Scale depth first, add only if gaps remain |
| Output has wrong conclusions | Neither — fix the logic, not the depth |

CARD 3: The Scaling Formula

  Output at Nx ≈ Output at 1x × (N^0.6)

  This means:
  - 2x depth → ~1.5x output
  - 4x depth → ~2.3x output
  - 8x depth → ~3.5x output
  - 16x depth → ~5.3x output

  Depth has diminishing returns BY DESIGN.
  The extra effort goes into harder-to-find items, not more items.
```

---

## Step 5: Failure Modes

| # | Failure Mode | How to Recognize | What to Do Instead |
|---|-------------|-----------------|-------------------|
| 1 | **Padding** — more depth produces more words but not more insight | Findings at 8x are rephrased versions of findings at 2x | Quality gate: each depth tier must produce findings NOT PRESENT at the tier below |
| 2 | **Uniform scaling** — treating all sub-skills equally | Validation (/pv) at 8x takes as long as dimension discovery at 8x but adds nothing | Use the per-sub-skill depth table from Step A4 |
| 3 | **Adding skills when scaling suffices** | You created a new skill but /se at 8x would have covered the same ground | Always test "would 32x of the existing chain cover this?" before adding |
| 4 | **Depth without direction** — "think more" without "about what" | 8x run wanders into irrelevant territory | Each depth tier should specify WHAT NEW TYPES OF THINKING are added (see Step A3d) |
| 5 | **Breaking the convention** — inventing a new depth system | Your skill uses "levels 1-5" while everything else uses 1x/2x/4x/8x | Always use the established 1x/2x/4x/8x/16x/32x tiers |
| 6 | **Forgetting the default** — no depth specified = undefined behavior | User types `/dcp choosing a car` with no depth flag | Default to 2x (consistent with AR/AW/ARAW default) |

---

## Step 6: Validation

| Check | Pass? |
|-------|-------|
| Can someone with no GOSM expertise follow Section A? | Yes — each step is concrete with examples |
| Are all decision points binary or explicit choice? | Yes — A1 is yes/no, Step 0 is 3-way |
| Does every path lead to a concrete output? | Yes — depth table written to SKILL.md |
| Are there dead ends or loops? | No — Section A and B both terminate |
| Is jargon defined? | Depth floors, MECE, compound skills all explained inline or by example |
| Are there worked examples? | The DCP-specific tables serve as worked examples throughout |

---

## COMMON MISTAKES

1. **Thinking 8x means 8x longer output.** It doesn't. 8x means ~4x more findings at ~8x more thoroughness. The extra effort finds harder-to-find things.
2. **Scaling the wrong sub-skill.** Not all links in a chain benefit equally. Validate and proofread don't scale well. Discovery and enumeration do.
3. **Adding new skills as a substitute for depth.** If the existing chain at high depth would cover it, you don't need a new skill.
4. **Not setting a default depth.** Every skill needs a default. Use 2x.
5. **Making depth floors targets instead of floors.** If you naturally produce 20 dimensions at 4x, don't stop at 15 just because the floor says 15.

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **The skill is atomic and can't meaningfully scale** (e.g., `/sf` — save file). Not everything needs depth.
- **The skill is already `/certainty`** — which is "run until done" and doesn't use tiers.
- **You're building a fundamentally new type of skill** that doesn't fit the chain pattern. In that case, design depth from scratch using the principles here but not the exact mechanics.

---

## RECOMMENDATION

**Scale existing skills (Section A) first.** Specifically:

1. Add depth floors to `/dcp` using the compound depth table from Step A4
2. Add depth floors to `/dd`, `/se`, `/aex`, `/fla` individually (they currently lack them)
3. Don't add new skills to the chain unless a specific gap is identified at 8x that can't be covered by existing sub-skills at higher depth
4. Default depth for `/dcp`: **2x**

The system already has a well-established depth convention. The gap isn't the convention — it's that `/dcp` and its sub-skills don't participate in it yet.
