---
name: canvas-design
description: Create original static visual artwork by defining a visual philosophy and expressing it as a PDF or PNG. Use for posters, art pieces, and visual artifacts—not application UI implementation.
license: Apache-2.0; see LICENSE.txt
---

# Canvas Design

> Define a distinct visual philosophy, then express it as original static artwork with minimal, intentional text.

> **Source notice:** This is a locally maintained copy of Anthropic's [canvas-design skill](https://github.com/anthropics/skills/tree/main/skills/canvas-design), pinned at repository commit e4bb5d960d87126ff3b3a8af1a104b7db67560ba. The local file has been edited to remove stale user-specific wording and clarify tool/renderer boundaries. Licensed under Apache-2.0; see the adjacent LICENSE.txt.

## When to use

Use when the user asks for an original poster, illustration, art object, or other static visual artifact in PDF or PNG form.

Do not use this skill for application screens, product UI, data dashboards, or implementation of React/CSS components. Use [UIX Designer](../../SKILL.md) for interface design and [video_generator](../../video_generator/SKILL.md) or [remotion_video](../../remotion_video/SKILL.md) for animation/video.

## Inputs and deliverables

Inputs:
- The user's visual brief, subject, intended audience, purpose, and constraints.
- Relevant references or assets the user is authorized to use.
- Available, licensed fonts and a rendering capability.

Deliver:
1. A design philosophy in Markdown.
2. An original PDF or PNG artwork.
3. A brief validation note covering dimensions, margins, text legibility, and whether the exported file opens.

Do not claim that a PDF or PNG was produced unless a real renderer ran and the file was opened or otherwise verified.

## Stage 1 — Create a visual philosophy

Develop an aesthetic direction, not a page layout or a list of generic style adjectives.

1. Name the movement or visual direction in one or two words.
2. Write four to six focused paragraphs covering:
   - Form and spatial structure.
   - Color and material.
   - Scale, repetition, and rhythm.
   - Composition and balance.
   - Typography and visual hierarchy.
3. Explain how the concept should be communicated visually rather than through long explanatory text.
4. Keep each design principle distinct. Avoid repeating the same craftsmanship or color statement in several paragraphs.
5. Leave enough interpretive room for the rendering stage to make concrete visual decisions.

The philosophy should be specific to the brief. Do not make it generic by stripping away the subject's defining ideas.

## Stage 2 — Develop the visual concept

Before rendering, identify the central concept that the artwork should express. A reference may be literal or subtle depending on the user's brief; do not force hidden references where they do not help the work.

Choose:
- The primary visual metaphor or organizing principle.
- The composition and focal hierarchy.
- A constrained palette with actual color values.
- Typography and font roles.
- The intended canvas dimensions and output format.

Create a quick layout sketch or structured composition note where it will prevent ambiguity. Do not substitute a text-heavy document for the artwork.

## Stage 3 — Render and refine

1. Use a rendering tool that is actually available in the current host.
2. Prefer bundled fonts in the adjacent licensed font directory when suitable. Read each font's own license notice before embedding or redistributing it.
3. Do not download arbitrary fonts or assets without checking their source, license, and relevance.
4. Render one page by default unless the user asks for multiple pages.
5. Check that all content fits within the canvas, has adequate margins, and contains no overlaps or clipped text.
6. Review the output at its intended display size; revise composition, spacing, contrast, and typography based on visible defects.
7. Make a refinement pass that improves existing elements before adding unnecessary decoration.

Aim for expert-level craftsmanship, but do not describe work as "human-crafted" or guarantee a quality level that has not been evaluated. Report specific checks and visible limitations.

## Tool and runtime boundary

This file is an instruction set, not a renderer or executable Python package. The local uix_designer/tools/canvas.py currently contains placeholder functions and does not create real PDF/PNG artwork. The host must provide an actual rendering capability (for example, an approved image-generation or design/rendering tool).

The bundled font files have separate license notices. The Apache-2.0 license for this skill does not override those font or data licenses.

## Reader and output checks

Before delivery, ask:
- Does the result satisfy the user's stated purpose and audience?
- Is the central visual idea immediately understandable?
- Are the hierarchy, contrast, margins, and typography readable?
- Are borrowed assets licensed and attributed where required?
- Does the PDF/PNG open and have the expected dimensions?

## Next steps

Present the philosophy and a first visual direction for review when the request calls for iteration. After approval or when the brief authorizes direct execution, render the artwork, inspect the exported file, and deliver the Markdown philosophy with the verified PDF/PNG.
