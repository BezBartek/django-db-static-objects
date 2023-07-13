from django.conf import settings
from .dynamic_models_fixtures import *  # noqa
from .fixtures import temp_migrations_dir  # noqa


pytest_plugins = ()


def pytest_configure():
    """Configure a django settings"""
    sqlite = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_db_static_objects'
    }

    settings.configure(
        DATABASES={
            "default": sqlite,
        },
        INSTALLED_APPS=[
            "django_db_static_objects",
            "tests.test_app"
        ]
    )
