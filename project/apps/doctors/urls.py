from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.DoctorViewSet)

urlpatterns = [
    # path('', views.ListDoctorsAPIView.as_view(), name='get_doctors'),
    # path('<int:pk>/', views.DoctorAPIView.as_view(), name='get_doctor'),
]

urlpatterns += router.urls
