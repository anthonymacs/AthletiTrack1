# audits/signals.py
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AuditLog
from events.models import Event
from athletes.models import Athlete, PerformanceStat

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    AuditLog.objects.create(
        user=user,
        action="User Logged In",
        details=f"User '{user.username}' logged in from IP: {request.META.get('REMOTE_ADDR')}"
    )

@receiver(post_save, sender=Event)
def log_event_save(sender, instance, created, **kwargs):
    action = "Event Created" if created else "Event Updated"
    AuditLog.objects.create(
        user=instance.coach_in_charge.user if instance.coach_in_charge else None,
        action=action,
        details=f"Event '{instance.name}' was { 'created' if created else 'updated' }."
    )


@receiver(post_save, sender=Event)
def log_event_save(sender, instance, created, **kwargs):
    action = "Event Created" if created else "Event Updated"
    # We need to find who performed the action. We can assume the coach in charge did it.
    user = instance.coach_in_charge.user if instance.coach_in_charge else None
    AuditLog.objects.create(
        user=user,
        action=action,
        details=f"Event '{instance.name}' was {'created' if created else 'updated'}."
    )

# --- THIS IS THE NEW SIGNAL HANDLER (Step 2) ---
@receiver(post_save, sender=PerformanceStat)
def log_performance_stat_save(sender, instance, created, **kwargs):
    """
    Creates an audit log entry whenever a PerformanceStat is created or updated.
    """
    action = "Statistic Added" if created else "Statistic Updated"
    
    # We need to figure out WHO performed the action. This is tricky with signals.
    # The 'instance' is the PerformanceStat itself. The user isn't directly attached.
    # We can assume the athlete's assigned coach is the one who updated the stats.
    # A more advanced system would pass the user from the view, but this is a good approximation.
    actor = None
    if instance.athlete and instance.athlete.coach:
        actor = instance.athlete.coach.user

    AuditLog.objects.create(
        user=actor, # The user who likely performed the action
        action=action,
        details=f"Stat '{instance.statistic.name}' for athlete '{instance.athlete.user.get_full_name()}' was {'added' if created else 'updated'} with value '{instance.value}' for year {instance.year}."
    )