import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


"""
проверка получения 1го курса (retrieve-логика)
    создаем курс через фабрику
    строим урл и делаем запрос через тестовый клиент
    проверяем, что вернулся именно тот курс, который запрашивали
"""


@pytest.mark.django_db
def test_get_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=1)

    temp_id = courses[Course.objects.count()-1].id
    temp_url = '/api/v1/courses/' + f'{temp_id}' + '/'

    # Act
    response = client.get(temp_url)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert temp_id == data['id']


"""
проверка получения списка курсов (list-логика)
    аналогично – сначала вызываем фабрики, затем делаем запрос и проверяем результат
"""


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


"""
проверка фильтрации списка курсов по id
    создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
"""


@pytest.mark.django_db
def test_filter_by_id(client, course_factory):
    count = Course.objects.count()
    courses = course_factory(_quantity=1, name='TestText')
    temp_id = courses[count-1].id
    temp_url = '/api/v1/courses/?id=' + f'{temp_id}'

    # Act
    response = client.get(temp_url)
    data = response.json()
    assert response.status_code == 200
    for m in data:
        assert m['id'] == temp_id


"""
проверка фильтрации списка курсов по name
"""


@pytest.mark.django_db
def test_filter_by_name(client):

    response = client.get('/api/v1/courses/?name=TestText')
    data = response.json()
    assert response.status_code == 200
    for m in data:
        assert m['name'] == 'TestText'


"""
тест успешного создания курса
    здесь фабрика не нужна, готовим JSON-данные и создаем курс
"""


@pytest.mark.django_db
def test_create_json_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'test text json create'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


"""
тест успешного обновления курса
    сначала через фабрику создаем, потом обновляем JSON-данным...
"""


@pytest.mark.django_db
def test_update_course(client, course_factory):

    count = Course.objects.count()
    courses = course_factory(_quantity=1)
    assert Course.objects.count() == count + 1

    temp_id = courses[count].id
    temp_url = '/api/v1/courses/' + f'{temp_id}' + '/'
    response = client.put(temp_url, data={'name': 'test json update'})

    assert response.status_code == 200


"""
тест успешного удаления курса
"""


@pytest.mark.django_db
def test_delete_course(client, course_factory):

    count = Course.objects.count()
    courses = course_factory(_quantity=1)
    assert Course.objects.count() == count + 1

    temp_id = courses[count].id
    temp_url = '/api/v1/courses/' + f'{temp_id}' + '/'
    response = client.delete(temp_url)

    assert response.status_code == 204
