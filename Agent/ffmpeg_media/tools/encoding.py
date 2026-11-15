"""Encoding presets and safe flag validation for ffmpeg."""

from __future__ import annotations

SAFE_VIDEO_CODECS = {"libx264", "libx265", "libvpx", "libvpx-vp9", "gif"}
SAFE_AUDIO_CODECS = {"aac", "libmp3lame", "libopus", "libvorbis"}
SAFE_PIXEL_FORMATS = {"yuv420p", "yuv444p", "yuv420p10le"}

PRESETS = {
    "web_mp4": {
        "video_codec": "libx264",
        "pixel_format": "yuv420p",
        "audio_codec": "aac",
        "audio_bitrate": "128k",
        "extra": ["-movflags", "+faststart"],
        "description": "Web-safe MP4, universally playable",
    },
    "webm": {
        "video_codec": "libvpx-vp9",
        "pixel_format": "yuv420p",
        "audio_codec": "libopus",
        "audio_bitrate": "128k",
        "extra": [],
        "description": "WebM with VP9/Opus",
    },
    "gif": {
        "video_codec": "gif",
        "pixel_format": "yuv420p",
        "audio_codec": None,
        "audio_bitrate": None,
        "extra": [],
        "description": "Animated GIF, no audio",
    },
    "thumbnail": {
        "video_codec": None,
        "pixel_format": "yuv420p",
        "audio_codec": None,
        "audio_bitrate": None,
        "extra": ["-vframes", "1"],
        "description": "Single frame thumbnail",
    },
}


def validate_codec(video_codec: str | None, audio_codec: str | None) -> bool:
    """Validate that codec flags are in the safe set."""
    if video_codec and video_codec not in SAFE_VIDEO_CODECS:
        return False
    if audio_codec and audio_codec not in SAFE_AUDIO_CODECS:
        return False
    return True


def get_preset(name: str) -> dict:
    """Get encoding preset by name."""
    if name not in PRESETS:
        raise ValueError(f"Unknown preset: {name}. Available: {list(PRESETS.keys())}")
    return PRESETS[name]


def build_args(preset_name: str, input_path: str, output_path: str, crf: int = 23) -> list[str]:
    """Build ffmpeg argument list from preset. Never returns a shell string."""
    preset = get_preset(preset_name)
    args = ["ffmpeg", "-i", input_path]
    if preset["video_codec"]:
        args.extend(["-c:v", preset["video_codec"], "-crf", str(crf)])
    if preset["pixel_format"]:
        args.extend(["-pix_fmt", preset["pixel_format"]])
    if preset["audio_codec"]:
        args.extend(["-c:a", preset["audio_codec"]])
    if preset["audio_bitrate"]:
        args.extend(["-b:a", preset["audio_bitrate"]])
    args.extend(preset["extra"])
    args.append(output_path)
    return args


__all__ = ["PRESETS", "SAFE_AUDIO_CODECS", "SAFE_PIXEL_FORMATS", "SAFE_VIDEO_CODECS", "build_args", "get_preset", "validate_codec"]
