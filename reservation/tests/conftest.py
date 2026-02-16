import os
import django

import shutil
from django.conf import settings
import pytest


def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()


@pytest.fixture(autouse=True)
def media_clean():
    yield
    # После каждого теста удаляем медиа-файлы
    if settings.MEDIA_ROOT.exists():
        shutil.rmtree(settings.MEDIA_ROOT)
