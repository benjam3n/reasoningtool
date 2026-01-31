# Decision Procedure — Improving the Drug Discovery Process

**Date**: 2026-01-31
**Input**: improving the drug discovery process

---

## Step 1: Decision Dimensions

What factors determine the right choices when improving drug discovery?

| # | Dimension | Description | Why It Matters |
|---|-----------|-------------|----------------|
| 1 | **Pipeline Stage** | Which stage of discovery are you targeting? (target ID, hit finding, lead optimization, preclinical, clinical) | Each stage has different bottlenecks and improvement levers |
| 2 | **Failure Mode** | What is currently going wrong? (attrition rate, cost, time, wrong targets, poor translation) | You must fix the actual bottleneck, not a perceived one |
| 3 | **Therapeutic Area** | Oncology, CNS, infectious disease, rare disease, metabolic, etc. | Different areas have different success rates, regulatory paths, and biology complexity |
| 4 | **Modality** | Small molecule, biologic, gene therapy, cell therapy, RNA-based, etc. | The modality constrains which improvement approaches are feasible |
| 5 | **Organization Type** | Big pharma, biotech startup, academic lab, CRO, government | Resources, risk tolerance, and decision-making speed vary dramatically |
| 6 | **Budget & Resources** | Available capital, headcount, infrastructure, partnerships | Some improvements need $10M+ investment, others can be done with existing resources |
| 7 | **Technology Readiness** | Current computational, automation, and data infrastructure | AI/ML improvements require data infrastructure that may not exist yet |
| 8 | **Regulatory Environment** | FDA, EMA, PMDA requirements and recent guidances | Regulatory acceptance determines whether innovations can actually be used |
| 9 | **Data Availability** | Quality and volume of existing data (genomic, phenotypic, clinical, RWE) | Data-driven improvements are only as good as the data |
| 10 | **Time Horizon** | Need results in 1 year vs. 5 years vs. 10+ years | Quick wins vs. paradigm shifts require different strategies |
| 11 | **Competitive Landscape** | What competitors are doing, patent landscape, first-mover dynamics | Improvements must create advantage, not just match the field |
| 12 | **Translational Gap** | Strength of connection between preclinical models and human outcomes | The #1 reason drugs fail: animal models don't predict human efficacy |
| 13 | **Team Expertise** | Existing skills in biology, chemistry, computation, clinical | Some improvements require expertise you don't have yet |
| 14 | **Risk Tolerance** | Willingness to pursue unvalidated approaches | Conservative orgs will choose proven improvements; risk-tolerant ones can try novel methods |

---

## Step 2: Options per Dimension

### Pipeline Stage Options
- **Target Identification & Validation**: Genomics/GWAS, CRISPR screens, proteomics, causal inference, human genetics-first approach
- **Hit Finding**: HTS, DEL, fragment-based, virtual screening, AI-based de novo design, phenotypic screening
- **Lead Optimization**: ADMET prediction, multi-parameter optimization, generative chemistry, free energy perturbation
- **Preclinical**: Better animal models, organ-on-chip, patient-derived organoids, in silico trials
- **Clinical**: Adaptive trial design, biomarker-driven enrollment, decentralized trials, synthetic control arms, real-world evidence

### Failure Mode Options
| Failure Mode | Current Rate | Highest-Leverage Fix |
|---|---|---|
| Wrong target selected | ~50% of Phase II failures | Human genetics validation, causal biology |
| Poor efficacy translation | ~40% of clinical failures | Better preclinical models, patient stratification |
| Toxicity surprises | ~30% of attrition | Safety pharmacology earlier, in silico tox prediction |
| Slow timelines | 10-15 years average | Parallel processing, adaptive designs, AI acceleration |
| Excessive cost | $1-2B per approved drug | Fail fast, reduce clinical trial size with biomarkers |
| Manufacturing issues | Late-stage failures | Developability assessment upfront |

