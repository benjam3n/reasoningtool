#!/usr/bin/env python3
"""Update output format for skills that produce structured (non-prose) output."""

import os
import re

SKILLS_DIR = os.path.join(os.path.dirname(__file__), '..', 'claude-code-plugin', 'skills')

# Skills with structured output and their correct format
STRUCTURED = {
    'araw': 'registry',
    'ar': 'registry',
    'aw': 'registry',
    'u': 'registry',
    'cmp': 'table',
    'cba': 'table',
    'dd': 'table',
    'se': 'table',
    'mv': 'table',
    'ro': 'ranked-list',
    'list': 'checklist',
    'stg': 'checklist',
    'dcp': 'tree',
    'to': 'hybrid',
    'extract': 'hybrid',
}

def update_skill(name, fmt):
    skill_md = os.path.join(SKILLS_DIR, name, 'SKILL.md')
    if not os.path.isfile(skill_md):
        print(f'  MISSING: {name}')
        return False

    with open(skill_md, 'r') as f:
        content = f.read()

    # Replace format: "prose" with the correct format
    new_content = re.sub(
        r'output:\n  format: "prose"',
        f'output:\n  format: "{fmt}"',
        content
    )

    if new_content == content:
        print(f'  NO CHANGE: {name} (may already be set or different format)')
        return False

    with open(skill_md, 'w') as f:
        f.write(new_content)

    return True

def main():
    updated = 0
    for name, fmt in sorted(STRUCTURED.items()):
        if update_skill(name, fmt):
            print(f'  {name}: prose → {fmt}')
            updated += 1

    print(f'\nUpdated {updated} skills to structured output formats')

if __name__ == '__main__':
    main()
