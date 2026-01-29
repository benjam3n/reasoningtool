#!/usr/bin/env python3
"""
GOSM Library Consolidation Pipeline (Memory-Efficient Version)

Phase 1: Cluster similar procedures using MinHash LSH
Phase 2: Quality stratification (platinum/gold/silver)
Phase 3: Generate lightweight retrieval index

Usage:
    python consolidate_library.py --phase 1  # Analyze redundancy
    python consolidate_library.py --phase 2  # Stratify quality
    python consolidate_library.py --phase 3  # Generate index
    python consolidate_library.py --all      # Run all phases
"""

import os
import sys
import json
import yaml
import argparse
import hashlib
import re
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional
import gc

# Paths
LIBRARY_ROOT = Path(__file__).parent.parent
PROCEDURES_DIR = LIBRARY_ROOT / "procedures" / "extracted" / "books"
OUTPUT_DIR = LIBRARY_ROOT / "consolidated"


@dataclass
class ProcedureMeta:
    """Lightweight procedure metadata for clustering."""
    id: str
    name: str
    description: str
    steps_text: str
    file_path: str
    quality_score: int = 50
    tier: str = "silver"
    category: str = "general"
    cluster_size: int = 1
    has_verification: bool = False
    has_failure_modes: bool = False
    has_when_to_use: bool = False
    step_count: int = 0

    def to_text(self) -> str:
        """Convert to searchable text."""
        return f"{self.name} {self.description} {self.steps_text}"

    def to_shingles(self, k: int = 3) -> set:
        """Convert to character k-shingles for MinHash."""
        text = self.to_text().lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        words = text.split()
        # Use word shingles instead of character shingles
        if len(words) < k:
            return set(words)
        return set(' '.join(words[i:i+k]) for i in range(len(words) - k + 1))

    def completeness_score(self) -> int:
        """Score based on field completeness."""
        score = 0
        if self.name: score += 10
        if len(self.description) > 20: score += 15
        if self.step_count >= 3: score += 20
        if self.has_when_to_use: score += 10
        if self.has_failure_modes: score += 15
        if self.has_verification: score += 15
        if self.cluster_size > 1: score += 10
        return score


def load_procedures_lightweight(procedures_dir: Path) -> list[ProcedureMeta]:
    """Load procedures with minimal memory footprint."""
    procedures = []
    yaml_files = list(procedures_dir.rglob("*.yaml"))

    print(f"Loading {len(yaml_files)} YAML files...")

    for i, fpath in enumerate(yaml_files):
        if fpath.name.startswith("_") or fpath.name in ("index.json", "README.md"):
            continue

        try:
            with open(fpath, "r") as f:
                data = yaml.safe_load(f)

            if not data or not isinstance(data, dict):
                continue

            # Skip index files
            if "procedures" in data or "by_category" in data:
                continue

            name = data.get("name", "")
            steps = data.get("steps", [])

            if not name or not steps:
                continue

            # Extract steps as text
            steps_text = " ".join(
                s.get("action", "") if isinstance(s, dict) else str(s)
                for s in steps
            )

            provenance = data.get("provenance", {})

            proc = ProcedureMeta(
                id=data.get("id", fpath.stem),
                name=name,
                description=data.get("description", "")[:500],
                steps_text=steps_text[:1000],
                file_path=str(fpath),
                quality_score=data.get("quality_score", 50),
                tier=data.get("tier", "silver"),
                category=data.get("category", "general"),
                cluster_size=provenance.get("cluster_size", 1),
                has_verification=bool(data.get("verification")),
                has_failure_modes=bool(data.get("failure_modes")),
                has_when_to_use=bool(data.get("when_to_use")),
                step_count=len(steps)
            )
            procedures.append(proc)

        except Exception as e:
            pass

        if (i + 1) % 5000 == 0:
            print(f"  Loaded {i + 1}/{len(yaml_files)}...")
            gc.collect()

    print(f"Loaded {len(procedures)} valid procedures")
    return procedures


