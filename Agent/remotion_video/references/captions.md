# Remotion Captions

For transcribing, displaying, and animating captions.

## Basic Captions

```tsx
import { Caption } from "@remotion/captions";

<Caption text="Hello world" startFrame={0} durationInFrames={60} />
```

## Word-Level Animation

Animate each word individually for karaoke-style captions:

```tsx
const words = caption.words;
words.map((word, i) => (
  <span key={i} style={{ opacity: interpolate(frame, [word.startFrame, word.endFrame], [0, 1]) }}>
    {word.text}
  </span>
));
```

Source: re-written from remotion-dev/skills research.
