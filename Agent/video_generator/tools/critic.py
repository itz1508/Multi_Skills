"""Critic tools: contact sheet generation and frame evaluation.

Generates contact sheets via ffmpeg for visual inspection, phone-test
scaling, and determinism verification. Used in the self-evaluation loop
between motion pipeline gates.
"""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path
from typing import Any


def contact_sheet(
    video_path: Path,
    output_path: Path | None = None,
    fps: int = 2,
    cols: int = 6,
    width: int = 1920,
) -> dict[str, Any]:
    """Generate a contact sheet from a video via ffmpeg.

    Args:
        video_path: Path to input video.
        output_path: Output PNG path (default: video_path parent / contact_sheet.png).
        fps: Frames per second to sample (default 2 = one frame every 0.5s).
        cols: Number of columns in the sheet.
        width: Tile width in pixels.

    Returns:
        dict with output path, tile count, and status.
    """
    if output_path is None:
        output_path = video_path.parent / "contact_sheet.png"

    # ffmpeg filter: sample frames, tile them into a grid
    # Calculate rows from video duration (tile=Wx0 fails silently in ffmpeg 6.x)
    import math
    try:
        dur_result = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(video_path)],
            capture_output=True, text=True, timeout=10, check=False,
        )
        duration = float(dur_result.stdout.strip()) if dur_result.returncode == 0 else 10.0
    except (ValueError, FileNotFoundError):
        duration = 10.0
    frame_count = max(1, math.ceil(duration * fps))
    tile_rows = max(1, math.ceil(frame_count / cols))
    filter_str = (
        f"fps={fps},"
        f"scale={width}:-1,"
        f"tile={cols}x{tile_rows}"
    )
    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path),
        "-vf", filter_str,
        "-frames:v", "1",
        str(output_path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "ffmpeg not installed"}

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip()[-500:]}

    size = output_path.stat().st_size if output_path.exists() else 0
    return {
        "status": "completed",
        "output_path": str(output_path),
        "file_size": size,
        "sample_fps": fps,
        "cols": cols,
    }


def phone_test(
    video_path: Path,
    output_path: Path | None = None,
    target_width: int = 360,
) -> dict[str, Any]:
    """Scale video frames to phone width for readability testing.

    Args:
        video_path: Path to input video.
        output_path: Output video path (default: video_path parent / phone_test.mp4).
        target_width: Target width in pixels (default 360).

    Returns:
        dict with output path and status.
    """
    if output_path is None:
        output_path = video_path.parent / "phone_test.mp4"

    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path),
        "-vf", f"scale={target_width}:-2",
        "-c:v", "libx264",
        "-crf", "23",
        "-pix_fmt", "yuv420p",
        str(output_path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "ffmpeg not installed"}

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip()[-500:]}

    return {
        "status": "completed",
        "output_path": str(output_path),
        "target_width": target_width,
    }


def loop_check(
    video_path: Path,
    output_path: Path | None = None,
) -> dict[str, Any]:
    """Concatenate the video twice to check loop seamlessness.

    Args:
        video_path: Path to input video.
        output_path: Output path for the doubled video.

    Returns:
        dict with output path and status.
    """
    if output_path is None:
        output_path = video_path.parent / "loop_check.mp4"

    # Create a concat list
    list_path = video_path.parent / "_concat.txt"
    list_path.write_text(f"file '{video_path}'\nfile '{video_path}'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(list_path),
        "-c", "copy",
        str(output_path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "ffmpeg not installed"}
    finally:
        list_path.unlink(missing_ok=True)

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip()[-500:]}

    return {
        "status": "completed",
        "output_path": str(output_path),
    }


def extract_strip(
    video_path: Path,
    start_time: float,
    duration: float = 0.2,
    output_path: Path | None = None,
) -> dict[str, Any]:
    """Extract 12 consecutive frames around the fastest move for motion inspection.

    Args:
        video_path: Path to input video.
        start_time: Start time in seconds.
        duration: Duration to capture in seconds.
        output_path: Output strip image path.

    Returns:
        dict with output path and status.
    """
    if output_path is None:
        output_path = video_path.parent / "motion_strip.png"

    cmd = [
        "ffmpeg", "-y",
        "-ss", str(start_time),
        "-i", str(video_path),
        "-t", str(duration),
        "-vf", "tile=12x1",
        "-frames:v", "1",
        str(output_path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "ffmpeg not installed"}

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip()[-500:]}

    return {
        "status": "completed",
        "output_path": str(output_path),
        "start_time": start_time,
        "duration": duration,
    }


CRITERIA = [
    "hook_in_2s",
    "phone_readability",
    "motion_quality",
    "variety",
    "sound_sync",
    "brand_accuracy",
]


def score_criteria(
    contact_sheet_path: Path,
    scores: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Validate critic scores against criteria. Returns structured evaluation.

    Args:
        contact_sheet_path: Path to the contact sheet image (for evidence).
        scores: Dict of criterion -> score (1-10). If None, returns template.

    Returns:
        dict with scores, worst 3 defects, and pass/fail status.
    """
    if scores is None:
        return {
            "status": "template",
            "criteria": CRITERIA,
            "instructions": "Score each criterion 1-10, then pass scores dict.",
        }

    # Validate all criteria are scored
    missing = [c for c in CRITERIA if c not in scores]
    if missing:
        return {"status": "error", "reason": f"Missing scores for: {missing}"}

    # Validate score range
    for k, v in scores.items():
        if not isinstance(v, int) or not 1 <= v <= 10:
            return {"status": "error", "reason": f"Score for {k} must be 1-10, got {v}"}

    # Identify worst 3
    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    worst_3 = sorted_scores[:3]
    all_pass = all(v >= 8 for v in scores.values())

    return {
        "status": "completed",
        "scores": scores,
        "worst_3": worst_3,
        "all_pass": all_pass,
        "evidence": str(contact_sheet_path) if contact_sheet_path.exists() else None,
    }


__all__ = ["CRITERIA", "contact_sheet", "extract_strip", "loop_check", "phone_test", "score_criteria"]
