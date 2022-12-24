from django.contrib.auth.forms import UserCreationForm
from django import forms
from weather.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """A User-Creation form for Registration,
       with additional tweaks.

    Args:
        UserCreationForm: A predefined django User creation form.
    """

    first_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    email = forms.EmailField(
        max_length=254, help_text="Required. Insert a valid email address."
    )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
