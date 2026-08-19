# Containers and Reproducibility for HPC

## Description

Docker, Apptainer/Singularity, Podman, conda-lock, Nix, and reproducible scientific environments.

## When to use

You want to ensure your scientific ML environment is reproducible across laptop, cluster, and cloud.

## Key concepts

- **Docker**: standard containers, root required for build.
- **Apptainer (Singularity)**: user-space, HPC-friendly, can run Docker images.
- **Podman**: daemonless, rootless alternative.
- **Conda-lock**: deterministic cross-platform lockfiles.
- **Nix**: purely functional, bit-for-bit reproducible builds.

## Code pattern

```bash
# Build Apptainer from Docker
apptainer build my.sif docker://my-image:latest

# Conda lock
conda-lock -f environment.yml -p linux-64 -p osx-64

# Run
apptainer run --nv my.sif python train.py
```

## Tuning notes

- Use multi-stage builds to reduce image size and attack surface.
- Bind host filesystems (`--bind /scratch`) in Apptainer.
- Pin CUDA/cuDNN versions in environment.

## Verification

1. Build a container and run the same script on two different hosts.
2. Verify `conda-lock install -n env conda-lock.yml` reproduces the exact packages.
3. Confirm the container can use the GPU with `nvidia-smi`.

## References

- https://apptainer.org/
- https://conda.github.io/conda-lock/
- https://nixos.org/
- https://docs.podman.io/
