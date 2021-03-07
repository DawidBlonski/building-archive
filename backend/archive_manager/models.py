import uuid

from django.contrib.gis.db import models as gis_models
from django.db import models


class City(models.Model):
    id_simc = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.city


class Street(models.Model):
    street_id = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.ForeignKey(City, models.SET_NULL, null=True)

    class Meta:
        unique_together = (("street_id", "city"),)

    def __str__(self) -> str:
        return f"{self.street} {self.city.city}"


class PostCode(models.Model):
    code = models.CharField(primary_key=True, max_length=6)

    def __str__(self) -> str:
        return self.code


class AdresPoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    city = models.ForeignKey(City, models.SET_NULL, null=True)
    street = models.ForeignKey(Street, models.SET_NULL, null=True, blank=True)
    post_code = models.ForeignKey(PostCode, models.SET_NULL, null=True)
    adres = models.CharField(max_length=15)
    geometry = gis_models.PointField()

    def __str__(self) -> str:
        return f"{self.city} {self.adres}"


class Buildings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    adress = models.ForeignKey(AdresPoint, models.SET_NULL, null=True)
    age = models.IntegerField(null=True)
    geometry = gis_models.MultiPolygonField(null=True)

    def __str__(self) -> str:
        return f"{self.id} {'Empty' if not self.age else self.age}"
