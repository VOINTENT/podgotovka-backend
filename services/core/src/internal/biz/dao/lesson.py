import datetime
from typing import Optional, List

from sqlalchemy import select, and_, func, Column, case, text
from sqlalchemy.sql import Select

from src.internal.biz.creators.biz.document import DocumentCreator
from src.internal.biz.entities.biz.document import Document
from src.internal.biz.entities.enum.homework_type import HomeworkTypeEnum
from src.internal.biz.entities.enum.order import OrderEnum
from src.schema.meta import lesson_table, course_table, subject_table, lesson_view_table, lesson_file_table, \
    subject_course_subscription_table, homework_table, homework_test_table, test_question_table
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

    async def get_detail_with_files_with_homework_info(self, lesson_id: int, account_student_id: Optional[int]) -> Optional[Lesson]:
        lesson: Lesson = await self.get_detail_with_homework_info(lesson_id, account_student_id)
        if not lesson:
            return None
        documents: List[Document] = await self.get_documents_by_lesson_id(lesson_id)
        lesson.documents = documents
        return lesson

    async def get_detail_with_homework_info(self, lesson_id: int, account_student_id: Optional[int]) -> Optional[Lesson]:
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
        ]).select_from(
            lesson_table.join(
                subject_course_subscription_table, onclause=and_(
                    lesson_table.c.course_id == subject_course_subscription_table.c.course_id,
                    lesson_table.c.subject_id == subject_course_subscription_table.c.subject_id,
                    subject_course_subscription_table.c.account_student_id == account_student_id), isouter=True
            ).join(
                homework_table, isouter=True
            )
        ).where(
            lesson_table.c.id == lesson_id
        )

        row = await self.fetchone(query)
        if not row:
            return None
        return LessonCreator.get_from_record(row)

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
