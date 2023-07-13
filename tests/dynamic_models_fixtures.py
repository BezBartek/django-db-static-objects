import pytest
from django.db import models

from tests.test_app.models import BasedOnListOfTuplesTemplate, BasedOnListOfDictsTemplate


def get_declared_class_attributes(cls) -> dict:
  return {key: value for key, value in cls.__dict__.items() if not key.startswith('__')}


def define_model(template_class, parent):
    attributes = get_declared_class_attributes(template_class)
    attrs = {
        **attributes,
        '__module__': 'tests.test_app.models'
    }
    return type(template_class.__name__.replace("Template", ""), (parent,), attrs)


@pytest.fixture
def BasedOnListOfTuples():  # noqa
    return define_model(BasedOnListOfTuplesTemplate, models.Model)


@pytest.fixture()
def BasedOnListOfDicts():  # noqa
    return define_model(BasedOnListOfDictsTemplate, models.Model)

