# Agent skills and capability sources

> Summary: 11 top-level skills plus one nested Canvas Design specialist. Each entry has an explicit trigger, owner, prerequisites, output, verification boundary, and next action.

## Skill catalog

| Skill | Entry point | Intended use |
|---|---|---|
| Handoff | [handoff/SKILL.md](handoff/SKILL.md) | Preserve verified state and resume a bounded engineering task |
| Cross Linker | [cross-linker/SKILL.md](cross-linker/SKILL.md) | Assess evidence-backed relationships between existing records |
| Memory Bridge | [memory-bridge/SKILL.md](memory-bridge/SKILL.md) | Compare source provenance across knowledge projections |
| Session Search | [session-search/SKILL.md](session-search/SKILL.md) | Retrieve original session messages and bounded excerpts |
| Wiki Build | [wiki-build/SKILL.md](wiki-build/SKILL.md) | Inspect, archive, rebuild, or restore an existing knowledge index/wiki |
| Pre-Write | [pre-write/SKILL.md](pre-write/SKILL.md) | Reconstruct technical references and generate a portable Agent Implementation Pack |
| FFmpeg Media | [ffmpeg_media/SKILL.md](ffmpeg_media/SKILL.md) | Process existing media using ffmpeg/ffprobe |
| Particle VFX | [particle_vfx/SKILL.md](particle_vfx/SKILL.md) | Build Three.js/three.quarks particle configuration JSON |
| Remotion Video | [remotion_video/SKILL.md](remotion_video/SKILL.md) | Scaffold, preview, and render programmatic React videos |
| UIX Designer | [uix_designer/SKILL.md](uix_designer/SKILL.md) | Search design references, produce design guidance, and audit web UI |
| Video Generator | [video_generator/SKILL.md](video_generator/SKILL.md) | Generate model-based or deterministic motion video |

### Nested specialist

- [Canvas Design](uix_designer/references/canvas-design-SKILL.md) — instruction-only workflow for visual philosophy and original static artwork, used through UIX Designer.

## Packaging and execution boundaries

- Instruction-only skills do not require a provider SDK; they do require access to their authorized source material and target repository context.
- Code-backed packages are source modules, not standalone wheels. In the consuming project they are expected under `agent/skills/<skill>/`.
- The media/visual package entrypoints import `agent.contracts.host`. This library does not ship that host contract, the host runtime, or a root `pyproject.toml`.
- Some `run.py` files only print preflight information and command examples. Their callable operation functions live in separate `tools/` modules. Read each `SKILL.md` before treating an entrypoint as an executable CLI.
- A callable function is not a stable public SDK facade unless the package explicitly exports and documents it. Use the exact imports shown by the skill.
- Provider credentials and outbound network access are capability-specific. Do not make them prerequisites for unrelated local operations.

## Shared boundaries

- Skills do not create workflow stages or grant approval, source-write, or Runtime privileges.
- Read the target repository's actual bootstrap, source, dependencies, and authorization rules before installing or invoking any code.
- Preserve original upstream attribution and license terms for adapted or copied references.
- Keep generated outputs separate from templates and bundled reference data.

## Next steps

Select one skill from the catalog, read its complete `SKILL.md`, and verify whether the task needs instruction-only guidance or target-host code integration before execution.
