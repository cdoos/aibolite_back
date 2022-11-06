from rest_framework import serializers
from .models import Doctor
from django.contrib.auth.models import User


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            "id",
            "department_id",
            "specialization_details_id",
            "experience_in_years",
            "category",
            "price_per_appointment",
            "schedule_details",
            "degree",
            "rating",
            "homepage_url",
        )
