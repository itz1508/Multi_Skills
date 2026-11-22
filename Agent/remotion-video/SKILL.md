---
name: remotion-video
description: Scaffold, preview, and render code-defined videos with Remotion and React. Use when the user needs programmatic compositions; render only after an explicit export request.
metadata:
  runtime_package: "remotion_video"
---

# Remotion Video

> Create video compositions as React code, preview them in Remotion Studio, and render only when the user explicitly requests an export.

## When to use

Use for code-driven video where React components define scenes, timing, transitions, and composition. Use [video_generator](../video-generator/SKILL.md) for model-generated footage, and [ffmpeg_media](../ffmpeg-media/SKILL.md) for post-processing an existing file.

## Ownership and boundaries

- Owns Remotion project scaffolding, Studio preview, and composition rendering.
- Does not own AI video generation.
- Scaffolding and rendering invoke npx subprocesses. The consuming host must authorize package execution and validate resulting files.
- Never render or overwrite an existing output unless the user explicitly requests that export and replacement is authorized.

## Prerequisites and installation

- Node.js 18 or newer and npx.
- A consuming project with the Remotion package dependencies installed.
- In the consuming Python host, place this package at agent/skills/remotion_video/; the hook entrypoint also expects agent.contracts.host, which is not included in this repository.
- The code in this library is not an independently installable Python package.

## Importable operations

~~~python
from agent.skills.remotion_video.tools.scaffold import scaffold_project
from agent.skills.remotion_video.tools.studio import start_studio
from agent.skills.remotion_video.tools.render import render_video
~~~

| Function | Inputs | Result |
|---|---|---|
| scaffold_project(target_dir, blank=True, no_tailwind=True) | Destination directory and scaffold options | Status/evidence dict |
| start_studio(project_dir, open_browser=False) | Existing Remotion project | Starts a long-running Studio process and returns initial status/URL evidence |
| render_video(composition_id, output_path, project_dir, codec="h264", quality=80) | Composition ID, destination, project root, codec/quality | Status/evidence dict |

tools/__init__.py does not currently re-export these functions. Import from the concrete modules shown above.

## Procedure

1. Inspect the target repository's package manager, Node version, Remotion version, and current project tree.
2. If no Remotion project exists, confirm the destination is safe and obtain authorization before scaffolding. create-video@latest can download and execute package code.
3. Start Studio and review the composition before rendering.
4. Make changes without overwriting user-authored components or assets.
5. Render only after an explicit request such as "render," "export," or "give me the MP4."
6. Verify the output file, codec, duration, dimensions, and expected composition.

## Commands

~~~bash
npx create-video@latest --yes --blank --no-tailwind .
npx remotion studio --no-open
npx remotion render <composition-id> out/video.mp4
~~~

Run commands from the consuming Remotion project root, not from the Multi_Skills repository root.

## Entry point behavior

run.py checks for Node.js/npx and prints the scaffold, preview, and render commands. It does not call the three operation functions or execute the video workflow.

## Outputs and verification

- Scaffolded React/Remotion project when requested.
- Preview server URL/status from Studio.
- Rendered MP4/WebM/GIF file when explicitly requested.
- Host integration expects a video_record or build_record reference. The consuming host must independently check the output file and media metadata.

## Failure handling

- Missing Node.js or npx: report blocked.
- Scaffold install or render subprocess error: return the actual stderr/exit status.
- Studio not started or composition not reviewed: do not proceed to render.
- Render not explicitly requested: leave the project at preview/review; do not export.

## Evaluation fixtures

`evals/evals.json` contains representative positive, edge, and scope-boundary prompts with observable expectations. These fixtures define what a compatible host should test; their presence does not prove that a host discovered this Skill, invoked it, or executed bundled capabilities.

When changing this Skill, preserve positive cases and adjacent-scope boundary cases. Add cases only for uncovered behavior, and keep expectations tied to observable evidence rather than preferred wording.

## Next steps

Scaffold only when needed, preview the composition, and wait for explicit export authorization before rendering.
