#!/usr/bin/env python3
"""Add output frontmatter field to all skills that don't have one.

Default output format is 'prose' since that's what most skills produce.
Skills that produce structured output should be manually updated afterward.
"""

import os
import re
import sys

SKILLS_DIR = os.path.join(os.path.dirname(__file__), '..', 'claude-code-plugin', 'skills')

# Skills that should have non-prose output formats (update these manually or here)
STRUCTURED_SKILLS = {
    'qrx': None,  # already has output field
}

def process_skill(skill_dir):
    skill_md = os.path.join(skill_dir, 'SKILL.md')
    if not os.path.isfile(skill_md):
        return None

    with open(skill_md, 'r') as f:
        content = f.read()

    # Check if it already has an output field
    if re.search(r'^output:', content, re.MULTILINE):
        return 'skip'

    # Find the frontmatter boundaries
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return 'no-frontmatter'

    frontmatter = match.group(1)
    rest = content[match.end():]

    # Add output field at end of frontmatter
    new_frontmatter = frontmatter.rstrip() + '\noutput:\n  format: "prose"'

    new_content = f'---\n{new_frontmatter}\n---{rest}'

    with open(skill_md, 'w') as f:
        f.write(new_content)

    return 'updated'

def main():
    updated = 0
    skipped = 0
    no_fm = 0
    errors = 0

    for name in sorted(os.listdir(SKILLS_DIR)):
        skill_dir = os.path.join(SKILLS_DIR, name)
        if not os.path.isdir(skill_dir):
            continue

        result = process_skill(skill_dir)
        if result == 'updated':
            updated += 1
        elif result == 'skip':
            skipped += 1
        elif result == 'no-frontmatter':
            no_fm += 1
            print(f'  NO FRONTMATTER: {name}')
        elif result is None:
            errors += 1

    print(f'\nDone: {updated} updated, {skipped} already had output, {no_fm} no frontmatter, {errors} missing SKILL.md')

if __name__ == '__main__':
    main()
