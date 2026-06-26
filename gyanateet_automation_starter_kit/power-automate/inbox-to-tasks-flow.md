# Power Automate Flow: Inbox to Tasks

## Goal
Turn emails containing commitments/deadlines into draft tasks for human review.

## Trigger
Outlook: When a new email arrives in Inbox.

## Conditions
Check subject/body for:

- deadline
- due
- please review
- can you send
- meeting preparation
- travel/action required

## AI step
Use Copilot/AI Builder or an HTTP call to classify:

```json
{
  "is_task": true,
  "task_title": "...",
  "due_date": "...",
  "priority": "low|medium|high",
  "source_email_id": "...",
  "confidence": 0.0
}
```

## Human approval
If confidence < 0.85 or email is from a new sender, use Approvals.

## Action
Create Microsoft To Do/Planner task with link back to source email.

## Safety
Do not send replies automatically. Draft only.
