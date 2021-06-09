import datetime
from typing import Optional, List

from sqlalchemy import select, and_, func, Column

from src.internal.biz.entities.enum.order import OrderEnum
from src.schema.meta import lesson_table, course_table, subject_table, lesson_view_table, lesson_file_table, \
    subject_course_subscription_table
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

    async def get_published_lessons(self, limit: int, offset: int, date_start: datetime.datetime, order: OrderEnum,
                                    course_id: int, subject_id: int, account_student_id: Optional[int] = None):
        query = select([
            *self.__class__._get_columns_id_name(),
            lesson_table.c.created_at.label('lesson_created_at'),
            course_table.c.id.label('course_id'), course_table.c.name.label('course_name'),
            subject_table.c.id.label('subject_id'), subject_table.c.name.label('subject_name'),
            lesson_table.c.time_start.label('lesson_time_start'),
            lesson_table.c.time_finish.label('lesson_time_finish'),
            lesson_view_table.c.id.isnot(None).label('lesson_is_watched')
        ]).select_from(
            lesson_table.join(course_table).join(subject_table).join(
                lesson_view_table, isouter=True, onclause=and_(
                    lesson_table.c.id == lesson_view_table.c.lesson_id,
                    lesson_view_table.c.account_student_id == account_student_id
                )
            )
        ).where(
            lesson_table.c.is_published.is_(True)
        ).limit(limit).offset(offset)

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

    async def get_count_last(self, max_datetime: datetime.datetime) -> int:
        query = select([func.count(lesson_table.c.id)]).select_from(lesson_table).where(
            lesson_table.c.created_at < max_datetime)

        return await self.fetchval(query)

    async def get_count_next(self, min_datetime: datetime.datetime) -> int:
        query = select([func.count(lesson_table.c.id)]).select_from(lesson_table).where(
            lesson_table.c.created_at > min_datetime)

        return await self.fetchval(query)

    async def get_detail_with_homework_info(self, lesson_id: int, account_student_id: Optional[int]) -> Lesson:
        query = select([
            *self.__class__._get_columns_id_name(),
            lesson_table.c.description.label('lesson_description'),
            lesson_table.c.lecture.label('lesson_lecture'),
            func.array_agg(lesson_file_table.c.file_link),
            subject_course_subscription_table.c.id.isnot(None).label('lesson_is_subscribed')
        ]).select_from(lesson_table.join(lesson_file_table, isouter=True).join(
            subject_course_subscription_table, onclause=and_(lesson_table.c.course_id == subject_course_subscription_table.c.course_id, lesson_table.c.subject_id == subject_course_subscription_table.c.subject_id, subject_course_subscription_table.c.account_student_id), isouter=True))

    @staticmethod
    def _get_columns_id_name() -> List[Column]:
        return [lesson_table.c.id.label('lesson_id'), lesson_table.c.name.label('lesson_name')]
