---
name: "statous - Status Resume"
description: Scans recent work context (git history, uncommitted changes, memory, open branches) to summarize what was in progress and help you figure out what to pick back up.
output:
  format: "prose"
---

# Statous

**Input**: $ARGUMENTS

---

## Step 1: Gather Signals

Collect everything that tells you what was recently happening. Run these in parallel:

1. **Git log** — last 15-20 commits across all branches (`git log --all --oneline -20 --date=relative --format="%h %ar %s"`)
2. **Uncommitted changes** — `git status` and `git diff --stat` (unstaged + staged)
3. **Recent branches** — `git branch --sort=-committerdate` (top 5-10)
4. **Memory files** — scan the memory directory for project memories that mention ongoing work
5. **Stashes** — `git stash list` for parked work

Rule: Cast a wide net. Don't filter yet.

---

## Step 2: Identify Threads

Group what you found into distinct **threads of work** — separate efforts that were happening.

```
ACTIVE THREADS:

1. [Thread name]
   - Last activity: [when]
   - What was happening: [1-2 sentences]
   - State: [in progress / paused / blocked / nearly done]
   - Evidence: [commits, branches, uncommitted files]

2. [Thread name]
   ...
```

Rule: A "thread" is a coherent line of work, not individual commits. Group related commits together.

SKIP: If there's only one thread, just describe it directly.

---

## Step 3: Assess Resumability

For each thread, evaluate how easy it is to pick back up.

```
RESUMABILITY:

| Thread | State | Complexity to Resume | Next Step |
|--------|-------|---------------------|-----------|
| [name] | [state] | [easy/medium/hard] | [concrete next action] |
```

- **Easy**: Clear next step, no blockers, context is fresh
- **Medium**: Needs some re-reading or context rebuild
- **Hard**: Stale, blocked, or requires significant ramp-up

---

## Step 4: Surface Danglers

Flag anything that looks unfinished, forgotten, or at risk:

```
DANGLERS:
- [thing that looks abandoned or forgotten]
- [uncommitted work that might get lost]
- [branch that diverged significantly]
- [stashed work that's been sitting]
```

SKIP: If nothing looks dangling, skip this.

---

## Step 5: Recommend

Based on what you found, suggest what to do next.

```
RECOMMENDED RESUME ORDER:

1. [Thread] — [why this first: urgency, momentum, ease, etc.]
2. [Thread] — [why next]
3. [Thread] — [if applicable]

IMMEDIATE ACTION: [the single most concrete thing to do right now]
```

Rule: Lead with the thread that has the most momentum or urgency. Don't default to chronological order.

---

## Step 6: One-Line Summary

```
STATUS: [one sentence capturing where things stand overall]
```

This should be useful even if the user reads nothing else.

---

## Integration

Use with:
- `/ornt` -> If you need to orient on a specific thread in more detail
- `/ata` -> To turn the resume plan into actionable tasks
- `/pri` -> To prioritize across threads if there are many
- `/to` -> To plan out a specific thread's next steps
