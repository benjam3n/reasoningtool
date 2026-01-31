---
name: "dop - Documentation Procedures"
description: "Create comprehensive project documentation that allows others to understand, reproduce, and maintain the project."
---

# Documentation Procedures

**Input**: $ARGUMENTS

---

## Overview

Good documentation lets someone else (or future you) understand what was built, why, and how to work with it. This procedure identifies what documentation is needed, creates it at the right level, and establishes maintenance.

## Steps

### Step 1: Identify Documentation Needs
- **Why** (context): Why does this project exist? What problem does it solve?
- **What** (architecture): What are the components and how do they fit together?
- **How** (usage): How do you use it? Install, configure, run.
- **How** (development): How do you modify it? Build, test, deploy.
- **Reference**: API docs, configuration options, data formats.

### Step 2: Choose Documentation Types
| Audience | Type | Format |
|----------|------|--------|
| New users | Getting started / tutorial | Step-by-step guide |
| Existing users | How-to guides | Task-oriented recipes |
| Developers | Architecture / design docs | Diagrams + explanations |
| Everyone | README | Overview + quick start |
| API consumers | API reference | Generated or manual spec |

### Step 3: Write Each Document
For each document:
1. Start with what the reader needs to DO (not what you want to explain)
2. Shortest path to working — minimal viable instructions first
3. Code examples > descriptions
4. Keep it current — outdated docs are worse than no docs

### Step 4: Establish Maintenance
1. Link docs to the code they describe (proximity)
2. Review docs when code changes (make it part of PR process)
3. Date-stamp documents
4. Delete outdated docs rather than leaving them

## When to Use
- Starting a project, onboarding new people, releasing software
- When someone asks "how does this work?" more than once

## Verification
- [ ] README exists with purpose and quick start
- [ ] Key decisions documented (architecture, design rationale)
- [ ] Usage instructions tested by someone who didn't write them
- [ ] Maintenance process defined
