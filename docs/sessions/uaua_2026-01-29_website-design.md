---
date: 2026-01-29 16:10
topic: Website design and architecture for reasoningtool.com - derive design principles from first principles, redesign, sophisticated architecture
depth: 16x
claims: 38
crux_points: 12
status: FOUNDATIONAL
---

# UAUA 16x: Website Design & Architecture for reasoningtool.com

## FINAL DESIGN SPECIFICATION

### Visual Direction
Editorial -- serious, literate, warm. Not startup, not developer-niche, not academic.

### Typography
- Headings + UI: Inter (loaded as web font) or system-ui fallback
- Body prose: Source Serif 4 (loaded as web font) -- editorial, screen-optimized
- Code: JetBrains Mono or system monospace
- Scale: Major Third (1.25x) -- 14 / 16-18 / 20 / 25 / 31 / 39
- Body: 18px, line-height 1.65
- Max prose width: 680px (~65 characters)

### Color
- Light mode: body #1a1a1a on background #faf9f6 (warm white)
- Dark mode: body #e8e6e3 on background #1a1a1e (warm dark)
- Accent: #3d5a80 (deep muted blue)
- Accent hover: #2b4570 (darker)
- Borders/separators: #e2e0dd (light) / #2a2a2e (dark)
- Code backgrounds: #f5f3f0 (light) / #232326 (dark)

### Spacing
8px grid -- 8/16/24/32/48/64/96/128

### Layouts
- ProseLayout: centered 680px column, serif body, margin TOC on desktop
- PageLayout: centered 960px column, sans body, for standard pages
- DocsLayout: 960px+ with optional sidebar
- CatalogLayout: full-width responsive grid

### Architecture
- Content collections for essays (MDX + frontmatter schema)
- Data-driven skills catalog from catalog.json
- ~8 reusable components: Card, EssayPreview, CodeBlock, Callout, TOC, SkillCard, Header, Footer
- 4 layout files
- Sitemap + Open Graph metadata
- Dark mode with system detection + toggle
- RSS feed for essays
- "Read next" at end of essays

### What NOT to include
- Decorative illustrations or icons
- Animations beyond basic hover transitions
- More than one accent color
- Client-side search (too few pages)
- Community features (premature)
- Reading progress indicator (decoration)
- Background gradients or patterns

## KEY INSIGHTS

1. From U1: The project's identity is "intellectual tool" -- not startup, not developer-niche. This rules out 80% of modern web design trends.
2. From A1: SaaS aesthetics create wrong expectations for an open-source philosophy project.
3. From U2: Sans headings + serif body is the key typographic decision. Signals "editorial" without "academic."
4. From A2: The accent color should be unremarkable. Deep muted blue.
5. From U3: Content collections + data-driven catalog = content as data, not code.
6. From U4: Eight principles derived from first principles (cognitive load, gestalt, reading research).
7. [NOVEL] Design philosophy should match writing philosophy. "No embellishment" in writing = "no decoration" in design.

## FIRST PRINCIPLES OF VISUAL DESIGN (Derived)

1. Visual hierarchy must match information hierarchy.
2. Consistency signals intentionality.
3. Whitespace is structural, not empty.
4. Fewer typefaces/sizes/colors = more clarity.
5. Alignment creates order.
6. Contrast controls attention.
7. Typography legibility has measurable properties (45-75 char lines, 1.5-1.7 line height, 16-20px body).
8. The design should be invisible -- reader notices ideas, not layout.

## FULL ANALYSIS

### U1: SPACE MAPPING

Input: The website looks terrible. Derive what looks good from first principles. Sophisticated architecture. No quirky software look.

25 candidates across: visual direction (5), architecture (5), typography (3), color (4), layout (4), content structure (4).

### A1: CANDIDATE TESTING

VALIDATED:
- Editorial direction (not academic -- editorial like The Atlantic)
- Hybrid architecture (different layouts per content type)
- Serif body text (screen-optimized, editorial)
- Warm white background (#faf9f6)
- Muted color palette (one accent)
- Content-specific layouts (prose vs catalog vs docs)
- Full-width with constrained content
- Essays prominent (marquee content)
- Progressive disclosure
- Problem-first landing page

REJECTED:
- Modern tool look (SaaS expectations, blends in with AI startups)
- Developer-focused primary (buries essays, narrows audience)
- Knowledge platform (over-scoped, implies community that doesn't exist)
- Blog-style (content isn't chronological)
- Wiki (over-engineered for 9 pages)
- Dark mode primary (controversial for long-form reading)
- High contrast B&W (too harsh for warm voice)

### U2: EDGE CASE DISCOVERY

18 edge cases found. Key ones:
- Mobile serif rendering -- manageable with screen-optimized fonts at 18px+
- Navigation confusion in hybrid layouts -- solved by shared header/footer
- Dark mode palette needs its own considered design (warm dark, not pure black)
- Code blocks need editorial treatment (light themed, subtle background)

6 novel insights:
- Sans headings + serif body = editorial standard
- Accent color derived from content identity (blue = trust/depth/intelligence)
- Homepage needs completely different layout from essays
- Code blocks should feel like deliberate inserts, not mode switches
- Getting Started should read like a tutorial, not a README
- Skills catalog needs card-based layout with category grouping

### A2: FINAL VALIDATION

All edge cases manageable. 7 final validated, 2 conditional, 0 rejected.

### U3: ARCHITECTURE DEEP DIVE

Candidates: content collections, data-driven catalog, component library, multiple layouts, MDX, SEO, dark mode, TOC, RSS, read-next navigation.

### A3: ARCHITECTURE TESTING

11 validated: content collections, data-driven catalog, component library (8 components), 4 layouts, MDX for essays, SEO (OG + sitemap), dark mode toggle, TOC for essays, RSS feed, read-next navigation.
2 rejected: client-side search (too few pages), reading progress indicator (decoration).

### U4: DESIGN FROM FIRST PRINCIPLES

8 principles derived. Specific rules produced:
- Max 2 design fonts + 1 functional (mono)
- Major Third type scale (1.25x ratio)
- 8px spacing grid
- One accent color
- No decoration that doesn't serve information hierarchy

### A4: FINAL SPECIFICATION

Validated specific values:
- Inter for headings/UI, Source Serif 4 for prose body
- #3d5a80 accent (contrast ratio ~7:1 on warm white, WCAG AAA)
- 18px body, line-height 1.65, max-width 680px
- 8px grid with 4px fine adjustments
