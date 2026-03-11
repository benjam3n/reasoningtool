# /col How should I collaborate with early users to improve the toolkit?
**Date:** 2026-03-09
**Skill:** /col (Collaboration)

---

## Step 1: Define the Goal

```
GOAL: Incorporate early user feedback to improve the reasoning toolkit without losing architectural coherence.
TIMELINE: Ongoing from first user onward; critical first 6 months.
CONSTRAINTS: Solo developer (you), open-source project, 592 skills already built,
             users are unpaid volunteers, no formal org structure,
             asynchronous-first (global open-source audience).
SUCCESS LOOKS LIKE: A feedback loop where users surface real problems, you triage
                    and act on the highest-signal ones, and the toolkit gets
                    meaningfully better — without devolving into design-by-committee.
```

---

## Step 2: Map Roles

Since this is a solo-developer + community situation, a full RACI matrix is overkill. Here's the practical split:

```
ROLES:
| Role            | Responsible For                        | Decision Rights                          | Key Deliverable                          |
|-----------------|----------------------------------------|------------------------------------------|------------------------------------------|
| You (maintainer)| Architecture, skill quality, merging   | ALL final decisions on what ships         | Reviewed skills, releases, roadmap        |
| Early adopters  | Using skills on real problems, reporting| Can propose anything; decide nothing alone | Bug reports, confusion reports, use cases |
| Power users     | Deep usage, pattern-finding, evangelism | Can draft PRs, suggest skill designs      | PRs, skill proposals, community answers   |
| Contributors    | Writing/improving specific skills      | Own their PR until you review it          | Skill drafts, improvements, test cases    |
```

**Key principle:** You retain all architectural authority. Users have unlimited voice, zero veto. This is non-negotiable for coherence at 592 skills.

---

## Step 3: Communication Design

```
COMMUNICATION CADENCE:
| Type                    | Frequency       | Who                    | Format   | Purpose                                       |
|-------------------------|-----------------|------------------------|----------|-----------------------------------------------|
| GitHub Issues           | Always open     | Anyone                 | Async    | Bug reports, confusion, feature requests        |
| GitHub Discussions      | Always open     | Anyone                 | Async    | Open-ended "how should X work" conversations    |
| Changelog / release log | Per release     | You -> everyone        | Async    | What changed and why                            |
| "What I'm working on"  | Weekly/biweekly | You -> early adopters  | Async    | Maintain trust, show responsiveness             |
| Direct feedback invite  | Monthly         | You -> top 5 users     | Async DM | Targeted questions about specific pain points   |
| PR review               | As submitted    | You <-> contributor    | Async    | Quality gate for contributed skills             |

DEFAULT CHANNEL: GitHub Issues + Discussions (everything public, searchable, archival).
ESCALATION PATH: If a user feels unheard, they can tag you directly in an issue.
                 No further escalation — you are the only decision-maker.
```

**Rule applied:** Every touchpoint has a purpose. No standing meetings. No Discord server yet — that's premature community-building before you have community.

---

## Step 4: Decision Rights

```
DECISION MAP:
| Decision Type                         | Who Decides | Who Must Be Consulted  | Tiebreaker |
|---------------------------------------|-------------|------------------------|------------|
| Add a new skill                       | You         | Nobody (but listen)     | You        |
| Remove or merge a skill               | You         | Users who filed issues  | You        |
| Change skill format/structure         | You         | Active contributors     | You        |
| Change routing architecture           | You         | Nobody                  | You        |
| Accept a contributed skill PR         | You         | PR author               | You        |
| Reject a contributed skill PR         | You         | PR author (explain why) | You        |
| Prioritize what to work on next       | You         | Top users (signal only) | You        |
| Naming conventions                    | You         | Nobody                  | You        |

DEFAULT RULE: If a decision isn't listed, you decide. Period.
```

**Why this is so centralized:** The toolkit's value is coherence across 592 skills. One bad merge can break conceptual integrity. Users contribute signal; you contribute judgment. This is the Linux kernel model, not the Wikipedia model.

---

## Step 5: Handoff Procedures

There are three handoffs that matter:

