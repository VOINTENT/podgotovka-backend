from typing import List

from sqlalchemy import select

from src.internal.biz.creators.biz.course import CourseCreator
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.course import Course
from src.schema.meta import course_table, subject_course_table, subject_course_lead_table


class CourseDao(BaseDao):
    async def get_all_courses(self, limit: int, offset: int, subject_id: int) -> List[Course]:
        query = select([course_table.c.id.label('course_id'), course_table.c.name.label('course_name')]).select_from(
            course_table.join(subject_course_table, isouter=True)).limit(limit).offset(offset).order_by(
            course_table.c.created_at)

        if subject_id:
            query = query.where(subject_course_table.c.subject_id == subject_id)

        rows = await self.fetchall(query)
        return CourseCreator.get_from_record_many(rows)

    async def get_teacher_courses(self, limit: int, offset: int, subject_id: int, account_teacher_id: int
                                  ) -> List[Course]:
        query = select([
            course_table.c.id.label('course_id'),
            course_table.c.name.label('course_name')
        ]).select_from(
            course_table.join(subject_course_table.join(subject_course_lead_table))
        ).where(
            subject_course_lead_table.c.account_teacher_id == account_teacher_id
        ).group_by(
            course_table.c.id,
            course_table.c.name
        ).order_by(
            course_table.c.created_at
        )

        if subject_id:
            query = query.where(subject_course_table.c.subject_id == subject_id)

        query = self.__class__._add_pagination(query, limit=limit, offset=offset)

        rows = await self.fetchall(query)
        return CourseCreator.get_from_record_many(rows)
