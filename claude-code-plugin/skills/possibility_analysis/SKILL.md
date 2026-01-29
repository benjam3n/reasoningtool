---
name: possibility_analysis
description: "Systematically explore the possibility space of what could be done."
---

# Possibility Analysis

## Overview
Systematically explore the possibility space of what could be done.
Counterpart to limitation_analysis - limitations ask "what can't we do?"
while possibilities ask "what COULD we do?"

Key insight: We often under-explore possibility space because we
anchor on current usage. This procedure forces broad enumeration
before filtering.

## Core Principle
1. Enumerate possibilities WITHOUT filtering (defer judgment)
2. Categorize by type (what kind of possibility)
3. Assess value (what would we gain)
4. Assess feasibility (what would it take)
5. Apply effort/impact gate to prioritize
6. Identify ADJACENT possibilities (small extensions of current)
7. Identify TRANSFORMATIVE possibilities (fundamental changes)

## Steps

### Step 1: Define scope
Clearly state what system/resource/situation you're analyzing.
Include: current purpose, current capabilities, current usage.

### Step 2: Enumerate possibilities freely
Use exploration_prompts to generate possibilities.
NO FILTERING - write down everything, even if it seems:
  - Obvious (still worth noting)
  - Impossible (might inspire adjacent ideas)
  - Stupid (might not be)
  - Already considered (document it anyway)

Aim for QUANTITY first. 20+ possibilities minimum.

### Step 3: Categorize each possibility
For each possibility, assign a category from possibility_categories.
Mark whether it's:
  - ADJACENT: One step from current (high feasibility)
  - DISTAL: Multiple steps away (lower feasibility, higher potential)

### Step 4: Assess value of each
Rate potential value: TRANSFORMATIVE / HIGH / MEDIUM / LOW / NEGLIGIBLE

TRANSFORMATIVE: Changes the game entirely
HIGH: Significant new capability or major improvement
MEDIUM: Useful improvement, noticeable difference
LOW: Minor improvement
NEGLIGIBLE: Not worth the effort

### Step 5: Assess feasibility of each
Rate feasibility: TRIVIAL / EASY / MODERATE / HARD / BREAKTHROUGH

TRIVIAL: < 1 hour, obvious how to do it
EASY: < 1 day, clear path
MODERATE: Days to weeks, some unknowns
HARD: Weeks to months, significant challenges
BREAKTHROUGH: Requires fundamental advance we don't have

### Step 6: Apply value/feasibility prioritization
Create priority matrix:

DO FIRST:   EASY/TRIVIAL feasibility + HIGH/TRANSFORMATIVE value
DO SECOND:  MODERATE feasibility + HIGH/TRANSFORMATIVE value
EXPLORE:    HARD feasibility + TRANSFORMATIVE value (worth investigating)
MAYBE:      EASY feasibility + MEDIUM/LOW value
DEFER:      HARD feasibility + MEDIUM/LOW value
MOONSHOT:   BREAKTHROUGH + TRANSFORMATIVE (track but don't invest yet)

### Step 7: Identify the ONE thing
From DO FIRST, identify the single highest-leverage possibility.
Ask: "If we could only do ONE new thing, what would it be?"

### Step 8: Map dependencies
For top possibilities, identify:
  - What must be true first (prerequisites)
  - What this enables next (unlocks)
  - What this conflicts with (tradeoffs)

### Step 9: Create exploration plan
For EXPLORE items (hard but potentially transformative):
  - What's the cheapest experiment to test feasibility?
  - What would we need to learn first?
  - What's the smallest version we could try?


---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.