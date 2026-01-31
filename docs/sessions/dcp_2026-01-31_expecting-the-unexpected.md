# Decision Procedure — Expecting the Unexpected

**Date**: 2026-01-31
**Input**: expecting the unexpected and searching for the unexpected before it happens

---

# EXPECTING THE UNEXPECTED: Decision Procedure
### How to systematically search for and prepare for unexpected events before they happen

---

## Step 1: Decision Dimensions

What factors determine whether you've adequately searched for the unexpected?

**D1: Domain Type** — What kind of system or situation are you scanning? (Personal life, business operation, technical system, physical environment, financial, health, geopolitical.) Different domains produce different categories of surprise.

**D2: Time Horizon** — How far ahead are you trying to look? (Next hour, next week, next quarter, next year, next decade.) Short horizons favor concrete scenarios; long horizons favor structural shifts.

**D3: Consequence Severity** — What's the worst-case impact if an unexpected event occurs? (Annoying, costly, catastrophic, existential.) This determines how much effort to invest in scanning.

**D4: Information Quality** — How well do you understand the current state of the system? (Deep expertise, moderate familiarity, surface knowledge, almost blind.) Lower knowledge = more hidden unknowns.

**D5: Rate of Change** — How quickly does this domain change? (Static, slow-moving, fast-moving, chaotic.) Faster change = more frequent scanning needed.

**D6: Coupling Tightness** — How interconnected are the components? (Loosely coupled, moderately linked, tightly coupled.) Tighter coupling = cascade failures more likely.

**D7: Historical Precedent Availability** — Have similar situations produced surprises before? (Rich history, some examples, novel territory.) Less precedent = harder to anticipate.

**D8: Number of Actors/Variables** — How many independent agents or moving parts exist? (Few, moderate, many, uncountable.) More actors = more sources of surprise.

**D9: Reversibility** — If the unexpected happens, can you undo the damage? (Fully reversible, partially, irreversible.) Irreversible consequences demand more thorough scanning.

**D10: Your Control Level** — How much influence do you have over the system? (Full control, partial, observer only.) Less control = more emphasis on preparation vs. prevention.

**D11: Detection Lag** — How long between an unexpected event starting and you noticing? (Instant, hours, days, months.) Long lag = need for monitoring systems.

**D12: Current Confidence Level** — How sure are you that things will go as planned? (Very uncertain, somewhat confident, highly confident.) High confidence is where the most dangerous surprises hide.

---

## Step 2: Options per Dimension

**D1 Domain Types & Their Surprise Categories:**
- Personal life → health shocks, relationship shifts, identity crises
- Business → market shifts, competitor moves, regulatory changes, talent loss
- Technical systems → failure modes, scaling limits, security breaches, dependency failures
- Physical → weather, equipment failure, supply chain, infrastructure
- Financial → market crashes, liquidity crunches, fraud, currency shifts
- Health → sudden onset, misdiagnosis, drug interactions, genetic factors
- Geopolitical → policy reversals, conflicts, trade disruptions, sanctions

**D3 Consequence Severity Levels:**
- **Annoying** (< 1 day disruption) → light scan
- **Costly** (financial/time loss, recoverable) → moderate scan
- **Catastrophic** (major loss, hard to recover) → thorough scan
- **Existential** (could end the enterprise/life) → exhaustive scan

**D5 Rate of Change → Scan Frequency:**
- Static → annual review
- Slow-moving → quarterly
- Fast-moving → weekly/monthly
- Chaotic → continuous monitoring

**D12 Confidence × Severity Interaction:**
- High confidence + high severity = **DANGER ZONE** (most blindsided here)
- Low confidence + high severity = appropriate caution already present
- High confidence + low severity = acceptable risk
- Low confidence + low severity = not worth heavy scanning

---

## Step 3: Hidden Assumptions

People searching for the unexpected typically assume:

1. **"The unexpected is rare"** — Actually, *some* unexpected thing happening is nearly certain. The error is thinking about specific scenarios rather than the base rate of surprise.

