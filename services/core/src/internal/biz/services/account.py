from src.internal.biz.creators.biz.token import TokenCreator
from src.internal.biz.dao.teacher import TeacherAccountDao
from src.internal.biz.entities.biz.account.account import Account
from src.internal.biz.entities.biz.account.token import Token
from src.internal.servers.http.exceptions.account import AccountsExceptionEnum


class AccountTeacherService:
    @staticmethod
    async def auth_account_base(account: Account) -> Token:
        existed_account = await TeacherAccountDao().get_by_email(account.email)
        if not existed_account or not existed_account.is_password_valid(account.password):
            raise AccountsExceptionEnum.WRONG_EMAIL_OR_PASSWORD

        token = TokenCreator().get_from_account(existed_account)
        token.create_auth_token()
        return token
