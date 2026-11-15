# MotionScore Performance Audit

## Grading (S to F)

| Grade | Properties | Example |
|-------|-----------|---------|
| S | transform, opacity, clipPath, filter | `x`, `y`, `scale`, `rotate` |
| A | filter, clipPath (non-transform) | `blur()`, `clip-path` |
| B | Motion `layout` prop | Layout animations (FLIP) |
| C | color, backgroundColor | `color`, `fill`, `stroke` |
| D | layout-triggering properties | `width`, `height`, `top`, `left`, `margin` |
| F | Forced layout thrash per frame | `getBoundingClientRect` in rAF |

Worst-tier wins: if any value in an animation reaches D, the whole animation is D.

## Anti-Patterns to Detect

1. **Layout thrashing** — animating `width`/`height`/`top`/`left` instead of transforms
2. **will-change abuse** — set permanently, never removed
3. **onUpdate de-optimization** — accelerated animation forced to main thread
4. **Missing reduced-motion** — no `prefers-reduced-motion` check
5. **Object allocation in rAF** — creating arrays/objects inside animation frame callbacks
6. **Simultaneous transform conflicts** — multiple tweens on same transform property

## Audit Workflow

1. Grep for: CSS `transition`/`animation`/`will-change`, `element.style` writes in rAF, `element.animate()`, Motion/GSAP/react-spring/anime.js/Lottie imports
2. Classify every animation by worst tier
3. Identify concrete upgrade for everything below S
4. Report: grade, upgrade grade, title, file:line, what/why/fix, example change (max 8 lines)

## MCP Dependency

The full methodology is served live from `motion://skills/performance-audit` on the Motion+ MCP server. Without Motion+, use this reference as the grading guide and state that the live methodology was not fetched.

Source: re-written from motiondivision/ai-kit research.
