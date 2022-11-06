from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .models import Doctor
from .serializers import DoctorSerializer


class ListCreateMovieAPIView(ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = (AllowAny, )
    pagination_class = None


class DoctorAPIView(RetrieveAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = (AllowAny, )
