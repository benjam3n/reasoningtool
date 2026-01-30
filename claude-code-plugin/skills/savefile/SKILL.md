---
name: savefile
description: Save the output from the most recent skill invocation to the appropriate library folder. Only saves when explicitly requested.
---

# Save File

Save the output from the most recent skill invocation to a file.

## What to Save

For analytical skills (`/ar`, `/aw`, `/araw`, `/uaua`, `/u`, `/p`): save **only the Claim/Finding Registry and Synthesis**. Skip Phase 1 (Exploration). The registry captures every numbered item; the synthesis derives conclusions from them. Phase 1's derivation trees are redundant with the registry.

For all other skills: save the complete output.

## Process

1. **Identify what to save**: Look back at the conversation for the most recent skill output. For analytical skills, extract only the registry and synthesis sections.

2. **Determine the file path**: Based on the skill that produced the output:

   | Skill Type | Save Path |
   |-----------|-----------|
   | `/u`, `/ar`, `/aw`, `/araw`, `/uaua` | `library/araw/sessions/{skill}_{date}_{topic-slug}.md` |
   | `/p` | `library/araw/sessions/p_{date}_{topic-slug}.md` |
   | `/generate`, `/design`, `/critique` | `library/araw/sessions/{skill}_{date}_{topic-slug}.md` |
   | `/unexpected` | `library/araw/sessions/unexpected_{date}_{topic-slug}.md` |
   | `/gosm`, `/procedure_engine` | `library/gosm/sessions/gosm_{date}_{topic-slug}.md` |
   | Other skills | `library/sessions/{skill}_{date}_{topic-slug}.md` |

   - `{date}` = YYYY-MM-DD
   - `{topic-slug}` = short kebab-case summary of the topic (e.g., "universal-design-principles", "skill-improvement")

3. **Format the file**: Add a header with metadata, then the saved content:

   ```
   # {Skill Name} — {Topic}

   **Date**: {date}
   **Depth**: {depth if applicable}
   **Input**: {what the user asked}

   ---

   {registry + synthesis for analytical skills, or full output for others}
   ```

4. **Create directories** if they don't exist.

5. **Confirm**: Tell the user the file path.

## Arguments

If the user provides arguments after `/savefile`, use them:
- A path → save to that specific path
- A topic name → use as the topic slug
- Nothing → auto-detect from the skill output

## Important

- This skill exists so that OTHER skills don't need to auto-save. Skills should focus on their job, not file management.
- Only save when the user explicitly invokes `/savefile`.
- Never overwrite an existing file — append a number if the filename already exists.
