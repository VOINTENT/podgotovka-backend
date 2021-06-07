from typing import Optional, List, Any

from sqlalchemy import select
from sqlalchemy.sql import Select

from src.internal.biz.creators.biz.subject import SubjectCreator
from src.internal.biz.dao.base import BaseDao
from src.schema.meta import subject_table, subject_course_table


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

    @staticmethod
    def _get_simple_fields() -> List[Any]:
        return [subject_table.c.id.label('subject_id'), subject_table.c.name.label('subject_name')]

    @staticmethod
    def _add_pagination(query: Select, limit: int = 1_000_000, offset: int = 0) -> Select:
        return query.limit(limit).offset(offset)
