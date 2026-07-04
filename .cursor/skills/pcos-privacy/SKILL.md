---
name: pcos-privacy
description: >-
  PCOS privacy policies, PII stripping, and cloud escalation gating. Use when
  working on privacy-sensitive routing, data redaction, or ensuring sensitive
  tasks never leave the device.
---

# PCOS Privacy & Escalation Policies

## Core Principle

**Privacy wins over capability.** Sensitive tasks stay on-device regardless of size or complexity. Cloud is the last resort, never the default.

## PII Stripping

`broker/policies/privacy.py` strips personally identifiable information before any cloud escalation:

| Pattern | Replacement | Regex |
|---------|-------------|-------|
| Email | `[EMAIL]` | `\b[\w.+-]+@[\w-]+\.[\w.-]+\b` |
| Phone | `[PHONE]` | `\b\d{3}[-.]?\d{3}[-.]?\d{4}\b` |
| IP address | `[IP]` | `\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b` |
| API key | `[API_KEY]` | `sk-[a-zA-Z0-9]{20,}` |
| Credit card | `[CARD]` | `\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b` |
| SSN | `[SSN] | `\b\d{3}-\d{2}-\d{4}\b` |
| Address | `[ADDRESS]` | `\b\d+\s+[A-Z][a-z]+\s+(Street|St|Avenue|Ave|...)\b` |

## Escalation Gating

`broker/policies/escalation.py` logs all cloud escalations with:
- Reason (explicit user, exceeds limits, long reasoning)
- Task text (PII-stripped)
- Whether user explicitly requested escalation

## Routing Privacy Rules

1. **`sensitivity == PRIVATE`** → Always Android FunctionGemma, never cloud
2. **Offline context** → Always Android, never cloud
3. **Cloud escalation** → PII stripped from `context_payload` and `task_text`
4. **`is_safe_for_cloud()`** check → Verifies no PII remains after stripping

## Key Files

- `broker/policies/privacy.py` — PII stripping and cloud safety check
- `broker/policies/escalation.py` — Escalation logging
- `broker/router/router.py` — Privacy-aware routing decisions
- `broker/routers/route_router.py` — PII stripping on cloud escalation in endpoints

## Testing Privacy

```python
from broker.policies.privacy import strip_pii, is_safe_for_cloud

# Strip PII
assert "john@example.com" not in strip_pii("contact john@example.com")
assert "[EMAIL]" in strip_pii("contact john@example.com")

# Check safety
assert is_safe_for_cloud("hello world") is True
assert is_safe_for_cloud("contact john@example.com") is False
assert is_safe_for_cloud(strip_pii("contact john@example.com")) is True
```

```bash
# Run privacy tests
python -m pytest tests/test_router.py::TestPrivacy -q
```
