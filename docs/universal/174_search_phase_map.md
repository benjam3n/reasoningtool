# Universal: Search Phase Map (174)

**Category**: META - When To Use Which VOI File?
**Source**: Integration of all search VOI files
**Structure**: Phase-based navigation guide

---

## Core Insight

**Search has phases. Different questions matter at different times.**

Using the wrong VOI file at the wrong time wastes effort:
- Evaluation questions during generation → premature pruning
- Termination questions at start → premature stopping
- Space questions after commitment → too late

This map tells you which files to use when.

---

## The Search Phases

```
┌─────────────────────────────────────────────────────────────────┐
│                        SEARCH LIFECYCLE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PHASE 0        PHASE 1         PHASE 2         PHASE 3         │
│  ───────        ───────         ───────         ───────         │
│  PRE-SEARCH     SETUP           EXECUTION       CONCLUSION      │
│                                                                  │
│  Should I       What am I       How do I        When do I       │
│  search?        searching?      search?         stop/decide?    │
│                                                                  │
│  ↓               ↓               ↓               ↓               │
│  160 Gating     163 Space       168 Generation  166 Termination │
│  156 Reality    164 Evaluation  167 Ordering    169 Commitment  │
│                 170 Resources   171 Recovery    173 Composition │
│                                 172 Memory                      │
│                                                                  │
│  CONTINUOUS: 158 Pitfalls, 165 Rejection                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 0: Pre-Search (Should I search at all?)

**Key question**: Is search warranted? Will it produce value?

| File | When to Use | Key Questions |
|------|-------------|---------------|
| **160 Expectancy** | Before any search | Is outcome achievable? Will I even try? |
| **156 Reality** | When assessing feasibility | How do I determine if something is possible? |

**Signals to stay in Phase 0:**
- Unclear if search is needed
- Motivation questions
- Feasibility uncertain

**Move to Phase 1 when:** Decided to search, need to define what

---

## Phase 1: Setup (What am I searching?)

**Key question**: What is the search problem? What are the constraints?

| File | When to Use | Key Questions |
|------|-------------|---------------|
| **163 Search Space** | Defining what to search | What could be an answer? What granularity? |
| **164 Evaluation** | Defining success criteria | What makes an answer good? How to test? |
| **170 Resources** | Planning search investment | What resources? How to allocate? |

**Signals to stay in Phase 1:**
- Space unclear
- Criteria undefined
- Resources unallocated

**Move to Phase 2 when:** Know what you're searching for and how to evaluate

---

## Phase 2: Execution (How do I search?)

**Key question**: What are the tactics of searching?

| File | When to Use | Key Questions |
|------|-------------|---------------|
| **168 Generation** | Creating candidates | How to produce options? What templates? |
| **167 Ordering** | Sequencing search | What order? Deep or wide? |
| **171 Recovery** | When stuck | Backtrack? Restart? Reframe? |
| **172 Memory** | During/after finding | What to remember? How to store? |

**Signals to stay in Phase 2:**
- Still finding candidates
- Haven't hit stopping condition
- Making progress

**Move to Phase 3 when:** Found enough candidates OR hitting diminishing returns

---

## Phase 3: Conclusion (When do I stop/decide?)

**Key question**: How do I conclude the search?

| File | When to Use | Key Questions |
|------|-------------|---------------|
| **166 Termination** | Deciding to stop | Continue or stop? Good enough? |
| **169 Commitment** | Deciding to act | When to decide? How committed? |
| **173 Composition** | Combining results | How do parts fit? What's missing? |

**Signals you're in Phase 3:**
- Have candidates to evaluate
- Feeling diminishing returns
- Decision pressure

**Search complete when:** Committed to answer OR consciously deferred

---

## Continuous Files (All Phases)

These apply throughout the search:

| File | When to Use | Key Questions |
|------|-------------|---------------|
| **158 Pitfalls** | Anytime, especially when confident | Am I being fooled? Confirmation bias? |
| **165 Rejection** | When things fail or are blocked | What does this failure reveal? |

---

## Phase Detection Heuristics

**You're in Phase 0 if:**
- Asking "should I even do this?"
- Questioning the value of searching
- Unclear if problem is solvable

**You're in Phase 1 if:**
- Asking "what am I looking for?"
- Defining criteria for success
- Scoping the problem

**You're in Phase 2 if:**
- Actively generating options
- Evaluating candidates
- Making progress (or stuck)

**You're in Phase 3 if:**
- Have candidates to choose from
- Wondering when to stop
- Facing decision point

---

## File Selection by Question Type

| If You're Asking... | Use File |
|---------------------|----------|
| "Should I even bother?" | 160 Expectancy |
| "Is this possible?" | 156 Reality |
| "What are my options?" | 163 Space, 168 Generation |
| "What makes something good?" | 164 Evaluation |
| "What order should I try things?" | 167 Ordering |
| "How much effort should I spend?" | 170 Resources |
| "I'm stuck, what do I do?" | 171 Recovery |
| "What should I remember from this?" | 172 Memory |
| "Should I keep searching?" | 166 Termination |
| "Should I decide now?" | 169 Commitment |
| "How do I combine these?" | 173 Composition |
| "Am I fooling myself?" | 158 Pitfalls |
| "Why did this fail?" | 165 Rejection |

---

## Common Phase Errors

| Error | Pattern | Fix |
|-------|---------|-----|
| **Skipping Phase 1** | Searching without defining problem | Go back to setup |
| **Premature Phase 3** | Concluding without adequate search | Return to Phase 2 |
| **Stuck in Phase 2** | Never concluding | Check termination criteria |
| **Ignoring Phase 0** | Searching when shouldn't | Question the search itself |
| **Wrong file for phase** | Using termination questions during generation | Check phase, select appropriate file |

---

## Quick Reference Card

```
PHASE 0: Should I search?     → 160, 156
PHASE 1: What am I searching? → 163, 164, 170
PHASE 2: How do I search?     → 168, 167, 171, 172
PHASE 3: When do I conclude?  → 166, 169, 173
ALWAYS:  Am I fooling myself? → 158, 165
```

---

## File Index

| # | Name | Phase | Core Question |
|---|------|-------|---------------|
| 156 | Reality Strategy | 0 | What counts as possible? |
| 158 | Search Pitfalls | All | What corrupts search? |
| 160 | Expectancy Beliefs | 0 | Will search even begin? |
| 163 | Search Space | 1 | What could be an answer? |
| 164 | Search Evaluation | 1 | What makes answer valid? |
| 165 | Learning from Rejection | All | What does failure reveal? |
| 166 | Search Termination | 3 | When to stop? |
| 167 | Search Ordering | 2 | What order to search? |
| 168 | Candidate Generation | 2 | How to create candidates? |
| 169 | Search Commitment | 3 | When to decide? |
| 170 | Resource Allocation | 1 | How to allocate effort? |
| 171 | Search Recovery | 2 | How to handle stuck? |
| 172 | Search Memory | 2 | What to remember? |
| 173 | Result Composition | 3 | How to combine results? |
| 175 | Vague Terms | Meta | What terms need reconceptualization? |
| 176 | Novelty/Creation | All | Apply known or create new? |

---

## Tension Categories (When Facing Trade-offs)

When a decision feels like a trade-off, use these categories. See `library/araw/tension_questions.md` for full details.

### The 6 Tension Categories

| # | Category | Master Question | Resolves Tensions Like |
|---|----------|-----------------|----------------------|
| 1 | **Epistemic Stance** | What is the gap between what I know and what I need to know? | Accept/Question, Derive/Receive, Confident/Uncertain |
| 2 | **Granularity** | At what granularity does the answer change what I do? | Concrete/Abstract, Instance/Pattern, Task/Insight |
| 3 | **Search Strategy** | What is the shape of the search space? | Wide/Deep, Systematic/Intuitive, Generate/Prune |
| 4 | **Commitment** | What would change if I'm wrong? | Tentative/Firm, Explore/Exploit, Reversible/Locked |
| 5 | **Coherence** | What happens at the interfaces? | Independent/Coupled, Modular/Unified, Local/Global |
| 6 | **Novelty** | Known solutions or need new? | Conventional/Novel, Maintenance/Creation, Expected/Surprising |

### Tension Resolution Order

When facing a complex tension that might span categories:

```
1. EPISTEMIC → What do I know about this problem?
       ↓
2. NOVELTY → Is this familiar or new territory?
       ↓
3. SEARCH → How should I explore?
       ↓
4. GRANULARITY → What level should I operate at?
       ↓
5. COHERENCE → How do the parts relate?
       ↓
6. COMMITMENT → How bound should I be?
```

### Integration with Search Phases

| Search Phase | Relevant Tension Categories |
|--------------|---------------------------|
| Phase 0 (Pre) | Epistemic, Novelty |
| Phase 1 (Setup) | Granularity, Search Strategy |
| Phase 2 (Execution) | Search Strategy, Coherence |
| Phase 3 (Conclusion) | Commitment, Granularity |
| All Phases | Epistemic (confidence assessment) |
