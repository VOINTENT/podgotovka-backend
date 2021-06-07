from typing import Optional

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

    async def add_many(self, obj):
        pass

    async def get_by_id(self, id):
        pass

    async def get_all(self, limit: Optional[int] = 1_000_000, offset: Optional[int] = 0):
        pass

    async def update(self, id, obj):
        pass

    async def remove_by_id(self, id):
        pass