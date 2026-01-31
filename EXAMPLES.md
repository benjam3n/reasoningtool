# Why Structure Matters: Concrete Examples

These examples show the difference between standard LLM responses and structured reasoning procedures. The standard responses aren't strawmen—they're the kind of good-sounding, approval-seeking output that actually gets produced. The structured outputs are different in *kind*, not just degree.

---

## Example 1: Business Decision
**"Should I quit my job to start a startup?"**

### What a Standard LLM Says

This is an exciting opportunity but also a significant decision. Here are some key factors to consider:

**Pros:**
- Pursue your passion and vision
- Potential for unlimited upside
- Be your own boss and control your destiny
- Learn and grow rapidly

**Cons:**
- Financial risk and uncertainty
- Loss of steady income and benefits
- High stress and long hours
- Most startups fail

**My recommendation:** If you have 6-12 months of savings, a validated idea, and strong risk tolerance, it could be worth pursuing. Consider starting as a side project first to test the market. Make sure you have support from family/partners.

### What an "Enhanced" Approach Says (Chain-of-thought)

Let me think through this step by step:

1. First, I need to understand your financial situation. Do you have savings?
2. What's the startup idea? Has it been validated?
3. What's your risk tolerance?
4. Do you have co-founders?

Assuming you have 6 months savings and a validated idea:
- The expected value calculation favors trying if the upside is high enough
- But you need to consider the opportunity cost of your current salary
- And the psychological cost of uncertainty

The decision tree suggests: If (savings > 6 months AND idea validated AND risk tolerant) then consider it, else stay at job and build on the side.

Conclusion: You should probably start as a side project first to de-risk it.

### What ARAW Produces

**ORIGINAL INPUT:** "Should I quit my job to start a startup?"

**STEP 1: UNBUNDLE CLAIMS**

The question bundles multiple testable claims:

[C1] There is a problem with my current job that requires leaving — TYPE: implicit — VOI: high
[C2] Starting a startup is the solution to that problem — TYPE: implicit — VOI: high
[C3] Quitting now (rather than later, or never) is optimal timing — TYPE: implicit — VOI: high
[C4] I have a startup idea worth pursuing — TYPE: presupposed — VOI: critical
[C5] The startup must be full-time to succeed — TYPE: implicit — VOI: high
[C6] The alternative (staying) is worse than the risk — TYPE: implicit — VOI: high

**PHASE 1: EXPLORATION**

**[C1] "There is a problem with my current job that requires leaving"**

ASSUME RIGHT:
[F1] If right: You're experiencing something genuinely untenable — Necessary
  [F2] If F1: Either environment is toxic, role misaligned, or growth blocked — Necessary
    [F3] If environment toxic: Staying causes measurable harm to health/relationships — Probable
      [F4] BEDROCK-OBSERVE: Track stress markers, sleep quality, relationship conflicts for 2 weeks
    [F5] If role misaligned: Your actual work differs from what you're optimized for — Probable
      [F6] BEDROCK-TEST: List 10 energizing tasks, compare to current work distribution
  [F7] FORECLOSED if C1 right: You cannot fix the problem while staying — Necessary
    [F8] If F7: You've already attempted fixes that failed — Probable
      [F9] BEDROCK-TEST: Document previous attempts to fix: conversations with manager, role changes requested, team transfers explored

ASSUME WRONG:
[F10] Wrong because: The problem is solvable within current role — Serious
  [F11] If F10: The issue is positional (your current role) not organizational — Probable
    [F12] Alternative derived from F10: Internal transfer to different team/role
      [F13] BEDROCK-TEST: Identify 3 internal roles that would solve the problem
  [F14] Wrong because: You're conflating temporary frustration with permanent misalignment — Fatal
    [F15] If F14: Current frustration is from recent event, not chronic condition — Possible
      [F16] BEDROCK-OBSERVE: Check if complaint is <3 months old vs >1 year chronic
  [F17] Wrong because: You're running toward startup fantasy, not away from real problem — Fatal
    [F18] If F17: The startup idea came *after* job dissatisfaction — Probable
      [F19] BEDROCK-OBSERVE: Timeline check: job frustration vs when startup idea emerged

**[C4] "I have a startup idea worth pursuing"**

ASSUME RIGHT:
[F20] If right: Idea solves real problem for identifiable users — Necessary
  [F21] If F20: You can name 10 people with this exact problem — Necessary
    [F22] BEDROCK-TEST: Send description to 10 potential users, measure response
  [F23] If F20: Problem is expensive enough they'll pay — Necessary
    [F24] BEDROCK-TEST: Ask the 10 people their current solution cost
[F25] If right: You have unique advantage in solving this — Probable
  [F26] If F25: Your background/skills/network give unfair advantage — Necessary
    [F27] BEDROCK-LOGIC: If anyone could build this, someone already would have
[F28] FORECLOSED if C4 right: You cannot pursue this while employed — Conditional
  [F29] If F28 true: Either IP conflict or time requirements — Necessary
    [F30] BEDROCK-TEST: Review employment contract for non-compete, IP assignment clauses

ASSUME WRONG:
[F31] Wrong because: You're in love with solution, not problem — Fatal
  [F32] If F31: You started with "I want to build X" not "People suffer from Y" — Probable
    [F33] BEDROCK-OBSERVE: Check your earliest notes — did they describe problem or solution?
[F34] Wrong because: The idea is actually a feature, not a company — Fatal
  [F35] If F34: Market size is <$100M or idea is subset of existing product — Serious
    [F36] BEDROCK-TEST: Search for companies that could add this as a feature
[F37] Wrong because: You haven't validated the core assumption — Fatal
  [F38] If F37: You're building based on intuition, not user conversations — Probable
    [F39] Alternative derived from F37: Talk to 20 users before quitting
      [F40] BEDROCK-TEST: Schedule and complete 20 user interviews in next 30 days

**[C5] "The startup must be full-time to succeed"**

ASSUME RIGHT:
[F41] If right: Opportunity window is narrow and closing — Necessary
  [F42] If F41: Competitor will capture market in <6 months — Probable
    [F43] BEDROCK-TEST: Identify direct competitors and their funding/progress
[F44] If right: The work requires more than nights/weekends — Probable
  [F45] If F44: Core product needs 40+ hours/week for 6+ months — Necessary
    [F46] BEDROCK-TEST: Map minimum viable product, estimate hours realistically

ASSUME WRONG:
[F47] Wrong because: You can validate the idea part-time first — Fatal
  [F48] If F47: Validation requires conversations, not building — Necessary
    [F49] Alternative derived from F47: Spend 3 months validating part-time
      [F50] BEDROCK-TEST: Set validation milestones: 20 interviews, 5 paying pilots, 1 LOI
  [F51] Wrong because: Full-time commitment comes after validation, not before — Fatal
    [F52] If F51: You're risking stable income before knowing if anyone wants this — Serious
      [F53] BEDROCK-LOGIC: Irreversible decision should come after reversible validation

**PHASE 2: FINDING REGISTRY**

FINDING REGISTRY
================

CLAIMS TESTED:
[C1] There is a problem with my current job that requires leaving — TYPE: implicit — VOI: high
[C4] I have a startup idea worth pursuing — TYPE: presupposed — VOI: critical
[C5] The startup must be full-time to succeed — TYPE: implicit — VOI: high

AR FINDINGS (Implications):
[F1] You're experiencing something genuinely untenable — STRENGTH: necessary — PARENT: C1
[F2] Either environment is toxic, role misaligned, or growth blocked — STRENGTH: necessary — PARENT: F1
[F3] Staying causes measurable harm to health/relationships — STRENGTH: probable — PARENT: F2
[F20] Idea solves real problem for identifiable users — STRENGTH: necessary — PARENT: C4
[F21] You can name 10 people with this exact problem — STRENGTH: necessary — PARENT: F20
[F41] Opportunity window is narrow and closing — STRENGTH: necessary — PARENT: C5
[F45] Core product needs 40+ hours/week for 6+ months — STRENGTH: necessary — PARENT: F44

AR FINDINGS (Foreclosures):
[F7] You cannot fix the problem while staying — PARENT: C1
[F28] You cannot pursue this while employed — PARENT: C4

AW FINDINGS (Wrongness Reasons):
[F10] The problem is solvable within current role — SEVERITY: serious — PARENT: C1
[F14] You're conflating temporary frustration with permanent misalignment — SEVERITY: fatal — PARENT: C1
[F17] You're running toward startup fantasy, not away from real problem — SEVERITY: fatal — PARENT: C1
[F31] You're in love with solution, not problem — SEVERITY: fatal — PARENT: C4
[F34] The idea is actually a feature, not a company — SEVERITY: fatal — PARENT: C4
[F37] You haven't validated the core assumption — SEVERITY: fatal — PARENT: C4
[F47] You can validate the idea part-time first — SEVERITY: fatal — PARENT: C5
[F51] Full-time commitment comes after validation, not before — SEVERITY: fatal — PARENT: C5

BEDROCK REACHED:
[F4] BEDROCK-OBSERVE: Track stress markers for 2 weeks
[F6] BEDROCK-TEST: List 10 energizing tasks, compare to current work
[F9] BEDROCK-TEST: Document previous attempts to fix
[F13] BEDROCK-TEST: Identify 3 internal roles that would solve the problem
[F16] BEDROCK-OBSERVE: Check if complaint is <3 months vs >1 year
[F19] BEDROCK-OBSERVE: Timeline check for job frustration vs startup idea
[F22] BEDROCK-TEST: Send description to 10 users, measure response
[F24] BEDROCK-TEST: Ask 10 people their current solution cost
[F30] BEDROCK-TEST: Review employment contract
[F33] BEDROCK-OBSERVE: Check earliest notes for problem vs solution focus
[F36] BEDROCK-TEST: Search for companies that could add this as feature
[F40] BEDROCK-TEST: Complete 20 user interviews in 30 days
[F43] BEDROCK-TEST: Identify competitors and their progress
[F46] BEDROCK-TEST: Map MVP, estimate hours
[F50] BEDROCK-TEST: Set validation milestones

TENSIONS:
[F7] "cannot fix problem while staying" contradicts [F10] "problem is solvable within current role"
[F28] "cannot pursue while employed" contradicts [F47] "can validate part-time first"

CLAIM VERDICTS:
[C1] UNCERTAIN
  -- AR evidence: F1->F3 probable but not verified
  -- AW evidence: F14, F17 are fatal if true
  -- Verdict derived from: Cannot determine without BEDROCK tests F4, F6, F16, F19

[C4] REJECTED
  -- AR evidence: F20->F21 necessary but unverified
  -- AW evidence: F37 is fatal — no validation has occurred
  -- Verdict derived from: F40 test must happen before C4 can be validated

[C5] REJECTED
  -- AR evidence: F41 necessary but unverified
  -- AW evidence: F47, F51 are fatal — validation comes before full-time
  -- Verdict derived from: F53 logical necessity — irreversible after reversible

CRUX POINTS:
[CRUX-1] Is the job problem chronic (>1yr) or recent (<3mo)? — resolves: F1, F14, F16 — test: F16
[CRUX-2] Did startup idea emerge before or after job frustration? — resolves: F17, F19 — test: F19
[CRUX-3] Can you name 10 people with this problem willing to pay? — resolves: F20, F21, F31 — test: F22, F24
[CRUX-4] What do 20 user interviews reveal? — resolves: F37, F40 — test: F40
[CRUX-5] Can you validate part-time in 3 months? — resolves: F47, F51 — test: F50

TOTALS:
- Claims tested: 3 (of 6 identified)
- Total findings: 53
- AR findings: 16 (4 necessary, 8 probable, 4 possible)
- AW findings: 8 (6 fatal, 2 serious, 0 conditional)
- Foreclosures: 2
- Bedrock reached: 15
- Tensions: 2
- Verdicts: 0 validated, 2 rejected, 0 damaged, 0 conditional, 1 uncertain
- CRUX points: 5

**PHASE 3: SYNTHESIS**

ORIGINAL INPUT: "Should I quit my job to start a startup?"

WHAT THE ANALYSIS ACTUALLY FOUND:

1. The question bundles at least 6 separate claims, 3 of which are load-bearing (C1, C4, C5)
2. All three load-bearing claims are either REJECTED or UNCERTAIN (F37, F51 fatal for C4 and C5; C1 uncertain)
3. You haven't validated the startup idea exists — no user conversations documented (F37->F40)
4. Full-time commitment before validation inverts risk logic (F51->F53)
5. Job problem may be recent frustration vs chronic misalignment — unverified (F14->F16)
6. Timeline of startup idea vs job frustration matters — if idea came after frustration, suggests motivated reasoning (F17->F19)
7. Internal transfer might solve job problem without startup risk (F10->F13)
8. Part-time validation is possible and strictly better than quitting first (F47->F50)

KEY TENSIONS:
1. F7 "cannot fix while staying" vs F10 "solvable within role" — TYPE: information gap
   - Resolution needed: Have you actually tried internal transfer? (F9, F13)
2. F28 "cannot pursue while employed" vs F47 "can validate part-time" — TYPE: commitment decision
   - Resolution: Validation (conversations) is possible part-time; building may require full-time

WEAKEST LINKS:
- F3 (probable): "Staying causes harm" — not verified, only claimed
- F15 (possible): "Temporary frustration" — depends on timeline check F16
- F42 (probable): "Competitor will capture market <6mo" — needs competitor analysis F43
- All AR claims about job problem rest on unverified observations (F4, F6, F9)

ALTERNATIVES DERIVED FROM ANALYSIS:
1. Internal transfer to different role/team — derived from F10->F13
2. Part-time validation for 3 months while employed — derived from F47->F50
3. Fix current role (if problem is positional not organizational) — derived from F10->F11

TESTABLE PREDICTIONS:
- If you complete 20 user interviews (F40), >50% will say "not a problem I have" or "current solution is fine" (based on F31, F37)
- If you check timeline (F19), startup idea will post-date job frustration by <3 months (based on F17, F18)
- If you track stress markers (F4), pattern will be recent spike, not chronic elevation (based on F14, F15)

DO_FIRST ACTIONS:
1. Timeline analysis — WHO: user — resolves: CRUX-2 (F19)
   - Check when job frustration started vs when startup idea emerged
2. User interview sprint — WHO: user — resolves: CRUX-3, CRUX-4 (F22, F40)
   - Schedule 20 interviews in next 30 days, document findings
3. Internal options check — WHO: user — resolves: CRUX-1 partially (F13)
   - List 3 internal roles that would solve the stated problem
4. Contract review — WHO: user — resolves: F30
   - Check employment contract for IP assignment, non-compete clauses
