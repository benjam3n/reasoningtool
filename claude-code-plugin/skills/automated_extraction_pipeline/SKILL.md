---
name: automated_extraction_pipeline
description: "Industrial-scale automation pipeline for extracting procedures from 70+ YouTube channels and other sources using the Ralph Wiggum / Conductor pattern for iterative LLM-driven extraction."
---

# Automated Extraction Pipeline

## Overview
Industrial-scale automation pipeline for extracting procedures from 70+ YouTube channels and other sources using the Ralph Wiggum / Conductor pattern for iterative LLM-driven extraction.

## Steps

### Step 1: Acquire transcripts
For each source in queue, get clean text:

YOUTUBE VIDEOS:
1. Try YouTube Transcript API (manual captions preferred)
2. Fall back to Whisper transcription if needed
3. Store with timestamps for source location

PDF PAPERS:
1. Extract text with PyMuPDF or pdfplumber
2. Fall back to OCR for scanned documents
3. Preserve page numbers

PODCASTS/AUDIO:
1. Download audio
2. Transcribe with Whisper (medium model recommended)
3. Store with timestamps

TOOL DOCUMENTATION:
1. Scrape with requests + BeautifulSoup
2. Convert HTML to Markdown
3. Preserve structure

Output standardized format:
- source_type, source_id, source_metadata
- full_text, segments (with timestamps/pages)
- quality assessment (manual | auto | whisper | ocr)

### Step 2: Run extraction loop (Pass 1 - Explicit)
For each transcript, run iterative explicit extraction:

PROMPT TEMPLATE:
"Find ALL explicitly stated procedures. Look for:
 'Here's how to...', 'The steps are...', numbered lists,
 direct explanations of HOW to do something.
 Output in YAML format with name, type, confidence, steps, gaps."

ITERATION LOGIC (Ralph Wiggum Pattern):
1. Call LLM with transcript + prompt
2. Parse YAML procedures from response
3. Check for "EXTRACTION_STATUS: COMPLETE" signal
4. If not complete, loop with accumulated extractions as context
5. Stop when: complete signal, max 3 iterations, or diminishing returns

Mark all procedures with:
- type: explicit
- confidence: HIGH (verbatim quotes support it)
- source_location: timestamp or page

### Step 3: Run extraction loop (Pass 2 - Implicit)
Extract procedures hidden in behavior and examples:

PROMPT TEMPLATE:
"Find procedures NOT explicitly stated but inferred from:
 Pattern matching (every time X, they do Y)
 Consistent behaviors, unstated steps,
 Decision criteria, error handling.
 Output with observed_pattern, evidence, reconstructed_steps."

ITERATION LOGIC:
1. Include explicit extractions as context
2. Focus on what they DO vs what they SAY
3. Max 3 iterations
4. Require evidence from source for each inference

Mark all procedures with:
- type: implicit
- confidence: MEDIUM
- uncertainty: what's not sure
- validation_needed: how to verify

### Step 4: Run extraction loop (Pass 3 - Meta)
Extract HOW they think, learn, teach, and improve:

PROMPT TEMPLATE:
"Find META-PROCEDURES about:
 Learning (how they acquire knowledge)
 Teaching (how they explain things)
 Thinking (how they reason and decide)
 Improvement (how they get better)
 These are procedures about procedures."

FOCUS AREAS:
- How do they introduce complex topics?
- What examples do they choose and why?
- How do they handle potential objections?
- What mental models do they use?

Mark all procedures with:
- type: meta
- category: learning | teaching | thinking | improvement
- why_valuable: how this can be applied elsewhere

### Step 5: Run extraction loop (Pass 4 - Tacit)
Surface knowledge they have but don't state:

PROMPT TEMPLATE:
"Excavate TACIT KNOWLEDGE through:
 Assumption surfacing (what must be true?)
 Expert blind spot detection (what do they skip?)
 Failure mode inference (what could go wrong?)
 Context dependency mapping (when would this NOT work?)"

TECHNIQUES:
- "What would a beginner miss?"
- "What do they 'just know'?"
- "What warnings would an expert give?"

Mark all extractions with:
- type: tacit
- confidence: LOW (needs validation)
- what_is_assumed: the unstated knowledge
- if_missing_consequence: what goes wrong without it

