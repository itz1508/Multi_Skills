# JSON Schema (Three.js ObjectLoader Compatible)

The output JSON is compatible with Three.js ObjectLoader and three.quarks QuarksLoader.parse().

## Top-Level Structure

```json
{
  "metadata": { "version": 4.6, "type": "Object", "generator": "Object3D.toJSON" },
  "geometries": [{ "uuid": "...", "type": "PlaneGeometry", "width": 1, "height": 1 }],
  "materials": [{ "uuid": "...", "type": "MeshBasicMaterial", "color": 16777215 }],
  "textures": [{ "uuid": "...", "name": "texture.png", "image": "..." }],
  "images": [{ "uuid": "...", "url": "" }],
  "object": {
    "type": "Group" | "QuarksPrefab",
    "uuid": "...",
    "layers": 1,
    "matrix": [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1],
    "children": [{
      "type": "ParticleEmitter",
      "uuid": "...",
      "ps": { "version": "3.0", "shape": {...}, "behaviors": [...], ... }
    }]
  }
}
```

## ParticleEmitter 'ps' Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| version | string | "3.0" | Schema version |
| autoDestroy | bool | false | Auto-destroy when finished |
| looping | bool | true | Loop the system |
| prewarm | bool | false | Prewarm on start |
| duration | float | 5 | System duration (seconds) |
| maxParticle | int | 10000 | Max particles |
| shape | object | cone | Emitter shape config |
| startLife | object | ConstantValue(5) | Particle lifetime |
| startSpeed | object | ConstantValue(10) | Initial speed |
| startSize | object | ConstantValue(1) | Initial size |
| startColor | object | ConstantColor(white) | Initial color |
| emissionOverTime | object | ConstantValue(10) | Emission rate |
| emissionBursts | array | [] | Burst emissions |
| onlyUsedByOther | bool | false | Sub-emitter only |
| instancingGeometry | string | — | UUID of instancing geometry |
| renderMode | int | 0 | Render mode (0=billboard) |
| blending | int | 2 | Blending (2=additive) |
| texture | string | — | UUID of texture |
| uTileCount | int | 1 | U sprite sheet tiles |
| vTileCount | int | 1 | V sprite sheet tiles |
| behaviors | array | [] | Behavior list |
| worldSpace | bool | false | World space particles |

## QuarksPrefab animationData

```json
{
  "startTime": 0,
  "duration": 2,
  "type": "ps",
  "targetUUID": "...",
  "loop": false
}
```

`type` can be `"ps"` (particle system) or `"three"` (Three.js animation with `clipUUID`).

Source: verified from three.quarks test/JsonFiles.ts, src/QuarksLoader.ts, src/QuarksPrefab.ts.
