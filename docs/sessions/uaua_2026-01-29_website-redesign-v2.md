---
date: 2026-01-29 16:45
topic: Website redesign v2 — what's actually wrong and what to do
depth: 16x
claims: 25
crux_points: 8
status: MIXED
---

# UAUA 16x: Website Redesign v2

## Summary

Framework is not the problem. CSS tooling is not the problem. The design DECISIONS are:
- Accent color too desaturated (#3d5a80 → #2563eb)
- Section spacing too tight (48-64px → 108px)
- Hero padding inverted (too much top, not enough between sections)
- Borders too visible (solid → rgba 8% opacity)
- Cards flat (border → shadow + hover lift)
- No individual skill pages (9 pages → 200+)
- "Essays" sounds academic → rename to "Foundations"
- No visual texture (flat → opacity borders, shadows, one gradient)

## P0: Individual Skill Pages
- Content collection from claude-code-plugin/skills/*/SKILL.md
- Dynamic routes at /skills/[name]
- Selective rendering: overview, steps, examples, when to use
- Strip internal patterns ($ARGUMENTS, [T:result], etc.)

## P1: CSS Fixes
- Accent: #2563eb (Tailwind blue-600)
- Section spacing: 6rem (108px), 3rem on mobile
- Hero: 3rem top padding, remove uppercase label
- Borders: rgba(0,0,0,0.08)
- Cards: shadow-based, hover lift
- Rename Essays → Foundations

## Rejected
- Tailwind migration (not the problem)
- Framework switch (HTML is HTML)
- Starlight (wrong format)
- Dark mode default (stylistic, not quality)
- Typography change (Inter is fine)

## Key Insight
The difference between "minimal" and "empty" is texture. Professional minimal sites use opacity, shadow, and subtle pattern. Current site has none.
