from functools import cached_property
from typing import Union

from django.db.migrations.autodetector import MigrationAutodetector
from django.db.migrations.operations.base import Operation


class ModelContentChangeOperation(Operation):
    option_name = "model_content_change"

    @cached_property
    def model_name_lower(self):
        return self.model_name.lower()


class AddRecords(ModelContentChangeOperation):
    pass


class RemoveRecords(ModelContentChangeOperation):
    pass


class UpdateRecords(ModelContentChangeOperation):
    pass


_MigrationAutodetectorMixin = Union[MigrationAutodetector, 'MigrationAutodetectorMixin']


class MigrationAutodetectorMixin:

    def _detect_changes(self: _MigrationAutodetectorMixin, *args, **kwargs):
        self.static_objects_operations = {}
        return super()._detect_changes(*args, **kwargs)
