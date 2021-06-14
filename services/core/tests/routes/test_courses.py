from starlette.testclient import TestClient

from tests.test_data import TestSubjectData, TestCourseData, TestCourseData2
from tests.utils.asserts.models.course import assert_course_simple_response
from tests.utils.utils import get_auth_headers


def test_get_all_courses(client: TestClient, truncate, courses):
    response = client.get('/core/v1/courses')
    assert response.status_code == 200

    result = response.json()
    assert len(result) == 2

    assert_course_simple_response(result[0], id=TestCourseData.id, name=TestCourseData.name)
    assert_course_simple_response(result[1], id=TestCourseData2.id, name=TestCourseData2.name)


def test_get_all_subjects_filter_course(client: TestClient, truncate, subjects, courses, subject_course):
    response = client.get(f'/core/v1/courses?subject_id={TestSubjectData.id}')
    assert response.status_code == 200

    result = response.json()
    assert len(result) == 1

    assert_course_simple_response(result[0], id=TestCourseData.id, name=TestCourseData.name)


def test_get_my_teacher_courses(client: TestClient, truncate, subjects, courses, access_token_teacher,
                                subject_course_with_id, subject_course_lead):
    response = client.get('/core/v1/courses/my/teachers', headers=get_auth_headers(access_token_teacher))
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json) == 1
    assert_course_simple_response(response_json[0], id=TestCourseData.id, name=TestCourseData.name)
