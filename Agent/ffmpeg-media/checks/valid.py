"""Checks for FFmpeg Media validity."""

from __future__ import annotations

import shutil
from pathlib import Path


def check_ffmpeg_available() -> bool:
    """Verify ffmpeg is on PATH."""
    return shutil.which("ffmpeg") is not None


def check_ffprobe_available() -> bool:
    """Verify ffprobe is on PATH."""
    return shutil.which("ffprobe") is not None


def check_output_exists(output_path: str | Path) -> bool:
    """Verify output file exists and has size > 0."""
    p = Path(output_path)
    return p.exists() and p.stat().st_size > 0


def check_input_exists(input_path: str | Path) -> bool:
    """Verify input file exists."""
    return Path(input_path).exists()


def check_crf_valid(crf: int) -> bool:
    """Validate CRF value is in acceptable range."""
    return isinstance(crf, int) and 0 <= crf <= 51


def check_duration_valid(duration: str | float) -> bool:
    """Validate duration format (HH:MM:SS string or seconds number)."""
    if isinstance(duration, (int, float)):
        return duration >= 0
    if isinstance(duration, str):
        parts = duration.split(":")
        return all(p.replace(".", "").isdigit() for p in parts) and 1 <= len(parts) <= 3
    return False


__all__ = [
    "check_crf_valid",
    "check_duration_valid",
    "check_ffmpeg_available",
    "check_ffprobe_available",
    "check_input_exists",
    "check_output_exists",
]
