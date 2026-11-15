# Remotion React Markup Best Practices

## Compositions

Register in Root.tsx:

```tsx
import { Composition } from "remotion";
import { MyVideo } from "./MyVideo";

export const RemotionRoot = () => (
  <Composition id="MyVideo" component={MyVideo} durationInFrames={300} fps={30} width={1920} height={1080} />
);
```

## Timing

- `useCurrentFrame()` — current frame number
- `interpolate(frame, [0, 30], [0, 1])` — map frame range to value
- `<Sequence from={0} durationInFrames={60}>` — timeline segment
- `<Series>` — sequential segments

## Layout

- `<AbsoluteFill>` — full-frame container
- Use CSS flexbox/grid inside AbsoluteFill
- Video-first sizing: text must be readable at target resolution

## Preserve User Changes

If you detect edits made outside the conversation, don't overwrite them. Assume intentional or ask.

## Editable in Studio

New markup is editable in Studio by default. Structure layers, timing, and styles to be editable.

Source: re-written from remotion-dev/skills research.
