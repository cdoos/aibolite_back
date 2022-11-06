from rest_framework import serializers
from .models import Patient
from apps.users.serializers import UserSerializer
from apps.users.models import User
from drf_writable_nested import WritableNestedModelSerializer


class PatientSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = "__all__"
