---
name: conda-env-setup
description: Create and manage conda/Miniforge environments on AIRE HPC with CUDA support. Use when creating new Python environments, installing PyTorch with CUDA, debugging library conflicts, or managing package installations on AIRE.
---

## Conda Environment Setup on AIRE HPC

### Base installation

```bash
# Miniforge is installed at /scratch/kcwp264/conda
source /scratch/kcwp264/conda/etc/profile.d/conda.sh
conda activate base
```

### Creating a new environment with CUDA PyTorch

```bash
# Create env with Python 3.10+ (required for PyTorch 2.4+ and TorchCodec)
conda create -n <env_name> python=3.10 -y
conda activate <env_name>

# Install PyTorch with CUDA 12.6 (AIRE L40S)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

# Or via conda:
# conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia
```

### Common dependencies for ML projects

```bash
pip install wandb opencv-python scipy scikit-learn matplotlib tqdm pyyaml einops timm
pip install av pandas numpy
```

### TorchCodec (GPU video decoding)

```bash
pip install torchcodec
# Requires: PyTorch >= 2.4, FFmpeg 6.x
# On AIRE, must set LD_LIBRARY_PATH:
export LD_LIBRARY_PATH=/scratch/kcwp264/conda/envs/<env_name>/lib:$LD_LIBRARY_PATH
```

### Troubleshooting

1. **GLIBCXX errors**: Set `LD_LIBRARY_PATH` to include conda env's `lib/` directory
2. **CUDA mismatch**: Verify `torch.cuda.is_available()` and `torch.version.cuda`
3. **Import failures between login/compute nodes**: Install packages in `$SCRATCH` conda, not system conda
4. **HOME quota full**: Use `conda config --add pkgs_dirs /scratch/kcwp264/.conda_pkgs`
5. **TorchCodec FFmpeg mismatch**: Ensure FFmpeg 6.x is in PATH or use PyAV fallback

### Exporting environments

```bash
# Export for reproducibility
conda env export --no-builds > environment.yml
# Or pack for transfer
conda pack -n <env_name> -o /scratch/kcwp264/<env_name>.tar.gz
```

### Known working configurations

| Env | Python | PyTorch | CUDA | Key packages |
|-----|--------|---------|------|-------------|
| `endofm-lv` | 3.10 | 2.11.0+cu126 | 12.6 | TorchCodec 0.13, FFmpeg 6.x |
| `surgi_world_track_cuda` | 3.10 | 2.7+ | 12.6 | timm, einops, wandb |
