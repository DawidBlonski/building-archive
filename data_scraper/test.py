from data_scraper.parse_address_point import ParseJson
import unittest
import types


class TestParseAdressPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.parse_json = ParseJson('test2.geojson')
        self.get_fetures = self.parse_json.get_features()

    def test_open_json_file(self):
        assert isinstance(self.parse_json.json_file, dict)

    def test_open_bad_file(self):
        self.assertRaises(FileNotFoundError, ParseJson, "teest2.geojson")

    def test_get_features(self):
        assert isinstance(self.get_fetures, list)

    def test_get_properties_and_geometry(self):
        assert isinstance(
            self.parse_json.get_properties_and_geometry(),
            types.GeneratorType,
        )
    def test_merge_objects(self):
        input_value = ({'a':'a','b':'b'},{'c':'c','d':'d'})
        output = self.parse_json._chain_dicts(input_value)
        expected = {'a':'a','b':'b','c':'c','d':'d'}
        self.assertEqual(output,expected)
