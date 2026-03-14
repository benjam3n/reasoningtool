---
name: "lcca - Life Cycle Cost Analysis"
description: Estimate total cost of ownership across the full system lifecycle. Covers development, production, operations, support, and disposal phases with sensitivity analysis and alternative comparison.
output:
  format: "table"
---

# Life Cycle Cost Analysis

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Estimate lifecycle cost for a new system**: The user has a system concept or design and needs to estimate the total cost of ownership across all lifecycle phases from development through disposal.
**Interpretation 2 — Compare alternatives on total cost of ownership**: The user has two or more candidate solutions and needs to compare them on lifecycle cost to inform a selection decision.
**Interpretation 3 — Identify and reduce cost drivers**: The user has an existing system or cost estimate and wants to find the biggest cost drivers and evaluate cost reduction strategies.

If ambiguous, ask: "I can help with estimating lifecycle cost for a new system, comparing alternatives on total cost, or identifying cost drivers for reduction — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/lcca 4x [input]").

| Depth | Min Cost Elements | Min Phases | Min Alternatives Compared | Min Sensitivity Factors | Min Risk Items |
|-------|------------------|-----------|--------------------------|------------------------|---------------|
| 1x    | 10               | 4         | 1                        | 3                      | 3             |
| 2x    | 25               | 5         | 2                        | 5                      | 5             |
| 4x    | 50               | 6         | 3                        | 8                      | 8             |
| 8x    | 100              | 6         | 4                        | 12                     | 12            |
| 16x   | 200              | 7         | 5                        | 20                     | 20            |

---

## The Process

### Step 1: Define Lifecycle Phases

Establish the lifecycle model for this system:

```
SYSTEM: [name]
EXPECTED SERVICE LIFE: [N years]
ANALYSIS PERIOD: [N years, may extend beyond service life for disposal]
BASE YEAR: [year for constant-dollar analysis]
DISCOUNT RATE: [rate, e.g., 3% real, 7% nominal]

LIFECYCLE PHASES:

| Phase | Description | Duration | Start | End |
|-------|-------------|----------|-------|-----|
| 1. Concept & Planning | Requirements, feasibility, initial design | [N months/years] | [date] | [date] |
| 2. Development & Design | Detailed design, prototyping, engineering | [N months/years] | [date] | [date] |
| 3. Production & Deployment | Manufacturing, integration, installation, rollout | [N months/years] | [date] | [date] |
| 4. Operations & Maintenance | Normal system operations | [N years] | [date] | [date] |
| 5. Support & Sustainment | Upgrades, tech refresh, ongoing support | [concurrent with ops] | [date] | [date] |
| 6. Disposal & Decommission | Shutdown, data migration, teardown, environmental | [N months/years] | [date] | [date] |
```

---

### Step 2: Identify Cost Elements Per Phase

Break each phase into its cost elements using a Cost Breakdown Structure (CBS):

```
COST BREAKDOWN STRUCTURE:

1. CONCEPT & PLANNING
   1.1 Requirements analysis
   1.2 Feasibility studies
   1.3 Trade studies
   1.4 Project management (planning phase)
   1.5 Regulatory/compliance planning

2. DEVELOPMENT & DESIGN
   2.1 Systems engineering
   2.2 Hardware design & engineering
   2.3 Software design & development
   2.4 Prototype fabrication
   2.5 Development testing
   2.6 Documentation (technical manuals, user guides)
   2.7 Project management (development phase)
   2.8 Facilities and equipment (development)
   2.9 Quality assurance
   2.10 Configuration management

3. PRODUCTION & DEPLOYMENT
   3.1 Manufacturing / procurement
   3.2 Assembly & integration
   3.3 Production testing & acceptance
   3.4 Packaging & shipping
   3.5 Site preparation
   3.6 Installation & commissioning
   3.7 Initial training
   3.8 Initial spare parts & supplies
   3.9 Data migration (if replacing existing system)

4. OPERATIONS
   4.1 Operating personnel (salaries, benefits)
   4.2 Energy / utilities
   4.3 Consumables & supplies
   4.4 Facilities (rent, utilities, insurance)
   4.5 Licenses & subscriptions (recurring)
   4.6 Communication / connectivity

5. SUPPORT & SUSTAINMENT
   5.1 Preventive maintenance (scheduled)
   5.2 Corrective maintenance (unscheduled repairs)
   5.3 Spare parts & replenishment
   5.4 Software updates & patches
   5.5 Technology refresh / upgrades
   5.6 Help desk / user support
   5.7 Training (ongoing / refresher)
   5.8 Contractor support services
   5.9 Re-certification / compliance audits

6. DISPOSAL & DECOMMISSION
   6.1 System shutdown procedures
   6.2 Data archival & migration
   6.3 Environmental remediation
   6.4 Physical disassembly & removal
   6.5 Salvage value (negative cost / revenue)
   6.6 Regulatory decommissioning compliance
```

