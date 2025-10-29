# athletes/admin.py
from django.contrib import admin
from .models import Athlete, PerformanceStat


class AthleteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'coach', 'is_featured') # Show the athlete's name and featured status
    list_filter = ('is_featured', 'coach') # Allow filtering by featured status
    search_fields = ('user__username', 'user__first_name', 'user__last_name') # Make athletes searchable

    
#admin.site.register(Athlete)
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(PerformanceStat)