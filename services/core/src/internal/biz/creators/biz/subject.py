from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.subject import Subject


class SubjectCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        return Subject(
            id=record.get('subject_id'),
            name=record.get('subject_name')
        )

    @staticmethod
    def get_from_request(subject_id: int) -> Subject:
        return Subject(id=subject_id)
