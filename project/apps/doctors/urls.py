from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListDoctorsAPIView.as_view(), name='get_doctors'),
    path('<int:pk>/', views.DoctorAPIView.as_view(), name='get_doctor'),
]
