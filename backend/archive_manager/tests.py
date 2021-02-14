from django.contrib.gis.geos.collections import MultiPolygon
from django.test import TestCase

from .models import AddresPoint, Buildings, City, PostCode, Street


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
        adress_point = AddresPoint.objects.get(
            pk="a0ef2e0a-269a-4656-ab79-ef1b8550bfa9"
        )
        self.assertEqual(adress_point.adres, "76")
        self.assertEqual(adress_point.city.pk, 987331)
        self.assertEqual(adress_point.street.pk, 281)
        self.assertEqual(adress_point.post_code.pk, "57-100")
        self.assertEqual(adress_point.__str__(), "57-100 Strzelin Wrocławska 76")

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
