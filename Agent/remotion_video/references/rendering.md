# Rendering a Remotion Video

Only render when the user is very explicit: "Render the video", "Export", "Give me the MP4".

## Basic Render

```bash
npx remotion render <composition-id> out/video.mp4
```

## Codec Options

| Codec | Flag | Use Case |
|-------|------|----------|
| H.264 | `--codec=h264` | Web-compatible MP4 (default) |
| H.265 | `--codec=h265` | Smaller files, less compatible |
| VP8 | `--codec=vp8` | WebM |
| VP9 | `--codec=vp9` | WebM, better compression |
| GIF | `--codec=gif` | Animated GIF |

## Quality

`--quality=80` (default). Lower = smaller file, higher = better quality.

## Image Sequence

```bash
npx remotion render <composition-id> --sequence out/frames
```

## Server-Side Rendering

For Lambda, Vercel, Cloudflare, or Express.js, see the SaaS reference.

Source: re-written from remotion-dev/skills research.
