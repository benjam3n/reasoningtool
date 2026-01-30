---
name: "fm - Financial Modeling"
description: "Build financial models for projections, scenario analysis, and sensitivity testing to support decision-making"
---

# Financial Modeling

## Overview
Build financial models for projections, scenario analysis, and sensitivity testing to support decision-making

## Steps

### Step 1: Define model scope and purpose
Establish clear objectives for the model:
1. Articulate the question the model needs to answer
   - "Should we invest in X?"
   - "What's the business worth?"
   - "How long until profitable?"
2. Identify key stakeholders and their needs
   - What outputs do they need?
   - What level of detail?
   - How will they use results?
3. Define scope boundaries
   - Time horizon for projections
   - Level of detail required
   - What's in vs out of scope
4. Select appropriate model type
   - Three-statement, DCF, operating model, etc.
   - Match complexity to decision importance
5. Establish timeline and resources

### Step 2: Gather data and develop assumptions
Collect information to build assumptions:
1. Gather historical data
   - Past financial statements
   - Operating metrics
   - Market data
2. Research external benchmarks
   - Industry averages
   - Comparable companies
   - Market growth rates
3. Develop key assumptions
   - Revenue drivers (growth, pricing, volume)
   - Cost structure (fixed, variable)
   - Working capital needs
   - Capital expenditure
4. Document assumption rationale
   - Source of each assumption
   - Confidence level
   - Range of plausible values
5. Validate assumptions with stakeholders

### Step 3: Build model structure
Create the model framework:
1. Set up workbook structure
   - Cover/summary sheet
   - Assumptions sheet
   - Calculation sheets
   - Output/dashboard sheets
2. Create time axis
   - Column for each period (month, quarter, year)
   - Include historical periods for validation
3. Build input section
   - All assumptions in one place
   - Clear labels and units
   - Input formatting (blue font or yellow fill)
4. Create calculation architecture
   - Revenue build-up
   - Cost build-up
   - Supporting schedules as needed
5. Set up output sections
   - Key metrics
   - Financial statements
   - Charts and visuals

### Step 4: Build projection formulas
Create calculations that project future:
1. Build revenue model
   - Start from drivers or growth rates
   - Calculate revenue by period
   - Include seasonality if relevant
2. Build cost model
   - Fixed costs (don't vary with volume)
   - Variable costs (scale with revenue)
   - Step costs (change at thresholds)
3. Calculate key metrics
   - Margins
   - Growth rates
   - Unit economics
   - Cash metrics
4. Build financial statements (if applicable)
   - Income statement
   - Balance sheet (if needed)
   - Cash flow statement
5. Apply best practices
   - No hardcoded numbers in formulas
   - Consistent formula patterns
   - Clear cell references

### Step 5: Validate and error-check model
Ensure model integrity:
1. Check formulas
   - Audit for errors
   - Trace precedents and dependents
   - Look for circular references
   - Check formula consistency across rows
2. Reasonableness checks
   - Do outputs make intuitive sense?
   - Compare to historical data
   - Compare to benchmarks
   - Check extreme cases (what if inputs are 0?)
3. Balance checks (for balance sheet models)
   - Assets = Liabilities + Equity
   - Cash flow reconciles
4. Stress test
   - Try extreme assumptions
   - Does model break?
   - Do errors cascade?
5. Document known limitations

### Step 6: Build scenario analysis
Create alternative scenario projections:
1. Identify key scenarios
   - Base case (already built)
   - Upside case
   - Downside case
   - Specific scenarios (expansion, recession, etc.)
2. Define assumptions for each scenario
   - What changes from base case?
   - Keep scenarios internally consistent
   - Document scenario logic/story
3. Implement scenarios in model
   - Create scenario selector
   - Link assumptions to scenarios
   - Or create parallel scenario columns
4. Generate outputs for each scenario
   - Key metrics by scenario
   - Financial statements by scenario
5. Create comparison view
   - Side-by-side scenario summary
   - Key differences highlighted

### Step 7: Conduct sensitivity analysis
Analyze sensitivity to key assumptions:
1. Identify critical assumptions
   - Revenue growth rate
   - Pricing
   - Cost structure
   - Timing assumptions
2. Build sensitivity tables
   - One-way: vary one input, see output
   - Two-way: vary two inputs, see output matrix
3. Create tornado diagram
   - Vary each input by same percentage
   - Rank by impact on key output
4. Calculate breakeven points
   - What input value makes output = target?
   - e.g., sales for breakeven profit
5. Interpret results
   - Which variables matter most?
   - Where is the model most uncertain?
   - What needs to be monitored?

### Step 8: Document and present findings
Prepare model for communication:
1. Create executive summary
   - Key findings
   - Recommendation (if applicable)
   - Critical assumptions
   - Risks and limitations
2. Document model thoroughly
   - Assumptions and sources
   - Methodology
   - How to use the model
   - Known limitations
3. Build presentation materials
   - Key charts and visuals
   - Scenario comparison
   - Sensitivity results
4. Prepare for questions
   - What are the key assumptions?
   - What could go wrong?
   - How confident are we?
5. Establish update process
   - How often to update
   - Who maintains
   - Version control


## When to Use
- Making decisions with significant financial implications
- Evaluating business plans or investment opportunities
- Planning for uncertain futures with multiple possible outcomes
- Need to understand which variables matter most
- Communicating financial plans to stakeholders
- Testing strategy resilience under different conditions
- Setting targets and milestones
- Fundraising or seeking investment

## Verification
- Model answers the intended question
- All assumptions are documented with rationale
- Formulas are error-free and consistent
- Outputs pass reasonableness checks
- Scenarios are internally consistent
- Sensitivity analysis identifies key drivers
- Documentation enables maintenance by others

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.