---

### Step 3: Estimate Costs

Apply appropriate estimation methods for each cost element:

| Method | When to Use | Accuracy | Data Needed |
|--------|------------|----------|-------------|
| **Analogy** | Similar system exists, early lifecycle | ±30-50% | Historical data from analogous system |
| **Parametric** | Statistical relationships known | ±20-35% | Cost estimating relationships (CERs), parameters |
| **Engineering Build-Up** | Detailed design available | ±10-20% | BOMs, labor rates, schedules, vendor quotes |
| **Expert Judgment** | No data available, unique system | ±40-60% | Subject matter experts, Delphi method |
| **Vendor Quotes** | Commercial components | ±5-15% | RFQs, catalog prices |

```
COST ESTIMATE TABLE:

| CBS ID | Cost Element | Method | Estimate (Base Year $) | Confidence | Basis of Estimate | Annual/One-Time |
|--------|-------------|--------|----------------------|------------|-------------------|-----------------|
| 1.1 | Requirements analysis | Expert | $[amount] | LOW/MED/HIGH | [source/rationale] | One-Time |
| 2.1 | Systems engineering | Parametric | $[amount] | MED | [CER used] | One-Time |
| 2.3 | Software development | Analogy | $[amount] | MED | [analogous system] | One-Time |
| 3.1 | Manufacturing | Build-Up | $[amount] | HIGH | [BOM + labor rates] | One-Time |
| 4.1 | Operating personnel | Build-Up | $[amount]/yr | HIGH | [N staff × rate] | Annual |
| 5.1 | Preventive maintenance | Parametric | $[amount]/yr | MED | [% of acquisition cost] | Annual |
...

ESTIMATE SUMMARY BY PHASE:

| Phase | One-Time Cost | Annual Cost | Phase Duration | Total Phase Cost |
|-------|--------------|-------------|----------------|-----------------|
| 1. Concept & Planning | $[amount] | — | [N years] | $[amount] |
| 2. Development | $[amount] | — | [N years] | $[amount] |
| 3. Production | $[amount] | — | [N years] | $[amount] |
| 4. Operations | — | $[amount]/yr | [N years] | $[amount] |
| 5. Support | — | $[amount]/yr | [N years] | $[amount] |
| 6. Disposal | $[amount] | — | [N years] | $[amount] |
| **TOTAL LIFECYCLE COST** | | | | **$[amount]** |
```

---

### Step 4: Account for Inflation and Discount Rates

Convert all costs to a common basis for comparison:

```
ECONOMIC ASSUMPTIONS:

| Parameter | Value | Source |
|-----------|-------|--------|
| Base year | [year] | [analysis convention] |
| Inflation rate (general) | [%] per year | [source, e.g., CPI forecast] |
| Inflation rate (labor) | [%] per year | [source] |
| Inflation rate (materials) | [%] per year | [source] |
| Real discount rate | [%] per year | [source, e.g., OMB Circular A-94] |
| Nominal discount rate | [%] per year | [calculated: real + inflation] |
| Analysis period | [N] years | [system lifecycle] |

PRESENT VALUE CALCULATION:

| Year | Phase | Nominal Cost | Discount Factor | Present Value (Base Year $) |
|------|-------|-------------|-----------------|---------------------------|
| 0 | Development | $[amount] | 1.000 | $[amount] |
| 1 | Development | $[amount] | [1/(1+r)^1] | $[amount] |
| 2 | Production | $[amount] | [1/(1+r)^2] | $[amount] |
| 3 | Operations | $[amount] | [1/(1+r)^3] | $[amount] |
...
| N | Disposal | $[amount] | [1/(1+r)^N] | $[amount] |

NET PRESENT VALUE (NPV): $[total]
TOTAL NOMINAL COST: $[total]
```

---

### Step 5: Perform Sensitivity Analysis

Identify which cost drivers have the biggest impact on total lifecycle cost:

