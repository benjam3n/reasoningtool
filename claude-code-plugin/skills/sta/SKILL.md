---
name: "sta - Statistical Analysis"
description: "Systematic procedure for selecting appropriate statistical tests and correctly interpreting results"
---

# Statistical Analysis

## Overview
Systematic procedure for selecting appropriate statistical tests and correctly interpreting results

## Steps

### Step 1: Clarify the statistical question
Translate the research question into a statistical question:

TYPES OF STATISTICAL QUESTIONS:

1. COMPARISON QUESTIONS
   - "Is there a difference between groups?"
   - "Are means/proportions different?"
   Examples: Treatment vs. control, before vs. after

2. RELATIONSHIP QUESTIONS
   - "Is there an association between variables?"
   - "Does X predict Y?"
   Examples: Correlation, regression

3. PREDICTION QUESTIONS
   - "Can we predict outcomes from predictors?"
   - "How accurate are predictions?"
   Examples: Machine learning, forecasting

4. STRUCTURE QUESTIONS
   - "What is the underlying structure?"
   - "How do variables cluster?"
   Examples: Factor analysis, cluster analysis

SPECIFY:
- What is the outcome/dependent variable?
- What are the predictors/independent variables?
- Are you testing a specific hypothesis or exploring?
- What kind of answer do you need? (yes/no, magnitude, prediction)

CONFIRMATORY VS. EXPLORATORY:
- Confirmatory: Testing pre-specified hypothesis
  * Requires pre-registration; controls Type I error
- Exploratory: Discovering patterns in data
  * Generates hypotheses; results need replication

Be explicit about which mode you're in.

### Step 2: Characterize the data
Understand your data before selecting tests:

VARIABLE TYPES:

Categorical (qualitative):
- Nominal: Categories without order (e.g., treatment group, gender)
- Ordinal: Ordered categories (e.g., Likert scale, education level)

Numerical (quantitative):
- Continuous: Any value in range (e.g., time, weight, temperature)
- Discrete: Countable values (e.g., count of events)

For each variable, note:
- Type (nominal, ordinal, continuous, discrete)
- Role (outcome, predictor, covariate, grouping)
- Distribution (normal, skewed, bimodal)
- Missing data pattern and extent

DATA STRUCTURE:

- Independence: Are observations independent?
  * Independent: Different subjects, no clustering
  * Paired/matched: Same subjects measured twice, or matched pairs
  * Clustered: Subjects nested in groups (students in classrooms)
  * Time series: Observations over time from same unit

- Sample size per group

- Balance: Equal or unequal group sizes?

PRELIMINARY EXAMINATION:
- Summary statistics (mean, SD, median, IQR)
- Frequency tables for categorical variables
- Histograms and boxplots for continuous variables
- Check for outliers and data entry errors
- Examine missing data patterns

### Step 3: Select appropriate statistical test
Choose the test that matches your question and data:

COMPARING TWO GROUPS:

| Outcome Type | Independent Groups | Paired/Matched |
|--------------|-------------------|----------------|
| Continuous   | Independent t-test | Paired t-test  |
| Ordinal      | Mann-Whitney U     | Wilcoxon signed-rank |
| Categorical  | Chi-square/Fisher  | McNemar's test |

COMPARING THREE+ GROUPS:

| Outcome Type | Independent Groups | Repeated Measures |
|--------------|-------------------|-------------------|
| Continuous   | One-way ANOVA     | Repeated-measures ANOVA |
| Ordinal      | Kruskal-Wallis    | Friedman test     |
| Categorical  | Chi-square        | Cochran's Q       |

EXAMINING RELATIONSHIPS:

| Predictor(s) | Outcome Type | Test |
|--------------|--------------|------|
| Continuous   | Continuous   | Pearson correlation, linear regression |
| Continuous   | Binary       | Logistic regression |
| Continuous   | Count        | Poisson regression |
| Multiple     | Continuous   | Multiple regression |
| Multiple     | Binary       | Multiple logistic regression |

SPECIAL CASES:

- Clustered data: Mixed-effects/multilevel models
- Time series: Time series methods, repeated measures
- Survival/duration: Survival analysis (Kaplan-Meier, Cox)
- Multiple outcomes: MANOVA, structural equation modeling

DECISION FACTORS:
1. Type of outcome variable (determines test family)
2. Number of groups/predictors
3. Independence structure of observations
4. Sample size (parametric vs. non-parametric)
5. Assumption satisfaction

