# events/admin.py
from django.contrib import admin
from .models import Event, ParticipationLog

admin.site.register(Event)
admin.site.register(ParticipationLog)