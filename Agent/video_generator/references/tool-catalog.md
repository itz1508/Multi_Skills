# Tool Catalog: 20 Animation/VFX Tools

## Agent Skills (1–6)

| # | Tool | Repo | Use Case |
|---|------|------|----------|
| 1 | motion-design-skill | github.com/LottieFiles/motion-design-skill | Timing, easing, Disney's 12 principles |
| 2 | ai-kit | github.com/motiondivision/ai-kit | CSS springs, motion audits for agents |
| 3 | Remotion Skills | github.com/remotion-dev/skills | Official video skills for coding agents |
| 4 | hairline | hairline.lucasmarkes.com/skills | Interactive line figures from idea or SVG |
| 5 | anatomy | skills.wheresryan.sh/anatomy | Machines/systems as isometric figures |
| 6 | anatomy-reveal | typingmind.com/skills/annnguyentt-anatomy-reveal | Exploded product views, reveal MP4 |

Install: `npx skills add <repo>` for agent skills 1–3. Skills 4–6 are web-hosted.

## Animation Libraries (7–16)

| # | Tool | Repo | Language | Use Case |
|---|------|------|----------|----------|
| 7 | blender-agents | github.com/scenario-labs/blender-plugin | Python | Full AI 3D team in Blender via MCP |
| 8 | Three.js | github.com/mrdoob/three.js | JS | 3D scenes, camera moves |
| 9 | react-three-rapier | github.com/pmndrs/react-three-rapier | JS/React | Real physics for R3F scenes |
| 10 | react-postprocessing | github.com/pmndrs/react-postprocessing | JS/React | Bloom, depth of field, film effects |
| 11 | three.quarks | github.com/Alchemist0823/three.quarks | JS | Particle trails, VFX |
| 12 | Tweakpane | github.com/cocopon/tweakpane | JS | Live controls for scene parameters |
| 13 | GSAP | github.com/greensock/GSAP | JS | Animation timelines (now fully free) |
| 14 | Remotion | github.com/remotion-dev/remotion | JS/React | React video engine |
| 15 | Manim | github.com/ManimCommunity/manim | Python | Animated diagrams, equations, explainers |
| 16 | Lottie | github.com/airbnb/lottie-web | JS | Lightweight vector animation playback |

### Python-native (use in this skill directly)

- **Manim**: `pip install manim` — animated diagrams, equations, explainers
- **blender-agents**: Blender MCP plugin — 3D modeling and rendering via MCP

### JS-native (use in seek(t) HTML)

- **Three.js**: `npm install three` — 3D scenes in the browser
- **GSAP**: `npm install gsap` — timeline-based animation (now free)
- **Lottie**: `npm install lottie-web` — play After Effects animations
- **Remotion**: `npm install remotion` — React-based video composition
- **Tweakpane**: `npm install tweakpane` — live parameter controls
- **three.quarks**: `npm install three.quarks` — particle systems
- **react-postprocessing**: `npm install @react-three/postprocessing` — post-FX

## Audio/Video Tools (17–20)

| # | Tool | Repo | Use Case |
|---|------|------|----------|
| 17 | Openverse API | api.openverse.org/v1/ | 5.2M+ free sound effects, ambience, music |
| 18 | librosa | github.com/librosa/librosa | Beat detection for music-synced animation |
| 19 | WhisperX | github.com/m-bain/whisperX | Word-level timing for captions |
| 20 | FFmpeg | github.com/FFmpeg/FFmpeg | Encoding and delivery |

### Installation

```bash
# Python audio tools
pip install librosa soundfile
pip install whisperx  # requires torch

# Node/Playwright for frame capture
npm i -D playwright
npx playwright install chromium

# FFmpeg (system)
brew install ffmpeg        # macOS
apt install ffmpeg         # Linux
```

## Integration Matrix

| Skill Module | Tool | How Used |
|-------------|------|---------|
| tools/motion.py | Playwright, FFmpeg | Frame capture and video encoding |
| tools/audio.py | librosa, Openverse API | Beat detection and SFX search |
| tools/captions.py | WhisperX | Word-level transcription and SRT |
| tools/critic.py | FFmpeg | Contact sheets, phone tests, loop checks |
| references/ | motion-design-skill, ai-kit | Style guides and motion principles |
| templates/seek_template.html | Three.js, GSAP (optional) | Starter HTML with seek(t) contract |
