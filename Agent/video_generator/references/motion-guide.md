# Motion Guide: seek(t) Deterministic Pipeline

## The Frame Function

The whole technique is one function:

```javascript
seek(t) → paint exactly what the screen shows at second t
```

A headless browser calls it N times (e.g., 900 for 15s at 60fps), grabs every frame, and ffmpeg encodes them into a video. Nothing runs on a timer, so frame 240 renders without replaying frames 0–239.

### Render Contract (enforced in checks/valid.py)

- `window.seek(t)` paints frame t, nothing else drives the picture
- No CSS transitions, `setTimeout`, or `requestAnimationFrame` in render mode
- Seeded noise only, never `Math.random()`
- Determinism check: render frame N twice, SHA-256 hashes must match

### Where seek(t) Wins

Product films, UI motion, data stories, typography, launch explainers.

### Where seek(t) Loses

Photoreal scenes, complex characters, organic movement — use belt mode (AI models) instead.

## Closed-Form Springs

Motion with mass: speeds up, overshoots a hair, settles. Pure function of time, so `seek(t)` stays deterministic.

```javascript
track(t) = v0 + Σ (vi − v(i-1)) × spring(t − ti)
```

Stack one spring per target change (cursor, container width) instead of restarting. Frame 812 renders without simulating frames 0–811.

### Per-class motion rules

| Object class | Rule |
|-------------|------|
| Small UI | Snap with minimal overshoot |
| Panels | Settle |
| Camera | Glide almost invisibly |
| Headlines | Land hard, hold long enough to read |
| Mascots | Bounce on purpose |

If everything overshoots, nothing feels precise.

## State Lists

A storyboard says what the viewer knows at each second, not a list of effects.

```
00-02s  HOOK     one image that earns attention
02-05s  PROBLEM  the friction, shown on screen
05-09s  REVEAL   the product enters through a real interaction
09-13s  PROOF    one screen or number backs the claim
13-16s  CLOSE    a clean final state and a readable CTA
```

A single container morphs size, radius, and color from state to state. Each beat needs an entry state, an exit state, and a reason to be there. If the agent can't explain why shot four exists, shot four gets cut.

## Sound on the Same Clock

```bash
python -c "import librosa; ..." song.wav > beats.json
```

State changes go on beats, big moments on downbeats, clicks and whooshes on hits.

Blindfold test: close your eyes and listen. If the audio has no shape without the picture, the sound design is unfinished.

## Banned Defaults

- Centered title on gradient
- Everything fading in
- Corner labels
- Glow on UI

One display face, one UI face, one accent. Something new on screen every 2–4 seconds.

## 6-Gate Quality Control

| Gate | Check | Output |
|------|-------|--------|
| 1 | References and product assets approved | Asset list |
| 2 | Style guide and shot list approved | style_guide.md, shotlist.md |
| 3 | Stills for every shot, critiqued | Contact sheet, scores |
| 4 | Animatic at 960×540 with placeholder audio | Low-res MP4 |
| 5 | Full pass, polish, sound | Final MP4 |
| 6 | Formats, loop check, poster frame, README | Multi-format exports |

The agent works between gates. A missing interface screenshot is a blocker. An unclear reference gets a question or one test frame before 900 polished wrong ones.
