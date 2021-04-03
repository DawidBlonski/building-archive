from rest_framework.generics import ListAPIView
from rest_framework_gis.filters import InBBoxFilter
from silk.profiling.profiler import silk_profile

from .models import Buildings
from .serializers import BuildingnSerializer


class BuildingsList(ListAPIView):
    queryset = Buildings.objects.values("age", "geometry").filter(
        geometry__isnull=False
    )
    serializer_class = BuildingnSerializer
    filter_backends = (InBBoxFilter,)
    bbox_filter_field = 'point'

    @silk_profile()
    def get(self, request, *args, **kwargs):
        print(request.build_absolute_uri())
        return super().get(request, *args, **kwargs)