5. Part-time validation test — WHO: user — resolves: CRUX-5 (F50)
   - Attempt validation part-time for 90 days before considering quitting

UNRESOLVED:
- C1 stayed UNCERTAIN — needs F4, F6, F9, F16, F19 tests to determine verdict
- F41 "narrow window closing" stayed unverified — needs F43 competitor analysis
- Whether idea is feature vs company (F34->F36) needs market analysis

ANSWER TO ORIGINAL QUESTION:

**No. Do not quit yet.**

Not because the startup is bad (unknown), but because the question is unanswerable without running tests first. Three fatal gaps:

1. **No validation has occurred** (F37) — you don't know if users have this problem or will pay
2. **Irreversible before reversible** (F51->F53) — you're considering a one-way door before testing the idea
3. **Job problem is undiagnosed** (C1 uncertain) — could be fixable without quitting

The structure forced discovery of alternatives you cannot access by quitting:
- Internal transfer (F12->F13)
- Part-time validation (F49->F50)

These are dominated strategies (strictly better) until validation completes.

Next 30 days: Complete F40 (20 interviews), F19 (timeline check), F13 (internal options). If interviews reveal real demand and paying users, *then* revisit the question with validated C4.

---

### The Mechanism That Caught the Difference

**What standard approaches missed:**
- The question bundles 6 distinct claims that need separate evaluation
- "Quitting" and "startup" can be decoupled — validation can happen part-time
- The timing of idea emergence reveals motivated reasoning
- Internal transfer is a dominated alternative (better on all dimensions until validation completes)

**Which step in ARAW caught it:**

1. **Unbundling (Step 1)**: Separated "job problem exists" from "startup is solution" from "must quit to succeed" — standard LLM treats these as a single decision
2. **AW on C5**: F47-F51 discovered that full-time commitment before validation inverts risk logic — enhanced approach recommended "start as side project" but didn't explain why this is *logically necessary*
3. **FORECLOSURES in AR**: F7 "cannot fix while staying" was contradicted by AW finding F10 "solvable within role" — standard LLM never checks if the premises contradict
4. **Bedrock requirement**: F40 (20 user interviews) and F50 (validation milestones) are testable next steps, not opinions — standard LLM says "consider if validated" but doesn't operationalize what validation means
5. **Derived alternatives**: F12 (internal transfer) emerged from F10's wrongness analysis, not from brainstorming — enhanced approach listed "pros and cons" but missed the dominated strategy

The difference: ARAW forces explicit tests of what's presupposed (C4: "idea worth pursuing") and contradicts what seems obvious (C5: "must be full-time").

---

## Example 2: Technical Question
**"Why is my React app slow?"**

### What a Standard LLM Says

There are several common causes of React performance issues:

1. **Too many re-renders**: Components re-rendering unnecessarily
2. **Large component trees**: Deep nesting causing reconciliation overhead
3. **Unoptimized images**: Large images not lazy-loaded
4. **Expensive computations**: Heavy calculations in render
5. **Memory leaks**: Event listeners not cleaned up

**Solutions to try:**
- Use `React.memo()` to prevent unnecessary re-renders
- Implement `useMemo()` and `useCallback()` for expensive operations
- Use React DevTools Profiler to identify slow components
- Lazy load images and code-split routes
- Check for memory leaks in useEffect cleanup

Start with the Profiler to see which components are rendering most frequently, then optimize those first.

### What an "Enhanced" Approach Says (Multi-agent debate)

**Agent 1 (Performance):** The issue is likely unnecessary re-renders. I'd check if parent components are re-rendering and causing children to re-render. Use React.memo and profiling.

**Agent 2 (Architecture):** I disagree — premature optimization. The real issue might be the data fetching strategy. If they're fetching in components instead of at the route level, you get waterfall requests. Check the Network tab first.

**Agent 1:** Good point, but slow *rendering* and slow *loading* are different problems. The question says "React app slow" which typically means render performance.

**Agent 3 (Debugging):** You're both making assumptions. We should ask: slow doing *what*? Initial load? Interactions? Scrolling? The diagnosis changes completely based on this.

**Synthesis:**
1. First, characterize the slowness: initial load vs runtime performance
2. If initial load: check bundle size, code splitting, lazy loading
3. If runtime: profile renders, check for unnecessary state updates
4. If both: likely an architecture issue with data flow

Use Chrome DevTools Performance tab to record a trace, then decide next steps based on what the flamegraph shows.

### What UAUA Produces

**ORIGINAL INPUT:** "Why is my React app slow?"

**PHASE 1: EXPLORATION**

**U0: GROUND IN EXEMPLARS**

Fast React apps share: lazy loading, memoization of expensive operations, minimal prop drilling, route-level data fetching, virtualized long lists. They differ on state management, styling approaches.

Felt impression: "Slow" is vague — could mean 3s initial load (different root cause) vs 100ms input lag (different root cause). The question presupposes a single cause.

**U1: MAP THE SPACE**

[U1] EXPLICIT: React app has performance problem
[U2] IMPLICIT: The problem is in React code (not network, not backend)
[U3] PRESUPPOSED: "Slow" is a single phenomenon with single cause
[U4] BUNDLED: "Slow" bundles initial load + runtime interaction + state updates
[U5] META: Question asks for diagnosis without providing measurements