class MinHashLSH:
    """Memory-efficient MinHash LSH for near-duplicate detection."""

    def __init__(self, num_hashes: int = 100, bands: int = 20):
        self.num_hashes = num_hashes
        self.bands = bands
        self.rows_per_band = num_hashes // bands
        self.hash_funcs = self._generate_hash_funcs(num_hashes)
        self.buckets = [defaultdict(list) for _ in range(bands)]

    def _generate_hash_funcs(self, n: int):
        """Generate hash function parameters."""
        import random
        random.seed(42)
        prime = 2147483647
        return [(random.randint(1, prime-1), random.randint(0, prime-1), prime) for _ in range(n)]

    def _minhash(self, shingles: set) -> tuple:
        """Compute MinHash signature."""
        signature = []
        for a, b, p in self.hash_funcs:
            min_hash = float('inf')
            for shingle in shingles:
                h = (a * hash(shingle) + b) % p
                min_hash = min(min_hash, h)
            signature.append(min_hash if min_hash != float('inf') else 0)
        return tuple(signature)

    def add(self, doc_id: str, shingles: set):
        """Add document to LSH index."""
        sig = self._minhash(shingles)
        for band_idx in range(self.bands):
            start = band_idx * self.rows_per_band
            end = start + self.rows_per_band
            band_sig = sig[start:end]
            bucket_key = hash(band_sig)
            self.buckets[band_idx][bucket_key].append(doc_id)

    def find_candidates(self) -> list[set]:
        """Find candidate pairs that share at least one bucket."""
        candidate_groups = defaultdict(set)

        for band_buckets in self.buckets:
            for bucket_key, doc_ids in band_buckets.items():
                if len(doc_ids) > 1:
                    # All docs in this bucket are candidates
                    key = frozenset(doc_ids)
                    for doc_id in doc_ids:
                        candidate_groups[doc_id].update(doc_ids)

        # Convert to clusters using Union-Find
        return self._cluster_candidates(candidate_groups)

    def _cluster_candidates(self, candidate_groups: dict) -> list[set]:
        """Cluster candidates using Union-Find."""
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Union all candidates
        for doc_id, candidates in candidate_groups.items():
            for cand in candidates:
                union(doc_id, cand)

        # Group by root
        clusters = defaultdict(set)
        for doc_id in parent:
            clusters[find(doc_id)].add(doc_id)

        return list(clusters.values())


def jaccard_similarity(set1: set, set2: set) -> float:
    """Compute Jaccard similarity between two sets."""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0


def phase1_analyze_redundancy(procedures: list[ProcedureMeta], output_dir: Path, threshold: float = 0.5):
    """Phase 1: Analyze redundancy using MinHash LSH."""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nPhase 1: Analyzing redundancy among {len(procedures)} procedures...")

    # Build id -> procedure mapping
    id_to_proc = {p.id: p for p in procedures}

    # Create shingles and add to LSH
    print("Building MinHash LSH index...")
    lsh = MinHashLSH(num_hashes=100, bands=25)

    shingles_cache = {}
    for i, proc in enumerate(procedures):
        shingles = proc.to_shingles(k=2)
        shingles_cache[proc.id] = shingles
        lsh.add(proc.id, shingles)

        if (i + 1) % 5000 == 0:
            print(f"  Indexed {i + 1}/{len(procedures)}...")

    # Find candidate clusters
    print("Finding similar procedure clusters...")
    candidate_clusters = lsh.find_candidates()

    print(f"  Found {len(candidate_clusters)} initial clusters")

    # Verify candidates with actual Jaccard similarity
    print("Verifying clusters with Jaccard similarity...")
    verified_clusters = []

    for cluster in candidate_clusters:
        if len(cluster) == 1:
            verified_clusters.append(cluster)
            continue

        # Verify pairwise similarity within cluster
        cluster_list = list(cluster)
        verified = set()

        for i, id1 in enumerate(cluster_list):
            for id2 in cluster_list[i+1:]:
                sim = jaccard_similarity(shingles_cache[id1], shingles_cache[id2])
                if sim >= threshold:
                    verified.add(id1)
                    verified.add(id2)

        if verified:
            verified_clusters.append(verified)
        else:
            # Split into singletons
            for doc_id in cluster:
                verified_clusters.append({doc_id})

    # Add singletons for procedures not in any cluster
    clustered_ids = set()
    for cluster in verified_clusters:
        clustered_ids.update(cluster)

    for proc in procedures:
        if proc.id not in clustered_ids:
            verified_clusters.append({proc.id})

    print(f"  Verified clusters: {len(verified_clusters)}")

    # Analyze redundancy
    redundant_clusters = [c for c in verified_clusters if len(c) > 1]
    singleton_clusters = [c for c in verified_clusters if len(c) == 1]

    total_in_redundant = sum(len(c) for c in redundant_clusters)

    report = {
        "total_procedures": len(procedures),
        "total_clusters": len(verified_clusters),
        "singleton_clusters": len(singleton_clusters),
        "redundant_clusters": len(redundant_clusters),
        "procedures_in_redundant_clusters": total_in_redundant,
        "estimated_unique": len(verified_clusters),
        "reduction_percentage": round((1 - len(verified_clusters) / len(procedures)) * 100, 1),
        "large_clusters": []
    }

    # Select representatives for each cluster
    cluster_mapping = {}
    sorted_clusters = sorted(verified_clusters, key=lambda x: len(x), reverse=True)

    for cluster in sorted_clusters:
        cluster_list = list(cluster)
        procs = [id_to_proc[pid] for pid in cluster_list if pid in id_to_proc]

        if not procs:
            continue

        # Select best representative
        scored = [(p.completeness_score() + p.quality_score + p.step_count * 2, p) for p in procs]
        scored.sort(key=lambda x: x[0], reverse=True)

        rep = scored[0][1]
        dups = [s[1] for s in scored[1:]]

        cluster_mapping[rep.id] = {
            "representative": True,
            "cluster_size": len(cluster),
            "absorbs": [d.id for d in dups]
        }

        for dup in dups:
            cluster_mapping[dup.id] = {
                "representative": False,
                "absorbed_by": rep.id
            }

        if len(cluster) > 1 and len(report["large_clusters"]) < 30:
            report["large_clusters"].append({
                "size": len(cluster),
                "representative": {"id": rep.id, "name": rep.name},
                "duplicates": [{"id": d.id, "name": d.name} for d in dups[:5]]
            })

    # Save results
    report_path = output_dir / "redundancy_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    mapping_path = output_dir / "cluster_mapping.json"
    with open(mapping_path, "w") as f:
        json.dump(cluster_mapping, f, indent=2)

    print(f"\n=== Phase 1 Summary ===")
    print(f"Total procedures: {report['total_procedures']}")
    print(f"Unique (after dedup): {report['estimated_unique']}")
    print(f"Redundant clusters: {report['redundant_clusters']}")
    print(f"Reduction potential: {report['reduction_percentage']}%")
    print(f"Report: {report_path}")

    return cluster_mapping, verified_clusters


