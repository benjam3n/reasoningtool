# DCP — When to Reorganize

**Date**: 2026-01-31
**Input**: When to reorganize a group (from /analyze 8x optimal group organization → /dcp)

---

# WHEN TO REORGANIZE — DECISION PROCEDURE

## STEP 0: CLASSIFICATION — IS THIS ACTUALLY A STRUCTURE PROBLEM?

**0A.** Write down the specific pain in one sentence.

**0B.** Did this pain exist 6 months ago?
- YES → Go to 0C
- NO → What changed? That's likely your root cause. → Section A.

**0C.** Have we tried a non-structural fix and it failed?
- YES → Section B
- NO → STOP. Try a non-structural fix first. → Section A.

---

## SECTION A: TRIAGE — STRUCTURE vs. PROCESS vs. PEOPLE

### A1. The Friction Locator

Ask 5 people who experience the pain:
1. "When this problem happens, who do you have to talk to that you shouldn't need to?"
2. "When this problem happens, what information do you lack that you should have?"
3. "When this problem happens, who is supposed to make the decision but doesn't?"

### A2. Read the pattern:

| Most answers point to... | Diagnosis | Go to... |
|---|---|---|
| Too many people / wrong people | STRUCTURE problem | Section B |
| Missing information | PROCESS problem | Section A3 |
| Person X is the bottleneck | PEOPLE problem | Section A4 |
| Mixed across all three | STRUCTURE problem | Section B |

### A3. Process Fix Path
- Information gap → shared dashboard/channel/sync. Trial 30 days.
- Handoff gap → written handoff protocol. Trial 30 days.
- Prioritization gap → single prioritization meeting. Trial 30 days.

### A4. People Fix Path
- Bottleneck person → reduce scope, add deputy, or replace.
- Conflict source → feedback with deadline, role change, or exit.
- Empty role → hire or promote.

---

## SECTION B: CONFIRMING THE NEED FOR REORGANIZATION

### The Five Structural Stress Signals (score 0 or 1 each)

1. **Coordination Overhead >30%** — median IC time in meetings/waiting/chasing
2. **Duplicate or Orphaned Work** — two teams built same thing, or important work nobody owns
3. **Decision Rights Unclear** — can't identify decision-maker for 2/3 recent decisions in 60 seconds
4. **Structure Doesn't Match Work** — daily collaborators report to different parts of the org
5. **Growth/Mission Outpaced Structure** — 50%+ larger or meaningfully different mission since structure was set

| Score | Recommendation |
|---|---|
| 0-1 | Do not reorganize. Return to Section A. |
| 2-3 | Reorganization plausible. Proceed, scope narrowly. |
| 4-5 | Reorganization strongly indicated. Proceed. |

---

## SECTION C: SCOPING THE REORGANIZATION

### C1. Identify the Structural Joint That Is Failing
Problems live at boundaries between groups, not inside groups.

### C2. Classify the Joint Failure

| Type | Description | Fix |
|---|---|---|
| Split | One group too large | Split into two |
| Merge | Two groups should be one | Merge |
| Rebalance | Work/people in wrong group | Move people or responsibilities |
| Layer | Need new coordination level (or remove one) | Add/remove management layer |

### C3. Define the Minimum Viable Reorganization
Change fewest reporting lines, move fewest people, keep working sub-teams intact. If >30% of people affected, pause and reconsider.

---

## SECTION D: DESIGNING THE NEW STRUCTURE

### D1. Choose an Organizing Principle

| Axis | Best when... | Worst when... |
|---|---|---|
| Function | Need deep specialization | Speed matters more than depth |
| Product | Products need autonomous teams | Products share heavy infrastructure |
| Customer | Segments have very different needs | Segments share the same product |
| Process | Workflow is sequential | Work doesn't flow sequentially |
| Geography | Regulatory/language/TZ differences dominate | Work is fully remote |

### D2. Define Decision Rights (OWN / ADVISE / ESCALATE / NO ROLE)
### D3. Draw the Collaboration Map

---

## SECTION E: EXECUTING THE REORGANIZATION

**E1. Pre-Announce (Week -2):** Tell every affected person individually.
**E2. Implement (Week 0):** Update all systems, hold all-hands, distribute decision rights doc.
**E3. Stabilize (Weeks 1-4):** Daily check-ins week 1, address concerns week 2, review collaboration map week 3, re-run stress signals week 4.
**E4. Evaluate (Week 8):** Re-interview same 5 people with same questions.

---

## SECTION F: THE REORG DID NOT WORK

**F1.** Wrong diagnosis? → Undo, go to Section A.
**F2.** Wrong scope? → Keep structure, address next joint.
**F3.** Wrong execution? → Fix execution, not structure.
**F4.** Situation changed? → Restart from Step 0.

---

## QUICK REFERENCE CARDS

### Card 1: "Should I Reorg?" (30-Second Version)
1. Can you name the specific pain?
2. Have you tried a non-structural fix?
3. Do at least 2 of 5 Stress Signals fire?
4. Can you scope to <30% of people?
5. Can you write one sentence explaining what it fixes?

### Card 2: "Is This a Reorg or a Process Fix?"

| Symptom | Process Fix | Reorg |
|---|---|---|
| Slow delivery | Kanban, reduce WIP, cut meetings | Only if structural waiting |
| Duplicate work | Shared intake/registry | Merge groups |
| Unclear ownership | RACI/decision doc | Only if charters overlap |
| Communication gaps | Sync meeting, liaison role | Only if 3+ management hops apart |
| Manager bottleneck | Deputy, reduce span | Split if span >10-12 |
| High attrition | Compensation, management, workload | Almost never fixed by reorg |

---

## COMMON MISTAKES

1. Reorganizing when the problem is a bad manager
2. Reorganizing too frequently (<12 months since last)
3. Reorganizing to solve a strategy problem
4. Copying another company's structure
5. Reorganizing to avoid a hard conversation
6. Reorganizing everything at once
7. Announcing without individual conversations

---

## WHEN TO OVERRIDE

1. Existential crisis (90-day survival)
2. CEO mandate with clear strategic rationale
3. Regulatory/legal requirement
4. M&A integration

---

## WORKED EXAMPLES

### Example 1: "Engineering is too slow"
Stress signals: 3/5. Failing joint: Platform↔Payments. Type: Rebalance. Fix: Move 4 engineers to new Payments squad. Result: coordination overhead 40%→20%, lead time 12→5 weeks.

### Example 2: "Teams keep stepping on each other"
Recent change (Growth team created 4 months ago). Process fix: weekly intake meeting + shared Notion board. Result: conflicts 3/month→0. No reorg needed.

### Example 3: "Nobody accountable for customer experience"
Stress signals: 5/5. Missing team. Fix: Create CX team of 5 from Product/Marketing/Support, hire Head of CX. Result: clear ownership, NPS stabilizing.
