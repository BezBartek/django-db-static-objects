import abc
from collections.abc import Container
from typing import Any

from django.db import models


class AbstractModelMeta(abc.ABCMeta, type(models.Model)):
    pass


class StaticObjectsModel(models.Model, metaclass=AbstractModelMeta):
    record_identifier = models.CharField(primary_key=True, db_index=True)

    @classmethod
    @abc.abstractmethod
    def get_static_objects(cls) -> Container[Any]:
        """
            :return: List of unique objects that can be map to table records.
        """
        ...

    class Meta:
        abstract = True
