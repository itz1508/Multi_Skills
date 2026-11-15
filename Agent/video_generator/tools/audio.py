"""Audio tools: beat detection, sound effects, audio synthesis.

Tools: librosa for beat detection, Openverse API for free sound effects,
and basic tone synthesis for SFX.
"""

from __future__ import annotations

import json
import subprocess
import urllib.parse
from pathlib import Path
from typing import Any


def detect_beats(
    audio_path: Path,
    output_json: Path | None = None,
) -> dict[str, Any]:
    """Detect beats, tempo, and downbeats via librosa.

    Args:
        audio_path: Path to audio file (wav, mp3, etc.).
        output_json: Output path for beats.json (default: audio_path parent).

    Returns:
        dict with bpm, beat times, downbeat times, and hit times.
    """
    if output_json is None:
        output_json = audio_path.parent / "beats.json"

    script = f"""
import json, librosa
y, sr = librosa.load("{audio_path}", sr=None)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beats, sr=sr).tolist()
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
onsets = librosa.onset.onset_detect(y=y, sr=sr)
hit_times = librosa.frames_to_time(onsets, sr=sr).tolist()
print(json.dumps({{
    "bpm": float(tempo),
    "beats": beat_times,
    "downbeats": beat_times[::4] if beat_times else [],
    "hits": hit_times,
}}))
"""
    try:
        result = subprocess.run(
            ["python", "-c", script],
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
    except FileNotFoundError:
        return {"status": "blocked", "reason": "python not available"}

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip()[-500:]}

    try:
        data = json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        return {"status": "error", "reason": "Failed to parse librosa output"}

    output_json.write_text(json.dumps(data, indent=2))
    data["output"] = str(output_json)
    data["status"] = "completed"
    return data


def get_sfx(
    query: str,
    api_key: str | None = None,
    limit: int = 10,
) -> dict[str, Any]:
    """Search Openverse API for free sound effects.

    Args:
        query: Search term (e.g., "whoosh", "click", "explosion").
        api_key: Openverse API token (optional for basic search).
        limit: Max results.

    Returns:
        dict with sound effect URLs, titles, and licenses.
    """
    base_url = "https://api.openverse.org/v1/audio/"
    params = urllib.parse.urlencode({"q": query, "page_size": str(limit)})
    url = f"{base_url}?{params}"

    import urllib.request
    headers = {"Accept": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"status": "blocked", "reason": f"Openverse API error: {e}"}

    results = [
        {
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "license": item.get("license", ""),
            "source": item.get("source", ""),
        }
        for item in data.get("results", [])[:limit]
    ]
    return {
        "status": "completed",
        "query": query,
        "count": len(results),
        "results": results,
    }


def synthesize_tone(
    freq: float = 440.0,
    duration: float = 0.1,
    output_path: Path | None = None,
    sr: int = 44100,
) -> dict[str, Any]:
    """Synthesize a simple sine wave tone for SFX.

    Args:
        freq: Frequency in Hz.
        duration: Duration in seconds.
        output_path: Output wav file path.
        sr: Sample rate.

    Returns:
        dict with output path and status.
    """
    if output_path is None:
        output_path = Path("sfx_tone.wav")

    script = f"""
import numpy as np, soundfile as sf
sr = {sr}
t = np.linspace(0, {duration}, int(sr * {duration}), endpoint=False)
wave = 0.3 * np.sin(2 * np.pi * {freq} * t)
sf.write("{output_path}", wave, sr)
print("ok")
"""
    try:
        result = subprocess.run(
            ["python", "-c", script],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except FileNotFoundError:
        return {"status": "blocked", "reason": "python not available"}

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip()[-300:]}

    return {
        "status": "completed",
        "output_path": str(output_path),
        "freq": freq,
        "duration": duration,
    }


__all__ = ["detect_beats", "get_sfx", "synthesize_tone"]
