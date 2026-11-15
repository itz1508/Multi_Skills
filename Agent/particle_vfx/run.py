"""Particle VFX skill entry point.

Run: uv run --no-sync python -m agent.skills.particle_vfx.run <repository-root>
Usage: Build JSON particle configs via quarks_builder, load with QuarksLoader.parse()
"""

from __future__ import annotations

import sys
from pathlib import Path

from agent.contracts.host import HostDispatchEnvelope, HostDispatchResult


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m agent.skills.particle_vfx.run <repository-root>")
        sys.exit(1)
    repo_root = Path(sys.argv[1])
    if not repo_root.exists():
        print(f"Repository root not found: {repo_root}")
        sys.exit(1)
    print("Particle VFX skill — three.quarks JSON particle effect builder")
    print(f"Repository root: {repo_root}")
    print("Shapes: point, cone, sphere, hemisphere, donut, circle, grid, rectangle, mesh_surface")
    print("Behaviors: SizeOverLife, ColorOverLife, SpeedOverLife, ForceOverLife, ...")
    print("Value types: ConstantValue, ConstantColor, IntervalValue, PiecewiseBezier, Gradient")
    print("Export: quarks_builder.build_effect(...) -> JSON compatible with QuarksLoader.parse()")


def pre_dispatch(request: HostDispatchEnvelope) -> HostDispatchEnvelope:
    """Validate before particle VFX operations."""
    if request.stage not in ("build", "research", "planning"):
        raise ValueError(f"Particle VFX stage must be build/research/planning, got '{request.stage}'")
    if request.requester_role not in ("host", "particle_vfx", "builder"):
        raise ValueError(f"Unauthorized role '{request.requester_role}' for particle vfx")
    enriched = request.model_copy(
        update={
            "information_needed": (
                request.information_needed + " | vfx_scope: quarks_json_emitter_shapes_behaviors"
            )
        }
    )
    return enriched


def post_dispatch(result: HostDispatchResult) -> HostDispatchResult:
    """Verify particle VFX result."""
    if not result.output_ref.artifact_id:
        raise ValueError("Particle VFX result must reference output artifact")
    if result.output_ref.contract_id not in ("vfx_record", "build_record"):
        raise ValueError(
            f"Particle VFX output contract must be vfx_record/build_record, got '{result.output_ref.contract_id}'"
        )
    return result


__all__ = ["main", "post_dispatch", "pre_dispatch"]
