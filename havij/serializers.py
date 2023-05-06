from rest_framework import serializers

from havij.models import Havij


class HavijSerializer(serializers.ModelSerializer):
    class Meta:
        model = Havij
        fields = "__all__"
