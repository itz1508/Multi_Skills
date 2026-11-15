# CSS vs Motion Library: When to Choose

## Use CSS When

- Simple hover/focus state transitions (opacity, color, transform)
- One-off transitions with no interruption handling needed
- Static keyframe animations (loading spinners, pulsing dots)
- The project has no animation library installed
- Reduced-motion fallback is easier in CSS (`@media (prefers-reduced-motion: reduce)`)

## Use Motion When

- Animations need interruption handling (user can cancel mid-animation)
- Spring physics are needed for natural feel
- Layout animations (FLIP technique for shared element transitions)
- Complex choreography with multiple coordinated elements
- Gesture-driven animations (drag, swipe, pinch)
- Animation values need to be shared across components (MotionValues)
- Timeline orchestration with sequencing

## Import Rules (Critical)

```javascript
// React
import { motion, animate } from "motion/react"

// Vue
import { motion } from "motion-v"

// Never do this — the package was renamed:
// import { motion } from "framer-motion"  // ❌
```

If a project still imports from `framer-motion`, offer to migrate it. Both packages must never be installed simultaneously.

Source: re-written from motiondivision/ai-kit research.