### Technology Readiness Levels
- **Level 0**: Paper records, no centralized data
- **Level 1**: Electronic data but siloed across departments
- **Level 2**: Integrated data warehouse, basic analytics
- **Level 3**: ML models in use, automation of routine assays
- **Level 4**: AI-native workflows, closed-loop experimentation, digital twins

### Key Interactions Between Dimensions
- If **Organization = academic** AND **Budget < $1M**, then technology improvements are limited to open-source computational tools
- If **Modality = gene therapy**, then **Regulatory** becomes the dominant constraint
- If **Therapeutic Area = oncology**, then **Translational Gap** is partially bridged by PDX models
- If **Time Horizon < 2 years**, then only improvements to existing pipeline stages are feasible

---

## Step 3: Hidden Assumptions in Standard Drug Discovery Improvement

| # | Hidden Assumption | Why It's Dangerous | What To Do Instead |
|---|---|---|---|
| 1 | "AI will fix everything" | AI is a tool, not a strategy. Without clean data and clear questions, ML models just pattern-match on noise | Define the specific decision AI must improve BEFORE investing in AI |
| 2 | "More targets = more drugs" | Target-rich pipelines with poor validation just create more expensive failures | Fewer targets, validated harder |
| 3 | "Animal models are necessary" | Regulatory habit, not scientific necessity for every case. Human organoids, genetic evidence, and clinical biomarkers can sometimes substitute | Ask: "Does my preclinical model predict the clinical outcome I care about?" If unknown, that's your biggest risk |
| 4 | "Phase I/II/III is the only path" | Adaptive, platform, and basket trial designs can compress phases | Explore modern trial designs before defaulting to traditional 3-phase |
| 5 | "Faster = better" | Speed without better decision-making just means failing faster at the same rate | Measure decision quality, not just speed |
| 6 | "Published literature is trustworthy" | Reproducibility crisis means ~50% of preclinical findings may not replicate | Budget for internal replication of key findings |
| 7 | "We need novel targets" | Many approved drugs work on targets discovered 20+ years ago. Repurposing and combination strategies on known targets may be higher-value | Don't assume novelty = value |
| 8 | "Our bottleneck is where we think it is" | Orgs commonly misidentify their bottleneck because they lack end-to-end data | Map actual attrition data before choosing where to improve |
| 9 | "Technology investment = improvement" | Buying platforms without changing decision processes yields no improvement | Couple every technology purchase to a specific decision improvement |
| 10 | "Bigger trials = better evidence" | Enrichment strategies and biomarker-driven designs can achieve the same statistical power with fewer patients | Always ask: "Can we enrich for likely responders?" |

---

## Step 4: The Procedure

