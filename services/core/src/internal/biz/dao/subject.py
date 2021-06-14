from typing import Optional, List, Any

from sqlalchemy import select, and_, func
from sqlalchemy.sql import Select

from src.internal.biz.creators.biz.subject import SubjectCreator
from src.internal.biz.creators.biz.subject_course import SubjectCourseCreator
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.subject import Subject
from src.schema.meta import subject_table, subject_course_table, course_table, \
    subject_course_lead_table, subject_course_subscription_table, lesson_table


class SubjectDao(BaseDao):
    async def get_all_subjects(self, limit: int = 1_000_000, offset: int = 0, course_id: Optional[int] = None):
        query = select(self.__class__._get_simple_fields()).select_from(
            subject_table.join(subject_course_table, isouter=True)).group_by(
            *self.__class__._get_simple_fields()).order_by(subject_table.c.created_at)

        if course_id:
            query = query.where(subject_course_table.c.course_id == course_id)

        query = self.__class__._add_pagination(query, limit, offset)

        rows = await self.fetchall(query)
        return SubjectCreator.get_from_record_many(rows)

    async def get_teacher_lead(self, limit: int, offset: int, account_teacher_id: int, lesson_search: Optional[str]):
        query = select(
            self.__class__._get_select_subject_course()
        ).select_from(
            subject_course_lead_table.join(
                subject_course_table
            ).join(
                subject_table
            ).join(
                course_table
            ).outerjoin(
                lesson_table, onclause=and_(subject_course_table.c.subject_id == lesson_table.c.subject_id,
                                            subject_course_table.c.course_id == lesson_table.c.course_id)
            )
        ).where(
            subject_course_lead_table.c.account_teacher_id == account_teacher_id
        ).group_by(
            course_table.c.id, subject_table.c.id
        ).order_by(
            subject_table.c.created_at
        )

        if lesson_search:
            query = query.where(lesson_table.c.name.ilike(f'%{lesson_search}%'))

        query = self.__class__._add_pagination(query, limit, offset)

        rows = await self.fetchall(query)

        return SubjectCourseCreator.get_from_record_many(rows)

    async def get_student_subscribed(self, limit: int, offset: int, account_student_id: int):
        select_from = self.__class__._add_select_from_with_join_subscribed()
        select_from = self.__class__._add_join_subject_course(select_from)

        query = select(
            self.__class__._get_select_subject_course()
        ).select_from(
            select_from
        ).where(
            subject_course_subscription_table.c.account_student_id == account_student_id
        ).group_by(
            course_table.c.id, subject_table.c.id, subject_table.c.name, course_table.c.id
        ).order_by(subject_table.c.created_at)
        query = self.__class__._add_pagination(query, limit, offset)

        rows = await self.fetchall(query)

        return SubjectCourseCreator.get_from_record_many(rows)

    async def get_teacher_subjects(self, limit: int, offset: int, account_teacher_id: int, course_id: Optional[int]
                                   ) -> List[Subject]:
        query = select([
            subject_table.c.id.label('subject_id'),
            subject_table.c.name.label('subject_name')
        ]).select_from(
            subject_table.join(subject_course_table.join(subject_course_lead_table))
        ).where(
            subject_course_lead_table.c.account_teacher_id == account_teacher_id
        ).group_by(
            subject_table.c.id,
            subject_table.c.name
        ).order_by(subject_table.c.created_at)

        if course_id:
            query = query.where(subject_course_table.c.course_id == course_id)

        query = self.__class__._add_pagination(query, limit=limit, offset=offset)

        rows = await self.fetchall(query)
        return SubjectCreator.get_from_record_many(rows)

    @staticmethod
    def _get_simple_fields() -> List[Any]:
        return [subject_table.c.id.label('subject_id'), subject_table.c.name.label('subject_name')]

    @staticmethod
    def _add_select_from_with_join_lead() -> Select:
        return subject_course_lead_table.join(subject_course_table, subject_course_table.c.id == subject_course_lead_table.c.subject_course_id)

    @staticmethod
    def _add_select_from_with_join_subscribed() -> Select:
        return subject_course_subscription_table. \
            join(subject_course_table,
                 subject_course_table.c.id == subject_course_subscription_table.c.subject_course_id)

    @staticmethod
    def _add_join_subject_course(query: Select) -> Select:
        return query. \
            join(subject_table, subject_table.c.id == subject_course_table.c.subject_id). \
            join(course_table, course_table.c.id == subject_course_table.c.course_id)

    @staticmethod
    def _get_select_subject_course() -> List[Any]:
        return [
            subject_table.c.name.label('subject_name'),
            course_table.c.name.label('course_name'),
            subject_table.c.id.label('subject_id'),
            course_table.c.id.label('course_id'),
        ]
