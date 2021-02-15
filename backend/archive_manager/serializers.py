from rest_framework import serializers

from .models import Buildings


class BuildingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buildings
        fields = ["age", "geometry"]
