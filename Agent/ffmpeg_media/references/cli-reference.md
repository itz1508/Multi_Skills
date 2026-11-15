# FFmpeg CLI Reference

## Probe

```bash
ffprobe -v quiet -print_format json -show_format -show_streams <input>
```

## Trim (Lossless)

```bash
ffmpeg -i <input> -ss 00:01:00 -to 00:02:00 -c copy <output>
```

`-ss` before `-i` is fast but seeks to nearest keyframe. After `-i` is frame-accurate but slow.

## Mux Audio

```bash
ffmpeg -i <video> -i <audio> -c copy -map 0:v -map 1:a <output>
```

## Transcode Web MP4

```bash
ffmpeg -i <input> -c:v libx264 -pix_fmt yuv420p -crf 23 -preset medium -c:a aac -b:a 128k -movflags +faststart <output>
```

## Thumbnail

```bash
ffmpeg -i <input> -ss 00:00:01 -vframes 1 -q:v 2 <output.jpg>
```

## Stream Copy

`-c copy` avoids re-encoding. Use for trim and mux. Seconds, not minutes.

Source: new wrapper work. FFmpeg repo has no Python.
