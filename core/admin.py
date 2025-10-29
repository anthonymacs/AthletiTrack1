# core/admin.py
from django.contrib import admin
from .models import Feedback, Campus, Sport, Team


admin.site.register(Feedback)
admin.site.register(Campus)
admin.site.register(Sport)
admin.site.register(Team)

def ready(self):
    import core.signals