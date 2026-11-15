"""Motion mode: seek(t) deterministic frame pipeline.

Pipeline: HTML with seek(t) → Playwright captures frames → ffmpeg encodes video.
The seek(t) function must be a pure function of time — no Math.random, setTimeout,
or CSS transitions in render mode.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


def render_frames(
    html_path: Path,
    duration: float,
    fps: int = 60,
    output_dir: Path | None = None,
    width: int = 1920,
    height: int = 1080,
) -> dict[str, Any]:
    """Capture frames from a seek(t) HTML file via Playwright.

    Args:
        html_path: Path to HTML file containing the seek(t) function.
        duration: Video duration in seconds.
        fps: Frames per second (default 60).
        output_dir: Directory for frame PNGs (default: html_path parent / frames).
        width: Viewport width in pixels.
        height: Viewport height in pixels.

    Returns:
        dict with frame count, output dir, and status.
    """
    if output_dir is None:
        output_dir = html_path.parent / "frames"
    output_dir.mkdir(parents=True, exist_ok=True)

    total_frames = int(duration * fps)
    node_script = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const browser = await chromium.launch();
  const page = await browser.newPage({{ viewport: {{ width: {width}, height: {height} }} }});
  await page.goto('file://{html_path.resolve()}');
  for (let i = 0; i < {total_frames}; i++) {{
    await page.evaluate((t) => window.seek(t), [i / {fps}]);
    await page.screenshot({{ path: '{output_dir.resolve()}/frame_' + String(i).padStart(5, '0') + '.png' }});
  }}
  await browser.close();
}})();
"""
    script_path = output_dir / "_render.js"
    script_path.write_text(node_script)

    try:
        result = subprocess.run(
            ["node", str(script_path)],
            capture_output=True,
            text=True,
            timeout=600,
            check=False,
        )
    except FileNotFoundError:
        return {"status": "blocked", "reason": "node not installed", "frame_count": 0}

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip(), "frame_count": 0}

    frame_count = len(list(output_dir.glob("frame_*.png")))
    return {
        "status": "completed",
        "frame_count": frame_count,
        "fps": fps,
        "duration": duration,
        "output_dir": str(output_dir),
    }


def encode_video(
    frames_dir: Path,
    output_path: Path,
    fps: int = 60,
    crf: int = 18,
) -> dict[str, Any]:
    """Encode frame PNGs into a video via ffmpeg.

    Args:
        frames_dir: Directory containing frame_XXXXX.png files.
        output_path: Output video path (e.g., out/video.mp4).
        fps: Frame rate (must match render_fps).
        crf: Constant rate factor (18 = visually lossless, 23 = default).

    Returns:
        dict with output path, file size, and status.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pattern = str(frames_dir / "frame_%05d.png")

    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(fps),
        "-i", pattern,
        "-c:v", "libx264",
        "-crf", str(crf),
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        str(output_path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300, check=False)
    except FileNotFoundError:
        return {"status": "blocked", "reason": "ffmpeg not installed"}

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip()[-500:]}

    size = output_path.stat().st_size if output_path.exists() else 0
    return {
        "status": "completed",
        "output_path": str(output_path),
        "file_size": size,
        "fps": fps,
    }


def check_determinism(
    html_path: Path,
    frame_index: int,
    fps: int = 60,
) -> dict[str, Any]:
    """Render the same frame twice and compare SHA-256 hashes.

    Args:
        html_path: Path to seek(t) HTML file.
        frame_index: Which frame to test (0-based).
        fps: Frame rate.

    Returns:
        dict with hash_a, hash_b, and deterministic (bool).
    """
    t = frame_index / fps
    node_script = f"""
const {{ chromium }} = require('playwright');
const crypto = require('crypto');
const fs = require('fs');
(async () => {{
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://{html_path.resolve()}');
  const screenshots = [];
  for (let run = 0; run < 2; run++) {{
    await page.evaluate((tt) => window.seek(tt), [{t}]);
    const buf = await page.screenshot({{ type: 'png' }});
    screenshots.push(crypto.createHash('sha256').update(buf).digest('hex'));
  }}
  console.log(JSON.stringify({{ a: screenshots[0], b: screenshots[1] }}));
  await browser.close();
}})();
"""
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".js", delete=False, mode="w") as f:
        f.write(node_script)
        script_path = Path(f.name)

    try:
        result = subprocess.run(
            ["node", str(script_path)],
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
    except FileNotFoundError:
        return {"status": "blocked", "reason": "node not installed"}
    finally:
        script_path.unlink(missing_ok=True)

    if result.returncode != 0:
        return {"status": "error", "stderr": result.stderr.strip()}

    data = json.loads(result.stdout.strip())
    return {
        "status": "completed",
        "frame_index": frame_index,
        "hash_a": data["a"],
        "hash_b": data["b"],
        "deterministic": data["a"] == data["b"],
    }


def render_motion(
    html_path: Path,
    duration: float,
    fps: int = 60,
    output_path: Path | None = None,
    width: int = 1920,
    height: int = 1080,
    crf: int = 18,
) -> dict[str, Any]:
    """Full motion pipeline: render frames → encode video → verify determinism.

    Args:
        html_path: Path to seek(t) HTML file.
        duration: Video duration in seconds.
        fps: Frames per second.
        output_path: Output video path.
        width: Viewport width.
        height: Viewport height.
        crf: ffmpeg constant rate factor.

    Returns:
        dict with full pipeline evidence.
    """
    if output_path is None:
        output_path = html_path.parent / "out" / "motion.mp4"

    frames_result = render_frames(html_path, duration, fps, None, width, height)
    if frames_result["status"] != "completed":
        return frames_result

    video_result = encode_video(Path(frames_result["output_dir"]), output_path, fps, crf)
    if video_result["status"] != "completed":
        return video_result

    det_result = check_determinism(html_path, int(fps), fps)

    return {
        "status": "completed",
        "frames": frames_result,
        "video": video_result,
        "determinism": det_result,
        "duration": duration,
        "fps": fps,
        "resolution": f"{width}x{height}",
    }


__all__ = ["check_determinism", "encode_video", "render_frames", "render_motion"]
