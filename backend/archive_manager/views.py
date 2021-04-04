from rest_framework.generics import ListAPIView
from rest_framework_gis.filters import InBBoxFilter
from silk.profiling.profiler import silk_profile
from django.core.cache import cache
from rest_framework.response import Response
from .models import Buildings
from .serializers import BuildingnSerializer


class BuildingsList(ListAPIView):
    queryset = Buildings.objects.values("age", "geometry").filter(
        geometry__isnull=False
    )
    serializer_class = BuildingnSerializer
    filter_backends = (InBBoxFilter,)
    bbox_filter_field = 'geometry'

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = cache.get('buildings')
        if not serializer:
            serializer = self.get_serializer(queryset, many=True).data
            cache.set('buildings',serializer)

        return Response(serializer)

    @silk_profile()
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
