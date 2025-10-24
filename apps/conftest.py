import pytest
from rest_framework.test import APIClient
from apps.users.models.user_model import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
@pytest.mark.django_db
def superuser():
    return User.objects.create_superuser(
        email='root@example.com',
        password='Pass@123',
        username='Root',
    )