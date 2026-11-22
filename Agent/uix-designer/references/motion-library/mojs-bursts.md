# mo.js Burst & Shape Motion Patterns

## Burst Animation

mo.js specializes in burst-style motion graphics — radial, shape-based, and curve-path animations.

```js
import mojs from "@mojs/core";

const burst = new mojs.Burst({
  left: 0, top: 0,
  radius: { 0: 100 },
  count: 20,
  children: {
    shape: "circle",
    fill: { "#FF6B9D": "#4FC3F7" },
    duration: 2000,
    easing: "cubic.out",
    isShowStart: false
  }
});

document.addEventListener("click", (e) => {
  burst.tune({ x: e.pageX, y: e.pageY }).replay();
});
```

## Shape Types

| Shape | Use Case |
|---|---|
| `circle` | Default burst particles |
| `rect` | Confetti, geometric patterns |
| `polygon` | Star bursts, geometric explosions |
| `cross` | Sparkle effects |
| `zigzag` | Electric/lightning effects |
| `curve` | Flowing organic paths |

## Curve Path Animation

```js
const curve = new mojs.ShapeCurve({
  parent: ".container",
  stroke: "#42A5F5",
  strokeWidth: 4,
  fill: "none",
  radius: 80,
  duration: 1000,
  isShowStart: true
});
```

## Shape Swarms

```js
const swarm = new mojs.ShapeSwirl({
  fill: "#FFA726",
  x: { 0: 200 },
  radius: 20,
  swirlSize: 15,
  swirlFrequency: 20,
  duration: 1500,
  pathScale: 0.5,
  degreeShift: 30
});
```

## mo.js vs Motion vs GSAP Decision

| Criterion | mo.js | Motion (Framer) | GSAP |
|---|---|---|---|
| Burst effects | Native, specialized | Not built-in | Not built-in |
| Shape variety | 6 built-in shapes | DOM elements only | DOM elements only |
| Curve paths | Native ShapeCurve | No | Via MotionPathPlugin |
| Timeline | Basic | AnimatePresence | Full timeline |
| Scroll animation | No | useScroll | ScrollTrigger |
| React integration | Manual ref binding | Native | useGSAP hook |
| Bundle size | ~30KB | ~30KB | ~30KB+ |
| Best for | Promotional, marketing, celebratory | UI transitions | Complex timelines, scroll |

**Choose mo.js when**: burst effects, radial animations, shape swarms, promotional/marketing motion.
**Choose Motion when**: React UI transitions, spring physics, layout animations.
**Choose GSAP when**: complex timelines, scroll-driven, SVG morphing, non-React.

## Timeline Orchestration

```js
const timeline = new mojs.Timeline();
timeline.add(burst, curve, swarm);
timeline.play();
```

Source: re-written from mojs/mojs documentation and API reference.
