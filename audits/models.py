# audits/models.py
from django.db import models
from users.models import CustomUser

class AuditLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255) # e.g., "User Login", "Event Created", "Athlete Deleted"
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True) # e.g., "Event 'Team Practice' created by Coach Smith."

    def __str__(self):
        user_str = self.user.username if self.user else "System"
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M')} - {user_str} - {self.action}"