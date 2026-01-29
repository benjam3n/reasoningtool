#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = REPO_ROOT / "library" / "PROCEDURE_REGISTRY.yaml"
DEFAULT_EVENTS = REPO_ROOT / "library" / "PROCEDURE_REGISTRY_EVENTS.yaml"
DEFAULT_USAGE_MD = REPO_ROOT / "library" / "PROCEDURE_USAGE.md"
DEFAULT_PROJECT_MAPPING = REPO_ROOT / "library" / "PROJECT_PROCEDURE_MAPPING.yaml"
DEFAULT_CATALOG = REPO_ROOT / "library" / "PROCEDURE_CATALOG.yaml"
DEFAULT_GATES_DIR = REPO_ROOT / "library" / "gates"
DEFAULT_PROCEDURES_DIR = REPO_ROOT / "library" / "procedures"


VALUE_RE = re.compile(r"^(HIGH|MEDIUM|LOW|NEGATIVE)$")
TIME_RE = re.compile(
    r"^(?P<num>[0-9]+(?:\.[0-9]+)?)\s*(?P<unit>m|min|mins|minute|minutes|h|hr|hrs|hour|hours)$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class UsageEntry:
    date: dt.date
    procedure_id: str
    project: str
    value: str
    minutes: float


def _today_iso() -> str:
    return dt.date.today().isoformat()


def _now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def _read_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _write_yaml(path: Path, data: Any) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def _parse_time_to_minutes(raw: str) -> float:
    raw = raw.strip()
    m = TIME_RE.match(raw)
    if not m:
        raise ValueError(f"Unsupported time format: {raw!r}")
    num = float(m.group("num"))
    unit = m.group("unit").lower()
    if unit in {"m", "min", "mins", "minute", "minutes"}:
        return num
    if unit in {"h", "hr", "hrs", "hour", "hours"}:
        return num * 60.0
    raise ValueError(f"Unsupported time unit: {unit!r}")


def _iter_markdown_table_rows(lines: Iterable[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    in_table = False
    for line in lines:
        if line.strip().startswith("| Date | Procedure |"):
            in_table = True
            continue
        if not in_table:
            continue
        if line.strip().startswith("|------"):
            continue
        if not line.strip().startswith("|"):
            if rows:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        rows.append(cells)
    return rows


def parse_usage_log_md(path: Path) -> list[UsageEntry]:
    text = path.read_text(encoding="utf-8").splitlines()
    rows = _iter_markdown_table_rows(text)
    entries: list[UsageEntry] = []
    for cells in rows:
        date_raw, procedure_id, project, value_raw, time_raw = cells[:5]
        date_val = dt.date.fromisoformat(date_raw.strip())
        procedure_id = procedure_id.strip()
        project = project.strip()
        value = value_raw.strip().upper()
        if not VALUE_RE.match(value):
            raise ValueError(f"Unsupported value rating {value_raw!r} in {path}")
        minutes = _parse_time_to_minutes(time_raw)
        entries.append(
            UsageEntry(
                date=date_val,
                procedure_id=procedure_id,
                project=project,
                value=value,
                minutes=minutes,
            )
        )
    return entries


def _iter_yaml_files(root: Path) -> Iterator[Path]:
    for p in sorted(root.rglob("*.yaml")):
        if p.name in {"index.yaml", "_index.yaml"}:
            continue
        yield p
    for p in sorted(root.rglob("*.yml")):
        if p.name in {"index.yml", "_index.yml"}:
            continue
        yield p


def _looks_like_category_definition(doc: Any) -> bool:
    return (
        isinstance(doc, dict)
        and "subcategories" in doc
        and "procedure" not in doc
        and "procedures" not in doc
        and "steps" not in doc
    )


def _extract_procedure_dicts(doc: Any) -> list[dict[str, Any]]:
    if isinstance(doc, list):
        return [d for d in doc if isinstance(d, dict)]
    if isinstance(doc, dict):
        if _looks_like_category_definition(doc):
            return []
        if "procedures" in doc and isinstance(doc["procedures"], list):
            return [d for d in doc["procedures"] if isinstance(d, dict)]
        if "procedure" in doc and isinstance(doc["procedure"], dict):
            return [doc["procedure"]]
        if "id" in doc:
            return [doc]
    return []


def _coerce_str_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    if isinstance(value, dict):
        return [str(k) for k in value.keys()]
    return [str(value)]


def _load_procedure_sources(procedures_dir: Path) -> dict[str, dict[str, Any]]:
    """
    Return procedure_id -> {path_rel, raw, name?, domain?}.

    Note: This scans YAML directly (not ProcedureStore) so we can compute structural quality.
    """
    proc_sources: dict[str, dict[str, Any]] = {}
    for fp in _iter_yaml_files(procedures_dir):
        try:
            doc = yaml.safe_load(fp.read_text(encoding="utf-8"))
        except Exception:
            continue
        for proc_dict in _extract_procedure_dicts(doc):
            proc_id_raw = proc_dict.get("id")
            if proc_id_raw is None:
                continue
            proc_id = str(proc_id_raw)
            if proc_id in proc_sources:
                raise ValueError(f"Duplicate procedure id while building registry: {proc_id} ({fp})")

            proc_sources[proc_id] = {
                "path_rel": str(fp.relative_to(REPO_ROOT / "library")),
                "raw": proc_dict,
                "name": proc_dict.get("name"),
                "domain": proc_dict.get("domain"),
            }
    return proc_sources


def _collect_values_by_key(doc: Any, key: str) -> list[Any]:
    found: list[Any] = []
    if isinstance(doc, dict):
        for k, v in doc.items():
            if k == key:
                found.append(v)
            found.extend(_collect_values_by_key(v, key))
    elif isinstance(doc, list):
        for item in doc:
            found.extend(_collect_values_by_key(item, key))
    return found


def _load_gate_procedure_references(gates_dir: Path, known_proc_ids: set[str]) -> dict[str, dict[str, Any]]:
    """
    Return procedure_id -> {any_count, core_count, gate_ids[], via{key:count}}.

    We count both:
    - evaluation procedure references (evaluation_procedure)
    - routing targets that reference procedures (on_fail/on_partial/on_pass/on_skip/on_error)
    """
    refs: dict[str, dict[str, Any]] = {}
    keys = ["evaluation_procedure", "on_fail", "on_partial", "on_pass", "on_skip", "on_error"]
    for fp in _iter_yaml_files(gates_dir):
        try:
            doc = yaml.safe_load(fp.read_text(encoding="utf-8"))
        except Exception:
            continue

        gate_ids = [v for v in _collect_values_by_key(doc, "id") if isinstance(v, str)]
        is_core = "gates/core" in str(fp).replace("\\", "/") or fp.name == "core_gates.yaml"

        for k in keys:
            vals = _collect_values_by_key(doc, k)
            for v in vals:
                if not isinstance(v, str):
                    continue
                if v not in known_proc_ids:
                    continue
                entry = refs.setdefault(v, {"any_count": 0, "core_count": 0, "gate_ids": [], "via": {}})
                entry["any_count"] += 1
                if is_core:
                    entry["core_count"] += 1
                via = entry.get("via", {})
                if not isinstance(via, dict):
                    via = {}
                via[k] = int(via.get(k, 0)) + 1
                entry["via"] = via
                entry["gate_ids"] = sorted(set(entry.get("gate_ids", []) + gate_ids))
    return refs


def _load_catalog_index(catalog_path: Path) -> dict[str, dict[str, Any]]:
    if not catalog_path.exists():
        return {}
    doc = _read_yaml(catalog_path) or {}
    if not isinstance(doc, dict):
        return {}
    out: dict[str, dict[str, Any]] = {}
    for section, items in doc.items():
        if section in {"version", "updated", "listed_procedures_count", "total_procedures"}:
            continue
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            pid = item.get("id")
            if not isinstance(pid, str):
                continue
            out[pid] = {
                "section": str(section),
                "path": item.get("path"),
                "tags": item.get("tags"),
                "when": item.get("when"),
            }
    return out


def _load_project_mapping_refs(mapping: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """
    Return proc_id -> {clusters: {cluster_id: count}, total_refs}.

    Mapping entries are often strings like "meta/framework_extension"; we use the last segment.
    """
    refs: dict[str, dict[str, Any]] = {}
    clusters = mapping.get("clusters", {})
    if isinstance(clusters, dict):
        for cluster_id, cluster in clusters.items():
            if not isinstance(cluster, dict):
                continue
            for p in cluster.get("procedures", []) or []:
                proc_token = str(p)
                proc_id = proc_token.split("/")[-1]
                entry = refs.setdefault(proc_id, {"clusters": {}, "total_refs": 0})
                entry["total_refs"] += 1
                entry["clusters"][str(cluster_id)] = entry["clusters"].get(str(cluster_id), 0) + 1
    standalone = mapping.get("standalone", {})
    if isinstance(standalone, dict):
        for _, block in standalone.items():
            if not isinstance(block, dict):
                continue
            for p in block.get("procedures", []) or []:
                proc_token = str(p)
                proc_id = proc_token.split("/")[-1]
                entry = refs.setdefault(proc_id, {"clusters": {}, "total_refs": 0})
                entry["total_refs"] += 1
                entry["clusters"]["standalone"] = entry["clusters"].get("standalone", 0) + 1
    return refs


def _project_to_cluster(mapping: dict[str, Any]) -> dict[str, str]:
    project_cluster: dict[str, str] = {}
    clusters = mapping.get("clusters", {})
    if isinstance(clusters, dict):
        for cluster_id, cluster in clusters.items():
            if not isinstance(cluster, dict):
                continue
            for p in cluster.get("projects", []) or []:
                project_cluster[str(p)] = str(cluster_id)

    standalone = mapping.get("standalone", {})
    if isinstance(standalone, dict):
        for project_id in standalone.keys():
            project_cluster[str(project_id)] = "standalone"

    return project_cluster


def _score_value(value_scores: dict[str, Any], value: str) -> int:
    score = value_scores.get(value)
    if not isinstance(score, int):
        raise ValueError(f"Missing score for value rating: {value}")
    return score


def _compute_quantitative_metrics(
    usage: list[UsageEntry],
    project_cluster: dict[str, str],
    value_scores: dict[str, Any],
) -> dict[str, Any]:
    per_proc: dict[str, dict[str, Any]] = {}
    for e in usage:
        proc = per_proc.setdefault(
            e.procedure_id,
            {
                "uses_total": 0,
                "minutes_total": 0.0,
                "value_scores": [],
                "value_counts": {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "NEGATIVE": 0},
                "negative_count": 0,
                "uses_by_cluster": {},
                "minutes_by_cluster": {},
                "uses_by_project": {},
            },
        )
        proc["uses_total"] += 1
        proc["minutes_total"] += e.minutes
        s = _score_value(value_scores, e.value)
        proc["value_scores"].append(s)
        if isinstance(proc.get("value_counts"), dict) and e.value in proc["value_counts"]:
            proc["value_counts"][e.value] = int(proc["value_counts"].get(e.value, 0)) + 1
        if s < 0:
            proc["negative_count"] += 1

        cluster = project_cluster.get(e.project, "unknown")
        proc["uses_by_cluster"][cluster] = proc["uses_by_cluster"].get(cluster, 0) + 1
        proc["minutes_by_cluster"][cluster] = proc["minutes_by_cluster"].get(cluster, 0.0) + e.minutes
        proc["uses_by_project"][e.project] = proc["uses_by_project"].get(e.project, 0) + 1

    for proc_id, stats in per_proc.items():
        scores = stats.get("value_scores", [])
        avg_value = (sum(scores) / len(scores)) if scores else None
        minutes_total = float(stats.get("minutes_total") or 0.0)
        uses_total = int(stats.get("uses_total") or 0)
        roi = (float(avg_value) * uses_total / minutes_total) if (avg_value is not None and minutes_total > 0) else None
        negative_count = int(stats.get("negative_count") or 0)
        negative_rate = (negative_count / uses_total) if uses_total > 0 else 0.0
        unique_projects_count = len((stats.get("uses_by_project") or {}).keys()) if isinstance(stats.get("uses_by_project"), dict) else 0

        stats["avg_value_score"] = avg_value
        stats["roi"] = roi
        stats["negative_rate"] = negative_rate
        stats["unique_projects_count"] = unique_projects_count
        stats.pop("value_scores", None)

    return per_proc


def _evidence_state(quantitative: dict[str, Any]) -> str:
    uses = int(quantitative.get("uses_total") or 0)
    if uses <= 0:
        return "no-evidence"

    unique_projects_count = int(quantitative.get("unique_projects_count") or 0)
    if unique_projects_count <= 1:
        return "single-project"

    counts = quantitative.get("value_counts") or {}
    if not isinstance(counts, dict):
        counts = {}
    high = int(counts.get("HIGH") or 0)
    medium = int(counts.get("MEDIUM") or 0)
    low = int(counts.get("LOW") or 0)
    negative = int(counts.get("NEGATIVE") or 0)

    if (low + negative) == 0:
        return "validated-beneficial"
    if (high + medium) == 0:
        return "validated-unhelpful"
    return "validated-mixed"


def _centrality_state(qualitative: dict[str, Any]) -> str:
    gate_refs = qualitative.get("gate_references", {})
    if not isinstance(gate_refs, dict):
        gate_refs = {}

    if gate_refs.get("in_core_gates") is True:
        return "required-by-core-gates"
    if gate_refs.get("in_any_gate") is True:
        return "required-by-gates"
    return "not-required-by-gates"


def _generality_state(qualitative: dict[str, Any]) -> str:
    clusters = qualitative.get("project_clusters", {})
    if not isinstance(clusters, dict):
        clusters = {}

    combined = clusters.get("combined") or []
    n = len(combined) if isinstance(combined, list) else int(clusters.get("combined_count") or 0)
    if n >= 2:
        return "multiple-project-clusters"
    if n == 1:
        return "one-project-cluster"
    return "no-project-cluster-signal"


def _schema_state(qualitative: dict[str, Any]) -> str:
    checks = qualitative.get("structure_checks", {})
    if isinstance(checks, dict) and checks.get("minimum_structure_present") is True:
        return "minimum-structure-present"
    return "minimum-structure-missing"


def _recommended_actions(states: dict[str, str]) -> list[str]:
    """
    Deterministic projection from states -> action list.
    """
    actions: list[str] = []
    evidence_state = states.get("evidence")
    centrality_state = states.get("centrality")
    schema_state = states.get("structure")

    if evidence_state in {"validated-mixed", "validated-unhelpful"}:
        actions.append("investigate")
    if centrality_state in {"required-by-core-gates", "required-by-gates"} and schema_state == "minimum-structure-missing":
        actions.append("improve")
    if centrality_state in {"required-by-core-gates", "required-by-gates"} and evidence_state == "no-evidence":
        actions.append("promote")
    if centrality_state in {"required-by-core-gates", "required-by-gates"} and evidence_state == "validated-beneficial":
        actions.append("expand")

    # Preserve order, de-duplicate.
    out: list[str] = []
    for a in actions:
        if a not in out:
            out.append(a)
    return out


def _structure_checks(proc: dict[str, Any]) -> dict[str, bool]:
    has_id = proc.get("id") is not None
    has_description = bool(proc.get("description") or proc.get("purpose"))
    steps = proc.get("steps")
    has_steps = isinstance(steps, list) and len(steps) > 0

    minimum_structure_present = bool(has_id and has_description and has_steps)

    inputs = proc.get("inputs") or proc.get("parameters") or []
    outputs = proc.get("outputs") or []
    inputs_present = isinstance(inputs, list) and len(inputs) > 0
    outputs_present = isinstance(outputs, list) and len(outputs) > 0
    usage_guidance_present = bool(proc.get("when_to_use") or proc.get("use_cases") or proc.get("triggers"))
    examples = proc.get("examples") or []
    examples_present = isinstance(examples, list) and len(examples) > 0

    recommended_structure_present = bool(
        minimum_structure_present and inputs_present and outputs_present and usage_guidance_present and examples_present
    )

    anti_patterns_present = bool(proc.get("anti_patterns") or proc.get("when_not_to_use"))
    failure_modes = proc.get("failure_modes") or []
    failure_modes_present = isinstance(failure_modes, list) and len(failure_modes) > 0
    integration_guidance_present = bool(proc.get("gosm_integration") or proc.get("integration_with_gosm"))

    integrated_structure_present = bool(
        recommended_structure_present and anti_patterns_present and failure_modes_present and integration_guidance_present
    )

    return {
        "minimum_structure_present": minimum_structure_present,
        "recommended_structure_present": recommended_structure_present,
        "integrated_structure_present": integrated_structure_present,
        "inputs_present": inputs_present,
        "outputs_present": outputs_present,
        "usage_guidance_present": usage_guidance_present,
        "examples_present": examples_present,
        "failure_modes_present": failure_modes_present,
        "integration_guidance_present": integration_guidance_present,
        "anti_patterns_present": anti_patterns_present,
    }


def _merge_registry(
    registry: dict[str, Any],
    proc_sources: dict[str, dict[str, Any]],
    quantitative: dict[str, Any],
    qualitative: dict[str, Any],
    derived: dict[str, dict[str, Any]],
    unresolved_usage: dict[str, Any],
) -> dict[str, Any]:
    procedures: dict[str, Any] = {}

    for proc_id in sorted(proc_sources.keys()):
        entry: dict[str, Any] = {}

        src = proc_sources[proc_id]
        entry["metadata"] = {
            "path": src.get("path_rel"),
            "domain": src.get("domain"),
            "name": src.get("name"),
        }
        entry["quantitative"] = quantitative.get(
            proc_id,
            {
                "uses_total": 0,
                "minutes_total": 0.0,
                "negative_rate": 0.0,
                "unique_projects_count": 0,
                "value_counts": {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "NEGATIVE": 0},
            },
        )
        entry["qualitative"] = qualitative.get(proc_id, {})
        entry["derived"] = derived.get(proc_id, {})

        procedures[proc_id] = entry

    registry["procedures"] = procedures
    registry["unresolved_usage"] = unresolved_usage
    registry["updated"] = _today_iso()
    return registry


def _append_events(
    events_doc: dict[str, Any],
    previous_registry: dict[str, Any],
    updated_registry: dict[str, Any],
    run_id: str,
) -> dict[str, Any]:
    events = events_doc.get("events", [])
    if not isinstance(events, list):
        events = []

    prev = previous_registry.get("procedures", {})
    new = updated_registry.get("procedures", {})
    if not isinstance(prev, dict):
        prev = {}
    if not isinstance(new, dict):
        new = {}

    axes = ["evidence", "centrality", "breadth", "structure"]
    for proc_id, new_entry in new.items():
        if not isinstance(new_entry, dict):
            continue
        prev_entry = prev.get(proc_id, {})
        if not isinstance(prev_entry, dict):
            continue
        new_derived = new_entry.get("derived", {})
        prev_derived = prev_entry.get("derived", {})
        if not isinstance(new_derived, dict) or not isinstance(prev_derived, dict):
            continue

        new_states = new_derived.get("states", {})
        prev_states = prev_derived.get("states", {})
        if not isinstance(new_states, dict) or not isinstance(prev_states, dict):
            continue

        for axis in axes:
            new_val = new_states.get(axis)
            prev_val = prev_states.get(axis)
            if prev_val is None or new_val is None or new_val == prev_val:
                continue

            q = new_entry.get("quantitative", {}) if isinstance(new_entry.get("quantitative"), dict) else {}
            qual = new_entry.get("qualitative", {}) if isinstance(new_entry.get("qualitative"), dict) else {}
            events.append(
                {
                    "timestamp": _now_iso(),
                    "run_id": run_id,
                    "procedure_id": proc_id,
                    "axis": axis,
                    "change": {"from": prev_val, "to": new_val},
                    "reason": "derived state evaluation",
                    "evidence": {
                        "uses_total": q.get("uses_total"),
                        "avg_value_score": q.get("avg_value_score"),
                        "roi": q.get("roi"),
                        "negative_rate": q.get("negative_rate"),
                        "unique_projects_count": q.get("unique_projects_count"),
                        "required_by_core_gates": (
                            (qual.get("gate_references") or {}).get("in_core_gates")
                            if isinstance(qual.get("gate_references"), dict)
                            else None
                        ),
                        "project_cluster_count": (
                            (qual.get("project_clusters") or {}).get("combined_count")
                            if isinstance(qual.get("project_clusters"), dict)
                            else None
                        ),
                    },
                }
            )

        # Recommended actions changes are also meaningful to track.
        new_actions = new_derived.get("recommended_actions", [])
        prev_actions = prev_derived.get("recommended_actions", [])
        if isinstance(new_actions, list) and isinstance(prev_actions, list) and new_actions != prev_actions:
            events.append(
                {
                    "timestamp": _now_iso(),
                    "run_id": run_id,
                    "procedure_id": proc_id,
                    "axis": "recommended_actions",
                    "change": {"from": prev_actions, "to": new_actions},
                    "reason": "projection evaluation",
                    "evidence": {"uses_total": (new_entry.get("quantitative") or {}).get("uses_total")},
                }
            )

    events_doc["events"] = events
    return events_doc


def main() -> int:
    parser = argparse.ArgumentParser(description="Update the central procedure registry (quantitative + qualitative signals).")
    parser.add_argument("--registry", type=str, default=str(DEFAULT_REGISTRY))
    parser.add_argument("--events", type=str, default=str(DEFAULT_EVENTS))
    parser.add_argument("--usage-md", type=str, default=str(DEFAULT_USAGE_MD))
    parser.add_argument("--project-mapping", type=str, default=str(DEFAULT_PROJECT_MAPPING))
    parser.add_argument("--catalog", type=str, default=str(DEFAULT_CATALOG))
    parser.add_argument("--procedures-dir", type=str, default=str(DEFAULT_PROCEDURES_DIR))
    parser.add_argument("--gates-dir", type=str, default=str(DEFAULT_GATES_DIR))
    args = parser.parse_args()

    registry_path = Path(args.registry)
    events_path = Path(args.events)
    usage_path = Path(args.usage_md)
    mapping_path = Path(args.project_mapping)
    catalog_path = Path(args.catalog)
    procedures_dir = Path(args.procedures_dir)
    gates_dir = Path(args.gates_dir)

    if not registry_path.exists():
        raise FileNotFoundError(f"Registry not found: {registry_path}")
    if not usage_path.exists():
        raise FileNotFoundError(f"Usage log not found: {usage_path}")
    if not mapping_path.exists():
        raise FileNotFoundError(f"Project mapping not found: {mapping_path}")
    if not procedures_dir.exists():
        raise FileNotFoundError(f"Procedures dir not found: {procedures_dir}")
    if not gates_dir.exists():
        raise FileNotFoundError(f"Gates dir not found: {gates_dir}")

    previous_registry = _read_yaml(registry_path) or {}
    if not isinstance(previous_registry, dict):
        raise ValueError("Registry must be a YAML mapping at top level")

    events_doc = {}
    if events_path.exists():
        events_doc = _read_yaml(events_path) or {}
    if not isinstance(events_doc, dict):
        raise ValueError("Events doc must be a YAML mapping at top level")
    events_doc.setdefault("version", "2.1")
    events_doc.setdefault("events", [])

    usage = parse_usage_log_md(usage_path)
    project_mapping = _read_yaml(mapping_path) or {}
    if not isinstance(project_mapping, dict):
        project_mapping = {}

    policy = previous_registry.get("policy", {})
    if not isinstance(policy, dict):
        raise ValueError("Registry missing policy mapping")

    project_cluster = _project_to_cluster(project_mapping)
    value_scores = policy.get("value_scores", {})
    if not isinstance(value_scores, dict):
        raise ValueError("policy.value_scores must be a mapping")

    proc_sources = _load_procedure_sources(procedures_dir)
    catalog_index = _load_catalog_index(catalog_path)
    mapping_refs = _load_project_mapping_refs(project_mapping)
    gate_refs = _load_gate_procedure_references(gates_dir, set(proc_sources.keys()))

    quantitative = _compute_quantitative_metrics(usage, project_cluster, value_scores)

    qualitative: dict[str, Any] = {}
    derived: dict[str, dict[str, Any]] = {}
    for proc_id, src in proc_sources.items():
        raw = src.get("raw", {})
        if not isinstance(raw, dict):
            raw = {}

        structure_checks = _structure_checks(raw)
        mapping_clusters = sorted(
            set(
                (
                    mapping_refs.get(proc_id, {}).get("clusters", {})
                    if isinstance(mapping_refs.get(proc_id, {}), dict)
                    else {}
                ).keys()
            )
        )
        gate_ref = gate_refs.get(proc_id, {})
        referenced_by_any_gates = bool(isinstance(gate_ref, dict) and int(gate_ref.get("any_count") or 0) > 0)
        referenced_by_core_gates = bool(isinstance(gate_ref, dict) and int(gate_ref.get("core_count") or 0) > 0)
        gate_ids = (gate_ref.get("gate_ids") if isinstance(gate_ref, dict) else []) or []
        if not isinstance(gate_ids, list):
            gate_ids = []
        via_keys = (gate_ref.get("via") if isinstance(gate_ref, dict) else {}) or {}
        if not isinstance(via_keys, dict):
            via_keys = {}

        q = quantitative.get(proc_id, {"uses_total": 0, "minutes_total": 0.0, "negative_rate": 0.0})
        uses_by_cluster = q.get("uses_by_cluster") if isinstance(q, dict) else {}
        if not isinstance(uses_by_cluster, dict):
            uses_by_cluster = {}
        usage_clusters_raw = sorted(set(str(k) for k in uses_by_cluster.keys()))
        usage_clusters = [c for c in usage_clusters_raw if c != "unknown"]
        combined_clusters = sorted(set(mapping_clusters).union(set(usage_clusters)))

        qualitative[proc_id] = {
            "catalog": {
                "listed": proc_id in catalog_index,
                "section": (
                    (catalog_index.get(proc_id, {}) if isinstance(catalog_index.get(proc_id, {}), dict) else {})
                ).get("section"),
            },
            "gate_references": {
                "in_any_gate": referenced_by_any_gates,
                "in_core_gates": referenced_by_core_gates,
                "gate_ids": gate_ids,
                "via_keys": via_keys,
            },
            "project_clusters": {
                "from_mapping": mapping_clusters,
                "from_usage": usage_clusters,
                "from_usage_raw": usage_clusters_raw,
                "combined": combined_clusters,
                "combined_count": len(combined_clusters),
            },
            "structure_checks": structure_checks,
        }

        states = {
            "evidence": _evidence_state(q),
            "centrality": _centrality_state(qualitative[proc_id]),
            "breadth": _generality_state(qualitative[proc_id]),
            "structure": _schema_state(qualitative[proc_id]),
        }
        derived[proc_id] = {
            "states": states,
            "recommended_actions": _recommended_actions(states),
        }

    unresolved_usage: dict[str, Any] = {}
    for proc_id, stats in quantitative.items():
        if proc_id in proc_sources:
            continue
        unresolved_usage[proc_id] = stats

    updated_registry = _merge_registry(
        previous_registry,
        proc_sources,
        quantitative,
        qualitative,
        derived,
        unresolved_usage,
    )

    run_id = f"update_procedure_registry@{_now_iso()}"
    events_doc = _append_events(events_doc, previous_registry, updated_registry, run_id)

    _write_yaml(registry_path, updated_registry)
    _write_yaml(events_path, events_doc)

    print(f"Updated: {registry_path}")
    print(f"Updated: {events_path}")
    print(f"Parsed usage entries: {len(usage)}")
    print(f"Procedures total: {len(proc_sources)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
