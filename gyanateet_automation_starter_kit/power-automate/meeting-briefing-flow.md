# Power Automate Flow: Meeting/Event Briefing

## Goal
Send a prep brief before important calendar events.

## Trigger
Scheduled cloud flow, every weekday at 07:00.

## Steps
1. Get today's Outlook calendar events.
2. Filter events with external attendees, event keywords, interviews, talks, demos, or travel.
3. For each event, collect:
   - title
   - time/location
   - attendees
   - links in description
   - related recent emails
4. Generate a briefing:
   - context
   - people/orgs
   - likely agenda
   - questions to ask
   - documents to review
5. Send to yourself in Teams or Outlook.

## Safety
No outbound messages to attendees are sent automatically.
