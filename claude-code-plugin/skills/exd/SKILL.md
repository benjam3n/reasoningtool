---
name: "exd - Experimental Design"
description: "Systematic procedure for designing rigorous experiments with proper controls, variables, and validity considerations"
---

# Experimental Design

## Overview
Systematic procedure for designing rigorous experiments with proper controls, variables, and validity considerations

## Steps

### Step 1: Formulate testable hypotheses
Transform the research question into testable hypotheses:

1. STATE THE RESEARCH HYPOTHESIS (H1)
   - Make it specific and directional when theory supports
   - Example: "Participants who receive intervention X will show
     higher scores on outcome Y than control participants"
   - Ensure it specifies the expected direction and magnitude

2. STATE THE NULL HYPOTHESIS (H0)
   - The hypothesis of no effect
   - Example: "There is no difference in outcome Y between
     intervention and control groups"

3. SPECIFY PREDICTIONS
   - Quantitative predictions when possible
   - What pattern of results would support H1?
   - What pattern would falsify H1?

4. GROUND IN THEORY
   - Why do you expect this effect?
   - What mechanism explains the causal relationship?
   - Hypotheses should follow from theory, not be data-mined

5. CHECK FOR TESTABILITY
   - Can the hypothesis be falsified?
   - Is the prediction specific enough to be tested?
   - Could any result be interpreted as support?

COMMON PITFALLS:
- Vague hypotheses that any result could "support"
- Untestable claims (no possible disconfirming evidence)
- HARKing (hypothesizing after results known)

### Step 2: Identify and operationalize variables
Define all variables with precise operational definitions:

INDEPENDENT VARIABLES (IVs)
- The variables you manipulate
- Specify levels/conditions precisely
- How will manipulation be delivered?
- Manipulation check: How will you verify manipulation worked?

DEPENDENT VARIABLES (DVs)
- The outcomes you measure
- How will each be measured? (instrument, scale, timing)
- What is the unit of analysis?
- Are measures reliable and valid?

CONTROL VARIABLES
- Variables held constant across conditions
- Why are they held constant?
- How will constancy be ensured?

CONFOUNDING VARIABLES
- Variables that could provide alternative explanations
- How will each be controlled or measured?
- Consider: selection, history, maturation, instrumentation

MODERATOR VARIABLES
- Variables that might change the effect strength
- Will you test for moderation?
- How will moderators be measured?

MEDIATOR VARIABLES
- Variables that might explain the causal mechanism
- Will you test for mediation?
- How will mediators be measured?

OPERATIONAL DEFINITIONS
For each variable, specify:
- Conceptual definition: What the construct means
- Operational definition: Exactly how it will be measured/manipulated
- Measurement timing: When measurement occurs
- Measurement source: Self-report, observation, physiological, etc.

### Step 3: Select experimental design
Choose the appropriate experimental design structure:

BETWEEN-SUBJECTS DESIGNS
- Different participants in each condition
- Pro: No carryover effects
- Con: Requires more participants; individual differences are noise
- Use when: Manipulation cannot be reversed; learning effects likely

WITHIN-SUBJECTS DESIGNS
- Same participants experience all conditions
- Pro: More statistical power; controls for individual differences
- Con: Order effects, carryover, practice effects
- Use when: Individual differences are large; participants scarce
- Requires: Counterbalancing order across participants

MIXED DESIGNS
- Some factors between, some within
- Example: Treatment vs. control (between) measured at multiple times (within)

FACTORIAL DESIGNS
- Multiple IVs crossed (all combinations)
- Allows testing of interaction effects
- 2x2 design: 2 IVs, each with 2 levels = 4 conditions
- Consider: Full factorial vs. fractional if many factors

SPECIFIC DESIGN TYPES:
- Randomized Controlled Trial (RCT): Random assignment to conditions
- Pre-test/Post-test Control Group: Measure before and after
- Solomon Four-Group: Controls for pre-test sensitization
- Crossover Design: Participants receive all treatments in sequence
- Matched Pairs: Match on key variables before random assignment
- Block Design: Group by nuisance variable, randomize within blocks

