"""Caption tools: WhisperX word-level transcription and SRT formatting.

Uses WhisperX for word-level timing alignment, then formats to SRT
for subtitle delivery.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


def transcribe(
    audio_path: Path,
    model: str = "large-v3",
    language: str | None = None,
    output_dir: Path | None = None,
) -> dict[str, Any]:
    """Transcribe audio with word-level timing via WhisperX.

    Args:
        audio_path: Path to audio file.
        model: WhisperX model size (tiny, base, small, medium, large-v3).
        language: Language code (e.g., 'en', 'es'). Auto-detect if None.
        output_dir: Directory for output files (default: audio_path parent).

    Returns:
        dict with word-level segments, SRT path, and JSON path.
    """
    if output_dir is None:
        output_dir = audio_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    base_name = audio_path.stem
    srt_path = output_dir / f"{base_name}.srt"
    json_path = output_dir / f"{base_name}.json"

    script = f"""
import json, whisperx
model = whisperx.load_model("{model}", device="cpu")
audio = whisperx.load_audio("{audio_path}")
result = model.transcribe(audio)
align_model, meta = whisperx.load_align_model(language_code="{language or 'en'}", device="cpu")
aligned = whisperx.align(result["segments"], align_model, meta, audio, device="cpu")
output = {{"segments": aligned["segments"], "language": "{language or 'en'}"}}
print(json.dumps(output, default=str))
"""
    try:
        result = subprocess.run(
            ["python", "-c", script],
            capture_output=True,
            text=True,
            timeout=600,
            check=False,
        )
    except FileNotFoundError:
        return {"status": "blocked", "reason": "python not available"}

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip()[-500:]}

    try:
        data = json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        return {"status": "error", "reason": "Failed to parse WhisperX output"}

    json_path.write_text(json.dumps(data, indent=2, default=str))
    srt_text = format_srt(data)
    srt_path.write_text(srt_text)

    word_count = sum(
        len(seg.get("words", [])) for seg in data.get("segments", [])
    )
    return {
        "status": "completed",
        "srt_path": str(srt_path),
        "json_path": str(json_path),
        "word_count": word_count,
        "language": data.get("language", language or "en"),
    }


def format_srt(transcription: dict[str, Any]) -> str:
    """Format transcription dict to SRT subtitle format.

    Args:
        transcription: WhisperX output with segments containing word-level timing.

    Returns:
        SRT-formatted string.
    """
    lines: list[str] = []
    idx = 1
    for seg in transcription.get("segments", []):
        start = seg.get("start", 0)
        end = seg.get("end", 0)
        text = seg.get("text", "").strip()
        if not text:
            continue
        lines.append(str(idx))
        lines.append(f"{_srt_time(start)} --> {_srt_time(end)}")
        lines.append(text)
        lines.append("")
        idx += 1
    return "\n".join(lines)


def _srt_time(seconds: float) -> str:
    """Convert seconds to SRT time format (HH:MM:SS,mmm)."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def sync_captions(
    beats: list[float],
    transcription: dict[str, Any],
) -> dict[str, Any]:
    """Align caption segments to nearest beat times.

    Args:
        beats: List of beat times in seconds.
        transcription: WhisperX output with segments.

    Returns:
        dict with aligned caption-beat pairs.
    """
    if not beats:
        return {"status": "blocked", "reason": "No beats provided"}

    segments = transcription.get("segments", [])
    aligned: list[dict[str, Any]] = []
    for seg in segments:
        start = seg.get("start", 0)
        nearest_beat = min(beats, key=lambda b: abs(b - start))
        aligned.append({
            "text": seg.get("text", "").strip(),
            "caption_start": start,
            "nearest_beat": nearest_beat,
            "offset": nearest_beat - start,
        })

    return {
        "status": "completed",
        "aligned_count": len(aligned),
        "segments": aligned,
    }


__all__ = ["format_srt", "sync_captions", "transcribe"]
