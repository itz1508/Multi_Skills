"""Video Generator tools — belt and motion modes."""

from agent.skills.video_generator.tools.generate import run_generate
from agent.skills.video_generator.tools.image_to_video import run_image_to_video
from agent.skills.video_generator.tools.avatar import run_avatar
from agent.skills.video_generator.tools.edit import run_edit
from agent.skills.video_generator.tools.upscale import run_upscale
from agent.skills.video_generator.tools.foley import run_foley

# Motion mode tools
from agent.skills.video_generator.tools.motion import render_frames, encode_video, render_motion, check_determinism
from agent.skills.video_generator.tools.audio import detect_beats, get_sfx, synthesize_tone
from agent.skills.video_generator.tools.captions import transcribe, format_srt, sync_captions
from agent.skills.video_generator.tools.critic import contact_sheet, phone_test, loop_check, extract_strip, score_criteria

__all__ = [
    # Belt mode
    "run_generate", "run_image_to_video", "run_avatar", "run_edit", "run_upscale", "run_foley",
    # Motion mode
    "render_frames", "encode_video", "render_motion", "check_determinism",
    "detect_beats", "get_sfx", "synthesize_tone",
    "transcribe", "format_srt", "sync_captions",
    "contact_sheet", "phone_test", "loop_check", "extract_strip", "score_criteria",
]
