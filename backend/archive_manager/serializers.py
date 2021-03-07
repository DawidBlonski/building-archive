from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Buildings


class BuildingnSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Buildings
        fields = ("age", "geometry")
        geo_field = "geometry"
