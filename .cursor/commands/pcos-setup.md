# PCOS Setup

Set up the PCOS broker for local development.

## Steps

1. Clone and install:
   ```bash
   git clone https://github.com/Ryukijano/pcos-edge-agent.git
   cd pcos-edge-agent
   pip install -r requirements.txt
   ```

2. Copy config: `cp .env.example .env`

3. Start broker: `uvicorn broker.main:app --reload --port 8000`

4. Verify: `curl http://localhost:8000/health`

5. Test routing:
   ```bash
   curl -X POST http://localhost:8000/route \
     -H 'Content-Type: application/json' \
     -d '{"task": {"text": "summarize this", "is_webpage_grounded": true, "is_short": true, "task_type": "transform"}}'
   ```

6. Run tests: `python -m pytest tests/ -q`

7. Load Chrome extension from `chrome://extensions` (Chrome Canary 138+)

8. Optional: Android (`cd apps/android && ./gradlew assembleDebug`)

9. Optional: HF Space (`cd hf_space && python app.py`)

10. Optional: Docs (`mkdocs serve`)

See skill: `pcos-deploy`
