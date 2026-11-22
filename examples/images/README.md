# Motion Skill Generation — UIX + VIDEO

## Overview

Two motion videos generated from the `uix_designer` (UIX) and `video_generator` (VIDEO) skills. Each video demonstrates the skill's visual style and motion profile using **text and borders only** — no solid colored blocks.

## Generated Assets

### uix_designer/ (Warm Theme)

| File | Size | Description |
|------|------|-------------|
| `video.mp4` | 81 KB | 8s, 30fps, H.264 — thinking mode + search info + content streaming |
| `animation.gif` | 6.6 MB | 480px wide, 15fps, looped |
| `contact_sheet.png` | 15 KB | 8 frames, one per second |
| `seek.html` | — | Future Playwright rendering template |
| `storyboard.md` | — | Beats, states, motion profile |

### video_generator/ (Cool Theme)

| File | Size | Description |
|------|------|-------------|
| `video.mp4` | 154 KB | 8s, 30fps, H.264 — pipeline + frame grid + critic scores |
| `animation.gif` | 7.3 MB | 480px wide, 15fps, looped |
| `contact_sheet.png` | 39 KB | 8 frames, one per second |
| `seek.html` | — | Future Playwright rendering template |
| `storyboard.md` | — | Beats, states, motion profile |

## Visual Style Comparison

| Property | uix_designer | video_generator |
|----------|-------------|-----------------|
| Theme | Warm (OneShot chat) | Cool (pipeline visualization) |
| Primary | #f4934a (orange) | #00a6d6 (cyan) |
| Secondary | #3dbfae (teal) | #7b4dff (purple) |
| Accent | #ff6b76 (red) | #e2308f (pink) |
| Background | #0d0b08 | #07061a |
| Motion | Spring, cubic-bezier | Deterministic, linear stepping |
| Focus | Thinking mode, search info, streaming text | Pipeline nodes, frame grid, critic scores |

## Motion Profile Comparison

| Phase | uix_designer | video_generator |
|-------|-------------|-----------------|
| 0-2s | Orb + shimmer + track nodes (thinking) | Pipeline nodes appear with arrows |
| 2-5s | Ephemeral call pills with status transitions | Frame grid fills (24 cells, 0.08s each) |
| 5-8s | Text streams char-by-char + gate checklist | Critic scores + quality gate + determinism stamp |

## Rendering Approach

### Current: PIL text + borders

All elements rendered using Python PIL (`ImageDraw.text()`, `ImageDraw.rectangle(outline=)`, `ImageDraw.ellipse(outline=)`, `ImageDraw.arc()`). **No solid colored blocks** — every element has text content and border outlines.

- Frames: 240 per video (8s × 30fps)
- Encoding: ffmpeg libx264 CRF 18
- GIF: ffmpeg 15fps, 480px, lanczos
- Contact sheet: ffmpeg fps=1, tile=8x1

### Future: Playwright (seek.html)

Each skill has a `seek.html` file with the same visual content implemented in CSS. When Playwright + Chromium is available on a networked compute:

```bash
playwright install chromium
python -m agent.skills.video_generator.tools.motion encode \
  --html examples/images/uix_designer/seek.html \
  --duration 8 --fps 30 \
  --output examples/images/uix_designer/video_playwright.mp4
```

Playwright rendering provides:
- CSS gradients (radial, conic, linear)
- backdrop-filter blur effects
- CSS spring animations (cubic-bezier)
- backdrop-filter and box-shadow glows
- Full typography (Google Fonts)

## Blocked on Serverless

The following could not be tested on serverless compute (no outbound network):
- Playwright frame capture (pip install fails — DNS resolution)
- librosa beat detection (pip install fails)
- WhisperX transcription (pip install fails)
- Openverse API SFX search (no outbound HTTPS)

## References

- `OneShot-chat-streaming-refactored.html` — warm theme UI source
- `oneshot-searching (2).html` — cool theme UI source
- `Agent/uix-designer/references/motion-library/` — CSS spring, React motion, Vue motion
- `Agent/uix-designer/references/motion-philosophy/` — Disney's 12 principles, choreography
- `Agent/video-generator/references/motion-guide.md` — seek(t) contract, springs, gates
- `Agent/video-generator/references/tool-catalog.md` — 20 motion tools categorized
