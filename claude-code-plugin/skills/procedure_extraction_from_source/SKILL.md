---
name: procedure_extraction_from_source
description: "Meta-procedure for extracting implicit procedures from ANY external source, turning tacit knowledge into explicit, reusable GOSM-compatible procedures."
---

# Procedure Extraction from Source

## Overview
Meta-procedure for extracting implicit procedures from ANY external source, turning tacit knowledge into explicit, reusable GOSM-compatible procedures.

## Steps

### Step 1: Surface scan
Quick pass to understand scope and structure:

1. Skim entire source (or sample if very long)
   - For videos: watch at 2x, note structure
   - For papers: read abstract, intro, conclusion
   - For books: read table of contents, chapter summaries

2. Note structure:
   - Chapters, sections, segments
   - How content is organized
   - Where "how to" content is concentrated

3. Identify main topics covered

4. Estimate procedure density:
   - High: mostly "how to" content
   - Medium: mix of explanation and procedure
   - Low: mostly "what is" content

Output: Source map with annotated sections

### Step 2: Creator analysis
Understand WHO created this and WHY it matters:

Questions to answer:
- What is this person known for?
- What unique perspective or access do they have?
- What can they do that others can't?
- What's their track record of results?
- Why should I trust their procedures?

Credibility signals:
- Verifiable achievements
- Peer recognition
- Students/followers with results
- Published/cited work
- Professional credentials

Warning signs:
- Only self-reported success
- No verifiable outcomes
- Contradicted by evidence

Output: Creator profile with credibility assessment

### Step 3: Identify procedure signals
Find markers that indicate procedures exist:

EXPLICIT SIGNALS (direct statements):
- "Here's how I do it..."
- "The steps are..."
- "First... then... finally..."
- "My process is..."
- "The framework I use..."
- Numbered lists
- Flowcharts or diagrams

IMPLICIT SIGNALS (patterns in behavior):
- Consistent patterns across examples
- Repeated decision points
- "I always..." or "I never..."
- Unstated assumptions that enable success
- What they do WITHOUT explaining why
- Transitions between states
- Error handling / edge cases mentioned

META SIGNALS (about their thinking):
- How they explain their own thinking
- How they teach others
- What they emphasize vs skip
- Where they slow down (important) vs speed up (obvious to them)

Create procedure signal map with locations in source.

### Step 4: Estimate extraction value
Decide if this source is worth deep extraction:

HIGH VALUE criteria:
- Unique procedures not found elsewhere
- Proven results from applying these procedures
- High procedure density
- Transferable to other domains
- Creator has exceptional track record

MEDIUM VALUE criteria:
- Good procedures but commonly known
- Some unique insights
- Moderate procedure density

LOW VALUE criteria:
- Mostly opinion, little procedure
- Procedures are obvious/common
- No evidence of results
- Very domain-specific, low transfer

Decision:
- HIGH: Proceed with full extraction
- MEDIUM: Extract selectively (explicit only)
- LOW: Skip or defer

Output: Value assessment with go/no-go decision

### Step 5: Extract explicit procedures
Extract procedures that are directly stated:

Process:
1. Find each explicit procedure signal
2. Copy the stated procedure verbatim
3. Note any gaps or ambiguities
4. Mark confidence as HIGH (they said it directly)

