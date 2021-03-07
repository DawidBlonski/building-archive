from rest_framework.request import Request
from rest_framework.views import APIView, Response
from django.http import JsonResponse
from silk.profiling.profiler import silk_profile

from .models import Buildings
from .serializers import buildings_serializer


class BuildingsList(APIView):
    @silk_profile(name="Build")
    def get(self, request: Request, *args, **kwargs) -> Response:
        queryset = Buildings.objects.values("age", "geometry").filter(
            geometry__isnull=False
        )
        serializer = buildings_serializer(queryset)
        return JsonResponse(serializer,safe=False)
