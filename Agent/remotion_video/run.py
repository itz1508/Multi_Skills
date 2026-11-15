"""Remotion Video skill entry point.

Run: uv run --no-sync python -m agent.skills.remotion_video.run <repository-root>
npx: npx create-video@latest --yes --blank --no-tailwind .
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from agent.contracts.host import HostDispatchEnvelope, HostDispatchResult


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m agent.skills.remotion_video.run <repository-root>")
        sys.exit(1)
    repo_root = Path(sys.argv[1])
    if not repo_root.exists():
        print(f"Repository root not found: {repo_root}")
        sys.exit(1)
    print("Remotion Video skill — programmatic video via React + npx")
    print(f"Repository root: {repo_root}")
    has_npx = shutil.which("npx") is not None
    has_node = shutil.which("node") is not None
    print(f"Node.js: {'found' if has_node else 'NOT FOUND'}")
    print(f"npx: {'found' if has_npx else 'NOT FOUND'}")
    if not has_npx:
        print("Install Node.js >=18 to use this skill")
    print("Scaffold: npx create-video@latest --yes --blank --no-tailwind .")
    print("Preview: npx remotion studio --no-open")
    print("Render: npx remotion render <composition-id> <output.mp4>")


def pre_dispatch(request: HostDispatchEnvelope) -> HostDispatchEnvelope:
    """Validate before Remotion operations."""
    if request.stage not in ("build", "research", "planning"):
        raise ValueError(f"Remotion Video stage must be build/research/planning, got '{request.stage}'")
    if request.requester_role not in ("host", "remotion_video", "builder"):
        raise ValueError(f"Unauthorized role '{request.requester_role}' for remotion video")
    enriched = request.model_copy(
        update={
            "information_needed": (
                request.information_needed + " | video_scope: remotion_scaffold_studio_render"
            )
        }
    )
    return enriched


def post_dispatch(result: HostDispatchResult) -> HostDispatchResult:
    """Verify remotion video result."""
    if not result.output_ref.artifact_id:
        raise ValueError("Remotion result must reference output artifact")
    if result.output_ref.contract_id not in ("video_record", "build_record"):
        raise ValueError(
            f"Remotion output contract must be video_record/build_record, got '{result.output_ref.contract_id}'"
        )
    return result


__all__ = ["main", "post_dispatch", "pre_dispatch"]
