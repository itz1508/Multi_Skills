"""Pydantic v2 models for three.quarks particle effect JSON.

Builds JSON compatible with QuarksLoader.parse() — Three.js ObjectLoader format
with metadata, geometries, materials, textures, images, and object tree containing
ParticleEmitter nodes with 'ps' (particle system) configuration.

Verified against three.quarks test/JsonFiles.ts and src/QuarksLoader.ts.
"""

from __future__ import annotations

import json
import uuid
from typing import Any

from pydantic import BaseModel, Field

from agent.skills.particle_vfx.tools.schema import (
    BehaviorType,
    BlendingMode,
    RenderMode,
    ShapeType,
    ValueType,
)


def _uuid() -> str:
    return str(uuid.uuid4())


# ─── Value Functions ───

class ConstantValue(BaseModel):
    """Single constant value."""
    type: str = Field(default=ValueType.CONSTANT_VALUE.value)
    value: float


class ConstantColor(BaseModel):
    """Single constant RGBA color."""
    type: str = Field(default=ValueType.CONSTANT_COLOR.value)
    color: dict[str, float] = Field(default_factory=lambda: {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0})


class IntervalValue(BaseModel):
    """Random value between min and max."""
    type: str = Field(default=ValueType.INTERVAL_VALUE.value)
    a: float = 0.0
    b: float = 1.0


# ─── Emitter Shapes ───

class PointShape(BaseModel):
    type: str = Field(default=ShapeType.POINT.value)
    radius: float = 0.0


class ConeShape(BaseModel):
    type: str = Field(default=ShapeType.CONE.value)
    radius: float = 10.0
    arc: float = 6.283185307179586
    thickness: float = 1.0
    angle: float = 0.5235987755982988


class SphereShape(BaseModel):
    type: str = Field(default=ShapeType.SPHERE.value)
    radius: float = 10.0
    arc: float = 6.283185307179586
    thickness: float = 1.0
    mode: int = 0
    spread: float = 0.0
    speed: dict[str, Any] | None = None


class MeshSurfaceShape(BaseModel):
    type: str = Field(default=ShapeType.MESH_SURFACE.value)
    geometry: str  # uuid reference to geometry in geometries array


# ─── Behaviors ───

class Behavior(BaseModel):
    """Base behavior — type field identifies the behavior."""
    type: str  # BehaviorType value


class EmitSubParticleSystemBehavior(Behavior):
    type: str = Field(default=BehaviorType.EMIT_SUB_PARTICLE_SYSTEM.value)
    sub_particle_system: str  # uuid of sub-emitter
    use_velocity_as_basis: bool = False


# ─── Particle System Config (the 'ps' object) ───

class ParticleSystemConfig(BaseModel):
    """Particle system configuration — the 'ps' field on a ParticleEmitter node."""
    version: str = "3.0"
    auto_destroy: bool = False
    looping: bool = True
    prewarm: bool = False
    duration: float = 5.0
    max_particle: int = 10000
    shape: dict[str, Any] = Field(default_factory=lambda: ConeShape().model_dump())
    start_life: dict[str, Any] = Field(default_factory=lambda: ConstantValue(value=5).model_dump())
    start_speed: dict[str, Any] = Field(default_factory=lambda: ConstantValue(value=10).model_dump())
    start_rotation: dict[str, Any] = Field(default_factory=lambda: ConstantValue(value=0).model_dump())
    start_size: dict[str, Any] = Field(default_factory=lambda: ConstantValue(value=1).model_dump())
    start_color: dict[str, Any] = Field(default_factory=lambda: ConstantColor().model_dump())
    emission_over_time: dict[str, Any] = Field(default_factory=lambda: ConstantValue(value=10).model_dump())
    emission_over_distance: dict[str, Any] = Field(default_factory=lambda: ConstantValue(value=0).model_dump())
    emission_bursts: list = Field(default_factory=list)
    only_used_by_other: bool = False
    instancing_geometry: str  # uuid of instancing geometry
    render_order: int = 0
    render_mode: int = Field(default=RenderMode.BILLBOARD)
    renderer_emitter_settings: dict[str, Any] = Field(default_factory=dict)
    speed_factor: float = 0
    texture: str  # uuid of texture
    start_tile_index: dict[str, Any] = Field(default_factory=lambda: ConstantValue(value=0).model_dump())
    u_tile_count: int = 1
    v_tile_count: int = 1
    blend_tiles: bool = False
    soft_particles: bool = False
    soft_far_fade: float = 0
    soft_near_fade: float = 0
    blending: int = Field(default=BlendingMode.ADDITIVE)
    behaviors: list[dict[str, Any]] = Field(default_factory=list)
    world_space: bool = False


