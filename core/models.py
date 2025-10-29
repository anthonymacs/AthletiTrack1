# core/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.models import CustomUser

class Campus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    
def get_absolute_url(self):
    return reverse('athlete-detail', kwargs={'pk': self.pk})

class Feedback(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # SUS Questions (1-5 scale)
    sus_q1 = models.IntegerField() # I think that I would like to use this system frequently.
    sus_q2 = models.IntegerField() # I found the system unnecessarily complex.
    sus_q3 = models.IntegerField() # I thought the system was easy to use.
    sus_q4 = models.IntegerField() # I think that I would need the support of a technical person to be able to use this system.
    sus_q5 = models.IntegerField() # I found the various functions in this system were well integrated.
    sus_q6 = models.IntegerField() # I thought there was too much inconsistency in this system.
    sus_q7 = models.IntegerField() # I would imagine that most people would learn to use this system very quickly.
    sus_q8 = models.IntegerField() # I found the system very cumbersome to use.
    sus_q9 = models.IntegerField() # I felt very confident using the system.
    sus_q10 = models.IntegerField()# I needed to learn a lot of things before I could get going with this system.
    # Qualitative Feedback
    comments = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} on {self.submitted_at.strftime('%Y-%m-%d')}"
    

class Team(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=CustomUser.Gender.choices)

    class Meta:
        # This ensures you can't create two "Basketball - Male" teams for the same campus
        unique_together = ('sport', 'campus', 'gender')

    def __str__(self):
        # This will create a nice display name like "Basketball (Male) - Main Campus"
        return f"{self.sport.name} ({self.get_gender_display()}) - {self.campus.name}"

class Statistic(models.Model):
    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE,
        related_name='statistics',
        null=True, # Still allow null for universal stats
        blank=True
    )
    name = models.CharField(
        max_length=100,
        help_text="The full name of the statistic (e.g., 'Points Per Game')"
    )
    # --- THIS IS THE FIX (Part 1) ---
    # Remove unique=True from here
    short_name = models.CharField(
        max_length=20,
        help_text="A short, unique code for this stat (e.g., 'ppg')"
    )
    # --- END OF FIX ---
    description = models.TextField(blank=True, null=True)

    class Meta:
        # A stat name should be unique within a given sport
        unique_together = ('sport', 'short_name')

    def __str__(self):
        sport_name = self.sport.name if self.sport else "Universal"
        return f"{self.name} ({sport_name})"