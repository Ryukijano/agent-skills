---
name: testing-strategy
description: Design and implement testing strategies for ML research code including unit tests, integration tests, smoke tests, and property-based tests. Use when writing tests for model components, data pipelines, training loops, or setting up pytest.
---

## Testing Strategy for ML Research Code

### Test pyramid for ML projects

```
        ┌─────────┐
        │  E2E    │  Full training run (1-2 steps, verify no crash)
        ├─────────┤
        │ Integr. │  Model + data + loss together
        ├─────────┤
        │  Unit   │  Individual functions, layers, metrics
        └─────────┘
```

### Test types

| Type | What | Example | Speed |
|------|------|---------|-------|
| **Smoke** | Does it run? | `python train.py --max-steps 2` | Seconds |
| **Unit** | Correct output shapes/values | `assert model(x).shape == (B, N, D)` | Fast |
| **Integration** | Components work together | `loss = model(batch); loss.backward()` | Medium |
| **Property** | Invariants hold | `loss >= 0`, `softmax sums to 1` | Fast |
| **Regression** | Old behavior preserved | `assert old_func() == new_func()` | Fast |

### Minimal pytest setup

```bash
pip install pytest pytest-cov
```

```
tests/
├── conftest.py          # Shared fixtures
├── test_smoke.py        # Import + instantiation tests
├── test_models.py       # Model forward/backward tests
├── test_data.py         # Dataset/dataloader tests
├── test_losses.py       # Loss function tests
└── test_utils.py        # Utility function tests
```

### conftest.py fixtures

```python
import pytest
import torch

@pytest.fixture
def device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

@pytest.fixture
def small_batch():
    """Tiny batch for quick tests."""
    return torch.randn(2, 3, 224, 224)

@pytest.fixture
def model():
    from core_app.models.tdv_model import TDVModel
    return TDVModel(model_name="dinov2_vits14", img_size=224, freeze=True)
```

### Key test patterns

```python
# Shape test
def test_encoder_output_shape(model, small_batch):
    out = model(small_batch)
    assert out.shape == (2, 1 + 256, 384)  # CLS + patches, embed_dim

# Backward pass test
def test_loss_backward(model, small_batch):
    out = model(small_batch)
    loss = out['loss']
    loss.backward()
    # Check gradients exist for trainable params
    trainable = [p for p in model.parameters() if p.requires_grad]
    assert all(p.grad is not None for p in trainable)

# Determinism test
def test_seed_reproducibility():
    set_all_seeds(42)
    a = torch.randn(10)
    set_all_seeds(42)
    b = torch.randn(10)
    assert torch.allclose(a, b)

# Property test: loss is non-negative
def test_loss_non_negative(model, small_batch):
    out = model(small_batch)
    assert out['loss'].item() >= 0

# Data pipeline test
def test_dataloader_yields_correct_shapes():
    ds = Cholec80TDVDataset(frames_root, video_names, num_frames=4)
    sample = ds[0]
    assert sample.shape == (4, 3, 224, 224)
```

### Running tests

```bash
# All tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=core_app --cov-report=term-missing

# Only smoke tests
pytest tests/test_smoke.py -v

# Parallel
pytest tests/ -n auto  # requires pytest-xdist
```
