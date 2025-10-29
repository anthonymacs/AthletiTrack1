# core/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sport, Campus, Team
from users.models import CustomUser

@receiver(post_save, sender=Sport)
def create_teams_for_new_sport(sender, instance, created, **kwargs):
    """
    When a new Sport is created, automatically create a Male and Female team
    for that sport at every existing Campus.
    """
    if created: # Only run when a new Sport is created
        campuses = Campus.objects.all()
        genders = [CustomUser.Gender.MALE, CustomUser.Gender.FEMALE]

        for campus in campuses:
            for gender in genders:
                # get_or_create prevents errors if a team somehow already exists
                Team.objects.get_or_create(
                    sport=instance,
                    campus=campus,
                    gender=gender
                )
        print(f"Created teams for new sport '{instance.name}' across {len(campuses)} campuses.")