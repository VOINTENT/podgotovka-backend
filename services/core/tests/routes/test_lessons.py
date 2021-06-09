from starlette.testclient import TestClient

from tests.test_data import TestLessonData, TestLessonData2
from tests.utils.asserts.lesson import assert_lesson_simple_list_with_counts_response


def test_get_lessons(client: TestClient, truncate, teacher_account, structures, courses, subjects, lesson, lesson2):
    response = client.get('/core/v1/lessons')
    assert response.status_code == 200

    result = response.json()
    assert len(result['lessons']) == 2
    assert_lesson_simple_list_with_counts_response(
        result, count_last=0, count_next=0,  lessons=[TestLessonData, TestLessonData2]
    )


def test_get_lessons_filters(client: TestClient, truncate, teacher_account, structures, courses, subjects, lesson, lesson2):
    date_start = round(TestLessonData2.time_start.timestamp())
    response = client.get(f'/core/v1/lessons?date_start={date_start}')
    assert response.status_code == 200
    assert len(response.json()['lessons']) == 1
    assert response.json()['lessons'][0]['id'] == TestLessonData2.id

    response = client.get(f'/core/v1/lessons?subject_id={TestLessonData2.subject.id}')
    assert response.status_code == 200
    assert len(response.json()['lessons']) == 1
    assert response.json()['lessons'][0]['id'] == TestLessonData2.id

    response = client.get(f'/core/v1/lessons?course_id={TestLessonData2.course.id}')
    assert response.status_code == 200
    assert len(response.json()['lessons']) == 1
    assert response.json()['lessons'][0]['id'] == TestLessonData2.id


def test_get_lessons_order(client: TestClient, truncate, teacher_account, structures, courses, subjects, lesson, lesson2):
    response = client.get(f'/core/v1/lessons?order=desc')
    assert response.status_code == 200
    assert len(response.json()['lessons']) == 2
    assert response.json()['lessons'][0]['id'] == TestLessonData.id
    assert response.json()['lessons'][1]['id'] == TestLessonData2.id


def test_get_lessons_pagination(client: TestClient, truncate, teacher_account, structures, courses, subjects, lesson, lesson2):
    response = client.get(f'/core/v1/lessons?limit=1&skip=1')
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json['lessons']) == 1
    assert response_json['count_last'] == 1
    assert response_json['count_next'] == 0
