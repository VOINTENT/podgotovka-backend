from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.response.lesson.only_name import LessonOnlyNameResponse


class LessonOnlyNameResponseCreator(Creator):
    @classmethod
    def get_many_from_lessons(cls, lessons: List[Lesson]) -> List[LessonOnlyNameResponse]:
        return [cls.get_from_lesson(lesson) for lesson in lessons]

    @staticmethod
    def get_from_lesson(lesson: Lesson) -> LessonOnlyNameResponse:
        return LessonOnlyNameResponse(
            id=lesson.id,
            name=lesson.name
        )
