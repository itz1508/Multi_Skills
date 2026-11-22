# Multi_Skills

A library of **11 top-level reusable Agent Skills**, plus one nested Canvas Design specialist under UIX Designer. Each Skill has a portable kebab-case identity, a focused `SKILL.md` entrypoint, and representative evaluation fixtures. Code-backed Skills also include capability source modules; this repository is not a complete agent runtime.

## Skills

| Skill | Purpose |
|---|---|
| [handoff](Agent/handoff/SKILL.md) | Transfer verified task state to a fresh agent and resume without inventing evidence |
| [cross-linker](Agent/cross-linker/SKILL.md) | Find and classify evidence-backed relationships between existing records |
| [memory-bridge](Agent/memory-bridge/SKILL.md) | Compare provenance of existing knowledge records across tools |
| [session-search](Agent/session-search/SKILL.md) | Retrieve and cite original historical messages from authorized sources |
| [wiki-build](Agent/wiki-build/SKILL.md) | Inspect, archive, rebuild, or restore a scoped knowledge projection |
| [pre-write](Agent/pre-write/SKILL.md) | Reconstruct technical references, trace SDK behavior, diagnose gaps, and package reusable capabilities |
| [ffmpeg-media](Agent/ffmpeg-media/SKILL.md) | Probe, trim, mux, and transcode existing media |
| [particle-vfx](Agent/particle-vfx/SKILL.md) | Build and validate Three.js/three.quarks particle configuration JSON |
| [remotion-video](Agent/remotion-video/SKILL.md) | Scaffold, preview, and explicitly render React/Remotion compositions |
| [uix-designer](Agent/uix-designer/SKILL.md) | Search UI/UX references, build design guidance, validate data, and audit web guidelines |
| [video-generator](Agent/video-generator/SKILL.md) | Generate video through authenticated belt services or deterministic local motion |

**Nested specialist:** [Canvas Design](Agent/uix-designer/references/canvas-design-SKILL.md) is a nested instruction set used by UIX Designer for original static artwork. It is not counted as a twelfth top-level Skill.

## Packaging and runtime boundary

- Top-level Skill IDs use lowercase kebab-case and match their source directory names.
- Five code-backed Skills keep their Python import/package names in snake_case. Their frontmatter `metadata.runtime_package` records this intentional mapping; do not rename import paths to match the Skill ID.
- Code-backed source packages are intended for a consuming project. Their runtime installation paths, including `agent/skills/ffmpeg_media/` and the other mapped package names, are documented in each Skill.
- Several packages import `agent.contracts.host`; this library does not include that consuming Host contract, a complete agent runtime, or a root Python distribution manifest.
- Some `run.py` files are informational/preflight launchers, not full operation dispatchers. Read each Skill before treating a script as an executable CLI.
- Optional remote capabilities retain their own authentication and network requirements. Do not make provider credentials prerequisites for unrelated local operations.

## Evaluation fixtures

Each top-level Skill and the nested Canvas Design specialist includes `evals/evals.json` with three representative positive, edge, or adjacent-scope prompts and observable expectations. The files define cases for a compatible host; they are not activation receipts, execution logs, or benchmark results. Structural checks, real Skill activation, and capability execution must be reported separately.

## Source and licensing

See [Agent/SOURCES.md](Agent/SOURCES.md) for pinned source attribution and adaptation notes, and [Agent/LICENSE-AR9AV.txt](Agent/LICENSE-AR9AV.txt) / [the Canvas Design license](Agent/uix-designer/references/LICENSE.txt) for the respective third-party license notices. Bundled fonts and data assets may have separate terms; inspect their accompanying notices.
