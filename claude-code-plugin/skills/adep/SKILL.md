---
name: "adep - Adaptive Extraction Pipeline"
description: "Breadth-first, learned extraction pipeline that clarifies goals first, samples broadly, learns user preferences, and extracts selectively from highest-value items."
---

# Adaptive Extraction Pipeline

## Overview
Breadth-first, learned extraction pipeline that clarifies goals first, samples broadly, learns user preferences, and extracts selectively from highest-value items.

## Steps

### Step 1: Clarify extraction goals (Phase 0)
Use question_generation to clarify extraction priorities:

WEIGHTING QUESTION:
"When evaluating for extraction, which matters MORE?"
- Procedure density (more 'how to' per minute)
- Uniqueness (rare insights, can't find elsewhere)
- Direct relevance (applicable to current goals)
- Roughly equal (balanced)

PROCEDURE TYPES QUESTION:
"What types of procedures are you MOST interested in?"
- Technical methods (how to build/code/engineer)
- Thinking patterns (how experts reason/decide)
- Research methods (how to find/validate/synthesize)
- All types equally

PRIORITY DOMAINS QUESTION:
"What are your CURRENT priority domains?"
- AI/ML systems, Business/income, Research/learning
- Health/o, Engineering/hardware

SKIP THRESHOLD QUESTION:
"At what point would you SKIP a video entirely?"
- < 1 procedure expected
- Low uniqueness (could find elsewhere)
- Off-topic for current goals

Duration: 10-15 minutes

### Step 2: Get broad sample (Phase 1)
Sample broadly across source collection:

1. Get video/content lists from sources
   - ~10 recent items from each Tier 1 source
   - Target: ~100 items total for calibration

2. Fetch transcript/content samples
   - First ~2000 characters per item
   - Enough to assess without full processing

3. Ensure diversity:
   - Mix of sources
   - Mix of content types
   - Mix of topics

### Step 3: Run initial triage
Score each sampled item on extraction profile criteria:

DENSITY (1-5): How much is 'how to' vs 'what is'?
UNIQUENESS (1-5): Could find this knowledge elsewhere?
RELEVANCE (1-5): Matches priority domains?
EXPECTED_PROCEDURES (0-10): Estimated extractable procedures

Calculate composite score:
composite = (density * w_d + uniqueness * w_u + relevance * w_r)
            * (expected_procedures / 5)

where weights come from extraction_profile.weighting:
- balanced: w_d=0.33, w_u=0.33, w_r=0.33
- density_first: w_d=0.5, w_u=0.25, w_r=0.25
- uniqueness_first: w_d=0.25, w_u=0.5, w_r=0.25
- relevance_first: w_d=0.25, w_u=0.25, w_r=0.5

### Step 4: Calibrate with user ratings
User manually rates ~20 items to calibrate model:

1. Present items in random order
2. User rates each 1-10 for extraction value
3. Duration: ~1 hour (3 min per item)

Purpose: Learn where model predictions diverge from user preferences

Calibration output:
- Items where model overestimated (user rated lower)
- Items where model underestimated (user rated higher)
- Patterns in divergence

### Step 5: Validate triage model
Compare model predictions to user ratings:

Calculate correlation:
- Pearson correlation between predicted and actual scores
- Target: correlation > 0.7 means model is calibrated

If correlation < 0.7:
- Identify systematic biases
- Ask clarifying questions about divergences
- Adjust weights or criteria
- Re-run triage on calibration set

If correlation >= 0.7:
- Model is calibrated, proceed to Phase 2

### Step 6: Scale triage to all sources (Phase 2)
Apply calibrated model to full source collection:

1. Expand to all sources:
   - Get content lists from ALL channels (Tier 1-3)
   - Target: full coverage (~5000 items typical)

2. Batch triage:
   - Fetch transcript samples for all items
   - Run calibrated scoring model
   - Use LLM for initial scoring (Haiku for efficiency)

3. Global ranking:
   - Sort ALL items by composite score
   - Single ranked list across all sources

### Step 7: Identify extraction targets
Mark items for extraction based on budget:

Heuristic: Top 100 items often = 50%+ of total value

Budget allocation:
- Calculate items affordable within budget
- Consider: top 10% often yields 50% of value
- Mark clear "extract" vs "skip" vs "maybe"

Create extraction queue:
- Ordered by score (highest first)
- Include estimated extraction time
- Include skip flags for items below threshold

### Step 8: Execute selective extraction (Phase 3)
Full extraction on highest-value items only:

1. Run 3-pass extraction on queued items:
   - Pass 1 (Explicit): What they SAY (HIGH confidence)
   - Pass 2 (Implicit): What they DO (MEDIUM confidence)
   - Pass 3 (Meta): HOW they think (MEDIUM confidence)

2. Track actual yield:
   - Record procedures extracted vs predicted
   - Note where predictions were accurate/inaccurate

3. Monitor for diminishing returns:
   - Track procedures per item in rolling window
   - If rate drops below 2 procedures/item, reassess

### Step 9: Update model for future runs
Apply evolutionary improvement to triage model:

1. Analyze prediction accuracy:
   - Which criteria correlated with actual yield?
   - Which criteria were noise?

2. Evolve successful criteria:
   - Keep/strengthen criteria that predicted well
   - Modify criteria that were partially predictive
   - Drop criteria that didn't correlate

3. Document learnings:
   - What types of content yielded best?
   - What skip criteria were accurate?
   - Recommendations for next extraction run


## When to Use
- When starting extraction from a new user's sources
- When user priorities are unclear or unstated
- When processing large source collections (100+ videos)
- When extraction budget requires high precision targeting
- When previous extraction didn't match user expectations
- After changing goals or priorities
- When optimizing extraction ROI is critical

## Verification
- User preferences captured through explicit questions
- Model calibrated with user ratings (correlation > 0.7)
- Global ranking covers all sources
- Extraction focused on highest-value items
- Actual yield tracked against predictions
- Model improved based on outcomes

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.