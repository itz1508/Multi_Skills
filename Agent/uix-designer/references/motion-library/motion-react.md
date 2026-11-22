# Motion for React Patterns

## Independent Transforms

Prefer independent transforms (`x`, `y`, `scale`, `rotate`) over `transform` when:
- Some transforms have different transition settings
- Some transforms are passed as motion values
- Defining transforms via `style` prop
- You have competing/composable transforms

```jsx
<motion.div animate={{ x: 100 }} whileHover={{ scale: 1.2 }} />
```

Both `transform` and independent transforms are hardware accelerated on HTML elements.

## De-optimization Triggers

Accelerated animations fall back to main thread when using:
- `onUpdate` (prop or transition option)
- `transformTemplate`
- `type: "inertia"`
- Layout animations
- SVG element animations
- Transform motion value set every frame (drag, useMotionValue streams)

Don't change working code to avoid these — they still perform well.

## MotionValues

```javascript
// Use onChange, not onChange (deprecated)
const x = useMotionValue(0)
x.on("change", (latest) => console.log(latest))

// Never use:
// x.onChange(update)  // ❌ deprecated
```

## will-change

Set `will-change` on animating properties when using de-optimizing features. Use sparingly and remove after animation finishes. For CSS `animation` or hardware-accelerated Motion animations, unnecessary — browser promotes automatically.

## Performance in Animation Frames

Inside rAF callbacks, `useTransform` callbacks, pointer move, `onUpdate`, `frame.render`:
- Avoid object allocation. Prefer mutation where safe.
- Prefer `for` loops over `forEach` or `map`.
- Avoid `Object.entries`, `Object.values`.

## Reduced Motion

```jsx
import { useReducedMotion } from "motion/react"

function Component() {
  const shouldReduce = useReducedMotion()
  return <motion.div animate={{ x: shouldReduce ? 0 : 100 }} />
}
```

Source: re-written from motiondivision/ai-kit research.
