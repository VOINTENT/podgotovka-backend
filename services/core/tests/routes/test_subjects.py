from starlette.testclient import TestClient

from tests.test_data import TestSubjectData, TestSubjectData2, TestCourseData
from tests.utils.asserts.subject import assert_simple_subject_response


def test_get_all_subjects(client: TestClient, truncate, subjects):
    response = client.get('/core/v1/subjects')
    assert response.status_code == 200

    result = response.json()
    assert len(result) == 2

    assert_simple_subject_response(result[0], id=TestSubjectData.id, name=TestSubjectData.name)
    assert_simple_subject_response(result[1], id=TestSubjectData2.id, name=TestSubjectData2.name)


def test_get_all_subjects_filter_course(client: TestClient, truncate, structures, subjects, courses, subject_course):
    response = client.get(f'/core/v1/subjects?course_id={TestCourseData.id}')
    assert response.status_code == 200

    result = response.json()
    assert len(result) == 1

    assert_simple_subject_response(result[0], id=TestSubjectData.id, name=TestSubjectData.name)
