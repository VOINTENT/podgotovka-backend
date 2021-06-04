from typing import Optional

from sqlalchemy import select, func

from src.internal.biz.creators.biz.account_teacher import AccountTeacherCreator
from src.internal.biz.dao.base import BaseDao
from src.internal.biz.entities.biz.account.account import Account
from src.schema.meta import account_teacher_table


class TeacherAccountDao(BaseDao):
    async def add(self, obj):
        pass

    async def add_many(self, obj):
        pass

    async def get_by_id(self, id):
        pass

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
