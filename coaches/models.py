# coaches/models.py
from django.db import models
from django.urls import reverse

# Import the models this model will have a relationship with
from users.models import CustomUser
from core.models import Team


class Coach(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    contact_number = models.CharField(max_length=20)

    # A coach is in charge of ONE specific team. A team can only have ONE head coach.
    # The OneToOneField enforces this unique relationship.
    team = models.OneToOneField(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The specific team this coach is in charge of (e.g., Basketball - Male - Main Campus)."
    )

    def get_absolute_url(self):
        """Returns the URL to access a particular coach instance."""
        return reverse('coach-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        """
        Overrides the default save method. When a coach is assigned to a team,
        this method finds all unassigned athletes on that team and assigns
        them to this coach.
        """
        # First, save the coach instance itself to ensure it has a PK.
        super().save(*args, **kwargs)
        
        # Now, perform the automatic assignment of athletes.
        if self.team:

            from athletes.models import Athlete
            # Find all athletes on this coach's team who currently have no coach.
            athletes_to_assign = Athlete.objects.filter(team=self.team, coach__isnull=True)
            
            # This check prevents an infinite loop if athlete.save() also triggers something.
            if athletes_to_assign.exists():
                # The .update() method is much more efficient than looping in Python.
                # It performs a single database query.
                athletes_to_assign.update(coach=self)

    def __str__(self):
        return f"{self.user.get_full_name()}"