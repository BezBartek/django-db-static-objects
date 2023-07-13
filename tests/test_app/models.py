from collections.abc import Container
from enum import auto
from typing import Any

from django.db import models


class BasedOnListOfTuplesTemplate:
    country = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    def get_static_objects(cls) -> Container[Any]:
        return [
            (auto(), "Poland", "Warsaw"),
            (auto(), "Germany", "Berlin")
        ]


class BasedOnListOfDictsTemplate:
    country = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    def get_static_objects(cls) -> Container[Any]:
        return [
            {"record_identifier": auto(), "country": "Poland", "capital": "Warsaw"},
            {"record_identifier": auto(), "country": "Germany", "capital": "Berlin"}
        ]
