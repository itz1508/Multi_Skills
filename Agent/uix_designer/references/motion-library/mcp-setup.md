# Motion MCP Server Setup

## Free Server (No Auth)

- URL: `https://mcp.motion.dev`
- Works signed out, no API key needed
- Provides: `search-motion-docs`, `generate-css-easing`, `insert-motion-component`

## Motion+ Server (Paid)

- URL: `https://mcp.motion.dev/plus`
- Requires Motion+ account sign-in
- Provides: `search-motion-source`, `insert-motion-plus-component`, full MotionScore audit methodology, Motion+ source code access, visual transition editor

## Configuration

### Agent (JSON config)
```json
{ "mcpServers": { "motion": { "type": "http", "url": "https://mcp.motion.dev" } } }
```

### Agent (TOML config)
```toml
[mcp_servers.motion]
type = "http"
url = "https://mcp.motion.dev"
```

### Manual (any agent)
```json
{ "mcpServers": { "motion": { "type": "http", "url": "https://mcp.motion.dev" } } }
```

## When MCP Is Unavailable

`best-practices/` references (css-or-motion.md, motion-react.md, motion-vue.md) work with no server. Search, easing generation, audit methodology, and transition editor need the server. If missing, tell the user the Motion MCP server is not connected and point to https://motion.dev/docs/ai-kit.

## Motion+ Components (Not in Free Package)

`Carousel`, `Ticker`, `AnimateNumber`, `Typewriter`, `ScrambleText`, `Cursor` from `motion-plus/react`, and `splitText` from `motion-plus`. Do not import from `motion-plus` unless the project already has it installed.

Source: re-written from motiondivision/ai-kit research.