For each procedure found, capture:
- Name (descriptive)
- Source location (timestamp/page/section)
- Verbatim quote
- Steps as stated
- Gaps (what's missing or unclear)
- Notes (additional context)

Do NOT interpret or add - capture what's actually said.

### Step 6: Extract implicit procedures
Extract procedures hidden in behavior and examples:

Techniques:
1. Pattern Matching
   - "Every time X happens, they do Y"
   - "They always check Z before proceeding"
   - "The order is consistently A then B then C"

2. Counterfactual Analysis
   - "What would happen if they skipped this step?"
   - "Why this order and not another?"
   - "What constraint does this step satisfy?"

3. Gap Filling
   - "They jumped from A to C - what's B?"
   - "This assumes X - where did X come from?"
   - "They didn't explain why - what's the reason?"

For each implicit procedure, capture:
- Name (descriptive)
- Source location (where observed)
- Observed pattern (what you saw)
- Evidence (examples supporting the inference)
- Reconstructed steps
- Uncertainty (what you're not sure about)
- Confidence: MEDIUM

These require interpretation - be explicit about inferences.

### Step 7: Extract meta-procedures
Extract HOW they think, learn, teach, and improve:

LEARNING PROCEDURES:
- How do they acquire new knowledge?
- What sources do they use?
- How do they validate what they learn?
- How do they integrate new with existing?

TEACHING PROCEDURES:
- How do they structure explanations?
- What examples do they choose?
- How do they handle confusion?
- What do they emphasize?

THINKING PROCEDURES:
- How do they approach problems?
- What mental models do they use?
- How do they make decisions?

IMPROVEMENT PROCEDURES:
- How do they refine their methods?
- How do they handle failure?
- How do they incorporate feedback?
- How do they know when something is "good enough"?

Meta-procedures are often the most transferable.

### Step 8: Excavate tacit knowledge
Surface knowledge they have but don't state:

Techniques:
1. Assumption Surfacing
   - "What must be true for this to work?"
   - "What do they take for granted?"
   - "What would a beginner miss?"
   - "What 'obvious' thing isn't obvious?"

2. Expert Blind Spot Detection
   - "What do they skip because it's automatic?"
   - "Where do they use jargon without explaining?"
   - "What intermediate steps are missing?"
   - "What do they 'just know'?"

3. Failure Mode Inference
   - "What could go wrong that they don't mention?"
   - "What warnings would an expert give?"
   - "What mistakes did they probably make learning this?"

4. Context Dependency Mapping
   - "When would this NOT work?"
   - "What conditions are assumed?"
   - "What resources are assumed?"

Confidence: LOW for tacit knowledge (needs validation)

### Step 9: Formalize procedures
Convert raw extractions to GOSM format:

For each procedure, create structured YAML:
```yaml
name: [procedure_name]
version: "1.0"
source:
  origin: "[Source name]"
  creator: "[Who]"
  location: "[Where in source]"
  extraction_date: "[Date]"
  confidence: "[HIGH/MEDIUM/LOW]"

description: |
  [What this procedure does]

when_to_use:
  - [Trigger condition 1]
  - [Trigger condition 2]

inputs:
  [input_name]:
    description: "[What it is]"
    required: [true/false]

outputs:
  [output_name]:
    description: "[What it produces]"

steps:
  - id: 1
    name: "[Step name]"
    action: "[What to do]"
  - id: 2
    name: "[Step name]"
    action: "[What to do]"

verification:
  - "[How to know it worked]"

failure_modes:
  - mode: "[What can go wrong]"
    resolution: "[What to do]"

notes:
  - "[Additional context]"
  - "[Caveats]"
```

Fill gaps where possible, mark unknowns explicitly.

### Step 10: Assess completeness
Rate how complete and usable each procedure is:

COMPLETE:
- Could be used immediately by someone unfamiliar
- All steps explicit
- All inputs defined
- Verification clear
- Failure modes covered

USABLE:
- Could be used with some domain knowledge
- Core steps clear
- Some gaps but manageable
- Verification possible

PARTIAL:
- Needs more work before use
- Key steps identified
- Significant gaps remain
- Would need expert to fill in

SKETCH:
- Rough outline only
- General shape visible
- Most details missing
- Starting point for further extraction

Categorize each procedure and note what's needed to improve.

### Step 11: Validate extractions
Verify extraction quality:

1. Internal Consistency
   - Do steps follow logically?
   - Are inputs sufficient for outputs?
   - Are there circular dependencies?
   - Does verification actually verify?

2. Source Fidelity
   - Re-read source with procedure in hand
   - Does procedure match observed behavior?
   - Did we add anything not in source?
   - Did we miss anything important?

3. Usefulness Test
   - Read procedure cold - is it clear?
   - Simulate following it - do you get stuck?
   - Compare to existing procedures - is it better/different?
   - Would you use this yourself?

4. Uniqueness Check
   - Does similar procedure already exist in library?
   - If yes, is this better or just different?
   - What unique value does this add?

Decision: add / merge / enhance existing / skip

### Step 12: Integrate into library
Add validated procedures to GOSM library:

1. Create procedure file:
   Path: library/procedures/extracted/[source_type]/[source_name]/[procedure_name].yaml

2. Update indexes:
   - library/procedures/extracted/EXTRACTED_PROCEDURES_INDEX.md
   - Any domain-specific indexes

3. Cross-reference with related procedures:
   - Find similar procedures
   - Note relationships in both

4. Create extraction log entry:
   - Source name and type
   - Creator
   - Procedures extracted (count by type)
   - Time spent
   - Value assessment


## When to Use
- When encountering high-value content with extractable procedures
- When a source creator has unique knowledge or access
- When building procedure library from curated sources
- When wanting to learn from experts systematically
- When source has proven results worth capturing
- After prioritizing sources using source_prioritization procedure
- When noticed patterns in external content worth codifying
- When seeking to transfer knowledge from one domain to another

## Verification
- Source was assessed for value before deep extraction
- Explicit procedures have verbatim source quotes
- Implicit procedures have evidence from source
- Tacit knowledge is clearly marked as inference
- All procedures are in valid GOSM format
- Completeness ratings reflect actual usability
- Integration decisions are justified
- Extraction logged for future reference

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.