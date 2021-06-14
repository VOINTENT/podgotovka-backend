from starlette.testclient import TestClient

from tests.test_data import TestSubjectData, TestSubjectData2, TestCourseData, TestSubjectCourseData3, TestCourseData2, \
    TestLessonData, TestLessonData2
from tests.utils.asserts.models.subject import assert_subject_simple_response, assert_subject_course_simple_response
from tests.utils.utils import get_auth_headers


def test_get_all_subjects(client: TestClient, truncate, subjects):
    response = client.get('/core/v1/subjects')
    assert response.status_code == 200

    result = response.json()
    assert len(result) == 2

    assert_subject_simple_response(result[0], id=TestSubjectData.id, name=TestSubjectData.name)
    assert_subject_simple_response(result[1], id=TestSubjectData2.id, name=TestSubjectData2.name)


def test_get_all_subjects_filter_course(client: TestClient, truncate, subjects, courses, subject_course):
    response = client.get(f'/core/v1/subjects?course_id={TestCourseData.id}')
    assert response.status_code == 200

    result = response.json()
    assert len(result) == 1

    assert_subject_simple_response(result[0], id=TestSubjectData.id, name=TestSubjectData.name)


def test_get_teacher_lead(client: TestClient, truncate, subjects, courses, subject_course_with_id,
                          access_token_teacher, subject_course_lead):
    response = client.get(f'/core/v1/subjects/my/teachers/lead',
                          headers=get_auth_headers(access_token_teacher))

    assert response.status_code == 200

    result = response.json()

    assert len(result) == 2
    assert_subject_course_simple_response(result[0], name='%s (%s)' % (TestSubjectData.name, TestCourseData.name),
                                          subject_id=TestSubjectData.id, course_id=TestCourseData.id)
    assert_subject_course_simple_response(result[1], name='%s (%s)' % (TestSubjectData2.name, TestCourseData.name),
                                          subject_id=TestSubjectData2.id, course_id=TestCourseData.id)


def test_get_teacher_lead_filter(client: TestClient, truncate, subjects, courses, subject_course_with_id,
                                 access_token_teacher, subject_course_lead, lesson2):
    response = client.get(f'/core/v1/subjects/my/teachers/lead?search=%s' % (TestLessonData2.name.lower()[:5]),
                          headers=get_auth_headers(access_token_teacher))
    assert response.status_code == 200

    result = response.json()
    assert len(result) == 1
    assert_subject_course_simple_response(result[0], name='%s (%s)' % (TestSubjectData2.name, TestCourseData.name),
                                          subject_id=TestSubjectData2.id, course_id=TestCourseData.id)


def test_get_student_subscribed(client: TestClient, truncate, subjects, courses, subject_course_with_id,
                                access_token_student, subject_course_subscribed):
    response = client.get(f'/core/v1/subjects/my/students/subscribed',
                          headers=get_auth_headers(access_token_student))

    assert response.status_code == 200

    result = response.json()

    assert len(result) == 2
    assert_subject_course_simple_response(result[0], name='%s (%s)' % (TestSubjectData.name, TestCourseData.name),
                                          subject_id=TestSubjectData.id, course_id=TestCourseData.id)
    assert_subject_course_simple_response(result[1], name='%s (%s)' % (TestSubjectData2.name, TestCourseData.name),
                                          subject_id=TestSubjectData2.id, course_id=TestCourseData.id)


def test_get_my_teacher_subjects(client: TestClient, truncate, access_token_teacher, subjects, courses,
                                 subject_course_with_id, subject_course_lead):
    response = client.get('/core/v1/subjects/my/teachers', headers=get_auth_headers(access_token_teacher))
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json) == 2
    assert_subject_simple_response(response_json[0], id=TestSubjectData.id, name=TestSubjectData.name)
    assert_subject_simple_response(response_json[1], id=TestSubjectData2.id, name=TestSubjectData2.name)
