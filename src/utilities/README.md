# Utilities

Scripts for managing the reasoning-toolkit procedure library: clustering similar procedures, converting between formats, auditing for quality issues, and syncing to Claude Code.

## Scripts

### consolidate_library.py — Cluster and stratify procedures

Three-phase pipeline for organizing the procedure library:

1. **Phase 1**: Cluster similar procedures using MinHash LSH (finds redundancy)
2. **Phase 2**: Quality stratification (platinum / gold / silver tiers)
3. **Phase 3**: Generate lightweight retrieval index

```bash
python consolidate_library.py --phase 1    # Analyze redundancy
python consolidate_library.py --phase 2    # Stratify quality
python consolidate_library.py --phase 3    # Generate index
python consolidate_library.py --all        # Run all phases
python consolidate_library.py --dry-run    # Preview changes
python consolidate_library.py --verbose    # Detailed output
```

### convert_procedures_to_skills.py — YAML to Claude Code skills

Converts GOSM procedures (YAML format) into Claude Code skills (Markdown SKILL.md files). This is how the 207 thinking skills in `claude-code-plugin/skills/` were generated.

```bash
python convert_procedures_to_skills.py                     # Convert all
python convert_procedures_to_skills.py --category core     # Convert one category
python convert_procedures_to_skills.py --output /path/to/skills/  # Custom output dir
```

### update_procedure_registry.py — Scan and update registry

Scans all procedure files and updates the central PROCEDURE_REGISTRY.yaml with current metadata, usage stats, and project mappings.

```bash
python update_procedure_registry.py                # Full update
python update_procedure_registry.py --check-only   # Report without modifying
python update_procedure_registry.py --output /path/to/registry.yaml
```

### audit_procedure_library_health.py — Library health audit

Checks the procedure library for issues: duplicate procedures, orphaned files, broken cross-references, missing required fields, schema violations.

```bash
python audit_procedure_library_health.py                   # Full audit
python audit_procedure_library_health.py --check duplicates  # Specific check
```

Outputs a markdown report to `projects/_reports/procedure_library_health_report.md`.

### sync_skills_to_claude.sh — Sync skills to Claude Code

Creates symlinks from the skills directory into Claude Code's plugin directory. Run after adding new skills.

```bash
./sync_skills_to_claude.sh
```

## Dependencies

```bash
pip install pyyaml
```

The utilities only require `pyyaml`. The `pandas`, `beautifulsoup4`, and other packages listed in `requirements.txt` are optional — only needed if you use specific features of the ARAW engine or runners.
