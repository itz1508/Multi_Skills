# Video Generator Skill

## Purpose
Dual-mode video generation: (1) AI video via inference.sh belt CLI (Veo 3.1, Seedance 2.0, HappyHorse, Wan 2.5, Grok Imagine, OmniHuman, Fabric, HunyuanVideo), and (2) code-driven deterministic motion via the seek(t) frame pipeline (Playwright + ffmpeg) for UI motion, data stories, typography, and launch explainers.

## Modes

| Mode | Use Case | Pipeline |
|------|----------|----------|
| `belt` | Photoreal scenes, complex characters, organic movement | AI model inference via belt CLI |
| `motion` | UI motion, data stories, typography, launch explainers | seek(t) → Playwright frames → ffmpeg encode |

## Entry Point
```bash
uv run --no-sync python -m agent.skills.video_generator.run <repository-root>
# Belt mode:
belt login
belt app run google/veo-3-1-fast --input '{"prompt": "drone shot flying over a forest"}'
# Motion mode:
python -m agent.skills.video_generator.run <repo> --mode motion --brief brief.md --output out/
```

## Belt Tools
- `generate` — Text-to-video via belt app (Veo, HappyHorse T2V, Seedance T2V)
- `image_to_video` — Animate image to video (Wan 2.5, Seedance I2V, HappyHorse I2V/R2V)
- `avatar` — Lipsync/avatar animation (OmniHuman, Fabric, PixVerse)
- `edit` — Natural language video editing (HappyHorse Edit)
- `upscale` — Video upscaling (Topaz)
- `foley` — Add sound effects (HunyuanVideo Foley)
- `merger` — Merge clips with transitions (Media Merger)

## Motion Tools
- `render_motion` — Full seek(t) pipeline: HTML → Playwright frames → ffmpeg video
- `detect_beats` — librosa beat detection for music-synced animation
- `get_sfx` — Openverse API sound effects search (5.2M+ free assets)
- `transcribe` — WhisperX word-level timing for captions
- `contact_sheet` — ffmpeg contact sheet for self-evaluation
- `critic` — Score rendered frames and identify worst defects

## Output
- `ArtifactRef` to generated video (contract `video_record`, v1.0)
- Belt mode: belt run ID, model, duration, resolution, pre/post digests
- Motion mode: frame count, fps, determinism hash, contact sheet path, critic scores
- Disposition: `completed` / `blocked` (missing deps) / `not_run`

## Ownership
Runtime-authorized media generation. Belt mode: scoped to bearer-auth belt calls. Motion mode: scoped to local Playwright + ffmpeg + librosa subprocess calls. Never fabricates video bytes.

## Responsibilities
- Belt: text-to-video with audio, image-to-video, avatar/lipsync, edit, foley, upscale, merge
- Motion: deterministic seek(t) rendering, spring physics, beat-synced animation, contact-sheet self-evaluation, 6-gate quality control

## Runtime Integration
- Reports through `HostDispatchResult` with `video_record` contract
- Belt mode: host validates belt `artifact_digest`; host binds approval for outbound belt calls (default_deny)
- Motion mode: host validates determinism hash; no outbound network calls required

## Constraints
- Belt mode: requires `belt login` (INFERENCE_SH token) — without it, disposition `blocked`
- Motion mode: requires Playwright (`npx playwright install chromium`), ffmpeg, and optionally librosa — missing deps yield `blocked`
- No whole-repository read; only explicit prompt/image/audio URLs or local file paths
- Max duration/resolution per model table in references/models.md
- Motion mode: seek(t) must be a pure function of time — no Math.random, setTimeout, or CSS transitions in render mode
- Motion mode: determinism check required — render frame N twice, hashes must match

## Motion Pipeline Gates
1. References and product assets approved
2. Style guide and shot list approved
3. Stills for every shot, critiqued
4. Animatic at 960x540 with placeholder audio
5. Full pass, polish, sound
6. Formats, loop check, poster frame, README
