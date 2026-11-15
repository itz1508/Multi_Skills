"""Checks for Particle VFX JSON validity."""

from __future__ import annotations

import json
from typing import Any

from agent.skills.particle_vfx.tools.schema import BehaviorType, ShapeType, ValueType


VALID_SHAPE_TYPES = {s.value for s in ShapeType}
VALID_BEHAVIOR_TYPES = {b.value for b in BehaviorType}
VALID_VALUE_TYPES = {v.value for v in ValueType}


def check_shape_type(shape: dict[str, Any]) -> bool:
    """Validate emitter shape has a known type."""
    return isinstance(shape, dict) and shape.get("type") in VALID_SHAPE_TYPES


def check_behavior_type(behavior: dict[str, Any]) -> bool:
    """Validate behavior has a known type."""
    return isinstance(behavior, dict) and behavior.get("type") in VALID_BEHAVIOR_TYPES


def check_value_type(value: dict[str, Any]) -> bool:
    """Validate value function has a known type."""
    return isinstance(value, dict) and value.get("type") in VALID_VALUE_TYPES


def check_particle_emitter(node: dict[str, Any]) -> bool:
    """Validate a ParticleEmitter node has required 'ps' fields."""
    if not isinstance(node, dict):
        return False
    if node.get("type") != "ParticleEmitter":
        return False
    ps = node.get("ps")
    if not isinstance(ps, dict):
        return False
    required = {"shape", "startLife", "startSpeed", "startSize", "emissionOverTime"}
    return required.issubset(ps.keys())


def check_effect_json(json_str: str) -> bool:
    """Validate a complete effect JSON string has required top-level fields."""
    try:
        data = json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return False
    if not isinstance(data, dict):
        return False
    required = {"metadata", "object"}
    if not required.issubset(data.keys()):
        return False
    obj = data.get("object", {})
    if not isinstance(obj, dict):
        return False
    if obj.get("type") not in ("Group", "QuarksPrefab"):
        return False
    children = obj.get("children", [])
    if not isinstance(children, list):
        return False
    return all(check_particle_emitter(c) for c in children if isinstance(c, dict) and c.get("type") == "ParticleEmitter")


def check_uuid_format(uuid_str: str) -> bool:
    """Basic UUID format check."""
    if not isinstance(uuid_str, str):
        return False
    parts = uuid_str.split("-")
    return len(parts) == 5


__all__ = [
    "VALID_BEHAVIOR_TYPES",
    "VALID_SHAPE_TYPES",
    "VALID_VALUE_TYPES",
    "check_behavior_type",
    "check_effect_json",
    "check_particle_emitter",
    "check_shape_type",
    "check_uuid_format",
    "check_value_type",
]
