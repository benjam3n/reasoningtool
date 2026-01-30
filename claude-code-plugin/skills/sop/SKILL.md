---
name: sop
description: "Given limited time to extract procedures from sources, prioritize which sources to process for maximum procedure value."
---

# Source Prioritization

## Overview
Given limited time to extract procedures from sources, prioritize which sources to process for maximum procedure value.

## Steps

### Step 1: Gather source metadata
For each candidate source, collect or estimate:

1. Basic information:
   - Title, creator, type, URL
   - Length (duration/pages)
   - Publication date
   - Initial reason for adding to queue

2. Quick assessment (don't deep-dive yet):
   - Skim description/abstract/table of contents
   - Check creator credentials
   - Note topic areas covered
   - Estimate procedure density (HIGH/MEDIUM/LOW)

3. Volume metrics:
   - Total videos/items (for channels)
   - Total hours of content
   - Estimated transcript characters (hours x 9000)

Create standardized metadata for each source.

### Step 2: Score procedure density
Rate how rich each source is in extractable procedures (1-5):

5 - Almost entirely procedural (tutorials, courses, how-tos)
4 - Mostly procedural with some context
3 - Mix of procedural and informational
2 - Mostly informational with some procedures
1 - Almost entirely informational/entertainment

High density signals:
- Tutorial channels, course creators
- "How to" in most titles
- Step-by-step format common
- Practical demonstrations

Low density signals:
- News/commentary
- Entertainment focus
- Opinion/reaction content
- Abstract theory without application

### Step 3: Score uniqueness
Assess whether this source has knowledge unavailable elsewhere (1-5):

5 - Completely unique - only source for this knowledge
4 - Rare - few others have this perspective/access
3 - Somewhat unique - different angle on common topics
2 - Common - similar to many other sources
1 - Commodity - same as everyone else

High uniqueness signals:
- Original research/data
- Unique professional access
- Contrarian successful approaches
- Proprietary methods
- Decades of specialized experience

Low uniqueness signals:
- Summarizes others' work
- Common knowledge packaged
- Follows trends
- No original insight

### Step 4: Score relevance
Assess how relevant to YOUR specific goals (1-5):

5 - Directly applicable to current goals
4 - Highly relevant to goals
3 - Moderately relevant
2 - Tangentially relevant
1 - Interesting but not relevant

NOTE: This is PERSONAL - depends on what you're trying to achieve.
Cross-reference with extraction_goals and library_gaps.

### Step 5: Score credibility
Rate creator's track record of producing results (1-5):

5 - Proven exceptional results, widely recognized
4 - Strong track record, credible in field
3 - Some evidence of results
2 - Claims results but limited evidence
1 - No evidence, unverified claims

Credibility signals:
- Verifiable achievements
- Peer recognition
- Students/followers with results
- Published/cited work
- Professional credentials used

Low credibility signals:
- Only self-reported success
- No verifiable outcomes
- Sells without substance
- Contradicted by evidence

### Step 6: Score extractability
Rate how easy it is to extract procedures (1-5, higher = easier):

5 - Very easy - clear explanations, transcripts, structured
4 - Easy - good explanations, some structure
3 - Moderate - requires inference
2 - Hard - implicit, scattered, unstructured
1 - Very hard - no transcripts, unclear, heavily visual

Factors that improve extractability:
- Transcripts available
- Clear step-by-step explanations
- Written summaries/notes
- Consistent format
- Explicit about methods

Factors that reduce extractability:
- No transcripts, heavy accent
- Visual demonstrations without explanation
- Scattered across many videos
- Personality-heavy, procedure-light
- Assumes high prior knowledge

### Step 7: Calculate composite scores and ROI
Calculate weighted score for each source:

raw_score = (procedure_density x 0.25) +
            (uniqueness x 0.25) +
            (relevance x 0.20) +
            (credibility x 0.15) +
            (extractability x 0.15)

Then estimate extraction metrics:

estimated_procedures = content_hours x density_factor
- density_factor: score_5=3.0, score_4=2.0, score_3=1.0, score_2=0.5, score_1=0.2

unique_procedures = estimated_procedures x (uniqueness / 5)

extraction_value = unique_procedures x (relevance / 5)

extraction_hours = content_hours x extraction_multiplier
- manual_deep: 3.0 hours per 1 hour content
- manual_quick: 1.5 hours per 1 hour content
- automated_review: 0.5 hours per 1 hour content

adjusted_cost = extraction_hours / extractability_score

ROI = extraction_value / adjusted_cost

ROI interpretation:
- excellent: > 2.0 procedures per hour
- good: 1.0 - 2.0 procedures per hour
- acceptable: 0.5 - 1.0 procedures per hour
- poor: < 0.5 procedures per hour

### Step 8: Assign tiers
Assign each source to a tier based on scores:

TIER 1 - EXTRACT NOW:
- Criteria: ROI > 2.0 OR (raw_score > 4.0 AND relevance = 5)
- Action: Extract immediately, high priority

TIER 2 - EXTRACT SOON:
- Criteria: ROI 1.0-2.0 OR raw_score 3.5-4.0
- Action: Extract when Tier 1 complete

TIER 3 - EXTRACT LATER:
- Criteria: ROI 0.5-1.0 OR raw_score 3.0-3.5
- Action: Extract if time permits

TIER 4 - MAYBE:
- Criteria: ROI 0.25-0.5 OR raw_score 2.5-3.0
- Action: Only if specifically needed

TIER 5 - SKIP:
- Criteria: ROI < 0.25 OR raw_score < 2.5
- Action: Do not extract

Special considerations:
- Foundational sources: bump to Tier 1 if Tier 2-3
- Time-sensitive: bump priority if may become unavailable
- Bundled value: extract early if unlocks other sources
- Diminishing returns: after 10 procedures from one source, reassess

### Step 9: Create extraction schedule
Build ordered extraction schedule:

1. Within Tier 1, sequence by:
   - Foundational sources first
   - Quick wins early (high ROI, low volume)
   - Batch similar sources for efficiency

2. Allocate time based on budget:
   - Sum hours needed for each tier
   - If budget limited, may not reach lower tiers
   - Leave buffer for unexpected difficulty

3. Set checkpoints:
   - After every 10 procedures extracted
   - After completing each source
   - Weekly review of priorities

4. Create schedule document with:
   - Rank, source name, ROI, hours, expected procedures
   - Cumulative totals
   - Summary statistics

### Step 10: Document skip list
For Tier 5 sources and any dropped from lower tiers:

1. Record why skipped:
   - Below ROI threshold
   - Insufficient time
   - Redundant with existing library
   - Low credibility

2. Decide retention:
   - KEEP FOR LATER: Still valuable, review next quarter
   - DROP: Remove from queue entirely
   - CONDITIONAL: Keep if specific need arises

3. Create skip list table:
   | Source | Raw Score | ROI | Reason | Disposition |


## When to Use
- When you have multiple sources waiting for extraction
- Before starting a procedure extraction sprint
- When building extraction queue from content backlog
- When deciding whether to process new source vs queued sources
- During quarterly library planning
- When extraction time is limited and must be optimized
- After accumulating "watch later" or "read later" items
- When onboarding to GOSM and choosing initial extraction targets

## Verification
- All sources scored on all dimensions with evidence
- Weights reflect current priorities
- ROI calculation is consistent across sources
- Top priorities align with actual needs
- Time allocation is realistic and complete
- Skipped sources have clear rationale

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.