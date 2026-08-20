# Quantum Neural Decoder

## Overview
Neural decoders replace classical minimum-weight perfect matching (MWPM) for syndrome decoding in quantum error correction, enabling real-time fault-tolerant computation.

## Key Approaches

### Neural Belief Propagation
- Replace BP decoders with learned message-passing GNNs
- Train on stabilizer syndrome patterns from surface/toric codes
- Generalizes to non-uniform noise models

### Transformer-Based Decoders
- Treat syndrome history as sequence; use attention for long-range correlations
- Scales to larger code distances (d=5 to d=21)
- Reference: arXiv:2604.08358 — 11x-800x logical error rate improvements (Nature 2026)

### GPU-Accelerated Decoding (SKQD)
- Batch decode syndromes on H100/H200
- Use SLURM array jobs for parallel circuit simulation
- Integrate with Qiskit runtime for hybrid HPC-quantum workflows

## Training Workflow
```python
# Generate syndromes
from qiskit_aer.noise import NoiseModel
syndromes, logical_errors = generate_surface_code_syndromes(
    distance=7, noise_model=noise_model, shots=100000
)
# Train decoder
model = NeuralDecoder(code_distance=7, num_layers=6)
train_decoder(model, syndromes, logical_errors)
```

## Evaluation
- Threshold: logical error rate vs physical error rate curves
- Compare against MWPM baseline
- Track sub-threshold scaling exponent

## Related Skills
- `quantum-error-correction` — stabilizer code fundamentals
- `vqe-hybrid-workflow` — variational algorithms
- `aire-slurm-submit` — HPC job submission for large-scale simulation

## Key References
- arXiv:2604.08358 (Scalable Neural Decoders, 2026)
- Nature s41586-026-10628-y (Improved logical error rates)
- IBM Qiskit Paulice blog
