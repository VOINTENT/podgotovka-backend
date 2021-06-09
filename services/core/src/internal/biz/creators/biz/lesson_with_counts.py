from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.lessons_with_counts import LessonsWithCounts


class LessonWithCountsCreator(Creator):
    @staticmethod
    def get_from_args(lessons: List[Lesson], count_last: int, count_next: int) -> LessonsWithCounts:
        return LessonsWithCounts(lessons=lessons, count_last=count_last, count_next=count_next)