def phase2_stratify_quality(procedures: list[ProcedureMeta], cluster_mapping: dict, output_dir: Path):
    """Phase 2: Stratify into platinum/gold/silver tiers."""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n=== Phase 2: Quality Stratification ===")

    # Get representatives only
    representatives = [p for p in procedures if cluster_mapping.get(p.id, {}).get("representative", True)]

    print(f"Scoring {len(representatives)} representative procedures...")

    # Score each with more granular scoring
    scored = []
    for proc in representatives:
        score = 0

        # Completeness factors (0-100)
        if proc.name: score += 5
        if len(proc.description) > 50: score += 10
        elif len(proc.description) > 20: score += 5
        if proc.step_count >= 7: score += 15
        elif proc.step_count >= 5: score += 10
        elif proc.step_count >= 3: score += 5
        if proc.has_when_to_use: score += 10
        if proc.has_failure_modes: score += 15
        if proc.has_verification: score += 20

        # Multi-source validation
        if proc.cluster_size >= 5: score += 20
        elif proc.cluster_size >= 3: score += 15
        elif proc.cluster_size > 1: score += 10

        # Core tier bonus
        if proc.tier == "core": score += 25

        scored.append((score, proc))

    scored.sort(key=lambda x: x[0], reverse=True)

    # Use fixed counts instead of percentiles (top 5%, next 25%, rest)
    n = len(scored)
    n_platinum = max(200, int(n * 0.05))  # Top 5% or at least 200
    n_gold = int(n * 0.25)  # Next 25%

    platinum = scored[:n_platinum]
    gold = scored[n_platinum:n_platinum + n_gold]
    silver = scored[n_platinum + n_gold:]

    # Get actual thresholds for reporting
    p_threshold = platinum[-1][0] if platinum else 0
    g_threshold = gold[-1][0] if gold else 0

    print(f"Thresholds: platinum>={p_threshold:.0f}, gold>={g_threshold:.0f}")
    print(f"Platinum: {len(platinum)}, Gold: {len(gold)}, Silver: {len(silver)}")

    # Save stratification
    stratification = {
        "thresholds": {"platinum": p_threshold, "gold": g_threshold},
        "counts": {"platinum": len(platinum), "gold": len(gold), "silver": len(silver)},
        "platinum": [
            {"id": p.id, "name": p.name, "score": round(s, 1), "category": p.category, "description": p.description[:200]}
            for s, p in platinum
        ],
        "gold": [
            {"id": p.id, "name": p.name, "score": round(s, 1), "category": p.category}
            for s, p in gold
        ]
    }

    strat_path = output_dir / "stratification.json"
    with open(strat_path, "w") as f:
        json.dump(stratification, f, indent=2)

    print(f"Stratification saved to: {strat_path}")

    return platinum, gold, silver