QUASI-EXPERIMENTAL DESIGNS (when randomization impossible):
- Non-equivalent control group: Compare existing groups
- Regression discontinuity: Exploit cutoff assignment
- Interrupted time series: Multiple measurements around intervention
- Difference-in-differences: Compare change across groups over time

### Step 4: Plan controls and randomization
Specify how you will control for alternative explanations:

CONTROL CONDITIONS
- No-treatment control: No intervention (measures natural change)
- Placebo control: Inactive treatment (controls for expectancy)
- Active control: Alternative treatment (compares interventions)
- Waitlist control: Delayed treatment (ethical for beneficial treatments)
- Attention control: Same time/attention, different content

Choose control based on:
- What comparison is scientifically meaningful?
- What is ethical given the intervention?
- What controls for expectancy and demand effects?

RANDOMIZATION
- Simple randomization: Coin flip, random number
- Stratified randomization: Ensure balance on key variables
- Block randomization: Randomize within blocks for temporal balance
- Minimization: Algorithm to minimize group differences
- Cluster randomization: Randomize groups, not individuals

Document:
- Randomization method and implementation
- Who generates the sequence?
- How is allocation concealed?

BLINDING
- Single-blind: Participants don't know condition
- Double-blind: Participants and administrators don't know
- Triple-blind: Includes analysts
- When blinding impossible, assess expectancy effects

ADDITIONAL CONTROLS
- Standardized procedures: Same protocol for all participants
- Standardized instructions: Script for experimenters
- Standardized environment: Same setting, time of day, etc.
- Manipulation checks: Verify manipulation worked as intended
- Attention checks: Verify participants engaged with materials

### Step 5: Determine sample size and power
Calculate required sample size through power analysis:

POWER ANALYSIS COMPONENTS
- Effect size: Expected magnitude of the effect
  * Cohen's d for means: 0.2 small, 0.5 medium, 0.8 large
  * Correlation r: 0.1 small, 0.3 medium, 0.5 large
  * Use prior research or smallest meaningful effect

- Alpha level (Type I error rate): Usually 0.05
  * Probability of false positive
  * Adjust for multiple comparisons if needed

- Power (1 - Type II error rate): Usually 0.80 or higher
  * Probability of detecting effect if it exists
  * 0.80 = 80% chance of detecting true effect

- Sample size: What we're solving for

POWER ANALYSIS PROCESS
1. Estimate expected effect size from:
   - Prior research (meta-analyses ideal)
   - Pilot study
   - Smallest effect that would be meaningful

2. Set alpha (usually 0.05)

3. Set desired power (usually 0.80)

4. Calculate required N using:
   - G*Power software
   - Statistical package functions
   - Online calculators

5. Adjust for:
   - Expected attrition (inflate N)
   - Cluster randomization (design effect)
   - Planned subgroup analyses

SAMPLE SIZE CONSIDERATIONS
- More conditions require more participants
- Within-subjects designs require fewer participants
- Cluster randomization requires more participants
- Rare populations may limit achievable N

WHEN EFFECT SIZE IS UNKNOWN
- Use smallest effect size of interest (SESOI)
- Conduct pilot study
- Use field-typical effect sizes
- Plan for range of effect sizes

Document power analysis with all inputs and calculations.

### Step 6: Analyze validity threats
Systematically identify and address threats to validity:

INTERNAL VALIDITY (Is the causal inference valid?)

- History: External events during study affect outcomes
  Mitigation: Control group experiences same history

- Maturation: Natural changes over time
  Mitigation: Control group matures equally; shorter timeframe

- Testing effects: Pre-test affects post-test
  Mitigation: Solomon four-group design; no pre-test

- Instrumentation: Measurement changes during study
  Mitigation: Standardize instruments; calibrate regularly

- Regression to mean: Extreme scores naturally regress
  Mitigation: Don't select on extreme scores; use reliable measures

- Selection bias: Groups differ before intervention
  Mitigation: Random assignment; matching; check baseline

