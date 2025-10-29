#athletes/models.py
from django.db import models
from users.models import CustomUser
from coaches.models import Coach
from core.models import Campus, Sport
from django.urls import reverse
from core.models import Team, Statistic


class Athlete(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    birthday = models.DateField(null=True, blank=True)
    medical_history = models.TextField(blank=True, null=True)
    contact_details = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)

    # An athlete belongs to ONE specific team.
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # The coach field is automatically managed by the save() method.
    coach = models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        """Returns the URL to access a particular athlete instance."""
        return reverse('athlete-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to automatically assign the
        correct coach based on the athlete's team.
        """
        if self.team:
            try:
                # Find the coach that is assigned to this athlete's team.
                # Since the 'team' field on the Coach model is a OneToOneField,
                # this will return one coach or raise a DoesNotExist error.
                self.coach = Coach.objects.get(team=self.team)
            except Coach.DoesNotExist:
                # If the team has no coach assigned, the athlete has no coach.
                self.coach = None
        else:
            # If the athlete is not on a team, they have no coach.
            self.coach = None

        # Call the original save method to save the instance to the database.
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.get_full_name()}"


class PerformanceStat(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name="performance_stats")
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)
    
    # Use a string reference to the Event model to prevent circular imports.
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        related_name="game_stats",
        null=True,
        blank=True
    )
    
    value = models.CharField(max_length=50)
    date_recorded = models.DateField(auto_now_add=True)

    class Meta:
        # The unique constraint now ensures one stat type per athlete per event.
        unique_together = ('athlete', 'statistic', 'event')

    def __str__(self):
        return f"{self.athlete} - {self.statistic.name} in {self.event.name}: {self.value}"