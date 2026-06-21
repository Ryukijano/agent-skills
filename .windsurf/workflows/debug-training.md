---
description: Debug ML training failures including loss=NaN, OOM, DDP hangs, and poor convergence
---

## Debug Training

Systematically diagnose and fix training failures.

1. Identify the failure mode from the error message or symptom:
   - **Loss=NaN**: Go to step 2
   - **CUDA OOM**: Go to step 5
   - **DDP hang/timeout**: Go to step 8
   - **Poor convergence**: Go to step 11
   - **Wrong output shapes**: Go to step 14

### Loss = NaN

2. Add gradient norm logging before clipping:
   ```python
   total_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=float('inf'))
   print(f"grad_norm: {total_norm.item()}")
   ```
   If grad_norm is NaN, the backward pass is producing NaN gradients.

3. Check for numerical instability:
   - Add `eps` to denominators: `x / (denom + 1e-6)`
   - Clamp logits: `logits.clamp(-10, 10)`
   - Use `torch.nan_to_num(x, nan=0.0)` as a temporary diagnostic
   - Check if any input tensors contain NaN: `assert not torch.isnan(input).any()`

4. Reduce learning rate by 10x and retry. If loss is stable, the LR was too high.

### CUDA OOM

5. Reduce batch size by half and retry. Note the maximum batch size that works.

6. If still OOM, enable memory-saving techniques:
   - Mixed precision: `torch.autocast(device_type='cuda', dtype=torch.bfloat16)`
   - Gradient checkpointing: `model.gradient_checkpointing_enable()`
   - Free memory between phases: `torch.cuda.empty_cache()`

7. Profile memory usage to find the bottleneck:
   ```python
   print(torch.cuda.memory_summary(device=0))
   ```

### DDP Hang

8. Set NCCL debug and disable P2P (L40S are PCIe, not NVLink):
   ```bash
   export NCCL_DEBUG=INFO
   export NCCL_P2P_DISABLE=1
   ```

9. Check that all ranks have the same model, same batch size, and same loss.
   Add a barrier before the first backward:
   ```python
   if torch.distributed.is_initialized():
       torch.distributed.barrier()
   ```

10. If using `DistributedDataParallel`, try `find_unused_parameters=True`:
    ```python
    model = DDP(model, device_ids=[local_rank], find_unused_parameters=True)
    ```

### Poor Convergence

11. Check the learning rate schedule — is it actually reaching the peak LR?
    ```python
    print(f"step={step}, lr={optimizer.param_groups[0]['lr']}")
    ```

12. Check that the model is actually training (parameters are changing):
    ```python
    # Before optimizer step
    before = model.encoder.blocks[0].attn.qkv.weight.clone()
    optimizer.step()
    after = model.encoder.blocks[0].attn.qkv.weight.clone()
    print(f"Weight change: {(after - before).abs().max().item()}")
    ```

13. Check data loading — are labels correct? Are augmentations too aggressive?
    Visualize a few samples:
    ```python
    batch = next(iter(dataloader))
    import matplotlib.pyplot as plt
    plt.imshow(batch[0][0].permute(1, 2, 0))
    plt.savefig('debug_sample.png')
    ```

### Wrong Output Shapes

14. Add shape assertions at every reshape/permute:
    ```python
    assert x.shape == (B, N, D), f"Expected {(B, N, D)}, got {x.shape}"
    ```

15. Trace the forward pass by printing shapes at each layer:
    ```python
    print(f"After patch_embed: {x.shape}")
    print(f"After block {i}: {x.shape}")
    ```

16. Summarize the root cause and the fix applied. Add a regression test if appropriate.
