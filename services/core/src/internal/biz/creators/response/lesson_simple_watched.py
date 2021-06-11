from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.creators.response.lesson_simple import LessonSimpleResponseCreator
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.response.lesson.simple import LessonSimpleResponse
from src.internal.biz.entities.response.lesson.simple_watched import LessonSimpleWatchedResponse


class LessonSimpleWatchedResponseCreator(Creator):
    @classmethod
    def get_many_from_lessons(cls, lessons: List[Lesson]) -> List[LessonSimpleResponse]:
        return [cls.get_from_lesson(lesson) for lesson in lessons]

    @staticmethod
    def get_from_lesson(lesson: Lesson) -> LessonSimpleWatchedResponse:
        lesson_simple_response = LessonSimpleResponseCreator.get_from_lesson(lesson)
        return LessonSimpleWatchedResponse(
            **lesson_simple_response.dict(),
            is_watched=lesson.is_watched
        )
