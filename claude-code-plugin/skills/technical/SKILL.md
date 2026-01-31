---
name: "technical - Domain-Specific Routing"
description: Sub-orchestrator for domain-specific questions. Routes to specialized skills based on domain and task type.
---

# Technical

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. What Domain?

| Domain | Skills available |
|--------|-----------------|
| **Software** | /dbg, /cor, /rf, /dsn, /ap, /apid, /ts, /sep |
| **Business** | /cd, /mf, /pos, /neg, /clr, /fm, /bm, /ivs, /roa |
| **Marketing** | /sms, /seb, /vm, /vdp, /cts, /orc |
| **Finance** | /b, /cfm, /ff, /fua, /gw, /isd |
| **Career** | /cpp, /ip, /rmo, /sn, /ska, /dlp |
| **Research** | /lr, /qr, /dc, /sta, /exd, /fia, /src |
| **Planning** | /pji, /de, /pjc, /op, /pt, /ria, /dpl |
| **Writing** | /w, /pw, /stl, /pus, /prd, /cts |
| **Learning** | /ska, /dlp, /spr, /acr, /lrs, /am |

If domain is unclear, ask: "What field is this in?"

### 2. What Task Type?

| Task | Pattern |
|------|---------|
| **Build/create** | use domain creation skills |
| **Fix/debug** | use domain diagnostic skills → or /diagnose |
| **Evaluate/review** | use domain evaluation skills → or /evaluate |
| **Plan** | use domain planning skills → or /how |
| **Research** | use domain research skills → or /search |
| **Decide** | → /decide with domain context |

### 3. Is This Too General for a Domain Skill?

- **Specific** ("Review this API design"): invoke /apid directly.
- **Broad** ("Help with my startup"): needs /want or /search first, then domain skills after goal is clear.
- **Cross-domain** ("Should I pivot from B2C to B2B?"): use /decide, with domain skills providing evidence.

---

## Execute

Route to the most specific applicable skill based on domain × task type.

If the input is broad, route to a category skill first (/want, /search, /how), then come back to /technical with a more specific question.

---

## After Completion

Report:
- Domain identified
- Skill(s) invoked
- Results
- Recommended follow-up (if any)