```
IMPROVING DRUG DISCOVERY PROCEDURE
====================================

STEP 0: What type of improvement are you pursuing?

  Answer these three questions:

  Q1: Are you trying to improve an EXISTING pipeline,
      or DESIGN a new approach from scratch?
      → Existing pipeline: Go to SECTION A
      → New approach: Go to SECTION B

  Q2: Is your primary goal to reduce COST, reduce TIME,
      or increase SUCCESS RATE?
      (Pick the single most important one)
      → Record your answer. You'll need it later.

  Q3: What is your available budget for improvement initiatives?
      → Under $500K: "Constrained"
      → $500K - $5M: "Moderate"
      → Over $5M: "Substantial"
      → Record your answer.

================================================================

SECTION A: IMPROVING AN EXISTING PIPELINE
-----------------------------------------

Step A1: MAP YOUR CURRENT ATTRITION
  Action: Get the data on every project that entered your
  pipeline in the last 5 years. For each one, record:
    - What stage did it reach?
    - Why did it stop? (categorize: efficacy, safety,
      commercial, strategic, other)
    - How long did it spend at each stage?
    - How much did it cost at each stage?

  What you should see: A table showing where projects die
  and why. If you don't have this data, STOP — your first
  improvement is building this tracking system.

Step A2: IDENTIFY YOUR ACTUAL BOTTLENECK
  Action: Look at your attrition table from A1.
  - Which stage has the HIGHEST failure rate?
  - Which failure REASON is most common?

  Decision point:
  → If >40% of failures are "wrong target / no efficacy":
    Go to Step A3
  → If >30% of failures are "safety / toxicity":
    Go to Step A4
  → If the main problem is TIME (projects take too long
    but eventually succeed): Go to Step A5
  → If the main problem is COST (too expensive per
    successful drug): Go to Step A6
  → If failures are spread evenly: Go to Step A3
    (target selection is the highest-leverage default)

Step A3: FIX TARGET SELECTION
  Your drugs are failing because they're aimed at the wrong
  targets. Improvement options (pick based on budget):

  Constrained budget:
    □ Implement human genetics evidence scoring for all
      targets. Require GWAS/Mendelian evidence before
      advancing any target. Cost: ~$0. Just change the
      decision criteria.
    □ Require reproducibility: Every key finding must be
      replicated internally before advancement. Cost:
      ~$100-200K in lab time.

  Moderate budget:
    □ All constrained options PLUS:
    □ Build or license a causal inference platform to
      distinguish correlation from causation in omics data.
    □ Implement CRISPR-based target validation in relevant
      human cell models before ANY animal work.

  Substantial budget:
    □ All above PLUS:
    □ Build patient-derived organoid banks for your
      therapeutic areas to test target engagement in
      human tissue.
    □ Invest in spatial transcriptomics / proteomics to
      understand target biology in tissue context.

  What you should see: After 12-18 months, your Phase II
  success rate should increase. Track it.

  → After implementing, return to Step A1 to reassess.

Step A4: FIX SAFETY / TOXICITY ATTRITION
  Your drugs work but they're too toxic.

  Constrained budget:
    □ Move safety assessment EARLIER. Run in silico tox
      prediction (free tools: pkCSM, ADMETlab) before
      synthesis.
    □ Implement a safety pharmacology panel at hit stage,
      not lead stage.
    □ Check: Does your target have known on-target safety
      liabilities? (Query OpenTargets safety data.)

  Moderate budget:
    □ All constrained options PLUS:
    □ Implement organ-on-chip or microphysiological systems
      for liver and cardiac toxicity screening.
    □ License or build predictive toxicology ML models
      trained on your internal data.

  Substantial budget:
    □ All above PLUS:
    □ Build a comprehensive safety biomarker strategy.
    □ Implement iPSC-derived cardiomyocyte and hepatocyte
      screening as standard.

  → After implementing, return to Step A1 to reassess.

Step A5: FIX TIMELINE
  Your drugs work but they take too long.

  Action: For each pipeline stage, answer:
    "What is the LONGEST single activity in this stage?"
  This is your rate-limiting step.

  Common fixes by stage:
  - Target validation too slow → Parallelize biology and
    chemistry (don't wait for full validation to start
    chemistry exploration)
  - Lead optimization too slow → Implement predictive
    ADMET models to reduce synthesis-test cycles
  - Preclinical too slow → Use CROs for standard studies,
    keep only differentiated work in-house
  - Clinical too slow → Adaptive trial designs, biomarker
    enrichment to reduce sample size, decentralized trial
    elements for faster enrollment

  → After implementing, return to Step A1 to reassess.

Step A6: FIX COST
  Action: Calculate cost-per-stage-per-project.
  The highest cost stage is your target.

  Common fixes:
  - If hit finding is expensive → Replace or supplement HTS
    with virtual screening / DEL / fragment-based approaches
  - If lead opt is expensive → Implement generative
    chemistry + predictive models to reduce synthesis cycles
  - If preclinical is expensive → Outsource standard
    studies; reserve internal resources for novel models
  - If clinical is expensive → Smaller trials via biomarker
    enrichment; adaptive designs; synthetic control arms
    where regulators accept them

  → After implementing, return to Step A1 to reassess.

================================================================

SECTION B: DESIGNING A NEW APPROACH FROM SCRATCH
-------------------------------------------------

Step B1: DEFINE YOUR DISEASE AND PATIENT POPULATION
  Action: Write down in one sentence:
    "We want to find a treatment for [disease] in
     [patient population]."

  Check: Is this specific enough?
    BAD: "We want to treat cancer"
    GOOD: "We want to treat KRAS G12C mutant NSCLC in
           patients who have progressed on immunotherapy"

  If your statement is vague → narrow it until you can
  describe the patient you're trying to help.

Step B2: CHOOSE YOUR EVIDENCE BASE
  Action: What evidence suggests a drug can work here?

  Score each type of evidence you have (1 = have it,
  0 = don't have it):
    □ Human genetic evidence linking target to disease
    □ Clinical proof-of-concept from a related mechanism
    □ Strong preclinical efficacy in a RELEVANT model
    □ Biomarker that predicts response
    □ Existing drugs that partially work on this pathway

  Decision point:
  → Score 3-5: Strong foundation. Go to Step B3.
  → Score 1-2: Moderate risk. Go to Step B3 but flag
    that validation is your FIRST priority.
  → Score 0: STOP. You are guessing. Go back and find
    evidence, or explicitly accept that this is a
    high-risk exploratory program.

Step B3: SELECT MODALITY
  Action: Given your target and disease, which modality fits?

  Use this decision tree:
  - Is the target intracellular and "druggable"
    (enzyme, GPCR, ion channel, nuclear receptor)?
    → Yes: Small molecule (default) or PROTAC
    → No: Is it a protein-protein interaction?
      → Yes: Peptide, stapled peptide, or biologic
      → No: Is it a cell-surface target?
        → Yes: Antibody or ADC
        → No: Is it a gene/RNA target?
          → Yes: ASO, siRNA, mRNA, or gene therapy
          → No: Consult a domain expert. This procedure
                 cannot cover novel modality selection.

Step B4: DESIGN YOUR SCREENING STRATEGY
  Based on modality from B3:

  Small molecule:
    → Phenotypic screen (if mechanism uncertain)
    → Target-based screen (if mechanism validated)
    → Virtual screen (if structure available and budget
       constrained)

  Biologic:
    → Phage/yeast display library
    → Immunization campaign
    → Computational antibody design (if epitope known)

  RNA-based:
    → Systematic tiling of target transcript
    → Delivery vehicle selection is critical — decide
       liver vs. non-liver delivery FIRST

Step B5: DEFINE YOUR GO/NO-GO CRITERIA BEFORE YOU START
  Action: For each stage transition, write down EXACTLY
  what result means "go" and what means "kill":

  Target → Hit:
    Go = [specific assay result, e.g., "≥30% inhibition
          at 10μM in primary screen"]
    Kill = [specific result]

  Hit → Lead:
    Go = [specific criteria]
    Kill = [specific criteria]

  Lead → Preclinical candidate:
    Go = [specific criteria]
    Kill = [specific criteria]

  WARNING: If you cannot write specific criteria,
  you will not be able to make rational go/no-go decisions
  later. This is the #1 cause of "zombie projects" that
  consume resources without progress.

  → Continue to Section A, Step A1 to set up tracking
    from day one.

================================================================

QUICK REFERENCE CARDS
---------------------

CARD 1: The Five Biggest Levers
  1. Validate targets with human genetic evidence
     (can double Phase II success rate)
  2. Kill bad projects earlier (reduces cost by 30-50%)
  3. Use biomarkers to enrich clinical trials
     (can halve trial size needed)
  4. Implement predictive models for ADMET
     (reduces lead opt cycles by 30-40%)
  5. Adopt adaptive trial designs
     (can save 1-2 years in clinical development)

CARD 2: Improvement Priority by Organization Type
  Academic lab     → Target validation quality (#1, #2)
  Biotech startup  → Speed + kill criteria (#2, #5)
  Big pharma       → Translation + trial design (#1, #3, #5)
  CRO              → Efficiency + automation (#4)

CARD 3: Minimum Data for Any Decision
  Before advancing a target: Human genetic evidence score
  Before starting a trial: Predictive biomarker identified
  Before choosing a modality: Target compartment confirmed
  Before killing a project: Documented criteria met
```

