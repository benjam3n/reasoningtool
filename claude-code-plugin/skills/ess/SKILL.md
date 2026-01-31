---
name: "ess - External Source Search"
description: "Systematic procedure for searching external sources to find evidence, data, and information relevant to a question."
---

# External Source Search

**Input**: $ARGUMENTS

---

## Overview

Structured approach to finding information from external sources. Defines what you're looking for, selects appropriate source types, executes a systematic search, evaluates what you find, and synthesizes results. Prevents both insufficient searching and unfocused browsing.

## Steps

### Step 1: Define the Search
1. What specific question are you trying to answer?
2. What kind of evidence would answer it? (data, studies, expert opinion, examples, documentation)
3. What would a satisfying answer look like?
4. What's the quality threshold? (rigorous research vs quick orientation)
5. Time budget: how long is this search worth?

### Step 2: Select Source Types
Choose based on what you need:

| Need | Source Types |
|------|------------|
| Scientific evidence | Academic databases, journals, preprints |
| Current events/trends | News, industry publications, social media |
| Technical documentation | Official docs, wikis, Stack Overflow, GitHub |
| Market/business data | Industry reports, financial databases, company filings |
| Expert opinion | Books, talks, interviews, podcasts |
| Historical precedent | Archives, case studies, historical databases |
| Public data | Government databases, census, open data portals |

### Step 3: Construct Search Queries
1. Primary query: key terms from the question
2. Synonyms and related terms
3. Boolean operators where supported (AND, OR, NOT)
4. Domain-specific terminology
5. Plan 3-5 query variations to cast a wide net

### Step 4: Execute Search
1. Search each source type with each query variation
2. For each result, record:
   - Source (where found)
   - Key claim or data point
   - Relevance to original question (high/medium/low)
   - Quality signal (peer-reviewed, reputable, unknown)
3. Stop when: finding repetition (same info from multiple sources) OR time budget exhausted

### Step 5: Evaluate Sources
For each relevant source:
1. **Credibility**: Who produced this? What's their expertise? Conflicts of interest?
2. **Methodology**: How was this information generated?
3. **Recency**: When was this produced? Still current?
4. **Corroboration**: Do other sources agree?
5. Assign tier: A (high quality) / B (moderate) / C (low) / D (unreliable)
   → INVOKE: /src [source] for deep credibility evaluation if needed

### Step 6: Synthesize
1. What do the sources collectively say?
2. Where do they agree? Disagree?
3. What's the answer to the original question based on what was found?
4. What's the confidence level? (depends on source quality and agreement)
5. What wasn't found? (gaps in the search)

```
SEARCH RESULTS:
Question: [original question]
Sources searched: [N types, N queries]
Results: [N sources found, N relevant]

Key findings:
1. [finding] — Source: [ref] — Quality: [tier]
2. [finding] — Source: [ref] — Quality: [tier]

Answer: [synthesis]
Confidence: [high/medium/low]
Gaps: [what wasn't found]
```

## When to Use
- Any question requiring external information
- Fact-checking claims
- Research for decisions or plans
- Finding precedents or examples

## Verification
- [ ] Search question defined precisely
- [ ] Multiple source types considered
- [ ] Multiple query variations used
- [ ] Sources evaluated for credibility
- [ ] Findings synthesized (not just listed)
- [ ] Gaps acknowledged
