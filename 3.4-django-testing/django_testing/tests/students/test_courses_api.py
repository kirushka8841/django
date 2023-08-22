import pytest
from rest_framework.test import APIClient
from students.models import Course
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_courses():
    client = APIClient()
    Course.objects.create(name='pidor')
    User.objects.create_user('admin')
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