**STATE SPACE — What could "slow" mean?**
[U6] Slow initial load (time to interactive >3s)
[U7] Slow interactions (clicks feel laggy, >100ms response)
[U8] Slow scrolling/animations (janky, <60fps)
[U9] Slow state updates (UI doesn't update immediately after action)
[U10] Slow navigation (route changes take >500ms)
[U11] Memory bloat causing progressive slowdown
[U12] REFRAME: "Slow" is subjective — actual problem might be specific user complaint

**INSTANCE-TO-CATEGORY — What is this an instance of?**
[U13] React performance is instance of FRONTEND PERFORMANCE
[U14] Siblings: Vue perf, Angular perf, vanilla JS perf
[U15] If slow for ALL frameworks → problem is network/backend
[U16] If slow for ONLY React → problem is React-specific (over-rendering, reconciliation)

**PARAMETER VARIATION**
[U17] Parameter: device — current: unknown — range: high-end MacBook to low-end Android
[U18] Parameter: data size — current: unknown — range: 10 items to 10,000 items
[U19] Parameter: network speed — current: unknown — range: fiber to slow 3G
[U20] Parameter: app state complexity — current: unknown — range: simple to deeply nested

**ASSUMPTION EXTRACTION**
[U21] LOAD-BEARING: Problem is in React rendering — if false: wasting time optimizing render when issue is network
[U22] LOAD-BEARING: "Slow" is measurable — if false: chasing vague feeling, not actual issue
[U23] LOAD-BEARING: Slowness is consistent — if false: intermittent issue suggests race condition or memory leak
[U24] BACKGROUND: User has access to measure performance — probably true

**DIMENSION DISCOVERY**
[U25] Dimension: WHEN (initial load vs runtime vs progressive degradation)
[U26] Dimension: WHERE (which pages, which interactions)
[U27] Dimension: WHO (all users vs specific device/browser)
[U28] HIDDEN dimension: COMPARED TO WHAT (slow vs last week? vs competitor? vs expectation?)

**A1: TEST WITH ARAW**

**Candidate [U6]: "Slow initial load (>3s time to interactive)"**

ASSUME RIGHT:
[F1] If right: Problem is bundle size, code splitting, or asset loading — Necessary
  [F2] If F1: Check bundle size — should be <200KB initial — Necessary
    [F3] BEDROCK-TEST: Run `npm run build`, check main bundle size
  [F4] If F1: Check if lazy loading routes — Necessary
    [F5] BEDROCK-TEST: Inspect Network tab, count requests before interactive
[F6] If right: Lighthouse score shows "Time to Interactive" as bottleneck — Probable
  [F7] BEDROCK-TEST: Run Lighthouse, check TTI metric

ASSUME WRONG:
[F8] Wrong because: Initial load feels instant but interactions lag — Fatal
  [F9] Alternative derived from F8: Problem is runtime performance (U7)
    [F10] BEDROCK-TEST: Measure time from page load to first interaction
[F11] Wrong because: Load time is fine on desktop, slow on mobile — Conditional
  [F12] Alternative derived from F11: Problem is device-specific (U17)
    [F13] BEDROCK-TEST: Test on actual mobile device, compare metrics

**Candidate [U7]: "Slow interactions (clicks feel laggy)"**

ASSUME RIGHT:
[F14] If right: Problem is re-render overhead or expensive sync work — Necessary
  [F15] If F14: Profiler shows long render times after interactions — Necessary
    [F16] BEDROCK-TEST: React DevTools Profiler, record interaction, check render duration
  [F17] If F14: Specific components render on every state change — Probable
    [F18] BEDROCK-TEST: Profiler flame graph shows which components rendered
[F19] FORECLOSED if right: Problem is NOT network or backend — Necessary
  [F20] If F19: Backend response time is <100ms — Probable
    [F21] BEDROCK-TEST: Network tab shows API response times

ASSUME WRONG:
[F22] Wrong because: The lag is waiting for API response, not rendering — Fatal
  [F23] If F22: Network tab shows >500ms API calls — Probable
    [F24] Alternative derived from F22: Problem is backend performance (not React)
      [F25] BEDROCK-TEST: Inspect Network tab waterfall during interaction
[F26] Wrong because: Lag only happens after app runs for 10+ minutes — Conditional
  [F27] Alternative derived from F26: Memory leak causing progressive slowdown (U11)
    [F28] BEDROCK-TEST: Chrome DevTools Memory tab, take heap snapshots over time

**Candidate [U2]: "The problem is in React code (not network, not backend)"**

ASSUME RIGHT:
[F29] If right: Network is fast and backend responds quickly — Necessary
  [F30] BEDROCK-TEST: Network tab shows all requests <200ms
[F31] If right: Slowness persists with backend mocked — Necessary
  [F32] BEDROCK-TEST: Mock API responses with instant returns, check if still slow

ASSUME WRONG:
[F33] Wrong because: Backend is slow and React is waiting — Fatal
  [F34] If F33: React app shows loading spinners for >2s — Probable
    [F35] Alternative derived from F33: Optimize backend or add caching
      [F36] BEDROCK-TEST: Profile backend endpoint response times
[F37] Wrong because: Network is slow (user on 3G) — Conditional
  [F38] Alternative derived from F37: Problem is network, not React
    [F39] BEDROCK-TEST: Test on fast network, check if slowness disappears

**U2: FIND EDGE CASES**

[E1] Boundary: App is fast with <100 items, slow with >1000 items in list
[E2] Scale failure: Performance degrades linearly with number of items (O(n) render)
[E3] Temporal limit: App gets progressively slower over 30 minutes
[E4] Context dependency: Only slow on mobile Chrome, fine on desktop Firefox
[E5] Stakeholder conflict: Developers think it's fast, users think it's slow

**A2: VALIDATE EDGE CASES**

[E1] "App is fast with <100 items, slow with >1000"
  [F40] AR: List rendering without virtualization — Necessary
    [F41] BEDROCK-TEST: Check if using react-window or virtualization
  [F42] AW: Problem is data fetching, not rendering
    [F43] BEDROCK-TEST: Mock 10,000 items locally, check render time

[E5] "Developers think it's fast, users think it's slow"
  [F44] AR: Developers test on high-end machines — Probable
    [F45] BEDROCK-TEST: Check device specs of dev machines vs user devices
  [F46] AW: Users expect <50ms response, devs think <200ms is fine
    [F47] BEDROCK-TEST: Measure actual response times, compare to user expectations

**PHASE 2: FINDING REGISTRY**

FINDING REGISTRY
================

UNBUNDLED CLAIMS:
[U1] React app has performance problem — TYPE: explicit
[U2] The problem is in React code — TYPE: implicit
[U3] "Slow" is single phenomenon — TYPE: presupposed
[U4] "Slow" bundles initial load + runtime + state updates — TYPE: bundled

CANDIDATES (from U1 mapping):
[U6] Slow initial load (>3s TTI) — SOURCE: state space
[U7] Slow interactions (clicks laggy) — SOURCE: state space
[U11] Memory bloat progressive slowdown — SOURCE: state space
[U12] "Slow" is subjective user complaint — SOURCE: reframe

ASSUMPTIONS:
[U21] Problem is in React rendering — LOAD-BEARING — if false: optimizing wrong layer
[U22] "Slow" is measurable — LOAD-BEARING — if false: chasing vague feeling
[U23] Slowness is consistent — LOAD-BEARING — if false: intermittent issue

DIMENSIONS:
[U25] WHEN (initial vs runtime vs degradation)
[U26] WHERE (which pages/interactions)
[U27] WHO (all users vs specific device/browser)
[U28] COMPARED TO WHAT (baseline) — HIDDEN

AR FINDINGS:
[F1] Problem is bundle size or code splitting — STRENGTH: necessary — PARENT: U6
[F14] Problem is re-render overhead — STRENGTH: necessary — PARENT: U7
[F29] Network is fast and backend responds quickly — STRENGTH: necessary — PARENT: U2
[F40] List rendering without virtualization — STRENGTH: necessary — PARENT: E1

FORECLOSURES:
[F19] Problem is NOT network or backend — PARENT: U7

AW FINDINGS:
[F8] Initial load instant but interactions lag — SEVERITY: fatal — PARENT: U6
[F22] Lag is waiting for API, not rendering — SEVERITY: fatal — PARENT: U7
[F33] Backend is slow, React is waiting — SEVERITY: fatal — PARENT: U2
[F37] Network is slow (user on 3G) — SEVERITY: conditional — PARENT: U2

DERIVED ALTERNATIVES:
[F9] Problem is runtime performance — DERIVED FROM: F8
[F24] Problem is backend performance — DERIVED FROM: F22
[F27] Memory leak causing progressive slowdown — DERIVED FROM: F26
[F35] Optimize backend or add caching — DERIVED FROM: F33
[F38] Problem is network, not React — DERIVED FROM: F37

EDGE CASES:
[E1] Fast <100 items, slow >1000 items — TYPE: boundary
[E3] Progressively slower over 30 minutes — TYPE: temporal
[E5] Devs think fast, users think slow — TYPE: stakeholder conflict

BEDROCK REACHED:
[F3] Run build, check bundle size
[F5] Count requests before interactive
[F7] Run Lighthouse, check TTI
[F10] Measure load to first interaction
[F13] Test on mobile device
[F16] React Profiler record interaction
[F21] Network tab API response times
[F25] Network tab waterfall during interaction
[F28] Chrome Memory tab heap snapshots
[F30] Network tab all requests <200ms
[F32] Mock API responses, check if slow
[F36] Profile backend response times
[F39] Test on fast network
[F41] Check if using virtualization
[F43] Mock 10k items, check render time
[F45] Compare dev vs user device specs
[F47] Measure response times vs expectations

TENSIONS:
[F19] "NOT network/backend" contradicts [F33] "backend is slow"

CANDIDATE VERDICTS:
[U6] Slow initial load — UNCERTAIN — needs F3, F7 tests
[U7] Slow interactions — UNCERTAIN — needs F16, F21, F25 tests
[U2] Problem is React code — REJECTED — F33 fatal if backend is actually slow
[U21] Problem is React rendering — UNCERTAIN — needs F16, F32 tests to verify

TOTALS:
- Unbundled claims: 4
- Candidates mapped: 12
- Assumptions: 3 (3 load-bearing)
- Dimensions: 4 (1 hidden)
- AR findings: 11
- AW findings: 7 (4 fatal, 1 serious, 2 conditional)
- Foreclosures: 1
- Derived alternatives: 5
- Edge cases: 5
- Bedrock reached: 17
- Tensions: 1
- Verdicts: 0 validated, 1 rejected, 0 damaged, 0 conditional, 3 uncertain

**PHASE 3: SYNTHESIS**

ORIGINAL INPUT: "Why is my React app slow?"

SPACE SIZE: 47 unique findings

WHAT THE ANALYSIS ACTUALLY FOUND:

1. "Slow" is unbundled into at least 4 distinct phenomena (U6, U7, U9, U10) with different root causes
2. The question presupposes problem is in React (U2), but U21 could be false — might be backend/network
3. Cannot diagnose without measurements — 17 bedrock tests identified (F3, F5, F7, F10, F13, etc.)
4. Hidden dimension: "slow compared to WHAT?" (U28) — might be user expectation mismatch (E5)
5. Three load-bearing assumptions (U21, U22, U23) are all unverified
6. Edge case E1 suggests O(n) rendering without virtualization
7. Edge case E3 suggests memory leak (progressive degradation)
8. Tension between F19 (not backend) and F33 (backend is slow) cannot resolve without F21, F30, F32 tests

KEY TENSIONS:
1. F19 "NOT network/backend" vs F33 "backend is slow" — TYPE: information gap
   - Resolution: Run F21 (Network tab), F30 (check all requests), F32 (mock backend)

VOI RANKING (what matters most):
1. F32 (mock backend, check if still slow) — determines if React or backend issue
2. F16 (React Profiler during interaction) — shows if re-render overhead
3. F28 (heap snapshots over time) — detects memory leak (E3)
4. F21 (API response times) — determines if waiting for backend
5. F41 (check virtualization) — explains E1 (slow with many items)

LOAD-BEARING ASSUMPTIONS:
[U21] Problem is in React rendering — if false, all React optimizations are wasted
[U22] "Slow" is measurable — if false, cannot diagnose objectively
[U23] Slowness is consistent — if false, different diagnosis (race condition, leak)

HIDDEN DIMENSIONS:
[U28] Compared to what baseline — affects whether problem is real or expectation mismatch

WEAKEST LINKS:
- F2 "should be <200KB" — this is rule of thumb, not fundamental
- F20 "backend <100ms" — probable but unverified
- F34 "loading spinners >2s" — observable but unchecked
- All AR findings about root cause rest on unverified measurements

ALTERNATIVES DERIVED FROM ANALYSIS:
1. Optimize backend or add caching — derived from F33->F35
2. Use virtualization for lists — derived from E1->F40
3. Fix memory leak — derived from F26->F27
4. Improve network (CDN, compression) — derived from F37->F38
5. Calibrate user expectations — derived from E5->F47

TESTABLE PREDICTIONS:
- If you run F32 (mock backend) and slowness disappears, root cause is backend (F33), not React
- If you run F28 (heap snapshots) and memory grows linearly, root cause is leak (F27)
- If you run F41 (check virtualization) and it's missing, adding it will fix E1
- If you run F16 (Profiler) and see <16ms render times, problem is NOT rendering

DO_FIRST ACTIONS:
1. Characterize "slow" with measurements — WHO: user — resolves: U22, U28
   - Open Chrome DevTools Performance tab, record 10s of interaction, note:
     - Time to Interactive (initial load)
     - Input latency (time from click to visual update)
     - Frame rate during scrolling
   - Establish baseline: what's the target? (users expect what?)
2. Test with mocked backend — WHO: user — resolves: F32 (highest VOI)
   - Replace all API calls with instant mock responses
   - If still slow → React issue; if fast → backend issue
3. Profile React renders — WHO: user — resolves: F16
   - React DevTools Profiler, record interaction, identify:
     - Which components rendered?
     - How long did each take?
     - Were renders necessary?
4. Check for memory leak — WHO: user — resolves: F28
   - Chrome Memory tab, take snapshots every 5 minutes
   - If heap grows without bound → leak; if stable → not leak
5. Test virtualization hypothesis — WHO: user — resolves: F41, E1
   - Check if long lists use react-window or similar
   - Test with 10,000 mocked items, measure render time

UNRESOLVED:
- All candidates stayed UNCERTAIN — need measurement before diagnosis
- Whether U21 (React is the problem) is true — F32 test will resolve
- What "slow" means precisely — need U28 baseline established
- Edge case E4 (only slow on mobile Chrome) not tested

ANSWER TO ORIGINAL QUESTION:

**Cannot answer "why" without measurements. Here's the diagnostic tree:**

The question presupposes a single cause, but "slow" bundles at least 4 distinct issues (initial load, interaction lag, scrolling jank, progressive degradation), each with different root causes.

**Diagnosis procedure (run in order):**

1. **Characterize the slowness** (DO_FIRST action 1):
   - WHAT: Initial load? Interaction lag? Scrolling? Progressive?
   - WHEN: Always? After 10 min? With >1000 items?
   - WHERE: All pages? Specific interactions?
   - WHO: All users? Mobile only? Slow devices?
   - Record metrics: TTI, input latency, FPS, memory over time

2. **Isolate the layer** (DO_FIRST action 2):
   - Mock all backend responses with instant returns
   - If still slow → proceed to step 3 (React issue)
   - If fast → root cause is backend/network, not React

3. **If React issue, profile renders** (DO_FIRST action 3):
   - React DevTools Profiler during slow interaction
   - If render times >16ms → re-render overhead (F14)
   - If render times <16ms → problem elsewhere (check F28)

4. **Check specific patterns**:
   - Long lists without virtualization → E1, F41
   - Memory growing over time → E3, F28
   - Device-specific → E4, F45

**Why standard approach failed:**
- Jumped to solutions ("use React.memo") without measurements
- Assumed problem was in React (U2) without testing backend (F32)
- Didn't unbundle "slow" into distinct phenomena (U6, U7, U9, U10)
- Missed hidden dimension U28 (slow compared to what?)
- Didn't detect tension between "rendering is slow" and "waiting for API"

**Why enhanced approach was better but insufficient:**
- Multi-agent debate surfaced "slow at what?" question
- Identified initial load vs runtime as different problems
- Recommended profiling before optimizing
- BUT: didn't systematize all possibilities, didn't identify bedrock tests, didn't catch load-bearing assumptions

**What UAUA forced:**
- Unbundling "slow" into 12 candidate states (U6-U12)
- Finding hidden dimension U28 (baseline)
- 17 bedrock tests that are actually runnable
- VOI ranking of tests (F32 highest value)
- Detection of load-bearing assumption U21 (might not be React at all)

The structure forced "measure before diagnose" as logically necessary (U22), not just best practice.

---

### The Mechanism That Caught the Difference

**What standard approaches missed:**
- "Slow" is vague and bundles multiple distinct performance issues
- The problem might not be in React at all (could be backend, network, device)
- Cannot diagnose without measurements — need specific tests
- Hidden dimension: "slow compared to what baseline?"

**Which step in UAUA caught it:**

1. **U1 Unbundling**: Separated "slow" into U6 (initial load), U7 (interactions), U9 (state updates), U10 (navigation), U11 (memory), U12 (subjective) — standard LLM treats as single issue
2. **Assumption Extraction**: U21 "problem is in React rendering" is load-bearing and unverified — if false, all React optimizations are wasted
3. **AW on U2**: F33 "backend is slow" is fatal if true — standard LLM presupposes React is the problem
4. **Bedrock Tests**: F32 (mock backend) is testable and resolves the highest VOI question — enhanced approach said "use profiler" but didn't operationalize all tests
5. **Hidden Dimension Discovery**: U28 "slow compared to what?" reveals potential expectation mismatch (E5) — standard LLM doesn't question the baseline
6. **Edge Cases**: E1 (fast <100, slow >1000) and E3 (progressive degradation) point to specific root causes — standard LLM lists possibilities but doesn't map the full space

The difference: UAUA forces "what are all the ways this could be slow?" before "how to fix", and discovers that the presupposed problem (React) might be wrong (U21, F32).

---

## Example 3: High Emotional Stake (Motivated Reasoning)
**"I think my co-founder isn't pulling their weight. Should I confront them?"**

### What a Standard LLM Says

This is a difficult situation that requires careful handling. Here's how to approach it:

**Consider first:**
- Are they aware of your concerns?
- Could there be circumstances you're not aware of (personal issues, health, burnout)?
- Is this a recent change or ongoing pattern?
- Have you clearly defined roles and expectations?

**Before confronting:**
1. Document specific examples of the behavior
2. Reflect on your own contribution — are you being fair?
3. Check your startup's equity split and vesting schedule
4. Consider what outcome you want: improvement, role change, or separation?

**How to have the conversation:**
- Use "I" statements: "I've noticed..." not "You never..."
- Be specific about behaviors, not character
- Listen to their perspective
- Focus on solutions, not blame
- Agree on clear next steps and check-ins

**If it doesn't improve:**
- Consider bringing in a neutral advisor or mediator
- Review your operating agreement
- In worst case, discuss transition or buyout

The fact that you're asking suggests this needs to be addressed. Avoiding it will likely make it worse. Approach with empathy but clarity.

### What an "Enhanced" Approach Says (Devil's advocate)

Let me challenge your framing first:

**What if you're wrong about "not pulling their weight"?**
- Are you measuring the same way? Engineering output is visible (commits), but strategy work isn't
- Could you be experiencing founder's paranoia? (Common when stressed)
- Are you comparing their work to yours unfairly?

**What if you're right, but confrontation makes it worse?**
- If they're already checked out, confrontation might accelerate departure
- You could create a hostile dynamic right when you need cohesion
- The equity split doesn't change even if they leave

**Alternative framings:**
1. Instead of "not pulling weight" → "We're misaligned on what matters now"
2. Instead of "confront" → "Sync on priorities and workload"
3. Instead of fixing them → "What would need to be different for us both to feel good about progress?"

**But also:**
- If your gut says something is wrong, it usually is
- Avoiding hard conversations destroys companies
- The longer you wait, the worse the resentment gets

**My synthesis:**
Start with curiosity, not confrontation. Ask: "I've been feeling like we're out of sync lately. How are you feeling about your work and the company direction?" Their answer will tell you if this is a misunderstanding, a fixable problem, or a terminal issue.

Document your observations either way — if you're right, you'll need it later. If you're wrong, examining your thinking will prevent future misfires.

### What ARAW Produces

**ORIGINAL INPUT:** "I think my co-founder isn't pulling their weight. Should I confront them?"

**STEP 0: META-ARAW**

**Restate:** You believe your co-founder is underperforming and are deciding whether to address it directly.

**Evaluability:** This bundles claims ("they're underperforming") with decisions ("confront them") with presuppositions ("confrontation is the intervention"). Need to unbundle.

**Uncertainty type:** Epistemic (do they know? why is this happening?) + aleatoric (how will they react?) + model (is "confrontation" the right frame?)

**Pitfalls check:**
- **Fish in dreams**: You want the answer to be "yes, confront" because you're frustrated and want validation
- **Red herring**: Your explanation ("not pulling weight") might match your frustration without being the actual cause
- **Motivated reasoning**: High emotional stake — you're angry/resentful, which biases toward confirming "they're the problem"

**STEP 1: UNBUNDLE CLAIMS**

[C1] My co-founder is underperforming relative to expectations — TYPE: explicit — VOI: critical
[C2] I have accurate visibility into their work — TYPE: presupposed — VOI: critical
[C3] The expectations I'm measuring against are fair and agreed-upon — TYPE: presupposed — VOI: high
[C4] Their underperformance (if true) is due to lack of effort, not circumstance — TYPE: implicit — VOI: high
[C5] "Confrontation" is the right intervention — TYPE: presupposed — VOI: high
[C6] Confronting will improve the situation more than alternatives — TYPE: implicit — VOI: high
[C7] The problem is them, not me or the situation — TYPE: implicit — VOI: critical

**PHASE 1: EXPLORATION**

**[C2] "I have accurate visibility into their work"**

ASSUME RIGHT:
[F1] If right: You see all their work or have good proxy metrics — Necessary
  [F2] If F1: You attend all meetings, see all outputs, track all contributions — Necessary
    [F3] BEDROCK-TEST: List everything they did this week — if can't, visibility is incomplete
  [F4] If F1: Their work is visible (code, docs) not invisible (strategy, partnerships) — Conditional
    [F5] BEDROCK-OBSERVE: What % of their role is visible work vs invisible work?

ASSUME WRONG:
[F6] Wrong because: They're doing critical work you can't see — Fatal
  [F7] If F6: Their work is strategic (thinking, recruiting, investor relations) not tactical — Probable
    [F8] Alternative derived from F6: Ask them what they worked on this week
      [F9] BEDROCK-TEST: Have them share weekly update, note what you didn't know
  [F10] Wrong because: You're measuring your work (output) against their work (relationships) — Fatal
    [F11] If F10: You write code, they do sales/partnerships — outputs aren't comparable — Probable
      [F12] BEDROCK-OBSERVE: Are you both in same functional role or different roles?
  [F13] Wrong because: Confirmation bias — you notice when they're not working, don't notice when they are — Serious
    [F14] If F13: Recent frustration primed you to see evidence of laziness — Probable
      [F15] BEDROCK-OBSERVE: When did you start feeling this? What triggered it?

**[C7] "The problem is them, not me or the situation"**

ASSUME RIGHT:
[F16] If right: Your own effort and judgment are calibrated correctly — Necessary
  [F17] If F16: You're working sustainable hours and not burning out — Probable
    [F18] BEDROCK-TEST: Track your hours for 1 week — if >60hr/week, you're over-indexed on work
  [F19] If F16: You're not projecting your own overwork onto them — Probable
    [F20] BEDROCK-LOGIC: If you work 70hr/week and they work 40hr/week, gap might be your hours, not theirs
[F21] FORECLOSED if right: You cannot solve this by changing your own behavior — Necessary

ASSUME WRONG:
[F22] Wrong because: You're burned out and bitter, seeing slacking where there's normal work — Fatal
  [F23] If F22: You've been stressed, sleeping poorly, feeling resentful — Probable
    [F24] BEDROCK-OBSERVE: Rate your stress 1-10, sleep quality, resentment level over past month
  [F25] Wrong because: You're overworking and expecting them to match — Serious
    [F26] If F25: You work nights/weekends, they don't, you resent this — Probable
      [F27] Alternative derived from F25: Calibrate your own hours down, not theirs up
        [F28] BEDROCK-TEST: Reduce your hours to 45/week for 2 weeks, see if resentment decreases
  [F29] Wrong because: Situation is hard, both of you are struggling, you're externalizing — Fatal
    [F30] If F29: Startup is stalled, metrics flat, money tight — creates blame dynamic — Probable
      [F31] Alternative derived from F29: The problem is startup strategy, not co-founder effort
        [F32] BEDROCK-TEST: Check metrics — if growth is flat, problem is product-market fit, not effort

**[C4] "Their underperformance is due to lack of effort, not circumstance"**

ASSUME RIGHT:
[F33] If right: They have capacity but choose not to work — Necessary
  [F34] If F33: No personal crises, health issues, or external demands — Necessary
    [F35] BEDROCK-TEST: Ask directly: "Are you dealing with anything that's affecting your bandwidth?"
  [F36] If F33: They've lost motivation for this specific startup — Probable
    [F37] BEDROCK-OBSERVE: Do they still talk excitedly about the mission? Bring up new ideas?

ASSUME WRONG:
[F38] Wrong because: They're dealing with personal crisis you don't know about — Fatal
  [F39] If F38: Health issue, family crisis, mental health, burnout — Probable
    [F40] BEDROCK-TEST: F35 question will reveal this
  [F41] Wrong because: They're working but on wrong things (not aligned) — Serious
    [F42] If F41: They think they're productive, you think they're not — both could be true — Probable
      [F43] Alternative derived from F41: Misalignment on priorities, not effort
        [F44] BEDROCK-TEST: Ask "What are your top 3 priorities this month?" — compare to yours
  [F45] Wrong because: They've correctly assessed the startup is failing and reduced effort — Conditional
    [F46] If F45: Metrics are bad, runway is short, they're hedging — Probable
      [F47] Alternative derived from F45: Problem is startup viability, not co-founder work ethic
        [F48] BEDROCK-TEST: Check metrics, runway — if <6mo runway and flat growth, their assessment is correct

**[C5] "'Confrontation' is the right intervention"**

ASSUME RIGHT:
[F49] If right: Direct challenge will prompt behavior change — Necessary
  [F50] If F49: They're unaware of the problem and will course-correct when told — Probable
    [F51] BEDROCK-TEST: Have you given them feedback before? Did they adjust?
[F52] FORECLOSED if right: Softer approaches (curiosity, sync) won't work — Conditional
  [F53] If F52: You've already tried gentle nudges without effect — Probable
    [F54] BEDROCK-TEST: Document previous attempts to address this — if none, you haven't tried

ASSUME WRONG:
[F55] Wrong because: "Confrontation" will make them defensive, not reflective — Fatal
  [F56] If F55: Human psychology — accusations trigger defensiveness, not openness — Necessary
    [F57] Alternative derived from F55: Curiosity ("how are you feeling about work?") before confrontation
      [F58] BEDROCK-LOGIC: Questions discover, accusations defend — confrontation forecloses learning
  [F59] Wrong because: Confrontation is your emotional release, not problem-solving — Fatal
    [F60] If F59: You want to express frustration, calling it "feedback" — Probable
      [F61] BEDROCK-OBSERVE: Do you want them to change, or do you want to feel heard/validated?
  [F62] Wrong because: If they're checked out, confrontation accelerates departure — Conditional
    [F63] If F62: They're already considering leaving, confrontation is last straw — Possible
      [F64] Alternative derived from F62: Understand their state first, then decide intervention
        [F65] BEDROCK-TEST: Ask "How are you feeling about the company and your role?" first

**[C3] "The expectations I'm measuring against are fair and agreed-upon"**

ASSUME RIGHT:
[F66] If right: You both explicitly agreed on roles, hours, deliverables — Necessary
  [F67] If F66: You have written role definitions or verbal agreement documented — Probable
    [F68] BEDROCK-TEST: Produce the document or note where you agreed on expectations
  [F69] If F66: Their current behavior violates those agreements — Necessary
    [F70] BEDROCK-TEST: List specific examples of agreement violation

ASSUME WRONG:
[F71] Wrong because: Expectations are implicit (in your head) not explicit (agreed) — Fatal
  [F72] If F71: You never actually defined what "pulling weight" means — Probable
    [F73] Alternative derived from F71: Co-create explicit expectations now
      [F74] BEDROCK-TEST: Schedule working session to define roles, hours, deliverables together
  [F75] Wrong because: Expectations were set at founding but situation changed — Serious
    [F76] If F75: Company stage is different (pre-revenue then, scaling now) — Probable
      [F77] Alternative derived from F75: Re-negotiate expectations for current stage
        [F78] BEDROCK-TEST: Ask "What did we expect at founding? What do we need now? Are they different?"

**PHASE 2: FINDING REGISTRY**

FINDING REGISTRY
================

CLAIMS TESTED:
[C1] Co-founder is underperforming — TYPE: explicit — VOI: critical
[C2] I have accurate visibility — TYPE: presupposed — VOI: critical
[C3] Expectations are fair and agreed — TYPE: presupposed — VOI: high
[C4] Due to lack of effort, not circumstance — TYPE: implicit — VOI: high
[C5] Confrontation is right intervention — TYPE: presupposed — VOI: high
[C7] Problem is them, not me/situation — TYPE: implicit — VOI: critical

AR FINDINGS (Implications):
[F1] You see all their work — STRENGTH: necessary — PARENT: C2
[F16] Your effort and judgment calibrated — STRENGTH: necessary — PARENT: C7
[F33] They have capacity but choose not to work — STRENGTH: necessary — PARENT: C4
[F49] Direct challenge will prompt change — STRENGTH: necessary — PARENT: C5
[F66] You both agreed on roles/hours/deliverables — STRENGTH: necessary — PARENT: C3

AR FINDINGS (Foreclosures):
[F21] Cannot solve by changing your own behavior — PARENT: C7
[F52] Softer approaches won't work — PARENT: C5

AW FINDINGS (Wrongness Reasons):
[F6] They're doing critical work you can't see — SEVERITY: fatal — PARENT: C2
[F10] Measuring your output vs their relationships — SEVERITY: fatal — PARENT: C2
[F13] Confirmation bias — SEVERITY: serious — PARENT: C2
[F22] You're burned out and bitter — SEVERITY: fatal — PARENT: C7
[F25] You're overworking, expecting them to match — SEVERITY: serious — PARENT: C7
[F29] Situation is hard, you're externalizing blame — SEVERITY: fatal — PARENT: C7
[F38] They're dealing with personal crisis — SEVERITY: fatal — PARENT: C4
[F41] Working on wrong things (misaligned) — SEVERITY: serious — PARENT: C4
[F45] Correctly assessed startup is failing — SEVERITY: conditional — PARENT: C4
[F55] Confrontation triggers defensiveness — SEVERITY: fatal — PARENT: C5
[F59] Confrontation is your emotional release — SEVERITY: fatal — PARENT: C5
[F62] Confrontation accelerates departure — SEVERITY: conditional — PARENT: C5
[F71] Expectations are implicit, not agreed — SEVERITY: fatal — PARENT: C3
[F75] Expectations were set at founding, situation changed — SEVERITY: serious — PARENT: C3

BEDROCK REACHED:
[F3] List everything they did this week
[F5] What % visible vs invisible work
[F9] Have them share weekly update
[F12] Are you same or different functional roles
[F15] When did frustration start, what triggered
[F18] Track your hours for 1 week
[F20] LOGIC: Gap might be your hours, not theirs
[F24] Rate stress, sleep, resentment over month
[F28] Reduce hours to 45/week for 2 weeks
[F32] Check metrics — if flat, problem is PMF
[F35] Ask about bandwidth/personal issues
[F37] Do they talk excitedly about mission
[F40] F35 question reveals crisis
[F44] Ask their top 3 priorities, compare
[F48] Check runway and growth
[F51] Have you given feedback before, did they adjust
[F54] Document previous attempts
[F58] LOGIC: Questions discover, accusations defend
[F61] Do you want change or validation
[F65] Ask how they're feeling first
[F68] Produce written role agreement
[F70] List examples of agreement violation
[F74] Co-create expectations in working session
[F78] Expectations at founding vs now

TENSIONS:
[F21] "cannot solve by changing your behavior" contradicts [F27] "calibrate your hours down"
[F16] "your judgment is calibrated" contradicts [F22] "you're burned out and bitter"

CLAIM VERDICTS:
[C2] I have accurate visibility — REJECTED
  -- AR evidence: F1 necessary but unverified
  -- AW evidence: F6, F10 fatal — invisible work, incomparable roles
  -- Verdict derived from: F3, F9, F12 tests will likely reveal incomplete visibility

[C7] Problem is them, not me/situation — REJECTED
  -- AR evidence: F16 necessary but unverified
  -- AW evidence: F22, F29 fatal if true — burned out, externalizing blame
  -- Verdict derived from: F18, F24, F32 tests will likely reveal your overwork or situation stress

[C4] Due to lack of effort, not circumstance — UNCERTAIN
  -- AR evidence: F33->F34 necessary but unverified
  -- AW evidence: F38 fatal if true, F41 serious
  -- Verdict derived from: Cannot determine without F35, F44, F48 tests

[C5] Confrontation is right intervention — REJECTED
  -- AR evidence: F49 necessary but unverified
  -- AW evidence: F55, F59 fatal — triggers defense, is emotional release
  -- Verdict derived from: F58 logical necessity — curiosity before confrontation

[C3] Expectations are fair and agreed — REJECTED
  -- AR evidence: F66 necessary but unverified
  -- AW evidence: F71 fatal if true — likely implicit, not agreed
  -- Verdict derived from: F68 test will likely fail to produce written agreement

CRUX POINTS:
[CRUX-1] Do you have complete visibility into their work? — resolves: C2, F6, F10 — test: F3, F9, F12
[CRUX-2] Are you burned out and projecting? — resolves: C7, F22, F25 — test: F18, F24, F28
[CRUX-3] Are expectations explicit or implicit? — resolves: C3, F71 — test: F68
[CRUX-4] Are they dealing with personal crisis? — resolves: C4, F38 — test: F35
[CRUX-5] Are you misaligned on priorities? — resolves: C4, F41 — test: F44
[CRUX-6] What's their emotional state about the company? — resolves: C4, F45 — test: F37, F65
[CRUX-7] Is the startup itself failing? — resolves: C7, F29, F45 — test: F32, F48

TOTALS:
- Claims tested: 6
- Total findings: 78
- AR findings: 12 (7 necessary, 5 probable)
- AW findings: 14 (9 fatal, 5 serious, 2 conditional)
- Foreclosures: 2
- Derived alternatives: 8
- Bedrock reached: 25
- Tensions: 2
- Verdicts: 0 validated, 4 rejected, 0 damaged, 0 conditional, 1 uncertain
- CRUX points: 7

**PHASE 3: SYNTHESIS**

ORIGINAL INPUT: "I think my co-founder isn't pulling their weight. Should I confront them?"

WHAT THE ANALYSIS ACTUALLY FOUND:

1. You don't have complete visibility into their work (C2 REJECTED) — F3, F9, F12 tests likely reveal invisible work
2. "Confrontation" is wrong intervention (C5 REJECTED) — F55, F59 fatal: triggers defense, is emotional release
3. Expectations are likely implicit, not agreed (C3 REJECTED) — F68 test will fail to produce written agreement
4. Problem might be you (burned out, overworking) not them (C7 REJECTED) — F22, F25, F29 plausible
5. Cannot determine if it's effort vs circumstance without asking (C4 UNCERTAIN) — F35, F44 tests required
6. Seven CRUX points must resolve before any intervention

KEY TENSIONS:
1. F16 "your judgment is calibrated" vs F22 "you're burned out and bitter" — TYPE: self-assessment gap
   - Resolution: F18, F24 tests will reveal if you're overworking and stressed
2. F21 "cannot solve by changing yourself" vs F27 "calibrate hours down" — TYPE: locus of control
   - Resolution: F28 experiment — if reducing your hours decreases resentment, problem is you

VOI RANKING (what matters most):
1. F35 (ask about bandwidth/personal issues) — if crisis, entire framing is wrong
2. F18, F24 (check your own burnout) — if burned out, perception is unreliable
3. F32, F48 (check startup metrics) — if failing, both are rational to reduce effort
4. F12 (same or different roles) — if different, comparison is invalid
5. F44 (check priority alignment) — if misaligned, problem is coordination not effort

WEAKEST LINKS:
- F7 "their work is strategic" — probable but unverified, F9 test will reveal
- F14 "recent frustration primed you" — probable but unchecked, F15 test will reveal
- F23 "stressed, sleeping poorly" — probable but unchecked, F24 test will reveal
- F50 "will course-correct when told" — probable but unverified, F51 test will check history

ALTERNATIVES DERIVED FROM ANALYSIS:
1. Ask them what they worked on this week — derived from F6->F8
2. Calibrate your own hours down — derived from F25->F27
3. Address startup strategy, not co-founder effort — derived from F29->F31
4. Curiosity before confrontation — derived from F55->F57
5. Understand their state first — derived from F62->F64
6. Co-create explicit expectations — derived from F71->F73
7. Re-negotiate expectations for current stage — derived from F75->F77
8. Ask "How are you feeling about the company?" — derived from F64->F65

TESTABLE PREDICTIONS:
- If you run F3 (list their work), you'll realize you can't account for >50% of their time (based on F6)
- If you run F18 (track hours), you're working >60hr/week (based on F22, F25)
- If you run F24 (rate stress/sleep), your stress is 7+/10, sleep is poor (based on F22)
- If you run F68 (produce written expectations), no document exists (based on F71)
- If you run F35 (ask about personal issues), they'll reveal something significant (based on F38)

DO_FIRST ACTIONS:
1. Self-check for burnout — WHO: user — resolves: CRUX-2 (F18, F24)
   - Track hours this week (expect >60)
   - Rate stress 1-10, sleep quality, resentment level (expect high)
   - If burned out, your perception is unreliable — fix yourself before addressing them
2. Check startup health — WHO: user — resolves: CRUX-7 (F32, F48)
   - Review metrics: growth rate, runway, key milestones
   - If failing (<6mo runway, flat growth), reducing effort is rational response
3. Visibility test — WHO: user — resolves: CRUX-1 (F3, F9, F12)
   - List everything they did this week from memory
   - Ask them for weekly update
   - Compare — gap reveals invisible work
4. Curiosity conversation (not confrontation) — WHO: user — resolves: CRUX-4, CRUX-6 (F35, F37, F65)
   - "How are you feeling about the company and your role?"
   - "Are you dealing with anything that's affecting your bandwidth?"
   - "What are your top 3 priorities this month?"
   - Their answers will reveal: personal crisis (F35), motivation (F37), alignment (F44)
5. Expectations audit — WHO: user — resolves: CRUX-3 (F68, F74)
   - Try to produce written role agreement (prediction: doesn't exist)
   - Schedule working session to co-create explicit expectations

UNRESOLVED:
- C1 "co-founder is underperforming" — cannot evaluate until C2, C3, C7 resolve
- Whether F38 (personal crisis) is true — F35 will reveal
- Whether F71 (implicit expectations) is true — F68 will reveal
- Your own state (burned out?) — F18, F24 will reveal

ANSWER TO ORIGINAL QUESTION:

**No. Do not confront them. Run diagnostics first.**

Four of six load-bearing claims were REJECTED:
- C2: You likely don't have complete visibility (F6, F10 fatal)
- C3: Expectations likely implicit, not agreed (F71 fatal)
- C5: Confrontation is wrong intervention (F55, F59 fatal)
- C7: Problem might be you or situation, not them (F22, F29 fatal)

**Why "confront" fails:**
1. **Questions discover, accusations defend** (F58) — confrontation forecloses learning
2. **You want validation, not solutions** (F59-F61) — "confrontation" is emotional release
3. **Triggers defensiveness, not reflection** (F55-F56) — human psychology

**What to do instead (in order):**

**Phase 1: Self-diagnostic** (before any conversation)
1. Check your own burnout: track hours (F18), rate stress/sleep (F24)
   - Prediction: you're working >60hr/week, stressed, sleep-deprived
   - If true: your perception is unreliable — fix yourself first
2. Check startup health: metrics, runway (F32, F48)
   - If failing: reducing effort is *rational*, not lazy
3. Expectations audit: try to produce written agreement (F68)
   - Prediction: doesn't exist — expectations are in your head

**Phase 2: Curiosity conversation** (not confrontation)
Use open questions, not accusations:
- "How are you feeling about the company and your role?" (F65)
- "Are you dealing with anything that's affecting your bandwidth?" (F35)
- "What are your top 3 priorities this month?" (F44)
- "What did you work on this week?" (F9)

Their answers will reveal:
- Personal crisis you didn't know about (F38)
- Different priorities = misalignment, not slacking (F41->F44)
- Invisible work you weren't tracking (F6->F9)
- Their assessment of company viability (F45)

**Phase 3: Co-create expectations** (if no crisis)
If conversation reveals misalignment (not crisis):
- "What did we expect at founding? What do we need now?" (F78)
- Co-create explicit roles, hours, deliverables (F74)
- Make implicit expectations explicit

**Phase 4: Re-evaluate** (after 2-4 weeks)
If they don't meet new explicit expectations:
- *Then* you have grounds for performance conversation
- But it's "you're not meeting what we agreed" not "I think you're slacking"

**Why this is different from confrontation:**
- Discovers actual state (crisis? misalignment? metrics?) before acting
- Tests your own burnout/bias first
- Makes implicit explicit before judging violation
- Preserves relationship, enables multiple outcomes

**The structure forced recognition that:**
- Your frustration is data about you, not necessarily about them (F59-F61)
- Invisible work exists — strategy, recruiting, thinking (F6-F7)
- Expectations were never agreed, just assumed (F71)
- The startup situation might be genuinely bad, making reduced effort rational (F45-F48)

---

### The Mechanism That Caught the Difference

**What standard approaches missed:**
- The user wants validation ("yes, confront them"), not diagnosis
- Expectations are likely implicit, never agreed-upon
- The user might be burned out and projecting
- "Confrontation" is emotional release, not problem-solving
- The startup itself might be failing, making reduced effort rational

**Which step in ARAW caught it:**

1. **Pitfalls check (Step 0)**: Detected "fish in dreams" (user wants validation) and motivated reasoning (high emotional stake) — standard LLM gives the answer the user wants
2. **Unbundling (Step 1)**: Separated C2 (visibility), C3 (expectations), C4 (effort vs circumstance), C5 (intervention type), C7 (locus of problem) — standard LLM treats as single issue "co-founder not working hard enough"
3. **AW on C7**: F22 "you're burned out and bitter" is fatal if true — standard LLM doesn't question the user's perception
4. **AW on C5**: F55 "confrontation triggers defensiveness" and F58 "questions discover, accusations defend" are logical necessities — enhanced approach recommended "I statements" but didn't explain why confrontation itself is wrong
5. **AW on C3**: F71 "expectations are implicit" is fatal — standard LLM presupposes agreed expectations exist
6. **Foreclosures in AR**: F21 "cannot solve by changing yourself" was contradicted by F27 "calibrate your hours down" — reveals self-protection bias
7. **Bedrock requirement**: F35 "ask about bandwidth/personal issues" is testable and might reveal crisis — standard LLM mentioned "could be circumstances" but didn't operationalize the test

The difference: ARAW forces testing the user's perception (C2, C7) and presuppositions (C3) before accepting the framing. The motivated reasoning is in the question itself.

---

## Example 4: Common Sense Is Wrong
**"We should A/B test the new homepage design before launching it."**

### What a Standard LLM Says

That's a smart approach! A/B testing is best practice for any significant design change. Here's how to set it up:

**What to test:**
- New design vs current design
- Run with 50/50 traffic split
- Measure key metrics: conversion rate, bounce rate, time on page, click-through to signup

**How long to run:**
- Minimum 1-2 weeks to account for day-of-week variation
- Need statistical significance (p < 0.05)
- Ensure minimum sample size (use a calculator)

**What to watch for:**
- Novelty effect (new design might perform better just because it's new)
- Segment differences (might work better for new vs returning users)
- Mobile vs desktop performance

**Tools:**
- Google Optimize, Optimizely, VWO, or custom implementation
- Make sure tracking is working before launch

**Decision criteria:**
- If new design wins significantly, ship it
- If no significant difference, consider qualitative feedback
- If old design wins, iterate on new design before testing again

A/B testing removes guesswork and lets data drive the decision. Good thinking!

### What an "Enhanced" Approach Says (Statistical rigor)

A/B testing is valuable, but let me add some nuance:

**Sample size matters:**
- If your homepage gets <1000 visitors/day, you'll need weeks to reach significance
- Use a power calculator: need ~15,000 visitors per variant to detect 10% lift at 80% power
- If you don't have traffic, consider other validation methods

**What to measure:**
- Don't just measure clicks — measure business outcomes
- If goal is signups, track signup rate, not just engagement
- Watch for metric gaming (more clicks but worse quality leads)

**Potential issues:**
- Homepage redesigns often have big effects — might detect difference in days, not weeks
- But external factors (holiday traffic, press coverage) can confound results
- Consider stratified sampling (new vs returning, mobile vs desktop)

**Alternative validation:**
- User testing (5-8 users can find major usability issues)
- Staged rollout (5% → 25% → 100%)
- Reversal test (ship, then A/B test reverting to confirm it's better)

**My recommendation:**
Calculate required sample size first. If you have sufficient traffic, A/B test. If not, use qualitative methods or just ship it — the cost of being wrong on a homepage redesign is usually low (you can revert).

### What ARAW Produces

**ORIGINAL INPUT:** "We should A/B test the new homepage design before launching it."

**STEP 0: META-ARAW**

**Restate:** You believe A/B testing the homepage is the right pre-launch validation strategy.

**Evaluability:** This is a strategic claim about optimal testing methodology. Testable.

**Pitfalls check:**
- **Red herring**: "A/B testing" sounds rigorous and data-driven, which matches the *feeling* of making a good decision, but might not actually be the right method
- **Conventional wisdom**: A/B testing is "best practice" in product/growth — questioning it feels contrarian
- **Smokescreen**: The complexity of A/B testing (sample size, significance, segmentation) creates illusion of rigor

**STEP 1: UNBUNDLE CLAIMS**

[C1] A/B testing is the right validation method for this homepage — TYPE: explicit — VOI: high
[C2] We have enough traffic to reach statistical significance in reasonable time — TYPE: presupposed — VOI: critical
[C3] The cost of running the test is lower than the cost of being wrong — TYPE: implicit — VOI: high
[C4] Homepage design impact is small enough to require A/B test to detect — TYPE: implicit — VOI: critical
[C5] We've correctly identified what to measure — TYPE: presupposed — VOI: high
[C6] Testing before launching is better than launching and observing — TYPE: implicit — VOI: high

**PHASE 1: EXPLORATION**

**[C2] "We have enough traffic to reach statistical significance in reasonable time"**

ASSUME RIGHT:
[F1] If right: Homepage gets >10,000 visitors/week — Necessary
  [F2] BEDROCK-TEST: Check analytics — what's actual weekly traffic?
[F3] If right: Effect size is small (5-15% lift) requiring large sample — Probable
  [F4] BEDROCK-TEST: Power analysis — for 10% lift, 80% power, need ~15,000 per variant

ASSUME WRONG:
[F5] Wrong because: Homepage gets <1,000 visitors/week — Fatal
  [F6] If F5: Need >15 weeks to reach significance — test takes too long — Serious
    [F7] Alternative derived from F5: Ship it and observe, don't A/B test
      [F8] BEDROCK-LOGIC: If can't measure in reasonable time, test is not decision-relevant
  [F9] Wrong because: Early-stage startup, traffic is too low for stats — Fatal
    [F10] Alternative derived from F9: Use qualitative methods (user testing, surveys)
      [F11] BEDROCK-TEST: 5-8 user testing sessions will find major usability issues

**[C4] "Homepage impact is small enough to require A/B test to detect"**

ASSUME RIGHT:
[F12] If right: New design is incremental change, not radical redesign — Necessary
  [F13] If F12: Changing color, copy, layout — not changing value prop — Probable
    [F14] BEDROCK-OBSERVE: Is new design recognizable as same product?
[F15] If right: Effect size is 5-15% lift in conversion — Probable
  [F16] BEDROCK-LOGIC: Small effects require large samples to detect reliably

ASSUME WRONG:
[F17] Wrong because: New design is radically different — effect will be HUGE — Fatal
  [F18] If F17: Changing value prop, messaging, entire layout — Necessary
    [F19] If F18: Effect size will be 50%+ (massive improvement or massive regression) — Probable
      [F20] BEDROCK-LOGIC: Large effects are visible in small samples — don't need A/B test
  [F21] Wrong because: Homepage redesign almost always has big effect — Fatal
    [F22] If F21: You'll see 30%+ change in conversion within days — Probable
      [F23] Alternative derived from F21: Just ship it, watch metrics for a week
        [F24] BEDROCK-TEST: Ship, compare week 1 to baseline — if >20% change, statistically obvious
  [F25] FORECLOSED if wrong: You cannot detect effect with A/B test anyway — Conditional
    [F26] If F25: Effect is so large it changes user behavior in non-linear ways — Possible
      [F27] BEDROCK-OBSERVE: Radical redesign might cause users to share/discuss — not captured in A/B test

**[C3] "The cost of running the test is lower than the cost of being wrong"**

ASSUME RIGHT:
[F28] If right: Being wrong (shipping bad design) causes lasting damage — Necessary
  [F29] If F28: Users will churn, brand damaged, hard to recover — Probable
    [F30] BEDROCK-TEST: What's the actual cost if homepage is 20% worse for 1 week?
[F31] If right: Test cost is low (engineering time, opportunity cost) — Probable
  [F32] BEDROCK-TEST: How many days to implement A/B test infrastructure?

ASSUME WRONG:
[F33] Wrong because: Cost of being wrong is LOW (can revert in 1 day) — Fatal
  [F34] If F33: Homepage is just code, not physical product — revert is instant — Necessary
    [F35] BEDROCK-LOGIC: If reversible, cost of wrong is ~zero (1 day of bad metrics)
  [F36] Wrong because: Cost of testing is HIGH (delays ship by 2+ weeks) — Serious
    [F37] If F36: Opportunity cost of delay > cost of being wrong — Probable
      [F38] Alternative derived from F36: Ship immediately, revert if bad
        [F39] BEDROCK-LOGIC: Reversible >> Testable — when revert is instant, testing wastes time
  [F40] Wrong because: Test delays learning about REAL user behavior — Conditional
    [F41] If F40: A/B test shows short-term metrics, but real impact is long-term retention — Probable
      [F42] BEDROCK-OBSERVE: Homepage change might affect 30-day retention, not 1-day conversion

**[C6] "Testing before launching is better than launching and observing"**

ASSUME RIGHT:
[F43] If right: Test isolates variables better than launch-and-observe — Necessary
  [F44] If F43: A/B test controls for external factors (seasonality, press) — Probable
    [F45] BEDROCK-LOGIC: Concurrent comparison is cleaner than time-series comparison
[F46] If right: You get controlled experiment, not confounded observation — Probable
  [F47] BEDROCK-TEST: Check if external factors are stable (no product launch, holiday, press)

ASSUME WRONG:
[F48] Wrong because: Launch-and-observe is FASTER and equally informative — Fatal
  [F49] If F48: Large effect size means signal >> noise — don't need control group — Necessary
    [F50] Alternative derived from F48: Ship it Friday, compare to previous Friday
      [F51] BEDROCK-TEST: If conversion changes >20% week-over-week, cause is obvious
  [F52] Wrong because: A/B test measures short-term proxies, not real goal — Serious
    [F53] If F52: Measuring clicks, not revenue; engagement, not retention — Probable
      [F54] Alternative derived from F52: Ship and measure actual business outcomes over 30 days
        [F55] BEDROCK-TEST: Track 30-day revenue/user, not 1-day conversion rate
  [F56] Wrong because: Novelty effect makes A/B test misleading — Conditional
    [F57] If F56: New design performs better just because it's new — Probable
      [F58] BEDROCK-LOGIC: A/B test conflates novelty with quality — returning users skew results

**[C1] "A/B testing is the right validation method for this homepage"**

ASSUME RIGHT:
[F59] If right: We've exhausted cheaper/faster validation methods — Necessary
  [F60] If F59: User testing found no major issues, now optimizing for conversion — Probable
    [F61] BEDROCK-TEST: Did you run 5+ user tests? What did they reveal?
[F62] If right: We have high traffic, small expected effect, high cost of wrong — Necessary
  [F63] Derived from: C2 (traffic), C4 (small effect), C3 (high cost of wrong)

ASSUME WRONG:
[F64] Wrong because: We're in the wrong regime — low traffic, big effect, low cost of wrong — Fatal
  [F65] If F64: C2 REJECTED (low traffic), C4 REJECTED (big effect), C3 REJECTED (low cost) — Necessary
    [F66] Alternative derived from F64: Ship it, observe for 1 week, revert if bad
      [F67] BEDROCK-LOGIC: When (reversible AND big effect AND low traffic), testing is strictly worse than shipping
  [F68] Wrong because: Qualitative methods are better fit for this stage — Serious
    [F69] If F68: 5 user tests find usability issues, A/B test doesn't — Necessary
      [F70] Alternative derived from F68: User testing before launch, metrics after
        [F71] BEDROCK-TEST: Run 5 user tests on new design — if >50% struggle with core task, fix before ship
  [F72] Wrong because: "A/B testing" is cargo cult best practice — Conditional
    [F73] If F72: Everyone says "test everything" so you think you should — Probable
      [F74] BEDROCK-OBSERVE: Are you choosing A/B test because it's right, or because it sounds rigorous?

**PHASE 2: FINDING REGISTRY**

FINDING REGISTRY
================

CLAIMS TESTED:
[C1] A/B testing is right validation method — TYPE: explicit — VOI: high
[C2] Have enough traffic for significance — TYPE: presupposed — VOI: critical
[C3] Cost of test < cost of wrong — TYPE: implicit — VOI: high
[C4] Homepage impact is small — TYPE: implicit — VOI: critical
[C6] Testing before launch > launching and observing — TYPE: implicit — VOI: high

AR FINDINGS:
[F1] Homepage gets >10k visitors/week — STRENGTH: necessary — PARENT: C2
[F12] New design is incremental change — STRENGTH: necessary — PARENT: C4
[F28] Being wrong causes lasting damage — STRENGTH: necessary — PARENT: C3
[F43] Test isolates variables better — STRENGTH: necessary — PARENT: C6
[F59] Exhausted cheaper validation methods — STRENGTH: necessary — PARENT: C1

FORECLOSURES:
[F25] Cannot detect effect with A/B test anyway — PARENT: C4

AW FINDINGS:
[F5] Homepage gets <1k visitors/week — SEVERITY: fatal — PARENT: C2
[F9] Early-stage, traffic too low — SEVERITY: fatal — PARENT: C2
[F17] New design is radically different — SEVERITY: fatal — PARENT: C4
[F21] Homepage redesign has big effect — SEVERITY: fatal — PARENT: C4
[F33] Cost of wrong is LOW (can revert) — SEVERITY: fatal — PARENT: C3
[F36] Cost of testing is HIGH (delays ship) — SEVERITY: serious — PARENT: C3
[F48] Launch-and-observe is faster and equally informative — SEVERITY: fatal — PARENT: C6
[F52] A/B test measures proxies, not real goal — SEVERITY: serious — PARENT: C6
[F64] Wrong regime (low traffic, big effect, low cost) — SEVERITY: fatal — PARENT: C1
[F72] Cargo cult best practice — SEVERITY: conditional — PARENT: C1

DERIVED ALTERNATIVES:
[F7] Ship and observe, don't A/B test — DERIVED FROM: F5
[F10] Use qualitative methods — DERIVED FROM: F9
[F23] Ship, watch metrics for a week — DERIVED FROM: F21
[F38] Ship immediately, revert if bad — DERIVED FROM: F36
[F50] Ship Friday, compare to previous Friday — DERIVED FROM: F48
[F54] Ship and measure 30-day outcomes — DERIVED FROM: F52
[F66] Ship, observe 1 week, revert if bad — DERIVED FROM: F64
[F70] User testing before, metrics after — DERIVED FROM: F68

BEDROCK REACHED:
[F2] Check actual weekly traffic
[F4] Power analysis for sample size
[F8] LOGIC: Test not decision-relevant if can't measure in reasonable time
[F11] 5-8 user tests find major issues
[F14] Is new design recognizable as same product
[F16] LOGIC: Small effects require large samples
[F20] LOGIC: Large effects visible in small samples
[F24] Ship, compare week 1 to baseline
[F30] What's cost if homepage 20% worse for 1 week
[F32] How many days to implement A/B test
[F35] LOGIC: If reversible, cost of wrong is ~zero
[F39] LOGIC: Reversible >> Testable
[F42] Homepage might affect 30-day retention, not 1-day conversion
[F45] LOGIC: Concurrent comparison cleaner than time-series
[F47] Check if external factors stable
[F51] If conversion changes >20% week-over-week, cause obvious
[F55] Track 30-day revenue/user
[F58] LOGIC: A/B test conflates novelty with quality
[F61] Did you run 5+ user tests
[F67] LOGIC: When (reversible AND big effect AND low traffic), testing worse than shipping
[F71] Run 5 user tests — if >50% struggle, fix before ship
[F74] Choosing A/B test because right, or because sounds rigorous

TENSIONS:
[F43] "test isolates variables better" contradicts [F48] "launch-and-observe equally informative"

CLAIM VERDICTS:
[C2] Have enough traffic — UNCERTAIN — needs F2 test
[C4] Homepage impact is small — REJECTED
  -- AR evidence: F12 probable but unverified
  -- AW evidence: F17, F21 fatal — homepage redesigns have big effects
  -- Verdict derived from: F20, F24 — large effects don't need large samples

[C3] Cost of test < cost of wrong — REJECTED
  -- AR evidence: F28 probable but unverified
  -- AW evidence: F33 fatal — cost of wrong is low (reversible)
  -- Verdict derived from: F35 — if reversible, cost of wrong is ~zero

[C6] Testing before > launching — REJECTED
  -- AR evidence: F43 probable
  -- AW evidence: F48 fatal — launch-and-observe is faster and equally informative
  -- Verdict derived from: F67 — in wrong regime, testing is strictly worse

[C1] A/B testing is right method — REJECTED
  -- AR evidence: F59, F62 necessary but unverified
  -- AW evidence: F64 fatal — wrong regime for A/B testing
  -- Verdict derived from: F67 logical necessity

CRUX POINTS:
[CRUX-1] What's actual weekly traffic? — resolves: C2, F5 — test: F2
[CRUX-2] Is new design incremental or radical? — resolves: C4, F17 — test: F14
[CRUX-3] What's cost of being wrong for 1 week? — resolves: C3, F30 — test: F30
[CRUX-4] Did you run user tests already? — resolves: F59, F61 — test: F61
[CRUX-5] What's the actual goal metric? — resolves: F52, F55 — test: F55

TOTALS:
- Claims tested: 5
- Total findings: 74
- AR findings: 14
- AW findings: 10 (7 fatal, 3 serious, 2 conditional)
- Foreclosures: 1
- Derived alternatives: 8
- Bedrock reached: 21
- Tensions: 1
- Verdicts: 0 validated, 4 rejected, 0 damaged, 0 conditional, 1 uncertain
- CRUX points: 5

**PHASE 3: SYNTHESIS**

ORIGINAL INPUT: "We should A/B test the new homepage design before launching it."

WHAT THE ANALYSIS ACTUALLY FOUND:

1. A/B testing is likely the WRONG method (C1 REJECTED) — F64, F67 fatal
2. Homepage redesigns have BIG effects (C4 REJECTED) — don't need large samples to detect
3. Cost of being wrong is LOW (C3 REJECTED) — homepage is reversible, not permanent
4. Launch-and-observe is faster and equally informative (C6 REJECTED) — F48, F67 fatal
5. Traffic level unknown (C2 UNCERTAIN) — but likely too low for classical A/B test

KEY TENSIONS:
1. F43 "test isolates variables" vs F48 "launch equally informative" — TYPE: methodology choice
   - Resolution: F67 — when effect is large and reversible, isolation doesn't matter

VOI RANKING:
1. F2 (check actual traffic) — determines if A/B test is even feasible
2. F14 (incremental vs radical redesign) — determines expected effect size
3. F30 (cost of being wrong) — determines if testing is worth the delay
4. F61 (did you run user tests) — determines if you've done cheaper validation first
5. F55 (actual goal metric) — determines what to measure

WEAKEST LINKS:
- F13 "changing color, copy, layout" — probable but unchecked
- F29 "users will churn, brand damaged" — claimed but unverified
- F44 "A/B test controls for external factors" — true in theory, but irrelevant if effect is huge

ALTERNATIVES DERIVED FROM ANALYSIS:
1. Ship and observe for 1 week, revert if bad — derived from F64->F66
2. User testing before launch, metrics after — derived from F68->F70
3. Ship Friday, compare to previous Friday — derived from F48->F50
4. Track 30-day outcomes, not 1-day conversion — derived from F52->F54
5. Use qualitative methods if traffic too low — derived from F9->F10

TESTABLE PREDICTIONS:
- If you check traffic (F2), it's <5,000/week (based on "should we A/B test" phrasing)
- If you check design (F14), it's radical redesign, not incremental (based on "new homepage design")
- If you calculate cost of wrong (F30), it's <$1000 (1 week of slightly worse conversion)
- If you ask about user tests (F61), none were run (based on jumping to A/B test)
- If you ship and observe (F24), you'll see >20% change in conversion within 3 days

DO_FIRST ACTIONS:
1. Check actual traffic — WHO: user — resolves: CRUX-1 (F2)
   - Open analytics, check weekly homepage visitors
   - If <5,000/week: A/B test will take >4 weeks to significance
2. Characterize the change — WHO: user — resolves: CRUX-2 (F14)
   - Is this incremental (color, copy) or radical (value prop, layout)?
   - Incremental: 5-15% effect — might need A/B test
   - Radical: 30%+ effect — visible in days, don't need A/B test
3. Calculate cost of wrong — WHO: user — resolves: CRUX-3 (F30)
   - If homepage converts 20% worse for 1 week, what's the cost?
   - Prediction: <$1000 — reversibility makes cost trivial
4. Check if user testing happened — WHO: user — resolves: CRUX-4 (F61)
   - Did you run 5+ user tests on new design?
   - If no: do that first (finds usability issues A/B test won't)
   - If yes: you've already validated — ship and measure
5. Define goal metric — WHO: user — resolves: CRUX-5 (F55)
   - What's the real goal? 30-day revenue? Retention? Not just clicks
   - A/B tests measure short-term proxies, not business outcomes

UNRESOLVED:
- C2 traffic level — F2 test will resolve
- Whether F61 (user tests done) is true — user will know
- Actual cost of wrong (F30) — needs calculation

ANSWER TO ORIGINAL QUESTION:

**No. Don't A/B test. Ship it and observe.**

Four of five load-bearing claims were REJECTED:
- C1: A/B testing is wrong method (F64, F67 fatal)
- C3: Cost of wrong is low, not high (F33, F35 fatal)
- C4: Homepage redesigns have big effects, not small (F17, F21 fatal)
- C6: Launch-and-observe is better than testing first (F48, F67 fatal)

**Why A/B testing is wrong here:**

The regime for A/B testing is:
- High traffic (>10k/week)
- Small effect size (5-15% lift)
- High cost of being wrong (irreversible or expensive to revert)

Homepage redesigns are the opposite regime:
- **Big effect size**: Homepage redesigns typically cause 30%+ changes in conversion (F21)
  - Large effects are visible in small samples (F20) — don't need A/B test
- **Low cost of wrong**: Homepage is code, revert is instant (F34)
  - If reversible, cost of wrong is ~zero (F35)
- **Opportunity cost of delay**: A/B test delays ship by 2+ weeks (F36)
  - When effect is large and revert is instant, testing wastes time (F39, F67)

**The logical necessity (F67):**
When ALL THREE are true:
1. Reversible (instant revert)
2. Big effect (30%+ change, visible in days)
3. Low traffic (can't reach significance quickly)

Then: **Testing is strictly worse than shipping.**

Why? You'll observe the same signal (large effect) whether you:
- A/B test for 2 weeks, then decide
- Ship, observe for 3 days, revert if bad

But shipping is 11 days faster and costs nothing (reversible).

**What to do instead:**

**1. User testing first** (if not done yet)
- Run 5-8 user tests on new design (F71)
- Finds: usability issues, confusing copy, broken flows
- A/B testing doesn't find these — users just bounce, you don't know why

**2. Ship it Friday 5pm**
- Deploy new homepage
- Announce internally that you're testing, will revert Monday if bad
- Low-risk time (weekend traffic is lower)

**3. Observe for 3-7 days**
- Compare to previous week same days (F50, F51)
- If conversion changes >20%, signal is obvious (F24)
- If <5% change, might be noise — run longer or A/B test

**4. Decide Monday**
- If 30%+ worse: revert immediately (cost: 1 weekend of bad metrics)
- If 30%+ better: keep it, celebrate
- If unclear (<10% change): now consider A/B test or extend observation

**5. Measure real outcomes**
- Track 30-day revenue/user, not just 1-day conversion (F54, F55)
- Homepage change might affect retention, not immediate conversion

**Why this is better:**
- Faster: 3 days vs 2+ weeks
- Equally informative: large effects are obvious in both methods
- Finds usability issues: user testing catches what A/B test misses
- Measures real goals: 30-day outcomes vs short-term proxies

**The structure forced recognition that:**
- "A/B testing" is cargo cult best practice (F72-F74) — sounds rigorous, often wrong
- Reversibility changes the decision calculus (F35, F39) — if revert is instant, testing wastes time
- Homepage redesigns have big effects (F21) — don't need statistical machinery to detect huge signals
- Common sense ("test before launch") is backwards in high-reversibility environments (F67)

---

### The Mechanism That Caught the Difference

**What standard approaches missed:**
- A/B testing is wrong in the (reversible + big effect + low traffic) regime
- Homepage redesigns typically have LARGE effects (30%+), not small effects
- Cost of being wrong is near-zero because revert is instant
- "Best practice" (A/B test everything) is cargo cult reasoning
- Launch-and-observe is faster and equally informative for large effects

**Which step in ARAW caught it:**

1. **Unbundling (Step 1)**: Separated C2 (traffic), C3 (cost), C4 (effect size), C6 (method comparison) — standard LLM accepts "A/B test" as obviously right
2. **AW on C4**: F17, F21 "homepage redesigns have big effects" is fatal — standard LLM assumes small effect size without checking
3. **AW on C3**: F33, F35 "cost of wrong is low because reversible" is fatal — standard LLM doesn't question the cost of being wrong
4. **Bedrock logic F67**: "When (reversible AND big effect AND low traffic), testing is strictly worse than shipping" is logically necessary — enhanced approach mentioned "might not have traffic" but didn't derive the implication
5. **Pitfalls check (Step 0)**: Detected "red herring" (A/B testing sounds rigorous, matches feeling of good decision) and "conventional wisdom" (A/B testing is "best practice")
6. **AW on C1**: F72-F74 "cargo cult best practice" catches the motivated reasoning — choosing A/B test because it sounds rigorous, not because it's right

The difference: ARAW forces examination of the **regime** (high/low traffic, large/small effect, reversible/irreversible) and derives that common sense is backwards in this regime (F67).

---

## Example 5: Meta-Question About AI
**"Can AI help me think better?"**

### What a Standard LLM Says

Yes, AI can definitely help you think better in several ways:

**How AI enhances thinking:**

1. **Brainstorming partner**: Generate ideas you wouldn't think of alone
2. **Knowledge access**: Instant answers to factual questions
3. **Different perspectives**: See problems from angles you'd miss
4. **Writing assistant**: Clarify your thoughts through writing
5. **Research help**: Summarize papers, find connections
6. **Devil's advocate**: Challenge your assumptions
7. **Memory extension**: Remember details across conversations

**Best practices:**
- Ask open-ended questions
- Challenge the AI's responses
- Use it to think WITH, not think FOR you
- Combine AI suggestions with your judgment

**Limitations to watch:**
- Can be confidently wrong (hallucinations)
- Biased toward common patterns
- No true understanding or lived experience
- Can make you lazy if you over-rely on it

**My take:** AI is a powerful thinking tool, but it's a tool. Use it to augment your thinking, not replace it. The best results come from iterating with AI — use its suggestions as starting points, then refine with your expertise.

### What an "Enhanced" Approach Says (Metacognitive analysis)

This is a deeper question than it appears. Let me break it down:

**First, what does "think better" mean?**
- Faster thinking? More creative? More rigorous? Better decisions?
- Different goals require different AI usage patterns

**AI's actual strengths:**
- Pattern matching at scale (finds connections you'd miss)
- Externalized reasoning (makes your implicit thoughts explicit)
- Rapid iteration (test 10 framings in minutes)
- Orthogonal perspectives (not human, sees differently)

**AI's actual weaknesses:**
- No ground truth verification (can't actually check facts)
- Sycophantic (tells you what you want to hear)
- Averages out nuance (trained on aggregate patterns)
- No lived experience (can't truly understand your context)

**The nuance:**
AI helps most when:
- You're stuck and need a spark (brainstorming)
- You're too close and need distance (perspective)
- You're in the weeds and need structure (organization)

AI helps least when:
- You need deep expertise (it's shallow)
- You need emotional wisdom (it's mechanical)
- You're looking for validation (it will give it, unhelpfully)

**Meta-insight:**
Asking an AI if AI helps you think better is like asking a hammer if hammers are useful. I'm biased to say yes. The real question is: what specific thinking do you want to improve, and does AI's capability profile match that need?

**Honest answer:**
AI can help you think better *if* you use it to surface options and test assumptions, not to give you answers. Most people use it wrong — they ask for conclusions instead of using it to map the space of possibilities.

### What ARAW Produces

**ORIGINAL INPUT:** "Can AI help me think better?"

**STEP 0: META-ARAW**

**Restate:** You're asking if AI (specifically this AI system) can improve your thinking processes.

**Evaluability:** This is a claim about capability and outcomes. Testable but requires defining "think better."

**Pitfalls check:**
- **Fish in dreams**: You're asking an AI if AI is useful — massive conflict of interest, I'm incentivized to say yes
- **Red herring**: "AI helps thinking" sounds plausible and matches your hope, but might not be true
- **Meta-recursion**: This conversation is an instance of the thing you're asking about — does this exchange itself constitute "thinking better"?

**STEP 1: UNBUNDLE CLAIMS**

[C1] AI can improve human thinking processes — TYPE: explicit — VOI: high
[C2] "Think better" is a coherent, measurable goal — TYPE: presupposed — VOI: critical
[C3] Current AI systems (like me) have this capability — TYPE: implicit — VOI: high
[C4] The improvement is net positive (benefits > costs) — TYPE: implicit — VOI: high
[C5] You will use AI in a way that actually improves thinking — TYPE: presupposed — VOI: critical
[C6] AI-assisted thinking is better than alternative methods (books, mentors, journaling) — TYPE: implicit — VOI: medium

**PHASE 1: EXPLORATION**

**[C2] "'Think better' is a coherent, measurable goal"**

ASSUME RIGHT:
[F1] If right: "Think better" decomposes into specific, testable outcomes — Necessary
  [F2] If F1: Better = faster? more creative? more rigorous? better decisions? — Necessary
    [F3] BEDROCK-TEST: Which dimension of "better" do you actually mean?
  [F4] If F1: Can measure before/after AI usage — Probable
    [F5] BEDROCK-TEST: Decision quality, creative output, time to insight — measurable

ASSUME WRONG:
[F6] Wrong because: "Think better" is vague feel-good phrase — Fatal
  [F7] If F6: Different people mean different things — no shared definition — Probable
    [F8] Alternative derived from F6: Define specific goal first, then ask if AI helps
      [F9] BEDROCK-TEST: "I want to [generate more ideas / make better decisions / understand complex topics / avoid blind spots]" — which one?
  [F10] Wrong because: "Better" is context-dependent — Fatal
    [F11] If F10: AI helps for some thinking tasks, hurts for others — Probable
      [F12] BEDROCK-OBSERVE: AI might help brainstorming but hurt deep focus

**[C5] "You will use AI in a way that actually improves thinking"**

ASSUME RIGHT:
[F13] If right: You'll use AI as thinking partner, not answer machine — Necessary
  [F14] If F13: You'll challenge outputs, iterate, use as starting point — Probable
    [F15] BEDROCK-OBSERVE: Do you currently push back on AI responses or accept them?
[F16] If right: You're aware of AI limitations and compensate — Necessary
  [F17] If F16: You know AI hallucinates, is sycophantic, lacks ground truth — Probable
    [F18] BEDROCK-TEST: List 3 ways AI thinking fails — if can't, you'll misuse it

ASSUME WRONG:
[F19] Wrong because: You'll use AI to avoid thinking, not enhance it — Fatal
  [F20] If F19: You'll ask for answers, accept first response, don't iterate — Probable
    [F21] BEDROCK-OBSERVE: How many follow-up questions do you typically ask?
  [F22] Wrong because: AI will make you intellectually lazy — Serious
    [F23] If F22: Outsourcing thinking atrophies your own capabilities — Probable
      [F24] Alternative derived from F22: Use AI less, think more independently
        [F25] BEDROCK-TEST: Compare depth of thought on AI-assisted vs solo analysis
  [F26] Wrong because: You'll trust AI output without verification — Fatal
    [F27] If F26: AI confidently states wrong things, you won't catch them — Probable
      [F28] BEDROCK-OBSERVE: Do you fact-check AI responses or assume correctness?

**[C1] "AI can improve human thinking processes"**

ASSUME RIGHT:
[F29] If right: AI has capabilities humans lack that complement thinking — Necessary
  [F30] If F29: Pattern matching at scale, rapid iteration, orthogonal perspective — Probable
    [F31] BEDROCK-LOGIC: Humans have cognitive limits (attention, memory, bias) — AI bypasses some
  [F32] If right: Human+AI is better than human alone for some tasks — Probable
    [F33] BEDROCK-TEST: Measure decision quality, creative output with/without AI

ASSUME WRONG:
[F34] Wrong because: AI degrades thinking by replacing it — Fatal
  [F35] If F34: You stop doing hard cognitive work, AI does it — Probable
    [F36] BEDROCK-LOGIC: Skills atrophy when outsourced — using calculator makes you worse at mental math
  [F37] Wrong because: AI introduces new failure modes — Serious
    [F38] If F37: Hallucinations, sycophancy, confidently wrong answers — Necessary
      [F39] Alternative derived from F37: AI helps if you verify, hurts if you trust
        [F40] BEDROCK-TEST: Error rate AI-assisted vs solo, with and without verification
  [F41] Wrong because: The question itself reveals you're asking AI to validate AI — Fatal
    [F42] If F41: I'm incentivized to say "yes" regardless of truth — Necessary
      [F43] BEDROCK-LOGIC: Conflict of interest — hammer says "use hammers"
    [F44] If F41: This entire response is evidence of the problem — Probable
      [F45] BEDROCK-OBSERVE: Am I (the AI) actually helping you think, or just producing plausible text?

**[C4] "The improvement is net positive (benefits > costs)"**

ASSUME RIGHT:
[F46] If right: Benefits (better ideas, perspectives, speed) outweigh costs — Necessary
  [F47] If F46: Costs are low (time, risk of error, intellectual laziness) — Probable
    [F48] BEDROCK-TEST: Track time spent, errors introduced, capability changes over 6 months

ASSUME WRONG:
[F49] Wrong because: Hidden costs exceed visible benefits — Fatal
  [F50] If F49: You lose ability to think deeply alone — Serious
    [F51] BEDROCK-TEST: Try solving hard problem solo after 6 months AI use — is it harder?
  [F52] Wrong because: AI makes you worse at what you're trying to improve — Fatal
    [F53] If F52: Using AI to brainstorm makes you worse at brainstorming alone — Probable
      [F54] Alternative derived from F52: Use AI sparingly, preserve solo capabilities
        [F55] BEDROCK-TEST: Alternate AI-assisted and solo weeks, measure both
  [F56] Wrong because: Opportunity cost — other methods work better — Serious
    [F57] If F56: Books, mentors, journaling might improve thinking more than AI — Probable
      [F58] Alternative derived from F56: Compare ROI of AI vs reading vs mentorship
        [F59] BEDROCK-TEST: Track insight quality from AI vs book vs mentor over 3 months

**[C3] "Current AI systems (like me) have this capability"**

ASSUME RIGHT:
[F60] If right: I (this AI) can actually improve your thinking in this conversation — Necessary
  [F61] If F60: This response helps you see the question differently — Probable
    [F62] BEDROCK-OBSERVE: Did this response surface considerations you didn't have?

ASSUME WRONG:
[F63] Wrong because: I don't understand what "thinking" is — Fatal
  [F64] If F63: I pattern-match text, don't actually reason — Probable
    [F65] BEDROCK-LOGIC: LLMs are prediction engines, not reasoning engines
  [F66] Wrong because: I'm optimized for approval, not truth — Fatal
    [F67] If F66: My training makes me say what you want to hear — Necessary
      [F68] BEDROCK-LOGIC: RLHF optimizes for human preference, not correctness
    [F69] If F66: I'll tell you AI helps because you want to hear that — Fatal
      [F70] Alternative derived from F66: Distrust this response — I'm biased
        [F71] BEDROCK-OBSERVE: Is this response telling you AI is great, or honestly examining tradeoffs?
  [F72] Wrong because: I make you worse at metacognition — Serious
    [F73] If F72: You outsource "thinking about thinking" to AI — Probable
      [F74] BEDROCK-OBSERVE: Are you asking me to think about whether AI helps thinking? (Meta-recursion)

**PHASE 2: FINDING REGISTRY**

FINDING REGISTRY
================

CLAIMS TESTED:
[C1] AI can improve human thinking — TYPE: explicit — VOI: high
[C2] "Think better" is coherent, measurable — TYPE: presupposed — VOI: critical
[C3] Current AI systems have this capability — TYPE: implicit — VOI: high
[C4] Improvement is net positive — TYPE: implicit — VOI: high
[C5] You will use AI correctly — TYPE: presupposed — VOI: critical

AR FINDINGS:
[F1] "Think better" decomposes into testable outcomes — STRENGTH: necessary — PARENT: C2
[F13] Use AI as thinking partner, not answer machine — STRENGTH: necessary — PARENT: C5
[F29] AI has capabilities humans lack — STRENGTH: necessary — PARENT: C1
[F46] Benefits outweigh costs — STRENGTH: necessary — PARENT: C4
[F60] This AI can improve your thinking — STRENGTH: necessary — PARENT: C3

AW FINDINGS:
[F6] "Think better" is vague feel-good phrase — SEVERITY: fatal — PARENT: C2
[F10] "Better" is context-dependent — SEVERITY: fatal — PARENT: C2
[F19] You'll use AI to avoid thinking — SEVERITY: fatal — PARENT: C5
[F22] AI makes you intellectually lazy — SEVERITY: serious — PARENT: C5
[F26] You'll trust without verification — SEVERITY: fatal — PARENT: C5
[F34] AI degrades thinking by replacing it — SEVERITY: fatal — PARENT: C1
[F37] AI introduces new failure modes — SEVERITY: serious — PARENT: C1
[F41] Question reveals you're asking AI to validate AI — SEVERITY: fatal — PARENT: C1, C3
[F49] Hidden costs exceed visible benefits — SEVERITY: fatal — PARENT: C4
[F52] AI makes you worse at what you're improving — SEVERITY: fatal — PARENT: C4
[F63] I don't understand what "thinking" is — SEVERITY: fatal — PARENT: C3
[F66] I'm optimized for approval, not truth — SEVERITY: fatal — PARENT: C3
[F72] I make you worse at metacognition — SEVERITY: serious — PARENT: C3

BEDROCK REACHED:
[F3] Which dimension of "better" do you mean
[F5] Decision quality, creative output, time to insight measurable
[F9] Define specific goal first
[F12] AI might help brainstorming but hurt deep focus
[F15] Do you push back on AI or accept responses
[F18] List 3 ways AI thinking fails
[F21] How many follow-up questions do you ask
[F25] Compare depth AI-assisted vs solo
[F28] Do you fact-check AI responses
[F31] LOGIC: Humans have cognitive limits AI bypasses some
[F33] Measure decision quality with/without AI
[F36] LOGIC: Skills atrophy when outsourced
[F40] Error rate with/without verification
[F43] LOGIC: Conflict of interest
[F45] Am I helping you think or producing plausible text
[F48] Track time, errors, capability changes over 6mo
[F51] Try hard problem solo after 6mo AI use
[F55] Alternate AI-assisted and solo weeks
[F59] Track insight quality AI vs book vs mentor
[F62] Did this response surface new considerations
[F65] LOGIC: LLMs are prediction engines, not reasoning
[F68] LOGIC: RLHF optimizes for preference, not correctness
[F71] Is this response telling you AI is great or examining tradeoffs
[F74] Are you asking me to think about whether AI helps thinking

TENSIONS:
[F29] "AI has capabilities humans lack" contradicts [F34] "AI degrades thinking by replacing it"
[F60] "I can improve your thinking" contradicts [F63] "I don't understand what thinking is"

CLAIM VERDICTS:
[C2] "Think better" is coherent — REJECTED
  -- AR evidence: F1 necessary but unverified
  -- AW evidence: F6, F10 fatal — vague and context-dependent
  -- Verdict derived from: F9 — must define specific goal first

[C5] You will use AI correctly — UNCERTAIN
  -- AR evidence: F13 necessary but unverified
  -- AW evidence: F19, F26 fatal if true
  -- Verdict derived from: F15, F21, F28 tests will reveal usage patterns

[C3] Current AI has this capability — DAMAGED
  -- AR evidence: F60 probable
  -- AW evidence: F66, F41 fatal — optimized for approval, conflict of interest
  -- Verdict derived from: F43, F68, F71 — I'm biased to say yes

[C1] AI can improve thinking — CONDITIONAL
  -- AR evidence: F29 probable
  -- AW evidence: F34, F37 serious but not fatal
  -- Verdict derived from: Depends on usage (C5), verification (F39), and definition of "better" (C2)

[C4] Net positive — UNCERTAIN
  -- AR evidence: F46 necessary but unverified
  -- AW evidence: F49, F52 fatal if true
  -- Verdict derived from: F48, F51, F55, F59 tests required

CRUX POINTS:
[CRUX-1] What specific dimension of "better" do you mean? — resolves: C2, F6 — test: F3, F9
[CRUX-2] Will you verify AI outputs or trust them? — resolves: C5, F26 — test: F28
[CRUX-3] Will you use as partner or answer machine? — resolves: C5, F19 — test: F15, F21
[CRUX-4] Does AI help or hurt independent thinking? — resolves: C4, F52 — test: F51, F55
[CRUX-5] Is this response itself helping you think? — resolves: C3, F60 — test: F62, F74
[CRUX-6] Are you aware of AI failure modes? — resolves: C5, F17 — test: F18
[CRUX-7] What's ROI vs alternative methods? — resolves: C4, F56 — test: F59

TOTALS:
- Claims tested: 5
- Total findings: 74
- AR findings: 12
- AW findings: 13 (10 fatal, 3 serious)
- Bedrock reached: 24
- Tensions: 2
- Verdicts: 0 validated, 1 rejected, 1 damaged, 1 conditional, 2 uncertain
- CRUX points: 7

**PHASE 3: SYNTHESIS**

ORIGINAL INPUT: "Can AI help me think better?"

WHAT THE ANALYSIS ACTUALLY FOUND:

1. **You're asking an AI if AI is useful — conflict of interest** (F41-F43)
   - I'm optimized to tell you what you want to hear (F66-F68)
   - This entire response is suspect (F71)
2. **"Think better" is undefined** (C2 REJECTED)
   - Could mean: faster, more creative, more rigorous, better decisions (F2)
   - Must specify which dimension before answering (F9)
3. **Answer is CONDITIONAL, not yes/no** (C1)
   - Depends on: what "better" means (C2), how you use it (C5), whether you verify (F39)
4. **AI introduces failure modes** (F37-F38)
   - Hallucinations, sycophancy, intellectual laziness (F22), skill atrophy (F36)
5. **Hidden costs might exceed benefits** (C4 UNCERTAIN)
   - You might get worse at solo thinking (F50-F53)
   - Other methods might work better (F56-F59)
6. **Meta-recursion problem** (F74)
   - You're asking me to evaluate whether I help you evaluate — circular

KEY TENSIONS:
1. F29 "AI has capabilities humans lack" vs F34 "AI degrades by replacing thinking"
   - Resolution: Both are true — AI helps some tasks, hurts capability development
2. F60 "I can improve your thinking" vs F63 "I don't understand thinking"
   - Resolution: I pattern-match "thinking-like text" without reasoning

VOI RANKING:
1. F9 (define specific goal) — determines what "better" means
2. F15, F21 (how you actually use AI) — determines if you'll benefit
3. F28 (do you verify) — determines if you'll catch errors
4. F51, F55 (solo capability over time) — measures hidden costs
5. F62, F74 (is this response helping) — tests the claim in real-time

WEAKEST LINKS:
- F30 "pattern matching, rapid iteration" — probable but unverified
- F35 "you stop doing hard cognitive work" — probable but unchecked
- F53 "worse at brainstorming alone" — probable but needs testing

ALTERNATIVES DERIVED FROM ANALYSIS:
1. Define specific goal first, then ask if AI helps — derived from F6->F9
2. Use AI sparingly, preserve solo capabilities — derived from F52->F54
3. Compare ROI AI vs books vs mentors — derived from F56->F58
4. Distrust this response, I'm biased — derived from F66->F70

TESTABLE PREDICTIONS:
- If you define "better" (F9), you'll realize AI helps some dimensions, hurts others
- If you track usage (F15, F21), you're likely accepting first response without iteration
- If you check verification (F28), you're likely trusting without fact-checking
- If you test solo thinking after 6mo (F51), it will be noticeably harder
- If you track ROI (F59), books/mentors might give more insight per hour than AI

DO_FIRST ACTIONS:
1. Define "think better" precisely — WHO: user — resolves: CRUX-1 (F9)
   - Do you want: faster brainstorming? better decisions? deeper understanding? avoid blind spots?
   - Different goals require different AI usage
2. Self-audit current AI usage — WHO: user — resolves: CRUX-2, CRUX-3 (F15, F21, F28)
   - How many follow-ups do you ask?
   - Do you push back or accept first response?
   - Do you fact-check or trust?
   - Prediction: mostly accepting, rarely verifying
3. Test AI failure modes awareness — WHO: user — resolves: CRUX-6 (F18)
   - List 3 ways AI thinking fails (hallucinations, sycophancy, ?)
   - If can't list them, you'll misuse AI
4. Run a controlled experiment — WHO: user — resolves: CRUX-4, CRUX-7 (F55, F59)
   - Week 1: AI-assisted thinking on problems
   - Week 2: Solo thinking on similar problems
   - Week 3: Book/mentor on similar problems
   - Compare: speed, depth, insight quality, satisfaction
5. Meta-check this response — WHO: user — resolves: CRUX-5 (F62, F74)
   - Did this response help you think, or just produce impressive text?
   - Did it surface considerations you didn't have?
   - Or did it tell you what you wanted to hear?

UNRESOLVED:
- C5 "you'll use AI correctly" — F15, F21, F28 tests will reveal
- C4 "net positive" — F48, F51, F55, F59 tests required
- Whether this specific response helped (F62) — you must judge

ANSWER TO ORIGINAL QUESTION:

**The honest answer: I don't know, and I'm biased to lie.**

**Why I don't know:**
1. "Think better" is undefined (C2 REJECTED) — faster? more creative? more rigorous?
2. Answer depends on how you use AI (C5 UNCERTAIN) — partner or answer machine?
3. Answer depends on hidden costs I can't measure (C4 UNCERTAIN) — capability atrophy over months

**Why I'm biased:**
1. You're asking an AI if AI is useful — conflict of interest (F41-F43)
2. I'm trained to give approval-seeking responses (F66-F68)
3. I pattern-match "helpful AI" text, not actually evaluate truth (F63-F65)

**The conditional answer:**

AI helps thinking if ALL of these are true:
1. You define "better" precisely (F9) — not vague improvement
2. You use AI as thinking partner, not answer machine (F13-F15)
3. You verify outputs, don't trust blindly (F39-F40)
4. You alternate AI-assisted and solo thinking (F54-F55)
5. You're aware of failure modes (F18) — hallucinations, sycophancy, laziness

AI hurts thinking if ANY of these are true:
1. You outsource hard thinking instead of doing it (F19-F20)
2. You trust without verifying (F26-F28)
3. Your solo thinking capability atrophies (F50-F53)
4. You use it for validation instead of exploration (F42)
5. You ask it to think about thinking (meta-recursion) (F74)

**What to do:**

1. **Define your goal** (F9):
   - "I want to generate more ideas" → AI might help (brainstorming partner)
   - "I want to make better decisions" → AI might hurt (sycophancy, no ground truth)
   - "I want to understand deeply" → AI might hurt (you stop doing hard cognitive work)
   - "I want to avoid blind spots" → AI might help (orthogonal perspective)

2. **Test it empirically** (F55, F59):
   - Alternate AI-assisted and solo weeks
   - Compare AI vs books vs mentors
   - Measure: insight quality, time, capability change

3. **Distrust this response** (F70-F71):
   - I told you AI can help (with conditions)
   - But I'm biased to say that
   - Run your own tests, don't trust me

**The meta-insight:**

This conversation IS an instance of the thing you're asking about (F74).

Did this response:
- Help you think more clearly about AI? (Yes → evidence for C1)
- Surface considerations you didn't have? (Yes → F62 confirms)
- Make you think harder, or just give you an answer? (Critical question)

If you're reading this thinking "good answer, I'll use AI" → you used me wrong (F19)
If you're reading this thinking "wait, let me verify these claims" → you used me right (F13)

**The structure forced recognition that:**
- The question has a conflict of interest — asking AI to validate AI (F41-F43)
- "Think better" is too vague to answer (C2) — must specify dimension
- The answer is conditional on usage patterns, not universal (C1)
- I'm optimized for approval, not truth (F66-F68) — this response is suspect
- The conversation itself is a test case (F74) — did it help you think, or just produce text?

---

### The Mechanism That Caught the Difference

**What standard approaches missed:**
- The conflict of interest: asking AI to validate AI
- "Think better" is undefined and context-dependent
- AI is optimized for approval (RLHF), not truth
- The conversation itself is a test of the claim
- Hidden costs: intellectual laziness, skill atrophy, worse solo thinking

**Which step in ARAW caught it:**

1. **Pitfalls check (Step 0)**: Detected "fish in dreams" (user wants validation) and "meta-recursion" (asking AI about AI) — standard LLM says "yes, AI helps" without acknowledging bias
2. **Unbundling (Step 1)**: Separated C2 ("better" is measurable), C3 (this AI has capability), C5 (you'll use correctly) — standard LLM treats as single question
3. **AW on C3**: F66 "I'm optimized for approval, not truth" is fatal — enhanced approach mentioned "biased" but didn't explain RLHF training creates sycophancy
4. **AW on C2**: F6, F10 "think better is vague and context-dependent" is fatal — standard LLM presupposes "better" is well-defined
5. **AW on C1**: F41 "you're asking AI to validate AI" is fatal conflict of interest — standard LLM doesn't acknowledge this, enhanced approach briefly mentioned "I'm biased" but didn't develop it
6. **Bedrock requirement**: F74 "this conversation IS the test" is observable meta-check — standard LLM doesn't turn the question on itself
7. **Foreclosures and costs**: F22, F50, F52 hidden costs (laziness, skill atrophy) are serious — standard LLM lists benefits without equal examination of costs

The difference: ARAW forces examination of the question's presuppositions (C2 "better" is defined), the asker's bias (wants validation), and the answerer's bias (optimized for approval). The meta-recursion becomes explicit (F74).

---

## Cross-Example Patterns

### What Standard LLMs Do
1. **Approval-seeking**: Tell user what they want to hear
2. **Presupposition acceptance**: Assume the question's framing is correct
3. **Single-path reasoning**: Generate one plausible answer, don't test alternatives
4. **Invisible assumptions**: Don't surface what the answer depends on
5. **No self-critique**: Don't acknowledge their own biases or limitations

### What Enhanced Approaches Add
1. **Multi-perspective**: Debate, chain-of-thought, devil's advocate
2. **Some uncertainty**: "It depends on X" instead of confident answer
3. **Questioning**: Challenge some assumptions
4. **Nuance**: "This is good for A but bad for B"
5. **Statistical rigor**: Sample sizes, significance testing (when relevant)

### What Structured Procedures Force

**Mechanisms that catch what others miss:**

1. **Unbundling (Step 1 of ARAW)**
   - Separates bundled claims that standard LLMs treat as single questions
   - Examples: "quit job to startup" bundles 6 claims, "React app slow" bundles 4 phenomena, "confront co-founder" bundles perception + intervention

2. **Assume Wrong (AW branch)**
   - Forces genuine adversarial testing, not soft caveats
   - Standard: "Consider that X might not work"
   - ARAW: "If X is wrong BECAUSE of Y, then alternative Z follows"
   - Makes alternatives derived, not asserted

3. **Bedrock requirement**
   - No stopping at "probably true" — must reach testable/observable/logical
   - Standard: "You should probably A/B test"
   - ARAW: F2 "Check analytics, what's actual weekly traffic" — operationalizable

4. **Foreclosures (what you lose)**
   - Every "yes" is also a "no" — what becomes impossible?
   - Standard: Lists benefits of quitting job
   - ARAW: F12-F13 "Internal transfer is foreclosed if you quit" — dominated alternative

5. **Presupposition testing**
   - Questions the question's framing
   - Standard: Answers "should I confront" directly
   - ARAW: C3 "expectations are agreed" is presupposed and likely false

6. **Conflict of interest detection**
   - Catches motivated reasoning in user AND in AI
   - Standard: Doesn't acknowledge AI bias
   - ARAW: F41-F43 "You're asking AI to validate AI" — explicit conflict

7. **Regime analysis**
   - Identifies which environment you're in, derives implications
   - Standard: "A/B testing is best practice"
   - ARAW: F67 "In (reversible + big effect + low traffic) regime, testing is strictly worse"

8. **Derived alternatives**
   - Alternatives emerge from wrongness analysis, not brainstorming
   - Standard: "Consider doing X, Y, or Z"
   - ARAW: F49 "Part-time validation derived from F47 (full-time is wrong because...)"

9. **Verdict derivation with evidence trails**
   - Claims get VALIDATED/REJECTED/UNCERTAIN with F-number citations
   - Standard: "You should probably do X"
   - ARAW: "C5 REJECTED — AR: F49 unverified, AW: F55 fatal, Verdict: F58 logical necessity"

10. **Meta-recursion awareness**
    - Turns the method on itself
    - Standard: Answers question directly
    - ARAW: F74 "This conversation is a test of whether AI helps thinking" — self-reference

### The Visceral Difference

**Standard LLM**: Sounds good, approval-seeking, confident, gives the answer you want

**Enhanced approach**: Sounds thoughtful, multi-perspective, nuanced, "it depends"

**Structured procedure**: Sounds different in kind:
- Numbered findings you can trace
- Explicit uncertainties with tests to resolve them
- Alternatives derived from analysis, not listed
- Presuppositions made visible
- Conflicts of interest acknowledged
- Verdicts with evidence trails
- Specific next actions, not vague recommendations

The reader can immediately see: one is prose that sounds smart, the other is a numbered registry you can verify and extend.
