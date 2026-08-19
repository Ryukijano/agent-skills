# Kubernetes and GPU Orchestration

## Description

NVIDIA GPU Operator, MIG, MPS, Kueue, Volcano, gang scheduling, and DRA for ML workloads on Kubernetes.

## When to use

You are running ML training or inference on Kubernetes and need to schedule, share, or partition GPUs.

## Key concepts

- **NVIDIA GPU Operator**: automates driver, container runtime, device plugin, DCGM, and MIG manager deployment.
- **MIG on Kubernetes**: `mig.strategy=single/mixed`; node labels like `nvidia.com/mig-1g.5gb`.
- **MPS**: multi-process service for sharing a GPU across containers; controlled via DRA driver feature gate.
- **Kueue**: Kubernetes native queueing with quotas, fair sharing, and preemption.
- **Volcano**: alternative scheduler with gang scheduling, hierarchical queues, and job-level co-scheduling.
- **DRA (Dynamic Resource Allocation)**: new device API in K8s; used by Kueue for fine-grained GPU allocation.

## Code pattern

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-job
spec:
  containers:
  - name: train
    image: nvcr.io/nvidia/pytorch:25.06-py3
    resources:
      limits:
        nvidia.com/gpu: 1
```

For Kueue:

```bash
kubectl label queue default-queue
kubectl apply -f job.yaml
```

## Tuning notes

- MIG and MPS are mutually exclusive in the DRA driver; choose one per node.
- Gang scheduling prevents partial-allocation deadlock for multi-pod jobs.
- Use `nvidia.com/gpu: 1` for whole GPU, `nvidia.com/mig-...` for slices.

## Verification

1. Check `kubectl get nodes` shows `nvidia.com/gpu` allocatable resources.
2. Run a small GPU pod and `nvidia-smi` inside the container.
3. With Kueue, verify the job is admitted and scheduled.

## References

- https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/26.3/gpu-operator-mig.html
- https://kueue.sigs.k8s.io/
- https://volcano.sh/
- https://dra-driver-nvidia-gpu.sigs.k8s.io/
