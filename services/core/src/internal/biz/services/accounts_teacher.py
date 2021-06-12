from typing import Optional

from src.internal.biz.creators.biz.token import TokenCreator
from src.internal.biz.dao.teacher import AccountTeacherDao
from src.internal.biz.entities.biz.account.account import Account
from src.internal.biz.entities.biz.account.account_teacher import AccountTeacher
from src.internal.biz.entities.biz.account.token import Token
from src.internal.servers.http.exceptions.account import AccountsExceptionEnum


class AccountsTeacherService:
    @staticmethod
    async def auth_account_base(account: Account) -> Token:
        existed_account = await AccountTeacherDao().get_by_email(account.email)
        if not existed_account or not existed_account.is_password_valid(account.password):
            raise AccountsExceptionEnum.WRONG_EMAIL_OR_PASSWORD

        token = TokenCreator().get_from_account(existed_account)
        token.create_auth_token()
        return token

    @staticmethod
    async def get_by_id_simple(account_teacher_id: int) -> Optional[AccountTeacher]:
        return await AccountTeacherDao().get_by_id(account_teacher_id)

    @staticmethod
    async def get_by_id_detail(account_teacher_id: int) -> AccountTeacher:
        return await AccountTeacherDao().get_detail_by_id(account_teacher_id)
