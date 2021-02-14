from django.contrib.gis import admin

from .models import AddresPoint, Buildings, City, PostCode, Street


@admin.register(PostCode, City, Street, AddresPoint, Buildings)
class OSMAdmin(admin.OSMGeoAdmin):
    pass
