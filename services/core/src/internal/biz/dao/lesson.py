import datetime
from typing import Optional

from src.internal.biz.entities.enum.order import OrderEnum
from src.schema.meta import lesson_table
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.creators.biz.lesson import LessonCreator


class LessonDao(BaseDao):
    async def add(self, account_teacher_id: int) -> Lesson:
        query = lesson_table.insert(). \
            values(account_teacher_id=account_teacher_id). \
            returning(lesson_table.c.id.label('lesson_id'))
        row = await self.fetchone(query)
        return LessonCreator().get_from_record(row)

    async def get_all_lessons(self, limit: int, offset: int, date_start: datetime.datetime, order: OrderEnum,
                              course_id: int, subject_id: int):
        pass
