from starlette.testclient import TestClient

from tests.test_data import TestSubjectData, TestCourseData, TestCourseData2
from tests.utils.asserts.course import assert_simple_course_response


def test_get_all_courses(client: TestClient, truncate, structures, courses):
    response = client.get('/core/v1/courses')
    assert response.status_code == 200

    result = response.json()
    assert len(result) == 2

    assert_simple_course_response(result[0], id=TestCourseData.id, name=TestCourseData.name)
    assert_simple_course_response(result[1], id=TestCourseData2.id, name=TestCourseData2.name)


def test_get_all_subjects_filter_course(client: TestClient, truncate, structures, subjects, courses, subject_course):
    response = client.get(f'/core/v1/courses?subject_id={TestSubjectData.id}')
    assert response.status_code == 200

    result = response.json()
    assert len(result) == 1

    assert_simple_course_response(result[0], id=TestCourseData.id, name=TestCourseData.name)