2. **"I'll recognize it when I see it"** — Detection lag (D11) means many unexpected events are well underway before anyone notices. By the time it's obvious, it's often too late.

3. **"Past patterns predict future surprises"** — The most damaging unexpected events are precisely those that *don't* match historical patterns. Scanning only for known failure types misses novel ones.

4. **"Experts see it coming"** — Experts are often the *most* blindsided because their models are the most rigid. They discount signals that don't fit their frameworks.

5. **"More information = better preparation"** — Information overload makes it *harder* to spot weak signals. The issue is usually filtering, not volume.

6. **"The big risk is one big event"** — Often it's a *cascade* of small events that individually seem manageable but compound into catastrophe.

7. **"If I can't predict it, I can't prepare"** — You can build generic resilience (reserves, redundancy, optionality) without predicting specific scenarios.

8. **"My current plan accounts for reasonable variation"** — Plans usually account for ±10% variation. Actual surprises are often ±50% or qualitative shifts.

9. **"The system boundaries are where I drew them"** — Surprises often come from outside the system boundary you defined. Adjacent systems, upstream dependencies, and downstream consequences get ignored.

---

## Step 4: The Procedure

```
EXPECTING THE UNEXPECTED — DECISION PROCEDURE
================================================

STEP 0: What kind of scan is this?

┌─────────────────────────────────────┬──────────────┐
│ Situation                           │ Go to        │
├─────────────────────────────────────┼──────────────┤
│ I have a specific plan or project   │ SECTION A    │
│ I run an ongoing system/operation   │ SECTION B    │
│ I feel uneasy but can't say why     │ SECTION C    │
│ Something small just went wrong     │ SECTION D    │
└─────────────────────────────────────┴──────────────┘


SECTION A: SCANNING A SPECIFIC PLAN
====================================

Step A1: Write down your plan in 5-10 bullet points.
  → What you should see: A concrete sequence of actions
    with expected outcomes.

Step A2: For each bullet, complete this sentence:
  "This step assumes that ____________ will remain true."
  Write down every assumption, no matter how obvious.
  → Target: 3-5 assumptions per step. If you have fewer,
    you're not looking hard enough.

Step A3: For each assumption, ask:
  "What would make this assumption false?"
  Write down at least one scenario per assumption.
  → What you should see: A list of 15-50 "assumption
    breakers." Many will seem unlikely. That's fine.

Step A4: Rate each assumption breaker:
  - Would I notice within 24 hours if this happened? (YES/NO)
  - Could I recover within my timeline if this happened? (YES/NO)

Step A5: Any item marked NO + NO?
  → If YES: This is a critical blind spot. Go to Step A7.
  → If NO: Go to Step A6.

Step A6: Any item marked NO (for either question)?
  → If YES: These are your warning items. For each one,
    write ONE concrete action: either a monitoring check
    or a backup plan. Then go to Step A9.
  → If NO: Your plan has good coverage. Go to Step A9.

Step A7: CRITICAL BLIND SPOTS — For each NO + NO item:
  (a) Can you add a monitoring mechanism?
      (A daily check, an alert, a person watching?)
      → If YES: Add it. Move item to "warning" category.
      → If NO: Go to (b).
  (b) Can you add a backup plan that works even without
      early warning?
      → If YES: Document it. This is your emergency
        procedure.
      → If NO: Go to (c).
  (c) Can you restructure the plan to remove this
      assumption entirely?
      → If YES: Restructure. Re-run from Step A2.
      → If NO: Go to Step A8.

Step A8: IRREDUCIBLE RISK
  You have identified a risk you cannot monitor, recover
  from, or avoid. You must decide:
  - Accept the risk explicitly (write: "I accept that
    [X] could happen and I cannot prevent or recover
    from it.")
  - Abandon or fundamentally redesign the plan.
  → There is no third option. Do not proceed without
    making this choice consciously.

Step A9: CROSS-CUTTING SCAN
  Look at your full assumption list. Ask:
  (a) "What single external event would break 3+ of
       these assumptions simultaneously?"
       (Examples: economic downturn, key person leaving,
       technology failure, regulatory change)
  (b) For each event found: create ONE response plan.
  → If you found zero such events: either your plan is
    very robust or your assumptions are too narrow.
    Ask one other person to review your list.

Step A10: BOUNDARY SCAN
  List everything your plan depends on that you do NOT
  control:
  - Other people's decisions
  - External services/systems
  - Market conditions
  - Weather/physical conditions
  - Legal/regulatory environment
  For each: "What is the most disruptive thing this
  external factor could do?" Add to your monitoring list.

→ DONE. Output: Your plan + assumption register +
  monitoring checklist + emergency procedures.


SECTION B: SCANNING AN ONGOING SYSTEM
======================================

Step B1: List the 5-10 things that MUST keep working
  for your system to function.
  → What you should see: The critical dependencies.
    Not features — foundations.

Step B2: For each critical dependency, answer:
  - When did I last verify this is actually working?
  - How would I know if it stopped working?
  - What's my longest plausible detection delay?

Step B3: Any dependency where detection delay > 1 week?
  → If YES: Create a check. A weekly verification,
    automated alert, or human review.
  → If NO: Go to Step B4.

Step B4: NEAR-MISS INVENTORY
  List every "close call" or "minor issue" from the
  last 6 months. Include things that were quickly fixed
  and forgotten.
  → Target: At least 5 items. If you have fewer, ask
    3 other people involved in the system.

Step B5: For each near-miss, ask:
  "Under what conditions would this have been a
   full failure instead of a near-miss?"
  → What you should see: Specific scenarios where
    luck or quick response prevented disaster.

Step B6: For each full-failure scenario:
  - Is the factor that prevented it RELIABLE or was
    it LUCK? (Be honest.)
  → If LUCK for any item: This is a ticking time bomb.
    Create a structural fix (redundancy, automation,
    process change) — not just "be more careful."

Step B7: DEGRADATION SCAN
  What has gotten slightly worse over time but hasn't
  broken yet?
  - Performance metrics trending down?
  - Response times increasing?
  - Error rates creeping up?
  - Team morale declining?
  - Customer complaints increasing slightly?
  → These are early warnings of future unexpected
    failures. For each: set an explicit threshold
    where you will act.

Step B8: WHAT CHANGED RECENTLY?
  List everything that changed in the last 30 days,
  no matter how minor. Changes introduce new failure
  modes that take time to manifest.
  For each change: "What could this break that we
  haven't seen yet?"

→ DONE. Output: Dependency health register + near-miss
  analysis + degradation dashboard + change impact log.


SECTION C: SCANNING A VAGUE UNEASE
====================================

Step C1: Complete this sentence 5 times:
  "Something feels off about ___________."
  Don't filter. Don't rationalize. Write gut feelings.

Step C2: For each item, ask:
  "What specific OBSERVATION triggered this feeling?"
  (Something you saw, heard, read, or noticed.)
  → If you can identify an observation: Go to Step C3.
  → If you cannot: Go to Step C4.

Step C3: For each observation, ask:
  "What are THREE possible explanations for this?"
  - One benign explanation
  - One concerning explanation
  - One alarming explanation
  For the concerning and alarming explanations:
  "What would I expect to see next if this were true?"
  → Now you have specific things to watch for.
    Monitor for 1-2 weeks, then reassess.

Step C4: PURE INTUITION ITEMS (no specific observation)
  These may be pattern-matching your subconscious is
  doing. Test them:
  (a) Describe the WORST CASE version of what you fear.
  (b) Rate it: How bad would this be? (1-10)
  (c) If rated 7+: Spend 30 minutes actively searching
      for evidence FOR and AGAINST this fear.
  (d) If rated <7: Note it and revisit in 2 weeks.

→ DONE. Output: Structured worry list with monitoring
  triggers and evidence searches.


SECTION D: SOMETHING SMALL JUST WENT WRONG
============================================

Step D1: Describe exactly what happened.
  → Just facts. What broke, when, what was the impact.

Step D2: Was this the FIRST time, or has something
  similar happened before?
  → First time: Go to Step D3.
  → Happened before: Go to Step D5.

Step D3: Ask: "What ELSE relies on the same thing
  that just failed?"
  List every system, process, or plan that shares this
  dependency.
  → These are all now at elevated risk.

Step D4: Ask: "Is the root cause fixed, or did we
  just fix the symptom?"
  → Root cause fixed: Monitor the related systems
    (Step D3 list) for 2 weeks.
  → Symptom fixed only: Treat this as a near-miss.
    Go to Section B, Step B4.

Step D5: RECURRING SMALL FAILURE
  This is the most dangerous signal. Small recurring
  failures indicate a systemic issue.
  (a) List every instance you can remember.
  (b) What's the TREND? (Getting worse? More frequent?
      Spreading to new areas?)
  (c) If trending worse: This WILL become a major
      failure. The question is when, not if.
      Escalate: involve someone with authority to
      make structural changes.

→ DONE. Output: Incident analysis + cascade risk
  map + escalation decision.
```

