from django.contrib.gis import admin

from .models import AdresPoint, Buildings, City, PostCode, Street


@admin.register(PostCode, City, Street, AdresPoint, Buildings)
class OSMAdmin(admin.OSMGeoAdmin):
    pass
