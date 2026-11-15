"""Start Remotion Studio preview server.

Studio-first workflow: always start the preview before rendering or editing.
Keep Studio running while working so the user can watch changes in real-time.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any


def start_studio(project_dir: str | Path, open_browser: bool = False) -> dict[str, Any]:
    """Start Remotion Studio dev server.

    Args:
        project_dir: Remotion project root.
        open_browser: If True, opens browser automatically (--no-open omitted).
                      If False, prints URL for in-app browser.

    Returns:
        dict with status and server URL (from stdout).
    """
    cmd = ["npx", "remotion", "studio"]
    if not open_browser:
        cmd.append("--no-open")

    try:
        # Studio is a long-running process — capture initial output
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=10, check=False,
            cwd=str(project_dir),
        )
    except FileNotFoundError:
        return {"status": "blocked", "reason": "npx not found — install Node.js >=18"}
    except subprocess.TimeoutExpired:
        # Expected: Studio runs indefinitely. Timeout means it started.
        return {
            "status": "completed",
            "project": str(project_dir),
            "note": "Studio started as long-running process. Check terminal for URL.",
        }
    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip(), "cmd": cmd}
    return {
        "status": "completed",
        "project": str(project_dir),
        "stdout": result.stdout.strip()[:500],
    }
