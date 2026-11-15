# Remotion Video Skill

## Purpose

Programmatic video creation via Remotion — React compositions rendered to MP4/WebM. Complements video_generator (AI generation via belt CLI). This skill handles code-based video: React code defines compositions, Studio previews in real-time, render exports to file.

## Entry Point

```bash
uv run --no-sync python -m agent.skills.remotion_video.run <repository-root>
# Scaffold:
npx create-video@latest --yes --blank --no-tailwind .
# Preview (always first):
npx remotion studio --no-open
# Render (only when explicit):
npx remotion render <composition-id> out/video.mp4
```

## Tools

- `scaffold` — Create new Remotion project via `npx create-video`
- `studio` — Start Remotion Studio preview server (always before rendering)
- `render` — Export composition to video file (only on explicit user request)



| Tool | Inputs | Outputs |
|------|--------|---------|
| `scaffold` | target_dir, blank, no_tailwind | Project dir with package.json, Root.tsx |
| `studio` | project_dir, open_browser | Long-running preview server URL |
| `render` | composition_id, output_path, project_dir, codec, quality | Video file (MP4/WebM/GIF) |

## Output

- `ArtifactRef` to rendered video (contract `video_record`, v1.0)
- Execution evidence: npx exit code, output file size, codec, duration
- Disposition: `completed` / `blocked` (missing npx/Node.js) / `not_run`

## Ownership

Runtime-authorized programmatic video creation, scoped to `npx` subprocess calls. Never fabricates video bytes; all output is Remotion-rendered files. Complements video_generator — does not replace AI generation.

## Responsibilities

- Scaffold Remotion projects with `create-video`
- Start Studio preview before building or rendering (Studio-first workflow)
- Render compositions to MP4/WebM/GIF on explicit user request only
- Route to reference files by intent: create → create-video.md, render → rendering.md, markup → markup.md, captions → captions.md, maps → maps.md

## Runtime Integration

- Reports through `HostDispatchResult` with `video_record` contract
- Never issues trusted receipts; host validates output file existence and size
- Host binds approval for outbound npx calls (default_deny)

## Constraints

- Requires Node.js >=18 and npx on PATH — without them, disposition `blocked`
- Studio-first: never render without previewing first
- Render only when user is very explicit ("Render", "Export", "Give me the MP4")
- Preserve user changes: don't overwrite edits made outside the conversation
- Max composition duration depends on system resources
- Different from video_generator: code-based creation vs AI generation
