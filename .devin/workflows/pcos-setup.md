---
description: Set up the PCOS broker for local development
---

## PCOS Local Development Setup

1. **Clone and install**:
   ```bash
   git clone https://github.com/Ryukijano/pcos-edge-agent.git
   cd pcos-edge-agent
   pip install -r requirements.txt
   ```

2. **Copy environment config**:
   ```bash
   cp .env.example .env
   # Edit .env if needed (default ports: broker=8000, piecesos=39300)
   ```

3. **Start the broker**:
   ```bash
   uvicorn broker.main:app --reload --port 8000
   ```

4. **Verify health**:
   ```bash
   curl http://localhost:8000/health
   # Should return {"status": "ok", "service": "pcos-context-broker", ...}
   ```

5. **Test routing**:
   ```bash
   curl -X POST http://localhost:8000/route \
     -H 'Content-Type: application/json' \
     -d '{"task": {"text": "summarize this article", "is_webpage_grounded": true, "is_short": true, "task_type": "transform"}}'
   ```

6. **Run tests**:
   ```bash
   python -m pytest tests/ -q
   ```

7. **Load Chrome extension**:
   - Open `chrome://extensions` in Chrome Canary 138+
   - Enable Developer mode
   - Load unpacked from `apps/chrome-extension/`

8. **Build Android app** (optional):
   ```bash
   cd apps/android
   ./gradlew assembleDebug
   ```

9. **Start HF Space demo** (optional):
   ```bash
   cd hf_space
   pip install -r requirements.txt
   python app.py
   ```

10. **Start docs site** (optional):
    ```bash
    pip install mkdocs-material mkdocstrings
    mkdocs serve
    ```
