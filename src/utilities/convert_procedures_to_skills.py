#!/usr/bin/env python3
"""
Convert GOSM procedures (YAML) to Claude Code skills (Markdown).

This allows Claude Code to use all GOSM procedures natively through the skill system.
"""

import argparse
import os
import re
import sys
from pathlib import Path

import yaml


def yaml_to_skill(proc: dict, proc_id: str) -> str:
    """Convert a procedure dict to skill markdown."""

    name = proc.get('name', proc_id.replace('_', ' ').title())
    desc_raw = proc.get('description', '')
    # Handle description being dict or other non-string
    if isinstance(desc_raw, str):
        description = desc_raw.strip()
    elif isinstance(desc_raw, dict):
        description = desc_raw.get('summary', str(desc_raw))
    else:
        description = str(desc_raw) if desc_raw else ''
    domain = proc.get('domain', 'core')
    version = proc.get('version', '1.0')

    # Build frontmatter
    # Short description for Claude's model invocation
    short_desc = description.split('\n')[0][:200] if description else f"GOSM {name} procedure"

    frontmatter = f"""---
name: {proc_id}
description: "{short_desc}"
---"""

    # Build body
    body_parts = [f"# {name}", ""]

    if description:
        body_parts.append("## Overview")
        body_parts.append(description)
        body_parts.append("")

    # Add core principle if present
    if proc.get('core_principle'):
        body_parts.append("## Core Principle")
        cp = proc['core_principle']
        body_parts.append(cp.strip() if isinstance(cp, str) else str(cp))
        body_parts.append("")

    # Add goal if present
    if proc.get('goal'):
        body_parts.append("## Goal")
        goal = proc['goal']
        body_parts.append(goal.strip() if isinstance(goal, str) else str(goal))
        body_parts.append("")

    # Add principles if present
    if proc.get('principles'):
        body_parts.append("## Principles")
        principles = proc['principles']
        if isinstance(principles, dict):
            for key, value in principles.items():
                body_parts.append(f"### {key.replace('_', ' ').title()}")
                body_parts.append(value.strip() if isinstance(value, str) else str(value))
                body_parts.append("")
        elif isinstance(principles, list):
            for p in principles:
                if isinstance(p, dict):
                    body_parts.append(f"- **{p.get('name', 'Principle')}**: {p.get('description', str(p))}")
                else:
                    body_parts.append(f"- {p}")
            body_parts.append("")

    # Add steps if present
    if proc.get('steps'):
        body_parts.append("## Steps")
        body_parts.append("")
        steps = proc['steps']
        for i, step in enumerate(steps, 1):
            if isinstance(step, dict):
                step_name = step.get('name', step.get('id', f'Step {i}'))
                step_action = step.get('action', step.get('description', ''))
                step_output = step.get('output', '')

                body_parts.append(f"### Step {i}: {step_name}")
                if step_action:
                    body_parts.append(step_action.strip() if isinstance(step_action, str) else str(step_action))
                if step_output:
                    body_parts.append(f"\n**Output**: {step_output}")
                body_parts.append("")
            else:
                body_parts.append(f"{i}. {step}")
        body_parts.append("")

    # Add when_to_use if present
    if proc.get('when_to_use'):
        body_parts.append("## When to Use")
        when = proc['when_to_use']
        if isinstance(when, list):
            for item in when:
                body_parts.append(f"- {item}")
        elif isinstance(when, dict):
            body_parts.append(yaml.dump(when, default_flow_style=False))
        else:
            body_parts.append(when.strip() if isinstance(when, str) else str(when))
        body_parts.append("")

    # Add common_cases if present
    if proc.get('common_cases'):
        body_parts.append("## Common Cases")
        cases = proc['common_cases']
        if isinstance(cases, dict):
            for case_name, case_data in cases.items():
                body_parts.append(f"### {case_name.replace('_', ' ').title()}")
                if isinstance(case_data, dict):
                    if case_data.get('old_behavior'):
                        body_parts.append(f"**Old behavior**: {case_data['old_behavior']}")
                    if case_data.get('new_behavior'):
                        body_parts.append(f"**New behavior**: {case_data['new_behavior']}")
                else:
                    body_parts.append(str(case_data))
                body_parts.append("")

    # Add verification if present
    if proc.get('verification'):
        body_parts.append("## Verification")
        verification = proc['verification']
        if isinstance(verification, list):
            for v in verification:
                body_parts.append(f"- {v}")
        else:
            body_parts.append(str(verification))
        body_parts.append("")

    # Add output_format if present
    if proc.get('output_format'):
        body_parts.append("## Output Format")
        body_parts.append("```")
        output_fmt = proc['output_format']
        if isinstance(output_fmt, str):
            body_parts.append(output_fmt.strip())
        elif isinstance(output_fmt, dict):
            body_parts.append(yaml.dump(output_fmt, default_flow_style=False))
        else:
            body_parts.append(str(output_fmt))
        body_parts.append("```")
        body_parts.append("")

    # Add invokes_gates if present
    if proc.get('invokes_gates'):
        body_parts.append("## Gates Invoked")
        for gate in proc['invokes_gates']:
            body_parts.append(f"- {gate}")
        body_parts.append("")

    # Add instruction to use $ARGUMENTS
    body_parts.append("---")
    body_parts.append("")
    body_parts.append("**Input**: $ARGUMENTS")
    body_parts.append("")
    body_parts.append("Apply this procedure to the input provided.")

    return frontmatter + "\n\n" + "\n".join(body_parts)


