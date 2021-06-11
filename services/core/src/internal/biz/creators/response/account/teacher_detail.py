from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher

from src.internal.biz.entities.response.account.teacher_detail import AccountTeacherDetailResponse


class AccountTeacherDetailResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, account_teacher: AccountTeacher) -> AccountTeacherDetailResponse:
        return AccountTeacherDetailResponse(
            id=account_teacher.id,
            email=account_teacher.email,
            name=account_teacher.name,
            last_name=account_teacher.last_name,
            middle_name=account_teacher.middle_name,
            photo_link=account_teacher.photo.short_url,
            description=account_teacher.description,
        )

    @classmethod
    def get_from_many(cls, account_teachers: List[AccountTeacher]) -> List[AccountTeacherDetailResponse]:
        return [cls.get_from_one(teacher) for teacher in account_teachers]
