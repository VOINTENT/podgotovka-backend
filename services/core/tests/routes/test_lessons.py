import datetime

from starlette.testclient import TestClient

from tests.test_data import TestLessonData, TestLessonData2, TestLessonFileData, TestHomeworkData, TestLessonFileData2, \
    TestAccountTeacherData, TestSubjectData, TestCourseData
from tests.utils.asserts.db.lesson import assert_lesson_in_db
from tests.utils.asserts.models.lesson import assert_lesson_simple_list_with_counts_response, \
    assert_lesson_detail_for_student_response, assert_lesson_detail_for_edit_response
from tests.utils.db import run_query
from tests.utils.utils import get_auth_headers, get_random_json


def test_add_empty_lesson(client: TestClient, truncate, account_teacher, access_token_teacher):
    response = client.post('/core/v1/lessons/', json={},
                           headers=get_auth_headers(access_token_teacher))
    assert response.status_code == 200
    lessons = run_query("SELECT id, account_teacher_id FROM lesson WHERE account_teacher_id=$1",
                        TestAccountTeacherData.id)
    assert lessons[0][1] == TestAccountTeacherData.id


def test_get_lessons(client: TestClient, truncate, account_teacher, courses, subjects, homework, lesson,
                     lesson2):
    response = client.get('/core/v1/lessons/')
    assert response.status_code == 200, response.text

    result = response.json()
    assert len(result['lessons']) == 2
    assert_lesson_simple_list_with_counts_response(
        result, count_last=0, count_next=0, lessons=[TestLessonData, TestLessonData2]
    )


def test_get_lessons_filters(client: TestClient, truncate, account_teacher, courses, subjects, homework,
                             lesson, lesson2):
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


def test_get_lessons_order(client: TestClient, truncate, account_teacher, courses, subjects, homework,
                           lesson, lesson2):
    response = client.get(f'/core/v1/lessons?order=desc')
    assert response.status_code == 200
    assert len(response.json()['lessons']) == 2
    assert response.json()['lessons'][0]['id'] == TestLessonData.id
    assert response.json()['lessons'][1]['id'] == TestLessonData2.id


def test_get_lessons_pagination(client: TestClient, truncate, account_teacher, courses, subjects, homework,
                                lesson, lesson2):
    response = client.get(f'/core/v1/lessons?limit=1&skip=1')
    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json['lessons']) == 1
    assert response_json['count_last'] == 1
    assert response_json['count_next'] == 0


def test_get_lesson_detail(client: TestClient, truncate, access_token_teacher, courses,
                           subjects, homework, lesson):
    response = client.get(f'/core/v1/lessons/{TestLessonData.id}/students')
    assert response.status_code == 200

    response_json = response.json()
    assert_lesson_detail_for_student_response(
        response_json, id=TestLessonData.id, name=TestLessonData.name, description=TestLessonData.description,
        files=[[TestLessonFileData.name, TestLessonFileData.file_link],
               [TestLessonFileData2.name, TestLessonFileData2.file_link]], lecture=TestLessonData.text,
        is_subscribed=False, homework_id=TestHomeworkData.id, homework_is_available=False,
        homework_type=TestHomeworkData.homework_type, homework_count_questions=2, homework_count_right_answers=0)


def test_get_lesson_detail_without_homework(client: TestClient, truncate, access_token_teacher,
                                            courses, subjects, lesson2):
    response = client.get(f'/core/v1/lessons/{TestLessonData2.id}/students')
    assert response.status_code == 200
    assert response.json()['homework'] is None


def test_update_lesson_set_empty(client: TestClient, truncate, access_token_teacher, courses,
                                 subjects, lesson2):
    response = client.patch(f'/core/v1/lessons/{TestLessonData2.id}', json={
        'subject_id': -1,
        'course_id': -1,
        'name': '',
        'description': '',
        'youtube_link': '',
        'time_start': -1,
        'time_finish': -1,
        'files': [],
        'lecture': ''
    }, headers=get_auth_headers(access_token_teacher))
    assert response.status_code == 200

    assert_lesson_in_db(
        subject_id=None, course_id=None, name=None, description=None, youtube_link=None, time_start=None,
        time_finish=None, files=[], lecture=None)


def test_update_lesson(client: TestClient, truncate, access_token_teacher, courses,
                       subjects, lesson2):
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.time()
    new_lecture = get_random_json()
    response = client.patch(f'/core/v1/lessons/{TestLessonData2.id}', json={
        'subject_id': TestSubjectData.id,
        'course_id': TestCourseData.id,
        'name': 'qwsdasd',
        'description': 'fsdfwef',
        'youtube_link': 'ghhfbcv',
        'time_start': int(current_datetime.timestamp()),
        'time_finish': current_time.hour * 3600 + current_time.minute * 60,
        'files': [],
        'lecture': new_lecture
    }, headers=get_auth_headers(access_token_teacher))
    assert response.status_code == 200

    assert_lesson_in_db(
        subject_id=TestSubjectData.id, course_id=TestCourseData.id, name='qwsdasd', description='fsdfwef',
        youtube_link='ghhfbcv', time_start=current_datetime,
        time_finish=current_time, files=[], lecture=new_lecture)


def test_update_lesson_do_nothing(client: TestClient, truncate, access_token_teacher, courses,
                                  subjects, lesson2):
    response = client.patch(f'/core/v1/lessons/{TestLessonData2.id}', json={},
                            headers=get_auth_headers(access_token_teacher))
    assert response.status_code == 200

    assert_lesson_in_db(
        subject_id=TestLessonData2.subject.id, course_id=TestLessonData2.course.id, name=TestLessonData2.name,
        description=TestLessonData2.description, youtube_link=TestLessonData2.youtube_link,
        time_start=TestLessonData2.time_start,
        time_finish=TestLessonData2.time_finish, files=[], lecture=TestLessonData2.text)


def test_get_my_teacher_lessons(client: TestClient, truncate, access_token_teacher, courses,
                                subjects, homework, lesson, lesson2):
    response = client.get(f'/core/v1/lessons/my/teachers', headers=get_auth_headers(access_token_teacher))
    assert response.status_code == 200

    response_json = response.json()
    assert_lesson_simple_list_with_counts_response(
        response_json, count_last=0, count_next=0, lessons=[TestLessonData, TestLessonData2]
    )


def test_get_lesson_detail_for_edit(client: TestClient, truncate, access_token_teacher, courses, subjects,
                                    lesson2):
    response = client.get(f'/core/v1/lessons/{TestLessonData2.id}/teachers/for-edit',
                          headers=get_auth_headers(access_token_teacher))
    assert response.status_code == 200

    response_json = response.json()
    assert_lesson_detail_for_edit_response(
        response_json, id=TestLessonData2.id, subject={
            'id': TestLessonData2.subject.id, 'name': TestLessonData2.subject.name
        }, course={'id': TestLessonData2.course.id, 'name': TestLessonData2.course.name}, name=TestLessonData2.name,
        description=TestLessonData2.description, youtube_link=TestLessonData2.youtube_link,
        time_start=TestLessonData2.time_start, time_finish=TestLessonData2.time_finish, files=[],
        lecture=TestLessonData2.text, status='published'
    )
