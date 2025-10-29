# events/tasks.py
import requests
from django.conf import settings

# Import your Event model
from .models import Event


def send_event_reminders(event_id):
    """
    A task function that fetches an event and sends email reminders to all
    participants using the Mailtrap Email Sending API.
    """
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        print(f"EMAIL TASK FAILED: Event with ID {event_id} does not exist.")
        return

    participants = event.participants.all().prefetch_related('user')
    if not participants:
        print(f"EMAIL TASK COMPLETED: Event '{event.name}' has no participants to notify.")
        return

    # Configuration for Mailtrap API
    url = f"https://sandbox.api.mailtrap.io/api/send/{settings.MAILTRAP_INBOX_ID}"
    headers = {
        "Authorization": f"Bearer {settings.MAILTRAP_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    email_sent_count = 0
    for athlete in participants:
        if not athlete.user.email:
            continue

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <body style="font-family: sans-serif; color: #333;">
            <h2>Event Reminder: {event.name}</h2>
            <p>Hi {athlete.user.first_name},</p>
            <p>This is a friendly reminder about your upcoming event.</p>
            <hr>
            <p><strong>Location:</strong> {event.location}</p>
            <p><strong>Starts:</strong> {event.start_time.strftime('%A, %B %d, %Y at %I:%M %p')}</p>
            <p><strong>Ends:</strong> {event.end_time.strftime('%A, %B %d, %Y at %I:%M %p')}</p>
            <hr>
            <p>We look forward to seeing you there!</p>
            <p><em>- The AthletiTrack System</em></p>
        </body>
        </html>
        """

        payload = {
            "from": {"email": "reminders@athletitrack.com", "name": "AthletiTrack System"},
            "to": [{"email": athlete.user.email}],
            "subject": f"Reminder: {event.name}",
            "text": f"Reminder for {event.name} starting at {event.start_time.strftime('%b %d, %I:%M %p')}",
            "html": html_content,
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            email_sent_count += 1
            print(f"  - Successfully sent Mailtrap email to {athlete.user.email} for event '{event.name}'.")
        except requests.exceptions.RequestException as e:
            print(f"  - FAILED to send Mailtrap email to {athlete.user.email}. Error: {e}")
            
    if email_sent_count > 0:
        print(f"EMAIL TASK COMPLETED: Sent {email_sent_count} reminders for '{event.name}'.")
    else:
        print(f"EMAIL TASK COMPLETED: No participants with valid emails for '{event.name}'.")