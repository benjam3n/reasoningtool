# DCP — Generating Decision Procedure Inputs

**Date**: 2026-01-31
**Input**: Coming up with new decision procedure inputs

---

## Step 1: Decision Dimensions (`/dd`)

### Dimension 1: Recurrence
**Why it matters**: DCPs are only valuable for decisions made repeatedly. A one-time decision doesn't justify building a procedure.
- Made once in a lifetime
- Made a few times per life
- Made regularly (monthly/yearly)
- Made constantly (daily/weekly)

### Dimension 2: Stakes
**Why it matters**: Low-stakes decisions don't need procedures — just pick and move. High-stakes decisions justify the investment.
- Trivial (wrong answer costs minutes)
- Moderate (wrong answer costs days or hundreds of dollars)
- High (wrong answer costs months or thousands)
- Critical (wrong answer costs years, careers, or life-altering money)

### Dimension 3: Expertise Gap
**Why it matters**: If most people already make this decision well, a DCP adds no value. DCPs shine where expertise is rare or expensive.
- Most people decide well intuitively
- Expertise helps but isn't essential
- Expertise dramatically changes outcomes
- Without expertise, most people get it wrong

### Dimension 4: Decision Complexity
**Why it matters**: Simple binary decisions don't need procedures. The sweet spot is decisions with multiple interacting dimensions that humans can't hold in their heads simultaneously.
- Binary (yes/no)
- Few options, clear tradeoffs
- Many options, interacting tradeoffs
- Combinatorial (options × dimensions × constraints)

### Dimension 5: Mechanizability
**Why it matters**: Some decisions are fundamentally judgment calls that resist proceduralization. Good DCP targets can be broken into concrete, observable steps.
- Requires taste/intuition that can't be articulated
- Mostly mechanizable with some judgment points
- Fully mechanizable with clear inputs → outputs
- Already partially proceduralized (checklists exist but are incomplete)

