import json
from typing import Dict, List, Generator,Tuple,Any
import time
from operator import itemgetter
from collections import ChainMap


class ParseJson:
    def __init__(self, path) -> None:
        self.path = path
        self.json_file = self._open_json()

    def _open_json(self,) -> Dict:
        with open(self.path, "r") as file:
            json_file = json.load(file)
        return json_file

    def get_features(self) -> List:
        return self.json_file["features"]

    def _chain_dicts(self,tuple):
        return dict(ChainMap(*tuple))

    def get_properties_and_geometry(self) -> Generator[Tuple[str,str], Any, None]:
        return (
            self._chain_dicts(itemgetter("properties", "geometry")(feature))
            for feature in self.get_features()
        )


if __name__ == "__main__":
    pass
