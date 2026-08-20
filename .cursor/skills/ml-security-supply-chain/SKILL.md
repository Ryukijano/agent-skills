# ML Security and Supply Chain

## Description

Model signing, AIBOM/ML-BOM, container scanning, malicious pickle detection, and provenance for ML artifacts.

## When to use

You need to secure the ML supply chain: models, datasets, containers, and dependencies.

## Key concepts

- **Model signing**: OpenSSF Model Signing (OMS), Sigstore keyless signing.
- **SBOM/AIBOM/ML-BOM**: CycloneDX, SPDX for AI models and dependencies.
- **Container scanning**: Trivy, Grype for CVEs in ML images.
- **Artifact scanning**: ML Guard for malicious pickles, leaked secrets, vulnerable dependencies.
- **Provenance**: in-toto attestations, signed hashes, lineage.

## Code pattern

```bash
# Sign a model with Sigstore/OMS
oms sign --model-dir ./model --identity user@example.com

# Scan container
trivy image my-ml-image:latest

# Generate CycloneDX SBOM
sbom-tool generate -b . -bc . -o sbom.json
```

## Tuning notes

- Treat models and datasets as code artifacts with version, hash, and signature.
- Use `safetensors` instead of `pickle` for model weights when possible.
- Quarantine external models/datasets before promoting to production.

## Verification

1. Sign a model artifact and verify the signature.
2. Run Trivy on a serving container and review CVEs.
3. Generate an AIBOM for a trained model and confirm it captures datasets, hyperparameters, and dependencies.

## References

- https://github.com/ossf/model-signing-spec
- https://cyclonedx.org/specification/overview/
- https://trivy.dev/
- https://github.com/ml-guard/ml-guard
