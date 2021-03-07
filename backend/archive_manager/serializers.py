from typing import Any, Dict, List

from django.db.models.query import QuerySet


def serialize_buiding(building: Dict) -> Dict[int, Any]:
    return {"age": building.get("age"), "geometry": building.get("geometry").coords}


def buildings_serializer(buildings_query: QuerySet) -> List:
    return list(map(serialize_buiding, buildings_query))