When in doubt:
- Simpler methods often more robust
- Non-parametric methods when assumptions violated
- Consult statistician for complex designs

### Step 4: Check assumptions
Verify that test assumptions are satisfied:

PARAMETRIC TEST ASSUMPTIONS:

1. NORMALITY
   Check: Histogram, Q-Q plot, Shapiro-Wilk test
   - Exact normality rarely required
   - Central Limit Theorem helps with n > 30 per group
   - More important for small samples
   Violation remedy: Transform data; use non-parametric test

2. HOMOGENEITY OF VARIANCE
   Check: Levene's test, F-max test, visual inspection
   - Groups should have similar variances
   - More important with unequal group sizes
   Violation remedy: Welch's t-test; transformed data; robust SE

3. INDEPENDENCE
   Check: Study design review
   - Observations should be independent
   - Most critical assumption
   Violation remedy: Use paired/clustered methods

4. LINEARITY (for regression)
   Check: Residual plots, scatterplots
   - Relationship should be linear
   Violation remedy: Transform variables; polynomial terms

5. HOMOSCEDASTICITY (for regression)
   Check: Residual vs. fitted plot
   - Variance should be constant across predicted values
   Violation remedy: Robust standard errors; weighted regression

REPORTING ASSUMPTION CHECKS:
- Report what was checked and how
- Report results of assumption tests
- Describe remedies applied if assumptions violated
- Consider sensitivity analysis with alternative methods

ROBUST ALTERNATIVES:
- Welch's t-test (doesn't assume equal variance)
- Non-parametric tests (don't assume normality)
- Robust regression (handles outliers)
- Bootstrapping (makes minimal assumptions)

### Step 5: Conduct the analysis
Execute the statistical analysis:

1. RUN THE ANALYSIS
   - Use appropriate software (R, Python, SPSS, Stata)
   - Double-check data entry and coding
   - Verify degrees of freedom match expectation
   - Save code/syntax for reproducibility

2. RECORD KEY STATISTICS

   For hypothesis tests:
   - Test statistic (t, F, chi-square, z, etc.)
   - Degrees of freedom
   - P-value (exact, not just < .05)
   - Sample size (per group if applicable)

   For effect sizes:
   - Point estimate (d, r, OR, RR, etc.)
   - 95% confidence interval
   - Interpret magnitude (small, medium, large)

   For regression:
   - Coefficients with standard errors
   - Confidence intervals
   - Model fit (R-squared, AIC, etc.)
   - Residual diagnostics

3. EFFECT SIZE CALCULATION

   For mean differences:
   - Cohen's d = (M1 - M2) / pooled SD
     * 0.2 = small, 0.5 = medium, 0.8 = large
   - Hedges' g (corrects for small sample bias)

   For correlations:
   - Pearson's r (or Spearman's rho)
     * 0.1 = small, 0.3 = medium, 0.5 = large
   - R-squared (proportion of variance explained)

   For categorical outcomes:
   - Odds ratio (OR)
   - Risk ratio/Relative risk (RR)
   - Number needed to treat (NNT)

   For ANOVA:
   - Eta-squared or partial eta-squared
   - Omega-squared (less biased)

4. CONFIDENCE INTERVALS
   - Always report CIs for effect sizes
   - 95% CI most common (corresponds to alpha = .05)
   - Interpret: Range of plausible population values
   - If CI excludes zero/one, effect is "significant"

### Step 6: Interpret results correctly
Translate statistical results into meaningful conclusions:

INTERPRETING P-VALUES:

What p-value IS:
- Probability of data (or more extreme) IF null hypothesis true
- Measure of evidence against H0

What p-value IS NOT:
- Probability that H0 is true
- Probability that results are due to chance
- Measure of effect size or importance
- Probability of replication

Common thresholds (arbitrary but conventional):
- p < .05: "Statistically significant"
- p < .01: "Highly significant"
- p < .001: "Very highly significant"

Better practice:
- Report exact p-values (p = .032, not p < .05)
- Focus on effect size and CI, not just significance
- Consider p-value in context of power and prior probability

INTERPRETING EFFECT SIZES:

Cohen's conventions (context-dependent):
- Small: d = 0.2, r = 0.1
- Medium: d = 0.5, r = 0.3
- Large: d = 0.8, r = 0.5

Better approach:
- Compare to prior research in the field
- Consider practical/clinical significance
- Use domain knowledge to interpret magnitude

