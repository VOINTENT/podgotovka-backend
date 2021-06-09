import datetime
from typing import Optional

from sqlalchemy import select

from src.internal.biz.entities.enum.order import OrderEnum
from src.schema.meta import lesson_table, course_table, subject_table
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
        query = select([lesson_table.c.id, lesson_table.c.name, course_table.c.id, course_table.c.name, subject_table.c.id, subject_table.c.name, lesson_table.time_start, lesson_table.c.time_finish, ]).select_from(lesson_table.join(course_table).join(subject_table)).limit(limit).offset(offset)

        if date_start:
            query = query.where(lesson_table.c.time_start == date_start)

        if course_id:
            query = query.where(lesson_table.c.course_id == course_id)

        if subject_id:
            query = query.where(lesson_table.c.subject_id == subject_id)

        if order:
            if order.value == OrderEnum.asc:
                query = query.order_by(lesson_table.c.created_at)
            elif order.value == OrderEnum.desc:
                query = query.order_by(lesson_table.c.created_at)
            else:
                raise TypeError
        else:
            query = query.order_by(lesson_table.c.created_at)

        rows = await self.fetchall(query)
        return LessonCreator.get_from_record_many(rows)
