from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher


class AccountTeacherCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        return AccountTeacher(
            id=record.get('account_teacher_id'),
            hash_password=record.get('account_hash_password'),
            email=record.get('account_email')
        )

    def get_from_record_many(self, records: List[Record]):
        super().get_from_record_many(records)
