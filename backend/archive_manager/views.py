from rest_framework import generics

from .models import Buildings
from .serializers import BuildingsSerializer


class BuildingsList(generics.ListAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingsSerializer
