# CSS Spring Generation via Motion

Springs and bounces are not native CSS easings. Motion approximates them by sampling the curve into a CSS `linear()` easing function.

## MCP Tool

```
generate-css-easing({ kind, duration, bounce })
```

- `kind` — `"spring"` (default) for springy settle, or `"bounce"` for ball-landing easing
- `duration` (seconds) — perceptual duration. Defaults to 0.4 (spring) or 1 (bounce)
- `bounce` (0 to 1) — overshoot amount. 0 = firm settle, 1 = max wobble. Defaults to 0.2

When `kind` is `"bounce"`, the `bounce` parameter is ignored — the feel is controlled by duration alone.

## Reading the Result

The tool returns the `<duration> <easing>` half of a CSS transition:

```css
/* generate-css-easing({ kind: "spring", duration: 0.2, bounce: 0.3 }) */
transition:
  opacity 0.2s linear,
  transform 0.35s linear(0, 0.28, 0.78, 1.04, ...);
```

The returned duration is longer than requested because it includes settle time. Time sibling animations off the requested duration, not the returned one.

## Choosing Values

- Snappy/quick: ~0.2s
- Normal: 0.3-0.4s
- Slow/heavy: ~1s
- Bounces read better long: 1s feels like normal gravity
- Match the product: stock trading = no overshoot; wedding site = softer, longer

## Without MCP

If the Motion MCP server is unavailable, approximate manually:
- Spring: `cubic-bezier(0.34, 1.56, 0.64, 1)` with overshoot
- Bounce: keyframes with decaying vertical offsets

Source: re-written from motiondivision/ai-kit research.
