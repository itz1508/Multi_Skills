# FFmpeg Media Skill

## Purpose

CLI-level multimedia processing via ffmpeg/ffprobe: probe metadata, trim segments, mux audio, transcode to web-safe formats. All operations use safe subprocess wrappers (no shell injection). Complements video_generator (AI generation) and remotion_video (code-based creation). This skill handles post-processing.

## Entry Point

```bash
uv run --no-sync python -m agent.skills.ffmpeg_media.run <repository-root>
# Probe:
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4
# Trim:
ffmpeg -i input.mp4 -ss 00:01:00 -to 00:02:00 -c copy output.mp4
# Transcode:
ffmpeg -i input.mp4 -c:v libx264 -pix_fmt yuv420p -c:a aac output.mp4
```

## Tools

- `probe` — Inspect media metadata via ffprobe JSON output
- `trim` — Lossless segment extraction via -ss/-to -c copy
- `mux` — Combine video + audio streams via -map -c copy
- `transcode` — Re-encode to web-safe MP4 (libx264, yuv420p, aac)



| Tool | Inputs | Outputs |
|------|--------|---------|
| `probe` | input_path | dict with format, streams (codec, resolution, fps, duration) |
| `trim` | input_path, output_path, start, end, copy | Trimmed video file |
| `mux` | video_path, audio_path, output_path | Muxed video file with both streams |
| `transcode` | input_path, output_path, crf, preset | Web-safe MP4 file |

## Output

- `ArtifactRef` to processed media (contract `media_record`, v1.0)
- Execution evidence: ffmpeg exit code, output file size, codec, duration
- Disposition: `completed` / `blocked` (missing ffmpeg/ffprobe) / `not_run`

## Ownership

Runtime-authorized media processing, scoped to `ffmpeg`/`ffprobe` subprocess calls with argument lists. Never uses shell=True. Never fabricates media bytes. Complements video_generator and remotion_video.

## Responsibilities

- Probe media files for metadata (codec, resolution, fps, duration, bitrate)
- Trim video segments losslessly (-c copy)
- Mux video and audio streams into one container
- Transcode to web-safe MP4 (libx264, yuv420p, aac, faststart)
- Validate safe encoding flags before execution

## Runtime Integration

- Reports through `HostDispatchResult` with `media_record` contract
- Never issues trusted receipts; host validates output file existence and size
- Host binds approval for outbound ffmpeg/ffprobe calls (default_deny)

## Constraints

- Requires `ffmpeg` and `ffprobe` on PATH — without them, disposition `blocked`
- Install: `apt install ffmpeg` | `brew install ffmpeg` | build from source
- All subprocess calls use argument lists, never shell=True (no shell injection)
- Always use `-pix_fmt yuv420p` for web compatibility
- Always use `-movflags +faststart` for streaming
- Use `-c copy` for trim/mux when no re-encoding is needed
- New wrapper work — FFmpeg repo has no Python bindings
