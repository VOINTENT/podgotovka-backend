from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.course import Course


class CourseCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record) -> Course:
        return Course(
            id=record.get('course_id'),
            name=record.get('course_name')
        )
