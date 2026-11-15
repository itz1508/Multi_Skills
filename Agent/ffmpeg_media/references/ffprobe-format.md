# ffprobe JSON Output Format

## Command

```bash
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4
```

## Response Structure

```json
{
  "format": {
    "filename": "input.mp4",
    "duration": "120.5",
    "size": "15000000",
    "bit_rate": "995022"
  },
  "streams": [
    {
      "codec_type": "video",
      "codec_name": "h264",
      "width": 1920,
      "height": 1080,
      "r_frame_rate": "30/1",
      "pix_fmt": "yuv420p"
    },
    {
      "codec_type": "audio",
      "codec_name": "aac",
      "sample_rate": 44100,
      "channels": 2
    }
  ]
}
```

## Key Fields

| Path | Meaning |
|------|---------|
| `format.duration` | Duration in seconds (string) |
| `format.size` | File size in bytes (string) |
| `format.bit_rate` | Overall bitrate (string) |
| `streams[video].width/height` | Resolution |
| `streams[video].r_frame_rate` | Frame rate as fraction |
| `streams[video].pix_fmt` | Pixel format |
| `streams[audio].sample_rate` | Audio sample rate |
| `streams[audio].channels` | Audio channel count |

Source: new wrapper work. FFmpeg repo has no Python bindings.
