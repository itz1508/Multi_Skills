# video_generator Motion Video — Storyboard

## Visual Style
- **Theme**: Cool (seek(t) pipeline visualization)
- **Colors**: Cyan #00a6d6, Purple #7b4dff, Pink #e2308f, Orange #e08a00
- **Background**: Dark #07061a, Panel #110f2b, Border #2a2658
- **Typography**: DejaVu Sans (body), DejaVu Sans Mono (code/labels)

## Motion Profile
- Deterministic frame stepping (each cell fills at 0.08s intervals)
- Spring appearance for pipeline nodes (0.4s per node)
- Color hue rotation based on frame index (i * 137 % 360)
- Stamp animation for determinism verification

## Storyboard (8s, 30fps)

| Time | Beat | Elements on screen |
|------|------|---------------------|
| 0-2s | PIPELINE | Four nodes appear: seek(t) → Playwright → frames → ffmpeg. Each with border and text label. Dotted arrows connect them. Ephemeral calls: render·seek.html → ✓, capture·frame_0001 → ✓ |
| 2-5s | RENDER | 8×3 grid (24 cells) fills one-by-one. Each cell shows frame number (f_001, f_002...) with colored border (deterministic hue rotation). Progress counter: "Frames rendered: N/24" |
| 5-6.5s | CRITIC | Six score badges appear: hook_in_2s:9, phone_readability:7, motion_quality:8, variety:8, sound_sync:5, brand_accuracy:9. Each with colored border and score bar |
| 6.5-8s | GATE | Quality gate checklist: hook_in_2s>=8 → MET, determinism verified → MET, sound_sync>=6 → FAIL. "✓ DETERMINISTIC" stamp appears |

## Rendering
- **PIL text+border**: Current (this video) — all elements use ImageDraw.text() and rectangle(outline=), no solid blocks
- **Playwright**: Future (seek.html) — full CSS gradients, grid transitions, stamp animation
