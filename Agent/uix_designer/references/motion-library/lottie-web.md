# Lottie-Web Playback Patterns

## Player Setup

Lottie renders After Effects animations as JSON via a lightweight web player.

```js
import lottie from "lottie-web";

const anim = lottie.loadAnimation({
  container: document.getElementById("lottie-box"),
  renderer: "svg",        // svg | canvas | html
  loop: true,
  autoplay: true,
  path: "animations/hero.json"
});
```

| Renderer | When to Use |
|---|---|
| `svg` | Default — crisp at all resolutions, DOM-accessible |
| `canvas` | Many simultaneous animations — better performance |
| `html` | Rare — DOM elements, limited feature support |

## Player API

```js
anim.play(); anim.pause(); anim.stop();
anim.setSpeed(1.5);          // playback rate
anim.goToAndStop(30, true);  // frame 30, absolute
anim.setSubframe(true);      // smooth sub-frame rendering
anim.destroy();              // cleanup
```

## After Effects to Lottie Workflow

1. Install Bodymovin extension in After Effects
2. Composition → Bodymovin → Export to JSON
3. Optimize: enable `Reduce File Size`, strip hidden layers
4. Test in LottieFiles previewer before shipping
5. Host JSON alongside assets — relative paths in JSON

## Lottie vs CSS/Motion Decision

| Criterion | Lottie | CSS/Motion |
|---|---|---|
| Source | Designer-authored (After Effects) | Code-authored |
| Timeline control | Frame-based scrubbing | Duration-based tweening |
| File size | JSON payload (10KB-500KB) | Zero (inline code) |
| Editability | Requires After Effects | Code changes in editor |
| Interactivity | Limited (play/pause/seek) | Full (gestures, state) |
| Team handoff | Designer owns motion | Developer owns motion |

**Choose Lottie when**: designer-authored animations, brand-consistent motion, complex path/keyframe sequences.
**Choose CSS/Motion when**: developer-authored UI transitions, interactive state changes, performance-critical lists.

## Performance Optimization

- Use `canvas` renderer when running 3+ simultaneous animations
- `rendererSettings: { hideOnTransparent: true }` skips empty frames
- Preload JSON via `fetch` and pass `animationData` instead of `path`
- `lottie.freeze()` / `lottie.unfreeze()` for tab visibility
- Lazy-load below-fold animations with IntersectionObserver

## Reduced Motion

```js
if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  anim.goToAndStop(anim.totalFrames - 1, true);  // show last frame only
}
```

Source: re-written from airbnb/lottie-web documentation and player API reference.
