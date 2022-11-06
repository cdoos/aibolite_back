from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdminModel(admin.ModelAdmin):
    list_display = ("user", "category", "price_per_appointment", "rating", "homepage_url")
