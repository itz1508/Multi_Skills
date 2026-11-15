"""Particle VFX skill — three.quarks JSON particle effect builder.

Ownership:
    GPU particle effect configuration for Three.js via three.quarks. Builds,
    validates, and exports JSON files compatible with QuarksLoader.parse().
    Uses Pydantic v2 models for type-safe construction. No overlap with
    existing skills — unique 3D particle domain.

Tools:
    quarks_builder — Pydantic models for ParticleSystem, emitter shapes,
        behaviors, value types, QuarksPrefab timeline
    schema — Enum classes for ShapeType, BehaviorType, RenderMode,
        BlendingMode, ValueType

Runtime integration:
    Results via HostDispatchResult (contract vfx_record). Host validates
    JSON structure and required fields.
"""

from agent.skills.particle_vfx.run import post_dispatch, pre_dispatch

__all__ = ["post_dispatch", "pre_dispatch"]
