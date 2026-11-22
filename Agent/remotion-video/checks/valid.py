"""Checks for Remotion Video validity."""

from __future__ import annotations

import shutil
from pathlib import Path


def check_npx_available() -> bool:
    """Verify npx is on PATH."""
    return shutil.which("npx") is not None


def check_node_available() -> bool:
    """Verify node is on PATH."""
    return shutil.which("node") is not None


def check_project_exists(project_dir: str | Path) -> bool:
    """Check if a Remotion project exists (has package.json with remotion)."""
    pkg = Path(project_dir) / "package.json"
    if not pkg.exists():
        return False
    try:
        content = pkg.read_text()
        return "remotion" in content
    except Exception:
        return False


def check_output_exists(output_path: str | Path) -> bool:
    """Verify rendered video file exists and has size > 0."""
    p = Path(output_path)
    return p.exists() and p.stat().st_size > 0


def check_composition_id_valid(composition_id: str) -> bool:
    """Validate composition ID format."""
    return isinstance(composition_id, str) and 1 <= len(composition_id.strip()) <= 100


__all__ = [
    "check_composition_id_valid",
    "check_node_available",
    "check_npx_available",
    "check_output_exists",
    "check_project_exists",
]
