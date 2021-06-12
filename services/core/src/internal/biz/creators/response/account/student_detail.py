from typing import List

from src.internal.biz.creators.base import Creator
from src.internal.biz.entities.biz.account.account_student import AccountStudent

from src.internal.biz.entities.response.account.student_detail import AccountStudentDetailResponse


class AccountStudentDetailResponseCreator(Creator):
    @classmethod
    def get_from_one(cls, account_student: AccountStudent) -> AccountStudentDetailResponse:
        return AccountStudentDetailResponse(
            id=account_student.id,
            email=account_student.email,
            name=account_student.name,
            last_name=account_student.last_name,
            middle_name=account_student.middle_name,
            photo_link=account_student.photo.short_url,
            description=account_student.description,
            vk_id=account_student.vk_id
        )

    @classmethod
    def get_from_many(cls, account_students: List[AccountStudent]) -> List[AccountStudentDetailResponse]:
        return [cls.get_from_one(student) for student in account_students]
