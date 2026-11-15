"""FFmpeg Media skill entry point.

Run: uv run --no-sync python -m agent.skills.ffmpeg_media.run <repository-root>
CLI: ffmpeg -i input.mp4 -c:v libx264 -pix_fmt yuv420p -c:a aac output.mp4
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from agent.contracts.host import HostDispatchEnvelope, HostDispatchResult


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m agent.skills.ffmpeg_media.run <repository-root>")
        sys.exit(1)
    repo_root = Path(sys.argv[1])
    if not repo_root.exists():
        print(f"Repository root not found: {repo_root}")
        sys.exit(1)
    print("FFmpeg Media skill — multimedia processing via ffmpeg/ffprobe")
    print(f"Repository root: {repo_root}")
    has_ffmpeg = shutil.which("ffmpeg") is not None
    has_ffprobe = shutil.which("ffprobe") is not None
    print(f"ffmpeg: {'found' if has_ffmpeg else 'NOT FOUND'}")
    print(f"ffprobe: {'found' if has_ffprobe else 'NOT FOUND'}")
    if not has_ffmpeg:
        print("Install ffmpeg: apt install ffmpeg | brew install ffmpeg")
    print("Probe: ffprobe -v quiet -print_format json -show_format -show_streams <input>")
    print("Trim: ffmpeg -i <input> -ss 00:01:00 -to 00:02:00 -c copy <output>")
    print("Transcode: ffmpeg -i <input> -c:v libx264 -pix_fmt yuv420p -c:a aac <output>")


def pre_dispatch(request: HostDispatchEnvelope) -> HostDispatchEnvelope:
    """Validate before ffmpeg operations."""
    if request.stage not in ("build", "research", "planning"):
        raise ValueError(f"FFmpeg Media stage must be build/research/planning, got '{request.stage}'")
    if request.requester_role not in ("host", "ffmpeg_media", "builder"):
        raise ValueError(f"Unauthorized role '{request.requester_role}' for ffmpeg media")
    enriched = request.model_copy(
        update={
            "information_needed": (
                request.information_needed + " | media_scope: ffmpeg_probe_trim_mux_transcode"
            )
        }
    )
    return enriched


def post_dispatch(result: HostDispatchResult) -> HostDispatchResult:
    """Verify ffmpeg media result."""
    if not result.output_ref.artifact_id:
        raise ValueError("FFmpeg result must reference output artifact")
    if result.output_ref.contract_id not in ("media_record", "video_record", "build_record"):
        raise ValueError(
            f"FFmpeg output contract must be media_record/video_record/build_record, got '{result.output_ref.contract_id}'"
        )
    return result


__all__ = ["main", "post_dispatch", "pre_dispatch"]
