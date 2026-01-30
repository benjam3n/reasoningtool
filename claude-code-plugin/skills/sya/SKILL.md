---
name: sya
description: "Analyze complex systems using causal loop diagrams, stock and flow models, feedback loop identification, and system archetypes"
---

# Systems Analysis

## Overview
Analyze complex systems using causal loop diagrams, stock and flow models, feedback loop identification, and system archetypes

## Steps

### Step 1: Define system boundary
Establish what is inside and outside the system:

1. IDENTIFY THE PROBLEM/BEHAVIOR:
   - What behavior are we trying to understand?
   - What is the problem symptom?
   - What pattern do we observe over time?
     - Growth (exponential, linear, S-curve)
     - Decline (gradual, rapid, oscillating)
     - Oscillation (boom-bust, cycles)
     - Equilibrium (stable, stuck)

2. DEFINE SYSTEM BOUNDARY:
   - What elements are "in" the system?
   - What is treated as external (given)?
   - Time horizon: How far back and forward to consider?

   Include in boundary:
   - Elements that directly cause the behavior
   - Elements affected by the behavior
   - Elements involved in feedback loops

   Exclude from boundary:
   - Elements that are truly external (weather, laws)
   - Elements too distant to matter
   - Elements we cannot influence at all

3. IDENTIFY KEY VARIABLES:
   List the important quantities that change:
   - Stocks: Things that accumulate (inventory, reputation, skills)
   - Rates: Things that flow (sales per day, hires per month)
   - Auxiliary: Factors that influence but don't accumulate

4. ESTABLISH TIME SCALE:
   - What is the dominant time constant?
   - Days, weeks, months, years?
   - This affects what feedback matters

### Step 2: Map causal relationships
Create a causal loop diagram showing cause-effect relationships:

NOTATION:
- Arrow: A → B means "A affects B"
- + sign: Same direction (A increases, B increases)
- - sign: Opposite direction (A increases, B decreases)

PROCESS:
1. Start with the problem variable
2. Ask: "What directly affects this?"
3. Draw arrows from causes to effects
4. For each arrow, determine polarity (+/-)
5. Ask: "Does this effect feed back to earlier causes?"
6. Continue until major relationships are mapped

CAUSAL LINK TYPES:

Positive link (+): Same direction
- "Higher prices → Higher revenue" (+) [if demand holds]
- "More training → Higher skill" (+)
- "More customers → More word-of-mouth → More customers" (+)

Negative link (-): Opposite direction
- "Higher prices → Lower demand" (-)
- "More inventory → Less urgency to order" (-)
- "More workload → Lower quality" (-)

DIAGRAM ELEMENTS:
- Boxes or labels for variables
- Arrows showing direction of causation
- +/- signs on arrows showing polarity
- R/B labels for feedback loops (added in next step)

QUALITY CHECKS:
- Each link has clear causal mechanism
- Polarity is correct (test: if A doubles, what happens to B?)
- No missing intermediate variables
- Important delays are noted

### Step 3: Identify feedback loops
Find and classify feedback loops in the causal structure:

LOOP IDENTIFICATION:
1. Start at any variable
2. Follow arrows until you return to the starting variable
3. This is a feedback loop
4. Classify the loop type

LOOP TYPES:

REINFORCING LOOP (R): Self-reinforcing, exponential
- Count the negative signs in the loop
- EVEN number of negatives (or zero) = Reinforcing
- Creates exponential growth OR exponential decline
- "Vicious cycle" or "Virtuous cycle"

Example: Compound Interest
Savings → (+) Interest Earned → (+) Savings
This is reinforcing: growth begets more growth

Example: Bank Run
Fear → (+) Withdrawals → (+) Bank Instability → (+) Fear
Reinforcing: fear creates more fear

BALANCING LOOP (B): Goal-seeking, stabilizing
- ODD number of negative signs = Balancing
- Seeks equilibrium, resists change
- Creates oscillation if delays exist
- "Checks and balances"

Example: Thermostat
Temperature Gap → (+) Heating → (+) Temperature → (-) Temperature Gap
This is balancing: seeks the goal temperature

Example: Market Price
Price → (-) Demand → (-) Inventory → (-) Price
Balancing: price adjusts to clear inventory

