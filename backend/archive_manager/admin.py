from django.contrib.gis import admin
from .models import PostCode,City,Street,AddresPoint,Buildings

@admin.register(PostCode,City,Street,AddresPoint,Buildings)
class OSMAdmin(admin.OSMGeoAdmin):
    pass