---

## Step 5: Failure Modes & Warnings

**FAILURE MODE 1: "I did Section A and found nothing concerning"**
- **How to recognize**: Your assumption list is short (<15 items) or every item seems low-risk.
- **What's happening**: You're not challenging your own thinking deeply enough.
- **Fix**: Have someone ELSE do Steps A2-A3 independently. Compare lists. The differences are your blind spots.

**FAILURE MODE 2: "Everything seems critical"**
- **How to recognize**: After scanning, you have 30+ high-priority items and feel paralyzed.
- **What's happening**: You're not distinguishing between "bad" and "bad AND undetectable AND unrecoverable."
- **Fix**: Re-run Step A4 strictly. Only NO + NO items are truly critical. Everything else is manageable with monitoring.

**FAILURE MODE 3: "I'll just keep scanning forever"**
- **How to recognize**: You've been at this for hours and keep finding new things.
- **What's happening**: The search space is infinite. Perfectionism is the enemy.
- **Fix**: Time-box the scan. Section A: 2 hours max. Section B: 1 hour. Section C: 30 minutes. Section D: 15 minutes. What you find in that time is enough.

**FAILURE MODE 4: "I scanned last month, nothing has changed"**
- **How to recognize**: You skip the scan because you believe the situation is stable.
- **What's happening**: This is exactly how unexpected events blindside you. The scan interval depends on rate of change (D5).
- **Fix**: Never skip a scheduled scan. Even a 15-minute quick pass through Section B, Steps B7-B8 is sufficient between full scans.

