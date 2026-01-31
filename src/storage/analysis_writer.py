"""
Analysis writer — saves structured non-tree output as JSON.

For skills that produce tables, lists, matrices, causal chains, etc.
(e.g., /cba, /rca, /se, /dd, /fia, /swa). Each skill's output keeps its
natural shape inside the "output" field.

Required envelope fields: session_id, skill, skill_family, input, timestamp, output.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .index_db import get_family


REQUIRED_ENVELOPE = {"session_id", "skill", "skill_family", "input", "timestamp", "output"}


def validate_envelope(data: Dict[str, Any]) -> List[str]:
    """Validate that analysis JSON has the required envelope fields.
    Returns list of missing fields (empty = valid).
    """
    return [f for f in REQUIRED_ENVELOPE if f not in data]


class AnalysisWriter:
    """Writes analysis.json files with validated envelope schema."""

    @staticmethod
    def build_envelope(
        session_id: str,
        skill: str,
        input_text: str,
        output: Dict[str, Any],
        parameters: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Build a validated analysis envelope."""
        return {
            "session_id": session_id,
            "skill": skill,
            "skill_family": get_family(skill),
            "input": input_text,
            "timestamp": datetime.now().isoformat(),
            "parameters": parameters or {},
            "output": output,
            "tags": tags or [],
        }

    @staticmethod
    def save(session_dir: str, data: Dict[str, Any]) -> Path:
        """Save analysis.json to a session directory.

        Validates the envelope before writing. Raises ValueError if invalid.
        """
        missing = validate_envelope(data)
        if missing:
            raise ValueError(f"Analysis envelope missing fields: {missing}")

        path = Path(session_dir) / "analysis.json"
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return path

    @staticmethod
    def load(session_dir: str) -> Optional[Dict[str, Any]]:
        """Load analysis.json from a session directory."""
        path = Path(session_dir) / "analysis.json"
        if not path.exists():
            return None
        with open(path) as f:
            return json.load(f)
