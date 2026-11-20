---
name: particle_vfx
description: Build and validate Three.js three.quarks particle-effect JSON with Pydantic v2. Use when a project needs particle-system configuration, not rendered video or live GPU preview.
---

# Particle VFX

> Construct Three.js particle configuration as typed JSON and validate its local structure before loading it in the target renderer.

## When to use

Use this skill to build a single-emitter effect or a multi-emitter QuarksPrefab timeline compatible with the target project's three.quarks integration.

Do not use it to render an animation, create a video, or replace the target project's Three.js runtime.

## Ownership and boundaries

- Owns Pydantic model construction and JSON serialization for particle effects.
- Produces configuration data; it does not render particles or prove that a browser/GPU renderer accepts the effect.
- The consuming application owns Three.js, three.quarks, actual loading, rendering, and visual validation.
- Host dispatch hooks do not replace user authorization or independent artifact checks.

## Prerequisites and installation

- Python 3.10 or newer.
- pydantic >= 2.
- For actual playback, the consuming Three.js project must install compatible three and three.quarks versions.
- Place the package at agent/skills/particle_vfx/ in the consuming project.
- The host-integrated run.py imports agent.contracts.host, which is not supplied by this library.

This repository does not include a standalone Python distribution manifest for this package.

## Importable operations

The source modules provide the builder and structural validator:

~~~python
from agent.skills.particle_vfx.tools.quarks_builder import (
    ConeShape,
    build_simple_effect,
    build_prefab_effect,
)
from agent.skills.particle_vfx.checks.valid import check_effect_json

shape = ConeShape().model_dump(by_alias=True)
effect = build_simple_effect(shape=shape)
payload = effect.model_dump_json(by_alias=True)
assert check_effect_json(payload)
~~~

| Function | Purpose |
|---|---|
| build_simple_effect(...) | Build a single-emitter QuarksEffect |
| build_prefab_effect(...) | Build a QuarksPrefab effect with emitters and timeline entries |
| check_effect_json(json_str) | Check local JSON structure and supported shape/behavior/value types |

Use model aliases when serializing for Three.js JSON (by_alias=True); the models emit camelCase field names expected by the target schema.

## Procedure

1. Inspect the target project's installed three and three.quarks versions and existing particle assets.
2. Select an emitter shape and supported behaviors from tools/schema.py.
3. Build the effect with build_simple_effect or construct emitter nodes and call build_prefab_effect.
4. Serialize with model_dump_json(by_alias=True).
5. Run check_effect_json and inspect referenced UUIDs, geometry, material, texture, and image references.
6. Load the JSON through the target project's QuarksLoader.parse() and run a browser/renderer check before claiming visual correctness.

## Outputs and verification

- A QuarksEffect model or serialized JSON payload.
- Structural validation result from check_effect_json.
- In the consuming host, an expected vfx_record or build_record artifact reference.

The local validator checks structure and declared enums. It is not a call to QuarksLoader.parse() and does not prove successful GPU rendering. Record the target Three.js version, loader result, and a visual check separately.

## Entry point behavior

run.py is informational: it verifies the supplied repository path and prints supported shapes, value types, and builder usage. It does not create an effect or run the Three.js loader.

## Failure handling

- Missing Pydantic: report blocked.
- Unsupported enum/value or malformed JSON: report not_valid with the offending field/path.
- No target Three.js/three.quarks test: report renderer compatibility as not_run, not valid by implication.
- Do not present configuration JSON as a rendered effect.

## Next steps

Build the smallest representative effect, validate its serialized JSON, then load it in the target project's actual QuarksLoader and record the result.
