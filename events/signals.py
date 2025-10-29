# events/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_q.models import Schedule
from django_q.tasks import schedule
from datetime import timedelta
from django.utils import timezone # Make sure timezone is imported
from .models import Event

@receiver(post_save, sender=Event)
def schedule_event_reminder(sender, instance, **kwargs):
    """
    Schedules or re-schedules an EMAIL reminder when an Event is saved.
    """
    email_task_name = f'event_email_reminder_{instance.pk}'

    # Manually delete any old schedule for this email to prevent duplicates
    Schedule.objects.filter(name=email_task_name).delete()

    # Schedule the new email reminder (e.g., 24 hours before the event)
    email_run_time = instance.start_time - timedelta(minutes=1)
    
    # Only schedule if the event is in the future
    if email_run_time > timezone.now():
        schedule(
            'events.tasks.send_event_reminders',
            instance.pk,
            name=email_task_name,
            schedule_type='O',
            next_run=email_run_time
        )
        print(f"Successfully scheduled EMAIL reminder for event '{instance.name}' to run at {email_run_time}.")


@receiver(post_delete, sender=Event)
def delete_event_reminders(sender, instance, **kwargs):
    """
    Deletes any scheduled reminders when an Event is deleted.
    """
    email_task_name = f'event_email_reminder_{instance.pk}'
    
    # Also remove the SMS task name just in case old ones are in the DB
    sms_task_name = f'event_sms_reminder_{instance.pk}'

    Schedule.objects.filter(name=email_task_name).delete()
    Schedule.objects.filter(name=sms_task_name).delete()

    print(f"Deleted reminders for event '{instance.name}' (ID: {instance.pk}).")