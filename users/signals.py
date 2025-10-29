# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from athletes.models import Athlete
from coaches.models import Coach

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create a related Athlete or Coach profile when a new
    CustomUser is created via the signup form.
    """
    if created: # Only run on initial creation
        if instance.role == CustomUser.Role.ATHLETE:
            Athlete.objects.create(user=instance)
        elif instance.role == CustomUser.Role.COACH:
            Coach.objects.create(user=instance)