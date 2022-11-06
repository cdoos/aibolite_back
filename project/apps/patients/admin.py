from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdminModel(admin.ModelAdmin):
    list_display = ("user", "email", "registration_date")
