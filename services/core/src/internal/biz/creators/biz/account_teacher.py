from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.biz.photo import Photo


class AccountTeacherCreator(CreatorBiz):
    @staticmethod
    def get_from_record(record: Record):
        photo = Photo(short_url=record.get('account_photo_link')) if 'account_photo_link' in record else None
        return AccountTeacher(
            id=record.get('account_teacher_id'),
            hash_password=record.get('account_hash_password'),
            email=record.get('account_email'),
            name=record.get('account_name'),
            last_name=record.get('account_last_name'),
            middle_name=record.get('account_middle_name'),
            description=record.get('account_description'),
            photo=photo,
        )

    def get_from_record_many(self, records: List[Record]):
        super().get_from_record_many(records)