### Dimension 6: Information Availability
**Why it matters**: A procedure that requires information the user can't access is useless.
- Required information is hidden or expensive
- Information exists but requires effort to find
- Information is freely available online
- User already has the information (it's about their own situation)

### Dimension 7: Consequence Asymmetry
**Why it matters**: The best DCP targets have asymmetric outcomes — a good decision and a bad decision produce very different results, and most people default to the bad one.
- Good and bad decisions have similar outcomes
- Moderate difference between good and bad
- Large difference — good decisions are 2-5x better
- Extreme — good decisions are 10x+ better or avoid catastrophe

### Dimension 8: Domain Breadth
**Why it matters**: Too narrow = only useful to a handful of people. Too broad = can't be specific enough to be actionable.
- Niche (< 1,000 people face this decision)
- Specialized (thousands to tens of thousands)
- Common (hundreds of thousands)
- Universal (millions+ face this decision)

### Dimension 9: Current Resource Quality
**Why it matters**: If excellent guides already exist, a DCP adds less value. If the current advice is vague platitudes, a DCP fills a real gap.
- Excellent step-by-step guides exist
- Good advice exists but isn't procedural
- Advice exists but is vague, contradictory, or self-serving
- Almost no reliable guidance available

### Dimension 10: Decomposability
**Why it matters**: Can the decision be broken into a sequence of smaller, verifiable sub-decisions? If not, it resists proceduralization.
- Monolithic — must be decided all at once
- Partially decomposable (2-3 sub-decisions)
- Highly decomposable (5-10 clear sub-decisions)
- Naturally sequential (obvious step order)

---

## Step 2: Option Space (`/se`)

### The Scoring Matrix

Each candidate DCP input gets scored on a 1-3 scale per dimension:

| Dimension | Score 1 (Poor fit) | Score 2 (Decent) | Score 3 (Ideal) |
|---|---|---|---|
| Recurrence | Once in a lifetime | Few times per life | Regularly/constantly |
| Stakes | Trivial | Moderate | High or critical |
| Expertise Gap | Most decide well | Expertise helps | Most get it wrong |
| Complexity | Binary | Few options | Many interacting |
| Mechanizable | Pure judgment | Mostly mechanizable | Fully mechanizable |
| Info Available | Hidden/expensive | Findable | Freely available |
| Asymmetry | Similar outcomes | Moderate gap | 10x+ |
| Breadth | < 1,000 people | Thousands | Millions |
| Poor Resources | Great guides exist | Vague advice | No reliable guidance |
| Decomposable | Monolithic | Partially | Sequential |

**Minimum viable score**: 20/30
**Sweet spot**: 24-30/30

### Interaction Rules
- If Recurrence = 1 AND Stakes < 3: **reject**
- If Mechanizable = 1: **reject**
- If Info Available = 1 AND unchangeable: **reject**
- If Resource Quality = 1: **deprioritize**

---

## Step 3: Hidden Assumptions (`/aex`)

**A1: "Any decision can become a DCP"**
Reality: Some decisions are fundamentally about taste, values, or identity. These need `/ve` or `/wt`, not `/dcp`.

**A2: "More specific = better DCP topic"**
Reality: Sweet spot exists. "How to choose a database for a CRUD app" = too narrow. "How to make technology decisions" = too broad. "How to choose a tech stack for a new software project" = right.

**A3: "Professional decisions are the best targets"**
Reality: Personal decisions (health, finance, housing) often have higher stakes, worse guidance, and larger audiences.

**A4: "The decision must be interesting to generate"**
Reality: The most useful DCPs are for boring, mundane decisions that people make badly — choosing insurance, evaluating a used car, deciding repair vs. replace.

**A5: "I should generate DCPs for what I know about"**
Reality: Best DCPs are for decisions where you lack expertise — forces you to build a procedure that works without expertise.

**A6: "One DCP per topic"**
Reality: Broad topics need multiple DCPs. Generate specific decision moments, not topic areas.

---

## Step 4: The Procedure (`/stg`)

```
GENERATING DCP INPUTS PROCEDURE
================================

WHO THIS IS FOR: Anyone who wants to find good topics for the /dcp skill.
WHAT YOU'LL GET: A ranked list of specific, high-value decision procedure targets.

═══════════════════════════════════════════════
STEP 0: CHOOSE YOUR SOURCE
═══════════════════════════════════════════════

Where are you looking for DCP ideas?

  → My own life/experience     → Go to SECTION A
  → A specific domain/industry → Go to SECTION B
  → Brainstorming broadly      → Go to SECTION C
  → Improving an existing DCP  → Go to SECTION D

═══════════════════════════════════════════════
SECTION A: MINING YOUR OWN EXPERIENCE
═══════════════════════════════════════════════

Step A1: List your last 20 decisions.
  Open a blank document. Write down the last 20 decisions you
  made that took more than 5 minutes of thought. Include:
  - What you were deciding
  - What you chose
  - Whether you're satisfied with the outcome

  EXAMPLES of what counts:
  ✓ "Whether to accept a job offer"
  ✓ "Which laptop to buy"
  ✓ "Whether to renew my lease or move"
  ✓ "Which health insurance plan to pick"
  ✓ "Whether to hire candidate A or B"

  EXAMPLES of what doesn't count:
  ✗ "What to eat for lunch" (too trivial)
  ✗ "Whether to break up" (too values-dependent)
  ✗ "How to feel about the news" (not a decision)

  Can't think of 20? Check these prompts:
  □ Last thing you bought over $100
  □ Last time you chose between service providers
  □ Last time you changed a subscription or contract
  □ Last time you made a career/work decision
  □ Last time you made a health decision
  □ Last time you chose how to spend a weekend
  □ Last time you had to pick a tool, app, or platform

Step A2: Circle the regrets and the struggles.
  Mark each decision with one of:
  [R] = I regret this or got it wrong
  [S] = This was really hard to decide
  [E] = This was easy and I'm satisfied

  Count your R's and S's. Those are your candidates.

Step A3: Generalize each candidate.
  For each [R] or [S] decision, rewrite it as a CATEGORY:

  SPECIFIC: "I chose the wrong health insurance plan"
  GENERAL: "Choosing a health insurance plan"

  SPECIFIC: "I spent too long picking a project management tool"
  GENERAL: "Choosing software tools for a specific workflow"

  RULE: The generalized version should describe a decision that
  THOUSANDS of people face, not just you.

  If you can't generalize it → cross it out (it's too personal
  for a DCP).

→ Go to SECTION E (Scoring).

═══════════════════════════════════════════════
SECTION B: MINING A SPECIFIC DOMAIN
═══════════════════════════════════════════════

Step B1: Name the domain.
  Write it here: _______________

Step B2: Map the decision lifecycle.
  Every domain has a lifecycle. List the STAGES someone goes
  through in this domain:

  EXAMPLE (Real Estate):
  1. Decide to invest → 2. Choose market → 3. Find property →
  4. Evaluate deal → 5. Finance purchase → 6. Close deal →
  7. Renovate/prepare → 8. Find tenants → 9. Manage property →
  10. Decide to sell/hold/refinance

  EXAMPLE (Software Engineering):
  1. Define requirements → 2. Choose architecture → 3. Choose
  tech stack → 4. Design system → 5. Build MVP → 6. Test →
  7. Deploy → 8. Monitor → 9. Scale → 10. Maintain

  Write YOUR domain's lifecycle stages (aim for 6-12).

Step B3: Extract decisions from each stage.
  For each stage, list the specific DECISIONS someone must make.
  Not tasks. Not actions. DECISIONS — moments where you choose
  between options.

  Do this for EVERY stage. Aim for 3-5 decisions per stage.

Step B4: Filter for DCP suitability.
  For each decision from B3, ask:
  □ Is this made by more than 1,000 people per year? (if no: cut)
  □ Can an expert consistently get a better outcome than a
    novice? (if no: cut — it's luck or taste, not skill)
  □ Can you describe the RIGHT answer process in concrete steps?
    (if no: cut — it's not mechanizable)

  Remaining items are your candidates.

→ Go to SECTION E (Scoring).

═══════════════════════════════════════════════
SECTION C: BROAD BRAINSTORMING
═══════════════════════════════════════════════

Step C1: Use the Universal Decision Categories.
  Scan this list and write down ONE specific decision for each
  category that you've seen people struggle with:

  FINANCIAL DECISIONS
  □ Major purchase decisions (house, car, appliance)
  □ Insurance selection (health, auto, home, life)
  □ Investment allocation
  □ Debt management (which to pay off, refinance, consolidate)
  □ Service provider selection (bank, accountant, lawyer)

  CAREER DECISIONS
  □ Job offer evaluation
  □ Career pivot / transition
  □ Skill investment (what to learn next)
  □ Freelance/contract pricing
  □ Whether to start a business

  TECHNOLOGY DECISIONS
  □ Tool/platform selection
  □ Architecture/design decisions
  □ Build vs. buy
  □ When to migrate/upgrade
  □ Security/privacy tradeoffs

  HEALTH DECISIONS
  □ Treatment option selection
  □ Provider selection (doctor, therapist, specialist)
  □ Lifestyle change evaluation (diet, exercise, sleep)
  □ Supplement/medication decisions

  HOUSING DECISIONS
  □ Rent vs. buy
  □ Location selection
  □ Renovation decisions (DIY vs. hire, which projects)
  □ Roommate/living arrangement decisions

  EDUCATION DECISIONS
  □ School/program selection
  □ Major/specialization selection
  □ Self-study vs. formal education
  □ Continuing education choices

  RELATIONSHIP DECISIONS
  □ Hiring decisions
  □ Partnership/collaboration evaluation
  □ When to end a professional relationship
  □ Delegation decisions

  LEGAL/ADMINISTRATIVE
  □ Entity structure selection (LLC, S-corp, etc.)
  □ Contract evaluation
  □ Dispute resolution approach
  □ Regulatory compliance choices

Step C2: Pick your top 10 from C1.
  Select the 10 that feel most universally painful.

→ Go to SECTION E (Scoring).

═══════════════════════════════════════════════
SECTION D: IMPROVING AN EXISTING DCP
═══════════════════════════════════════════════

Step D1: Identify the existing DCP's weakest section.
  Read through the DCP. Find the section where:
  "A novice would get stuck here" or "This is too vague."

Step D2: Is the weak section actually a SUB-DECISION?
  → YES: That sub-decision is your new DCP input. Extract it
    and run /dcp on it separately. Then link back.
  → NO: The existing DCP needs /pv and /rf, not a new DCP.

Step D3: Check scope.
  Does the existing DCP try to cover too many decision types?
  → YES: Split it. Each decision type becomes a new DCP input.
  → NO: The DCP is appropriately scoped.

→ Go to SECTION E (Scoring).

═══════════════════════════════════════════════
SECTION E: SCORING & RANKING
═══════════════════════════════════════════════

Step E1: Score each candidate.
  For every candidate, fill in this table:

  | Candidate | Rec | Stk | Exp | Cmx | Mch | Inf | Asy | Brd | Res | Dec | TOTAL |

  SCORING GUIDE:
  - Recurrence: 1 = once ever, 2 = few times, 3 = regularly
  - Stakes: 1 = trivial, 2 = moderate, 3 = high/critical
  - Expertise Gap: 1 = most decide well, 2 = helps, 3 = most wrong
  - Complexity: 1 = binary, 2 = few options, 3 = many interacting
  - Mechanizable: 1 = pure judgment, 2 = mostly, 3 = fully
  - Info Available: 1 = hidden, 2 = findable, 3 = freely available
  - Asymmetry: 1 = similar outcomes, 2 = moderate, 3 = 10x+
  - Breadth: 1 = < 1,000 people, 2 = thousands, 3 = millions
  - Poor Resources: 1 = great guides, 2 = vague advice, 3 = none
  - Decomposable: 1 = monolithic, 2 = partially, 3 = sequential

Step E2: Apply kill criteria.
  Cross out any candidate where:
  □ Recurrence = 1 AND Stakes < 3
  □ Mechanizable = 1
  □ Info Available = 1
  □ Total < 20

Step E3: Rank remaining candidates by total score.
  Your top 3-5 are your best DCP inputs.

Step E4: Final phrasing check.
  Rewrite each as:
  "[Deciding/Choosing/Evaluating] [specific thing] [for whom]
  [in what context]"

  □ Specific enough that two people would build similar procedures
  □ Broad enough that thousands face this exact decision
  □ Action-oriented (starts with a verb)

Step E5: Output your ranked list.
  RANK 1: [Decision statement] (Score: X/30)
  RANK 2: [Decision statement] (Score: X/30)
  [...]

  These are ready to feed into /dcp.

→ PROCEDURE COMPLETE
```

---

## Step 5: Failure Modes (`/fla`)

### FAILURE MODE 1: "Too Abstract"
**Recognize**: Candidate sounds like a college course title.
**Fix**: Add specificity until it describes a single decision moment.

### FAILURE MODE 2: "Too Personal"
**Recognize**: Decision depends on values, identity, or taste.
**Fix**: If core question is "what do I want?" not "how do I choose?" — route to `/ve` or `/wt`.

### FAILURE MODE 3: "Already Solved"
**Recognize**: Scored Resource Quality high, but excellent guide already exists.
**Fix**: Search "[decision] step by step guide" before building. Don't duplicate.

### FAILURE MODE 4: "Scoring Inflation"
**Recognize**: Every dimension scored 3.
**Fix**: Write one-sentence justification for each 3. If you hedge, downgrade to 2.

### FAILURE MODE 5: "Generating for Yourself Instead of Others"
**Recognize**: All candidates are decisions YOU face.
**Fix**: Ask: "Would my parent use this? A 22-year-old? Someone in a different industry?" Add 2+ candidates for unlike audiences.

### FAILURE MODE 6: "Confusing Topics with Decisions"
**Recognize**: Candidates are nouns not verbs.
**Fix**: Every DCP input must describe a CHOICE POINT. Rewrite until it starts with a decision verb.

---

## Step 6: Validation (`/pv`)

All steps verified as executable by non-experts. All paths terminate at Section E or retry loops with clear exit conditions. No dead ends or infinite loops.

---

## QUICK REFERENCE CARDS

### Card 1: The Ideal DCP Target
```
Recurring + High stakes + Most people get it wrong +
Multiple interacting options + Can be proceduralized +
Information is available + No good guide exists
```

### Card 2: Instant Kill Criteria
```
REJECT if any are true:
- One-time AND low-stakes
- Requires pure judgment/taste
- Required info is inaccessible
- Excellent step-by-step guide already exists
- Core question is "what do I want?" not "how do I choose?"
```

### Card 3: The Phrasing Template
```
"[Choosing/Deciding/Evaluating] [specific thing]
 [for whom] [in what context]"
```

---

## COMMON MISTAKES

1. **Generating topics instead of decisions** — "Real estate" is a topic. "Choosing which investment property to buy" is a decision.
2. **Going too broad** — "Making better life decisions" can't be proceduralized.
3. **Going too narrow** — "Choosing between PostgreSQL and MySQL for Django < 1000 users" — answer is just "use PostgreSQL."
4. **Ignoring existing resources** — Don't duplicate NerdWallet's credit card comparison.
5. **Prioritizing interesting over useful** — Boring decisions with high aggregate impact are the best targets.
6. **Not testing the phrasing** — Show to 3 people: "Do you know exactly what decision this is about?"

---

## WHEN TO OVERRIDE

- You're an expert in a niche domain — skip breadth scoring
- Someone specifically requested a DCP — demand validates the input
- Building a DCP library — build all candidates above 18 rather than top 5
- Decision is time-sensitive — skip this procedure, go directly to `/dcp`

---

## WORKED EXAMPLES

### Example 1: Mining Personal Experience (Section A)

**A1 excerpt**:
- "Chose wrong health insurance plan" [R]
- "Picked a contractor for bathroom renovation" [S]
- "Decided to learn Rust instead of Go" [E]

**A3**: "Choosing a health insurance plan during open enrollment" / "Selecting a contractor for home renovation" / (dropped — [E])

**E1 scoring**:
| Candidate | Rec | Stk | Exp | Cmx | Mch | Inf | Asy | Brd | Res | Dec | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Health insurance | 3 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | **27** |
| Contractor selection | 2 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 | **27** |

### Example 2: Domain Mining (Section B)

**Domain**: Software Engineering
**Lifecycle**: Requirements → Architecture → Stack → Build → Test → Deploy → Monitor → Scale

**B3** (from "Stack" stage): Which language? Which framework? Which database? Which cloud? Which third-party services? Build vs. integrate?

**E4**: "Choosing a programming language and framework for a new web application project" (24/30)

### Example 3: Broad Brainstorm (Section C)

**Top 3**:
1. "Evaluating whether to accept a job offer vs. staying at current job" (28/30)
2. "Choosing a health insurance plan during US open enrollment" (27/30)
3. "Deciding whether to repair or replace a major home appliance" (25/30)

---

**Validation status**: This procedure has not been validated by domain experts.
