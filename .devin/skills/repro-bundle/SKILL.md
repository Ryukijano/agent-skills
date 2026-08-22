---
name: repro-bundle
description: >-
  Build a reproducibility bundle: code, data manifests, environment lockfiles,
  verify runs reproduce expected outputs, and lock artifacts. Use when packaging
  experiments for publication, artifact evaluation, open-science release, or
  submission supplementary materials.
---

# Repro Bundle

Iterative loop: **assemble code + data + env manifest → verify runs → lock artifacts → refine until reproducible**.

## Verification Loop

**Assemble → run clean reproduction → verify outputs match expected hashes → refine manifest → lock.**

## Read First

- [references/checklist.md](references/checklist.md) — reproducibility checklist
- `experiments/<exp-id>/` — protocol, outputs, environment.lock
- Project README and license for data/code

## Procedure

### 1. Scope the bundle

Define in `repro/BUNDLE.md`:

- What claim(s) this bundle supports
- Minimal commands to reproduce primary result
- Expected runtime and hardware
- License for code and data

### 2. Assemble components

```
repro/
├── BUNDLE.md           # Entry point
├── CODE.md             # Code provenance
├── DATA.md             # Data sources and checksums
├── ENVIRONMENT.lock    # Pinned dependencies
├── scripts/
│   ├── 00_setup.sh
│   ├── 01_download_data.sh
│   └── 02_run_experiment.sh
├── expected/
│   └── metrics.json    # Golden outputs
└── artifacts/          # Locked after verification
```

### 3. Environment manifest

- Pin all dependencies (pip freeze, conda export, or uv.lock)
- Record OS, CUDA, driver versions
- Record git commit: `git rev-parse HEAD`
- Docker/Singularity definition if used

### 4. Data manifest

For each dataset:

- Source URL and access instructions
- Version / snapshot date
- SHA256 checksum
- License and redistribution rights

### 5. Verify runs

On clean environment (fresh venv or container):

1. Run `00_setup.sh` → `01_download_data.sh` → `02_run_experiment.sh`
2. Compare outputs to `expected/metrics.json` within documented tolerance
3. Log verification in `repro/VERIFICATION.log`

Tolerance policy: exact match for integers; ±0.1% relative for floats unless protocol specifies otherwise.

### 6. Lock artifacts

After successful verification:

- Copy outputs to `artifacts/` with checksums
- Write `artifacts/MANIFEST.sha256`
- Tag git commit or create release archive
- Mark bundle version in `BUNDLE.md`

### 7. Refine

If verification fails:

- Diagnose: env drift, missing seed, data version mismatch
- Fix manifest or code; re-run from clean state
- Never adjust `expected/` to match broken runs without protocol amendment

## Rules

- One-command reproduction path documented in `BUNDLE.md`.
- No manual steps omitted from scripts.
- Secrets excluded; use env var placeholders.
- Data redistribution follows license; document download-only if needed.
- Verification log required before locking.

## Done When

- Clean-run verification passes per `VERIFICATION.log`
- [references/checklist.md](references/checklist.md) complete
- `artifacts/MANIFEST.sha256` matches locked files
- `BUNDLE.md` documents exact reproduce commands
