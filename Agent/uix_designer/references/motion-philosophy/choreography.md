# Multi-Element Choreography

## Coordinated Entry Rules

- Lead with the hero — primary element enters first or most prominently
- Spatial consistency — all elements enter from the same direction
- Counter-motion — hero moves right, ambient moves left at 20-30% speed

## The 1/3 Rules

1. **Distance**: No motion travels more than 1/3 of screen without a keyframe change
2. **Elements**: With 3+ elements, no more than 1/3 in active motion simultaneously

## Stagger Budgets

| Pattern | Delay | Total Budget | Use Case |
|---------|-------|-------------|----------|
| Micro cascade | 20-40ms | <200ms | List items, grid cells |
| Standard | 50-100ms | <400ms | Cards, panels, nav |
| Dramatic | 100-200ms | <600ms | Hero sections |
| Wave | 30-60ms | <500ms | Data visualizations |

Total stagger must stay under 500ms.

## Three Motion Layers

Every scene must have all three:

1. **Primary** — Main action the viewer follows (card sliding in)
2. **Secondary** — Supporting richness (shadow arriving, icons shifting)
3. **Ambient** — Background life (gradient pulse, subtle parallax)

Flat animation = missing layers.

## Narrative Structure (Micro-Story)

1. **Setup** — Element at rest, context established
2. **Action** — The motion itself, timed to the emotional beat
3. **Resolution** — Settling, follow-through, return to rest or new state

Each animation should express a cause-effect relationship, not just decoration.

Source: re-written from LottieFiles/motion-design-skill research.
