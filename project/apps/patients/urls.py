from .views import PatientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PatientViewSet)


urlpatterns = [
]

urlpatterns += router.urls
