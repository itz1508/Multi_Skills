# Emitter Shapes

9 emitter shapes verified from `quarks.core/src/shape/`.

## Shape Types

| Class | JSON `type` | Key Parameters |
|-------|------------|----------------|
| PointEmitter | `point` | radius |
| ConeEmitter | `cone` | radius, arc, thickness, angle |
| SphereEmitter | `sphere` | radius, arc, thickness, mode, spread, speed |
| HemisphereEmitter | `hemisphere` | radius, arc, thickness |
| DonutEmitter | `donut` | radius, arc, thickness |
| CircleEmitter | `circle` | radius, arc, thickness |
| GridEmitter | `grid` | width, height |
| RectangleEmitter | `rectangle` | width, height |
| MeshSurfaceEmitter | `mesh_surface` | geometry (uuid ref) |

## Common Parameters

- `radius` — Emitter radius
- `arc` — Angular span (default 2π = full circle)
- `thickness` — Emission thickness (0-1, 1 = full volume)
- `angle` — Cone half-angle (cone only)
- `mode` — Emission mode (sphere only)
- `spread` — Spread amount (sphere only)
- `speed` — Emission speed value function (sphere only)
- `geometry` — UUID reference to geometry in geometries array (mesh_surface only)

Source: verified from quarks.core/src/shape/ directory.
