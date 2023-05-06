from rest_framework import viewsets

from havij.models import Havij
from havij.serializers import HavijSerializer


class HavijViewSet(viewsets.ModelViewSet):
    queryset = Havij.objects.all()
    serializer_class = HavijSerializer
