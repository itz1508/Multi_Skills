---
name: uix_designer
description: Search the local UI/UX reference dataset, assemble design-system guidance, validate reference data, and audit web-interface guidelines. Use for design research and review, not as proof that an interface is implemented or accessible.
---

# UIX Designer

> Use the local UI/UX reference corpus to inform design decisions, then validate the actual interface against current guidance and target-platform constraints.

## When to use

Use for UI/UX research, design-system recommendations, token and component guidance, typography and chart selection, reference-data validation, or a web-interface guideline audit.

Use the nested [Canvas Design instructions](references/canvas-design-SKILL.md) only when the user requests original static visual artwork. It is a specialist instruction set, not a general UI implementation tool.

## Capabilities and ownership

| Capability | Local owner | Input | Result |
|---|---|---|---|
| UI/UX search | tools/search.py and tools/core.py | Query, optional domain/stack | Ranked local reference results |
| Design-system generation | tools/design_system.py | Project brief and stack context | Design-system data/Markdown/JSON |
| Reference data validation | tools/validate_data.py | Bundled CSV/JSON data | Integrity findings and exit status |
| Web guideline retrieval | tools/web_guidelines.py and checks/guideline.py | Network access and target files | Current Vercel guideline text and file:line findings |
| Canvas instructions | references/canvas-design-SKILL.md | User art brief | Design philosophy plus artwork when a compatible renderer is available |

The local reference corpus is under references/ui-ux-data/. Use catalog-summary.json and data-provenance.json for dataset counts and provenance; do not hardcode changing counts in this skill.

## Important implementation boundary

- run.py is a host-integrated informational entrypoint. It prints the package path and suggests the search/design-system tools; it does not run a design task.
- tools/search.py is the concrete search CLI. Its imports are module-local (core, design_system); use the script entrypoint rather than assuming a stable package-level re-export.
- tools/__init__.py currently has no public re-exports (__all__ is empty). The package does not yet expose a stable unified SDK facade.
- tools/canvas.py is a stub: create_philosophy writes a short placeholder Markdown file, and render_canvas writes placeholder text rather than rendering a real PDF or PNG. Do not report a completed canvas artifact from those functions.
- The nested Canvas Design skill is instruction-only. A host must supply a real image/canvas renderer and validate the resulting PDF/PNG.

## Prerequisites and host integration

- Local search and data validation use files bundled under references/ui-ux-data/; no provider API key is needed for these operations.
- Web guideline retrieval calls the Vercel raw GitHub URL over HTTPS. It requires outbound network access; if unavailable, report blocked or not_run and do not use stale cached text as current guidance.
- The host entrypoint imports agent.contracts.host. The consuming project must provide that contract and install this package under agent/skills/uix_designer/.
- This repository does not include a standalone Python distribution manifest for UIX Designer.

## Entry points

Search:

~~~bash
python agent/skills/uix_designer/tools/search.py "keyboard focus modal" --domain ux
~~~

Run from the consuming project's root with the package installed at agent/skills/uix_designer/. Use only supported domains/stacks shown by the tool's own help or local configuration.

Data validation:

~~~bash
python agent/skills/uix_designer/tools/validate_data.py
~~~

Design-system generation can be invoked through generate_design_system in tools/design_system.py; confirm the target project's import layout before treating it as a stable public API.

## Procedure

1. Clarify the design target, audience, primary user action, platform, and technical stack.
2. Search the local reference corpus first. Inspect exact source rows and provenance for consequential recommendations.
3. Build a design-system proposal that fits the product rather than copying a style recipe mechanically.
4. Check accessibility, responsive behavior, interaction states, and platform-specific requirements against the target interface.
5. Fetch current web guidelines when network is available; retain source/version context.
6. Validate the local dataset when its integrity or freshness is in question.
7. For static artwork, follow Canvas Design's philosophy-then-art process and use an actual renderer. Verify the final image/PDF opens and has expected page dimensions.

## Outputs and verification

Possible outputs:
- Search results with query/domain and selected reference rows.
- Design-system recommendations or generated Markdown/JSON.
- Dataset validation findings.
- Web audit findings with exact file:line locations.
- Canvas philosophy Markdown and a real PDF/PNG only when a rendering capability actually ran.

Report source rows, target stack, guideline retrieval timestamp/revision where available, validator result, and any capability that remained a stub or unavailable.

## Safety and limitations

- Never fabricate search results when the local query returns zero matches. Use a clearly labeled fallback and state that no exact match was found.
- Keep the query within the documented five-term limit.
- Use bundled fonts only when their individual licenses permit the intended output. The Canvas Design Apache license does not override separate font/data licenses.
- Do not use external guideline text as a substitute for testing the actual interface.
- Do not claim WCAG conformance from a checklist alone; verify the rendered product and relevant assistive-technology behavior.

## Next steps

Search the local corpus, prepare a stack-specific design recommendation, and validate the implementation or generated artifact with the checks that actually ran.