# ─── Three.js ObjectLoader Compatible Nodes ───

class ParticleEmitterNode(BaseModel):
    """A ParticleEmitter node in the Three.js object tree."""
    uuid: str = Field(default_factory=_uuid)
    type: str = "ParticleEmitter"
    name: str = ""
    layers: int = 1
    matrix: list[float] = Field(default_factory=lambda: [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1])
    ps: ParticleSystemConfig


class QuarksPrefabNode(BaseModel):
    """A QuarksPrefab node — unified timeline for Three.js + particle animations."""
    uuid: str = Field(default_factory=_uuid)
    type: str = "QuarksPrefab"
    layers: int = 1
    matrix: list[float] = Field(default_factory=lambda: [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1])
    children: list[dict[str, Any]] = Field(default_factory=list)
    animation_data: list[dict[str, Any]] = Field(default_factory=list)


class AnimationDataEntry(BaseModel):
    """An entry in the QuarksPrefab animationData timeline."""
    start_time: float = 0
    duration: float = 1
    type: str = "ps"  # "ps" or "three"
    target_uuid: str
    clip_uuid: str | None = None
    loop: bool = False


# ─── Geometry / Material / Texture helpers ───

class PlaneGeometry(BaseModel):
    uuid: str = Field(default_factory=_uuid)
    type: str = "PlaneGeometry"
    width: float = 1
    height: float = 1
    width_segments: int = 1
    height_segments: int = 1


class MeshBasicMaterial(BaseModel):
    uuid: str = Field(default_factory=_uuid)
    type: str = "MeshBasicMaterial"
    color: int = 16777215


class TextureRef(BaseModel):
    uuid: str = Field(default_factory=_uuid)
    name: str = "./textures/texture1.png"
    image: str  # uuid of image
    mapping: int = 300
    repeat: list[float] = Field(default_factory=lambda: [1, 1])
    offset: list[float] = Field(default_factory=lambda: [0, 0])
    wrap: list[int] = Field(default_factory=lambda: [1001, 1001])
    format: int = 1023


class ImageRef(BaseModel):
    uuid: str = Field(default_factory=_uuid)
    url: str = ""


# ─── Top-Level Effect Document ───

class QuarksEffect(BaseModel):
    """Top-level three.quarks effect document — Three.js ObjectLoader compatible."""
    metadata: dict[str, Any] = Field(default_factory=lambda: {
        "version": 4.6,
        "type": "Object",
        "generator": "Object3D.toJSON",
    })
    geometries: list[dict[str, Any]] = Field(default_factory=list)
    materials: list[dict[str, Any]] = Field(default_factory=list)
    textures: list[dict[str, Any]] = Field(default_factory=list)
    images: list[dict[str, Any]] = Field(default_factory=list)
    object: dict[str, Any] = Field(default_factory=lambda: {
        "type": "Group",
        "uuid": _uuid(),
        "layers": 1,
        "matrix": [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1],
        "children": [],
    })

    def to_json(self) -> str:
        """Export to JSON string compatible with QuarksLoader.parse()."""
        return json.dumps(self.model_dump(), indent=2)

    def to_dict(self) -> dict[str, Any]:
        """Export to dict."""
        return self.model_dump()


