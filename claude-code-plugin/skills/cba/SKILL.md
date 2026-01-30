---
name: cba
description: "Systematically quantify costs and benefits to evaluate decisions, including NPV calculation, sensitivity analysis, and intangible factors"
---

# Cost-Benefit Analysis

## Overview
Systematically quantify costs and benefits to evaluate decisions, including NPV calculation, sensitivity analysis, and intangible factors

## Steps

### Step 1: Frame the analysis
Establish the scope and baseline for analysis:

1. DEFINE THE DECISION:
   - What specific decision are we evaluating?
   - What are we trying to achieve?
   - Who is the decision for?

2. IDENTIFY ALTERNATIVES:
   Always include:
   - The proposed action
   - "Do nothing" / status quo baseline
   - At least one other alternative if exists

   Each alternative should be mutually exclusive and complete.

3. SET ANALYSIS PARAMETERS:
   - Time horizon: How far out to project?
     - Capital investments: 5-10 years
     - Technology: 3-5 years
     - Operational changes: 1-3 years
   - Discount rate: Cost of capital or opportunity cost
     - Corporate: Often 8-15%
     - Government/public: Often 3-7%
     - Personal: Your alternative return rate
   - Currency and inflation handling

4. DEFINE PERSPECTIVE:
   - Whose costs and benefits count?
   - Organization only? Include externalities?
   - Single project or portfolio view?

5. IDENTIFY CONSTRAINTS:
   - Budget limits
   - Payback period requirements
   - Risk tolerance

### Step 2: Identify and quantify costs
Create comprehensive inventory of all costs:

COST CATEGORIES:

1. UPFRONT/CAPITAL COSTS (Year 0):
   - Purchase price or development cost
   - Implementation and setup
   - Training and change management
   - Integration and customization
   - Infrastructure and equipment
   - Licensing (if upfront)
   - Consultants and external help

2. ONGOING/OPERATING COSTS (Years 1-N):
   - Maintenance and support
   - Licensing (if recurring)
   - Personnel (salaries, benefits)
   - Infrastructure (hosting, utilities)
   - Consumables and supplies
   - Insurance
   - Compliance and auditing

3. OPPORTUNITY COSTS:
   - What else could this money/time be used for?
   - Revenue from alternatives foregone
   - Other projects delayed or cancelled

4. RISK COSTS:
   - Expected value of potential failures
   - Mitigation costs
   - Insurance costs

5. HIDDEN/OFTEN-MISSED COSTS:
   - Transition and migration
   - Productivity loss during change
   - Coordination and management overhead
   - Technical debt created
   - Vendor lock-in costs (future switching)
   - End-of-life and decommissioning

FOR EACH COST:
1. Name and describe the cost
2. Estimate amount (use ranges if uncertain)
3. Assign to year(s) when cost occurs
4. Note confidence level (high/medium/low)
5. Document estimation methodology

### Step 3: Identify and quantify benefits
Create comprehensive inventory of all benefits:

BENEFIT CATEGORIES:

1. REVENUE/INCOME BENEFITS:
   - New revenue enabled
   - Revenue protected from loss
   - Price premium achieved
   - Market share gained
   - Customer acquisition
   - Customer retention improvement

2. COST REDUCTION BENEFITS:
   - Labor savings
   - Efficiency improvements
   - Error reduction
   - Waste reduction
   - Infrastructure consolidation
   - Vendor cost reduction

3. PRODUCTIVITY BENEFITS:
   - Time savings
   - Throughput increases
   - Quality improvements
   - Faster time-to-market
   - Reduced rework

4. RISK REDUCTION BENEFITS:
   - Avoided losses (expected value)
   - Compliance risk reduction
   - Security risk reduction
   - Operational risk reduction
   - Reputation protection

5. STRATEGIC BENEFITS:
   - Competitive advantage
   - Market positioning
   - Capability building
   - Options created for future
   - Learning and knowledge gained

QUANTIFICATION APPROACHES:
- Direct measurement: When benefits are directly observable
- Proxy metrics: When direct measurement isn't possible
- Comparison: Before/after or with/without comparisons
- Industry benchmarks: What others have achieved
- Expert estimation: Informed judgment with ranges

FOR EACH BENEFIT:
1. Name and describe the benefit
2. Define how it will be measured
3. Estimate value (use ranges if uncertain)
4. Assign to year(s) when benefit occurs
5. Note probability/confidence level
6. Document estimation methodology

### Step 4: Calculate Net Present Value
Compute NPV by discounting future cash flows:

NPV FORMULA:
NPV = Sum of [Cash Flow(t) / (1 + r)^t] for t = 0 to N

Where:
- Cash Flow(t) = Benefits(t) - Costs(t) for year t
- r = discount rate
- N = time horizon in years

STEP-BY-STEP CALCULATION:

1. CREATE CASH FLOW TABLE:
   | Year | Costs | Benefits | Net Cash Flow |
   |------|-------|----------|---------------|
   | 0    | ...   | ...      | ...           |
   | 1    | ...   | ...      | ...           |
   | ...  | ...   | ...      | ...           |
   | N    | ...   | ...      | ...           |

2. CALCULATE DISCOUNT FACTORS:
   Year 0: 1.000
   Year 1: 1/(1+r) = 1/1.10 = 0.909 (at 10%)
   Year 2: 1/(1+r)^2 = 0.826
   ...

3. CALCULATE PRESENT VALUES:
   PV(t) = Net Cash Flow(t) x Discount Factor(t)

4. SUM PRESENT VALUES:
   NPV = Sum of all PV(t)

