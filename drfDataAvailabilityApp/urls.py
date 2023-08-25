from rest_framework import routers
from django.urls import path, include
from .views import DataPointViewSet

router = routers.DefaultRouter()
router.register(r'data_points', DataPointViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
