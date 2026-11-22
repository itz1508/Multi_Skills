---
name: ffmpeg-media
description: Probe, trim, mux, and transcode local audio/video files with ffmpeg and ffprobe. Use for deterministic media post-processing, not AI generation or React composition authoring.
metadata:
  runtime_package: "ffmpeg_media"
---

# FFmpeg Media

> Post-process existing local media with bounded ffmpeg/ffprobe commands and verify the resulting file.

## When to use

Use this skill to inspect media metadata, trim a segment, combine audio and video streams, or transcode a file to a web-compatible MP4.

Do not use it to generate video from prompts, author React/Remotion compositions, or create particle effects. Use [video_generator](../video-generator/SKILL.md) for AI/motion generation and [remotion_video](../remotion-video/SKILL.md) for programmatic compositions.

## Ownership and boundaries

- Owns local media probing and post-processing only.
- Uses ffmpeg and ffprobe subprocesses with argument arrays; it does not use shell=True.
- Does not generate media bytes by itself and does not issue trusted execution receipts.
- The consuming host must approve process execution and independently validate the output artifact.

## Prerequisites and installation

- Python 3.10 or newer for the supplied modules.
- ffmpeg and ffprobe installed and available on PATH.
- In a consuming project, place this package at agent/skills/ffmpeg_media/.
- The host-integrated entrypoint imports agent.contracts.host. That contract is not included in this skill library; install only into a project that supplies the expected host interface.

This repository does not include a standalone Python distribution manifest for this package.

## Entry point versus operations

run.py is an informational preflight entrypoint: it checks whether ffmpeg and ffprobe are on PATH and prints example commands. It does not dispatch probe, trim, mux, or transcode operations.

The reusable operations are in tools/ffmpeg_ops.py:

~~~python
from agent.skills.ffmpeg_media.tools.ffmpeg_ops import (
    probe_media,
    trim_video,
    mux_audio,
    transcode_web_mp4,
)
~~~

| Function | Inputs | Result |
|---|---|---|
| probe_media(input_path) | Local media path | Dict with status and ffprobe metadata |
| trim_video(input_path, output_path, start="00:00:00", end=None, copy=True) | Source, destination, time range | Dict with execution status and output evidence |
| mux_audio(video_path, audio_path, output_path) | Video, audio, destination | Dict with execution status and output evidence |
| transcode_web_mp4(input_path, output_path, crf=23, preset="medium") | Source, destination, encoder quality/speed | Dict with execution status and output evidence |

The status field is an operation result (completed, error, or blocked); it is not a substitute for host-level artifact validation.

## Procedure

1. Confirm the input paths, intended output path, and operation.
2. Check that the source files exist and inspect relevant streams with probe_media.
3. Choose the least destructive operation:
   - use stream copy when re-encoding is unnecessary;
   - transcode only when codec, pixel format, or container compatibility requires it.
4. Execute the operation through the supplied function or an explicitly approved command.
5. Verify the output exists, is non-empty, and can be probed. Check codec, duration, resolution, and audio/video streams against the request.

Stream-copy trimming avoids re-encoding, but cut positions can be constrained by keyframes; do not promise frame-exact cuts without checking the produced file.

## Command examples

~~~bash
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4
ffmpeg -i input.mp4 -ss 00:01:00 -to 00:02:00 -c copy output.mp4
ffmpeg -i input.mp4 -c:v libx264 -pix_fmt yuv420p -c:a aac -movflags +faststart output.mp4
~~~

Run commands only after confirming the selected input and output paths. Preserve argument-list subprocesses when adding wrapper operations.

## Outputs and verification

- Probe result: input path plus parsed format and stream metadata.
- Processing result: operation status, output path/evidence, and stderr when available.
- Host artifact contract: expected media_record, video_record, or build_record reference. The current post_dispatch hook checks artifact identity and contract ID; the consuming host must still verify file existence, size, and media metadata independently.

Report the exact command/function, exit or operation status, output path, codec, duration, and checks not performed.

## Failure handling

- Missing ffmpeg or ffprobe: report blocked; do not silently skip processing.
- Non-zero subprocess exit: report error and the relevant stderr.
- Invalid or empty output: do not report the operation as completed.
- Never overwrite an input or existing user output unless the user explicitly authorized replacement.

## Evaluation fixtures

`evals/evals.json` contains representative positive, edge, and scope-boundary prompts with observable expectations. These fixtures define what a compatible host should test; their presence does not prove that a host discovered this Skill, invoked it, or executed bundled capabilities.

When changing this Skill, preserve positive cases and adjacent-scope boundary cases. Add cases only for uncovered behavior, and keep expectations tied to observable evidence rather than preferred wording.

## Next steps

Probe the source first, perform only the requested transformation, then validate the output media before handing back its path and evidence.
