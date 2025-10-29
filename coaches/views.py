# coaches/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.db import transaction
from .models import Coach, CustomUser
from .forms import CoachUserForm, CoachProfileForm
from core.models import Campus, Sport, Team
from django.contrib import messages
from athletes.models import Athlete
from users.models import CustomUser


class CoachListView(LoginRequiredMixin, ListView):
    model = Coach
    template_name = 'coaches/coach_list.html'
    context_object_name = 'coaches'
    paginate_by = 12 # Optional: Adds pagination if you have many coaches

    def get_queryset(self):
        """
        Builds the queryset for the list of coaches, including filtering
        and pre-fetching related data for efficiency.
        """
        # The new, correct query uses the team relationship.
        queryset = Coach.objects.select_related('user', 'team__sport', 'team__campus')
        team_filter = self.request.GET.get('team')
        sport_filter = self.request.GET.get('sport')
        campus_filter = self.request.GET.get('campus')
        gender_filter = self.request.GET.get('gender')

        # Updated filtering logic.
        if sport_filter:
            queryset = queryset.filter(team__sport_id=sport_filter)
        if campus_filter:
            queryset = queryset.filter(team__campus_id=campus_filter)
        if gender_filter:
            queryset = queryset.filter(user__gender=gender_filter)

        return queryset.order_by('user__first_name')

    def get_context_data(self, **kwargs):
        """
        Adds the necessary data for the filter forms to the context.
        """
        context = super().get_context_data(**kwargs)
        # Pass the correct context variables for the new filters.
        context['sports'] = Sport.objects.all().order_by('name')
        context['campuses'] = Campus.objects.all().order_by('name')
        context['genders'] = CustomUser.Gender.choices
        return context

    
class CoachCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = CoachUserForm
    template_name = 'coaches/coach_form.html'
    success_url = reverse_lazy('coach-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['profile_form'] = CoachProfileForm(self.request.POST)
        else:
            context['profile_form'] = CoachProfileForm()
        context['form_title'] = "Add New Coach"
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']
        with transaction.atomic():
            if form.is_valid() and profile_form.is_valid():
                # --- START OF FIX ---
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                email = form.cleaned_data.get('email')

                # Generate a simple username
                base_username = f"{first_name.lower()}.{last_name.lower()}"
                username = base_username
                counter = 1
                # Ensure the username is unique
                while CustomUser.objects.filter(username=username).exists():
                    username = f"{base_username}{counter}"
                    counter += 1

                # Check if email already exists
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(self.request, f"A user with the email {email} already exists.")
                    return self.form_invalid(form)

                user = form.save(commit=False)
                user.username = username # Assign the generated username
                # --- END OF FIX ---
                user.role = CustomUser.Role.COACH
                user.set_password('password123')
                user.save()

                self.object = user

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                messages.success(self.request, f"Coach '{user.get_full_name()}' created successfully.")
                return redirect(self.get_success_url())
        return super().form_invalid(form)

class CoachDetailView(LoginRequiredMixin, DetailView):
    model = Coach
    template_name = 'coaches/coach_detail.html'
    context_object_name = 'coach'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all athletes assigned to this coach
        context['assigned_athletes'] = Athlete.objects.filter(coach=self.object)
        return context
    

class CoachUpdateView(LoginRequiredMixin, UpdateView):
    model = Coach
    template_name = 'coaches/coach_form.html'
    form_class = CoachProfileForm # We only edit the profile part here for simplicity
    second_form_class = CoachUserForm
    success_url = reverse_lazy('coach-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = f"Edit Coach: {self.object.user.get_full_name()}"
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=self.object.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        form2 = self.second_form_class(request.POST, request.FILES, instance=self.object.user)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, 'Coach profile updated successfully!')
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class CoachDeleteView(LoginRequiredMixin, DeleteView):
    model = Coach
    template_name = 'coaches/coach_confirm_delete.html'
    success_url = reverse_lazy('coach-list')