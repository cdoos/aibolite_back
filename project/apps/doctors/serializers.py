from rest_framework import serializers
from .models import Doctor
from apps.users.serializers import UserSerializer
from drf_writable_nested import WritableNestedModelSerializer


class DoctorSerializer(WritableNestedModelSerializer,
                       serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = (
            "user",
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
