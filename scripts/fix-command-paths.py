#!/usr/bin/env python3
"""Rewrite all command stubs to use absolute paths instead of relative paths.
This makes skills work from any project directory, not just reasoningtool."""

import os
import glob

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
COMMANDS_DIR = os.path.join(REPO_ROOT, '.claude', 'commands')
RELATIVE_PREFIX = 'claude-code-plugin/skills/'
ABSOLUTE_PREFIX = os.path.join(REPO_ROOT, 'claude-code-plugin', 'skills') + '/'

def main():
    updated = 0
    skipped = 0

    for cmd_file in sorted(glob.glob(os.path.join(COMMANDS_DIR, '*.md'))):
        with open(cmd_file, 'r') as f:
            content = f.read()

        if RELATIVE_PREFIX in content and ABSOLUTE_PREFIX not in content:
            new_content = content.replace(RELATIVE_PREFIX, ABSOLUTE_PREFIX)
            with open(cmd_file, 'w') as f:
                f.write(new_content)
            updated += 1
        else:
            skipped += 1

    print(f'Updated {updated} stubs to absolute paths, {skipped} already absolute or no match')

if __name__ == '__main__':
    main()