# ─── Builder Factory Functions ───

def build_simple_effect(
    shape: dict[str, Any] | None = None,
    start_life: float = 5,
    start_speed: float = 10,
    start_size: float = 1,
    emission_rate: float = 10,
    duration: float = 5,
    looping: bool = True,
    world_space: bool = False,
    texture_uuid: str | None = None,
    geometry_uuid: str | None = None,
) -> QuarksEffect:
    """Build a simple single-emitter particle effect.

    Args:
        shape: Emitter shape config dict (use ConeShape, SphereShape, etc.)
        start_life: Particle lifetime in seconds
        start_speed: Initial particle speed
        start_size: Initial particle size
        emission_rate: Emission rate per second
        duration: System duration in seconds
        looping: Whether the system loops
        world_space: Whether particles live in world space
        texture_uuid: UUID of texture (must be in textures array)
        geometry_uuid: UUID of instancing geometry (must be in geometries array)

    Returns:
        QuarksEffect ready to export as JSON for QuarksLoader.parse().
    """
    geo_uuid = geometry_uuid or _uuid()
    tex_uuid = texture_uuid or _uuid()

    geometry = PlaneGeometry(uuid=geo_uuid)
    image = ImageRef()
    texture = TextureRef(uuid=tex_uuid, image=image.uuid)

    ps_config = ParticleSystemConfig(
        duration=duration,
        looping=looping,
        world_space=world_space,
        shape=shape or ConeShape().model_dump(),
        start_life=ConstantValue(value=start_life).model_dump(),
        start_speed=ConstantValue(value=start_speed).model_dump(),
        start_size=ConstantValue(value=start_size).model_dump(),
        emission_over_time=ConstantValue(value=emission_rate).model_dump(),
        instancing_geometry=geo_uuid,
        texture=tex_uuid,
    )

    emitter = ParticleEmitterNode(ps=ps_config)

    effect = QuarksEffect(
        geometries=[geometry.model_dump()],
        textures=[texture.model_dump()],
        images=[image.model_dump()],
    )
    effect.object["children"] = [emitter.model_dump()]

    return effect


def build_prefab_effect(
    emitters: list[ParticleEmitterNode],
    animation_entries: list[AnimationDataEntry] | None = None,
    geometries: list[dict[str, Any]] | None = None,
    materials: list[dict[str, Any]] | None = None,
    textures: list[dict[str, Any]] | None = None,
    images: list[dict[str, Any]] | None = None,
) -> QuarksEffect:
    """Build a QuarksPrefab effect with timeline.

    Args:
        emitters: List of ParticleEmitterNode objects.
        animation_entries: Timeline entries mixing 'ps' and 'three' animations.
        geometries: Geometry definitions.
        materials: Material definitions.
        textures: Texture definitions.
        images: Image definitions.

    Returns:
        QuarksEffect with QuarksPrefab root node.
    """
    children = [e.model_dump() for e in emitters]
    anim_data = [a.model_dump() for a in (animation_entries or [])]

    prefab = QuarksPrefabNode(
        children=children,
        animation_data=anim_data,
    )

    effect = QuarksEffect(
        geometries=geometries or [],
        materials=materials or [],
        textures=textures or [],
        images=images or [],
    )
    effect.object = prefab.model_dump()

    return effect


__all__ = [
    "AnimationDataEntry",
    "Behavior",
    "ConstantColor",
    "ConstantValue",
    "ConeShape",
    "EmitSubParticleSystemBehavior",
    "ImageRef",
    "IntervalValue",
    "MeshBasicMaterial",
    "MeshSurfaceShape",
    "ParticleEmitterNode",
    "ParticleSystemConfig",
    "PlaneGeometry",
    "PointShape",
    "QuarksEffect",
    "QuarksPrefabNode",
    "SphereShape",
    "TextureRef",
    "build_prefab_effect",
    "build_simple_effect",
]
