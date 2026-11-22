# 2D Web Particles (tsParticles)

## Configuration Schema

tsParticles renders 2D particle effects in DOM/Canvas. Config is JSON — no Three.js required.

```json
{
  "particles": {
    "number": { "value": 80, "density": { "enable": true, "area": 800 } },
    "color": { "value": ["#5C6BC0", "#42A5F5", "#26C6DA"] },
    "shape": { "type": "circle" },
    "opacity": { "value": 0.6, "animation": { "enable": true, "speed": 1, "sync": false } },
    "size": { "value": { "min": 1, "max": 5 } },
    "move": {
      "enable": true, "speed": 2, "direction": "none",
      "outModes": { "default": "bounce" }
    },
    "links": { "enable": true, "distance": 150, "color": "#5C6BC0", "opacity": 0.4 }
  },
  "interactivity": {
    "events": {
      "onHover": { "enable": true, "mode": "grab" },
      "onClick": { "enable": true, "mode": "push" }
    },
    "modes": {
      "grab": { "distance": 200, "links": { "opacity": 0.8 } },
      "push": { "quantity": 4 }
    }
  }
}
```

## Emitter Presets

| Preset | Particles | Behavior |
|---|---|---|
| `links` | Connected dots with proximity lines | Background ambient |
| `snow` | Falling white particles | Seasonal/decorative |
| `bubble` | Floating circles with hover scale | Interactive hero sections |
| `confetti` | Burst of colored shapes | Celebration effect |
| `fireworks` | Upward burst with gravity | Event trigger |

```js
import { tsParticles } from "@tsparticles/engine";
import { loadLinksPreset } from "@tsparticles/preset-links";

await loadLinksPreset(tsParticles);
await tsParticles.load({ id: "bg", options: { preset: "links" } });
```

## Interactivity Modes

| Mode | Trigger | Effect |
|---|---|---|
| `grab` | Hover | Draws line from cursor to nearby particles |
| `bubble` | Hover | Enlarges and highlights nearby particles |
| `repulse` | Hover | Pushes particles away from cursor |
| `push` | Click | Adds particles at click position |
| `remove` | Click | Removes particles at click position |

## 2D tsParticles vs 3D three.quarks Decision

| Criterion | tsParticles (2D) | three.quarks (3D) |
|---|---|---|
| Dimension | 2D DOM/Canvas | 3D WebGL scene |
| Runtime | Browser DOM/Canvas only | Three.js + WebGL |
| Config format | JSON with CSS-like values | Three.js ObjectLoader JSON |
| Physics | Basic move/bounce | Full 3D behaviors (GravityForce, ForceField) |
| Shapes | circle, square, triangle, star, polygon | point, cone, sphere, hemisphere, donut |
| GPU instancing | No | Yes — thousands of particles |
| Use case | Website backgrounds, UI ambiance | Game effects, 3D scenes, high-particle-count |

**Choose tsParticles when**: website backgrounds, interactive UI particle effects, no WebGL needed.
**Choose three.quarks when**: 3D game/scene particle effects, GPU-instanced thousands, complex 3D behaviors.

Source: re-written from tsparticles/tsparticles documentation and configuration reference.
