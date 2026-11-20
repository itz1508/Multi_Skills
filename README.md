# Multi_Skills

A library of **11 top-level reusable agent skills**, plus one nested Canvas Design specialist under UIX Designer. It contains instruction files, reference assets, and selected capability source modules—not a complete agent runtime.

## Skills

| Skill | Purpose |
|---|---|
| [handoff](Agent/handoff/SKILL.md) | Transfer verified task state to a fresh agent and resume without inventing evidence |
| [cross-linker](Agent/cross-linker/SKILL.md) | Find and classify evidence-backed relationships between existing records |
| [memory-bridge](Agent/memory-bridge/SKILL.md) | Compare the provenance of existing knowledge records across tools |
| [session-search](Agent/session-search/SKILL.md) | Retrieve and cite original historical messages from authorized sources |
| [wiki-build](Agent/wiki-build/SKILL.md) | Inspect, archive, rebuild, or restore a scoped knowledge projection |
| [pre-write](Agent/pre-write/SKILL.md) | Reconstruct a technical reference, diagnose gaps, and produce a portable implementation pack |
| [ffmpeg_media](Agent/ffmpeg_media/SKILL.md) | Probe, trim, mux, and transcode existing media |
| [particle_vfx](Agent/particle_vfx/SKILL.md) | Build and validate Three.js/three.quarks particle configuration JSON |
| [remotion_video](Agent/remotion_video/SKILL.md) | Scaffold, preview, and explicitly render React/Remotion compositions |
| [uix_designer](Agent/uix_designer/SKILL.md) | Search UI/UX references, build design guidance, validate data, and audit web guidelines |
| [video_generator](Agent/video_generator/SKILL.md) | Generate video through authenticated belt services or local deterministic motion |

**Nested specialist:** [Canvas Design](Agent/uix_designer/references/canvas-design-SKILL.md) is an instruction set used by UIX Designer for original static artwork. It is not counted as a twelfth top-level package.

## Distribution and runtime boundary

- Every skill is documented at its canonical path under `Agent/`.
- Instruction-only skills can be followed by an agent that has access to their Markdown and the target's authorized sources.
- Code-backed packages are source modules intended for a consuming project. Several import `agent.contracts.host` and expect installation under `agent/skills/<skill>/`; this repository does not include that host runtime or a root Python distribution manifest.
- The `run.py` entrypoints in the media/visual packages are informational or preflight launchers, not complete operation dispatchers. Read each skill's entrypoint boundary before invoking it.
- Optional remote capabilities (for example belt model calls or live web-guideline retrieval) retain their own authentication/network requirements. Local reference search and static validation do not require a provider API key.
- Do not infer runtime integration, test coverage, permissions, or completion from file presence.

## Source and licensing

See [Agent/SOURCES.md](Agent/SOURCES.md) for pinned source attribution and adaptation notes, and [Agent/LICENSE-AR9AV.txt](Agent/LICENSE-AR9AV.txt) / [the Canvas Design license](Agent/uix_designer/references/LICENSE.txt) for the respective third-party license notices. Bundled font/data assets may have separate terms; inspect their accompanying notices.

## Next steps

Choose the skill that matches the task, read its `SKILL.md` and linked references, verify the consuming project's actual prerequisites, then follow its procedure and report the evidence it requires.
