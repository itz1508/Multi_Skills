"""Scaffold a new Remotion project via npx create-video."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any


def scaffold_project(target_dir: str | Path, blank: bool = True, no_tailwind: bool = True) -> dict[str, Any]:
    """Create a new Remotion project.

    Args:
        target_dir: Directory to scaffold into. Empty or "." for current.
        blank: Use --blank for minimal project (no template).
        no_tailwind: Skip Tailwind CSS setup.

    Returns:
        dict with status and scaffold evidence.
    """
    cmd = ["npx", "create-video@latest", "--yes"]
    if blank:
        cmd.append("--blank")
    if no_tailwind:
        cmd.append("--no-tailwind")
    cmd.append(str(target_dir))

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "npx not found — install Node.js >=18"}
    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip(), "cmd": cmd}
    return {
        "status": "completed",
        "target": str(target_dir),
        "stdout": result.stdout.strip()[:500],
    }
