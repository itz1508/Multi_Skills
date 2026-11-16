# Motion Canvas — Code-Driven Animated Explainers

## Project Setup

Motion Canvas is a TypeScript animation framework for creating code-driven explainer videos.

```bash
npx create-motion-canvas@latest my-explainer
cd my-explainer
npm install
npm run dev    # open editor at localhost:9000
```

## Signal-Based Animation

Motion Canvas uses reactive signals for animation values.

```typescript
import { makeScene2D, Rect } from "@motion-canvas/core";
import { waitFor } from "@motion-canvas/core/lib/flow";

export default makeScene2D(function* (view) {
  const box = view.create(Rect, {
    width: 100, height: 100,
    fill: "#4FC3F7",
    x: -400, y: 0
  });

  yield* box.x(400, 1).to(-400, 1).to(0, 0.5);
  yield* waitFor(0.5);
});
```

## Generator-Based Timelines

Animations use JavaScript generators — sequential, pausable, and debuggable.

```typescript
// Sequential animation
yield* box.scale(2, 0.5);
yield* box.rotation(180, 1);
yield* box.opacity(0, 0.3);

// Parallel animation
yield* all(
  box.x(200, 1),
  box.fill("#FF6B9D", 1),
  box.scale(1.5, 1)
);

// Stagger children
yield* view.children().map(child => child.y(100, 0.3));
```

## Rendering Pipeline

```bash
# Render to video
npm run render --output out/explainer.mp4

# Render specific scene
npm run render --scene MyScene --output out/scene.mp4
```

## Motion Canvas vs Remotion Decision

| Criterion | Motion Canvas | Remotion |
|---|---|---|
| Use case | Educational/technical explainers | General video production |
| Animation model | Generator-based (sequential) | Frame-based (useCurrentFrame) |
| Editor | Built-in visual timeline editor | Studio (separate preview) |
| Sync model | Signal-based reactivity | React component re-render |
| Best for | Step-by-step tutorials, algorithm visualizations | Marketing, social, product videos |
| Rendering | FFmpeg via CLI | FFmpeg via CLI |
| Complexity | Simpler for sequential content | More flexible for complex compositions |

**Choose Motion Canvas when**: step-by-step explainers, algorithm visualizations, educational content with clear sequence.
**Choose Remotion when**: marketing videos, social content, multi-scene compositions, React-native workflow.

## Key Concepts

- **Signals**: reactive values that auto-update dependents
- **Generators**: `yield*` for sequential animation flow
- `all()` for parallel execution
- `waitFor()` for pauses
- `view.create()` for scene graph objects
- Scene exports are TypeScript files — version-controllable

Source: re-written from motion-canvas/motion-canvas documentation and API reference.
