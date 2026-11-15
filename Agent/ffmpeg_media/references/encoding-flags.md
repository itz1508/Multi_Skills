# Safe Encoding Flags

## Video Codecs

| Codec | Flag | Use Case |
|-------|------|----------|
| H.264 | `libx264` | Web-safe MP4 (default) |
| H.265 | `libx265` | Smaller files, less compatible |
| VP8 | `libvpx` | WebM |
| VP9 | `libvpx-vp9` | WebM, better compression |
| GIF | `gif` | Animated GIF, no audio |

## Pixel Formats

| Format | Flag | Use Case |
|--------|------|----------|
| yuv420p | `-pix_fmt yuv420p` | Web-safe (default) |
| yuv444p | `-pix_fmt yuv444p` | Higher color, larger |
| yuv420p10le | `-pix_fmt yuv420p10le` | 10-bit HDR |

## Audio Codecs

| Codec | Flag | Bitrate |
|-------|------|---------|
| AAC | `-c:a aac -b:a 128k` | Web-safe (default) |
| MP3 | `-c:a libmp3lame -b:a 192k` | Wide compatibility |
| Opus | `-c:a libopus -b:a 128k` | Best quality/size |
| Vorbis | `-c:a libvorbis -b:a 128k` | WebM |

## Quality Control

- CRF (libx264): 18-28. Lower = better quality, larger file. Default 23.
- Preset (libx264): ultrafast...veryslow. Slower = better compression. Default medium.
- `-movflags +faststart` moves moov atom to start for streaming.

## Critical Rules

1. Always use `-pix_fmt yuv420p` for web compatibility
2. Always use `-movflags +faststart` for streaming
3. Use `-c copy` for trim/mux when no re-encoding is needed
4. Never use `shell=True` — always argument lists

Source: new wrapper work, not a port. FFmpeg repo has no Python.
