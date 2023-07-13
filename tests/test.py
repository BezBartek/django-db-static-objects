import pytest
from django.core.management import call_command

from tests.decorators import roll_back_schema

pytestmark = pytest.mark.django_db


@pytest.mark.django_db(transaction=True)
@roll_back_schema
def test_migrations(temp_migrations_dir, BasedOnListOfTuples):
    assert not (temp_migrations_dir / "0001_initial.py").exists()
    call_command("makemigrations", "test_app")
    assert (temp_migrations_dir / "0001_initial.py").exists()
    file_content = (temp_migrations_dir / "0001_initial.py").read()
