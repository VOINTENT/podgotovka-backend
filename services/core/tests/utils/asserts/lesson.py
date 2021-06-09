import datetime
from typing import Dict, Any, List, Type

from tests.test_data import TestLessonData, TestCourseData, TestSubjectData
from tests.utils.asserts.course import assert_course_simple_response
from tests.utils.asserts.subject import assert_subject_simple_response


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
