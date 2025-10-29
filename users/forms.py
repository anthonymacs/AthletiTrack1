from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from athletes.models import Athlete
from coaches.models import Coach

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'birthday', 'role', 'image', 'password1', 'password2')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'gender': 'Gender',
            'role': 'Register As',
            'image': 'Profile Picture',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit roles for public registration
        self.fields['role'].choices = [
            (CustomUser.Role.ATHLETE, 'Athlete'),
            (CustomUser.Role.COACH, 'Coach'),
        ]
        # Styling password fields
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['birthday'].widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'gender', 'birthday', 'image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'gender': 'Gender',
            'image': 'Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance.email != email and CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already used by another account.")
        return email


class AthleteProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['medical_history', 'contact_details', 'team']
        labels = {
            'birthday': 'Date of Birth',
            'sport': 'Sport',
        }
        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sport': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CoachProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('team',)  # Adjust according to your Coach model
        labels = {
            'team': 'Team',
        }
        widgets = {
            'team': forms.TextInput(attrs={'class': 'form-control'}),
        }