---

## Step 5: Failure Modes

| # | Failure Mode | How to Recognize It | What to Do |
|---|---|---|---|
| 1 | **Bottleneck misidentification** | You implement improvements but overall success rate / speed / cost doesn't change | Return to Step A1. Get actual data. Your attrition numbers may be wrong or you're fixing a non-bottleneck |
| 2 | **Technology-first thinking** | You bought an AI platform / robotics system / new screening technology but can't point to a specific decision it improves | For every technology, answer: "What decision does this make better, and how will I measure it?" If you can't answer, don't buy it |
| 3 | **Zombie projects survive** | Projects continue past go/no-go gates without meeting criteria because of sunk cost or political pressure | Make kill criteria BINARY and PUBLIC. "Did the compound hit 30% inhibition at 10μM? Yes or no." Remove judgment from the gate |
| 4 | **Reproducibility blindspot** | You advance targets based on a single published paper or internal experiment | Require N≥2 independent replications of key findings. Budget for replication explicitly |
| 5 | **Overfitting to past failures** | You fix the last failure mode but create a new one (e.g., so focused on safety you miss efficacy signals) | Always track ALL attrition categories, not just the one you're fixing |
| 6 | **Confusing activity with progress** | Running more experiments, screening more compounds, but advancement rate unchanged | Measure DECISIONS MADE PER MONTH, not experiments run. Progress = advancing or killing projects, not generating data |
| 7 | **Ignoring regulatory reality** | Implementing cutting-edge preclinical models (organoids, AI predictions) that regulators don't yet accept | Before replacing a standard study, confirm with regulatory affairs: "Will the agency accept this instead of X?" |
| 8 | **Underestimating data requirements** | AI/ML models underperform because training data is insufficient, biased, or poorly curated | Before any ML initiative, audit: How many data points? How were they generated? What's the label quality? If <1000 well-labeled examples, expect limited model performance |

