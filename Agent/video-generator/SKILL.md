---
name: video-generator
description: Generate or transform video through authenticated belt model calls or a local deterministic motion pipeline. Use belt for model-generated footage and motion for code-driven UI/data animation.
metadata:
  runtime_package: "video_generator"
---

# Video Generator

> Choose either authenticated model generation (belt) or the local seek(t) motion pipeline; keep their dependencies, network behavior, and evidence separate.

## When to use

Use for AI-generated video, image-to-video, avatar/lip-sync, video editing/upscaling/foley, or deterministic code-driven motion.

Use [remotion_video](../remotion-video/SKILL.md) when the deliverable is a React/Remotion composition. Use [ffmpeg_media](../ffmpeg-media/SKILL.md) for post-processing an existing media file.

## Modes and dependencies

| Mode | Intended use | External requirements |
|---|---|---|
| belt | Prompt-to-video, image-to-video, avatar, edit, upscale, foley | belt CLI, authenticated belt login, network, and the selected remote model/service |
| motion | UI motion, data stories, typography, beat-synced animation | Playwright/Chromium and ffmpeg; optional librosa, WhisperX and related local models depending on selected tools |

Motion rendering can be local, but the overall motion toolbox is not unconditionally offline: get_sfx calls the Openverse API, and model/transcription dependencies may need separate installation or model downloads. Do not describe every motion operation as offline.

## Ownership and boundaries

- Belt mode calls the configured belt service through subprocess commands; it does not call an OpenAI or Anthropic SDK directly.
- Motion mode renders deterministic frames from seek(t) content and encodes them with ffmpeg.
- The skill does not fabricate media bytes or claim that a generated file is correct without checking its metadata and content.
- Use only user-provided or explicitly approved media inputs. Do not read an unrestricted repository or upload private assets to a remote model without authorization.

## Host installation

- Place this package at agent/skills/video_generator/ in the consuming project.
- The host-integrated run.py imports agent.contracts.host, which is not included in this library.
- This repository does not include a standalone Python distribution manifest for this package.

## Entry point versus operations

run.py is an informational launcher. It prints guidance for belt or motion mode; it does not orchestrate the full generation pipeline. In particular, its current main() does not parse --brief or --output arguments. Do not rely on those flags as working CLI options.

The package's tools/__init__.py re-exports callable tools, including:

- Belt: run_generate, run_image_to_video, run_avatar, run_edit, run_upscale, run_foley.
- Motion: render_frames, encode_video, render_motion, check_determinism, detect_beats, get_sfx, synthesize_tone, transcribe, format_srt, sync_captions, contact_sheet, phone_test, loop_check, extract_strip, score_criteria.

Use the consuming project's installed module path:

~~~python
from agent.skills.video_generator.tools import (
    run_generate,
    render_motion,
    check_determinism,
)
~~~

## Procedure

1. Confirm mode, final format, aspect ratio, duration, target platform, and source assets.
2. Confirm input rights and whether any asset may be sent to an external service.
3. For belt, confirm CLI availability and authentication before invoking a paid/remote model. Record the belt run ID and selected model.
4. For motion, ensure seek(t) is deterministic; render the same frame twice and compare hashes before encoding.
5. Review a contact sheet and the worst-scoring frames before final export.
6. Verify duration, frame rate, dimensions, audio, loop behavior, and output digest as applicable.

## Outputs and evidence

- Video artifact path/reference and output metadata.
- Belt: model ID, belt run ID, duration, resolution, and available pre/post digests.
- Motion: frame count, fps, determinism result, contact-sheet path, and critic findings.
- Host contract: expected video_record reference. The host must independently validate the artifact.

Use dispositions completed, blocked, and not_run accurately. A missing token or tool is blocked, not a successful empty run.

## Motion pipeline checkpoints

1. Approve source references and product assets.
2. Approve the style guide and shot list.
3. Generate and critique stills for each shot.
4. Review the 960x540 animatic with placeholder audio.
5. Complete motion, polish, and sound.
6. Verify formats, loop behavior, poster frame, and README.

## Evaluation fixtures

`evals/evals.json` contains representative positive, edge, and scope-boundary prompts with observable expectations. These fixtures define what a compatible host should test; their presence does not prove that a host discovered this Skill, invoked it, or executed bundled capabilities.

When changing this Skill, preserve positive cases and adjacent-scope boundary cases. Add cases only for uncovered behavior, and keep expectations tied to observable evidence rather than preferred wording.

## Next steps

Choose the mode, confirm its credentials/dependencies and data-sharing boundary, then produce and review a small representative output before final render.