### Step 6: Validate extractions
Run automated validation on all extractions:

STRUCTURAL CHECKS:
- YAML parses correctly
- Required fields present (name, type, steps)
- Steps are non-empty
- No placeholder text ([brackets], TODO)

SEMANTIC CHECKS:
- Name is descriptive (3+ words)
- Steps start with verbs (actionable)
- Source citations are valid

CONSISTENCY CHECKS:
- No exact duplicates within source
- HIGH confidence has verbatim quote
- Type matches extraction characteristics

CALCULATE CONFIDENCE:
- explicit_quote: present/partial/absent
- multiple_evidence: 3+/2/1/inference
- step_completeness: all clear/some gaps/major gaps
- source_clarity: directly stated/implied/inferred/speculation

Flag for human review if:
- Average confidence < MEDIUM
- >50% are tacit type
- >3 validation issues
- Contradictory procedures found

### Step 7: Deduplicate across sources
Prevent duplicate procedures across sources:

DETECTION METHODS:
1. Name similarity (fuzzy match, threshold 0.85)
2. Step similarity (longest common subsequence, threshold 0.80)
3. Embedding similarity (cosine distance, threshold 0.90)

RESOLUTION STRATEGIES:
- Exact duplicate: Keep first, discard duplicate
- Cross-source duplicate: Keep both, link as variants
- Similar but different: Keep both, create procedure family
- Enhanced version: Merge, keeping best parts

Document all deduplication decisions.

### Step 8: Create procedure files
Write GOSM-compatible YAML files:

PATH DETERMINATION:
- YouTube: library/procedures/extracted/youtube/{channel}/{procedure}.yaml
- Papers: library/procedures/extracted/papers/{author}_{year}/{procedure}.yaml
- Books: library/procedures/extracted/books/{author}/{procedure}.yaml
- Tools: library/procedures/extracted/tools/{tool}/{procedure}.yaml

FILE CONTENT:
- id, name, version, domain, description
- source (origin, type, creator, url, location, extraction_date, confidence)
- when_to_use, when_not_to_use
- inputs, outputs
- steps (with action, details, reasoning)
- verification, failure_modes
- notes (extraction metadata, gaps, confidence)

Validate YAML syntax before writing.

### Step 9: Update indexes
Keep library indexes current:

INDEXES TO UPDATE:
1. library/procedures/extracted/EXTRACTED_PROCEDURES_INDEX.md
   - Total procedures by source type
   - Recent additions
   - Domain groupings

2. library/procedures/extracted/EXTRACTION_LOG.md
   - Date, source, creator
   - Procedures extracted by type
   - Time, tokens, cost

3. Source-specific indexes
   - library/procedures/extracted/youtube/{channel}/INDEX.md
   - Videos processed, procedures by video

Include in log:
- Source metadata
- Extraction statistics
- Files created
- Cost breakdown

### Step 10: Generate extraction report
Create comprehensive report of extraction run:

SUMMARY:
- Sources processed / failed
- Procedures extracted (by type: explicit/implicit/meta/tacit)
- Procedures flagged for review
- Time elapsed
- Tokens used
- Cost incurred

BY SOURCE:
- Each source with procedures extracted
- Confidence distribution
- Notable findings

QUALITY METRICS:
- Validation pass rate
- Confidence distribution
- Deduplication rate

RECOMMENDATIONS:
- Sources worth re-processing
- Prompt improvements needed
- Budget projections for remaining queue

Save report to output_directory/EXTRACTION_REPORT.md


## When to Use
- When processing more than 10 sources at once
- When building initial procedure library at scale
- When systematically processing a YouTube channel backlog
- When you have approved budget for automated extraction
- When sources have been prioritized and queued
- When rapid library expansion is needed
- After completing pilot extraction to validate prompts
- When diminishing returns on manual extraction

## Verification
- All queued sources processed or documented as failed
- Each pass ran to convergence for each source
- Validation checks ran on all extractions
- Duplicates identified and resolved
- Procedure files are valid YAML
- Indexes updated with all new procedures
- Cost stayed within budget
- Extraction report is accurate and complete

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.