INTERPRETING CONFIDENCE INTERVALS:

95% CI interpretation:
- "We are 95% confident the true value is in this range"
- If CI for difference excludes zero: significant difference
- Narrow CI: Precise estimate; Wide CI: Imprecise estimate

What CI tells you that p-value doesn't:
- Magnitude of effect (not just direction)
- Precision of estimate
- Range of plausible values

NON-SIGNIFICANT RESULTS:

"Not significant" does NOT mean:
- No effect exists
- Effect is zero
- Null hypothesis is true

It DOES mean:
- Cannot reject H0 with this sample
- Effect may exist but study underpowered
- Evidence is inconclusive

Report: Effect size, CI, and power to detect meaningful effect

### Step 7: Address multiple testing and report fully
Handle multiple comparisons and report transparently:

MULTIPLE TESTING PROBLEM:

- Each test at alpha = .05 has 5% false positive rate
- 20 tests: expect 1 false positive by chance
- Family-wise error rate increases rapidly

CORRECTION METHODS:

1. Bonferroni correction
   - Adjusted alpha = 0.05 / number of tests
   - Conservative; reduces power
   - Use when: Small number of planned tests

2. Holm-Bonferroni (step-down)
   - Less conservative than Bonferroni
   - Controls family-wise error
   - Use when: Multiple planned comparisons

3. False Discovery Rate (FDR)
   - Benjamini-Hochberg procedure
   - Controls proportion of false positives
   - Use when: Many tests (e.g., genomics)

4. No correction (with justification)
   - Pre-registered primary analysis
   - Clearly labeled exploratory analyses
   - Replication planned

WHEN TO CORRECT:
- Multiple outcomes on same hypothesis
- Multiple subgroup analyses
- Post-hoc pairwise comparisons

WHEN CORRECTION MAY NOT BE NEEDED:
- Single pre-registered primary outcome
- Clearly labeled exploratory analyses
- Independent research questions

TRANSPARENT REPORTING:

Report:
1. All analyses conducted (not just significant ones)
2. How analyses were specified (pre-registered or post-hoc)
3. Any corrections applied for multiple testing
4. Exact p-values, effect sizes, and confidence intervals
5. Sample sizes and degrees of freedom
6. Assumption checks and any violations
7. Software and version used

Follow reporting guidelines:
- APA style for psychology
- CONSORT for clinical trials
- STROBE for observational studies

### Step 8: Document limitations and conclusions
Identify statistical limitations and draw appropriate conclusions:

COMMON STATISTICAL LIMITATIONS:

1. POWER LIMITATIONS
   - Small sample may miss real effects
   - Report achieved power for observed effect
   - Non-significant ≠ no effect

2. ASSUMPTION VIOLATIONS
   - Which assumptions were questionable?
   - How might this affect conclusions?
   - Did robust methods help?

3. MISSING DATA
   - How much was missing?
   - Was missingness random or systematic?
   - How was it handled?

4. MEASUREMENT ISSUES
   - Reliability of measures
   - Validity concerns
   - Measurement error implications

5. GENERALIZABILITY
   - Sample representativeness
   - Context specificity
   - Replication needs

APPROPRIATE CONCLUSIONS:

DO:
- Conclude about population parameters
- Distinguish statistical from practical significance
- Acknowledge uncertainty (CIs, p-values)
- Note limitations on causal inference
- Suggest replication and future directions

DON'T:
- Overstate certainty
- Treat non-significant as "no effect"
- Confuse correlation with causation
- Generalize beyond sample characteristics
- Make causal claims from observational data

FINAL CHECKLIST:
- [ ] Research question answered?
- [ ] Appropriate test used?
- [ ] Assumptions checked?
- [ ] Effect size reported with CI?
- [ ] Multiple testing addressed?
- [ ] Limitations acknowledged?
- [ ] Conclusions proportionate to evidence?


## When to Use
- Analyzing data from experiments or observational studies
- Testing hypotheses with quantitative data
- Comparing groups or examining relationships
- Building predictive or explanatory models
- Evaluating program or intervention effectiveness
- Making data-driven decisions requiring statistical evidence
- Reviewing or critiquing statistical analyses

## Verification
- Statistical question clearly specified
- Test selection matches data type and research question
- All assumptions checked and violations addressed
- Effect sizes reported with confidence intervals
- P-values correctly interpreted (not over-interpreted)
- Multiple testing addressed if applicable
- Limitations acknowledged
- Analysis is reproducible

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.