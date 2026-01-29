#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO_ROOT / "projects" / "_reports" / "procedure_library_health_report.md"


@dataclass(frozen=True)
class FileYAMLError:
    file_path: Path
    error: str


@dataclass(frozen=True)
class ProcedureParseError:
    file_path: Path
    procedure_id: str | None
    error: str


def _iter_procedure_files() -> list[Path]:
    base = REPO_ROOT / "library" / "procedures"
    files = sorted(base.rglob("*.yaml")) + sorted(base.rglob("*.yml"))
    return [p for p in files if p.name not in {"index.yaml", "index.yml", "_index.yaml", "_index.yml"}]


def _extract_procedure_dicts(doc: Any) -> list[dict[str, Any]]:
    if isinstance(doc, list):
        return [d for d in doc if isinstance(d, dict)]
    if isinstance(doc, dict):
        # Some YAML files under `library/procedures/**` are category definitions
        # (e.g. question banks) rather than executable procedures.
        if (
            "subcategories" in doc
            and "procedure" not in doc
            and "procedures" not in doc
            and "steps" not in doc
        ):
            return []
        if "procedures" in doc and isinstance(doc["procedures"], list):
            return [d for d in doc["procedures"] if isinstance(d, dict)]
        if "procedure" in doc and isinstance(doc["procedure"], dict):
            return [doc["procedure"]]
        if "id" in doc:
            return [doc]
    return []


def _now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit procedure library health (parseability + duplicates).")
    parser.add_argument(
        "--out",
        type=str,
        default=str(DEFAULT_OUT),
        help=f"Output report path (default: {DEFAULT_OUT})",
    )
    args = parser.parse_args()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    proc_files = _iter_procedure_files()
    yaml_errors: list[FileYAMLError] = []
    proc_errors: list[ProcedureParseError] = []

    procedure_ids: list[str] = []
    procedure_sources: dict[str, list[Path]] = {}
    domain_counts: dict[str, int] = {}

    # Allow running without installing the project as a package.
    import sys

    sys.path.insert(0, str(REPO_ROOT))

    # Import here so this script can still run enough to surface YAML parse errors even if
    # the Python package graph is broken elsewhere.
    from gosm.storage.procedure_store import ProcedureStore

    store = ProcedureStore(REPO_ROOT / "library" / "procedures")

    for f in proc_files:
        try:
            doc = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception as e:
            yaml_errors.append(FileYAMLError(file_path=f, error=str(e)))
            continue

        for proc_dict in _extract_procedure_dicts(doc):
            proc_id = None
            if isinstance(proc_dict.get("id"), str):
                proc_id = proc_dict.get("id")
            elif proc_dict.get("id") is not None:
                proc_id = str(proc_dict.get("id"))

            try:
                proc = store._parse_procedure(proc_dict)  # noqa: SLF001 (intentionally using parser)
            except Exception as e:
                proc_errors.append(
                    ProcedureParseError(
                        file_path=f,
                        procedure_id=proc_id,
                        error=str(e),
                    )
                )
                continue

            procedure_ids.append(proc.id)
            procedure_sources.setdefault(proc.id, []).append(f)
            domain = getattr(proc.domain, "value", str(proc.domain))
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

    duplicates = {k: v for k, v in procedure_sources.items() if len(v) > 1}

    lines: list[str] = []
    lines.append("# Procedure Library Health Report")
    lines.append("")
    lines.append(f"- Generated: `{_now_iso()}`")
    lines.append(f"- Procedure files scanned: `{len(proc_files)}`")
    lines.append(f"- YAML parse errors: `{len(yaml_errors)}`")
    lines.append(f"- Procedure parse errors: `{len(proc_errors)}`")
    lines.append(f"- Procedures parsed successfully: `{len(procedure_ids)}`")
    lines.append(f"- Duplicate procedure IDs: `{len(duplicates)}`")
    lines.append("")

    lines.append("## Domain Counts (Parsed Procedures)")
    for d in sorted(domain_counts.keys()):
        lines.append(f"- `{d}`: `{domain_counts[d]}`")
    lines.append("")

    if duplicates:
        lines.append("## Duplicate Procedure IDs")
        for proc_id in sorted(duplicates.keys()):
            files = duplicates[proc_id]
            lines.append(f"- `{proc_id}`:")
            for fp in files:
                lines.append(f"  - `{fp}`")
        lines.append("")

    if yaml_errors:
        lines.append("## YAML Parse Errors")
        for e in sorted(yaml_errors, key=lambda x: str(x.file_path)):
            lines.append(f"- `{e.file_path}`")
            lines.append(f"  - {e.error}")
        lines.append("")

    if proc_errors:
        lines.append("## Procedure Parse Errors")
        for e in sorted(proc_errors, key=lambda x: (str(x.file_path), x.procedure_id or "")):
            pid = e.procedure_id or "unknown_id"
            lines.append(f"- `{e.file_path}` (`{pid}`)")
            lines.append(f"  - {e.error}")
        lines.append("")

    lines.append("## Raw Summary (JSON)")
    summary = {
        "generated_at": _now_iso(),
        "procedure_files_scanned": len(proc_files),
        "yaml_parse_errors": len(yaml_errors),
        "procedure_parse_errors": len(proc_errors),
        "procedures_parsed_successfully": len(procedure_ids),
        "duplicate_procedure_ids": len(duplicates),
        "domain_counts": domain_counts,
    }
    lines.append("```json")
    lines.append(json.dumps(summary, indent=2, sort_keys=True))
    lines.append("```")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
