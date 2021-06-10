import datetime
from typing import Dict, Any, List, Type

from tests.test_data import TestLessonData, TestCourseData, TestSubjectData
from tests.utils.asserts.models.course import assert_course_simple_response
from tests.utils.asserts.models.homework import assert_homework_info_response
from tests.utils.asserts.models.lesson_file import assert_file_simple_response
from tests.utils.asserts.models.subject import assert_subject_simple_response
from tests.utils.asserts.utils import assert_json


def assert_lesson_simple_list_with_counts_response(response: Dict[str, Any], count_last: int, count_next: int,
                                                   lessons: [List[Type[TestLessonData]]]):
    assert response['count_last'] == count_last
    assert response['count_next'] == count_next
    for response_lesson, lesson in zip(response['lessons'], lessons):
        assert_lesson_simple_response(
            response_lesson, id=lesson.id, name=lesson.name, course=lesson.course, subject=lesson.subject,
            start_time=lesson.time_start, finish_time=lesson.time_finish, is_watched=lesson.is_watched)


def assert_lesson_simple_response(response: Dict[str, Any], id: int, name: str, course: Type[TestCourseData],
                                  subject: Type[TestSubjectData], start_time: datetime.datetime,
                                  finish_time: datetime.time, is_watched: bool):
    assert response['id'] == id
    assert response['name'] == name
    assert_course_simple_response(response['course'], id=course.id, name=course.name)
    assert_subject_simple_response(response['subject'], id=subject.id, name=subject.name)
    assert response['start_time'] == round(start_time.timestamp())
    assert response['finish_time'] == finish_time.hour * 3600 + finish_time.minute * 60
    assert response['is_watched'] is is_watched


def assert_lesson_detail_for_student_response(
        response: Dict[str, Any], id: int, name: str, description: str, files: List[List[Any]],
        lecture: str, is_subscribed: bool, homework_id: int, homework_is_available: bool, homework_type: str,
        homework_count_questions: int, homework_count_right_answers: int):

    assert response['id'] == id
    assert response['name'] == name
    assert response['description'] == description
    for file_simple_response, file in zip(response['files'], files):
        assert_file_simple_response(file_simple_response, name=file[0], file_link=file[1])

    assert_homework_info_response(
        response['homework'], id=homework_id, is_available=homework_is_available, type=homework_type,
        count_questions=homework_count_questions, count_right_answers=homework_count_right_answers)

    assert_json(response['lecture'], lecture)
    assert response['is_subscribed'] is is_subscribed
