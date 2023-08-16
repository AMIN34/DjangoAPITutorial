from django.urls import path, include
from .views import PowerDataViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('PowerData', PowerDataViewSet, basename='power_data')


urlpatterns = [
    path('', include(router.urls))
]