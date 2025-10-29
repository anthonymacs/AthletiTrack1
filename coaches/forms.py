# coaches/forms.py
from django import forms
from .models import Coach
from users.models import CustomUser

class CoachUserForm(forms.ModelForm):
    """Form for the CustomUser part of the Coach profile."""
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender', 'birthday', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CoachProfileForm(forms.ModelForm):
    """Form for the Coach-specific part of the profile."""
    class Meta:
        model = Coach
        fields = ['contact_number', 'team',]
        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            # Update the widget for the new 'team' field
            'team': forms.Select(attrs={'class': 'form-select select2-filter'}),
        }


