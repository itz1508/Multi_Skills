# Particle VFX Skill

## Purpose

GPU particle effect configuration for Three.js via three.quarks. Builds, validates, and exports JSON files compatible with QuarksLoader.parse(). Uses Pydantic v2 models for type-safe construction of particle systems with 9 emitter shapes, 20 behaviors, and value functions. No overlap with existing skills — unique 3D particle domain.

## Entry Point

```bash
uv run --no-sync python -m agent.skills.particle_vfx.run <repository-root>
# Build effect:
from agent.skills.particle_vfx.tools.quarks_builder import build_simple_effect
effect = build_simple_effect(shape=ConeShape().model_dump())
json_str = effect.to_json()
# Load in Three.js:
# new QuarksLoader().parse(JSON.parse(json_str))
```

## Tools

- `quarks_builder` — Pydantic v2 models for ParticleSystem, emitter shapes, behaviors, value types, QuarksPrefab timeline
- `schema` — Enum classes for ShapeType, BehaviorType, RenderMode, BlendingMode, ValueType



| Tool | Inputs | Outputs |
|------|--------|---------|
| `build_simple_effect` | shape, start_life, start_speed, emission_rate, duration | QuarksEffect JSON |
| `build_prefab_effect` | emitters[], animation_entries[], geometries[] | QuarksEffect JSON with timeline |
| `check_effect_json` | JSON string | bool (valid for QuarksLoader) |

## Output

- `ArtifactRef` to JSON effect file (contract `vfx_record`, v1.0)
- Execution evidence: JSON structure, emitter count, behavior count, schema version
- Disposition: `completed` / `blocked` (missing pydantic) / `not_run`

## Ownership

Runtime-authorized particle effect construction, scoped to Pydantic model validation and JSON export. Never fabricates particle rendering — all output is configuration JSON for QuarksLoader.parse(). Unique 3D domain, no overlap with video_generator, remotion_video, or ffmpeg_media.

## Responsibilities

- Build ParticleSystem configurations with 9 emitter shapes
- Apply 20 behavior types (SizeOverLife, ColorOverLife, ForceOverLife, etc.)
- Construct value functions (ConstantValue, ConstantColor, IntervalValue, etc.)
- Build QuarksPrefab timelines mixing Three.js and particle animations
- Export Three.js ObjectLoader-compatible JSON with uuid references
- Validate JSON output matches QuarksLoader.parse() expectations

## Runtime Integration

- Reports through `HostDispatchResult` with `vfx_record` contract
- Never issues trusted receipts; host validates JSON structure
- Host binds approval for particle VFX construction (default_deny)

## Constraints

- Requires `pydantic >=2` for model construction — without it, disposition `blocked`
- Runtime requires `three` and `three.quarks` in the Three.js project
- JSON format is Three.js ObjectLoader-compatible (uuid references, matrix arrays, nested geometries/materials/textures)
- 9 emitter shapes: point, cone, sphere, hemisphere, donut, circle, grid, rectangle, mesh_surface
- 20 behaviors verified from quarks.core/src/behaviors/
- Pydantic models handle Three.js conventions (uuid refs, matrix arrays)
- No overlap with any existing Multi_Skills skill