def phase3_generate_index(platinum: list, gold: list, silver: list, output_dir: Path):
    """Phase 3: Generate lightweight retrieval index."""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n=== Phase 3: Generating Retrieval Index ===")

    # Build by category
    categories = defaultdict(lambda: {"platinum": [], "gold": []})

    for score, proc in platinum:
        cat = proc.category or "general"
        categories[cat]["platinum"].append({
            "id": proc.id,
            "name": proc.name,
            "summary": proc.description[:150]
        })

    for score, proc in gold:
        cat = proc.category or "general"
        categories[cat]["gold"].append({
            "id": proc.id,
            "name": proc.name,
            "summary": proc.description[:100]
        })

    # Problem -> procedure mapping
    problem_keywords = {
        "negotiat": "negotiation", "conflict": "conflict_resolution",
        "decision": "decision_making", "analyz": "analysis",
        "optimi": "optimization", "learn": "learning",
        "communicat": "communication", "persuad": "persuasion",
        "strateg": "strategy", "plan": "planning",
        "problem": "problem_solving", "creativ": "creativity",
        "risk": "risk_management", "change": "change_management",
        "goal": "goal_setting", "focus": "focus",
        "bias": "cognitive_bias", "reason": "reasoning",
        "meta": "meta_cognition", "system": "systems_thinking",
    }

    problem_mapping = defaultdict(list)
    for score, proc in platinum + gold:
        text = (proc.name + " " + proc.description).lower()
        for kw, problem in problem_keywords.items():
            if kw in text:
                problem_mapping[problem].append({
                    "id": proc.id,
                    "name": proc.name,
                    "tier": "platinum" if score >= 80 else "gold"
                })

    # Dedupe
    for problem in problem_mapping:
        seen = set()
        unique = []
        for p in problem_mapping[problem]:
            if p["id"] not in seen:
                seen.add(p["id"])
                unique.append(p)
        problem_mapping[problem] = unique[:10]

    # Save index
    index = {
        "version": "1.0",
        "summary": {
            "total": len(platinum) + len(gold) + len(silver),
            "platinum": len(platinum),
            "gold": len(gold),
            "silver": len(silver)
        },
        "categories": {k: dict(v) for k, v in categories.items()},
        "problem_to_procedure": dict(problem_mapping)
    }

    index_path = output_dir / "PROCEDURE_INDEX.yaml"
    with open(index_path, "w") as f:
        yaml.dump(index, f, default_flow_style=False, allow_unicode=True)

    print(f"Index saved: {index_path} ({index_path.stat().st_size / 1024:.1f} KB)")

    # Quick reference
    quick_ref = {
        "title": "GOSM Platinum Procedures",
        "procedures": [
            {"name": p.name, "id": p.id, "category": p.category, "summary": p.description[:200]}
            for s, p in platinum[:100]
        ]
    }

    quick_path = output_dir / "PLATINUM_QUICK_REF.yaml"
    with open(quick_path, "w") as f:
        yaml.dump(quick_ref, f, default_flow_style=False, allow_unicode=True)

    print(f"Quick ref saved: {quick_path}")

    return index


def main():
    parser = argparse.ArgumentParser(description="GOSM Library Consolidation")
    parser.add_argument("--phase", type=int, choices=[1, 2, 3])
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--threshold", type=float, default=0.5)
    args = parser.parse_args()

    if not args.phase and not args.all:
        parser.print_help()
        return

    procedures = load_procedures_lightweight(PROCEDURES_DIR)
    if not procedures:
        print("No procedures found!")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    cluster_mapping = None
    clusters = None
    platinum = gold = silver = None

    if args.all or args.phase == 1:
        cluster_mapping, clusters = phase1_analyze_redundancy(procedures, OUTPUT_DIR, args.threshold)

    if args.all or args.phase == 2:
        if cluster_mapping is None:
            mapping_path = OUTPUT_DIR / "cluster_mapping.json"
            if mapping_path.exists():
                with open(mapping_path) as f:
                    cluster_mapping = json.load(f)
            else:
                print("Run phase 1 first")
                return
        platinum, gold, silver = phase2_stratify_quality(procedures, cluster_mapping, OUTPUT_DIR)

    if args.all or args.phase == 3:
        if platinum is None:
            strat_path = OUTPUT_DIR / "stratification.json"
            if strat_path.exists():
                if cluster_mapping is None:
                    mapping_path = OUTPUT_DIR / "cluster_mapping.json"
                    with open(mapping_path) as f:
                        cluster_mapping = json.load(f)
                platinum, gold, silver = phase2_stratify_quality(procedures, cluster_mapping, OUTPUT_DIR)
            else:
                print("Run phase 2 first")
                return
        phase3_generate_index(platinum, gold, silver, OUTPUT_DIR)

    print("\n=== Pipeline Complete ===")


if __name__ == "__main__":
    main()
