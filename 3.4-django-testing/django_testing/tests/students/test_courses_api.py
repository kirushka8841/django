import pytest
from rest_framework.test import APIClient
from students.models import Course, Student
from model_bakery import baker
from rest_framework.reverse import reverse


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def student(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return student


@pytest.fixture
def course_factory():
    def course(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return course


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity = 5)
    
    # Act
    url = reverse('courses-detail', args=(courses[0].id,))
    response = client.get(url)

    # Assert
    data = response.json()
    assert response.status_code == 200
    assert courses[0].id == data.get('id')
    


@pytest.mark.django_db
def test_get_list_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity = 5)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_list_courses_id(client, course_factory):
    # Arrange
    courses = course_factory(_quantity = 5)
    id = courses[0].id

    # Act
    response = client.get(f'/api/v1/courses/?id={id}')

    # Assert
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['id'] == id


@pytest.mark.django_db
def test_filter_list_courses_name(client, course_factory):
    # Arrange
    courses = course_factory(_quantity = 5)
    name = courses[0].name

    # Act
    response = client.get(f'/api/v1/courses/?name={name}')

    # Assert
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == name


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    # Act
    response = client.post('/api/v1/courses/', data={'name': 'Python с нуля'})

    # Assert
    data = response.json()
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert data['name'] == 'Python с нуля'


@pytest.mark.django_db
def test_upgrade_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity = 5)
    new_course = {'name': 'Java'}
    id = courses[0].id

    # Act
    response = client.patch(f'/api/v1/courses/{id}/', data=new_course)

    # Assert
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == new_course['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity = 5)
    id = courses[0].id

    # Act
    response = client.delete(f'/api/v1/courses/{id}/')

    # Assert
    # data = response.json()
    assert response.status_code == 204
    