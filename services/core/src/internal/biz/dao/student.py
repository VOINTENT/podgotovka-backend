from typing import Optional

from sqlalchemy import func, select

from src.internal.biz.creators.biz.account_student import AccountStudentCreator
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.schema.meta import account_student_table


class AccountStudentDao(BaseDao):
    async def get_by_id(self, account_student_id: int) -> Optional[AccountStudent]:
        query = select([
            account_student_table.c.id.label('account_student_id'),
            account_student_table.c.hash_password.label('account_hash_password'),
            account_student_table.c.email.label('account_email')
        ]).select_from(account_student_table). \
            where(account_student_table.c.id == account_student_id)

        row = await self.fetchone(query)
        if not row:
            return None
        return AccountStudentCreator().get_from_record(row)

    async def add(self, account_student: AccountStudent) -> AccountStudent:
        query = account_student_table.insert(). \
            values(email=account_student.email,
                   name=account_student.name,
                   last_name=account_student.last_name,
                   middle_name=account_student.middle_name,
                   photo_link=account_student.photo.short_url,
                   description=account_student.description,
                   hash_password=account_student.hash_password,
                   vk_id=account_student.vk_id,
                   ). \
            returning(account_student_table.c.id.label('account_student_id'),
                      account_student_table.c.hash_password.label('account_hash_password'),
                      account_student_table.c.email.label('account_email'),
                      )
        row = await self.fetchone(query)

        return AccountStudentCreator().get_from_record(row)

    async def get_by_email(self, email: str) -> Optional[AccountStudent]:
        query = select([
            account_student_table.c.id.label('account_student_id'),
            account_student_table.c.hash_password.label('account_hash_password'),
            account_student_table.c.email.label('account_email'),
        ]). \
            select_from(account_student_table). \
            where(func.lower(account_student_table.c.email) == email.lower())

        row = await self.fetchone(query)
        if not row:
            return None
        return AccountStudentCreator().get_from_record(row)

    async def get_by_vk_id(self, vk_id: int) -> Optional[AccountStudent]:
        query = select([
            account_student_table.c.id.label('account_student_id'),
            account_student_table.c.email.label('account_email'),
            account_student_table.c.vk_id.label('account_student_vk_id'),
        ]). \
            select_from(account_student_table). \
            where(account_student_table.c.vk_id == vk_id)

        row = await self.fetchone(query)
        if not row:
            return None
        return AccountStudentCreator().get_from_record(row)