- Attrition: Differential dropout across conditions
  Mitigation: Track attrition; analyze dropouts; intent-to-treat

- Diffusion: Control group receives treatment elements
  Mitigation: Separate conditions physically/temporally

- Compensatory behavior: Controls compensate or demoralize
  Mitigation: Keep conditions blind; use active controls

EXTERNAL VALIDITY (Does it generalize?)

- Population validity: Do findings generalize to other people?
  Mitigation: Representative sampling; replicate in other samples

- Ecological validity: Do findings generalize to real settings?
  Mitigation: Field experiments; realistic contexts

- Temporal validity: Do findings hold over time?
  Mitigation: Replicate at different times; long-term follow-up

- Treatment variation: Would other implementations show effect?
  Mitigation: Describe treatment fully; test variations

CONSTRUCT VALIDITY (Are we measuring what we think?)

- Mono-operation bias: Single operationalization of construct
  Mitigation: Multiple measures of each construct

- Mono-method bias: Single method for all measures
  Mitigation: Multiple methods (self-report, behavioral, etc.)

- Hypothesis guessing: Participants figure out hypothesis
  Mitigation: Blinding; cover story; measure awareness

- Demand characteristics: Participants respond to expectations
  Mitigation: Blinding; implicit measures; unobtrusive measures

- Experimenter bias: Experimenter influences results
  Mitigation: Blinding; scripted protocols; multiple experimenters

STATISTICAL CONCLUSION VALIDITY

- Low power: True effects missed
  Mitigation: Adequate sample size; power analysis

- Violated assumptions: Statistical test assumptions not met
  Mitigation: Check assumptions; use robust methods

- Multiple testing: Inflated false positive rate
  Mitigation: Correct for multiple comparisons; pre-register

- Unreliable measures: Measurement error obscures effects
  Mitigation: Use reliable instruments; aggregate measures

### Step 7: Specify analysis plan
Pre-specify the statistical analysis approach:

1. PRIMARY ANALYSIS
   - State the main analysis that tests the primary hypothesis
   - Specify the statistical test to be used
   - Define what constitutes support for the hypothesis
   - Alpha level and any corrections

2. SECONDARY ANALYSES
   - Additional planned analyses
   - Exploratory analyses (label as such)
   - Distinguish confirmatory from exploratory

3. STATISTICAL TESTS BY DESIGN
   - Two groups, one DV: t-test (independent or paired)
   - Multiple groups, one DV: ANOVA
   - Multiple DVs: MANOVA
   - Continuous predictor: Regression
   - Categorical outcome: Logistic regression/chi-square
   - Repeated measures: Repeated-measures ANOVA, mixed models
   - Nested data: Multilevel/hierarchical models

4. ASSUMPTION CHECKS
   - What assumptions will be checked?
   - What will you do if assumptions violated?
   - Planned alternatives (non-parametric, transformations)

5. HANDLING MISSING DATA
   - Prevention strategies
   - Analysis approach (listwise, pairwise, imputation)
   - Sensitivity analyses

6. EFFECT SIZE REPORTING
   - Which effect sizes will be reported?
   - Confidence intervals around effects

7. SENSITIVITY ANALYSES
   - Alternative specifications to test robustness
   - What would change conclusions?

PRE-REGISTRATION
- Register analysis plan before data collection
- Platforms: OSF, AsPredicted, ClinicalTrials.gov
- Document any deviations from pre-registered plan


## When to Use
- Designing a study to test a causal hypothesis
- Planning A/B tests or randomized experiments
- Evaluating interventions or treatments
- Testing product or feature changes
- Conducting laboratory or field experiments
- Designing pilot studies before larger trials
- Planning quasi-experimental research when randomization is limited
- Preparing grant proposals requiring experimental methodology

## Verification
- Hypotheses are specific, directional, and falsifiable
- All variables have operational definitions
- Design supports causal inference (randomization or quasi-experimental controls)
- Sample size justified by power analysis
- All four types of validity threats addressed
- Analysis plan pre-specified before data collection
- Appropriate controls for research question

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.