**FAILURE MODE 5: "The procedure found a risk but I rationalized it away"**
- **How to recognize**: You complete Step A8 and choose "accept" for everything without genuine deliberation.
- **What's happening**: Cognitive dissonance — you don't want to redesign your plan.
- **Fix**: For each "accept" decision, write the sentence out loud: "I accept that [specific bad thing] could happen and I cannot prevent or recover from it." If you can't say it comfortably, you haven't actually accepted it.

**FAILURE MODE 6: "I only scanned my own domain"**
- **How to recognize**: Your assumption list references only things within your direct area.
- **What's happening**: You missed the Boundary Scan (Step A10). Most surprises come from outside your defined system.
- **Fix**: Go back to Step A10. Force yourself to list at least 5 external dependencies.

---

## Step 6: Validation Check

Validation against executability criteria:

| Criterion | Status |
|---|---|
| Every step is a concrete action (not "consider" or "think about") | PASS — all steps produce written output |
| All decision points are binary or explicit multiple choice | PASS — all branches are YES/NO or go-to |
| No jargon without definition | PASS — plain language throughout |
| Every path leads to a concrete output | PASS — each section ends with defined deliverables |
| No dead ends or loops | PASS — Step A7c can loop but with a redesign gate |
| Followable without domain expertise | PASS — no domain knowledge required |
| "What you should see" markers included | PASS — present at key steps |

