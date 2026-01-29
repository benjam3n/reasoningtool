# Universal: User Guidance Questions (116)

**Category**: META - Questions to Ask When Giving User Actionable Guidance
**Source**: [D: from ARAW session on GOSM publication strategy - identified gap in GOSM treating user as execution machine]
**Structure**: Six question categories for user-action output
**Purpose**: Ensure Claude's guidance accounts for user's actual capacity, alignment, and protection

## The Core Problem

Current GOSM focuses on WHAT should be done, not:
- WHO can do it (user capacity)
- WHETHER user wants to do it (user alignment)
- WHAT happens if wrong (protection)
- WHAT actually happens vs plan (execution reality)

When output is "steps for user to take," these questions become critical.

---

## Category 1: OPERATOR CAPACITY

**What it addresses**: Can the user actually do this?

| Question | Why It Matters | Example |
|----------|----------------|---------|
| Does user have the skills for this? | Unskilled execution fails | "Build a SaaS" requires many skills |
| Does user have time for this? | Time is the hardest constraint | Full-time job + family limits capacity |
| Does user have resources for this? | Money, tools, access | "Get external feedback" requires network |
| Does user have authority for this? | Some actions need permission | "Change team process" needs role authority |
| What constraints limit user? | Unstated constraints block action | Health, location, commitments |

**CRUX Ratings**:
- HIGH: Skill requirements (can't do what you can't do)
- HIGH: Time availability (most common real constraint)
- MED: Resource requirements (often solvable if known)
- LOW: Tool access (usually acquirable)

---

## Category 2: USER ALIGNMENT

**What it addresses**: Does user actually want this?

| Question | Why It Matters | Example |
|----------|----------------|---------|
| What does user actually value? | Stated goals ≠ real values | Says "money," values autonomy |
| Will user accept this trade-off? | Every action has trade-offs | Financial gain vs time cost |
| Does this fit user's life situation? | Life context constrains choices | Career advice ignoring family |
| Is user's stated goal their real goal? | Surface goals mask deeper ones | "Start business" may mean "escape job" |
| Would user choose this with full information? | Informed consent matters | Hidden costs change decisions |

**CRUX Ratings**:
- HIGH: Stated vs real goal (solving wrong problem entirely)
- HIGH: Trade-off acceptance (user may reject "right" answer)
- MED: Life situation fit (important but often known)
- MED: Value alignment (guides preference)
- LOW: Informed consent (usually achievable)

---

## Category 3: REVERSIBILITY

**What it addresses**: Can user undo this if wrong?

| Question | Why It Matters | Example |
|----------|----------------|---------|
| Is this a one-way door? | One-way decisions need more care | License choice, public statements |
| What's locked in by this action? | Some actions close options | Signing contract, quitting job |
| What options close vs open? | Good strategy keeps options | Experimentation vs commitment |
| Can user pivot if this fails? | Failure recovery matters | Burnt bridges vs maintained relationships |
| What would reversal cost? | High reversal cost ≈ irreversible | Reputational damage, financial loss |

**CRUX Ratings**:
- HIGH: One-way door detection (changes everything)
- HIGH: Option closure (strategy-defining)
- MED: Reversal cost (calibrates risk)
- LOW: Pivot ability (usually exists if thought about)

---

## Category 4: PROTECTIVE

**What it addresses**: What could go wrong for user?

| Question | Why It Matters | Example |
|----------|----------------|---------|
| What could go wrong? | Pre-mortem before action | Publication could be ignored or attacked |
| How is user exposed? | Vulnerabilities need awareness | Public work exposes to criticism |
| What's the downside scenario? | Worst case planning | Financial ruin, reputation damage |
| What would user lose if this fails? | Loss framing clarifies stakes | Time, money, relationships, options |
| Who might act against user's interests? | Adversarial thinking | Competitors, bad actors, capture |