DECISION RULES:
- NPV > 0: Project creates value, generally accept
- NPV < 0: Project destroys value, generally reject
- NPV = 0: Breakeven, indifferent

ADDITIONAL METRICS:

IRR (Internal Rate of Return):
- The discount rate that makes NPV = 0
- If IRR > required return, project is attractive

Payback Period:
- Time to recover initial investment
- Simple payback: Without discounting
- Discounted payback: With discounting

ROI (Return on Investment):
- (Total Benefits - Total Costs) / Total Costs
- Doesn't account for timing, use NPV when timing matters

BCR (Benefit-Cost Ratio):
- PV of Benefits / PV of Costs
- BCR > 1 means NPV > 0

### Step 5: Conduct sensitivity analysis
Test how conclusions change with different assumptions:

1. IDENTIFY KEY VARIABLES:
   Which assumptions have the most impact on NPV?
   Common sensitive variables:
   - Benefit estimates (especially revenue projections)
   - Discount rate
   - Time horizon
   - Implementation costs
   - Adoption rates
   - Market conditions

2. ONE-WAY SENSITIVITY:
   Vary one variable at a time:
   - Pessimistic case (e.g., -20%)
   - Base case
   - Optimistic case (e.g., +20%)

   Calculate NPV for each scenario.

3. TORNADO DIAGRAM:
   Rank variables by impact on NPV:
   | Variable        | Low NPV  | Base NPV | High NPV |
   |-----------------|----------|----------|----------|
   | Revenue         | -100K    | 500K     | 1.2M     |
   | Costs           | 400K     | 500K     | 600K     |
   | Discount rate   | 450K     | 500K     | 550K     |

4. BREAKEVEN ANALYSIS:
   Find the point where NPV = 0:
   - What revenue level breaks even?
   - What cost level breaks even?
   - What adoption rate is needed?

5. SCENARIO ANALYSIS:
   Test coherent combinations of assumptions:
   - Best case: All favorable assumptions
   - Worst case: All unfavorable assumptions
   - Most likely: Best estimates

6. MONTE CARLO (OPTIONAL for high-stakes):
   - Define probability distributions for uncertain variables
   - Run many simulations
   - Get probability distribution of NPV

### Step 6: Assess intangible factors
Acknowledge and evaluate factors that can't be quantified:

COMMON INTANGIBLES:

1. STRATEGIC VALUE:
   - Alignment with strategy
   - Competitive positioning
   - Market perception
   - Options created for future

2. ORGANIZATIONAL IMPACT:
   - Employee morale and satisfaction
   - Organizational learning
   - Culture change
   - Talent attraction/retention

3. CUSTOMER IMPACT:
   - Customer satisfaction
   - Brand perception
   - Customer relationships
   - Trust and loyalty

4. RISK AND RESILIENCE:
   - Flexibility and adaptability
   - Reduced dependency
   - Business continuity
   - Peace of mind

5. SOCIAL/ENVIRONMENTAL:
   - Environmental impact
   - Community impact
   - Ethical considerations
   - Sustainability

EVALUATION APPROACH:

1. List all relevant intangibles
2. For each, assess:
   - Direction: Positive, negative, or neutral
   - Magnitude: High, medium, or low impact
   - Confidence: How sure are we?
3. Consider if intangibles could override NPV conclusion:
   - Positive NPV but significant negative intangibles?
   - Negative NPV but strategic necessity?
4. Attempt rough quantification where possible:
   - What would we pay to have this benefit?
   - What would we pay to avoid this risk?

HANDLING IN DECISION:
- Document intangibles explicitly
- Don't pretend to quantify what you can't
- Make judgment call transparent

### Step 7: Compare alternatives and recommend
Synthesize all analysis into a recommendation:

1. COMPARISON TABLE:
   For each alternative (including do nothing):
   | Criterion        | Option A | Option B | Do Nothing |
   |------------------|----------|----------|------------|
   | NPV              | ...      | ...      | 0          |
   | IRR              | ...      | ...      | N/A        |
   | Payback          | ...      | ...      | N/A        |
   | Risk level       | ...      | ...      | ...        |
   | Intangibles      | ...      | ...      | ...        |
   | Constraints met? | ...      | ...      | ...        |

2. DECISION MATRIX:
   Weight criteria and score alternatives:
   - NPV/financial return (weight: ?)
   - Risk/sensitivity (weight: ?)
   - Strategic fit (weight: ?)
   - Implementation feasibility (weight: ?)
   - Intangible benefits (weight: ?)

3. RECOMMENDATION:
   - Which alternative is recommended?
   - Why is it better than alternatives?
   - Under what conditions would conclusion change?

4. IMPLEMENTATION CONSIDERATIONS:
   - What needs to happen to capture the projected benefits?
   - What are the key risks to manage?
   - What milestones should trigger re-evaluation?

5. DOCUMENTATION:
   - Summarize key assumptions
   - Note what would invalidate the analysis
   - Set review date for assumptions


## When to Use
- Before major investments or expenditures
- When comparing alternatives with different cost/benefit profiles
- For build vs buy decisions
- When evaluating new projects or initiatives
- For pricing decisions (does the revenue justify the cost?)
- When stakeholders need quantified justification
- For resource allocation across competing priorities
- When evaluating whether to continue or stop an initiative
- For policy decisions with broad impact

## Verification
- All significant costs and benefits are included
- Estimates have documented basis (not arbitrary)
- NPV calculation is mathematically correct
- Sensitivity analysis covers key uncertainties
- Intangibles are acknowledged even if not quantified
- Recommendation follows logically from analysis
- Key assumptions are explicit and testable

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.