def convert_procedure(yaml_path: Path, output_dir: Path) -> bool | str:
    """Convert a single procedure file to a skill.

    Returns:
        True if converted successfully
        False if skipped (e.g., index file, empty)
        str if error (contains error message)
    """
    try:
        content = yaml_path.read_text(encoding='utf-8')
        proc = yaml.safe_load(content)

        if not proc:
            return False

        proc_id = proc.get('id', yaml_path.stem)

        # Skip index files
        if proc_id.startswith('_'):
            return False

        # Create skill directory
        skill_dir = output_dir / proc_id
        skill_dir.mkdir(parents=True, exist_ok=True)

        # Generate skill content
        skill_content = yaml_to_skill(proc, proc_id)

        # Write skill file
        skill_file = skill_dir / "SKILL.md"
        skill_file.write_text(skill_content, encoding='utf-8')

        return True

    except yaml.YAMLError as e:
        error_msg = f"YAML error: {str(e).split(chr(10))[0]}"
        print(f"  ✗ {yaml_path.stem}: {error_msg}", file=sys.stderr)
        return error_msg
    except Exception as e:
        error_msg = f"Error: {e}"
        print(f"  ✗ {yaml_path.stem}: {error_msg}", file=sys.stderr)
        return error_msg


def convert_all(procedures_dir: Path, output_dir: Path, domains: list[str] | None = None) -> dict:
    """Convert all procedures to skills."""
    stats = {"converted": 0, "skipped": 0, "errors": 0, "failed_files": []}

    # Default to core if no domains specified
    if not domains:
        domains = ["core"]

    for domain in domains:
        domain_dir = procedures_dir / domain
        if not domain_dir.exists():
            print(f"Domain directory not found: {domain_dir}", file=sys.stderr)
            continue

        for yaml_file in domain_dir.rglob("*.yaml"):
            result = convert_procedure(yaml_file, output_dir)
            if result is True:
                stats["converted"] += 1
                print(f"  ✓ {yaml_file.stem}")
            elif result is False:
                # Skipped (e.g., index file)
                stats["skipped"] += 1
            else:
                # Error - result is the error message
                stats["errors"] += 1
                stats["failed_files"].append((yaml_file.stem, result))

    return stats


def main():
    parser = argparse.ArgumentParser(
        description='Convert GOSM procedures to Claude Code skills'
    )
    parser.add_argument(
        '--procedures-dir',
        default='library/procedures',
        help='Path to procedures directory'
    )
    parser.add_argument(
        '--output-dir',
        default='claude-code-plugin/skills',
        help='Output directory for skills'
    )
    parser.add_argument(
        '--domains',
        nargs='+',
        default=['core'],
        help='Domains to convert (default: core)'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Convert all domains'
    )
    parser.add_argument(
        '--single',
        help='Convert a single procedure file'
    )

    args = parser.parse_args()

    # Find GOSM root
    script_dir = Path(__file__).parent
    gosm_root = script_dir.parent

    procedures_dir = gosm_root / args.procedures_dir
    output_dir = gosm_root / args.output_dir

    if args.single:
        # Convert single file
        yaml_path = Path(args.single)
        if not yaml_path.exists():
            yaml_path = procedures_dir / args.single
        if not yaml_path.exists():
            print(f"File not found: {args.single}", file=sys.stderr)
            sys.exit(1)

        if convert_procedure(yaml_path, output_dir):
            print(f"Converted: {yaml_path.stem}")
        else:
            print(f"Failed to convert: {yaml_path}", file=sys.stderr)
            sys.exit(1)
    else:
        # Convert all in domains
        if args.all:
            domains = [d.name for d in procedures_dir.iterdir() if d.is_dir()]
        else:
            domains = args.domains

        print(f"Converting procedures from: {procedures_dir}")
        print(f"Domains: {domains}")
        print(f"Output: {output_dir}")
        print()

        stats = convert_all(procedures_dir, output_dir, domains)

        print()
        print(f"Converted: {stats['converted']}")
        print(f"Skipped: {stats['skipped']}")
        print(f"Errors: {stats['errors']}")

        if stats['failed_files']:
            print()
            print("Failed files (YAML syntax errors - originals not modified):")
            for name, error in stats['failed_files']:
                print(f"  - {name}")


if __name__ == '__main__':
    main()
