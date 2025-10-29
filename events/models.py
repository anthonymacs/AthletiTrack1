#events/models.py
from django.db import models
from users.models import CustomUser
from athletes.models import Athlete
from coaches.models import Coach

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    participants = models.ManyToManyField(Athlete, related_name='attended_events', blank=True, through='ParticipationLog')

    coach_in_charge = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_events')

    our_score = models.IntegerField(null=True, blank=True, help_text="The score of the EVSU team.")
    opponent_score = models.IntegerField(null=True, blank=True, help_text="The score of the opponent.")

    def __str__(self):
        return self.name

class ParticipationLog(models.Model):

    class Status(models.TextChoices):
        REGISTERED = 'REGISTERED', 'Registered' # Add a default status
        PRESENT = 'PRESENT', 'Present'
        ABSENT = 'ABSENT', 'Absent'
        EXCUSED = 'EXCUSED', 'Excused'

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    
    # The new status field is more descriptive than a boolean.
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.REGISTERED # Default to 'Registered' when a participant is added
    )
    notes = models.TextField(blank=True, null=True, help_text="Reason for absence, etc.")

    class Meta:
        unique_together = ('event', 'athlete')

    def __str__(self):
        return f"{self.athlete.user.get_full_name()} - {self.event.name} ({self.get_status_display()})"
