from django.contrib import admin
from doctors.models import Doctor
from patients.models import Patient


@admin.register(Doctor)
class DoctorAdminModel(admin.ModelAdmin):
    list_display = ("user", "category", "price_per_appointment", "rating", "homepage_url")


@admin.register(Patient)
class PatientAdminModel(admin.ModelAdmin):
    list_display = ("user", "email", "registration_date")
