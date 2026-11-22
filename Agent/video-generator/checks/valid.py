"""Checks for prompt → video validity."""

from __future__ import annotations


def check_prompt_valid(prompt: str) -> bool:
    return isinstance(prompt, str) and 1 <= len(prompt.strip()) <= 5000


def check_duration_valid(duration: int | None, model: str) -> bool:
    if duration is None:
        return True
    max_by_model = {
        "alibaba/happyhorse-1-0-t2v": 15,
        "bytedance/seedance-2-0": 10,
        "xai/grok-imagine-video": 10,
    }
    limit = max_by_model.get(model, 10)
    return 1 <= duration <= limit


def check_resolution_valid(resolution: str | None) -> bool:
    if resolution is None:
        return True
    return resolution in ("480P", "720P", "1080P", "1080p")


def check_fps_valid(fps: int) -> bool:
    """Motion mode: validate frame rate."""
    return isinstance(fps, int) and 1 <= fps <= 120


def check_seek_html_valid(html: str) -> bool:
    """Motion mode: validate seek(t) contract in HTML."""
    if not isinstance(html, str) or len(html) < 50:
        return False
    must_have = ["seek", "function"]
    banned = ["Math.random()", "setTimeout", "requestAnimationFrame"]
    has_all = all(k in html for k in must_have)
    has_banned = any(b in html for b in banned)
    return has_all and not has_banned


def check_determinism(hash_a: str, hash_b: str) -> bool:
    """Motion mode: two renders of the same frame must produce identical hashes."""
    return isinstance(hash_a, str) and isinstance(hash_b, str) and hash_a == hash_b and len(hash_a) > 0


def check_aspect_ratio_valid(ratio: str) -> bool:
    """Motion mode: validate aspect ratio string."""
    return ratio in ("16:9", "9:16", "1:1", "4:3", "21:9")


__all__ = [
    "check_aspect_ratio_valid",
    "check_determinism",
    "check_duration_valid",
    "check_fps_valid",
    "check_prompt_valid",
    "check_resolution_valid",
    "check_seek_html_valid",
]
