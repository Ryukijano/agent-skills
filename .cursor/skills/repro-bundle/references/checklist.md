# Reproducibility Bundle Checklist

## Bundle Metadata

- [ ] `BUNDLE.md` states claim supported and cite experiment protocol ID
- [ ] Hardware requirements documented (GPU, RAM, disk)
- [ ] Expected runtime documented
- [ ] License files present (code + data)

## Code

- [ ] Git commit hash recorded
- [ ] Entry-point script runs without manual intervention
- [ ] Random seeds fixed and documented
- [ ] No hardcoded absolute paths (use env vars or relative paths)
- [ ] Dependencies fully pinned in `ENVIRONMENT.lock`

## Data

- [ ] All datasets listed in `DATA.md`
- [ ] Download scripts or access instructions work
- [ ] SHA256 checksums verified after download
- [ ] License permits redistribution or download-only documented

## Environment

- [ ] Clean-environment reproduction tested (fresh venv/container)
- [ ] CUDA/driver versions recorded if GPU required
- [ ] Docker/Singularity file builds and runs (if provided)

## Verification

- [ ] `02_run_experiment.sh` completes without error
- [ ] Output metrics match `expected/metrics.json` within tolerance
- [ ] `VERIFICATION.log` records date, commit, verifier, pass/fail
- [ ] Failed attempts logged with diagnosis

## Lock

- [ ] `artifacts/MANIFEST.sha256` generated
- [ ] Bundle version tagged in `BUNDLE.md`
- [ ] Archive or release created (if publishing)

## Integrity

- [ ] No secrets in bundle
- [ ] No proprietary data included without permission
- [ ] Expected outputs not retrofitted to match broken runs
