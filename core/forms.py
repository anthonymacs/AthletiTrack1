# core/forms.py
from django import forms
from .models import Feedback
from .models import Sport, Campus, Team, Statistic

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['sport', 'campus', 'gender']
        widgets = {
            # Add the 'select2-filter' class to make these searchable
            'sport': forms.Select(attrs={'class': 'form-select select2-filter'}),
            'campus': forms.Select(attrs={'class': 'form-select select2-filter'}),
            'gender': forms.Select(attrs={'class': 'form-select'}), # Gender doesn't need to be searchable
        }

# Define CHOICES here, at the module level, so it's globally accessible within this file.
CHOICES = [(i, str(i)) for i in range(1, 6)]

class FeedbackForm(forms.ModelForm):
    # No longer need CHOICES defined here

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define labels for each question
        self.fields['sus_q1'].label = "1. I think that I would like to use this system frequently."
        self.fields['sus_q2'].label = "2. I found the system unnecessarily complex."
        self.fields['sus_q3'].label = "3. I thought the system was easy to use."
        self.fields['sus_q4'].label = "4. I think that I would need the support of a technical person to be able to use this system."
        self.fields['sus_q5'].label = "5. I found the various functions in this system were well integrated."
        self.fields['sus_q6'].label = "6. I thought there was too much inconsistency in this system."
        self.fields['sus_q7'].label = "7. I would imagine that most people would learn to use this system very quickly."
        self.fields['sus_q8'].label = "8. I found the system very cumbersome to use."
        self.fields['sus_q9'].label = "9. I felt very confident using the system."
        self.fields['sus_q10'].label = "10. I needed to learn a lot of things before I could get going with this system."
        self.fields['comments'].label = "Please provide any additional comments, suggestions, or issues you found (critical feedback)."

    class Meta:
        model = Feedback
        exclude = ['user']
        # Now, the 'Meta' class can find 'CHOICES' because it's defined in the module scope.
        widgets = {
            'sus_q1': forms.RadioSelect(choices=CHOICES),
            'sus_q2': forms.RadioSelect(choices=CHOICES),
            'sus_q3': forms.RadioSelect(choices=CHOICES),
            'sus_q4': forms.RadioSelect(choices=CHOICES),
            'sus_q5': forms.RadioSelect(choices=CHOICES),
            'sus_q6': forms.RadioSelect(choices=CHOICES),
            'sus_q7': forms.RadioSelect(choices=CHOICES),
            'sus_q8': forms.RadioSelect(choices=CHOICES),
            'sus_q9': forms.RadioSelect(choices=CHOICES),
            'sus_q10': forms.RadioSelect(choices=CHOICES),
        }


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['sport', 'name', 'short_name', 'description']
        widgets = {
            'sport': forms.HiddenInput(), # The sport is set automatically
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }