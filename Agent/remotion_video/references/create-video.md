# Creating a Remotion Video

## Scaffold

If no project exists, scaffold one:

```bash
npx create-video@latest --yes --blank --no-tailwind .
```

For a non-empty folder, scaffold into a subfolder:

```bash
npx create-video@latest --yes --blank --no-tailwind my-video
cd my-video
```

## Studio First

Open the preview before building. Keep Studio running while working:

```bash
npx remotion studio --no-open
```

## Designing a Video

1. Register `<Composition>` in Root.tsx
2. Write React markup for each scene
3. Use `<Sequence>` for timeline segments
4. Use `<AbsoluteFill>` for full-frame layers
5. Use `<Img>`, `<Video>`, `<Audio>` for media

## Multi-Scene

For multi-scene videos, use `<Series>` or `<Sequence>` with `from` and `durationInFrames`.

## Is This a Timeline of Clips?

If the video arranges multiple clips on a timeline, give every clip its own authored JSX node for independent editing.

Source: re-written from remotion-dev/skills research.
