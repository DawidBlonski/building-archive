import time

from django.contrib.gis.geos.collections import MultiPolygon
from django.test import Client, TestCase
from django.urls import reverse

from .models import AdresPoint, Buildings, City, PostCode, Street


class ModelTests(TestCase):
    fixtures = ["backend/archive_manager/fixtures/archive.json"]

    def test_create_city(self):
        city = City.objects.get(pk=987331)
        self.assertEqual(city.city, "Strzelin")
        self.assertEqual(city.__str__(), "Strzelin")

    def test_create_street(self):
        city = Street.objects.get(pk=281)
        self.assertEqual(city.street, "Wrocławska")
        self.assertEqual(city.street_id, 24806)
        self.assertEqual(city.city.pk, 987331)
        self.assertEqual(city.__str__(), "Wrocławska Strzelin")

    def test_create_post_code(self):
        post_code = PostCode.objects.get(pk="57-100")
        self.assertEqual(post_code.pk, "57-100")
        self.assertEqual(post_code.__str__(), "57-100")

    def test_create_adress_point(self):
        adress_point = AdresPoint.objects.get(pk="a0ef2e0a-269a-4656-ab79-ef1b8550bfa9")
        self.assertEqual(adress_point.adres, "76")
        self.assertEqual(adress_point.city.pk, 987331)
        self.assertEqual(adress_point.street.pk, 281)
        self.assertEqual(adress_point.post_code.pk, "57-100")
        self.assertEqual(adress_point.__str__(), "Strzelin 76")

    def test_create_buildings(self):
        buildings = Buildings.objects.get(pk="001bf341-5618-485f-b215-95c3324a8a8a")
        self.assertEqual(buildings.age, 1978)
        self.assertEqual(
            str(buildings.adress.pk), "a0ef2e0a-269a-4656-ab79-ef1b8550bfa9"
        )
        self.assertTrue(isinstance(buildings.geometry, MultiPolygon))
        self.assertEqual(
            buildings.__str__(), "001bf341-5618-485f-b215-95c3324a8a8a 1978"
        )

    def test_adres_point_foregin_key(self):
        adress_point = AdresPoint.objects.get(pk="a0ef2e0a-269a-4656-ab79-ef1b8550bfa9")
        street_id = adress_point.street.id
        self.assertEqual(street_id, 281)


class ViewTests(TestCase):
    fixtures = ["backend/archive_manager/fixtures/archive.json"]

    def setUp(self) -> None:
        self.buildings_url = reverse("buildings")
        self.client = Client()

    def test_get_all_view_url(self):
        self.assertEqual(self.buildings_url, "/api/buildings")

    def test_get_buildings(self):
        response = self.client.get(self.buildings_url)
        self.assertEqual(response.status_code, 200)

    def test_bbox(self):
        response = self.client.get(
            self.buildings_url, {"in_bbox": "17.078129,50.777480,17.087989,50.780808"}
        )
        self.assertEqual(response.data["features"], [])
        response = self.client.get(self.buildings_url, {"in_bbox": "17,50,18,51"})
        self.assertEqual(len(response.data["features"]), 1)
