---
description: Scaffold a new ML research project with standard structure
---

## Setup ML Project

Create a new ML research project with the standard directory structure.

1. Create the project directory and initialize git:
   ```bash
   mkdir <project_name>
   cd <project_name>
   git init
   ```

2. Create the standard directory structure:
   ```bash
   mkdir -p core_app/models core_app/data core_app/eval
   mkdir -p configs configs/splits
   mkdir -p scripts jobs logs outputs
   mkdir -p tests
   mkdir -p .devin/skills .devin/workflows
   ```

3. Create `requirements.txt` with standard ML dependencies:
   ```
   torch>=2.4
   torchvision
   numpy
   pandas
   pyyaml
   wandb
   opencv-python
   matplotlib
   tqdm
   einops
   timm
   ```

4. Create `.gitignore`:
   ```
   data/
   outputs/
   logs/
   wandb/
   __pycache__/
   *.pyc
   .env
   *.pth
   *.tar
   ```

5. Create a template config file `configs/default.yaml`:
   ```yaml
   meta:
     name: <project_name>
     seed: 42

   data:
     root: data/
     batch_size: 8
     num_workers: 4
     img_size: 224

   model:
     encoder: dinov2
     backbone: vitb14

   optimization:
     lr: 1e-4
     epochs: 100
     warmup_epochs: 5
     weight_decay: 0.01

   wandb:
     enabled: true
     project: <project_name>
   ```

6. Create a template SLURM job script `jobs/train.slurm` using the AIRE template.

7. Create `core_app/__init__.py` and `core_app/models/__init__.py`.

8. Create a basic test file `tests/test_smoke.py`:
   ```python
   def test_imports():
       import core_app
       assert True
   ```

9. Create `README.md` with project description, setup instructions, and usage.

10. Make the initial commit:
    ```bash
    git add -A
    git commit -m "chore: scaffold project structure"
    ```

11. Summarize the created structure and next steps for the user.