```
HANDOFFS:

1. USER -> YOU: Feedback / bug report
   - FORMAT: GitHub Issue using a template you provide (categories:
     "Skill didn't help", "Skill was confusing", "Skill is missing", "Routing sent me wrong place")
   - DEFINITION OF DONE: User has described the problem with enough context to reproduce
   - ACCEPTANCE: You label the issue (acknowledged, needs-info, wontfix, planned)
   - SLA: Acknowledge within 72 hours. No promise on resolution timeline.

2. CONTRIBUTOR -> YOU: Skill PR
   - FORMAT: Pull request with the skill file + a "test case" (an example input and expected output)
   - DEFINITION OF DONE: Skill follows your format, passes your quality bar,
     includes at least one worked example
   - ACCEPTANCE: You review, request changes or merge.
     Rejection is always explained with a reason.
   - RULE: You may rewrite substantially before merging.
     Contributor gets credit but not ownership of final form.

3. YOU -> USERS: Decisions and changes
   - FORMAT: Changelog entry or issue comment explaining what you did and why
   - DEFINITION OF DONE: Every non-trivial change has a one-sentence rationale visible to users
   - ACCEPTANCE: Implicit — users can respond if they disagree, but the change ships.
```

---

## Step 6: Accountability

```
ACCOUNTABILITY:
- CHECK-IN CADENCE: Monthly self-review — "Is feedback actually changing what I build?"
- LEADING INDICATOR:
    (Healthy) Users file specific, actionable issues about real usage.
    (Healthy) You close issues with commits, not just words.
    (Unhealthy) Users stop filing issues.
    (Unhealthy) You have 30+ open issues you haven't triaged.
- FAILURE SIGNAL:
    1. Feature requests outnumber confusion/bug reports 10:1
       (users are designing, not using)
    2. You start avoiding the issue tracker
       (feedback feels like noise, not signal)
    3. Contributors submit PRs that don't match your format
       (you haven't documented standards clearly enough)
- ADJUSTMENT RULE:
    If signal-to-noise drops, tighten the issue template.
    If contributions keep missing the bar, write a CONTRIBUTING.md with examples.
    If no one is contributing, the tool isn't valuable enough yet — go back to solo building.
```

---

## Practical Playbook: First 10 Users

Here's what this looks like concretely:

### Phase 0: Before any users arrive
1. **Create issue templates** with four categories: "Skill didn't help," "Skill was confusing," "Missing skill," "Wrong routing."
2. **Write a short CONTRIBUTING.md** explaining: skill format, quality bar, how PRs are reviewed, your right to rewrite.
3. **Pick 5 skills you're most confident in.** These are your "starter pack" — point first users here, not at 592 skills.

### Phase 1: First 1-5 users
4. **Ask them to use specific skills on real problems** and tell you what happened. Don't ask "what do you think?" — ask "did it help you reach a decision/answer?"
5. **Watch for confusion, not preferences.** If someone can't figure out what a skill does, that's a bug. If someone wishes a skill worked differently, that's an opinion. Fix bugs; file opinions.
6. **Respond to every issue personally.** At this scale, each user matters enormously.

### Phase 2: 5-20 users
7. **Identify your 2-3 power users** (the ones who use it repeatedly, not just once). Give them direct access to you — DM, email, whatever. Their feedback is 10x more valuable than drive-by opinions.
8. **Start tracking which skills get used** and which get ignored. Ignored skills are either undiscoverable or not useful. Both are your problem.
9. **Accept your first contributed PR** if one comes. Even if you rewrite it substantially, the act of accepting contributions sets the tone.

### Phase 3: 20+ users
10. **Stop responding to every issue personally.** Use labels and templates. Batch triage weekly.
11. **Publish a simple roadmap** ("here's what I'm working on next") so users can see their feedback landing.
12. **Say no publicly.** When you reject a suggestion, explain why in the issue. This teaches the community your design values.

---

## The Core Tension (and How to Manage It)

The fundamental tension is: **users want the toolkit to serve their specific needs; you need the toolkit to stay coherent across 592 skills.**

Manage it with one rule: **Users own the problems. You own the solutions.**

- When a user says "this skill didn't help me figure out X" — that's a problem you should take seriously.
- When a user says "this skill should work like Y instead" — that's a proposed solution you should listen to but not necessarily adopt.
- When a user says "you should add a skill for Z" — that's a signal about a gap, not a spec for a skill.

Every piece of feedback gets decomposed: **What's the underlying problem?** Then you decide the solution within your architecture.

---

## Integration

- `/conr` — If a contributor conflict arises (rejected PR, disagreement on direction)
- `/to` — To break down the "prepare for first users" work into ordered tasks
- `/pri` — When you have 20 open issues and need to decide what to work on next
- `/de` — If you decide to build a formal contributor program later
