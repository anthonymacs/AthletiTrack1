# athletes/forms.py
from django import forms
from .models import PerformanceStat, Athlete
from users.models import CustomUser
from core.models import Campus, Sport
from core.models import Team, Statistic
import datetime


#class PerformanceStatForm(forms.ModelForm):
#    class Meta:
#        model = PerformanceStat
#        # We will set the 'athlete' field in the view, so we exclude it from the form
#        fields = ['statistic_name', 'value', 'year']
#        widgets = {
#            'statistic_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 100m Sprint Time'}),
#            'value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 11.2s or 15'}),
#            'year': forms.NumberInput(attrs={'class': 'form-control'}),
#        }
#        labels = {
#            'statistic_name': 'Statistic Name',
#        }

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        # You could pre-populate the year field or add other logic here if needed
#        self.fields['year'].help_text = "The year this statistic was recorded for."


class AthleteUserForm(forms.ModelForm):
    """Form for the CustomUser part of the Athlete profile."""
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender', 'birthday', 'image']
        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class AthleteProfileForm(forms.ModelForm):
    """Form for the Athlete-specific part of the profile."""
    class Meta:
        model = Athlete
        fields = ['contact_details', 'team', 'is_featured', 'medical_history']




#class BulkFilterForm(forms.Form):
#    sport = forms.ModelChoiceField(
#        queryset=Sport.objects.all(),
#        empty_label="-- Select a Sport --",
#        widget=forms.Select(attrs={'class': 'form-select'})
#    )
#    campus = forms.ModelChoiceField(
#        queryset=Campus.objects.all(),
#        empty_label="-- Select a Campus --",
#        widget=forms.Select(attrs={'class': 'form-select'})
#    )


class TeamSelectForm(forms.Form):
    """A simple form to select a single team. Replaces BulkFilterForm."""
    team = forms.ModelChoiceField(
        queryset=Team.objects.all().order_by('sport__name', 'campus__name', 'gender'),
        label="Select Team",
        empty_label="-- Select a Team --",
        widget=forms.Select(attrs={'class': 'form-select select2-filter'})
    )


class BulkAthleteEntryForm(forms.Form):
    """
    A form for a single row in the new team-based bulk athlete creation process.
    Replaces BulkAthleteForm and CategorizedBulkAthleteForm.
    """
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))


class AthleteCategorySelectForm(forms.Form):
    """Step 1: The form to select the category for a new athlete."""
    sport = forms.ModelChoiceField(
        queryset=Sport.objects.all(),
        empty_label="-- Select a Sport --",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    campus = forms.ModelChoiceField(
        queryset=Campus.objects.all(),
        empty_label="-- Select a Campus --",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    gender = forms.ChoiceField(
        choices=[('', '-- Select a Gender --')] + CustomUser.Gender.choices,
        widget=forms.Select(attrs={'class': 'form-select'})
    )


CORE_STATISTICS = [
    ('sprint_100m', '100m Sprint (seconds)'),
    ('long_jump', 'Long Jump (meters)'),
    ('vertical_leap', 'Vertical Leap (inches)'),
    ('wins', 'Wins (for the year)'),
    ('losses', 'Losses (for the year)'),
]

UNIVERSAL_STATISTICS = [
    ('wins', 'Wins'),
    ('losses', 'Losses'),
]

class ScorecardForm(forms.Form):
    """
    A form for entering a "scorecard" of the 5 core statistics for a given year.
    """
    year = forms.IntegerField(
        initial=datetime.date.today().year,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        sport = kwargs.pop('sport', None)
        super().__init__(*args, **kwargs)
        # Dynamically create a field for each core statistic

        for key, label in UNIVERSAL_STATISTICS:
            self.fields[key] = forms.CharField(
                label=label,
                required=False,
                widget=forms.TextInput(attrs={'class': 'form-control'})
            )


        if sport:
            sport_specific_stats = Statistic.objects.filter(sport=sport)
            for stat in sport_specific_stats:
                self.fields[stat.short_name] = forms.CharField(
                    label=stat.name,
                    required=False,
                    widget=forms.TextInput(attrs={'class': 'form-control'})
                )

class TeamSelectForm(forms.Form):
    """A simple form to select a single team."""
    team = forms.ModelChoiceField(
        queryset=Team.objects.all().order_by('sport__name', 'campus__name', 'gender'),
        label="Select Team",
        empty_label="-- Select a Team --",
        widget=forms.Select(attrs={'class': 'form-select select2-filter'})
    )

class BulkAthleteEntryForm(forms.Form):
    """A form for a single row in the new team-based bulk athlete creation process."""
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    gender = forms.ChoiceField(choices=CustomUser.Gender.choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))


