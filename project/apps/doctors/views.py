from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Doctor
from .serializers import DoctorSerializer


# class ListDoctorsAPIView(ListAPIView):
#     serializer_class = DoctorSerializer
#     queryset = Doctor.objects.all()
#     permission_classes = (AllowAny, )
#     pagination_class = None
#
#
# class DoctorAPIView(RetrieveAPIView):
#     serializer_class = DoctorSerializer
#     queryset = Doctor.objects.all()
#     permission_classes = (AllowAny, )


class DoctorViewSet(ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = (AllowAny, )
    pagination_class = None