# users/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required # We need this
from django.contrib import messages


from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
    AthleteProfileUpdateForm,
    CoachProfileUpdateForm
)
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') # Redirect to login page on successful registration
    template_name = 'registration/signup.html'


@login_required
def profile_view(request):
    """
    Displays and handles the update form for a user's profile.
    """
    user = request.user
    ProfileForm = None
    profile_instance = getattr(user, 'athlete', None)

    # Determine which profile form to use based on the user's role
    if hasattr(user, 'athlete'):
        ProfileForm = AthleteProfileUpdateForm
        profile_instance = user.athlete
    elif hasattr(user, 'coach'):
        ProfileForm = CoachProfileUpdateForm
        profile_instance = user.coach

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile_instance) if ProfileForm else None

        if user_form.is_valid() and (profile_form is None or profile_form.is_valid()):
            user_form.save()
            if profile_form:
                profile_form.save()

            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile') # Redirect back to the same page

    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileForm(instance=profile_instance) if ProfileForm else None

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)