```
SENSITIVITY ANALYSIS:

Baseline Total Lifecycle Cost: $[amount]

| Cost Driver | Baseline Value | Low Case (-20%) | High Case (+20%) | Impact on LCC | Rank |
|-------------|---------------|-----------------|------------------|---------------|------|
| Operating personnel | $[amount]/yr | $[total LCC] | $[total LCC] | ±$[delta] ([%]) | [1-N] |
| Software development | $[amount] | $[total LCC] | $[total LCC] | ±$[delta] ([%]) | [1-N] |
| Maintenance rate | [%]/yr | $[total LCC] | $[total LCC] | ±$[delta] ([%]) | [1-N] |
| System service life | [N] years | $[total LCC] | $[total LCC] | ±$[delta] ([%]) | [1-N] |
| Discount rate | [%] | $[total LCC] | $[total LCC] | ±$[delta] ([%]) | [1-N] |
| Energy costs | $[amount]/yr | $[total LCC] | $[total LCC] | ±$[delta] ([%]) | [1-N] |
...

TOP 3 COST DRIVERS (most sensitive):
1. [driver] — [%] of LCC, ±[%] swing
2. [driver] — [%] of LCC, ±[%] swing
3. [driver] — [%] of LCC, ±[%] swing

SCENARIO ANALYSIS:

| Scenario | Description | Total LCC | Delta from Baseline | Likelihood |
|----------|-------------|-----------|--------------------|-----------|
| Best Case | [low costs, short schedule, high salvage] | $[amount] | -[%] | LOW |
| Baseline | [expected values] | $[amount] | — | MEDIUM |
| Worst Case | [high costs, delays, no salvage] | $[amount] | +[%] | LOW |
| Most Likely | [weighted estimate] | $[amount] | [±%] | HIGH |
```

---

### Step 6: Compare Alternatives on Total Cost of Ownership

If comparing multiple options:

```
ALTERNATIVE COMPARISON:

| Cost Category | Alternative A | Alternative B | Alternative C | Notes |
|--------------|--------------|--------------|--------------|-------|
| Concept & Planning | $[amount] | $[amount] | $[amount] | |
| Development | $[amount] | $[amount] | $[amount] | |
| Production | $[amount] | $[amount] | $[amount] | |
| Operations (total) | $[amount] | $[amount] | $[amount] | |
| Support (total) | $[amount] | $[amount] | $[amount] | |
| Disposal | $[amount] | $[amount] | $[amount] | |
| **Total LCC (nominal)** | **$[amount]** | **$[amount]** | **$[amount]** | |
| **Total LCC (NPV)** | **$[amount]** | **$[amount]** | **$[amount]** | |
| Annual O&S cost | $[amount]/yr | $[amount]/yr | $[amount]/yr | |
| Break-even point | Year [N] | Year [N] | Year [N] | vs lowest acquisition cost |

COST-EFFECTIVENESS COMPARISON:

| Metric | Alt A | Alt B | Alt C |
|--------|-------|-------|-------|
| Total LCC (NPV) | $[amount] | $[amount] | $[amount] |
| Meets all MUST requirements? | YES/NO | YES/NO | YES/NO |
| Performance score (0-100) | [score] | [score] | [score] |
| Cost per performance point | $[amount] | $[amount] | $[amount] |
| Risk level | LOW/MED/HIGH | LOW/MED/HIGH | LOW/MED/HIGH |

RECOMMENDATION: Alternative [X] because [rationale]
```

---

## Output Format

```
## LIFECYCLE COST ESTIMATE: [System Name]

### System Profile
[Service life, analysis period, economic assumptions]

### Cost Breakdown Structure
[Hierarchical CBS with estimates per element]

### Phase Summary
| Phase | Cost | % of Total |
Development: $[X] ([Y]%)
Production: $[X] ([Y]%)
Operations & Support: $[X] ([Y]%)
Disposal: $[X] ([Y]%)
**Total LCC: $[X]**
**NPV: $[X]**

### Cost Distribution
Acquisition (one-time): $[X] ([Y]%)
Sustaining (recurring): $[X] ([Y]%)

### Sensitivity Analysis
Top cost drivers: [list]
Cost range: $[low] to $[high]

### Alternative Comparison (if applicable)
[Summary table with recommendation]

### Risks and Uncertainties
[Key cost risks with impact estimates]

### Recommendations
[Cost reduction opportunities, further analysis needed]
```

---

## Quality Checklist

Before completing:
- [ ] All lifecycle phases included (development through disposal)
- [ ] Cost elements identified for each phase
- [ ] Estimation method stated and justified for each element
- [ ] Inflation and discounting applied consistently
- [ ] Present value calculated using appropriate discount rate
- [ ] Sensitivity analysis performed on top cost drivers
- [ ] Confidence level stated for each estimate
- [ ] Recurring vs one-time costs clearly distinguished
- [ ] Basis of estimate documented for each element
- [ ] Alternatives compared on NPV (not just acquisition cost)

---

## Next Steps

After lifecycle cost analysis:
1. Use `/requirements` to verify cost-driving requirements and consider relaxing non-critical ones
2. Use `/sysdecomp` to map cost elements to system components
3. Use `/tpm` to track cost performance measures during development
4. Use `/tracematrix` to link cost estimates to requirements they support
5. Use `/dcp` to create decision procedure for cost vs performance trade-offs
6. Use `/fla` to anticipate cost overrun risks and plan mitigations