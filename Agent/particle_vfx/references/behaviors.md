# Behaviors

20 behavior types verified from `quarks.core/src/behaviors/`.

## Life-Based Behaviors

| Behavior | JSON `type` | Description |
|----------|------------|-------------|
| SizeOverLife | `SizeOverLife` | Animate size over particle lifetime |
| ColorOverLife | `ColorOverLife` | Animate color over particle lifetime |
| SpeedOverLife | `SpeedOverLife` | Animate speed over particle lifetime |
| ForceOverLife | `ForceOverLife` | Apply force over particle lifetime |
| RotationOverLife | `RotationOverLife` | Animate rotation over lifetime |
| Rotation3DOverLife | `Rotation3DOverLife` | 3D rotation over lifetime |
| FrameOverLife | `FrameOverLife` | Animate texture frame over lifetime |

## Speed-Based Behaviors

| Behavior | JSON `type` | Description |
|----------|------------|-------------|
| RotationBySpeed | `RotationBySpeed` | Rotation based on particle speed |
| ColorBySpeed | `ColorBySpeed` | Color based on particle speed |
| SizeBySpeed | `SizeBySpeed` | Size based on particle speed |
| LimitSpeedOverLife | `LimitSpeedOverLife` | Limit speed over lifetime |

## Force Behaviors

| Behavior | JSON `type` | Description |
|----------|------------|-------------|
| GravityForce | `GravityForce` | Apply gravity to particles |
| ApplyForce | `ApplyForce` | Apply directional force |
| TurbulenceField | `TurbulenceField` | Turbulent force field |
| Noise | `Noise` | Noise-based force |
| OrbitOverLife | `OrbitOverLife` | Orbital motion over lifetime |

## Collision Behaviors

| Behavior | JSON `type` | Description |
|----------|------------|-------------|
| ApplyCollision | `ApplyCollision` | Collision response |
| ApplySequences | `ApplySequences` | Sequential animation |

## Sub-System Behaviors

| Behavior | JSON `type` | Description |
|----------|------------|-------------|
| EmitSubParticleSystem | `EmitSubParticleSystem` | Spawn sub-emitters |
| WidthOverLength | `WidthOverLength` | Trail width over length |

Source: verified from quarks.core/src/behaviors/ directory.
