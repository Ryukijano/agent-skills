---
name: pcos-chrome-ai
description: >-
  Chrome Built-in AI API integration for PCOS. Use when working on the Chrome
  extension, adding Built-in AI API calls, debugging Chrome AI availability,
  or updating the side panel UI.
---

# Chrome Built-in AI for PCOS

The PCOS Chrome extension uses Chrome's Built-in AI APIs for on-browser inference with zero network latency.

## Available APIs (Chrome 138+)

| API | Object | Status | Use Case |
|-----|--------|--------|----------|
| Prompt | `ai.languageModel` | ✅ Stable | General NL instructions |
| Summarizer | `ai.summarizer` | ✅ Stable | Summarization |
| Translator | `ai.translator` | ✅ Stable | Translation |
| Language Detector | `ai.languageDetector` | ✅ Stable | Language detection |
| Writer | `ai.writer` | 🔄 Dev trial | Long-form generation |
| Rewriter | `ai.rewriter` | 🔄 Dev trial | Text transformation |
| Proofreader | `ai.proofreader` | 🔄 Dev trial | Grammar/correction |

**Non-existent APIs (do NOT use):**
- ~~`ai.classifier`~~ — Chrome has no classifier built-in AI
- ~~Multimodal Prompt API~~ — Not a built-in API; multimodal goes to Android

## API Usage Patterns

### Prompt API
```javascript
const session = await ai.languageModel.create();
const result = await session.prompt("Summarize: " + text);
session.destroy();
```

### Summarizer API
```javascript
const summarizer = await ai.summarizer.create({
  type: "key-points",
  format: "markdown",
  length: "medium",
});
const result = await summarizer.summarize(text);
summarizer.destroy();
```

### Translator API
```javascript
const translator = await ai.translator.create({
  sourceLanguage: "en",
  targetLanguage: "fr",
});
const result = await translator.translate(text);
translator.destroy();
```

### Streaming
```javascript
const stream = await session.promptStreaming(text);
for await (const chunk of stream) {
  // Append chunk to UI
}
```

## Availability Detection

```javascript
async function checkAvailability() {
  const apis = {
    prompt: 'languageModel' in ai,
    summarizer: 'summarizer' in ai,
    translator: 'translator' in ai,
    language_detector: 'languageDetector' in ai,
    writer: 'writer' in ai,
    rewriter: 'rewriter' in ai,
    proofreader: 'proofreader' in ai,
  };
  return apis;
}
```

## WebSocket Keepalive (MV3)

Chrome MV3 service workers die after 30s inactivity. The extension uses:
1. **Offscreen document** — maintains the WebSocket connection
2. **Ping/pong** every 25s
3. **Reconnect** on disconnect

## Key Files

- `apps/chrome-extension/chrome_ai.js` — Chrome AI API wrapper
- `apps/chrome-extension/sidepanel.html` — Side panel UI
- `apps/chrome-extension/sidepanel.css` — Polished dark theme
- `apps/chrome-extension/sidepanel.js` — Panel logic and broker communication
- `apps/chrome-extension/background.js` — Service worker with keepalive
- `apps/chrome-extension/offscreen.html` — Offscreen document for WS
- `apps/chrome-extension/manifest.json` — Extension manifest

## Build

Load unpacked extension from `chrome://extensions` in Chrome Canary 138+.
