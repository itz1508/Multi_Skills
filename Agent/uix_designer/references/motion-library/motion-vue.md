# Motion for Vue Patterns

## Basic Usage

```vue
<script setup>
import { motion } from "motion-v"
</script>

<template>
  <motion.div
    :animate="{ x: 100, opacity: 1 }"
    :initial="{ x: 0, opacity: 0 }"
    :transition="{ duration: 0.4, ease: 'easeOut' }"
  />
</template>
```

## Vue-Specific Notes

- Import from `motion-v`, not `motion/react` or `framer-motion`
- Template refs work with `motion` components
- Use `v-for` with `motion` for staggered lists — pass index as delay
- Vue's reactivity system handles MotionValue updates automatically

## Reduced Motion

```vue
<script setup>
import { useReducedMotion } from "motion-v"
const shouldReduce = useReducedMotion()
</script>
```

## Installation

```bash
npm install motion-v
```

If the project has `framer-motion` installed, remove it: `npm remove framer-motion`. They must never coexist.

Source: re-written from motiondivision/ai-kit research.
