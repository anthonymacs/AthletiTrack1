# events/forms.py
from django import forms
from .models import Event
from athletes.models import Athlete
from core.models import Statistic, Team
#from django.utils import timezone


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        # We will handle 'participants' separately
        fields = ['name', 'description', 'start_time', 'end_time', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            # Use HTML5 date/time input for better UX
            'schedule': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

       # --- DELETE OR COMMENT OUT THIS ENTIRE METHOD ---
    # def clean_schedule(self):
    #     """
    #     This method is no longer needed as the form field now correctly
    #     provides a timezone-aware datetime.
    #     """
    #     schedule_time = self.cleaned_data.get('schedule')
    #     if schedule_time:
    #         return timezone.make_aware(schedule_time, timezone.get_current_timezone())
    #     return schedule_time



class ParticipantManagementForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(
        queryset=Athlete.objects.none(), # Start with an empty queryset
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="" # Hide the default label
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # The queryset will be set dynamically in the view
        # We set the full queryset here as a fallback
        self.fields['participants'].queryset = Athlete.objects.all().select_related('user', 'sport', 'campus')

        
    class Meta:
        model = Event
        fields = ['participants']


class EventScheduleForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_time', 'end_time', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'start_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }


class GameReportForm(forms.Form):
    """
    A dynamic form for entering a "game report" (stats for an athlete in an event).
    Its fields are built based on the event's sport.
    """
    def __init__(self, *args, **kwargs):
        # The view must pass the 'sport' object to this form
        sport = kwargs.pop('sport', None)
        super().__init__(*args, **kwargs)

        if sport:
            # Get stats for the specific sport of the event
            sport_specific_stats = Statistic.objects.filter(sport=sport)
            
            for stat in sport_specific_stats:
                self.fields[stat.short_name] = forms.CharField(
                    label=stat.name,
                    required=False,
                    widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
                )


class EventOutcomeForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['our_score', 'opponent_score']
        labels = {
            'our_score': 'Our Team\'s Score',
            'opponent_score': 'Opponent\'s Score',
        }
        widgets = {
            'our_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'opponent_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }