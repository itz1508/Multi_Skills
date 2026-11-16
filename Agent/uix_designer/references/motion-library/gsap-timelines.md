# GSAP Timeline & ScrollTrigger Patterns

## Timeline Orchestration

GSAP timelines sequence animations with precise control over overlap, staggering, and positioning.

```js
// Basic timeline with positioned tweens
const tl = gsap.timeline();
tl.to(".card", { x: 100, duration: 0.5 })
  .to(".card", { y: 50, duration: 0.3 }, "+=0.1")   // 0.1s after previous ends
  .to(".card", { opacity: 1, duration: 0.2 }, "<");  // at same time as previous
```

## Staggers

Staggers distribute animation delays across multiple elements.

```js
// Grid-aware stagger
gsap.from(".grid-item", {
  y: 30, opacity: 0, duration: 0.4,
  stagger: { amount: 0.6, grid: "auto", from: "center" }
});
```

| Stagger Type | Use Case |
|---|---|
| `amount` | Total spread across all elements |
| `each` | Fixed delay between each element |
| `grid` | 2D layout awareness (rows + columns) |
| `from` | Origin: start, center, edges, random, or index |

## ScrollTrigger

ScrollTrigger ties animations to scroll position — scrubbing, pinning, and triggering.

```js
// Scrub animation tied to scroll
gsap.to(".hero", {
  y: -200, opacity: 0,
  scrollTrigger: {
    trigger: ".hero", start: "top top", end: "bottom top",
    scrub: 1, pin: true
  }
});
```

```js
// Batch trigger for performance
gsap.utils.toArray(".reveal").forEach((el) => {
  gsap.from(el, {
    y: 60, opacity: 0, duration: 0.6,
    scrollTrigger: { trigger: el, start: "top 85%" }
  });
});
```

## GSAP vs Motion Decision

| Criterion | GSAP | Motion (Framer) |
|---|---|---|
| Timeline orchestration | Native, powerful | Limited to AnimatePresence |
| Scroll animation | ScrollTrigger plugin | Requires useScroll |
| Stagger control | Grid-aware, directional | Simple staggerChildren |
| Bundle size | ~30KB min (plugins add) | ~30KB tree-shakeable |
| React integration | Via useGSAP hook | Native React components |
| SVG morphing | MorphSVG plugin | No built-in |
| Physics | No built-in | Spring physics native |

**Choose GSAP when**: complex timelines, scroll-driven animation, SVG morphing, non-React projects.
**Choose Motion when**: React UI transitions, spring physics, layout animations, declarative JSX.

## useGSAP Hook (React)

```jsx
import { useGSAP } from "@gsap/react";

function Component() {
  useGSAP(() => {
    gsap.from(".item", { y: 30, opacity: 0, stagger: 0.1 });
  }, { scope: ".container" });
  return <div className="container"><div className="item" /></div>;
}
```

## Performance Notes

- `will-change: transform` on animated elements prevents paint thrash
- `force3D: true` (default) pushes transforms to GPU layer
- Avoid animating top/left — use x/y (transform-based)
- ScrollTrigger.batch handles many elements efficiently
- `gsap.matchMedia()` for responsive animation variants

Source: re-written from greensock/GSAP documentation and API reference.
