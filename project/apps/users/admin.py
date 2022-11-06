from django.contrib import admin
from .models import User


@admin.register(User)
class PatientAdminModel(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "middle_name", "date_of_birth", "iin")
