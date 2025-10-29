#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class CustomUser(AbstractUser):
    """
    An extended user model that includes roles, gender, birthday, and a profile image.
    """
    class Role(models.TextChoices):
        ADMINISTRATOR = "ADMINISTRATOR", "Administrator"
        COACH = "COACH", "Coach"
        ATHLETE = "ATHLETE", "Athlete"

    class Gender(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'
        OTHER = 'OTHER', 'Other'

    # --- Fields ---
    role = models.CharField(max_length=50, choices=Role.choices)
    gender = models.CharField(max_length=10, choices=Gender.choices, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    # --- Methods ---
    def save(self, *args, **kwargs):
        # This logic seems to be for setting a default role, but 'base_role'
        # is only defined on the class, not the instance. Let's adjust slightly.
        if not self.pk and not self.role:
             self.role = CustomUser.Role.ATHLETE # A more sensible default for signup
        return super().save(*args, **kwargs)

    @property
    def age(self):
        """
        Calculates the user's age based on their birthday.
        Returns None if no birthday is set.
        """
        if self.birthday:
            today = date.today()
            # This calculation correctly handles leap years and birth dates yet to occur in the current year.
            return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return None
    
    # --- THIS IS THE NEW, CORRECTED save() METHOD ---
    def save(self, *args, **kwargs):
        """
        Overrides the default save method to set the correct role for users,
        especially ensuring superusers are always administrators.
        """
        # If the user is being created (no primary key yet) and has no role set
        if not self.pk and not self.role:
            # Check if the user is a superuser
            if self.is_superuser:
                self.role = self.Role.ADMINISTRATOR
            else:
                # You could set a different default for normal users if needed,
                # but our forms handle this. For now, we can leave it blank.
                # self.role = self.Role.ATHLETE # (Example)
                pass
        
        # Call the original save method
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"