---

## QUICK REFERENCE CARDS

**The 3 Questions That Find 80% of Hidden Risks:**
1. "What am I most confident about?" → Scan THAT hardest
2. "What changed recently?" → Changes breed surprises
3. "What almost went wrong last time?" → Near-misses predict failures

**Scan Frequency by Domain Speed:**
| Domain pace | Full scan | Quick check (B7-B8) |
|---|---|---|
| Static | Every 6 months | Quarterly |
| Slow-moving | Quarterly | Monthly |
| Fast-moving | Monthly | Weekly |
| Chaotic | Weekly | Daily |

**The Danger Quadrant:**

```
                  LOW SEVERITY    HIGH SEVERITY
HIGH CONFIDENCE   Acceptable      ⚠ DANGER ZONE
LOW CONFIDENCE    Ignore          Appropriate caution
```

---

## COMMON MISTAKES

1. **Scanning for specific scenarios instead of structural vulnerabilities.** Don't ask "will there be a recession?" Ask "what happens if revenue drops 40% from any cause?"
2. **Treating the scan as a one-time activity.** This is a recurring practice, not a project.
3. **Confusing "unlikely" with "impossible."** If the consequence is severe enough, unlikely events demand preparation.
4. **Only scanning downside risks.** Unexpected *opportunities* are also "unexpected." Missing a sudden opening can be as costly as hitting an unseen obstacle.
5. **Producing a risk register nobody reads.** If your output goes in a drawer, the scan was wasted. Each scan must produce at least ONE concrete action you take this week.
6. **Anchoring on your last surprise.** Generals fight the last war. Your next surprise will probably be qualitatively different from your last one.

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **Active crisis**: Stop scanning. Act. Use Section D only after the immediate crisis is resolved.
- **Decision is trivially reversible**: If you can undo any mistake in under a day with no lasting cost, skip the scan.
- **Expert with deep domain knowledge is available**: Show them your assumption list (Step A2) and ask what you missed, rather than running the full procedure yourself.
- **The scan is causing decision paralysis**: If after 2 hours you're more anxious and less decisive, stop. Pick the top 3 risks, make a plan for those, and move forward.

---

## WORKED EXAMPLES

### Example 1: Launching a New Product Feature

**Section A applied:**
- Plan: Build feature → test → ship to 10% of users → monitor → full rollout
- Assumption breakers found: "test environment doesn't match production" (NO detection within 24h + NO recovery within timeline = CRITICAL)
- Action taken: Added production-mirror staging environment and canary deployment with automated rollback
- Boundary scan found: Third-party API dependency has no SLA. Added fallback behavior.

### Example 2: Running a Small Business (Ongoing)

**Section B applied:**
- Critical dependencies: 1 key supplier, 3 key clients, 1 essential employee
- Near-miss inventory revealed: Key employee almost quit 4 months ago (resolved with raise). This was LUCK, not structure.
- Structural fix: Cross-trained second person on all critical functions. Documented all processes.
- Degradation scan: Client payment times trending from 30 → 45 days over 6 months. Set threshold: if any client exceeds 60 days, trigger collections protocol.

### Example 3: Vague Unease About a Partnership

**Section C applied:**
- "Something feels off about how Partner X responds to timeline questions."
- Observation: They've been vague about delivery dates 3 times in the last month.
- Three explanations: (1) They're busy (benign), (2) They're behind schedule (concerning), (3) They're planning to exit the partnership (alarming)
- If concerning: expect missed minor deadlines next. If alarming: expect reduced communication.
- Monitoring plan: Track response times and deadline accuracy for 2 weeks. If 2+ deadlines slip → direct conversation.

---

*This procedure has not been validated by domain experts. It is a structured thinking aid, not a substitute for professional risk management in high-stakes domains.*
