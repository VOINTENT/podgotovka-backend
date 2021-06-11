from src.internal.biz.creators.biz.account_student import AccountStudentCreator
from src.internal.biz.creators.biz.token import TokenCreator
from src.internal.biz.dao.student import AccountStudentDao
from src.internal.biz.entities.biz.account.account import Account
from src.internal.biz.entities.biz.account.account_student import AccountStudent
from src.internal.biz.entities.biz.account.token import Token
from src.internal.drivers.vk_driver import VKApiDriver
from src.internal.servers.http.exceptions.account import AccountsExceptionEnum


class AccountsStudentService:
    @staticmethod
    async def get_by_id_simple(account_student_id: int) -> AccountStudent:
        pass

    @staticmethod
    async def register_account(account_student: AccountStudent) -> Token:
        account_student = await AccountStudentDao().add(account_student)
        token = TokenCreator().get_from_account(account_student)
        token.create_auth_token()
        return token

    @staticmethod
    async def auth_account_base(account: Account) -> Token:
        existed_account = await AccountStudentDao().get_by_email(account.email)
        if not existed_account or not existed_account.is_password_valid(account.password):
            raise AccountsExceptionEnum.WRONG_EMAIL_OR_PASSWORD

        token = TokenCreator().get_from_account(existed_account)
        token.create_auth_token()
        return token

    @staticmethod
    async def auth_or_register_by_vk(vk_temp_code: str) -> Token:
        err, vk_access_token, email, deactivated = await VKApiDriver.get_vk_access_token(vk_temp_code)

        if err:
            raise AccountsExceptionEnum.INVALID_VK_CODE
        if deactivated:
            raise AccountsExceptionEnum.INVALID_VK_STATUS

        vk_user_info_response = await VKApiDriver.get_user_info(vk_access_token)

        account_student = AccountStudentCreator.get_from_vk_response(vk_user_info_response, email)

        existed_account = await AccountStudentDao().get_by_vk_id(account_student.vk_id)

        if not existed_account:
            existed_account = await AccountStudentDao().add(account_student)
        token = TokenCreator().get_from_account(existed_account)
        token.create_auth_token()
        return token