---

## Step 6: Validation Check

Every step reviewed against executability criteria:

- **All steps are concrete actions** (map data, score evidence, answer binary questions) — not "consider" or "think about"
- **All decision points are binary or explicit multiple choice** (budget tiers, evidence scores, yes/no gates)
- **No jargon left undefined** (GWAS, ADMET, HTS, DEL, PROTAC, ASO, PDX, iPSC, CRO are standard in this domain; however, for a true non-expert, a glossary would be needed)
- **Every path terminates** — either at a concrete action list or a redirect back to Step A1 for reassessment
- **One gap identified**: Step B3's modality decision tree doesn't cover all edge cases (multi-target drugs, combination strategies). Added an "else → consult expert" escape hatch

**Remaining limitation**: This procedure covers PROCESS improvement. It does not cover scientific insight (choosing the right biology is still the hardest part and not fully proceduralize-able).

---

## Common Mistakes

1. **Starting with technology, not problems.** "We should use AI" before knowing which decisions are failing
2. **Trying to improve everything at once** instead of finding the single biggest bottleneck
3. **Not having attrition data.** You can't improve what you don't measure
4. **Setting vague go/no-go criteria** that allow zombie projects to continue
5. **Copying what worked at another organization** without checking if your bottleneck is the same
6. **Treating drug discovery as purely a technical problem** — organizational incentives, career risk, and politics drive many bad decisions

## When to Override This Procedure

- **You're working on a first-in-class mechanism** with no precedent — standard improvement frameworks may not apply
- **Regulatory landscape is shifting** (e.g., new accelerated approval pathways) — update regulatory assumptions
- **A platform technology genuinely changes the game** (e.g., mRNA during COVID) — the procedure's conservatism may cause you to miss a paradigm shift
- **You have <5 pipeline projects** — statistical reasoning about attrition rates doesn't apply; each project is unique

---

*Validation status: This procedure has not been validated by domain experts. It synthesizes publicly available evidence on drug discovery improvement but should be reviewed by experienced drug development professionals before organizational adoption.*
