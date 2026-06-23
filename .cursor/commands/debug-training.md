# Debug Training

Diagnose and fix training failures in MOT / TDV pretrain / surgical video models. Use symptom-driven flow.

## 0. Capture state
```bash
cd /home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking
conda activate surgi_track   # or surgi_world_track_cuda / endofm-lv
export XFORMERS_DISABLED=1
python -c "import torch; print(torch.__version__, torch.version.cuda, torch.cuda.get_device_name(0))"
```
Save last 200 lines of logs + the config used + `git rev-parse HEAD`.

## 1. Classify symptom
- **Loss = NaN / Inf within first 50 steps**: gradient explosion, bad init, bad data, LR too high.
- **CUDA OOM**: batch too big, activation spikes, no checkpointing.
- **DDP hang / NCCL timeout**: rank mismatch, NCCL peer-to-peer, network.
- **No learning / flat curves**: data static, wrong loss weighting, frozen wrong parts, LR schedule broken.
- **Low GPU util (<30%)**: dataloader bottleneck, CPU decode, small batch, blocking ops.
- **Shape errors**: temporal dimension off, DINO patch size mismatch (must be ÷14), missing keys on load.

## 2. Immediate safe actions
- Smoke test with `max_steps: 2` or `batch_size=1` first.
- Add `torch.autocast('cuda', dtype=torch.bfloat16)` + grad scaler if not using.
- Clamp logits in heads: `logits = logits.clamp(-10, 10)`.
- Enable anomaly detection temporarily: `torch.autograd.set_detect_anomaly(True)`.
- For video: verify `rgb_diff = (frame_{t+1} - frame_t).abs().mean()` is > 1e-4 (not static frames).

## 3. Symptom-specific fixes (apply relevant skill)

**NaN / explosion**:
- Reduce peak LR 10x.
- Add `torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)`.
- Check loss weights: start with `mse_loss_weight=1.0`, lower others.
- For TDV: ensure EMA momentum high (0.996+) and teacher updated every step.
- Add `center + sharpen` on targets (see tdv_losses).

**OOM**:
- `batch_size /= 2`, use grad accumulation.
- `gradient_checkpointing_enable()` on backbone.
- Use smaller backbone: `dinov2_vits14` (384) instead of vitb14 (768).
- `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`.
- Move non-essential tensors to CPU (metrics, some logs).

**DDP / NCCL**:
- Match `--nproc_per_node` to Slurm `--gres=gpu:l40s:N`.
- `NCCL_P2P_DISABLE=1 NCCL_IB_DISABLE=1 NCCL_DEBUG=INFO`.
- Ensure identical conda env + CUDA on all nodes/ranks.
- Add `dist.barrier()` before heavy eval.

**No learning**:
- Confirm `requires_grad` on intended params only (LoRA vs full).
- Verify dataloader yields different frames (not all black or same video looped).
- For MOT: ensure pseudo-labels from Stage 1 teacher are non-trivial.
- Check LR schedule: warmup must reach peak before decay.
- Log `grad_norm` and `param_norm` per layer.

**Low GPU util**:
- Increase `num_workers` (4–8), pin_memory.
- Pre-decode or use TorchCodec / NVIDIA DALI.
- Profile: `torch.profiler.profile(...)` or `nvidia-smi dmon`.
- Avoid Python-side per-frame loops in collate.

## 4. Regression guard
After any fix:
```bash
python -m core_app.mot.main --fname configs/... --devices cuda:0 --max_steps 5
pytest tests/test_mot_smoke.py -q
```
Record before/after in WandB (same group).

## 5. Handoff
Update the run notes in WandB with root cause + fix. Create `debug/<run>-notes.md` if complex.

Apply skills: `debug-pytorch-gpu`, `tdv-pretrain`, `surgical-mot-eval`, `systematic-debug`, `iterative-test-loop`.

Reference verification gate: do not mark fixed until smoke + narrow test pass.
