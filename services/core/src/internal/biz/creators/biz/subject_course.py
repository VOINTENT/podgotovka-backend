from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.subject_course import SubjectCourse


class SubjectCourseCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        name = f"{record.get('subject_name')} ({record.get('course_name')})"
        return SubjectCourse(
            name=name,
            course_id=record.get('course_id'),
            subject_id=record.get('subject_id'),
        )
