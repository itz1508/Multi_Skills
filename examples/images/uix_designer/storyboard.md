# uix_designer Motion Video — Storyboard

## Visual Style
- **Theme**: Warm (OneShot chat interface)
- **Colors**: Orange #f4934a, Teal #3dbfae, Red #ff6b76, Amber #d4a73e
- **Background**: Dark #0d0b08, Panel #1a1612, Border #332d22
- **Typography**: DejaVu Sans (body), DejaVu Sans Mono (code/labels)

## Motion Profile
- Spring physics for orb and panel appearances
- Cubic-bezier(.22,1,.36,1) for text and call transitions
- 150-300ms transition durations
- Blinking cursor at 2Hz (0.8s steps)

## Storyboard (8s, 30fps)

| Time | Beat | Elements on screen |
|------|------|---------------------|
| 0-0.5s | ACTIVATE | Process card border appears. Orb fades in with radial gradient. |
| 0.5-2s | THINKING | Shimmer bar animates. Track nodes 1-5 light up sequentially. Label: "Thinking mode: analyzing input..." |
| 2-5s | SEARCH | Three ephemeral call pills appear: hook·read_file·file1.txt → ✓ done, tool·sha256·compute hash → ✓ done, hook·compare·file2.md → ↷ skip |
| 5-6.5s | STREAM | Content streams char-by-char: "SHA-256 verification complete. file1.txt matches file2.md. Evidence packet generated." Blinking cursor ▍ |
| 6.5-8s | GATE | Verification gate appears with checklist: Source files read → MET, SHA-256 computed → MET, Timestamp check → STALE |

## Rendering
- **PIL text+border**: Current (this video) — all elements use ImageDraw.text() and rectangle(outline=), no solid blocks
- **Playwright**: Future (seek.html) — full CSS gradients, backdrop-filter, spring animations
