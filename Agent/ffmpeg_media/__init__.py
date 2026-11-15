"""FFmpeg Media skill — multimedia processing via ffmpeg/ffprobe CLI wrappers.

Ownership:
    CLI-level multimedia processing: probe, trim, mux, transcode. All operations
    use subprocess with argument lists (no shell injection). Complements
    video_generator (AI generation via belt CLI). This skill handles
    post-processing: trim, merge, transcode, extract metadata.

Tools:
    probe — inspect media metadata via ffprobe JSON output
    trim — lossless segment extraction via -ss/-to -c copy
    mux — combine video + audio streams via -map
    transcode — re-encode to web-safe MP4 (libx264, yuv420p, aac)

Runtime integration:
    Results via HostDispatchResult (contract media_record). Host validates
    output file existence. All ffmpeg/ffprobe calls use subprocess.run with
    argument lists, never shell=True.
"""

from agent.skills.ffmpeg_media.run import post_dispatch, pre_dispatch

__all__ = ["post_dispatch", "pre_dispatch"]
