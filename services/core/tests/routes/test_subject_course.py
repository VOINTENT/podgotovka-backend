from starlette.testclient import TestClient

from tests.test_data import TestSubjectCourseData3, TestSubjectCourseData2
from tests.utils.asserts.models.subject_course import assert_subject_course_simple_response
from tests.utils.utils import get_auth_headers


def test_get_teacher_lead(client: TestClient, truncate, subjects, courses, subject_course_with_id,
                          account_teacher, subject_course_lead, access_token_teacher):
    response = client.get(f'/core/v1/subjects/my/teachers/lead',
                          headers=get_auth_headers(access_token_teacher))

    assert response.status_code == 200

    result = response.json()

    assert len(result) == 2
    for res in result:
        assert '(' in res['name']
        assert ')' in res['name']


def test_get_student_subscribed(client: TestClient, truncate, subjects, courses, subject_course_with_id,
                                account_student, subject_course_subscribed, access_token_student):
    response = client.get(f'/core/v1/subjects/my/students/subscribed',
                          headers=get_auth_headers(access_token_student))

    assert response.status_code == 200

    result = response.json()

    assert len(result) == 2
    for res in result:
        assert '(' in res['name']
        assert ')' in res['name']