FOR EACH LOOP:
1. Name the loop (descriptive)
2. Classify as R (reinforcing) or B (balancing)
3. Describe the behavior it drives
4. Note any significant delays in the loop
5. Assess loop strength (dominant or secondary?)

### Step 4: Model stocks and flows
Identify accumulations (stocks) and rates of change (flows):

STOCKS:
Things that accumulate over time
- Physical: Inventory, cash, equipment
- Intangible: Reputation, skills, relationships
- Informational: Knowledge, data, backlog

Properties of stocks:
- Change gradually (can't jump instantly)
- Create memory in the system
- Create delays between cause and effect
- Can only change through flows

FLOWS:
Rates that change stocks
- Inflows: Add to the stock
- Outflows: Remove from the stock

Stock change = Inflows - Outflows

STOCK-FLOW STRUCTURE:

[Inflow] → [STOCK] → [Outflow]

Example: Workforce
[Hiring Rate] → [EMPLOYEES] → [Attrition Rate]

Example: Technical Debt
[Debt Creation Rate] → [TECHNICAL DEBT] → [Debt Paydown Rate]

FOR EACH STOCK:
1. Name the stock (noun - what accumulates)
2. Identify inflows (what adds to it)
3. Identify outflows (what depletes it)
4. Estimate typical time to fill/drain
5. Note current level (high, medium, low)

LINKING TO CAUSAL LOOPS:
- Stocks often appear in feedback loops
- The stock level affects the flows
- This creates the feedback structure

### Step 5: Recognize system archetypes
Identify common system behavior patterns:

ARCHETYPE 1: LIMITS TO GROWTH
Structure:
- Reinforcing loop drives growth
- Balancing loop creates limiting constraint
- Initially growth dominates
- Eventually constraint dominates

Behavior: S-curve growth, then plateau or decline

Example: New product adoption
- R: Success → Word of mouth → More customers → More success
- B: Market saturation → Fewer remaining prospects → Slower growth

Leverage: Focus on the constraint before it bites

ARCHETYPE 2: SHIFTING THE BURDEN
Structure:
- Symptom prompts quick fix
- Quick fix reduces symptom
- But undermines fundamental solution
- Dependency on quick fix grows

Behavior: Short-term improvement, long-term degradation

Example: Technical debt
- Quick fix: Skip tests to ship faster
- Fundamental solution: Build quality processes
- Side effect: More bugs → more quick fixes needed

Leverage: Invest in fundamental solution; avoid quick fixes

ARCHETYPE 3: FIXES THAT FAIL
Structure:
- Fix addresses symptom
- Unintended consequence makes problem worse
- After delay, problem returns stronger

Behavior: Oscillation, worsening over time

Example: Firefighting mode
- Fix: Heroic effort to solve crisis
- Consequence: No time for prevention
- Delay: Next crisis is worse

Leverage: Break the link to unintended consequences

ARCHETYPE 4: SUCCESS TO THE SUCCESSFUL
Structure:
- Two activities compete for resources
- Success in one attracts more resources
- Less resources for the other
- Winner takes all

Behavior: One grows, other shrinks; lock-in

Example: Internal project competition
- Successful project gets more budget
- Other project starves
- Eventually only "winner" survives

Leverage: Create separate resource pools; explicit portfolio balance

ARCHETYPE 5: TRAGEDY OF THE COMMONS
Structure:
- Shared resource benefits individual users
- Each user gains by using more
- Total use depletes the resource
- Everyone loses

Behavior: Resource depletion, collapse

Example: Technical infrastructure
- Each team benefits from using shared service
- No one invests in maintenance
- Service degrades, everyone suffers

Leverage: Regulate the commons; assign ownership; align incentives

ARCHETYPE 6: ESCALATION
Structure:
- One party acts to gain advantage
- Other party responds to restore balance
- First party escalates further
- Arms race ensues

Behavior: Mutual escalation, exhaustion

Example: Price war
- Company A cuts price
- Company B matches
- Company A cuts more
- Both margins destroyed

Leverage: Refuse to play; find non-zero-sum alternatives

ARCHETYPE 7: GROWTH AND UNDERINVESTMENT
Structure:
- Growth creates demand for capacity
- Underinvestment in capacity
- Performance degrades
- Demand drops, "justifying" low investment

Behavior: Growth stalls, self-fulfilling low expectations

Example: Startup scaling
- Growth creates load on infrastructure
- Don't invest in scaling infrastructure
- Site becomes slow
- Customers leave, growth stops

Leverage: Invest ahead of demand; watch performance standards

### Step 6: Identify leverage points
Find high-leverage intervention points:

LEVERAGE POINTS (from least to most powerful):

12. CONSTANTS AND PARAMETERS
    Numbers: taxes, subsidies, standards
    Easy to change but usually low leverage
    Example: Adjusting price by 5%

11. BUFFER SIZES
    Stabilizing stocks relative to flows
    Example: Increasing inventory safety stock

10. STRUCTURE OF STOCKS AND FLOWS
    Physical structure of the system
    Example: Adding a new warehouse location

9. DELAYS
    Length of delays relative to system change rate
    Example: Faster feedback loops

8. BALANCING FEEDBACK LOOPS
    Strength of stabilizing loops
    Example: Stronger quality control

7. REINFORCING FEEDBACK LOOPS
    Strength of growth/decline drivers
    Example: Reducing viral coefficient

6. INFORMATION FLOWS
    Who has access to what information
    Example: Making performance data visible

5. RULES OF THE SYSTEM
    Incentives, constraints, agreements
    Example: Changing how bonuses are calculated

4. POWER TO ADD/CHANGE RULES
    Self-organization, evolution
    Example: Enabling teams to set their own processes

3. GOALS OF THE SYSTEM
    Purpose and direction
    Example: Shifting from growth to sustainability

2. PARADIGM/MINDSET
    Deep beliefs and assumptions
    Example: From "resources are scarce" to "abundance"

1. TRANSCENDING PARADIGMS
    Not being attached to any paradigm
    Highest leverage, hardest to achieve

FOR THE ANALYZED SYSTEM:
1. List potential intervention points
2. Classify by leverage level
3. Assess feasibility (can we actually change this?)
4. Assess unintended consequences
5. Prioritize: High leverage + Feasible + Low risk

### Step 7: Analyze interventions
Evaluate potential interventions and predict effects:

FOR EACH POTENTIAL INTERVENTION:

1. DESCRIBE THE INTERVENTION:
   - What specific change would be made?
   - Which leverage point does it target?
   - What mechanism do we expect?

2. TRACE DIRECT EFFECTS:
   - What variables change immediately?
   - What is the expected direction and magnitude?

3. TRACE FEEDBACK EFFECTS:
   - Which feedback loops are affected?
   - Do reinforcing loops amplify the change?
   - Do balancing loops counteract it?
   - How strong are these effects?

4. CONSIDER DELAYS:
   - How long until effects are visible?
   - Will there be oscillation during transition?
   - Could we declare failure before success appears?

5. IDENTIFY UNINTENDED CONSEQUENCES:
   - What side effects might occur?
   - Which archetypes might we trigger?
   - Who else is affected and how might they respond?

6. COMPARE TO DOING NOTHING:
   - What happens if we don't intervene?
   - Is the system self-correcting?
   - Is patience an option?

INTERVENTION EVALUATION:

| Intervention | Leverage | Feasibility | Time to Effect | Confidence | Unintended Risks |
|--------------|----------|-------------|----------------|------------|------------------|
| ...          | ...      | ...         | ...            | ...        | ...              |

RECOMMENDATION:
- Which interventions should be pursued?
- In what sequence?
- What should we monitor to verify effects?


## When to Use
- When dealing with problems that resist simple solutions
- When interventions seem to make things worse
- When symptoms keep recurring despite treatment
- For understanding organizational dynamics
- When there are long delays between action and effect
- For strategic planning in complex environments
- When multiple stakeholders with conflicting goals interact
- For understanding market dynamics and competition
- When exponential growth or decline is observed
- For policy analysis with broad systemic effects

## Verification
- System boundary is clearly defined
- Causal links have clear mechanisms (not just correlations)
- Feedback loops are correctly classified (R vs B)
- Stocks and flows are properly distinguished
- Relevant archetypes are identified
- Leverage points are prioritized by actual leverage
- Interventions are traced through feedback effects

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.