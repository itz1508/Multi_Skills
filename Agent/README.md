# Agent Skills and capability sources

The library contains **11 top-level Agent Skills** plus the nested Canvas Design specialist. Each top-level Skill has a portable kebab-case identity, a matching source directory, a focused `SKILL.md`, and an evaluation set.

## Skill catalog

| Skill ID | Entry point | Intended use |
|---|---|---|
| Handoff | [handoff/SKILL.md](handoff/SKILL.md) | Preserve verified state and resume a bounded engineering task |
| Cross Linker | [cross-linker/SKILL.md](cross-linker/SKILL.md) | Assess evidence-backed relationships between existing records |
| Memory Bridge | [memory-bridge/SKILL.md](memory-bridge/SKILL.md) | Compare source provenance across knowledge projections |
| Session Search | [session-search/SKILL.md](session-search/SKILL.md) | Retrieve original session messages and bounded excerpts |
| Wiki Build | [wiki-build/SKILL.md](wiki-build/SKILL.md) | Inspect, archive, rebuild, or restore an existing knowledge index/wiki |
| Pre-Write | [pre-write/SKILL.md](pre-write/SKILL.md) | Reconstruct technical references and transfer portable capabilities |
| FFmpeg Media | [ffmpeg-media/SKILL.md](ffmpeg-media/SKILL.md) | Process existing media using ffmpeg/ffprobe |
| Particle VFX | [particle-vfx/SKILL.md](particle-vfx/SKILL.md) | Build Three.js/three.quarks particle configuration JSON |
| Remotion Video | [remotion-video/SKILL.md](remotion-video/SKILL.md) | Scaffold, preview, and render programmatic React videos |
| UIX Designer | [uix-designer/SKILL.md](uix-designer/SKILL.md) | Search design references, produce design guidance, and audit web UI |
| Video Generator | [video-generator/SKILL.md](video-generator/SKILL.md) | Generate model-based or deterministic motion video |

### Nested specialist

- [Canvas Design](uix-designer/references/canvas-design-SKILL.md) — original static visual artwork. It is a nested instruction file, not a separate top-level Skill directory.

## Python package-name mapping

The Skill ID is the portable discovery name. Existing Python source/import names remain unchanged for consuming projects:

| Skill ID | Runtime Python package | Consumer package path |
|---|---|---|
| ffmpeg-media | `ffmpeg_media` | `agent/skills/ffmpeg_media/` |
| particle-vfx | `particle_vfx` | `agent/skills/particle_vfx/` |
| remotion-video | `remotion_video` | `agent/skills/remotion_video/` |
| uix-designer | `uix_designer` | `agent/skills/uix_designer/` |
| video-generator | `video_generator` | `agent/skills/video_generator/` |

The frontmatter field `metadata.runtime_package` declares this mapping. Keep Python imports such as `agent.skills.uix_designer.tools.search` unchanged; the portable Skill ID is not a Python module identifier.

## Package and resource contract

- `SKILL.md` is the agent-facing entry point. It defines activation, ownership, procedure, outputs, boundaries, and references.
- `references/`, `examples/`, `scripts/`, `templates/`, and `assets/` remain supporting resources; load only what the current task needs.
- `evals/evals.json` stores representative positive, edge, and adjacent-scope prompts with observable expectations. These are fixtures, not proof of runtime behavior.
- Third-party attribution and licensing remain in [SOURCES.md](SOURCES.md) and the relevant license files.

## Runtime and execution boundaries

- Instruction-only Skills do not require a provider SDK; they do require access to authorized source material and target-repository context.
- Code-backed packages are source modules, not standalone wheels. Several import `agent.contracts.host`; the consuming project must provide that Host contract.
- Some `run.py` files only print preflight information or command examples. Concrete operations may live in separate `tools/` modules.
- Skills do not create workflow stages or grant approval, source-write, Runtime, shell, network, or subprocess permissions.
- Read the target repository's actual bootstrap, source, dependencies, and authorization rules before installing or invoking code.

## Evaluation evidence

The repository supports static checks of metadata, directory identity, local references, evaluation JSON, and package inventory. It does not supply a universal agent Skill runtime. Actual triggering/selection, instruction adherence, and capability execution must be tested in the consuming host and reported as separate evidence.

## Next steps

Select a Skill from the catalog, read its complete `SKILL.md`, and verify whether the task needs instruction-only guidance or target-host code integration before execution.
