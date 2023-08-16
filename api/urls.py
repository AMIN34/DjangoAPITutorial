from django.urls import path, include
from .views import PowerDataViewSet, FileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('PowerData', PowerDataViewSet, basename='power_data')
router.register('file', FileViewSet, basename='file')

urlpatterns = [
    path('', include(router.urls)),
]