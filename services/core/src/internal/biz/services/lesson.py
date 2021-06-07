import datetime
from typing import List

from src.internal.biz.dao.lesson import LessonDao
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.entities.enum.order import OrderEnum


class LessonService:
    @staticmethod
    async def create_empty_lesson(account_teacher_id: int) -> Lesson:
        return await LessonDao().add(account_teacher_id)

    @staticmethod
    async def get_all_lessons_with_counts(limit: int, skip: int, date_start: datetime.datetime, order: OrderEnum,
                                          course_id: int, subject_id: int):
        lessons: List[Lesson] = await LessonDao().get_all_lessons(
            limit=limit, offset=skip, date_start=date_start, order=order, course_id=course_id, subject_id=subject_id)

        if lessons:
            count_last = await LessonDao().get_count_last(lessons[0].created_at)
            count_next = await LessonDao().get_count_next(lessons[-1].created_at)
        else:
            count_last = 0
            count_next = 0

        return LessonWithCountsCreator.get_from_agrs(lessons=lessons, count_last=count_last, count_next=count_next)
