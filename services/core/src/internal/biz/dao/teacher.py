from typing import Optional, List, Any

from sqlalchemy import select, func

from src.internal.biz.creators.biz.account_teacher import AccountTeacherCreator
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.account.account import Account
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.schema.meta import account_teacher_table


class AccountTeacherDao(BaseDao):
    async def add(self, obj):
        pass

    async def add_many(self, obj):
        pass

    async def get_detail_by_id(self, account_teacher_id: int) -> Optional[AccountTeacher]:
        query = select(self.__class__._get_select_detail()). \
            where(account_teacher_table.c.id == account_teacher_id)

        row = await self.fetchone(query)

        if not row:
            return None

        return AccountTeacherCreator().get_from_record(row)

    async def get_by_id(self, id):
        query = select([
            account_teacher_table.c.id.label('account_teacher_id'),
            account_teacher_table.c.hash_password.label('account_hash_password'),
            account_teacher_table.c.email.label('account_email')
        ]).select_from(account_teacher_table). \
            where(account_teacher_table.c.id == id)

        row = await self.fetchone(query)
        if not row:
            return None
        return AccountTeacherCreator().get_from_record(row)

    async def get_all(self, limit: Optional[int] = 1_000_000, offset: Optional[int] = 0):
        pass

    async def update(self, id, obj):
        pass

    async def remove_by_id(self, id):
        pass

    async def get_by_email(self, email: str) -> Optional[Account]:
        query = select([
            account_teacher_table.c.id.label('account_teacher_id'),
            account_teacher_table.c.hash_password.label('account_hash_password'),
            account_teacher_table.c.email.label('account_email')
        ]).select_from(account_teacher_table).where(func.lower(account_teacher_table.c.email) == email.lower())

        row = await self.fetchone(query)
        if not row:
            return None
        return AccountTeacherCreator().get_from_record(row)

    @staticmethod
    def _get_select_detail() -> List[Any]:
        return [
            account_teacher_table.c.id.label('account_teacher_id'),
            account_teacher_table.c.email.label('account_email'),
            account_teacher_table.c.name.label('account_name'),
            account_teacher_table.c.last_name.label('account_last_name'),
            account_teacher_table.c.middle_name.label('account_middle_name'),
            account_teacher_table.c.description.label('account_description'),
            account_teacher_table.c.photo_link.label('account_photo_link'),
            account_teacher_table.c.hash_password.label('account_hash_password'),
        ]
