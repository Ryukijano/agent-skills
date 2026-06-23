---
description: Diagnose and fix PyTorch GPU issues including OOM, DDP hangs, NCCL errors
---

## Debug PyTorch GPU

1. Run quick diagnostics:
   ```python
   import torch
   print(f"PyTorch: {torch.__version__}, CUDA: {torch.cuda.is_available()}")
   print(f"GPUs: {torch.cuda.device_count()}")
   ```

2. Identify the failure mode:
   - **OOM** → Go to step 3
   - **DDP hang** → Go to step 5
   - **NCCL error** → Go to step 6
   - **GPU not detected** → Go to step 7
   - **Loss=NaN** → Go to step 8

3. **OOM**: Reduce batch_size by half. Enable mixed precision:
   ```python
   with torch.autocast(device_type='cuda', dtype=torch.bfloat16):
       output = model(input)
   ```

4. **OOM persists**: Enable gradient checkpointing, call `torch.cuda.empty_cache()`.

5. **DDP hang**: Set `NCCL_P2P_DISABLE=1`, `NCCL_DEBUG=INFO`. Check all ranks have same batch size.

6. **NCCL error**: Set `NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 NCCL_CUMEM_ENABLE=0`. Preload bundled NCCL:
   ```bash
   PY_SITE=$(python -c "import site; print(site.getsitepackages()[0])")
   export LD_PRELOAD=${PY_SITE}/nvidia/nccl/lib/libnccl.so.2
   ```

7. **GPU not detected**: `export CUDA_VISIBLE_DEVICES=0,1,2`, `module load cuda/12.6`.

8. **Loss=NaN**: Reduce LR 10x, add gradient clipping `max_norm=1.0`, clamp logits.

9. Summarize root cause and fix applied.
