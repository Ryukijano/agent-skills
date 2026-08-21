# AI for Personal Productivity

## Description

Use AI to prioritize tasks, resolve calendar conflicts, block focus time, and automate repetitive personal workflows.

## When to use

You want to prioritize tasks, resolve calendar conflicts, block focus time, or automate repetitive personal workflows.

## Usage

- Prioritize tasks with urgency/importance scoring or learned preferences.
- Resolve calendar conflicts and propose reschedules or declines.
- Block deep-work windows and protect focus time.
- Automate email triage, travel booking, and recurring task workflows.

## Steps

1. Sync calendar, task, and email data with minimal, scoped permissions.
2. Build a preference model from user edits and past decisions.
3. Generate a daily or weekly plan and compare it to the user's manual plan.
4. Propose conflict resolutions and schedule focus blocks.
5. Test on synthetic data first, then let the user approve every change.

## Code pattern

```python
# Simplified task ordering by priority (lower number = higher priority)
tasks = [("email", 3), ("planning", 2), ("deep_work", 1)]
ordered = sorted(tasks, key=lambda x: x[1])
print([t[0] for t in ordered])
```

## Tuning notes

- Learn from user edits rather than overriding their preferences.
- Respect focus time and avoid over-scheduling back-to-back meetings.
- Integrate with calendar APIs using minimal, scoped permissions.
- Test on synthetic calendars before applying to a user's real schedule.

## Verification

1. Build a daily task scheduler and compare its plan to a user's manual plan.
2. Resolve a synthetic calendar conflict using stated priorities.
3. Auto-categorize low-priority emails and measure time saved.

## References

- https://aclanthology.org/2026.acl-long.1648.pdf
- https://arxiv.org/abs/2601.11957
- https://arxiv.org/abs/2509.25693
- https://aclanthology.org/2026.acl-long.1614.pdf
