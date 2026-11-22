"""FFmpeg/ffprobe CLI wrappers — safe subprocess calls, no shell injection.

All functions use subprocess.run with argument lists (never shell=True).
All handle FileNotFoundError for missing ffmpeg/ffprobe binaries.
All return dicts with status: completed/blocked/error.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


def probe_media(input_path: str | Path) -> dict[str, Any]:
    """Probe media metadata via ffprobe JSON output.

    Returns:
        dict with status, format (duration, bitrate), streams (codec, resolution, fps).
    """
    cmd = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(input_path)]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "ffprobe not found on PATH"}
    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip(), "cmd": cmd}
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"status": "error", "reason": "ffprobe returned invalid JSON"}
    return {"status": "completed", "input": str(input_path), "probe": data}


def trim_video(
    input_path: str | Path,
    output_path: str | Path,
    start: str = "00:00:00",
    end: str | None = None,
    copy: bool = True,
) -> dict[str, Any]:
    """Trim video to a segment. Uses -c copy for lossless by default.

    Args:
        input_path: Source video file.
        output_path: Output file path.
        start: Start time (HH:MM:SS or seconds).
        end: End time (HH:MM:SS or seconds). None = to end.
        copy: If True, use -c copy (no re-encode, fast, lossless).
    """
    cmd = ["ffmpeg", "-i", str(input_path), "-ss", start]
    if end:
        cmd.extend(["-to", end])
    if copy:
        cmd.append("-c")
        cmd.append("copy")
    cmd.append(str(output_path))

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "ffmpeg not found on PATH"}
    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip(), "cmd": cmd}
    out = Path(output_path)
    if not out.exists():
        return {"status": "error", "reason": f"Output not found: {out}"}
    return {"status": "completed", "input": str(input_path), "output": str(out), "size": out.stat().st_size}


def mux_audio(
    video_path: str | Path,
    audio_path: str | Path,
    output_path: str | Path,
) -> dict[str, Any]:
    """Mux video and audio streams into one file via -map.

    Uses -c copy for both streams (no re-encode).
    """
    cmd = [
        "ffmpeg",
        "-i", str(video_path),
        "-i", str(audio_path),
        "-c", "copy",
        "-map", "0:v",
        "-map", "1:a",
        str(output_path),
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "ffmpeg not found on PATH"}
    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip(), "cmd": cmd}
    out = Path(output_path)
    if not out.exists():
        return {"status": "error", "reason": f"Output not found: {out}"}
    return {"status": "completed", "output": str(out), "size": out.stat().st_size}


def transcode_web_mp4(
    input_path: str | Path,
    output_path: str | Path,
    crf: int = 23,
    preset: str = "medium",
) -> dict[str, Any]:
    """Transcode to web-safe MP4 (libx264, yuv420p, aac).

    Args:
        input_path: Source media file.
        output_path: Output MP4 path.
        crf: Quality (18-28, lower = better quality, larger file).
        preset: Encoding speed (ultrafast...veryslow, slower = better compression).
    """
    cmd = [
        "ffmpeg",
        "-i", str(input_path),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", str(crf),
        "-preset", preset,
        "-c:a", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        str(output_path),
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "ffmpeg not found on PATH"}
    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip(), "cmd": cmd}
    out = Path(output_path)
    if not out.exists():
        return {"status": "error", "reason": f"Output not found: {out}"}
    return {
        "status": "completed",
        "input": str(input_path),
        "output": str(out),
        "size": out.stat().st_size,
        "codec": "libx264",
        "pixel_format": "yuv420p",
        "audio_codec": "aac",
        "crf": crf,
        "preset": preset,
    }


__all__ = ["mux_audio", "probe_media", "transcode_web_mp4", "trim_video"]
