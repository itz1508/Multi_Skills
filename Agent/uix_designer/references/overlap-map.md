# Overlap Map — No Duplication

| Capability | Owner | Upstream | Reason |
|---|---|---|---|
| Tokens/styles/palettes/typography/charts | tools/search.py + design_system.py | ui-ux-pro-max | Single DB, no duplicate |
| Canvas philosophy + .pdf/.png | tools/canvas.py | canvas-design | Visual art only, not web |
| Web a11y/perf/responsive audit | checks/guideline.py + tools/web_guidelines.py | web-design-guidelines | Audit only, no token gen |
| Data validation | tools/validate_data.py | ui-ux-pro-max | Data integrity |
| Motion philosophy (WHY) | references/motion-philosophy/ | LottieFiles/motion-design-skill | Philosophy layer, not code |
| Motion library patterns (HOW-Motion) | references/motion-library/ | motiondivision/ai-kit | Motion/Framer Motion specific, not GSAP |
| GSAP timeline & scroll patterns | references/motion-library/gsap-timelines.md | greensock/GSAP | Timeline/ScrollTrigger, not Motion/Framer |
| Lottie playback & AE handoff | references/motion-library/lottie-web.md | airbnb/lottie-web | Designer handoff format, not code animation |
| Burst & shape motion graphics | references/motion-library/mojs-bursts.md | mojs/mojs | Burst/shape style, not UI transitions |
| 2D web particles (DOM/Canvas) | references/2d-web-particles.md | tsparticles/tsparticles | 2D DOM/Canvas, not 3D three.quarks |
| Explainer video creation | references/motion-canvas.md | motion-canvas/motion-canvas | Educational explainers, not general video |

**Rule:** One capability → one owner. No tool appears in 2 places. References hold docs only.

**Supporting-files resolved:**
- ui-ux-pro-max: /tmp/skills-use-kKJRsH/ui-ux-pro-max/{data,references,scripts} → tools/* + references/ui-ux-data
- canvas-design: /tmp/skills-use-aBguNV/canvas-design/{canvas-fonts,SKILL.md} → references/canvas-fonts
- web-design-guidelines: No local files — fetch https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
