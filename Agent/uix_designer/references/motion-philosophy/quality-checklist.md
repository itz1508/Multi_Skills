# Motion Design Quality Checklist

## CRITICAL — Never Break

1. Never use `linear` for spatial movement — always easing curves (linear only for spinners, progress bars)
2. Never opacity-only for important state changes — combine with position or scale
3. Never exceed 1/3 screen without intermediate keyframe
4. Always three motion layers — primary + secondary + ambient

## HIGH — Strongly Follow

1. Match duration to element type (see motion-personality.md tables)
2. Use directional easing (ease-out entrance, ease-in exit)
3. Apply Disney principles (especially anticipation, follow-through)
4. Maintain consistent personality across the scene
5. Enter longer than exit (30-50% longer — users care about what appears)
6. Respect `prefers-reduced-motion`
7. Keep stagger under 500ms total

## Interactive Feedback Timing

| State | Duration |
|-------|----------|
| Hover | <100ms |
| Press | <150ms |
| Release/settle | 200-300ms |
| Error shake | 300-400ms (2-3 oscillations) |

## Distance Scales Duration

- 100px = base duration
- 200px = 1.3x duration
- 400px = 1.6x duration

Source: re-written from LottieFiles/motion-design-skill research.
