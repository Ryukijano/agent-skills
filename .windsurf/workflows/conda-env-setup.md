---
description: Create and manage conda environments on AIRE HPC with CUDA support
---

## Conda Environment Setup

1. Source conda and activate base:
   ```bash
   source /scratch/kcwp264/conda/etc/profile.d/conda.sh
   conda activate base
   ```

2. Create new environment with Python 3.10+:
   ```bash
   conda create -n <env_name> python=3.10 -y
   conda activate <env_name>
   ```

3. Install PyTorch with CUDA 12.6:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
   ```

4. Install project dependencies:
   ```bash
   pip install wandb opencv-python scipy scikit-learn matplotlib tqdm pyyaml einops timm
   ```

5. Set LD_LIBRARY_PATH for the environment:
   ```bash
   export LD_LIBRARY_PATH=/scratch/kcwp264/conda/envs/<env_name>/lib:$LD_LIBRARY_PATH
   ```

6. Verify installation:
   ```bash
   python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
   ```

7. Export environment for reproducibility:
   ```bash
   conda env export --no-builds > environment.yml
   ```

8. Summarize: env name, Python version, PyTorch version, CUDA version.
