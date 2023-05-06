from django.urls import include, path
from rest_framework import routers

from havij.views import HavijViewSet


router = routers.DefaultRouter()
router.register(r"", HavijViewSet)

urlpatterns = [
    path(r"", include(router.urls)),
]
