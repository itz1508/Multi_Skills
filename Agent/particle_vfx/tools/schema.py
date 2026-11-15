"""Enum classes for three.quarks JSON schema.

All values verified from three.quarks source code:
- quarks.core/src/shape/ — 9 emitter shapes
- quarks.core/src/behaviors/ — 20 behavior types
- test/JsonFiles.ts — JSON schema examples
"""

from __future__ import annotations

from enum import Enum, IntEnum


class ShapeType(str, Enum):
    """Emitter shape types — maps to JSON 'shape.type' field."""
    POINT = "point"
    CONE = "cone"
    SPHERE = "sphere"
    HEMISPHERE = "hemisphere"
    DONUT = "donut"
    CIRCLE = "circle"
    GRID = "grid"
    RECTANGLE = "rectangle"
    MESH_SURFACE = "mesh_surface"


class BehaviorType(str, Enum):
    """Behavior types — maps to JSON 'behaviors[].type' field."""
    SIZE_OVER_LIFE = "SizeOverLife"
    COLOR_OVER_LIFE = "ColorOverLife"
    SPEED_OVER_LIFE = "SpeedOverLife"
    FORCE_OVER_LIFE = "ForceOverLife"
    ROTATION_OVER_LIFE = "RotationOverLife"
    ROTATION_3D_OVER_LIFE = "Rotation3DOverLife"
    ROTATION_BY_SPEED = "RotationBySpeed"
    COLOR_BY_SPEED = "ColorBySpeed"
    SIZE_BY_SPEED = "SizeBySpeed"
    GRAVITY_FORCE = "GravityForce"
    NOISE = "Noise"
    TURBULENCE_FIELD = "TurbulenceField"
    FRAME_OVER_LIFE = "FrameOverLife"
    WIDTH_OVER_LENGTH = "WidthOverLength"
    LIMIT_SPEED_OVER_LIFE = "LimitSpeedOverLife"
    ORBIT_OVER_LIFE = "OrbitOverLife"
    APPLY_FORCE = "ApplyForce"
    APPLY_COLLISION = "ApplyCollision"
    APPLY_SEQUENCES = "ApplySequences"
    EMIT_SUB_PARTICLE_SYSTEM = "EmitSubParticleSystem"


class ValueType(str, Enum):
    """Value function types — maps to JSON value object 'type' field."""
    CONSTANT_VALUE = "ConstantValue"
    CONSTANT_COLOR = "ConstantColor"
    INTERVAL_VALUE = "IntervalValue"
    PIECEWISE_BEZIER = "PiecewiseBezier"
    GRADIENT = "Gradient"
    RANDOM_COLOR_BETWEEN_GRADIENT = "RandomColorBetweenGradient"


class RenderMode(IntEnum):
    """Render mode — maps to JSON 'renderMode' integer field."""
    BILLBOARD = 0
    STRETCHED_BB = 1
    MESH = 2
    TRAIL = 3


class BlendingMode(IntEnum):
    """Blending mode — maps to JSON 'blending' integer field."""
    NONE = 0
    NORMAL = 1
    ADDITIVE = 2
    SUBTRACTIVE = 3
    MULTIPLY = 4


__all__ = [
    "BehaviorType",
    "BlendingMode",
    "RenderMode",
    "ShapeType",
    "ValueType",
]
