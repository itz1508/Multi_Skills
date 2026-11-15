"""Render a Remotion composition to video file.

CRITICAL: Only render when the user is very explicit ("Render the video",
"Export", "Give me the MP4"). Default behavior is preview, not render.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any


def render_video(
    composition_id: str,
    output_path: str | Path,
    project_dir: str | Path,
    codec: str = "h264",
    quality: int = 80,
) -> dict[str, Any]:
    """Render a Remotion composition to a video file.

    Args:
        composition_id: The composition ID from Root.tsx.
        output_path: Output file path (e.g., out/video.mp4).
        project_dir: Remotion project root.
        codec: Video codec (h264, h265, vp8, vp9, gif).
        quality: CRF value (0-100, lower = higher quality).

    Returns:
        dict with status and output file evidence.
    """
    cmd = [
        "npx", "remotion", "render",
        composition_id,
        str(output_path),
        f"--codec={codec}",
        f"--quality={quality}",
    ]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=600, check=False,
            cwd=str(project_dir),
        )
    except FileNotFoundError:
        return {"status": "blocked", "reason": "npx not found — install Node.js >=18"}
    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip(), "cmd": cmd}

    out = Path(output_path)
    if not out.exists():
        return {"status": "error", "reason": f"Output file not found: {out}"}
    return {
        "status": "completed",
        "composition": composition_id,
        "output": str(out),
        "size_bytes": out.stat().st_size,
        "codec": codec,
    }
