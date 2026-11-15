"""Remotion Video skill — programmatic video creation via React + npx.

Ownership:
    Code-based video creation via Remotion (React compositions rendered to MP4/WebM).
    Complements video_generator (AI generation via belt CLI). This skill handles
    programmatic video: React code that defines compositions, rendered headlessly.

Tools:
    scaffold — create new Remotion project via npx create-video
    studio — start Remotion Studio preview server (always before rendering)
    render — export composition to video file (only on explicit user request)

Runtime integration:
    Results via HostDispatchResult (contract video_record). Host validates
    output file existence and size. Studio-first workflow: never render without
    preview.
"""

from agent.skills.remotion_video.run import post_dispatch, pre_dispatch

__all__ = ["post_dispatch", "pre_dispatch"]
