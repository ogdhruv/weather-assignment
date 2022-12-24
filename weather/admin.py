from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from weather.forms import CustomUserCreationForm
from weather.models import CustomUser, City

admin.site.register(City)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_staff",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
