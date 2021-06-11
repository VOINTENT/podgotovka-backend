from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.course_simple import CourseSimpleResponseCreator
from src.internal.biz.creators.response.subject_simple import SubjectSimpleResponseCreator
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.response.lesson.simple import LessonSimpleResponse


class LessonSimpleResponseCreator(Creator):
    @classmethod
    def get_many_from_lessons(cls, lessons: List[Lesson]) -> List[LessonSimpleResponse]:
        return [cls.get_from_lesson(lesson) for lesson in lessons]

    @staticmethod
    def get_from_lesson(lesson: Lesson) -> LessonSimpleResponse:
        return LessonSimpleResponse(
            id=lesson.id,
            name=lesson.name,
            course=CourseSimpleResponseCreator.get_from_course(lesson.course),
            subject=SubjectSimpleResponseCreator.get_from_subject(lesson.subject),
            start_time=int(lesson.datetime_start.timestamp()),
            finish_time=lesson.finish_time_in_seconds,
        )
