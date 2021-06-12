from typing import List

from asyncpg import Record

from src.internal.biz.creators.biz.base import CreatorBiz
from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.internal.biz.entities.biz.photo import Photo
from src.internal.biz.entities.request.account.student.add import AccountStudentAddRequest


class AccountStudentCreator(CreatorBiz):
    def get_from_record(self, record: Record):
        photo = Photo(short_url=record.get('account_photo_link')) if 'account_photo_link' in record else None
        return AccountStudent(
            id=record.get('account_student_id'),
            hash_password=record.get('account_hash_password'),
            email=record.get('account_email'),
            name=record.get('account_name'),
            last_name=record.get('account_last_name'),
            middle_name=record.get('account_middle_name'),
            description=record.get('account_description'),
            photo=photo,
            vk_id=record.get('account_student_vk_id'),
        )

    def get_from_record_many(self, records: List[Record]):
        super().get_from_record_many(records)

    @staticmethod
    def get_from_request(account_student: AccountStudentAddRequest) -> AccountStudent:
        return AccountStudent(name=account_student.name,
                              last_name=account_student.last_name,
                              middle_name=account_student.middle_name,
                              description=account_student.description,
                              photo=Photo(optional_url=account_student.photo_link),
                              email=account_student.email,
                              password=account_student.password,
                              )

    @staticmethod
    def get_from_vk_response(vk_response: dict, email: str) -> AccountStudent:
        photo = Photo(optional_url=vk_response['photo_max_orig'])
        photo.create_short_link_from_optional()
        return AccountStudent(name=vk_response['first_name'],
                              last_name=vk_response['last_name'],
                              email=email,
                              photo=photo,
                              vk_id=vk_response['id'])
