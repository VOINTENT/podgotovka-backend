import datetime
import json
from typing import Optional, List

from src.internal.biz.dao.homework.homework import HomeworkDao
from sqlalchemy import select, and_, func, Column, case, text, null
from sqlalchemy.sql import Select
from src.internal.biz.creators.biz.document import DocumentCreator
from src.internal.biz.entities.biz.document import Document
from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.internal.biz.entities.enum.lesson_status import LessonStatusEnum
from src.internal.biz.entities.enum.order import OrderEnum
from src.schema.meta import lesson_table, course_table, subject_table, lesson_view_table, lesson_file_table, \
    subject_course_subscription_table, homework_table, homework_test_table, test_question_table, subject_course_table
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.lesson import Lesson
from src.internal.biz.creators.biz.lesson import LessonCreator


class LessonDao(BaseDao):
    async def delete(self, lesson_id: int) -> None:
        query = lesson_table.delete(). \
            where(lesson_table.c.id == lesson_id)

        await self.execute(query)

    async def exist(self, lesson_id: int) -> Optional[int]:
        query = select([True]).select_from(lesson_table).where(lesson_table.c.id == lesson_id)

        exist = await self.fetchval(query)
        return bool(exist)

    async def get(self, lesson_id: int) -> Optional[Lesson]:
        query = select(
            self.__class__._get_simple_select_columns()
        ).select_from(
            lesson_table.outerjoin(subject_table).outerjoin(course_table).outerjoin(lesson_file_table)
        ).where(and_(
            lesson_table.c.id == lesson_id
        ))

        row = await self.fetchone(query)
        if not row:
            return None
        return LessonCreator().get_from_record(row)

    async def get_with_files(self, lesson_id: int) -> Optional[Lesson]:
        lesson = await self.get(lesson_id)
        documents: List[Document] = await self.get_documents_by_lesson_id(lesson_id)
        lesson.documents = documents
        return lesson

    async def add(self, lesson: Lesson) -> Lesson:
        query = lesson_table.insert().values(
            account_teacher_id=lesson.account_teacher_id,
            status=lesson.status
        ).returning(
            lesson_table.c.id.label('lesson_id')
        )
        row = await self.fetchone(query)
        return LessonCreator().get_from_record(row)

    async def delete_homework_deep(self, lesson_id: int) -> None:
        async with self._connection as conn:
            homework_dao = HomeworkDao(conn)
            homework_id = await homework_dao.exist(lesson_id)

            if not homework_id:
                return

            await homework_dao.delete_deep(homework_id)

    async def update(self, lesson_id: int, lesson: Lesson) -> Lesson:
        query = lesson_table.update().values(
            name=lesson.name,
            description=lesson.description,
            youtube_link=lesson.youtube_link,
            time_start=lesson.datetime_start,
            time_finish=lesson.time_finish,
            text=json.loads(lesson.lecture) if lesson.lecture else null(),
            subject_id=lesson.subject.id if lesson.subject else None,
            course_id=lesson.course.id if lesson.course else None
        ).where(
            lesson_table.c.id == lesson_id)

        await self.execute(query)

        return lesson

    async def get_published_lessons(
            self, limit: int, offset: int, date_start: Optional[datetime.datetime], order: Optional[OrderEnum],
            course_id: Optional[int], subject_id: Optional[int], date_finish: Optional[datetime.datetime],
            account_student_id: Optional[int] = None):
        query = select([
            *self.__class__._get_columns_id_name(),
            lesson_table.c.created_at.label('lesson_created_at'),
            course_table.c.id.label('course_id'), course_table.c.name.label('course_name'),
            subject_table.c.id.label('subject_id'), subject_table.c.name.label('subject_name'),
            lesson_table.c.time_start.label('lesson_datetime_start'),
            lesson_table.c.time_finish.label('lesson_time_finish'),
            lesson_view_table.c.id.isnot(None).label('lesson_is_watched')
        ]).select_from(
            lesson_table.join(course_table).join(subject_table).join(
                lesson_view_table, isouter=True, onclause=and_(
                    lesson_table.c.id == lesson_view_table.c.lesson_id,
                    lesson_view_table.c.account_student_id == account_student_id
                )
            )
        )

        query = self.__class__._add_is_published_condition(query)
        query = self.__class__._add_conditions(
            query, date_start=date_start, date_finish=date_finish, course_id=course_id, subject_id=subject_id)
        query = self.__class__._add_pagination(query, limit, offset)
        query = self.__class__._add_order(query, order)

        rows = await self.fetchall(query)
        return LessonCreator.get_from_record_many(rows)

    async def get_published_lessons_by_teacher(
            self, account_teacher_id: int, limit: int, offset: int, date_start: Optional[datetime.datetime],
            date_finish: Optional[datetime.datetime], order: Optional[OrderEnum], course_id: Optional[int],
            subject_id: Optional[int]) -> List[Lesson]:
        query = select([
            *self.__class__._get_columns_id_name(),
            lesson_table.c.created_at.label('lesson_created_at'),
            course_table.c.id.label('course_id'), course_table.c.name.label('course_name'),
            subject_table.c.id.label('subject_id'), subject_table.c.name.label('subject_name'),
            lesson_table.c.time_start.label('lesson_datetime_start'),
            lesson_table.c.time_finish.label('lesson_time_finish')
        ]).select_from(
            lesson_table.join(course_table).join(subject_table)
        )

        query = self.__class__._add_is_published_condition(query)
        query = self.__class__._add_conditions(
            query, date_start=date_start, date_finish=date_finish, course_id=course_id, subject_id=subject_id,
            account_teacher_id=account_teacher_id)
        query = self.__class__._add_pagination(query, limit, offset)
        query = self.__class__._add_order(query, order)

        rows = await self.fetchall(query)

        return LessonCreator.get_from_record_many(rows)

    async def get_count_last(self, max_datetime: datetime.datetime, account_teacher_id: Optional[int] = None,
                             course_id: Optional[int] = None, subject_id: Optional[int] = None) -> int:
        query = select([func.count(lesson_table.c.id)]).select_from(lesson_table). \
            where(lesson_table.c.created_at < max_datetime)

        query = self.__class__._add_conditions(query, account_teacher_id=account_teacher_id, course_id=course_id,
                                               subject_id=subject_id)
        return await self.fetchval(query)

    async def get_count_next(self, min_datetime: datetime.datetime, account_teacher_id: Optional[int] = None,
                             course_id: Optional[int] = None, subject_id: Optional[int] = None) -> int:
        query = select([func.count(lesson_table.c.id)]).select_from(lesson_table).where(
            lesson_table.c.created_at > min_datetime)

        query = self.__class__._add_conditions(query, account_teacher_id=account_teacher_id, course_id=course_id,
                                               subject_id=subject_id)

        return await self.fetchval(query)

    async def get_detail_with_files_with_homework_info(self, lesson_id: int,
                                                       account_student_id: Optional[int]) -> Optional[Lesson]:
        lesson: Lesson = await self.get_detail_with_homework_info(lesson_id, account_student_id)
        if not lesson:
            return None
        documents: List[Document] = await self.get_documents_by_lesson_id(lesson_id)
        lesson.documents = documents
        return lesson

    async def get_detail_with_homework_info(self, lesson_id: int,
                                            account_student_id: Optional[int]) -> Optional[Lesson]:
        query = select([
            *self.__class__._get_columns_id_name(),
            lesson_table.c.description.label('lesson_description'),
            lesson_table.c.text.label('lesson_lecture'),
            subject_course_subscription_table.c.id.isnot(None).label('lesson_is_subscribed'),

            homework_table.c.id.label('homework_id'),
            select([account_student_id is not None]).as_scalar().label('homework_is_available'),
            homework_table.c.homework_type.label('homework_type'),
            case([
                (homework_table.c.homework_type == HomeworkTypeEnum.test,
                 self.__class__._get_select_count_questions(homework_table.c.id).as_scalar())
            ], else_=text('0')).label('homework_count_questions'),
            select([0]).as_scalar().label('homework_count_right_answers'),
        ]). \
            select_from(self.__class__._add_select_from_joined(account_student_id)). \
            where(lesson_table.c.id == lesson_id)

        row = await self.fetchone(query)
        if not row:
            return None
        return LessonCreator.get_from_record(row)

    async def get_documents_by_lesson_id(self, lesson_id) -> List[Document]:
        query = select([
            lesson_file_table.c.name.label('lesson_document_name'),
            lesson_file_table.c.file_link.label('lesson_document_file_link')
        ]).select_from(
            lesson_file_table
        ).where(
            lesson_file_table.c.lesson_id == lesson_id
        )

        rows = await self.fetchall(query)
        return DocumentCreator.get_many_from_record(rows)

    async def get_owner_account_teacher_id(self, lesson_id) -> Optional[int]:
        query = select([lesson_table.c.account_teacher_id]).select_from(
            lesson_table).where(lesson_table.c.id == lesson_id)

        account_teacher_id = await self.fetchval(query)
        return account_teacher_id

    async def update_status(self, lesson_id: int, status: LessonStatusEnum) -> None:
        query = lesson_table.update().values(status=status).where(lesson_table.c.id == lesson_id)
        await self.execute(query)

    @staticmethod
    def _add_select_from_joined(account_student_id: int) -> Select:
        return lesson_table. \
            outerjoin(subject_course_subscription_table,
                      subject_course_subscription_table.c.account_student_id == account_student_id). \
            outerjoin(subject_course_table,
                      and_(subject_course_table.c.id == subject_course_subscription_table.c.subject_course_id,
                           subject_course_table.c.subject_id == lesson_table.c.subject_id,
                           subject_course_table.c.course_id == lesson_table.c.course_id)). \
            outerjoin(homework_table)

    @staticmethod
    def _get_select_count_questions(homework_id: int) -> Select:
        return select([
            func.count(homework_table.c.id)
        ]).select_from(
            homework_table.join(homework_test_table.join(test_question_table))
        ).where(
            homework_table.c.id == homework_id
        )

    @staticmethod
    def _get_columns_id_name() -> List[Column]:
        return [lesson_table.c.id.label('lesson_id'), lesson_table.c.name.label('lesson_name')]

    @classmethod
    def _get_simple_select_columns(cls) -> List[Column]:
        return [
            *cls._get_columns_id_name(),
            lesson_table.c.description.label('lesson_description'),
            lesson_table.c.status.label('lesson_status'),
            lesson_table.c.youtube_link.label('lesson_youtube_link'),
            lesson_table.c.time_start.label('lesson_datetime_start'),
            lesson_table.c.time_finish.label('lesson_time_finish'),
            lesson_table.c.text.label('lesson_lecture'),
            lesson_table.c.subject_id.label('subject_id'),
            lesson_table.c.course_id.label('course_id'),
            lesson_table.c.account_teacher_id.label('account_teacher_id'),

            subject_table.c.name.label('subject_name'),
            course_table.c.name.label('course_name')
        ]

    @staticmethod
    def _get_joined_for_select():
        return lesson_table.outerjoin(subject_table).outerjoin(course_table)

    @staticmethod
    def _add_is_published_condition(query: Select) -> Select:
        return query.where(lesson_table.c.status == LessonStatusEnum.published)

    @staticmethod
    def _add_pagination(query: Select, limit: int, offset: int) -> Select:
        return query.limit(limit).offset(offset)

    @staticmethod
    def _add_conditions(query: Select, date_start: Optional[datetime.datetime] = None,
                        date_finish: Optional[datetime.datetime] = None, course_id: Optional[int] = None,
                        subject_id: Optional[int] = None, account_teacher_id: Optional[int] = None) -> Select:
        if date_start:
            query = query.where(lesson_table.c.time_start >= date_start)

        if date_finish:
            query = query.where(lesson_table.c.time_start <= date_finish)

        if course_id:
            query = query.where(lesson_table.c.course_id == course_id)

        if subject_id:
            query = query.where(lesson_table.c.subject_id == subject_id)

        if account_teacher_id:
            query = query.where(lesson_table.c.account_teacher_id == account_teacher_id)

        return query

    @staticmethod
    def _add_order(query: Select, order: Optional[OrderEnum] = None) -> Select:
        if order:
            if order.value == OrderEnum.asc:
                query = query.order_by(lesson_table.c.created_at)
            elif order.value == OrderEnum.desc:
                query = query.order_by(lesson_table.c.created_at)
            else:
                raise TypeError
        else:
            query = query.order_by(lesson_table.c.created_at)
        return query