**CRUX Ratings**:
- HIGH: Exposure identification (what you don't see can hurt you)
- HIGH: Downside scenario (calibrates risk tolerance)
- MED: Loss inventory (clarifies stakes)
- MED: Adversarial actors (relevant in competitive domains)
- LOW: Failure probability (hard to estimate accurately)

---

## Category 5: EXECUTION REALITY

**What it addresses**: What will actually happen vs intended?

| Question | Why It Matters | Example |
|----------|----------------|---------|
| What will actually happen? | Plans ≠ reality | "Community will form" - will it? |
| What implementation friction exists? | Friction blocks execution | Documentation is tedious |
| What's the likely drift from plan? | Plans drift predictably | Timeline optimism, scope creep |
| What's the gap between plan and execution? | Gap awareness enables correction | Perfect plan, no follow-through |
| What typically goes wrong at this stage? | Pattern recognition | "Launch" often means "crickets" |

**CRUX Ratings**:
- HIGH: Implementation friction (friction stops action)
- MED: Plan-reality gap (common, manageable)
- MED: Predictable drift (can be planned for)
- LOW: Stage-specific patterns (useful reference)

---

## Category 6: TIMING/SEQUENCING

**What it addresses**: What order should things happen?

| Question | Why It Matters | Example |
|----------|----------------|---------|
| What must happen first? | Dependencies define order | License before publish |
| What's the right sequence? | Order affects outcome | Community before launch vs after |
| What dependencies exist? | Blocking relationships | Infrastructure before features |
| What can be parallelized? | Efficiency opportunity | Feedback gathering + writing |
| What's the critical path? | Longest sequence determines timeline | What must be sequential? |

**CRUX Ratings**:
- HIGH: Dependencies (blocking = must do first)
- MED: Critical path (affects timeline)
- MED: Sequence effects (order can matter)
- LOW: Parallelization (optimization, not critical)

---

## When to Apply These Categories

**Apply when:**
- Output includes steps for user to take
- Advice depends on user's situation
- Actions have significant consequences
- User capacity is uncertain
- Trade-offs exist

**Skip when:**
- Output is informational only
- User has already decided, just needs execution
- Actions are trivially reversible
- Situation is well-understood

---

## Integration with GOSM

### Add to ARAW DO_FIRST Section
Before generating DO_FIRST actions for user:
1. Check OPERATOR CAPACITY for each action
2. Check REVERSIBILITY for one-way doors
3. Note PROTECTIVE concerns

### Add to Steps Generation
When generating steps:
1. Include capacity requirements
2. Flag irreversible actions
3. Order by dependencies
4. Note execution friction

### Create User Guidance Meta-Procedure
When output is for user action, invoke:
```
→ INVOKE: /user_guidance [proposed steps]
```
This applies all 6 categories before finalizing recommendations.

---

## Example Application

**Proposed step**: "Publish GOSM on GitHub"

| Category | Questions | Findings |
|----------|-----------|----------|
| OPERATOR CAPACITY | Can user do this? | Yes - has GitHub account, technical skill |
| USER ALIGNMENT | Does user want this? | Ambivalent - wants impact but fears criticism |
| REVERSIBILITY | One-way door? | Partially - can delete but history persists |
| PROTECTIVE | What could go wrong? | Ignored, criticized, captured by large org |
| EXECUTION REALITY | What will actually happen? | Likely slow adoption, need marketing effort |
| TIMING/SEQUENCING | Prerequisites? | License decision, minimal documentation |

**Adjusted recommendation**: "Publish GOSM on GitHub after: (1) making license decision (AGPL recommended), (2) writing minimal explanation document, (3) preparing for likely silence initially."

---

## Coverage Summary

```
CATEGORIES: 6
QUESTIONS PER CATEGORY: 5
TOTAL QUESTIONS: 30

HIGHEST CRUX (strategy-changing):
- One-way door detection (REVERSIBILITY)
- Skill requirements (CAPACITY)
- Stated vs real goal (ALIGNMENT)
- Exposure identification (PROTECTIVE)
- Implementation friction (EXECUTION)

PURPOSE:
Move from "what should be done" to "what can user actually do, given their situation, with acceptable risk"

KEY INSIGHT:
Current GOSM treats user as execution machine.
These questions treat user as person with constraints, values, and vulnerabilities.
```
