---
name: debug-pytorch-gpu
description: Diagnose and fix PyTorch GPU issues including CUDA OOM, DDP hangs, NCCL errors, device mismatches, and gradient instability. Use when training crashes with GPU-related errors or when GPU utilization is low.
---

## Debugging PyTorch GPU Issues

### Quick diagnostic checklist

```python
import torch
print(f"PyTorch: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
print(f"Device count: {torch.cuda.device_count()}")
for i in range(torch.cuda.device_count()):
    print(f"  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem / 1e9:.1f} GB)")
```

### Common issues and fixes

#### 1. CUDA Out of Memory (OOM)
- **Symptom**: `RuntimeError: CUDA out of memory`
- **Fixes**:
  - Reduce `batch_size` by 2x until it fits
  - Use gradient accumulation: `loss /= accumulation_steps`
  - Use mixed precision: `torch.autocast(device_type='cuda', dtype=torch.bfloat16)`
  - Call `torch.cuda.empty_cache()` between eval phases
  - Use `gradient_checkpointing_enable()` on large models
  - Move metrics to CPU: `loss.item()` detaches from graph

#### 2. DDP Hang / No Progress
- **Symptom**: Training hangs at first backward pass with DDP
- **Fixes**:
  - Ensure all ranks have same batch size (or use `find_unused_parameters=True`)
  - Check NCCL: `NCCL_DEBUG=INFO python script.py`
  - Set `NCCL_P2P_DISABLE=1` if peer-to-peer fails on PCIe GPUs
  - Ensure `torchrun --nproc_per_node=N` matches `--gres=gpu:l40s:N`
  - Add `torch.distributed.barrier()` before eval to sync ranks

#### 3. NCCL Errors
- **Symptom**: `NCCL error: unhandled system error` or timeout
- **Fixes**:
  - `export NCCL_P2P_DISABLE=1` (L40S are PCIe, not NVLink)
  - `export NCCL_IB_DISABLE=1` if InfiniBand issues
  - `export NCCL_TIMEOUT=1800` (increase from default 600s)
  - Check `NCCL_SOCKET_IFNAME` matches cluster network

#### 4. GPU Not Detected
- **Symptom**: `torch.cuda.device_count() == 0`
- **Fixes**:
  - `export CUDA_VISIBLE_DEVICES=0,1,2` in SBATCH script
  - `module load cuda/12.6` before activating conda
  - Verify Slurm allocation: `nvidia-smi` should show GPUs

#### 5. Gradient Instability (loss=NaN)
- **Symptom**: Loss becomes NaN after a few steps
- **Fixes**:
  - Clamp logits: `logits.clamp(-10.0, 10.0)`
  - Reduce learning rate by 10x
  - Add gradient clipping: `torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)`
  - Check for mixed precision overflow: use `torch.autocast` with `GradScaler`
  - Add numerical stability: `eps = 1e-6 if x.dtype == torch.float16 else 1e-12`

#### 6. Low GPU Utilization
- **Symptom**: `nvidia-smi` shows <50% GPU utilization
- **Fixes**:
  - Increase `num_workers` in DataLoader (try 8-16)
  - Use `pin_memory=True` and `persistent_workers=True`
  - Use `prefetch_factor=2` in DataLoader
  - Move data preprocessing to GPU (e.g., `kornia` instead of `torchvision`)
  - Avoid CPU-GPU sync points: don't call `.item()`, `.cpu()`, or print tensors in the loop

### Debugging tools

```bash
# Monitor GPU in real-time
watch -n 1 nvidia-smi

# Profile with PyTorch
python -m torch.profiler profile --script <script.py>

# Check memory breakdown
python -c "import torch; print(torch.cuda.memory_summary())"

# NCCL debug
NCCL_DEBUG=INFO NCCL_P2P_DISABLE=1 python script.py
```
