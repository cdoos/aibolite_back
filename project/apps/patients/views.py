from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = (AllowAny, )
    http_method_names = ['get', 'post', 'head', 'patch']
    pagination_class = None
