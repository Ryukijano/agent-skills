# AlphaEvolve Experiment Runner

## Prerequisites
- `initial_program.py` with `EVOLVE-BLOCK` markers
- `evaluator.py` (CLI-compatible)
- GCP project with AlphaEvolve provisioned
- `gcloud` CLI authenticated
- `.env` file with: PROJECT_ID, LOCATION, COLLECTION, GE_APP_ID, ASSISTANT, BASE_URL

## Stage 1: Configure
1. Auto-discover GCP configuration from `.env` and `gcloud config`
2. Set configuration in the client
3. Test connectivity to AlphaEvolve API

## Stage 2: Verify Evaluator
1. Validate input files exist and are syntactically correct
2. Run baseline evaluation: `uv run python evaluator.py --output-file baseline.json --program-dir .`
3. Review baseline score — if it fails, fix before proceeding

## Stage 3: Review & Confirm
1. Determine experiment parameters:
   - `MAX_PROGRAMS_GENERATED` / `MAX_PROGRAMS_EVALUATED` (budget)
   - `CONCURRENCY` / `WORKER_CONCURRENCY` (parallelism)
   - Model mixture: `gemini-3.5-flash` (breadth) + `gemini-3.1-pro-preview` (depth)
2. Confirm with user before launching

## Stage 4: Create & Launch
```python
from alpha_evolve.client import AlphaEvolveClient
from alpha_evolve.experiment import AlphaEvolveExperiment
from alpha_evolve.controller import run_controller_loop
import asyncio

client = AlphaEvolveClient(
    project_id="my-project", location="global",
    collection="default_collection", engine="my-engine-id",
    assistant="default_assistant",
    base_url="discoveryengine.googleapis.com",
)
experiment = AlphaEvolveExperiment(client, my_evaluation_fn, max_programs_evaluated=100)
experiment.create_experiment({
    "title": "My Experiment",
    "problem_description": "Evolve <function> to maximize <metric>.",
    "program_language": "python",
    "run_settings": {"max_programs": 100, "concurrency": 4},
    "generation_settings": {
        "models": [
            {"name": "gemini-3.5-flash", "weight": 0.7},
            {"name": "gemini-3.1-pro-preview", "weight": 0.3},
        ]
    },
})
experiment.create_initial_program(seed_program)
experiment.start_experiment()
asyncio.run(run_controller_loop(experiment))
```

## Important
- No pause command — once started, the experiment runs until budget exhausted or cancelled
- Progress is non-monotonic — score can plateau then jump. Don't stop early.
- Invalid candidates are expected — failures return sentinel scores and feed insights back

## Error Handling
- API connection errors → check GCP auth, project ID, engine ID
- Evaluator timeout → increase `timeout_seconds` or optimize evaluator
- All candidates failing → check evaluator correctness, EVOLVE-BLOCK syntax
